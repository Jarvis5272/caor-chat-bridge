# 当前结果与 Claim Boundary

## A. 已确认结果

- 当前 runner path、参数来源、online constraints 已确认。
- CAPPED_17 row-key scope 和 row-key SHA256 已确认。
- 旧 STWC 活动正文已退役。

## B. 待交叉验证结果（provisional）

当前 CAPPED_17_MATCHED benchmark row keys: 82,462 prefix rows, row-key SHA256 `7ac2b177a2b5a42d4f1f882610cbb384caa024bd6c60d36944beb57832b8596d`。以下数字在交叉验证完成前统一标为 provisional：

- 当前方法: Accuracy 0.9660, Exact 0.3485, ED 4.2801, 1-thread runtime 103.53s, Prefix/s 796.5。
- BBS: Accuracy 0.9688, Exact 0.2461, ED 3.8344, runtime 684.30s。
- CPL: Accuracy 0.9972, Exact 0.9170, ED 0.3852, runtime 3743.20s。
- VS: Accuracy 0.9450, Exact 0.2943, ED 6.8944, runtime 39.10s。
- MUSCLE: Accuracy 0.9292, Exact 0.2194, ED 8.8211, runtime 2035.70s。
- BMALA: Accuracy 0.5378, Exact 0.0009, ED 61.1629, runtime 119.90s。


## C. 历史结果

旧 STWC、SparseViterbi、BAEPC/FEIW、TPC/OCWP、DICEC/TICEC 等历史线只作为 negative evidence 或 development provenance，不进入当前方法正文。

## D. 不可使用结果

- 未通过 independent output/metric audit 的数字不能写成 locked。
- 旧 STWC 摘要、旧 Overleaf method、旧 candidate sea 不能复制进新论文。
- CAPPED_17 不能作为 full-source scalability 结论。

## Claim boundary

可以说：当前方法在 CAPPED_17 same row keys 上有强 realtime evidence，且算法结构是 BBS-free online evidence-state update。

不能说：质量超过 CPL；替代 BBS/CPL；完成 formal integration；完成 full-source scalability；C++/多线程是算法贡献；16线程吞吐等同单线程公平比较。

必须写清：CPL 质量更高；VS 单线程更快但质量更低；当前方法的主贡献是 stable anchors + anchor-bounded local evidence + incremental evidence-state + confidence-aware consensus。
