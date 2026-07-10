#!/usr/bin/env python3
"""Refresh the standalone chat_bridge_export mirror safely."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
from pathlib import Path


FORBIDDEN_SUFFIX = {".fastq", ".fq", ".fasta", ".fa", ".bam", ".sam", ".gz", ".npy", ".npz", ".pkl", ".chunk", ".chunks"}
EXPORT_SKIP_SUFFIX = {".png", ".jpg", ".jpeg", ".pdf", ".svg", ".html", ".pptx"}
MAX_BRIDGE_FILE_BYTES = 1024 * 1024
SECRET_RE = re.compile(r"(^|[/_.-])(secret|token|api[-_]?key|credential|password|passwd|id_rsa|id_dsa|id_ed25519|\.env)([/_.-]|$)", re.I)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bridge", default="chat_bridge")
    parser.add_argument("--package", default="chat_bridge_feedback_package.zip")
    parser.add_argument("--scripts", default="scripts/chat_bridge")
    parser.add_argument("--out", default="chat_bridge_export")
    return parser.parse_args()


def write_tsv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    args = parse_args()
    root = Path.cwd().resolve()
    bridge = (root / args.bridge).resolve()
    package = (root / args.package).resolve()
    scripts = (root / args.scripts).resolve()
    export = (root / args.out).resolve()
    export.mkdir(parents=True, exist_ok=True)

    for child in list(export.iterdir()):
        if child.name == ".git":
            continue
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()

    def ignore_bridge_files(src: str, names: list[str]) -> set[str]:
        ignored = {"__pycache__"}
        src_path = Path(src)
        for name in names:
            path = src_path / name
            if name.endswith(".pyc"):
                ignored.add(name)
            elif path.is_file() and (path.suffix.lower() in EXPORT_SKIP_SUFFIX or path.stat().st_size > MAX_BRIDGE_FILE_BYTES):
                ignored.add(name)
        return ignored

    shutil.copytree(bridge, export / "chat_bridge", ignore=ignore_bridge_files)
    shutil.copy2(package, export / package.name)
    (export / "scripts").mkdir(parents=True, exist_ok=True)
    shutil.copytree(scripts, export / "scripts" / "chat_bridge", ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))

    latest = json.loads((bridge / "02_LATEST_CODEX_RESULT.json").read_text(encoding="utf-8"))
    label = latest.get("final_label", "missing")
    latest_dir = latest.get("output_dir", "missing")
    claim = latest.get("claim_boundary", "missing")
    next_action = latest.get("next_action", "missing")

    (export / "README.md").write_text(
        f"""# ChatGPT-Codex Bridge Mirror

This is a safe standalone ChatGPT-Codex bridge mirror for the ACOR online reconstruction project.

It contains only project-state summary files and bridge scripts. It does not contain raw data, full results, original BBS source, protected code, or large per-read/per-prefix artifacts.

## Start Here

ChatGPT should first read:

`chat_bridge/00_README_FIRST.md`

## Current Latest Result

- latest result: `{latest_dir}`
- latest final label: `{label}`

## Claim Boundary

{claim}

## Next Action

{next_action}

## If Linking From GitHub

If this mirror is pushed to a public GitHub repository, give ChatGPT the raw link:

`https://raw.githubusercontent.com/<USER>/<REPO>/main/chat_bridge/00_README_FIRST.md`

## If Uploading Directly

Upload `chat_bridge_feedback_package.zip` and tell ChatGPT:

Please read this chat_bridge package and update project state from `00_README_FIRST.md`.
""",
        encoding="utf-8",
    )

    (export / "CHATGPT_LINK_INSTRUCTIONS_CN.md").write_text(
        """# ChatGPT Link Instructions

## If pushed to GitHub public repo

Give ChatGPT this raw URL pattern:

```text
https://raw.githubusercontent.com/<USER>/<REPO>/main/chat_bridge/00_README_FIRST.md
```

## If not pushed

Upload:

```text
chat_bridge_feedback_package.zip
```

Then tell ChatGPT:

```text
请读取这个 chat_bridge package，并基于 00_README_FIRST.md 更新项目状态。
```

## Important boundary

This bridge package is a project-state mirror only. It is not a benchmark result, not a new algorithm claim, and not a full repository/data export.
""",
        encoding="utf-8",
    )

    large: list[str] = []
    secret: list[str] = []
    raw: list[str] = []

    def iter_files():
        for path in sorted(export.rglob("*")):
            if path.is_file() and ".git" not in path.parts:
                yield path

    for path in iter_files():
        rel = path.relative_to(export).as_posix()
        if path.stat().st_size > 1024 * 1024:
            large.append(rel)
        if SECRET_RE.search(rel):
            secret.append(rel)
        if path.suffix.lower() in FORBIDDEN_SUFFIX:
            raw.append(rel)

    top = {p.name for p in export.iterdir() if p.name != ".git"}
    allowed_top = {"chat_bridge", "chat_bridge_feedback_package.zip", "scripts", "README.md", "EXPORT_MANIFEST.tsv", "EXPORT_SAFETY_AUDIT.tsv", "CHATGPT_LINK_INSTRUCTIONS_CN.md", "PUSH_STATUS.tsv"}
    audit = [
        {"check_item": "contains_data_dir", "status": "pass" if not (export / "data").exists() else "fail", "details": str((export / "data").exists()).lower()},
        {"check_item": "contains_results_dir", "status": "pass" if not (export / "results").exists() else "fail", "details": str((export / "results").exists()).lower()},
        {"check_item": "contains_large_files", "status": "pass" if not large else "fail", "details": ",".join(large) if large else "false"},
        {"check_item": "contains_secret_like_files", "status": "pass" if not secret else "fail", "details": ",".join(secret) if secret else "false"},
        {"check_item": "contains_raw_reads", "status": "pass" if not raw else "fail", "details": ",".join(raw) if raw else "false"},
        {"check_item": "contains_only_bridge", "status": "pass" if top <= allowed_top else "fail", "details": ",".join(sorted(top))},
        {"check_item": "latest_result_final_label", "status": "pass", "details": label},
        {"check_item": "claim_boundary_present", "status": "pass" if claim != "missing" else "warn", "details": claim[:200]},
    ]
    write_tsv(export / "EXPORT_SAFETY_AUDIT.tsv", audit, ["check_item", "status", "details"])

    manifest: list[dict[str, str]] = []
    for path in iter_files():
        if path.name == "EXPORT_MANIFEST.tsv":
            continue
        data = path.read_bytes()
        manifest.append(
            {
                "relative_path": path.relative_to(export).as_posix(),
                "size_bytes": str(len(data)),
                "sha256": hashlib.sha256(data).hexdigest(),
                "included": "yes",
                "reason": "allowed bridge mirror file",
                "notes": "no raw/data/results full export; EXPORT_MANIFEST.tsv is not self-listed",
            }
        )
    write_tsv(export / "EXPORT_MANIFEST.tsv", manifest, ["relative_path", "size_bytes", "sha256", "included", "reason", "notes"])

    if any(row["status"] == "fail" for row in audit):
        raise SystemExit("export safety audit failed")
    print(f"refreshed {export.relative_to(root)} with {len(manifest)} manifest rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
