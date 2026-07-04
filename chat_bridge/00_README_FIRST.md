# ChatGPT-Codex Bridge Snapshot

## 当前项目一句话目标

在 ACOR / clean IDS / baseline-aware original algorithm 研究中，用小型、可审查的状态快照让 ChatGPT 读取 Codex 的最新结果、claim boundary 和下一步。

## 当前主线状态

最新自动检测结果为 `results/spwic_identity_certificate_hand_toy_20260704`；当前最新 Codex label 为 `SPWIC_HAND_TOY_PASS_GO_TO_TOY_ONLY_PROTOTYPE`。当前 bridge 初始化状态为 `CHAT_BRIDGE_WORKFLOW_INITIALIZED_WITH_MISSING_CONTEXT`。

## 最新 Codex final label

`SPWIC_HAND_TOY_PASS_GO_TO_TOY_ONLY_PROTOTYPE`

## 最新输出目录

`results/spwic_identity_certificate_hand_toy_20260704`

## ChatGPT 应先读哪些文件

- chat_bridge/00_README_FIRST.md
- chat_bridge/01_CURRENT_STATE_CN.md
- chat_bridge/02_LATEST_CODEX_RESULT.json
- chat_bridge/04_ACTIVE_CLAIM_BOUNDARY_CN.md
- chat_bridge/05_NEXT_ACTION_CN.md
- chat_bridge/09_SYNC_STATUS.tsv

## 当前 claim boundary

可以说：

- SPWIC hand toy 规则具体；
- hand toy 上有 9 个 constructive recovery；
- S/I/D 都有；
- harmful residual traps 被拒绝；
- 非唯一 witness low-confidence；
- no full alignment / graph / BBS / EPBSD semantics。

不能说：

- 不能说 SPWIC 是算法成功；
- 不能说 toy prototype 已通过；
- 不能说 real-data 成功；
- 不能说 smoke/benchmark 允许；
- 不能把 low-confidence 当 success。

下一步只允许 toy-only prototype，并且需要用户明确批准。

## 是否有 missing context

`missing_expected_files=['FINAL*_REPORT_CN.md', 'leakage_audit.tsv']`。这些缺失项只作为上下文缺口记录；若 required bridge files 全部生成，则不阻塞 bridge 使用。

## 当前下一步

Toy-only prototype is allowed next with explicit user approval; no real-data dry-run, smoke, or benchmark.

## protected diff 状态

`protected_files_modified=no`。本 bridge 任务只写入 `chat_bridge/` 和 `scripts/chat_bridge/`。

## original BBS source 状态

`original_bbs_source_modified=no`。本 bridge 任务未写入 `../bbs-src` 或 BBS source。
