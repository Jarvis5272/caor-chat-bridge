#!/usr/bin/env bash
set -euo pipefail

latest_result="${1:-}"
final_label="${2:-}"

if [[ -z "$latest_result" || -z "$final_label" ]]; then
  echo "bridge_failed_missing_required: usage bash scripts/chat_bridge/bridge_after_run.sh results/<run_dir> \"<FINAL_LABEL>\"" >&2
  exit 2
fi

repo_root="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$repo_root"

bridge_remote_url="git@github-caor-chat-bridge:Jarvis5272/caor-chat-bridge.git"
bridge_branch="main"
raw_base="https://raw.githubusercontent.com/Jarvis5272/caor-chat-bridge/main"

if [[ -f chat_bridge/bridge_remote.env ]]; then
  set -a
  # shellcheck disable=SC1091
  source chat_bridge/bridge_remote.env
  set +a
  bridge_remote_url="${BRIDGE_REMOTE_URL:-$bridge_remote_url}"
  bridge_branch="${BRIDGE_BRANCH:-$bridge_branch}"
fi

if [[ ! -d "$latest_result" ]]; then
  echo "bridge_failed_missing_required: explicit latest result not found: $latest_result" >&2
  exit 2
fi

echo "bridge status: updating explicit latest result"
python scripts/chat_bridge/update_chat_bridge_snapshot.py \
  --latest-result "$latest_result" \
  --final-label-override "$final_label" \
  --no-auto-detect \
  --out chat_bridge

echo "bridge status: local validation"
if ! python scripts/chat_bridge/validate_bridge_latest.py \
  --bridge chat_bridge \
  --expected-result "$latest_result" \
  --expected-label "$final_label"; then
  echo "bridge_failed_local_mismatch" >&2
  exit 3
fi

rm -f chat_bridge/BRIDGE_RAW_VALIDATION.tsv chat_bridge/BRIDGE_FINALIZE_STATUS.tsv

echo "bridge status: package"
python scripts/chat_bridge/build_feedback_package.py \
  --in chat_bridge \
  --out chat_bridge_feedback_package.zip

zip -T chat_bridge_feedback_package.zip

echo "bridge status: refresh export"
python scripts/chat_bridge/refresh_bridge_export.py \
  --bridge chat_bridge \
  --package chat_bridge_feedback_package.zip \
  --scripts scripts/chat_bridge \
  --out chat_bridge_export

echo "bridge status: commit and push export"
(
  cd chat_bridge_export
  if [[ ! -d .git ]]; then
    git init
  fi
  git config user.name "chat-bridge-bot"
  git config user.email "chat-bridge-bot@example.local"
  git remote remove origin >/dev/null 2>&1 || true
  git remote add origin "$bridge_remote_url"
  git branch -M "$bridge_branch"
  git add .
  if ! git diff --cached --quiet; then
    git commit -m "Transactional bridge finalize: $final_label"
  else
    echo "No export changes to commit."
  fi
  if [[ -n "${BRIDGE_GIT_SSH_COMMAND:-}" ]]; then
    GIT_SSH_COMMAND="$BRIDGE_GIT_SSH_COMMAND" git push -u origin "$bridge_branch"
  else
    git push -u origin "$bridge_branch"
  fi
)

echo "bridge status: raw validation"
if ! python scripts/chat_bridge/validate_bridge_raw.py \
  --expected-result "$latest_result" \
  --expected-label "$final_label" \
  --raw-base "$raw_base"; then
  echo "bridge_failed_raw_mismatch" >&2
  exit 4
fi

cat > chat_bridge/BRIDGE_FINALIZE_STATUS.tsv <<EOF_STATUS
item	status	details
bridge_status	pass	bridge_ok_pushed_and_raw_verified
expected_result	pass	$latest_result
expected_label	pass	$final_label
raw_readme_link	pass	$raw_base/chat_bridge/00_README_FIRST.md
fallback_package	pass	chat_bridge_feedback_package.zip
EOF_STATUS

echo "bridge_ok_pushed_and_raw_verified"
echo "raw_readme_link=$raw_base/chat_bridge/00_README_FIRST.md"
echo "fallback_package=chat_bridge_feedback_package.zip"
