# ChatGPT-Codex Bridge Snapshot

## 当前项目一句话目标

在 ACOR / clean IDS / baseline-aware original algorithm 研究中，用小型、可审查的状态快照让 ChatGPT 读取 Codex 的最新结果、claim boundary 和下一步。

## 当前主线状态

最新自动检测结果为 `results/scc_sparse_consistency_certificate_theory_note_20260705`；当前最新 Codex label 为 `SCC_THEORY_READY_FOR_HAND_TOY`。当前 bridge 初始化状态为 `CHAT_BRIDGE_WORKFLOW_INITIALIZED`。

## 最新 Codex final label

`SCC_THEORY_READY_FOR_HAND_TOY`

## 最新输出目录

`results/scc_sparse_consistency_certificate_theory_note_20260705`

## ChatGPT 应先读哪些文件

- chat_bridge/00_README_FIRST.md
- chat_bridge/01_CURRENT_STATE_CN.md
- chat_bridge/02_LATEST_CODEX_RESULT.json
- chat_bridge/04_ACTIVE_CLAIM_BOUNDARY_CN.md
- chat_bridge/05_NEXT_ACTION_CN.md
- chat_bridge/09_SYNC_STATUS.tsv

## 当前 claim boundary

An event `e` may be accepted only if:

1. paired witness unique；
2. bounded counterfactual delta over no-event and bounded competitors is at least `m`；
3. cross-read order consistency support exceeds `m`；
4. no competing certificate has comparable or stronger dominance；
5. independent support exceeds `m`；
6. all checks stay within `a/W` and the competitor registry remains sparse.

If any condition fails, SCC must output low-confidence/no correction or stop. It cannot widen W, add helper families, use graph/POA/full alignment, or call BBS/EPBSD semantics.


SCC is not guaranteed to cover all useful edits. It has coverage when true edits often have unique sparse identity and positive local counterfactual margin. It becomes refusal-only in repeats, homopolymers, low coverage, cost ties, competing certificate ties, and long-range ambiguity. These cases are not patched; they are reported.

## 是否有 missing context

`missing_expected_files=[]`。这些缺失项只作为上下文缺口记录；若 required bridge files 全部生成，则不阻塞 bridge 使用。

## 当前下一步

Revise the sync/global-search mechanism before any small reconstruction smoke; review gate matrix and failure taxonomy.

## protected diff 状态

`protected_files_modified=no`。本 bridge 任务只写入 `chat_bridge/` 和 `scripts/chat_bridge/`。

## original BBS source 状态

`original_bbs_source_modified=no`。本 bridge 任务未写入 `../bbs-src` 或 BBS source。
