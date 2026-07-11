#!/usr/bin/env bash
set -u

ROOT=/home/hanlinxuan/research/ACOR-online-reconstruction
BRIDGE="$ROOT/chat_bridge"
EXPORT="$ROOT/chat_bridge_export"
RESULT="$ROOT/results/chat_bridge_v3_repair_20260711"
RAW_BASE=https://raw.githubusercontent.com/Jarvis5272/caor-chat-bridge/main
BRANCH=main
mkdir -p "$RESULT"
cd "$ROOT" || exit 1

STATUS_TSV="$RESULT/BRIDGE_PUSH_TRANSPORT_STATUS.tsv"
printf 'transport\tconfigured\tfetch_status\treconcile_status\tpush_status\traw_verify_status\terror_summary\n' > "$STATUS_TSV"

python scripts/chat_bridge/build_feedback_package.py --in chat_bridge --out chat_bridge_feedback_package.zip >/dev/null || exit 1
zip -T chat_bridge_feedback_package.zip >/dev/null || exit 1
python scripts/chat_bridge/refresh_bridge_export.py --bridge chat_bridge --package chat_bridge_feedback_package.zip --scripts scripts/chat_bridge --out chat_bridge_export >/dev/null || exit 1

git -C "$EXPORT" config user.name chat-bridge-bot
git -C "$EXPORT" config user.email chat-bridge-bot@example.local
git -C "$EXPORT" branch -M "$BRANCH"
git -C "$EXPORT" add .
if ! git -C "$EXPORT" diff --cached --quiet; then
  git -C "$EXPORT" commit -m "Bridge V3 paper pipeline snapshot" >/dev/null || exit 1
fi

sanitize_error() {
  tr '\r\n\t' '   ' < "$1" | sed -E 's#(https?://)[^/@ ]+@#\1<redacted>@#g' | cut -c1-500
}

