# 当前项目状态（Chat Bridge）

## 实时故事状态

最新结果目录 `results/final_full_17dataset_baseline_benchmark_20260707` 是当前 latest result；最新 label 是 `FINAL_BENCHMARK_PARTIAL_EXTERNAL_COMPLETE_PENDING`。

## clean IDS 数据状态

最新结果记录的数据状态来自 `results/final_full_17dataset_baseline_benchmark_20260707`。若报告中的 input scope 不完整，以源 artifact 为准，不在 bridge 中编造。

## EPBSD / BBS acceleration 状态

当前 bridge 只同步状态，不新增 EPBSD/BBS acceleration 实验。latest audit: protected=`unknown`, original_bbs=`unknown`。

## baseline-aware / independent algorithm 状态

当前 active track: `missing`。根据 latest gate，当前结论是 `FINAL_BENCHMARK_PARTIAL_EXTERNAL_COMPLETE_PENDING`。

BAEPC+FEIW 的 `BAEPC_FEIW_STOP_FULL_ALIGNMENT_REQUIRED` 仅是 historical frozen negative evidence；它不可 revise、不可 patch，也不属于 active frontier。

## 项目状态源

权威顺序是：服务器 `results/` 与 controller state、服务器 `chat_bridge/`、GitHub raw bridge。旧聊天附件不得作为状态源或阻塞原因。

## 当前 active candidate

`missing`

## 当前 gate

FINAL_BENCHMARK_PARTIAL_EXTERNAL_COMPLETE_PENDING

## 当前最大风险

如果继续把低置信/拒绝、同步失败、method-card 通过或工程加速当作 reconstruction success，会越过当前 claim boundary。

## 当前不建议继续的方向

- 不建议在 gate 未允许时做小 reconstruction smoke。
- 不建议把 method-card、hand-toy 或 sync dry-run 写成 benchmark 质量成功。
- 不建议修改 protected code、原始数据或 original BBS source。
