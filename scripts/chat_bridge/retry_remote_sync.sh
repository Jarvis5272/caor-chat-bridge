#!/usr/bin/env bash
set -u
PYTHON_BIN=/home/hanlinxuan/miniconda3/bin/python3
ROOT=/home/hanlinxuan/research/ACOR-online-reconstruction
RESULT="$ROOT/results/chat_bridge_v3_repair_20260711"
LOCK=/tmp/caor-chat-bridge-sync.lock
LOG="$RESULT/remote_retry.log"
mkdir -p "$RESULT"
exec 9>"$LOCK"
flock -n 9 || exit 0
cd "$ROOT" || exit 1
exec >>"$LOG" 2>&1
echo "[$(date --iso-8601=seconds)] retry start"

if [[ -f chat_bridge/REMOTE_SYNC_STATUS.json ]] && "$PYTHON_BIN" -c 'import json,sys;s=json.load(open("chat_bridge/REMOTE_SYNC_STATUS.json"));sys.exit(0 if s.get("verified") else 1)' 2>/dev/null; then
  if "$PYTHON_BIN" scripts/chat_bridge/validate_bridge_raw_v3.py --bridge chat_bridge --out "$RESULT/RAW_BRIDGE_VERIFICATION.tsv" --retries 1 --retry-sleep 1 >/dev/null 2>&1; then
    echo "[$(date --iso-8601=seconds)] remote already verified; no commit"
    exit 0
  fi
fi

if ! "$PYTHON_BIN" scripts/chat_bridge/update_chat_bridge_v3.py --locked-result results/final_result_cross_validation_20260711 --out chat_bridge --audit-out results/chat_bridge_v3_repair_20260711 >/dev/null; then
  echo "[$(date --iso-8601=seconds)] local generation failed"
  exit 1
fi
if ! "$PYTHON_BIN" scripts/chat_bridge/validate_bridge_semantics_v3.py --bridge chat_bridge --out "$RESULT/BRIDGE_V3_SEMANTIC_VALIDATION.tsv" >/dev/null; then
  echo "[$(date --iso-8601=seconds)] local semantic validation failed"
  exit 1
fi
echo "[$(date --iso-8601=seconds)] local generation and semantics pass"
if bash scripts/chat_bridge/push_bridge_v3.sh; then
  echo "[$(date --iso-8601=seconds)] remote push and raw verification pass"
else
  echo "[$(date --iso-8601=seconds)] remote unavailable; retry remains armed"
fi
# Remote unavailability is expected retry state, not a broken timer service.
exit 0
