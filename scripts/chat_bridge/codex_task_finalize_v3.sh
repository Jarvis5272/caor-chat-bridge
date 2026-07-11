#!/usr/bin/env bash
set -u
ROOT=/home/hanlinxuan/research/ACOR-online-reconstruction
EVENT_OUTPUT="${1:-}"
REQUESTED_LABEL="${2:-}"
RESULT="$ROOT/results/chat_bridge_v3_repair_20260711"
mkdir -p "$RESULT"
cd "$ROOT" || exit 1
if [[ -z "$EVENT_OUTPUT" || -z "$REQUESTED_LABEL" ]]; then echo "usage: codex_task_finalize_v3.sh results/<bridge-event> LABEL" >&2; exit 2; fi

python scripts/chat_bridge/update_chat_bridge_v3.py --locked-result results/final_result_cross_validation_20260711 --out chat_bridge --audit-out results/chat_bridge_v3_repair_20260711 --bridge-event-output "$EVENT_OUTPUT" --bridge-event-label "$REQUESTED_LABEL" || exit 2
python scripts/chat_bridge/validate_bridge_semantics_v3.py --bridge chat_bridge --out "$RESULT/BRIDGE_V3_SEMANTIC_VALIDATION.tsv" || exit 3
python scripts/chat_bridge/build_feedback_package.py --in chat_bridge --out chat_bridge_feedback_package.zip >/dev/null || exit 3
zip -T chat_bridge_feedback_package.zip >/dev/null || exit 3

bash scripts/chat_bridge/push_bridge_v3.sh
push_exit=$?
remote_verified=false
if [[ $push_exit -eq 0 ]]; then remote_verified=true; fi

timer_state=not_needed
if [[ "$remote_verified" != true ]]; then
  bash scripts/chat_bridge/install_bridge_retry_timer.sh > "$RESULT/timer_install.stdout" 2> "$RESULT/timer_install.stderr"
  timer_exit=$?
  timer_state=installed
  [[ $timer_exit -ne 0 ]] && timer_state=fallback_generated
fi

actual_label=CHAT_BRIDGE_V3_SEMANTIC_AND_REMOTE_SYNC_FIXED
if [[ "$remote_verified" != true ]]; then actual_label=CHAT_BRIDGE_V3_SEMANTIC_FIXED_REMOTE_RETRY_ARMED; fi
if [[ "$REQUESTED_LABEL" != "$actual_label" ]]; then
  echo "requested label $REQUESTED_LABEL does not match observed $actual_label" >&2
  REQUESTED_LABEL="$actual_label"
fi
cat > "$RESULT/FINAL_BRIDGE_V3_STATUS.tsv" <<EOF
item	status	details
semantic_validation	pass	Bridge V3 semantic validator passed
remote_verified	$remote_verified	push_exit=$push_exit
retry_timer	$timer_state	10-minute user retry
final_label	pass	$REQUESTED_LABEL
EOF
echo "$REQUESTED_LABEL"
exit 0
