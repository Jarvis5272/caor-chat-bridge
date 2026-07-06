# ChatGPT-Codex Bridge Snapshot

## 当前项目一句话目标

在 ACOR / clean IDS / baseline-aware original algorithm 研究中，用小型、可审查的状态快照让 ChatGPT 读取 Codex 的最新结果、claim boundary 和下一步。

## 当前主线状态

最新自动检测结果为 `results/cgbapc_speed_decisive_validation_20260706`；当前最新 Codex label 为 `CGBAPC_FAIL_WRAPPER_OR_REFUSAL`。当前 bridge 初始化状态为 `CHAT_BRIDGE_WORKFLOW_INITIALIZED_WITH_MISSING_CONTEXT`。

## 最新 Codex final label

`CGBAPC_FAIL_WRAPPER_OR_REFUSAL`

## 最新输出目录

`results/cgbapc_speed_decisive_validation_20260706`

## ChatGPT 应先读哪些文件

- chat_bridge/00_README_FIRST.md
- chat_bridge/01_CURRENT_STATE_CN.md
- chat_bridge/02_LATEST_CODEX_RESULT.json
- chat_bridge/04_ACTIVE_CLAIM_BOUNDARY_CN.md
- chat_bridge/05_NEXT_ACTION_CN.md
- chat_bridge/09_SYNC_STATUS.tsv

## 当前 claim boundary

可以说：CGBAPC 是当前 BAPC 线上最强 PostGate quality signal，且 previous PostGate 修复了 BBS trio collapse。

不能说：CGBAPC 达到 realtime speed target；不能说 cheap PreGate 已经成功；不能说这是 BBS/EPBSD 替代；不能把 PostGate 写成 PreGate。

## 是否有 missing context

`missing_expected_files=['FINAL*_REPORT_CN.md']`。这些缺失项只作为上下文缺口记录；若 required bridge files 全部生成，则不阻塞 bridge 使用。

## 当前下一步

Revise the sync/global-search mechanism before any small reconstruction smoke; review gate matrix and failure taxonomy.

## protected diff 状态

`protected_files_modified=unknown`。本 bridge 任务只写入 `chat_bridge/` 和 `scripts/chat_bridge/`。

## original BBS source 状态

`original_bbs_source_modified=unknown`。本 bridge 任务未写入 `../bbs-src` 或 BBS source。