reconcile_and_push() {
  transport="$1"; remote="$2"; ssh_command="$3"; configured="$4"
  err="$RESULT/push_${transport}.stderr"
  : > "$err"
  if [[ "$configured" != yes ]]; then
    printf '%s\tno\tskipped\tskipped\tskipped\tskipped\tcredential_not_configured\n' "$transport" >> "$STATUS_TSV"
    return 1
  fi
  git -C "$EXPORT" remote remove origin >/dev/null 2>&1 || true
  git -C "$EXPORT" remote add origin "$remote"
  if [[ -n "$ssh_command" ]]; then
    if ! timeout 40 env GIT_SSH_COMMAND="$ssh_command" git -C "$EXPORT" fetch origin "$BRANCH" >>"$err" 2>&1; then
      printf '%s\tyes\tfail\tskipped\tskipped\tskipped\t%s\n' "$transport" "$(sanitize_error "$err")" >> "$STATUS_TSV"; return 1
    fi
  else
    if ! timeout 40 env GIT_TERMINAL_PROMPT=0 git -C "$EXPORT" fetch origin "$BRANCH" >>"$err" 2>&1; then
      printf '%s\tyes\tfail\tskipped\tskipped\tskipped\t%s\n' "$transport" "$(sanitize_error "$err")" >> "$STATUS_TSV"; return 1
    fi
  fi
  reconcile=already_ahead
  if git -C "$EXPORT" show-ref --verify --quiet refs/remotes/origin/$BRANCH; then
    if git -C "$EXPORT" merge-base --is-ancestor origin/$BRANCH HEAD; then
      reconcile=fast_forward_push_safe
    elif git -C "$EXPORT" merge-base --is-ancestor HEAD origin/$BRANCH; then
      if git -C "$EXPORT" rebase origin/$BRANCH >>"$err" 2>&1; then reconcile=rebased_onto_remote; else git -C "$EXPORT" rebase --abort >/dev/null 2>&1 || true; printf '%s\tyes\tpass\tconflict\tskipped\tskipped\t%s\n' "$transport" "$(sanitize_error "$err")" >> "$STATUS_TSV"; return 1; fi
    else
      if git -C "$EXPORT" rebase origin/$BRANCH >>"$err" 2>&1; then reconcile=divergence_rebased; else git -C "$EXPORT" rebase --abort >/dev/null 2>&1 || true; printf '%s\tyes\tpass\tconflict\tskipped\tskipped\t%s\n' "$transport" "$(sanitize_error "$err")" >> "$STATUS_TSV"; return 1; fi
    fi
  fi
  if [[ -n "$ssh_command" ]]; then
    timeout 50 env GIT_SSH_COMMAND="$ssh_command" git -C "$EXPORT" push -u origin "$BRANCH" >>"$err" 2>&1
  else
    timeout 50 env GIT_TERMINAL_PROMPT=0 git -C "$EXPORT" push -u origin "$BRANCH" >>"$err" 2>&1
  fi
  if [[ $? -ne 0 ]]; then
    printf '%s\tyes\tpass\t%s\tfail\tskipped\t%s\n' "$transport" "$reconcile" "$(sanitize_error "$err")" >> "$STATUS_TSV"; return 1
  fi
  if ! python scripts/chat_bridge/validate_bridge_raw_v3.py --raw-base "$RAW_BASE" --bridge chat_bridge --out "$RESULT/RAW_BRIDGE_VERIFICATION.tsv" --retries 2 --retry-sleep 2 >>"$err" 2>&1; then
    printf '%s\tyes\tpass\t%s\tpass\tfail\t%s\n' "$transport" "$reconcile" "$(sanitize_error "$err")" >> "$STATUS_TSV"; return 1
  fi
  pushed_commit=$(git -C "$EXPORT" rev-parse HEAD)
  python scripts/chat_bridge/update_remote_sync_status_v3.py --bridge chat_bridge --status verified --verified true --transport "$transport" --commit "$pushed_commit" --error "" >/dev/null
  python scripts/chat_bridge/update_chat_bridge_v3.py --locked-result results/final_result_cross_validation_20260711 --out chat_bridge --audit-out results/chat_bridge_v3_repair_20260711 >/dev/null
  python scripts/chat_bridge/validate_bridge_semantics_v3.py --bridge chat_bridge --out "$RESULT/BRIDGE_V3_SEMANTIC_VALIDATION.tsv" >/dev/null || return 1
  python scripts/chat_bridge/build_feedback_package.py --in chat_bridge --out chat_bridge_feedback_package.zip >/dev/null
  python scripts/chat_bridge/refresh_bridge_export.py --bridge chat_bridge --package chat_bridge_feedback_package.zip --scripts scripts/chat_bridge --out chat_bridge_export >/dev/null
  git -C "$EXPORT" add .
  if ! git -C "$EXPORT" diff --cached --quiet; then git -C "$EXPORT" commit -m "Mark Bridge V3 remote verified via $transport" >/dev/null || return 1; fi
  if [[ -n "$ssh_command" ]]; then timeout 50 env GIT_SSH_COMMAND="$ssh_command" git -C "$EXPORT" push -u origin "$BRANCH" >>"$err" 2>&1; else timeout 50 env GIT_TERMINAL_PROMPT=0 git -C "$EXPORT" push -u origin "$BRANCH" >>"$err" 2>&1; fi
  if [[ $? -ne 0 ]]; then printf '%s\tyes\tpass\t%s\tstatus_push_fail\tpass_first_commit\t%s\n' "$transport" "$reconcile" "$(sanitize_error "$err")" >> "$STATUS_TSV"; return 1; fi
  if ! python scripts/chat_bridge/validate_bridge_raw_v3.py --raw-base "$RAW_BASE" --bridge chat_bridge --out "$RESULT/RAW_BRIDGE_VERIFICATION.tsv" --retries 3 --retry-sleep 3 >>"$err" 2>&1; then printf '%s\tyes\tpass\t%s\tpass\tfail_after_status\t%s\n' "$transport" "$reconcile" "$(sanitize_error "$err")" >> "$STATUS_TSV"; return 1; fi
  printf '%s\tyes\tpass\t%s\tpass\tpass\t\n' "$transport" "$reconcile" >> "$STATUS_TSV"
  return 0
}

https_configured=no
if gh auth status -h github.com >/dev/null 2>&1 || [[ -n "$(git config --global --get credential.helper 2>/dev/null || true)" ]]; then https_configured=yes; fi
key="$HOME/.ssh/caor_chat_bridge_ed25519"
ssh_configured=no; [[ -f "$key" ]] && ssh_configured=yes

if reconcile_and_push https "https://github.com/Jarvis5272/caor-chat-bridge.git" "" "$https_configured"; then exit 0; fi
if reconcile_and_push ssh443 "ssh://git@ssh.github.com:443/Jarvis5272/caor-chat-bridge.git" "ssh -i $key -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new -o ConnectTimeout=15" "$ssh_configured"; then exit 0; fi
if reconcile_and_push ssh22 "git@github.com:Jarvis5272/caor-chat-bridge.git" "ssh -i $key -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new -o ConnectTimeout=15" "$ssh_configured"; then exit 0; fi

summary=$(tail -n +2 "$STATUS_TSV" | tr '\n' ';' | cut -c1-450)
python scripts/chat_bridge/update_remote_sync_status_v3.py --bridge chat_bridge --status retry_armed --verified false --transport none --commit pending --error "$summary" >/dev/null
python scripts/chat_bridge/update_chat_bridge_v3.py --locked-result results/final_result_cross_validation_20260711 --out chat_bridge --audit-out results/chat_bridge_v3_repair_20260711 >/dev/null
exit 1
