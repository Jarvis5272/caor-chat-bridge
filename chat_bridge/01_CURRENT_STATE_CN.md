# 当前项目状态（Chat Bridge）

## 实时故事状态

最新结果目录 `results/originality_boundary_baseline_aware_update_20260704` 是 claim/originality boundary 更新，不是实验或 benchmark；latest label 是 `ORIGINALITY_BOUNDARY_BASELINE_AWARE_UPDATED`。

## clean IDS 数据状态

本轮没有新增数据、实验或 evaluation。clean IDS 数据资产仍来自既有结果目录；bridge 只同步状态，不复制 raw data 或 large result files。

## EPBSD / BBS acceleration 状态

EPBSD / optimized BBS fork 是 BBS-compatible exact-equivalent acceleration 结果，属于 engineering / algorithm-engineering acceleration，不是 independent CleanIDS decoder，也不是 BBS-semantics-independent reconstruction algorithm。

## baseline-aware original algorithm 状态

原创性边界已更新：当前目标不是 zero-baseline algorithm，而是 **baseline-aware original CleanIDS algorithm**。允许合理借鉴 baseline 的通用先进模块，但必须保持自己的核心 state / update / decode / confidence / stop rule，且不能复制 baseline 的完整框架、输出语义或核心决策流程。

“BBS-free” 不再作为过度排斥所有通用模块的唯一口径；更准确的边界是 **BBS-semantics-independent**：不能使用 BBS output、BBS full decoder wrapper、BBS path-likelihood / beam / pruning semantics 作为在线核心。

## 当前 active candidate

无 active decoder candidate。TPC+OCWP 已停止；下一步若继续算法创新，应先做少量深理论 method-card，不做候选海。

## 当前 gate

ORIGINALITY_BOUNDARY_BASELINE_AWARE_UPDATED

## 当前最大风险

如果继续把低置信/拒绝、同步失败、global_search_risk、baseline wrapper 或 EPBSD/BBS-compatible acceleration 当作 independent decoder success，会越过当前 claim boundary。

## 当前不建议继续的方向

- 不建议继续 TPC+OCWP patch 或进入 small reconstruction smoke。
- 不建议把同步 dry-run 写成 benchmark 质量成功。
- 不建议把 EPBSD / BBS-compatible acceleration 写成独立 decoder。
- 不建议把 baseline 模块借鉴写成复制 baseline 语义。
- 不建议修改 protected code、原始数据或 original BBS source。
