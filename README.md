# ChatGPT-Codex Bridge Mirror

This is a safe standalone ChatGPT-Codex bridge mirror for the ACOR online reconstruction project.

It contains only project-state summary files and bridge scripts. It does not contain raw data, full results, original BBS source, protected code, or large per-read/per-prefix artifacts.

## Start Here

ChatGPT should first read:

`chat_bridge/00_README_FIRST.md`

## Current Latest Result

- latest result: `results/pareto_run_to_completion_controller_20260706`
- latest final label: `PARETO_RUN_RESOURCE_CHECKPOINT_RESUME_REQUIRED`

## Claim Boundary

可以说：QGEC/BLCM/ONRC 已按 checkpoint 验证，并新增 anti-degenerate audit；duplicate/degenerate 候选不计入有效探索。

不能说：不能 claim target success、不能 claim BBS replacement、不能用 speed-only 或 aggregate 正信号遮盖 BBS trio/safety/originality failure。

## Next Action

Resume the run-to-completion Pareto controller with the command in controller_state.json or stageF_next_command_recommendation.md; current tested candidates are frozen and target success is not claimed.

## If Linking From GitHub

If this mirror is pushed to a public GitHub repository, give ChatGPT the raw link:

`https://raw.githubusercontent.com/<USER>/<REPO>/main/chat_bridge/00_README_FIRST.md`

## If Uploading Directly

Upload `chat_bridge_feedback_package.zip` and tell ChatGPT:

Please read this chat_bridge package and update project state from `00_README_FIRST.md`.
