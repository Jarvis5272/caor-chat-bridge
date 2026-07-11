#!/usr/bin/env bash
set -u
ROOT=/home/hanlinxuan/research/ACOR-online-reconstruction
RESULT="$ROOT/results/chat_bridge_v3_repair_20260711"
LOCK=/tmp/caor-chat-bridge-sync.lock
mkdir -p "$RESULT"
exec 9>"$LOCK"
flock -n 9 || exit 0
cd "$ROOT" || exit 1

if [[ -f chat_bridge/REMOTE_SYNC_STATUS.json ]] && python -c 'import json,sys;s=json.load(open("chat_bridge/REMOTE_SYNC_STATUS.json"));sys.exit(0 if s.get("verified") else 1)' 2>/dev/null; then
  if python scripts/chat_bridge/validate_bridge_raw_v3.py --bridge chat_bridge --out "$RESULT/RAW_BRIDGE_VERIFICATION.tsv" --retries 1 --retry-sleep 1 >/dev/null 2>&1; then
    exit 0
  fi
fi

python scripts/chat_bridge/update_chat_bridge_v3.py --locked-result results/final_result_cross_validation_20260711 --out chat_bridge --audit-out results/chat_bridge_v3_repair_20260711 >/dev/null || exit 1
python scripts/chat_bridge/validate_bridge_semantics_v3.py --bridge chat_bridge --out "$RESULT/BRIDGE_V3_SEMANTIC_VALIDATION.tsv" >/dev/null || exit 1
bash scripts/chat_bridge/push_bridge_v3.sh >> "$RESULT/remote_retry.log" 2>&1
exit $?
