#!/usr/bin/env bash
set -euo pipefail

latest_result="${1:-}"
task_final_label="${2:-TASK_FINAL_LABEL_MISSING}"

repo_root="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$repo_root"

bridge_status="bridge_failed_blocking"
if bash scripts/chat_bridge/bridge_after_run.sh "$latest_result"; then
  bridge_status="bridge_ok"
else
  bridge_status="bridge_failed_blocking"
fi

python - "$task_final_label" "$bridge_status" <<'PY'
from __future__ import annotations

import json
import sys
from pathlib import Path

task_final_label = sys.argv[1]
bridge_status = sys.argv[2]
root = Path.cwd()
bridge = root / "chat_bridge"
latest_path = bridge / "02_LATEST_CODEX_RESULT.json"

latest = json.loads(latest_path.read_text(encoding="utf-8")) if latest_path.exists() else {}
missing = latest.get("missing_expected_files", [])
if bridge_status == "bridge_ok" and missing:
    bridge_status = "bridge_ok_with_nonblocking_missing"

feedback = f"""# Codex Final Feedback

1. final label: `{task_final_label}`
2. output dir: `{latest.get('output_dir', 'missing')}`
3. completed stages: `{', '.join(latest.get('completed_stages', [])) or 'missing'}`
4. key metrics: `{latest.get('main_metrics', {})}`
5. gate decision: `{latest.get('gate_decision', 'missing')}`
6. claim boundary: `{latest.get('claim_boundary', 'missing')}`
7. next recommendation: `{latest.get('next_action', 'missing')}`
8. bridge status: `{bridge_status}`
9. chat_bridge_feedback_package path: `chat_bridge_feedback_package.zip`
10. bridge raw link if pushed: `see chat_bridge_export/CHATGPT_LINK_INSTRUCTIONS_CN.md`
11. protected files modified?: `{latest.get('protected_files_modified', 'unknown')}`
12. original BBS source modified?: `{latest.get('original_bbs_source_modified', 'unknown')}`
"""
(bridge / "codex_final_feedback.md").write_text(feedback, encoding="utf-8")
(bridge / "08_CODEX_FEEDBACK_TO_CHATGPT.md").write_text(feedback, encoding="utf-8")
print(feedback)
PY

python scripts/chat_bridge/build_feedback_package.py \
  --in chat_bridge \
  --out chat_bridge_feedback_package.zip
zip -T chat_bridge_feedback_package.zip
python scripts/chat_bridge/refresh_bridge_export.py \
  --bridge chat_bridge \
  --package chat_bridge_feedback_package.zip \
  --scripts scripts/chat_bridge \
  --out chat_bridge_export
(
  cd chat_bridge_export
  git add .
  if ! git diff --cached --quiet; then
    git commit -m "Finalize Codex bridge feedback" || (
      git config user.name "chat-bridge-bot"
      git config user.email "chat-bridge-bot@example.local"
      git commit -m "Finalize Codex bridge feedback"
    )
  fi
  if git remote get-url origin >/dev/null 2>&1; then
    git push -u origin HEAD || echo "EXPORT_PUSH_STATUS=push_failed"
  fi
)

if [[ "$bridge_status" == "bridge_failed_blocking" ]]; then
  exit 1
fi
