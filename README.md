# ChatGPT-Codex Bridge Mirror

This is a safe standalone ChatGPT-Codex bridge mirror for the ACOR online reconstruction project.

It contains only project-state summary files and bridge scripts. It does not contain raw data, full results, original BBS source, protected code, or large per-read/per-prefix artifacts.

## Start Here

ChatGPT should first read:

`chat_bridge/00_README_FIRST.md`

## Current Latest Result

- latest result: `results/final_result_cross_validation_20260711`
- latest final label: `FINAL_RESULT_CROSS_VALIDATION_PASS_AND_NUMBERS_LOCKED`

## Claim Boundary

Can use:
- locked CAPPED_17_MATCHED scope
- locked Accuracy / Exact / Mean ED
- locked end-to-end current-method runtime and Prefix/s
- 100% determinism across 9 reruns and workers
- no-leakage PASS
- online prefix-only protocol

Cannot use yet:
- retired 63.3 / 9.6 / 5.3 runtime
- old speedup values
- baseline speedup not rerun under the same end-to-end boundary
- full-source scalability
- parameter sensitivity, ablation, confidence calibration, or new large-scale results

## Next Action

review and paper-sync the locked oligo0 full-source result; do not start medium or large without an explicit task

## If Linking From GitHub

If this mirror is pushed to a public GitHub repository, give ChatGPT the raw link:

`https://raw.githubusercontent.com/<USER>/<REPO>/main/chat_bridge/LATEST_FOR_CHATGPT.md`

## If Uploading Directly

Upload `chat_bridge_feedback_package.zip` and tell ChatGPT:

Please read this chat_bridge package and update project state from `LATEST_FOR_CHATGPT.md`.
