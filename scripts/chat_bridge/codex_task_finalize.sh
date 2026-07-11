#!/usr/bin/env bash
exec bash "$(dirname "$0")/codex_task_finalize_v3.sh" "$@"
set -euo pipefail

# ============================================================================
# Bridge V2 Transactional Task Finalize
# ============================================================================
# Finalizes a task run by running state consistency checks, regenerating the
# chat_bridge/ snapshot, validating locally, packaging, pushing to GitHub,
# and verifying the raw README link.
#
# Bridge V2 additions:
#   - Pre-finalize consistency check against ACTIVE_TASK.json
#   - FROZEN_HISTORY.tsv integrity verification
#   - State drift detection (refuses to finalize if inconsistent)
#   - Bridge v2 status recorded in final feedback
#
# Usage:
#   bash scripts/chat_bridge/codex_task_finalize.sh results/<run_dir> "<FINAL_LABEL>"
#
# Exit codes:
#   0 - success, bridge pushed and raw verified
#   1 - bridge finalize step failed
#   2 - missing required arguments or state inconsistency
#   3 - local validation mismatch
#   4 - raw validation mismatch
# ============================================================================

latest_result="${1:-}"
task_final_label="${2:-}"

repo_root="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$repo_root"

raw_readme_link="https://raw.githubusercontent.com/Jarvis5272/caor-chat-bridge/main/chat_bridge/00_README_FIRST.md"
fallback_package="chat_bridge_feedback_package.zip"

# ── Pre-flight: bridge v2 state consistency ────────────────────────────────

ACTIVE_TASK="chat_bridge/ACTIVE_TASK.json"
FROZEN_HISTORY="chat_bridge/FROZEN_HISTORY.tsv"

bridge_v2_consistency="unknown"
bridge_v2_checks=""

if [[ -z "$latest_result" || -z "$task_final_label" ]]; then
  mkdir -p chat_bridge
  cat > chat_bridge/codex_final_feedback.md <<EOF_FEEDBACK
# Codex Final Feedback

1. final label: TASK_COMPLETED_BUT_BRIDGE_FINALIZE_FAILED
2. output dir: ${latest_result:-missing}
3. bridge status: bridge_failed_missing_required
4. bridge v2 consistency: skipped_missing_args
5. raw README link: $raw_readme_link
6. fallback package: $fallback_package
7. local bridge validation: fail
8. raw bridge validation: fail
9. protected files modified?: unknown
10. original BBS source modified?: unknown
11. message to ChatGPT: Bridge V2 finalize failed — missing run_dir or FINAL_LABEL.
EOF_FEEDBACK
  cp chat_bridge/codex_final_feedback.md chat_bridge/08_CODEX_FEEDBACK_TO_CHATGPT.md 2>/dev/null || true
  cat chat_bridge/codex_final_feedback.md
  exit 2
fi

# ── Bridge V2 Consistency Check ────────────────────────────────────────────

echo "=== Bridge V2 Pre-Finalize Consistency Check ==="

if [[ -f "$ACTIVE_TASK" ]]; then
  at_dir="$(python3 -c "import json;print(json.load(open('$ACTIVE_TASK'))['active_output_dir'])")"
  at_label="$(python3 -c "import json;print(json.load(open('$ACTIVE_TASK'))['final_label'])")"
  at_frozen="$(python3 -c "import json;print(json.load(open('$ACTIVE_TASK'))['frozen_candidate_count'])")"
  at_status="$(python3 -c "import json;print(json.load(open('$ACTIVE_TASK'))['task_status'])")"

  # Check 1: output dir matches
  if [[ "$at_dir" != "$latest_result" ]]; then
    echo "BRIDGE_V2_CONSISTENCY_FAIL: output_dir mismatch"
    echo "  ACTIVE_TASK.json active_output_dir: $at_dir"
    echo "  finalize arg latest_result:         $latest_result"
    bridge_v2_consistency="fail_output_dir_mismatch"
    bridge_v2_checks="output_dir_mismatch"
  fi

  # Check 2: FROZEN_HISTORY.tsv exists and row count matches
  if [[ -f "$FROZEN_HISTORY" ]]; then
    fh_rows="$(tail -n +2 "$FROZEN_HISTORY" | grep -v "^__RESERVED__" | grep -c . || true)"
    if [[ "$fh_rows" -ne "$at_frozen" ]]; then
      echo "BRIDGE_V2_CONSISTENCY_FAIL: frozen count mismatch"
      echo "  ACTIVE_TASK.json frozen_candidate_count: $at_frozen"
      echo "  FROZEN_HISTORY.tsv data rows:            $fh_rows"
      bridge_v2_consistency="fail_frozen_count_mismatch"
      bridge_v2_checks="${bridge_v2_checks};frozen_count_mismatch"
    fi
  else
    echo "BRIDGE_V2_CONSISTENCY_FAIL: FROZEN_HISTORY.tsv missing"
    bridge_v2_consistency="fail_frozen_history_missing"
    bridge_v2_checks="${bridge_v2_checks};frozen_history_missing"
  fi

  # Check 3: controller_state.json consistency
  cs="$latest_result/controller_state.json"
  if [[ -f "$cs" ]]; then
    cs_label="$(python3 -c "import json;print(json.load(open('$cs')).get('final_label',''))")"
    if [[ "$cs_label" != "$task_final_label" ]]; then
      echo "BRIDGE_V2_CONSISTENCY_WARN: controller_state.json label differs from finalize arg"
      echo "  controller_state.json final_label: $cs_label"
      echo "  finalize arg FINAL_LABEL:           $task_final_label"
      bridge_v2_checks="${bridge_v2_checks};controller_label_warn"
    fi
  fi

  # If any hard fail, abort
  if [[ "$bridge_v2_consistency" == fail_* ]]; then
    echo ""
    echo "=== BRIDGE_V2_FINALIZE_BLOCKED ==="
    echo "State inconsistency detected. Finalize aborted."
    echo "Fix the inconsistency before re-running finalize."
    echo ""
    mkdir -p chat_bridge
    cat > chat_bridge/codex_final_feedback.md <<EOF_FEEDBACK
