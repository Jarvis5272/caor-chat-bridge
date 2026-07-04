# ChatGPT-Codex Bridge Snapshot

## 当前项目一句话目标

在 ACOR / clean IDS / BBS-free 同步重建研究中，用小型、可审查的状态快照让 ChatGPT 读取 Codex 的最新结果、claim boundary 和下一步。

## 当前主线状态

最新自动检测结果为 `results/tpc_ocwp_real_data_validation_20260704`；当前最新 Codex label 为 `TPC_OCWP_REAL_SYNC_STOP_GLOBAL_SEARCH_REQUIRED`。当前 bridge 初始化状态为 `CHAT_BRIDGE_WORKFLOW_INITIALIZED_WITH_MISSING_CONTEXT`。

## 最新 Codex final label

`TPC_OCWP_REAL_SYNC_STOP_GLOBAL_SEARCH_REQUIRED`

## 最新输出目录

`results/tpc_ocwp_real_data_validation_20260704`

## ChatGPT 应先读哪些文件

- chat_bridge/00_README_FIRST.md
- chat_bridge/01_CURRENT_STATE_CN.md
- chat_bridge/02_LATEST_CODEX_RESULT.json
- chat_bridge/04_ACTIVE_CLAIM_BOUNDARY_CN.md
- chat_bridge/05_NEXT_ACTION_CN.md
- chat_bridge/09_SYNC_STATUS.tsv

## 当前 claim boundary

This is a BBS-free sync dry-run. It does not claim reconstruction benchmark quality. Low-confidence/refusal is not counted as decoder success.

## 是否有 missing context

`missing_expected_files=['FINAL*_REPORT_CN.md', 'final_decision_matrix.tsv']`。这些缺失项只作为上下文缺口记录；若 required bridge files 全部生成，则不阻塞 bridge 使用。

## 当前下一步

Revise the sync/global-search mechanism before any small reconstruction smoke; review gate matrix and failure taxonomy.

## protected diff 状态

`protected_files_modified=no`。本 bridge 任务只写入 `chat_bridge/` 和 `scripts/chat_bridge/`。

## original BBS source 状态

`original_bbs_source_modified=no`。本 bridge 任务未写入 `../bbs-src` 或 BBS source。
