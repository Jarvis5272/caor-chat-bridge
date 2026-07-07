#!/usr/bin/env bash
set -euo pipefail

# ============================================================================
# Bridge V2 Agent Task Startup
# ============================================================================
# This script reads ACTIVE_TASK.json and validates state consistency before
# any agent (Codex / Claude Code / ChatGPT) starts algorithmic work.
#
# Usage:
#   bash scripts/chat_bridge/start_agent_task.sh [--agent <name>]
#
# Exit codes:
#   0 - state consistent, agent may proceed
#   1 - general error
#   2 - state inconsistency detected (BLOCKING)
#   3 - missing required files
# ============================================================================

AGENT_NAME="${AGENT_NAME:-unknown}"
while [[ $# -gt 0 ]]; do
  case "$1" in
    --agent) AGENT_NAME="$2"; shift 2 ;;
    *) echo "Unknown arg: $1" >&2; exit 1 ;;
  esac
done

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$REPO_ROOT"

BRIDGE_DIR="chat_bridge"
ACTIVE_TASK="$BRIDGE_DIR/ACTIVE_TASK.json"
FROZEN_HISTORY="$BRIDGE_DIR/FROZEN_HISTORY.tsv"

# ── Phase 0: Verify bridge v2 files exist ──────────────────────────────────

MISSING=""
for f in "$ACTIVE_TASK" "$FROZEN_HISTORY" "$BRIDGE_DIR/AGENT_HANDOFF.md"; do
  [[ -f "$f" ]] || MISSING="$MISSING $f"
done

if [[ -n "$MISSING" ]]; then
  echo "BRIDGE_V2_STARTUP_FAILED: missing required bridge v2 files:$MISSING" >&2
  exit 3
fi

# ── Phase 1: Parse ACTIVE_TASK.json ────────────────────────────────────────

echo "=== Bridge V2 Agent Startup ==="
echo "Agent: $AGENT_NAME"
echo "Time:  $(date -Iseconds)"

ACTIVE_OUTPUT_DIR="$(python3 -c "import json;print(json.load(open('$ACTIVE_TASK'))['active_output_dir'])")"
TASK_STATUS="$(python3 -c "import json;print(json.load(open('$ACTIVE_TASK'))['task_status'])")"
FINAL_LABEL="$(python3 -c "import json;print(json.load(open('$ACTIVE_TASK'))['final_label'])")"
FROZEN_COUNT="$(python3 -c "import json;print(json.load(open('$ACTIVE_TASK'))['frozen_candidate_count'])")"
ACTIVE_FRONTIER="$(python3 -c "import json;print(json.load(open('$ACTIVE_TASK'))['active_frontier'])")"
LAST_AGENT="$(python3 -c "import json;print(json.load(open('$ACTIVE_TASK'))['last_agent'])")"

echo ""
echo "Active Task:"
echo "  task_status:       $TASK_STATUS"
echo "  output_dir:        $ACTIVE_OUTPUT_DIR"
echo "  final_label:       $FINAL_LABEL"
echo "  frozen_count:      $FROZEN_COUNT"
echo "  active_frontier:   $ACTIVE_FRONTIER"
echo "  last_agent:        $LAST_AGENT"

# ── Phase 2: Verify FROZEN_HISTORY.tsv integrity ───────────────────────────

# Count non-header, non-reserved rows
FROZEN_ROWS="$(tail -n +2 "$FROZEN_HISTORY" | grep -v "^__RESERVED__" | grep -c . || true)"
echo ""
echo "FROZEN_HISTORY.tsv: $FROZEN_ROWS data rows"

if [[ "$FROZEN_ROWS" -ne "$FROZEN_COUNT" ]]; then
  echo ""
  echo "=== BRIDGE_V2_STATE_INCONSISTENCY ==="
  echo "ACTIVE_TASK.json frozen_candidate_count = $FROZEN_COUNT"
  echo "FROZEN_HISTORY.tsv data rows          = $FROZEN_ROWS"
  echo "MISMATCH: these MUST be equal."
  echo ""
  echo "Action: DO NOT start algorithmic work."
  echo "        Resolve the inconsistency manually before proceeding."
  exit 2
