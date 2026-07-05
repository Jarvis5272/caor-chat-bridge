# ChatGPT-Codex Bridge Mirror

This is a safe standalone ChatGPT-Codex bridge mirror for the ACOR online reconstruction project.

It contains only project-state summary files and bridge scripts. It does not contain raw data, full results, original BBS source, protected code, or large per-read/per-prefix artifacts.

## Start Here

ChatGPT should first read:

`chat_bridge/00_README_FIRST.md`

## Current Latest Result

- latest result: `results/sipc_sparse_identity_path_consistency_toy_only_prototype_20260705`
- latest final label: `SIPC_TOY_PASS_GO_TO_REAL_DATA_SYNC_DRYRUN`

## Claim Boundary

Online SIPC sees only observed toy reads. Hidden targets and edit metrics are used only after Decode for offline audit. The prototype does not call or read BBS, does not use BBS score/beam/path likelihood, does not use EPBSD, and does not build POA/full graph/full alignment.

## Next Action

Revise the sync/global-search mechanism before any small reconstruction smoke; review gate matrix and failure taxonomy.

## If Linking From GitHub

If this mirror is pushed to a public GitHub repository, give ChatGPT the raw link:

`https://raw.githubusercontent.com/<USER>/<REPO>/main/chat_bridge/00_README_FIRST.md`

## If Uploading Directly

Upload `chat_bridge_feedback_package.zip` and tell ChatGPT:

Please read this chat_bridge package and update project state from `00_README_FIRST.md`.
