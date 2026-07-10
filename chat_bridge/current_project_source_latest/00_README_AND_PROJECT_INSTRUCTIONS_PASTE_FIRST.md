# ACOR-online-reconstruction 当前项目源文件包（2026-07-10）

**旧 STWC 材料已经退役，仅作为历史归档。当前方法、实验和论文必须以本迁移包为准。**

## 项目路径

`/home/hanlinxuan/research/ACOR-online-reconstruction`

## 当前研究问题

在 clean IDS / DNA storage per-cluster reconstruction 中，给定 streaming prefix reads，在严格 online 约束下持续输出当前或最终 consensus，同时区分单线程公平 latency 与多 worker deployment throughput。

## 当前算法一句话定义

当前方法（正式命名待定）维护稳定 k-mer / seed 锚点、锚点约束局部证据和增量 evidence state，用 confidence / margin 控制 consensus 输出；代码 runner 当前为 `scripts/pareto_run_to_completion_controller_20260706/run_cecc_bounded.py`，但论文正文暂不采用旧候选名作为方法名。

## 当前在线约束

Online decode 只允许使用当前 prefix reads、历史内部状态和当前局部证据；禁止使用 reference、truth、未来 reads、BBS/CPL/VS/MUSCLE/BMALA 输出或任何 baseline output。Reference 只允许用于 offline Eval。

## 当前主结果状态

当前 CAPPED_17_MATCHED benchmark row keys: 82,462 prefix rows, row-key SHA256 `7ac2b177a2b5a42d4f1f882610cbb384caa024bd6c60d36944beb57832b8596d`。以下数字在交叉验证完成前统一标为 provisional：

- 当前方法: Accuracy 0.9660, Exact 0.3485, ED 4.2801, 1-thread runtime 103.53s, Prefix/s 796.5。
- BBS: Accuracy 0.9688, Exact 0.2461, ED 3.8344, runtime 684.30s。
- CPL: Accuracy 0.9972, Exact 0.9170, ED 0.3852, runtime 3743.20s。
- VS: Accuracy 0.9450, Exact 0.2943, ED 6.8944, runtime 39.10s。
- MUSCLE: Accuracy 0.9292, Exact 0.2194, ED 8.8211, runtime 2035.70s。
- BMALA: Accuracy 0.5378, Exact 0.0009, ED 61.1629, runtime 119.90s。

这些数字来自最新 CAPPED_17_MATCHED fair benchmark，尚需 P0 independent cross-validation 后才可锁定。

## 已锁定 vs provisional

- 锁定：当前任务边界、online constraint、runner path、参数来源、small/medium/large scale plan、旧 STWC 退役。
- Provisional：所有主结果数值、runtime、multi-thread scalability、output identity，直到 cross-validation 通过。

## 当前最高优先级任务

P0 result cross-validation: input/output hash, independent metric recomputation, runtime repeatability, no-leakage audit。

## full-source 规划

- small: `oligo0`, 1,466 clusters / 167,546 reads。
- medium: `ncomms19_365_dishes_full_strict_clean`, 2,038 clusters / 66,804 reads。
- large: `binned_nanopore`, 10,000 clusters / 213,740 reads。
- 当前未发现单一十万 cluster 来源，不得编造。

## 论文冲刺状态

INFOCOM / paper sprint 是 conditional GO：可以并行写 problem/method/experiment skeleton，但正式 claim 依赖 P0 cross-validation 和至少 large full-source validation。

## Codex / ChatGPT 工作流

ChatGPT 负责拆任务、审 claim、组织论文；Codex 负责读取真实代码/结果、执行命令、生成审计产物、finalize bridge。所有新任务结束必须给出路径、label、claim boundary、protected/BBS source audit。

## 新对话启动顺序

1. 先读本文件。
2. 读 `01_CURRENT_PROJECT_STATE_AND_DECISIONS.md`。
3. 读 `02_CURRENT_METHOD_SPECIFICATION_CN.md`。
4. 读 `04_PROTOCOL_AND_EVALUATION_CONTRACT.md`。
5. 读 `05_CURRENT_RESULTS_AND_CLAIM_BOUNDARY_CN.md`。
6. 读 `07_RESULT_CROSS_VALIDATION_PLAN_AND_STATUS_CN.md` 和 `08_EXPERIMENT_MASTER_PLAN_CN.md`。
7. 写论文时再读 `10_NEW_PAPER_OUTLINE_AND_WRITING_PLAN_CN.md`。

## 不得继续沿用旧 STWC 正文

旧 STWC paper skeleton、旧 Overleaf section、旧 candidate pool narrative 已经归档在 `archive/legacy_stwc_project_context_20260710/`，只可作为历史背景，不可作为当前 source of truth。
