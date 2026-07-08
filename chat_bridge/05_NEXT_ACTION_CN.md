# Next Action

## 当前建议下一步

Revise the sync/global-search mechanism before any small reconstruction smoke; review gate matrix and failure taxonomy.

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

是否继续算法严格服从本页 latest result 的 gate 和 `Revise the sync/global-search mechanism before any small reconstruction smoke; review gate matrix and failure taxonomy.`；不得从旧聊天附件或 frozen BAEPC 状态恢复任务。

## 推荐给 ChatGPT/Codex 的下一步动作

- 只执行 `Revise the sync/global-search mechanism before any small reconstruction smoke; review gate matrix and failure taxonomy.` 指向的显式 controller action；
- 不从 BAEPC+FEIW historical negative evidence 继续；
- 不依赖聊天上传附件恢复项目状态；
- 不修改 protected code / original BBS / raw data。
