你正在接手 ACOR-online-reconstruction 的 INFOCOM / 论文冲刺对话。请先读取 `00_README_AND_PROJECT_INSTRUCTIONS_PASTE_FIRST.md`，再按其中顺序读取项目源文件。

重要边界：旧 STWC 材料已经退役，只作为历史归档；当前方法暂名“当前方法”，主结构是稳定 k-mer/seed 锚点 -> 锚点约束局部证据 -> 增量 evidence state update -> confidence/margin consensus output。当前结果尚未完全锁定，P0 是 result cross-validation；full-source small/medium/large 实验尚未运行。

不要重新建议大规模算法探索，不要把线程或语言写成主贡献，不要扩大 claim。写作与实验并行推进：先做 P0 cross-validation，再做 oligo0 / NComms19 365 Dishes / binned_nanopore full-source，随后做参数敏感性、消融、置信度校准和论文表格锁定。Codex 负责实际执行和审计，ChatGPT 负责任务拆解、claim boundary 和论文组织。
