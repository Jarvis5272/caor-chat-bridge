#!/usr/bin/env bash
set -euo pipefail
USER_DIR="$HOME/.config/systemd/user"
systemctl --user disable --now caor-chat-bridge-sync.timer >/dev/null 2>&1 || true
rm -f "$USER_DIR/caor-chat-bridge-sync.timer" "$USER_DIR/caor-chat-bridge-sync.service"
systemctl --user daemon-reload >/dev/null 2>&1 || true
echo "ACOR bridge retry timer removed."
