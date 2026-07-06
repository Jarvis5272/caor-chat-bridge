# ChatGPT-Codex Bridge Mirror

This is a safe standalone ChatGPT-Codex bridge mirror for the ACOR online reconstruction project.

It contains only project-state summary files and bridge scripts. It does not contain raw data, full results, original BBS source, protected code, or large per-read/per-prefix artifacts.

## Start Here

ChatGPT should first read:

`chat_bridge/00_README_FIRST.md`

## Current Latest Result

- latest result: `results/adaptive_quality_speed_pareto_explorer_wave4_20260706`
- latest final label: `PARETO_WAVE4_CONTINUE_REQUIRED_WITH_UNTESTED_FRONTIER`

## Claim Boundary

可以说：Wave4 必测 frontier CPES/RDIS/SWMC 已完成，且 Wave4 失败后自动验证了 Wave5 候选 PSEC/ISPC/WRMC；所有 tested candidates 都保持 observed-only selector、no BBS/EPBSD online、no reference online、no dataset route。可以说这些候选在 aggregate quality 上相对 best simple baseline 有小幅正信号。

不能说：不能 claim target success、不能 claim clean IDS realtime reconstruction algorithm found、不能 claim BBS replacement、不能把 source-gap/projected 正信号覆盖 BBS trio collapse、不能把 fallback/refusal 或 posterior-heavy replay 当作成功。当前 blocking reason 是 BBS trio group gate 与 safety gate 未通过，部分候选同时未达到 speed gate。

## Next Action

Continue only with the declared next Pareto frontier LPEC/SMPC/NESC from stage9_next_frontier.tsv; do not claim target success, BBS replacement, or clean IDS decoder found.

## If Linking From GitHub

If this mirror is pushed to a public GitHub repository, give ChatGPT the raw link:

`https://raw.githubusercontent.com/<USER>/<REPO>/main/chat_bridge/00_README_FIRST.md`

## If Uploading Directly

Upload `chat_bridge_feedback_package.zip` and tell ChatGPT:

Please read this chat_bridge package and update project state from `00_README_FIRST.md`.
