# Bioinformatics 论文线预同步候选

## 同步状态

`READY_FOR_METHOD_HARDENING_INTEGRATION_TIMING_PENDING`

这是 timing closure 前的预同步候选，不是最终 hardening lock。

## 可立即整合

1. Methods：冻结 revision、默认参数、source-balanced diagnostic scope、SHA-256 selection、reference-offline 与 first-t protocol。
2. Results：默认等价性、九个可识别消融、18 点单因素敏感性、五个 read-order seeds。
3. Statistics：2,000-replicate cluster-block bootstrap；CPL 三个运行分别处理。
4. Discussion：Oligo0、低 prefix、低 anchor/repetitive/homopolymer/drift regimes，以及 conservative fallback 权衡。
5. Figures：`FIG5_ABLATION_DATA.tsv`、`FIG5_SENSITIVITY_DATA.tsv`、`FIGS1_READ_ORDER_DATA.tsv`、`FIGS2_FAILURE_STRATA_DATA.tsv`。

## 必须保留的结果边界

- Aggregate K-mer backbone support 是可识别消融中的最大平均质量贡献项。
- 参数敏感性描述冻结默认附近的稳定性，不构成重新调参。
- Read-order 结果支持 measured robustness，不支持 order invariance。
- Current 对 BBS/VS 的质量区间占优；对 BMALA 的 Accuracy/Mean ED 占优但 Exact 落后。
- CPL 和 MUSCLE 显示质量/运行代价 trade-off；不得隐藏其有利指标。
- 不声称 universal dominance。

## 暂缓整合

- 新五重复 Current runtime
- P32 locked throughput
- P1-to-P32 scaling 和 efficiency

这些项目必须等待 `CURRENT_METHOD_TIMING_CLOSURE.tsv` 与 `HARDENING_POST_COMPLETION_AUDIT.tsv`。

## 方法事实禁区

当前算法没有 confidence、calibration、adaptive early stopping、cross-prefix persistent state 或 target-window normalization。不得新增这些表述或实验。

## 论文工作区

本包只提供同步候选，不直接修改论文源码。
