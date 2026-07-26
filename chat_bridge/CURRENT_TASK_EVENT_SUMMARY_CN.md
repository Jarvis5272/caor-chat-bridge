# Bioinformatics Current Method Hardening 已完成证据汇总

## 当前状态

- 上游任务：`BIOINFORMATICS_CURRENT_METHOD_HARDENING_20260726`
- 当前标签：`BIOINFORMATICS_METHOD_HARDENING_PARTIAL_WITH_BLOCKERS`
- 唯一 blocker：`timing_closure_missing`
- Current P1/P8/P16/P32 五重复计时：等待预注册资源门，尚未启动
- 算法、baseline、evaluator、默认参数和数据范围均未修改

本文件只汇总已经完成并可追溯的证据。不得用它提前锁定新的 runtime、并行效率或吞吐量。

## 冻结方法与范围

- 权威 revision：`582cd6d124eb1012232abea0df81f858c77e1ad9`
- 默认参数：`K=7, W=80, M=2, rho=0.35`
- Diagnostic scope：五个 F5 来源各 1,466 clusters
- 总规模：7,330 clusters，41,406 prefix rows，252,774 prefix-read uses
- Row-key SHA-256：`03c8325f018d0eae04e3c26db448f65f396502ccab5d519b158754fc0a09e50d`
- 预注册偏差：Oligo0 full 只有 1,466 clusters，无法无重复地达到每来源 2,000；因此采用最大等量五来源范围
- Reference online：No
- Future reads：No

## 默认等价性

Diagnostic default 与冻结正式 Current kernel 在 41,406/41,406 rows 上：

- row keys identical：100%
- reconstructed sequences identical：100%
- different rows：0
- Accuracy/Exact/Mean ED identical
- empty-output handling identical

因此后续 diagnostic variant 结果具有可解释的默认基线。

## 消融

九个可识别 variant 均完成 20-cluster smoke、100-cluster pilot 和三次完整 diagnostic run；三次输出均确定一致。

- `A1 NO_AGGREGATE_KMER_BACKBONE_SUPPORT` 是最大平均质量贡献项：diagnostic Accuracy 下降 `0.0172813`，Mean ED 增加 `2.20722`；full-F5 confirmation Accuracy 为 `0.9513265`。
- `A2 BACKBONE_ONLY` 在 diagnostic scope 的 Accuracy 下降 `0.0007704`、Mean ED 增加 `0.08965`；full-F5 Accuracy 为 `0.9698377`。
- `A6 NO_FRACTION_AND_SUPPORT_GAP` 的 diagnostic 平均变化很小；full-F5 Accuracy 为 `0.9700678`。
- `A7 NO_CONSERVATIVE_GUARDS` 的平均 Accuracy 变化很小，但不能据此否定 guards 在局部风险控制中的作用；full-F5 Accuracy 为 `0.9701256`。
- `A8/A9/A10` 作为 micro-ablation 保留，用于拆分 subset、diversity 和 cross-event guards。
- `A5 NO_W_BOUND` 仅作为 diagnostic evidence，不自动推广为正式方法。
- `A3 NONUNIQUE_ANCHORS` 与 `A4 NO_MONOTONE_FILTER` 被源码审计判定为 `NOT_IDENTIFIABLE`，未猜测实现、未运行。

安全结论：aggregate K-mer backbone support 是该组可识别消融中最主要的平均质量贡献；其余机制主要体现较小的平均变化和局部保守性权衡。不得写成每个组件在所有来源均单调获益。

## 参数敏感性

18 个唯一配置点全部完成：

- K：5、6、7、8、9、11
- W：40、60、80、100、120、160
- M：1、2、3、4
- rho：0.20、0.275、0.35、0.425、0.50

按预注册稳定区间：

- `K=5` 明确不稳定：Accuracy 下降 `0.0023562`，Mean ED 增加 `0.28858`
- `K=6/7/8/9/11` 属于测得稳定区域
- 所有 W 点属于测得稳定区域
- 所有 M 点属于测得稳定区域
- 所有 rho 点属于测得稳定区域
- rho 轴最大 Accuracy 差异约 `1.79e-6`

单因素结果未支持执行额外交互网格。默认参数未被重新选择或修改。

## Read-order robustness

固定 seeds 1–5 的 cluster 内 read shuffle 全部完成：

- mean Accuracy delta：`-0.00028649`
- sample standard deviation：`0.00017759`
- worst-seed Accuracy delta：`-0.00048408`
- normal-approximation 95% interval：`[-0.00063456, 0.00006159]`
- changed-row fraction：约 `80.5%–80.8%`

安全结论：五个固定 arrival-order 扰动下平均 Accuracy 变化较小，但大量 row 的具体输出发生变化，因此只能称为 quality robustness，不能称为 order invariant。

## Cluster-block bootstrap

按 cluster、固定 seed、2,000 replicates：

- Current 相对 BBS：Accuracy、Exact 和 Mean ED 的区间均支持 Current。
- Current 相对 VS：Accuracy、Exact 和 Mean ED 的区间均支持 Current。
- Current 相对 BMALA：Accuracy 与 Mean ED 支持 Current；BMALA Exact 显著更高。
- CPL 三个非确定运行分别处理：row-weighted Accuracy/Mean ED 略支持 Current；source-macro Accuracy/Mean ED 与 Exact 支持 CPL。
- MUSCLE：row-weighted 与 source-macro 的 Accuracy、Exact、Mean ED 均支持 MUSCLE，但优势幅度和运行代价必须与正式锁表一起报告。

不得声称 universal dominance。CPL 不得先挑选单次运行再形成单值结论。

## Failure regimes

- Full-F5 Current 最弱来源：`oligo0`，row Accuracy `0.908744`
- Prefix `t=1`：Accuracy `0.947134`，Exact `0.045765`，Mean ED `7.235479`
- 低 anchor、重复上下文、homopolymer、较大 read-length drift 和 overlong interval 是主要困难分层
- fallback 分层用于描述保守策略的 fidelity/Exact 权衡
- 高 prefix 下的 CPL/MUSCLE 比较仅来自冻结六方法结果

所有 failure strata 均为 reconstruction 后的离线分析，没有用 truth 调整 online 输出。

## Full-F5 confirmation

六个预注册 confirmation 均完成 739,143/739,143 rows，missing=0，duplicate=0：

- A1、A2、A6、A7
- `SENS_K5`
- `SENS_RHO0200`

这些 confirmation 不改变默认算法，也不形成新方法版本。

## 已完成的全局比较证据

- F5 六方法 online/all-protocol matrix：79/79 run tasks 完成
- 全数据/全 baseline 整合：101 formal configuration cells，303 formal runs
- TrellisBMA CPL/MUSCLE supplement：6/6 formal runs；CPL 非确定性单独报告

这些证据已经锁定，不因本轮 Current timing 等待而失效。

## 当前不得同步的内容

- 新 P1/P8/P16/P32 五重复 median、CV、Prefix/s 或 prefix-read uses/s
- P32 参考值 `57.249 s` 作为锁定结果
- diagnostic runtime 作为正式 F5 runtime
- confidence、calibration、adaptive early stopping、cross-prefix persistent state
- order invariance、universal dominance
- multi-worker 对 baseline w1 的 single-core algorithmic speedup

## 论文线状态

论文线现在可以整合：

- diagnostic scope 与默认等价性
- 消融与参数敏感性
- read-order robustness
- cluster-block bootstrap
- failure taxonomy
- 已锁定的 F5 六方法比较

论文线必须暂留 timing closure 占位，等后台 20 次 Current timing 和独立完成后验收通过后再填入最终数字。
