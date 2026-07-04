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

echo
echo "=== Copy to ChatGPT ==="
echo "Use: chat_bridge_feedback_package.zip"
echo "Or start from: chat_bridge/00_README_FIRST.md"
echo
echo "=== Recommended Git commands ==="
echo 'git add chat_bridge chat_bridge_feedback_package.zip scripts/chat_bridge'
echo 'git commit -m "Update ChatGPT-Codex bridge snapshot"'
echo 'git push origin HEAD:chat-bridge'

if [[ "${CHAT_BRIDGE_AUTO_PUSH:-0}" == "1" ]]; then
  if git remote get-url origin >/dev/null 2>&1; then
    git push origin HEAD:chat-bridge || echo "AUTO_PUSH_FAILED"
  else
    echo "AUTO_PUSH_SKIPPED_NO_ORIGIN"
  fi
fi
