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

可以说：PIMC/DRPC/CENF 已完成，且失败后自动验证了 BLEM/PSWP/NEDP/CSWRC/SDWMDP/ALHC/TMICNE；所有 tested candidates 都保持 observed-only selector、no BBS/EPBSD online、no reference online、no dataset route。可以报告 absolute quality/speed/group/safety 表和每个候选的 gate failure。

不能说：不能 claim target success、不能 claim clean IDS realtime reconstruction algorithm found、不能 claim BBS replacement、不能把 aggregate 正信号覆盖 BBS trio collapse、不能把 fallback/refusal 或 posterior-heavy replay 当作成功。当前 blocking reason 以 BBS trio group gate / safety gate / speed gate 为准。

## Next Action

Resume the run-to-completion Pareto controller with the command in controller_state.json or stageF_next_command_recommendation.md; current tested candidates are frozen and target success is not claimed.

## If Linking From GitHub

If this mirror is pushed to a public GitHub repository, give ChatGPT the raw link:

`https://raw.githubusercontent.com/<USER>/<REPO>/main/chat_bridge/00_README_FIRST.md`

## If Uploading Directly

Upload `chat_bridge_feedback_package.zip` and tell ChatGPT:

Please read this chat_bridge package and update project state from `00_README_FIRST.md`.
