#!/usr/bin/env bash
set -euo pipefail

latest_result="${1:-}"
task_final_label="${2:-}"

repo_root="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$repo_root"

raw_readme_link="https://raw.githubusercontent.com/Jarvis5272/caor-chat-bridge/main/chat_bridge/00_README_FIRST.md"
fallback_package="chat_bridge_feedback_package.zip"

if [[ -z "$latest_result" || -z "$task_final_label" ]]; then
  mkdir -p chat_bridge
  cat > chat_bridge/codex_final_feedback.md <<EOF_FEEDBACK
# Codex Final Feedback

1. final label: TASK_COMPLETED_BUT_BRIDGE_FINALIZE_FAILED
2. output dir: ${latest_result:-missing}
3. bridge status: bridge_failed_missing_required
4. raw README link: $raw_readme_link
5. fallback package: $fallback_package
6. local bridge validation: fail
7. raw bridge validation: fail
8. protected files modified?: unknown
9. original BBS source modified?: unknown
10. message to ChatGPT: 请等待 bridge 修复；当前 latest pointer 未验证。
EOF_FEEDBACK
  cp chat_bridge/codex_final_feedback.md chat_bridge/08_CODEX_FEEDBACK_TO_CHATGPT.md 2>/dev/null || true
  cat chat_bridge/codex_final_feedback.md
  exit 2
fi

if ! bash scripts/chat_bridge/bridge_after_run.sh "$latest_result" "$task_final_label"; then
  mkdir -p chat_bridge
  cat > chat_bridge/codex_final_feedback.md <<EOF_FEEDBACK
# Codex Final Feedback

1. final label: TASK_COMPLETED_BUT_BRIDGE_FINALIZE_FAILED
2. output dir: $latest_result
3. bridge status: bridge_finalize_failed
4. raw README link: $raw_readme_link
5. fallback package: $fallback_package
6. local bridge validation: see chat_bridge/BRIDGE_LOCAL_VALIDATION.tsv
7. raw bridge validation: see chat_bridge/BRIDGE_RAW_VALIDATION.tsv
8. protected files modified?: unknown
9. original BBS source modified?: unknown
10. message to ChatGPT: 请等待 bridge 修复；当前 latest pointer 未验证。
EOF_FEEDBACK
  cp chat_bridge/codex_final_feedback.md chat_bridge/08_CODEX_FEEDBACK_TO_CHATGPT.md 2>/dev/null || true
  cat chat_bridge/codex_final_feedback.md
  exit 1
fi

protected_modified="unknown"
original_modified="unknown"
if [[ -f chat_bridge/02_LATEST_CODEX_RESULT.json ]]; then
  protected_modified="$(python -c 'import json;print(json.load(open("chat_bridge/02_LATEST_CODEX_RESULT.json")).get("protected_files_modified","unknown"))')"
  original_modified="$(python -c 'import json;print(json.load(open("chat_bridge/02_LATEST_CODEX_RESULT.json")).get("original_bbs_source_modified","unknown"))')"
fi

cat <<EOF_SUCCESS
1. final label: $task_final_label
2. output dir: $latest_result
3. bridge status: bridge_ok_pushed_and_raw_verified
4. raw README link: $raw_readme_link
5. fallback package: $fallback_package
6. local bridge validation: pass
7. raw bridge validation: pass
8. protected files modified?: $protected_modified
9. original BBS source modified?: $original_modified
10. message to ChatGPT: 请读取 $raw_readme_link 并基于 chat_bridge 更新项目状态。
EOF_SUCCESS
