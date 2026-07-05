# ChatGPT-Codex Bridge Snapshot

## 当前项目一句话目标

在 ACOR / clean IDS / baseline-aware original algorithm 研究中，用小型、可审查的状态快照让 ChatGPT 读取 Codex 的最新结果、claim boundary 和下一步。

## 当前主线状态

最新自动检测结果为 `results/spwic_identity_certificate_toy_only_prototype_20260704`；当前最新 Codex label 为 `SPWIC_TOY_PASS_GO_TO_REAL_DATA_SYNC_DRYRUN`。当前 bridge 初始化状态为 `CHAT_BRIDGE_WORKFLOW_INITIALIZED`。

## 最新 Codex final label

`SPWIC_TOY_PASS_GO_TO_REAL_DATA_SYNC_DRYRUN`

## 最新输出目录

`results/spwic_identity_certificate_toy_only_prototype_20260704`

## ChatGPT 应先读哪些文件

- chat_bridge/00_README_FIRST.md
- chat_bridge/01_CURRENT_STATE_CN.md
- chat_bridge/02_LATEST_CODEX_RESULT.json
- chat_bridge/04_ACTIVE_CLAIM_BOUNDARY_CN.md
- chat_bridge/05_NEXT_ACTION_CN.md
- chat_bridge/09_SYNC_STATUS.tsv

## 当前 claim boundary

可以说：SPWIC toy-only prototype 在 48 toy cases 上通过 gate，constructive recovery 非零且 S/I/D/LD 都出现，harmful traps 被拒绝，high-confidence wrong 为 0。

不能说：不能说 real-data proven、small smoke allowed、benchmark success、clean IDS decoder success。

## 是否有 missing context

`missing_expected_files=[]`。这些缺失项只作为上下文缺口记录；若 required bridge files 全部生成，则不阻塞 bridge 使用。

## 当前下一步

SPWIC real-data sync dry-run is allowed next with explicit user approval; no small reconstruction smoke, benchmark, or algorithm success claim.

## protected diff 状态

`protected_files_modified=no`。本 bridge 任务只写入 `chat_bridge/` 和 `scripts/chat_bridge/`。

## original BBS source 状态

`original_bbs_source_modified=no`。本 bridge 任务未写入 `../bbs-src` 或 BBS source。
