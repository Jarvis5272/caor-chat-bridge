#!/usr/bin/env python3
"""Validate local chat_bridge latest-result consistency."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


REQUIRED_BRIDGE_FILES = [
    "00_README_FIRST.md",
    "01_CURRENT_STATE_CN.md",
    "02_LATEST_CODEX_RESULT.json",
    "03_RUN_LEDGER.tsv",
    "04_ACTIVE_CLAIM_BOUNDARY_CN.md",
    "05_NEXT_ACTION_CN.md",
    "06_FILES_FOR_REVIEW.tsv",
    "07_LAST_CHATGPT_PROMPT_TO_CODEX.md",
    "08_CODEX_FEEDBACK_TO_CHATGPT.md",
    "09_SYNC_STATUS.tsv",
    "10_PROTECTED_AUDIT.tsv",
    "11_ORIGINAL_SOURCE_AUDIT.tsv",
    "12_OPEN_QUESTIONS_CN.md",
    "13_BRIDGE_USAGE_CN.md",
]


def read_tsv(path: Path) -> dict[str, tuple[str, str]]:
    rows: dict[str, tuple[str, str]] = {}
    if not path.exists():
        return rows
    with path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            rows[row.get("item", "")] = (row.get("status", ""), row.get("details", ""))
    return rows


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["check_item", "status", "details"], delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def add(rows: list[dict[str, str]], item: str, ok: bool, details: str) -> None:
    rows.append({"check_item": item, "status": "pass" if ok else "fail", "details": details})


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bridge", default="chat_bridge")
    parser.add_argument("--expected-result", required=True)
    parser.add_argument("--expected-label", required=True)
    args = parser.parse_args()

    bridge = Path(args.bridge)
    expected_result = args.expected_result.rstrip("/")
    expected_label = args.expected_label
    rows: list[dict[str, str]] = []

    readme_path = bridge / "00_README_FIRST.md"
    json_path = bridge / "02_LATEST_CODEX_RESULT.json"
    feedback_path = bridge / "08_CODEX_FEEDBACK_TO_CHATGPT.md"
    sync_path = bridge / "09_SYNC_STATUS.tsv"

    readme = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""
    feedback = feedback_path.read_text(encoding="utf-8") if feedback_path.exists() else ""
    latest = json.loads(json_path.read_text(encoding="utf-8")) if json_path.exists() else {}
    sync = read_tsv(sync_path)

    add(rows, "json_final_label", latest.get("final_label") == expected_label, str(latest.get("final_label", "missing")))
    add(rows, "json_output_dir", latest.get("output_dir") == expected_result, str(latest.get("output_dir", "missing")))
    add(rows, "readme_contains_expected_label", expected_label in readme, expected_label)
    add(rows, "readme_contains_expected_result", expected_result in readme, expected_result)
    add(rows, "feedback_contains_expected_label", expected_label in feedback, expected_label)
    add(rows, "feedback_contains_expected_result", expected_result in feedback, expected_result)

    explicit_status, explicit_details = sync.get("explicit_latest_result_used", ("missing", "missing"))
    used_status, used_details = sync.get("used_latest_result", ("missing", "missing"))
    auto_status, auto_details = sync.get("auto_detected", ("missing", "missing"))
    label_status, label_details = sync.get("latest_final_label", ("missing", "missing"))
    output_status, output_details = sync.get("latest_output_dir", ("missing", "missing"))
    add(rows, "sync_explicit_latest_result_used", explicit_status == "yes" and explicit_details == "true", f"{explicit_status}:{explicit_details}")
    add(rows, "sync_used_latest_result", used_details == expected_result, used_details)
    add(rows, "sync_auto_detect_disabled", auto_status == "no" and auto_details == "false", f"{auto_status}:{auto_details}")
    add(rows, "sync_latest_final_label", label_details == expected_label, label_details)
    add(rows, "sync_latest_output_dir", output_details == expected_result, output_details)

    present = [name for name in REQUIRED_BRIDGE_FILES if (bridge / name).exists()]
    add(rows, "required_bridge_files_present", len(present) == len(REQUIRED_BRIDGE_FILES), f"{len(present)}/{len(REQUIRED_BRIDGE_FILES)}")

    status = "pass" if all(row["status"] == "pass" for row in rows) else "fail"
    add(rows, "bridge_local_validation_status", status == "pass", status)
    write_tsv(bridge / "BRIDGE_LOCAL_VALIDATION.tsv", rows)
    print(f"local bridge validation: {status} ({expected_result} / {expected_label})")
    return 0 if status == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
