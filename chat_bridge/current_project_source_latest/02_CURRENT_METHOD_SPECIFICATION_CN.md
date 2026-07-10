# 当前方法 specification（中文）

## 1. 输入

每个 cluster 的 prefix reads。对于 prefix t，online method 只看到 reads[1:t] 和历史内部状态。

## 2. 输出

当前 consensus sequence、output hash、confidence / margin、状态审计字段，以及 offline eval 所需的输出。Reference 只在 offline evaluation 中使用。

## 3. Prefix-online protocol

`S_0 = Init()`；每个新 read 到达时执行 `Update(S_{t-1}, r_t)`，再 `Decode(S_t)` 和 `Confidence(S_t)`。不得重放未来 reads，不得读取 baseline output。

## 4. 稳定锚点

方法使用 unique k-mer / seed anchors 在 carrier 与 read 之间建立单调 anchor pairs。真实代码中 `K=7`，`ExtractAnchors` 只保留在 carrier 和 read 中都唯一、且单调递增的 anchor 匹配。

## 5. k-mer / seed 证据作用

k-mer 不作为 BBS-like likelihood，也不调用 beam/path score。它用于稳定局部坐标、选择 carrier、累计 anchor support，并把 local evidence 限制在可审计的小窗口内。

## 6. 锚点约束局部处理

相邻 anchor pair 之间的 segment 被作为 local evidence bucket。若 segment 长度超过 `W=80` 或 anchor 不可用，该部分记为 ambiguous，不扩展成 full alignment / POA / graph。

## 7. 证据状态增量更新

`ReadState` 维护 observed reads、per-read k-mer counters、unique positions、anchor support；`CrossEventState` 维护局部 event variant 的跨 segment consistency。新 read 只更新当前状态，不重新设计候选框架。

## 8. 共识生成

局部 segment evidence 先做 event/no-event decision，再用 cross-event consistency 抑制相邻不兼容更新。最后将 accepted local variants 组装到 carrier coordinate 上得到 consensus。

## 9. Confidence / margin

Confidence 来自 support、subset/geometry diversity、posterior margin、ambiguity and conflict counts。低证据或冲突区不能伪装为高置信恢复。

## 10. 输出条件

输出可以是当前 prefix consensus；若 ambiguity / conflict 过高，应保留 carrier 或低置信，而不是调用 forbidden global search。

## 11. Fallback

Allowed fallback 只能是内部 carrier / no-change protection；禁止使用 BBS、CPL、VS、MUSCLE、BMALA、reference 或 truth 作为 online fallback。

## 12. Reference / truth / future-read 边界

Reference/truth/ED/accuracy/exact 只用于 offline Eval，不参与 Update、Decode、Confidence 或 StopRule。

## 13. 计算轻量原因

核心计算是 unique k-mer lookup、anchor-bounded local segment aggregation、sparse event counters 和 local consistency checks。没有 full graph、large beam 或 full alignment。

## 14. 多 worker 适配

Cluster / prefix rows 可并行调度；线程数只是实现手段，不属于算法参数。论文必须分开报告单线程公平结果和多线程 throughput。

## 15. 失败边界

Repeated context、long-range ambiguity beyond W、homopolymer length ambiguity、系统性同向错误、低覆盖、anchor 缺失或 local evidence collision 都可能导致保守输出或质量下降。这些边界需要 full-source failure analysis 和 calibration。
