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

python scripts/chat_bridge/refresh_bridge_export.py \
  --bridge chat_bridge \
  --package chat_bridge_feedback_package.zip \
  --scripts scripts/chat_bridge \
  --out chat_bridge_export

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

  push_status="not_attempted_no_remote"
  push_remote=""
  push_branch="$(git branch --show-current)"
  if git remote get-url origin >/dev/null 2>&1; then
    push_remote="$(git remote get-url origin)"
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
