# ChatGPT-Codex Bridge Snapshot

## 当前项目一句话目标

在 ACOR / clean IDS / baseline-aware original algorithm 研究中，用小型、可审查的状态快照让 ChatGPT 读取 Codex 的最新结果、claim boundary 和下一步。

## 当前主线状态

最新自动检测结果为 `results/pareto_run_to_completion_controller_20260706`；当前最新 Codex label 为 `PARETO_RUN_RESOURCE_CHECKPOINT_RESUME_REQUIRED`。当前 bridge 初始化状态为 `CHAT_BRIDGE_WORKFLOW_INITIALIZED`。

## 最新 Codex final label

`PARETO_RUN_RESOURCE_CHECKPOINT_RESUME_REQUIRED`

## 最新输出目录

`results/pareto_run_to_completion_controller_20260706`

## ChatGPT 应先读哪些文件

- chat_bridge/00_README_FIRST.md
- chat_bridge/01_CURRENT_STATE_CN.md
- chat_bridge/02_LATEST_CODEX_RESULT.json
- chat_bridge/04_ACTIVE_CLAIM_BOUNDARY_CN.md
- chat_bridge/05_NEXT_ACTION_CN.md
- chat_bridge/09_SYNC_STATUS.tsv

## 当前 claim boundary

可以说：PIMC/DRPC/CENF 已完成，且失败后自动验证了 BLEM/PSWP/NEDP/CSWRC/SDWMDP/ALHC/TMICNE；所有 tested candidates 都保持 observed-only selector、no BBS/EPBSD online、no reference online、no dataset route。可以报告 absolute quality/speed/group/safety 表和每个候选的 gate failure。

不能说：不能 claim target success、不能 claim clean IDS realtime reconstruction algorithm found、不能 claim BBS replacement、不能把 aggregate 正信号覆盖 BBS trio collapse、不能把 fallback/refusal 或 posterior-heavy replay 当作成功。当前 blocking reason 以 BBS trio group gate / safety gate / speed gate 为准。

## 是否有 missing context

`missing_expected_files=[]`。这些缺失项只作为上下文缺口记录；若 required bridge files 全部生成，则不阻塞 bridge 使用。

## 当前下一步

Resume the run-to-completion Pareto controller with the command in controller_state.json or stageF_next_command_recommendation.md; current tested candidates are frozen and target success is not claimed.

## protected diff 状态

`protected_files_modified=no`。本 bridge 任务只写入 `chat_bridge/` 和 `scripts/chat_bridge/`。

## original BBS source 状态

`original_bbs_source_modified=no`。本 bridge 任务未写入 `../bbs-src` 或 BBS source。
