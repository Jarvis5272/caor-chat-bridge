# Open Questions

- ChatGPT 是否认可新目标应写成 `baseline-aware original CleanIDS algorithm`，而不是过度排斥通用模块的 strict BBS-free？
- 当前是否应把独立性边界表述为 `BBS-semantics-independent`：不使用 BBS output / full decoder wrapper / path likelihood / beam / pruning semantics 作为在线核心？
- 哪些 baseline 模块可以安全作为通用工具借鉴：k-mer/minimizer、bounded local DP、local POA-like micro-consensus、edit sketches、run-length normalization、confidence/margin？
- 下一轮如果继续算法创新，是否只允许 1 个 primary 和 1 个 backup 的深理论 method-card？
- 是否应先做 paper-positioning / negative-evidence package，而不是马上继续新候选？
