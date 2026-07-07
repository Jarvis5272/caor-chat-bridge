# ChatGPT-Codex Bridge Snapshot

## 当前项目一句话目标

在 ACOR / clean IDS / baseline-aware original algorithm 研究中，用小型、可审查的状态快照让 ChatGPT 读取 Codex 的最新结果、claim boundary 和下一步。

## 当前主线状态

服务器显式结果为 `results/final_full_17dataset_baseline_benchmark_20260707`；当前最新 Codex label 为 `FINAL_FULL_17DATASET_BASELINE_COMPLETE`。当前 bridge 初始化状态为 `CHAT_BRIDGE_WORKFLOW_INITIALIZED_WITH_MISSING_CONTEXT`。

## 项目状态源

服务器 `chat_bridge/`、服务器 `results/` 及本 bridge 的 GitHub raw mirror 是唯一项目状态源。聊天上传附件和旧聊天上下文不具权威性，也不得覆盖本页的显式 latest result。

## 最新 Codex final label

`FINAL_FULL_17DATASET_BASELINE_COMPLETE`

## 最新输出目录

`results/final_full_17dataset_baseline_benchmark_20260707`

## ChatGPT 应先读哪些文件

- chat_bridge/00_README_FIRST.md
- chat_bridge/01_CURRENT_STATE_CN.md
- chat_bridge/02_LATEST_CODEX_RESULT.json
- chat_bridge/04_ACTIVE_CLAIM_BOUNDARY_CN.md
- chat_bridge/05_NEXT_ACTION_CN.md
- chat_bridge/09_SYNC_STATUS.tsv

## 当前 claim boundary

### 可以说 (Can claim):
- On 17 datasets same-scope, our BBS-free realtime method achieves accuracy 0.9660 (between kmer_medoid 0.9663 and BBS 0.9698)
- Our method is 7.6× faster than BBS and 5.5× faster than CGBAPC (796 vs 105 vs 146 prefix/s)
- Our method is BBS-free, reference-free, online-only decode
- 10 of 17 target baselines have same-scope results; 5 external baselines and 2 MSA tools are unavailable

### 不能说 (Cannot claim):
- Cannot claim our method exceeds BBS in quality (Δacc = -0.0038)
- Cannot claim our method exceeds CGBAPC in quality (Δacc = -0.0061)
- Cannot claim our method outperforms MUSCLE/VS/BMALA/ITR/CPL (no same-scope results)
- Cannot claim BBS trio harmful is solved (11.1% harmful in BBS trio rows)
- Cannot claim final algorithm success (harmful 6.9% > 5% gate)
- Cannot use historical 4-dataset results for same-scope comparison

## 是否有 missing context

`missing_expected_files=['final_decision_matrix.tsv', 'no_protected_files_modified.tsv', 'original_bbs_unchanged_audit.tsv', 'leakage_audit.tsv', 'commands_run.sh', 'environment_summary.txt']`。这些缺失项只作为上下文缺口记录；若 required bridge files 全部生成，则不阻塞 bridge 使用。

## 当前下一步

Review latest result artifacts and confirm whether another validation step is warranted.

## protected diff 状态

`protected_files_modified=unknown`。本 bridge 任务只写入 `chat_bridge/` 和 `scripts/chat_bridge/`。

## original BBS source 状态

`original_bbs_source_modified=unknown`。本 bridge 任务未写入 `../bbs-src` 或 BBS source。