# Codex Final Feedback (Bridge V2)

1. final label: BRIDGE_V2_STATE_INCONSISTENCY_DETECTED
2. output dir: $latest_result
3. bridge status: bridge_v2_blocked_state_inconsistency
4. bridge v2 consistency: $bridge_v2_consistency
5. bridge v2 checks: $bridge_v2_checks
6. raw README link: $raw_readme_link
7. fallback package: $fallback_package
8. message to ChatGPT: Bridge V2 blocked — state files are inconsistent. Manual resolution required.
EOF_FEEDBACK
    cp chat_bridge/codex_final_feedback.md chat_bridge/08_CODEX_FEEDBACK_TO_CHATGPT.md 2>/dev/null || true
    cat chat_bridge/codex_final_feedback.md
    exit 2
  fi

  bridge_v2_consistency="pass"
  echo "Bridge V2 consistency: PASS"
else
  echo "Bridge V2: ACTIVE_TASK.json not found — running in legacy mode"
  bridge_v2_consistency="legacy_no_active_task"
fi

# ── Update ACTIVE_TASK.json ────────────────────────────────────────────────

if [[ -f "$ACTIVE_TASK" ]]; then
  python3 -c "
import json
with open('$ACTIVE_TASK') as f:
    state = json.load(f)
state['final_label'] = '$task_final_label'
state['task_status'] = 'frozen_no_admissible_frontier' if '$task_final_label' == 'PARETO_RUN_NO_ADMISSIBLE_FRONTIER_LEFT' else state.get('task_status','updated')
state['last_agent'] = state.get('last_agent','bridge_finalize')
state['last_agent_action'] = 'bridge_v2_finalize: $task_final_label'
import datetime
state['last_modified_iso'] = datetime.datetime.now().astimezone().isoformat()
with open('$ACTIVE_TASK', 'w') as f:
    json.dump(state, f, indent=2, ensure_ascii=False)
    f.write('\n')
"
  echo "ACTIVE_TASK.json updated"
fi

# ── Core bridge finalize ───────────────────────────────────────────────────

echo ""
echo "=== Bridge Finalize ==="

if ! bash scripts/chat_bridge/bridge_after_run.sh "$latest_result" "$task_final_label"; then
  mkdir -p chat_bridge
  cat > chat_bridge/codex_final_feedback.md <<EOF_FEEDBACK
# Codex Final Feedback (Bridge V2)

1. final label: TASK_COMPLETED_BUT_BRIDGE_FINALIZE_FAILED
2. output dir: $latest_result
3. bridge status: bridge_finalize_failed
4. bridge v2 consistency: $bridge_v2_consistency
5. raw README link: $raw_readme_link
6. fallback package: $fallback_package
7. local bridge validation: see chat_bridge/BRIDGE_LOCAL_VALIDATION.tsv
8. raw bridge validation: see chat_bridge/BRIDGE_RAW_VALIDATION.tsv
9. protected files modified?: unknown
10. original BBS source modified?: unknown
11. message to ChatGPT: Bridge finalize step failed. Check validation files.
EOF_FEEDBACK
  cp chat_bridge/codex_final_feedback.md chat_bridge/08_CODEX_FEEDBACK_TO_CHATGPT.md 2>/dev/null || true
  cat chat_bridge/codex_final_feedback.md
  exit 1
fi

# ── Final feedback ─────────────────────────────────────────────────────────

protected_modified="unknown"
original_modified="unknown"
if [[ -f chat_bridge/02_LATEST_CODEX_RESULT.json ]]; then
  protected_modified="$(python3 -c 'import json;print(json.load(open("chat_bridge/02_LATEST_CODEX_RESULT.json")).get("protected_files_modified","unknown"))')"
  original_modified="$(python3 -c 'import json;print(json.load(open("chat_bridge/02_LATEST_CODEX_RESULT.json")).get("original_bbs_source_modified","unknown"))')"
fi

cat <<EOF_SUCCESS
=== Bridge V2 Finalize Success ===

1. final label: $task_final_label
2. output dir: $latest_result
3. bridge status: bridge_ok_pushed_and_raw_verified
4. bridge v2 consistency: $bridge_v2_consistency
5. raw README link: $raw_readme_link
6. fallback package: $fallback_package
7. local bridge validation: pass
8. raw bridge validation: pass
9. protected files modified?: $protected_modified
10. original BBS source modified?: $original_modified
11. message to ChatGPT: 请读取 $raw_readme_link 并基于 chat_bridge/ACTIVE_TASK.json 恢复项目状态。
12. active task file: chat_bridge/ACTIVE_TASK.json
13. frozen history: chat_bridge/FROZEN_HISTORY.tsv
14. handoff protocol: chat_bridge/AGENT_HANDOFF.md
EOF_SUCCESS
