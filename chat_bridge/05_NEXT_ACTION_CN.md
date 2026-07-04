# Next Action

## 当前建议下一步

不要继续 TPC+OCWP、不要重新开 broad candidate sea。若用户仍想推进独立算法，应先做 **baseline-aware original CleanIDS algorithm** 的少量深理论 method-card：每个候选必须说明可借鉴的 baseline 模块、不可复制的 baseline 语义、自己的 streaming state 和复杂度优势。

## 不建议做什么

- 不建议运行新实验、toy、dry-run、smoke 或 benchmark 来填补当前边界更新。
- 不建议继续 patch TPC+OCWP 或把 global_search_risk 包装成可修小问题。
- 不建议把 EPBSD / BBS-compatible acceleration 写成 independent decoder。
- 不建议把 low-confidence/refusal/fallback 当作 decoder success。
- 不建议复制 raw data、large result files、fastq/fasta/bam/gz/chunk 文件。
- 不建议修改 protected code、original BBS source、原始数据或 evaluator。

## 如果交给 Codex，推荐 prompt 文件

`chat_bridge/05_NEXT_ACTION_CN.md` 和 `chat_bridge/06_FILES_FOR_REVIEW.tsv` 可作为下一轮 prompt 的输入索引。

## 如果需要 ChatGPT 审查，推荐打开哪些文件

- chat_bridge/00_README_FIRST.md
- chat_bridge/01_CURRENT_STATE_CN.md
- chat_bridge/02_LATEST_CODEX_RESULT.json
- chat_bridge/04_ACTIVE_CLAIM_BOUNDARY_CN.md
- chat_bridge/05_NEXT_ACTION_CN.md
- chat_bridge/12_OPEN_QUESTIONS_CN.md

## 是否需要用户批准

当前 bridge / claim-boundary 更新不需要额外批准；任何新实验、long-running validation、protected/BBS/source 修改、大文件打包或新候选实现都需要用户批准。

## 是否继续算法

当前不继续实验性算法。若要重新打开算法线，建议只允许 1 个 primary 和 1 个 backup 的深理论 method-card，不允许候选海，不允许 wallclock / candidate count 充当进展。

## 推荐给 ChatGPT 的下一步问题

- 新目标 `baseline-aware original CleanIDS algorithm` 是否比 “BBS-free” 更准确？
- 哪些 baseline 模块可以安全借鉴，哪些会变成 wrapper / semantic copy？
- 如果继续理论线，哪个问题机制最值得先写 method-card：indel coordinate ambiguity、edit-sketch consensus、bounded local alignment consensus，还是 posterior edit-event model？

## 推荐给 Codex 的下一步动作

- 优先生成 baseline-aware originality / strategy package；
- 不运行实验；
- 不修改 protected code / original BBS / raw data；
- 若用户明确批准，再进入新的 bounded theory-only task。
