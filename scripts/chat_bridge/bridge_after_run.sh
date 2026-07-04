#!/usr/bin/env bash
set -euo pipefail

latest_result="${1:-}"
repo_root="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$repo_root"

bridge_remote_url="${CHAT_BRIDGE_REMOTE_URL:-}"
bridge_branch="${BRIDGE_BRANCH:-main}"
auto_push="${CHAT_BRIDGE_AUTO_PUSH:-0}"
if [[ -f chat_bridge/bridge_remote.env ]]; then
  # shellcheck disable=SC1091
  source chat_bridge/bridge_remote.env
  bridge_remote_url="${CHAT_BRIDGE_REMOTE_URL:-${BRIDGE_REMOTE_URL:-$bridge_remote_url}}"
  bridge_branch="${BRIDGE_BRANCH:-$bridge_branch}"
  auto_push="${CHAT_BRIDGE_AUTO_PUSH:-${AUTO_PUSH:-$auto_push}}"
fi

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
  git config user.name "chat-bridge-bot"
  git config user.email "chat-bridge-bot@example.local"
  if [[ -n "$bridge_remote_url" ]]; then
    git remote remove origin >/dev/null 2>&1 || true
    git remote add origin "$bridge_remote_url"
    git branch -M "$bridge_branch"
  fi
  push_status="not_attempted_no_remote"
  push_remote="$bridge_remote_url"
  push_branch="$(git branch --show-current 2>/dev/null || true)"
  if [[ -n "$push_remote" ]]; then
    push_status="pending_push"
  fi
  {
    printf 'item\tstatus\tdetails\n'
    printf 'push_status\t%s\t%s\n' "$push_status" "$push_remote"
    printf 'push_branch\t%s\t%s\n' "${push_branch:-none}" "${push_branch:-none}"
    printf 'commit_hash\tpending\tupdated_after_commit\n'
  } > PUSH_STATUS.tsv
  git add .
  if ! git diff --cached --quiet; then
    git commit -m "Update ChatGPT-Codex bridge snapshot"
  else
    echo "No export changes to commit."
  fi

  final_push_status="$push_status"
  if [[ "$auto_push" == "1" && -n "$push_remote" ]]; then
    if git push -u origin "$push_branch"; then
      final_push_status="pushed"
    else
      final_push_status="push_failed"
    fi
  elif [[ -n "$push_remote" ]]; then
    final_push_status="configured_not_pushed"
  fi
  {
    printf 'item\tstatus\tdetails\n'
    printf 'push_status\t%s\t%s\n' "$final_push_status" "$push_remote"
    printf 'push_branch\t%s\t%s\n' "${push_branch:-none}" "${push_branch:-none}"
    printf 'commit_hash\tpass\t%s\n' "$(git rev-parse HEAD)"
  } > PUSH_STATUS.tsv
  git add PUSH_STATUS.tsv
  if ! git diff --cached --quiet; then
    git commit -m "Record bridge export push status"
  fi
)

echo
echo "=== Copy to ChatGPT ==="
echo "Use: chat_bridge_export/chat_bridge_feedback_package.zip"
echo "Or start from: chat_bridge_export/chat_bridge/00_README_FIRST.md"
echo "Raw link after push: https://raw.githubusercontent.com/Jarvis5272/caor-chat-bridge/main/chat_bridge/00_README_FIRST.md"
echo
echo "=== Recommended standalone bridge Git commands ==="
echo 'cd chat_bridge_export'
if [[ -n "$bridge_remote_url" ]]; then
  echo "git remote remove origin >/dev/null 2>&1 || true"
  echo "git remote add origin $bridge_remote_url"
else
  echo 'git remote add origin <YOUR_PUBLIC_BRIDGE_REPO_URL>'
fi
echo "git branch -M $bridge_branch"
echo "git push -u origin $bridge_branch"