fi

# ── Phase 3: Verify controller state matches ACTIVE_TASK ───────────────────

CONTROLLER_STATE="$ACTIVE_OUTPUT_DIR/controller_state.json"
FROZEN_TSV="$ACTIVE_OUTPUT_DIR/frozen_candidates.tsv"

if [[ ! -f "$CONTROLLER_STATE" ]]; then
  echo "WARNING: controller_state.json not found at $CONTROLLER_STATE"
  echo "         This may be a fresh task. Proceeding with ACTIVE_TASK.json only."
else
  CS_LABEL="$(python3 -c "import json;print(json.load(open('$CONTROLLER_STATE')).get('final_label',''))")"
  CS_COUNT="$(python3 -c "import json;print(json.load(open('$CONTROLLER_STATE')).get('total_frozen',0))")"
  echo ""
  echo "controller_state.json:  label=$CS_LABEL  frozen=$CS_COUNT"

  if [[ "$CS_LABEL" != "$FINAL_LABEL" ]]; then
    echo ""
    echo "=== BRIDGE_V2_STATE_INCONSISTENCY ==="
    echo "ACTIVE_TASK.json final_label:        $FINAL_LABEL"
    echo "controller_state.json final_label:   $CS_LABEL"
    echo "MISMATCH: labels must agree."
    exit 2
  fi

  if [[ -f "$FROZEN_TSV" ]]; then
    TSV_ROWS="$(tail -n +2 "$FROZEN_TSV" | grep -c . || true)"
    if [[ "$TSV_ROWS" -ne "$FROZEN_COUNT" ]]; then
      echo ""
      echo "=== BRIDGE_V2_STATE_INCONSISTENCY ==="
      echo "ACTIVE_TASK.json frozen_candidate_count: $FROZEN_COUNT"
      echo "frozen_candidates.tsv rows:              $TSV_ROWS"
      echo "MISMATCH: counts must agree."
      exit 2
    fi
  fi
fi

# ── Phase 4: Task status decision ──────────────────────────────────────────

echo ""
echo "=== Task Status Decision ==="

case "$TASK_STATUS" in
  frozen_no_admissible_frontier)
    echo "STATUS: Frontier exhausted. No remaining candidates."
    echo "ACTION: Do NOT start new algorithmic work."
    echo "        Report current state only."
    echo "        New candidates require an approved new theory."
    echo ""
    echo "STARTUP_BLOCKED: no_admissible_frontier"
    exit 0
    ;;
  target_success)
    echo "STATUS: Target already achieved."
    echo "ACTION: Do NOT start new work. Report only."
    echo ""
    echo "STARTUP_GATE: target_already_met"
    exit 0
    ;;
  in_progress|resource_checkpoint)
    echo "STATUS: $TASK_STATUS — frontier has remaining candidates."
    echo "FRONTIER: $ACTIVE_FRONTIER"
    echo "ACTION: Resume from these candidates."
    echo "        Do NOT re-run frozen candidates."
    echo "        Do NOT restore BAEPC."
    ;;
  *)
    echo "STATUS: $TASK_STATUS (unknown)"
    echo "ACTION: Proceed with caution. Verify with user."
    ;;
esac

# ── Phase 5: Print working instructions ────────────────────────────────────

echo ""
echo "=== Agent Working Instructions ==="
echo ""
echo "1. Read:  $BRIDGE_DIR/AGENT_HANDOFF.md"
echo "2. Read:  $BRIDGE_DIR/00_README_FIRST.md"
echo "3. Read:  $BRIDGE_DIR/FROZEN_HISTORY.tsv (DO NOT MODIFY)"
echo "4. Read:  $BRIDGE_DIR/ACTIVE_TASK.json (for boundaries)"
echo ""
echo "5. Output dir:  $ACTIVE_OUTPUT_DIR"
echo "6. DO NOT re-run or modify any candidate in FROZEN_HISTORY.tsv"
echo "7. DO NOT use BBS/EPBSD/reference/dataset online"
echo "8. Append results only — never overwrite"
echo ""
echo "=== Bridge V2 Startup Complete ==="
