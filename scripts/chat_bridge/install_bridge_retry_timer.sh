#!/usr/bin/env bash
set -euo pipefail
ROOT=/home/hanlinxuan/research/ACOR-online-reconstruction
USER_DIR="$HOME/.config/systemd/user"
mkdir -p "$USER_DIR"
if systemctl --user show-environment >/dev/null 2>&1; then
  install -m 0644 "$ROOT/scripts/chat_bridge/caor-chat-bridge-sync.service" "$USER_DIR/caor-chat-bridge-sync.service"
  install -m 0644 "$ROOT/scripts/chat_bridge/caor-chat-bridge-sync.timer" "$USER_DIR/caor-chat-bridge-sync.timer"
  systemctl --user daemon-reload
  systemctl --user enable --now caor-chat-bridge-sync.timer
  systemctl --user status caor-chat-bridge-sync.timer --no-pager || true
  exit 0
fi
echo "systemd --user unavailable. Suggested user crontab entry:" >&2
echo "*/10 * * * * /usr/bin/flock -n /tmp/caor-chat-bridge-sync-cron.lock /bin/bash $ROOT/scripts/chat_bridge/retry_remote_sync.sh >> $ROOT/results/chat_bridge_v3_repair_20260711/cron_retry.log 2>&1" >&2
exit 2
