# ChatGPT-Codex Bridge Mirror

This is a safe standalone ChatGPT-Codex bridge mirror for the ACOR online reconstruction project.

It contains only project-state summary files and bridge scripts. It does not contain raw data, full results, original BBS source, protected code, or large per-read/per-prefix artifacts.

## Start Here

ChatGPT should first read:

`chat_bridge/00_README_FIRST.md`

## Current Latest Result

- latest result: `results/controlled_baseline_aware_cleanids_long_goal_20260704`
- latest final label: `CONTROLLED_CLEANIDS_NO_SMOKE_SIGNAL_FREEZE_CANDIDATES`

## Claim Boundary

可以说：

- SEIC 是一个 baseline-aware original framework attempt；
- SEIC toy 和 real-sync dry-run 有部分正信号；
- SEIC 未通过 smoke gate；
- VEMC method-card 停止；
- 当前仍没有 BBS-free independent decoder success。

不能说：

- 不能说找到 clean IDS decoder；
- 不能说 SEIC reconstruction quality success；
- 不能说 smoke/bounded/benchmark pass；
- 不能说 BBS 被替代；
- 不能把 refusal/low-confidence 当 success。

## Next Action

Revise the sync/global-search mechanism before any small reconstruction smoke; review gate matrix and failure taxonomy.

## If Linking From GitHub

If this mirror is pushed to a public GitHub repository, give ChatGPT the raw link:

`https://raw.githubusercontent.com/<USER>/<REPO>/main/chat_bridge/00_README_FIRST.md`

## If Uploading Directly

Upload `chat_bridge_feedback_package.zip` and tell ChatGPT:

Please read this chat_bridge package and update project state from `00_README_FIRST.md`.
