#!/usr/bin/env python3
"""Validate GitHub raw chat_bridge latest-result consistency."""

from __future__ import annotations

import argparse
import csv
import json
import time
import urllib.error
import urllib.request
from pathlib import Path


RAW_FILES = [
    "chat_bridge/00_README_FIRST.md",
    "chat_bridge/02_LATEST_CODEX_RESULT.json",
    "chat_bridge/08_CODEX_FEEDBACK_TO_CHATGPT.md",
    "chat_bridge/09_SYNC_STATUS.tsv",
]


def fetch(url: str) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "User-Agent": "acor-chat-bridge-validator/1.0",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def read_tsv_text(text: str) -> dict[str, tuple[str, str]]:
    rows: dict[str, tuple[str, str]] = {}
    for row in csv.DictReader(text.splitlines(), delimiter="\t"):
        rows[row.get("item", "")] = (row.get("status", ""), row.get("details", ""))
    return rows


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["check_item", "status", "details"], delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def add(rows: list[dict[str, str]], item: str, ok: bool, details: str) -> None:
    rows.append({"check_item": item, "status": "pass" if ok else "fail", "details": details})


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expected-result", required=True)
    parser.add_argument("--expected-label", required=True)
    parser.add_argument("--raw-base", default="https://raw.githubusercontent.com/Jarvis5272/caor-chat-bridge/main")
    parser.add_argument("--out", default="chat_bridge/BRIDGE_RAW_VALIDATION.tsv")
    parser.add_argument("--allow-raw-pending", action="store_true")
    parser.add_argument("--retries", type=int, default=5)
    parser.add_argument("--retry-sleep", type=float, default=3.0)
    args = parser.parse_args()

    expected_result = args.expected_result.rstrip("/")
    expected_label = args.expected_label
    last_rows: list[dict[str, str]] = []
    for attempt in range(1, max(1, args.retries) + 1):
        rows: list[dict[str, str]] = []
        contents: dict[str, str] = {}
        add(rows, "attempt", True, str(attempt))
        try:
            for name in RAW_FILES:
                url = f"{args.raw_base.rstrip('/')}/{name}"
                contents[name] = fetch(url)
                add(rows, f"download_{name}", True, url)
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            add(rows, "raw_validation_status", False, f"failed_network_or_404: {exc}")
            last_rows = rows
            if attempt < args.retries:
                time.sleep(args.retry_sleep)
                continue
            write_tsv(Path(args.out), rows)
            print(f"raw bridge validation: failed_network_or_404 ({exc})")
            return 0 if args.allow_raw_pending else 1

        readme = contents["chat_bridge/00_README_FIRST.md"]
        feedback = contents["chat_bridge/08_CODEX_FEEDBACK_TO_CHATGPT.md"]
        latest = json.loads(contents["chat_bridge/02_LATEST_CODEX_RESULT.json"])
        sync = read_tsv_text(contents["chat_bridge/09_SYNC_STATUS.tsv"])

        add(rows, "raw_json_final_label", latest.get("final_label") == expected_label, str(latest.get("final_label", "missing")))
        add(rows, "raw_json_output_dir", latest.get("output_dir") == expected_result, str(latest.get("output_dir", "missing")))
        add(rows, "raw_readme_contains_expected_label", expected_label in readme, expected_label)
        add(rows, "raw_readme_contains_expected_result", expected_result in readme, expected_result)
        add(rows, "raw_feedback_contains_expected_label", expected_label in feedback, expected_label)
        add(rows, "raw_feedback_contains_expected_result", expected_result in feedback, expected_result)
        add(rows, "raw_sync_explicit_latest_result_used", sync.get("explicit_latest_result_used", ("", "")) == ("yes", "true"), str(sync.get("explicit_latest_result_used", ("missing", "missing"))))
        add(rows, "raw_sync_used_latest_result", sync.get("used_latest_result", ("", ""))[1] == expected_result, str(sync.get("used_latest_result", ("missing", "missing"))))
        add(rows, "raw_sync_auto_detect_disabled", sync.get("auto_detected", ("", "")) == ("no", "false"), str(sync.get("auto_detected", ("missing", "missing"))))
        add(rows, "raw_sync_latest_final_label", sync.get("latest_final_label", ("", ""))[1] == expected_label, str(sync.get("latest_final_label", ("missing", "missing"))))
        add(rows, "raw_sync_latest_output_dir", sync.get("latest_output_dir", ("", ""))[1] == expected_result, str(sync.get("latest_output_dir", ("missing", "missing"))))
        add(rows, "no_stale_previous_label_as_latest", latest.get("final_label") == expected_label and latest.get("output_dir") == expected_result, "latest JSON exact match")

        status = "pass" if all(row["status"] == "pass" for row in rows) else "fail"
        add(rows, "raw_validation_status", status == "pass", status)
        last_rows = rows
        if status == "pass":
            write_tsv(Path(args.out), rows)
            print(f"raw bridge validation: {status} ({expected_result} / {expected_label})")
            return 0
        if attempt < args.retries:
            time.sleep(args.retry_sleep)
    write_tsv(Path(args.out), last_rows)
    print(f"raw bridge validation: fail ({expected_result} / {expected_label})")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
