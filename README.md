# ChatGPT-Codex Bridge Mirror

This is a safe standalone ChatGPT-Codex bridge mirror for the ACOR online reconstruction project.

It contains only project-state summary files and bridge scripts. It does not contain raw data, full results, original BBS source, protected code, or large per-read/per-prefix artifacts.

## Start Here

ChatGPT should first read:

`chat_bridge/00_README_FIRST.md`

## Current Latest Result

- latest result: `results/final_full_17dataset_baseline_benchmark_20260707`
- latest final label: `FINAL_CAPPED_17_EXTERNAL_BASELINE_AUDITED_ITR_BACKGROUND`

## Claim Boundary

CGBAPC/BAPC excluded from main table — per user instruction. These are internal pipeline/intermediate algorithms, NOT external baselines. Moved to excluded_internal_methods.tsv.

All 38 internal Pareto exploration candidates (ACDC/DICEC/TICEC/GLICE/CECC + waves 10-20) excluded from main table. See FROZEN_HISTORY.tsv and excluded_internal_methods.tsv.

## Next Action

Review latest result artifacts and confirm whether another validation step is warranted.

## If Linking From GitHub

If this mirror is pushed to a public GitHub repository, give ChatGPT the raw link:

`https://raw.githubusercontent.com/<USER>/<REPO>/main/chat_bridge/00_README_FIRST.md`

## If Uploading Directly

Upload `chat_bridge_feedback_package.zip` and tell ChatGPT:

Please read this chat_bridge package and update project state from `00_README_FIRST.md`.
