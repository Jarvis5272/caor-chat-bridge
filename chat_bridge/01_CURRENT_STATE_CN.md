# 当前项目状态（Chat Bridge）

## 实时故事状态

最新结果目录 `results/tpc_ocwp_real_data_validation_20260704` 显示当前主线仍处在同步/拒绝/风险门控阶段；最新 label 是 `TPC_OCWP_REAL_SYNC_STOP_GLOBAL_SEARCH_REQUIRED`。

## clean IDS 数据状态

最新结果记录的数据状态来自 `results/tpc_ocwp_real_data_validation_20260704`。若报告中的 input scope 不完整，以源 artifact 为准，不在 bridge 中编造。

## EPBSD / BBS acceleration 状态

当前 bridge 只同步状态，不新增 EPBSD/BBS acceleration 实验。latest audit: protected=`no`, original_bbs=`no`。

## BBS-free independent algorithm 状态

当前 active track: `TPC+OCWP real-data synchronization dry-run`。根据 latest gate，当前结论是 `SKIPPED: sync gate did not pass (TPC_OCWP_REAL_SYNC_STOP_GLOBAL_SEARCH_REQUIRED); small reconstruction smoke not allowed.`。

## 当前 active candidate

`TPC+OCWP real-data synchronization dry-run`

## 当前 gate

SKIPPED: sync gate did not pass (TPC_OCWP_REAL_SYNC_STOP_GLOBAL_SEARCH_REQUIRED); small reconstruction smoke not allowed.

## 当前最大风险

如果继续把低置信/拒绝、同步失败或 global_search_risk 当作重建成功，会越过当前 claim boundary。

## 当前不建议继续的方向

- 不建议在 gate 失败时做小 reconstruction smoke。
- 不建议把同步 dry-run 写成 benchmark 质量成功。
- 不建议修改 protected code、原始数据或 original BBS source。
