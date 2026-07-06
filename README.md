# ChatGPT-Codex Bridge Mirror

This is a safe standalone ChatGPT-Codex bridge mirror for the ACOR online reconstruction project.

It contains only project-state summary files and bridge scripts. It does not contain raw data, full results, original BBS source, protected code, or large per-read/per-prefix artifacts.

## Start Here

ChatGPT should first read:

`chat_bridge/00_README_FIRST.md`

## Current Latest Result

- latest result: `results/adaptive_quality_speed_pareto_explorer_wave6_20260706`
- latest final label: `PARETO_WAVE6_CONTINUE_REQUIRED_WITH_UNTESTED_FRONTIER`

## Claim Boundary

可以说：Wave6 必测 frontier LPEC/SMPC/NESC 已完成，且 Wave6 失败后自动验证了 Wave7 候选 BLMC/TMIC/PSCF；所有 tested candidates 都保持 observed-only selector、no BBS/EPBSD online、no reference online、no dataset route。可以报告 absolute quality/speed/group/safety 表和每个候选的 gate failure。

不能说：不能 claim target success、不能 claim clean IDS realtime reconstruction algorithm found、不能 claim BBS replacement、不能把 aggregate 正信号覆盖 BBS trio collapse、不能把 fallback/refusal 或 posterior-heavy replay 当作成功。当前 blocking reason 以 BBS trio group gate / safety gate / speed gate 为准。

## Next Action

Continue only with the declared next Pareto frontier EPCM/DDSC/NRCM from stage9_next_frontier.tsv; do not claim target success, BBS replacement, or clean IDS decoder found.

## If Linking From GitHub

If this mirror is pushed to a public GitHub repository, give ChatGPT the raw link:

`https://raw.githubusercontent.com/<USER>/<REPO>/main/chat_bridge/00_README_FIRST.md`

## If Uploading Directly

Upload `chat_bridge_feedback_package.zip` and tell ChatGPT:

Please read this chat_bridge package and update project state from `00_README_FIRST.md`.
