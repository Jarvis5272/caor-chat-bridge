# Next Action

## 当前建议下一步

Freeze BAEPC+FEIW as a stopped line; no revise, smoke, or benchmark. Return to strategy review or open a new theory-only candidate only with explicit approval.

## 不建议做什么

- 不建议运行新实验或 benchmark 来填补 bridge 缺口。
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
- chat_bridge/09_SYNC_STATUS.tsv

## 是否需要用户批准

当前 bridge 初始化本身不需要额外批准；任何新实验、long-running validation、protected/BBS/source 修改或大文件打包都需要用户批准。

## 是否继续算法

当前不继续算法。若要重新打开算法线，必须由用户单独批准，并保留新的 result dir 与 claim boundary。

## 推荐给 ChatGPT 的下一步问题

- 当前是否应该把 TPC+OCWP 作为负结果冻结？
- 当前 strategy review / paper positioning 是否应把 EPBSD 与 independent decoder 负结果分开叙述？
- 若继续理论线，是否只允许少数 deep candidates 而不是 broad search？

## 推荐给 Codex 的下一步动作

- 优先生成 strategy review / positioning package；
- 不运行实验；
- 不修改 protected code / original BBS / raw data；
- 若用户明确批准，再进入新的 bounded task。
