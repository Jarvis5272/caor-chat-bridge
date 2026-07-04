# ChatGPT-Codex Bridge Snapshot

## 当前项目一句话目标

在 ACOR / clean IDS / baseline-aware original algorithm 研究中，用小型、可审查的状态快照让 ChatGPT 读取 Codex 的最新结果、claim boundary 和下一步。

## 当前主线状态

最新自动检测结果为 `results/edit_event_identity_certificate_synthesis_20260704`；当前最新 Codex label 为 `IDENTITY_CERTIFICATE_READY_FOR_HAND_TOY`。当前 bridge 初始化状态为 `CHAT_BRIDGE_WORKFLOW_INITIALIZED_WITH_MISSING_CONTEXT`。

## 最新 Codex final label

`IDENTITY_CERTIFICATE_READY_FOR_HAND_TOY`

## 最新输出目录

`results/edit_event_identity_certificate_synthesis_20260704`

## ChatGPT 应先读哪些文件

- chat_bridge/00_README_FIRST.md
- chat_bridge/01_CURRENT_STATE_CN.md
- chat_bridge/02_LATEST_CODEX_RESULT.json
- chat_bridge/04_ACTIVE_CLAIM_BOUNDARY_CN.md
- chat_bridge/05_NEXT_ACTION_CN.md
- chat_bridge/09_SYNC_STATUS.tsv

## 当前 claim boundary

可以说：

- 当前 independent decoder 仍未找到；
- SEIC/VEMC 冻结；
- 当前核心数学问题是 event identity certificate；
- SPWIC 是值得进入 hand toy 的 certificate 候选。

不能说：

- 不能说 SPWIC 是算法成功；
- 不能说可以进入 toy prototype / real-sync / smoke；
- 不能说 BBS-free decoder found；
- 不能说 SEIC/VEMC 可以继续 patch；
- 不能把 refusal 当 success。

## 是否有 missing context

`missing_expected_files=['FINAL*_REPORT_CN.md', 'leakage_audit.tsv']`。这些缺失项只作为上下文缺口记录；若 required bridge files 全部生成，则不阻塞 bridge 使用。

## 当前下一步

Run SPWIC hand toy only with explicit approval; no code, toy prototype, real-data sync, smoke, benchmark, SEIC patching, or BBS/EPBSD semantics.

## protected diff 状态

`protected_files_modified=no`。本 bridge 任务只写入 `chat_bridge/` 和 `scripts/chat_bridge/`。

## original BBS source 状态

`original_bbs_source_modified=no`。本 bridge 任务未写入 `../bbs-src` 或 BBS source。
