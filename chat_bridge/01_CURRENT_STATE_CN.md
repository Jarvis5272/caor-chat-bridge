# 当前项目状态（Chat Bridge）

## 实时故事状态

最新结果目录 `results/scc_real_sync_failure_reconciliation_20260705` 是当前 latest result；最新 label 是 `SCC_STOP_SOUNDNESS_COVERAGE_TRADEOFF`。

## clean IDS 数据状态

最新结果记录的数据状态来自 `results/scc_real_sync_failure_reconciliation_20260705`。若报告中的 input scope 不完整，以源 artifact 为准，不在 bridge 中编造。

## EPBSD / BBS acceleration 状态

当前 bridge 只同步状态，不新增 EPBSD/BBS acceleration 实验。latest audit: protected=`no`, original_bbs=`no`。

## baseline-aware / independent algorithm 状态

当前 active track: `scc_real_sync_failure_reconciliation`。根据 latest gate，当前结论是 `Decision: `RECONCILIATION_PROCEED_READ_ONLY` 关键 SCC real-sync 表可读；当前任务只做数学-实验对齐，不运行新实验、不重跑 real-sync、不修改算法。`。

## 当前 active candidate

`scc_real_sync_failure_reconciliation`

## 当前 gate

Decision: `RECONCILIATION_PROCEED_READ_ONLY` 关键 SCC real-sync 表可读；当前任务只做数学-实验对齐，不运行新实验、不重跑 real-sync、不修改算法。

## 当前最大风险

如果继续把低置信/拒绝、同步失败、method-card 通过或工程加速当作 reconstruction success，会越过当前 claim boundary。

## 当前不建议继续的方向

- 不建议在 gate 未允许时做小 reconstruction smoke。
- 不建议把 method-card、hand-toy 或 sync dry-run 写成 benchmark 质量成功。
- 不建议修改 protected code、原始数据或 original BBS source。
