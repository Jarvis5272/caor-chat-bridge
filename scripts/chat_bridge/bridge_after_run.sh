#!/usr/bin/env bash
set -euo pipefail

latest_result="${1:-}"
repo_root="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$repo_root"

if [[ -n "$latest_result" && -d "$latest_result" ]]; then
  python scripts/chat_bridge/update_chat_bridge_snapshot.py \
    --latest-result "$latest_result" \
    --out chat_bridge
else
  if [[ -n "$latest_result" ]]; then
    echo "Requested latest result not found: $latest_result" >&2
    echo "Falling back to --auto-detect-latest." >&2
  fi
  python scripts/chat_bridge/update_chat_bridge_snapshot.py \
    --auto-detect-latest \
    --out chat_bridge
fi

python scripts/chat_bridge/build_feedback_package.py \
  --in chat_bridge \
  --out chat_bridge_feedback_package.zip

zip -T chat_bridge_feedback_package.zip

python - <<'PY'
from __future__ import annotations

import csv
import hashlib
import json
import re
import shutil
from pathlib import Path

root = Path.cwd().resolve()
export = root / "chat_bridge_export"
export.mkdir(parents=True, exist_ok=True)

# Refresh the export working tree but preserve an existing standalone .git.
for child in list(export.iterdir()):
    if child.name == ".git":
        continue
    if child.is_dir():
        shutil.rmtree(child)
    else:
        child.unlink()

shutil.copytree(root / "chat_bridge", export / "chat_bridge", ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
shutil.copy2(root / "chat_bridge_feedback_package.zip", export / "chat_bridge_feedback_package.zip")
(export / "scripts").mkdir(parents=True, exist_ok=True)
shutil.copytree(root / "scripts" / "chat_bridge", export / "scripts" / "chat_bridge", ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))

latest = json.loads((root / "chat_bridge" / "02_LATEST_CODEX_RESULT.json").read_text(encoding="utf-8"))
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

forbidden_suffix = {".fastq", ".fq", ".fasta", ".fa", ".bam", ".sam", ".gz", ".npy", ".npz", ".pkl", ".chunk", ".chunks"}
secret_re = re.compile(r"(^|[/_.-])(secret|token|api[-_]?key|credential|password|passwd|id_rsa|id_dsa|id_ed25519|\.env)([/_.-]|$)", re.I)
large, secret, raw = [], [], []

def iter_export_files():
    for path in sorted(export.rglob("*")):
        if not path.is_file() or ".git" in path.parts:
            continue
        yield path

audit_probe = []
for path in iter_export_files():
    rel = path.relative_to(export).as_posix()
    size = path.stat().st_size
    if size > 1024 * 1024:
        large.append(rel)
    if secret_re.search(rel):
        secret.append(rel)
    if path.suffix.lower() in forbidden_suffix:
        raw.append(rel)
    audit_probe.append(rel)

top = {p.name for p in export.iterdir() if p.name != ".git"}
contains_data = (export / "data").exists()
contains_results = (export / "results").exists()
contains_only_bridge = top <= {
    "chat_bridge",
    "chat_bridge_feedback_package.zip",
    "scripts",
    "README.md",
    "EXPORT_MANIFEST.tsv",
    "EXPORT_SAFETY_AUDIT.tsv",
    "CHATGPT_LINK_INSTRUCTIONS_CN.md",
}

audit = [
    {"check_item": "contains_data_dir", "status": "pass" if not contains_data else "fail", "details": str(contains_data).lower()},
    {"check_item": "contains_results_dir", "status": "pass" if not contains_results else "fail", "details": str(contains_results).lower()},
    {"check_item": "contains_large_files", "status": "pass" if not large else "fail", "details": ",".join(large) if large else "false"},
    {"check_item": "contains_secret_like_files", "status": "pass" if not secret else "fail", "details": ",".join(secret) if secret else "false"},
    {"check_item": "contains_raw_reads", "status": "pass" if not raw else "fail", "details": ",".join(raw) if raw else "false"},
    {"check_item": "contains_only_bridge", "status": "pass" if contains_only_bridge else "fail", "details": ",".join(sorted(top))},
    {"check_item": "latest_result_final_label", "status": "pass", "details": label},
    {"check_item": "claim_boundary_present", "status": "pass" if claim != "missing" else "warn", "details": claim[:200]},
]
with (export / "EXPORT_SAFETY_AUDIT.tsv").open("w", encoding="utf-8", newline="") as handle:
    fields = ["check_item", "status", "details"]
    writer = csv.DictWriter(handle, delimiter="\t", fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(audit)

manifest = []
for path in iter_export_files():
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
with (export / "EXPORT_MANIFEST.tsv").open("w", encoding="utf-8", newline="") as handle:
    fields = ["relative_path", "size_bytes", "sha256", "included", "reason", "notes"]
    writer = csv.DictWriter(handle, delimiter="\t", fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(manifest)

if any(row["status"] == "fail" for row in audit):
    raise SystemExit("export safety audit failed")
PY

push_status="not_attempted_no_remote"
push_remote=""
push_branch=""

(
  cd chat_bridge_export
  if [[ ! -d .git ]]; then
    git init
  fi
  git add .
  if ! git diff --cached --quiet; then
    git commit -m "Update ChatGPT-Codex bridge snapshot" || (
      git config user.name "chat-bridge-bot"
      git config user.email "chat-bridge-bot@example.local"
      git commit -m "Update ChatGPT-Codex bridge snapshot"
    )
  else
    echo "No export changes to commit."
  fi
  if git remote get-url origin >/dev/null 2>&1; then
    push_remote="$(git remote get-url origin)"
    push_branch="$(git branch --show-current)"
    if git push -u origin HEAD; then
      push_status="pushed"
    else
      push_status="push_failed"
    fi
  fi
  {
    printf 'item\tstatus\tdetails\n'
    printf 'push_status\t%s\t%s\n' "$push_status" "$push_remote"
    printf 'push_branch\t%s\t%s\n' "${push_branch:-none}" "${push_branch:-none}"
    printf 'commit_hash\tpass\t%s\n' "$(git rev-parse HEAD)"
  } > PUSH_STATUS.tsv
  git add PUSH_STATUS.tsv
  if ! git diff --cached --quiet; then
    git commit -m "Record bridge export push status" || true
  fi
)

echo
echo "=== Copy to ChatGPT ==="
echo "Use: chat_bridge_export/chat_bridge_feedback_package.zip"
echo "Or start from: chat_bridge_export/chat_bridge/00_README_FIRST.md"
echo "Raw link after push: https://raw.githubusercontent.com/<USER>/<REPO>/main/chat_bridge/00_README_FIRST.md"
echo
echo "=== Recommended standalone bridge Git commands ==="
echo 'cd chat_bridge_export'
echo 'git remote add origin <YOUR_PUBLIC_BRIDGE_REPO_URL>'
echo 'git branch -M main'
echo 'git push -u origin main'
