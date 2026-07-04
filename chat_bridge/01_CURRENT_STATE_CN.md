# 当前项目状态（Chat Bridge）

## 实时故事状态

最新结果目录 `results/baepc_baseline_aware_method_card_20260704` 是 BAEPC baseline-aware method-card，不是实验、toy、真实数据 dry-run、smoke 或 benchmark；latest label 是 `BAEPC_METHOD_CARD_GO_TO_HAND_TOY`。

## clean IDS 数据状态

本轮没有新增数据或 evaluation。clean IDS 数据资产仍来自既有结果目录；bridge 只同步状态，不复制 raw data 或 large result files。

## EPBSD / BBS acceleration 状态

EPBSD / optimized BBS fork 仍是 BBS-compatible exact-equivalent engineering / algorithm-engineering acceleration，不是 independent CleanIDS decoder。BAEPC 不使用 EPBSD scoring kernel。

## BAEPC 状态

BAEPC = Baseline-aware Edit-Event Posterior Consensus。它借鉴 medoid scaffold、bounded local DP/alignment、local edit-event posterior 和 confidence/margin 等通用模块，但其核心对象是 streaming edit-event posterior field，定义了自己的 `S_t / Update / Decode / Confidence / StopRule`。

BAEPC 不使用 BBS output、BBS full decoder wrapper、BBS score/beam/pruning/path likelihood、EPBSD kernel、reference/truth/ED/exact/accuracy online 或 dataset/source routing。

## 当前 active candidate

`BAEPC baseline-aware original CleanIDS method card`

## 当前 gate

BAEPC_METHOD_CARD_GO_TO_HAND_TOY

## 当前最大风险

BAEPC 仍可能在 repeated context、homopolymer tied length、branch ambiguity 和 long-range ambiguity 中只能 low-confidence。hand toy 必须证明它有 bounded constructive correction，不是 medoid + refusal。

## 当前不建议继续的方向

- 不建议直接写代码或跑 toy 之外的任何实验。
- 不建议进入真实数据 dry-run、smoke 或 benchmark。
- 不建议把 method-card 写成 decoder success。
- 不建议把 BAEPC 扩展成 full alignment / full POA / full graph。
- 不建议修改 protected code、原始数据、EPBSD fork 或 original BBS source。
