# ChatGPT-Codex Bridge Snapshot

## 当前项目一句话目标

在 ACOR / clean IDS / baseline-aware original algorithm 研究中，用小型、可审查的状态快照让 ChatGPT 读取 Codex 的最新结果、claim boundary 和下一步。

## 当前主线状态

服务器显式结果为 `results/pareto_run_to_completion_controller_20260706`；当前最新 Codex label 为 `PARETO_RUN_RESOURCE_CHECKPOINT_RESUME_REQUIRED`。当前 bridge 初始化状态为 `CHAT_BRIDGE_WORKFLOW_INITIALIZED`。

## 项目状态源

服务器 `chat_bridge/`、服务器 `results/` 及本 bridge 的 GitHub raw mirror 是唯一项目状态源。聊天上传附件和旧聊天上下文不具权威性，也不得覆盖本页的显式 latest result。

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

可以说：QGEC/BLCM/ONRC 已按 checkpoint 验证，并新增 anti-degenerate audit；duplicate/degenerate 候选不计入有效探索。

不能说：不能 claim target success、不能 claim BBS replacement、不能用 speed-only 或 aggregate 正信号遮盖 BBS trio/safety/originality failure。

## 是否有 missing context

`missing_expected_files=[]`。这些缺失项只作为上下文缺口记录；若 required bridge files 全部生成，则不阻塞 bridge 使用。

## 当前下一步

Resume the run-to-completion Pareto controller with the command in controller_state.json or stageF_next_command_recommendation.md; current tested candidates are frozen and target success is not claimed.

## protected diff 状态

`protected_files_modified=no`。本 bridge 任务只写入 `chat_bridge/` 和 `scripts/chat_bridge/`。

## original BBS source 状态

`original_bbs_source_modified=no`。本 bridge 任务未写入 `../bbs-src` 或 BBS source。
