# ChatGPT-Codex Bridge Mirror

This is a safe standalone ChatGPT-Codex bridge mirror for the ACOR online reconstruction project.

It contains only project-state summary files and bridge scripts. It does not contain raw data, full results, original BBS source, protected code, or large per-read/per-prefix artifacts.

## Start Here

ChatGPT should first read:

`chat_bridge/00_README_FIRST.md`

## Current Latest Result

- latest result: `results/spwic_identity_certificate_toy_only_prototype_20260704`
- latest final label: `SPWIC_TOY_PASS_GO_TO_REAL_DATA_SYNC_DRYRUN`

## Claim Boundary

可以说：SPWIC toy-only prototype 在 48 toy cases 上通过 gate，constructive recovery 非零且 S/I/D/LD 都出现，harmful traps 被拒绝，high-confidence wrong 为 0。

不能说：不能说 real-data proven、small smoke allowed、benchmark success、clean IDS decoder success。

## Next Action

Revise the sync/global-search mechanism before any small reconstruction smoke; review gate matrix and failure taxonomy.

## If Linking From GitHub

If this mirror is pushed to a public GitHub repository, give ChatGPT the raw link:

`https://raw.githubusercontent.com/<USER>/<REPO>/main/chat_bridge/00_README_FIRST.md`

## If Uploading Directly

Upload `chat_bridge_feedback_package.zip` and tell ChatGPT:

Please read this chat_bridge package and update project state from `00_README_FIRST.md`.
