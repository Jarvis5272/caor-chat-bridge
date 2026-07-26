# Method Selection V2 阶段性同步

- Status: `PRELIMINARY_DIAGNOSTIC_V2_NOT_READY_FOR_PAPER_LOCK`
- Generated: `2026-07-26T21:15:15+08:00`
- Completed evidence: split lock, variant contracts, leave-one-out, cumulative
  build-up, module coupling, event counterfactual audit, K x W grid, M x rho grid.
- Pending: 735 formal DEV timing runs, VALIDATION, HOLDOUT, full F5 confirmation,
  selected revision regeneration when required, final baseline bootstrap, and
  final method/parameter decision.
- Paper boundary: Results 3.8, Results 3.9, and Fig. 5 remain pending.
- Manuscript modified: No
- Baselines rerun: No
- Algorithm promoted or revised: No

## 冻结分区

- DEV: 3000 clusters, 16864
  rows, 102031 prefix-read uses,
  SHA-256 `ed8d242969c62a032ce68d78893d0cc1afd4ff23773452381db5f63655c00aee`.
- VALIDATION: 2000 clusters,
  11293 rows,
  SHA-256 `3c0988ff5fd9ae03632d68f64243bc685d24d2a006e96cf3d03def45f46f3707`.
- HOLDOUT: 128464 clusters,
  710986 rows,
  SHA-256 `5f94945390f5c00af412089eadded61448f14e87b31f78f656fcf1eaec021d33`.

## 已完成 DEV 主要结果

- Frozen Full: Row Accuracy 0.9571348266823837, source-macro Accuracy
  0.957699735972172, Exact 0.19171015180265655, Mean ED
  5.236005692599621.
- Aggregate K-mer backbone is the dominant observed module:
  C0 -> C1 source-macro Accuracy changes from
  0.9366181298706904 to 0.9568956093823171, and Exact
  from 0.06410104364326376 to 0.18228178368121442.
- Local candidate construction adds a smaller positive point effect:
  C1 -> C2 source-macro Accuracy 0.9568956093823171 ->
  0.9575313216607038; Exact 0.18228178368121442 -> 0.18927893738140417.
- W eligibility and drift gates add small point improvements:
  C2 -> C3 -> C4 source-macro Accuracy
  0.9575313216607038 -> 0.9576376781935683 ->
  0.9577154832817572.
- Conservative guards change the DEV point estimate only slightly:
  C4 -> C5 source-macro Accuracy 0.9577154832817572 ->
  0.9576997359721883. This is not a deletion decision; VALIDATION
  and HOLDOUT gates remain pending.
- Diversity rejected zero events on this DEV scope, and NO_DIVERSITY matched
  Full output hash. This is evidence of inactivity on DEV, not proof of global
  redundancy.

## 反事实 gate 证据

- Accepted events: 1176 total,
  1036 beneficial and 117 harmful.
- W-bound rejected 672 events; it prevented
  642 harmful counterfactuals and
  missed 30 beneficial ones
  (rejection precision 0.9553571428571429).
- Fraction/support-gap rejected
  65415 events; it prevented
  55779 harmful
  counterfactuals and missed
  6906 beneficial ones
  (rejection precision
  0.8898301028954295).
- Subset and cross-event gates have negative DEV net counterfactual values
  (-54 and
  -49); their retention
  must therefore be decided by preregistered VALIDATION/HOLDOUT evidence, not
  by this DEV point audit alone.

## 参数网格阶段性结果

- Frozen K/W: K=7, W=80.
- DEV top-quality K/W: K=7,
  W=20, source-macro Accuracy
  0.9578456229278522.
- Diagnostic top-throughput K/W: K=11,
  W=40; throughput is diagnostic
  under external load and is not a runtime lock.
- M/rho top source-macro point candidate: `MRHO_top_quality_K7_W20_M2_RHO0p5`
  with source-macro Accuracy 0.9578456229278522 and
  source-macro Mean ED 5.158188239648946.
- M/rho top Exact point candidate: `MRHO_top_quality_throughput_K11_W40_M2_RHO0p5` with Exact
  0.19473434535104364.

## Paper boundary

该包只供中枢与论文线提前了解已完成诊断证据，不是 Number Lock、Claim
Lock 或最终论文结果。任何候选排名都必须等待预注册的
VALIDATION -> HOLDOUT -> full confirmation 流程完成。
