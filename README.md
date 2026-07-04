# ChatGPT-Codex Bridge Mirror

This is a safe standalone ChatGPT-Codex bridge mirror for the ACOR online reconstruction project.

It contains only project-state summary files and bridge scripts. It does not contain raw data, full results, original BBS source, protected code, or large per-read/per-prefix artifacts.

## Start Here

ChatGPT should first read:

`chat_bridge/00_README_FIRST.md`

## Current Latest Result

- latest result: `results/baepc_toy_only_prototype_20260704`
- latest final label: `BAEPC_TOY_PASS_GO_TO_REAL_DATA_SYNC_DRYRUN`

## Claim Boundary

Online state machine 只读取 observed reads。Hidden target 只在 offline toy audit 中用于 ED/exact。没有 BBS output、BBS score/beam/pruning/path likelihood、EPBSD kernel、STWC/CAOR core、dataset/source route、full alignment、POA 或 graph。

## Next Action

Revise the sync/global-search mechanism before any small reconstruction smoke; review gate matrix and failure taxonomy.

## If Linking From GitHub

If this mirror is pushed to a public GitHub repository, give ChatGPT the raw link:

`https://raw.githubusercontent.com/<USER>/<REPO>/main/chat_bridge/00_README_FIRST.md`

## If Uploading Directly

Upload `chat_bridge_feedback_package.zip` and tell ChatGPT:

Please read this chat_bridge package and update project state from `00_README_FIRST.md`.
