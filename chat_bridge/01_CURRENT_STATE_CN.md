# 当前项目状态（Chat Bridge）

## 实时故事状态

最新结果目录 `results/sipc_sparse_identity_path_consistency_method_handtoy_20260705` 是当前 latest result；最新 label 是 `SIPC_HAND_TOY_PASS_GO_TO_TOY_ONLY_PROTOTYPE`。

## clean IDS 数据状态

最新结果记录的数据状态来自 `results/sipc_sparse_identity_path_consistency_method_handtoy_20260705`。若报告中的 input scope 不完整，以源 artifact 为准，不在 bridge 中编造。

## EPBSD / BBS acceleration 状态

当前 bridge 只同步状态，不新增 EPBSD/BBS acceleration 实验。latest audit: protected=`no`, original_bbs=`no`。

## baseline-aware / independent algorithm 状态

当前 active track: `sipc_method_card_handtoy`。根据 latest gate，当前结论是 `Decision: `PASS_TO_METHOD_CARD_AND_HAND_TOY_ONLY` All required upstream SCC/SPWIC/CLEC evidence is readable enough for theory/hand-toy work. No real-data experiment, benchmark, or prototype run is allowed in this stage.`。

## 当前 active candidate

`sipc_method_card_handtoy`

## 当前 gate

Decision: `PASS_TO_METHOD_CARD_AND_HAND_TOY_ONLY` All required upstream SCC/SPWIC/CLEC evidence is readable enough for theory/hand-toy work. No real-data experiment, benchmark, or prototype run is allowed in this stage.

## 当前最大风险

如果继续把低置信/拒绝、同步失败、method-card 通过或工程加速当作 reconstruction success，会越过当前 claim boundary。

## 当前不建议继续的方向

- 不建议在 gate 未允许时做小 reconstruction smoke。
- 不建议把 method-card、hand-toy 或 sync dry-run 写成 benchmark 质量成功。
- 不建议修改 protected code、原始数据或 original BBS source。
