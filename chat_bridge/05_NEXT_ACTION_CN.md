# Next Action

## 当前建议下一步

只允许进入 **BAEPC hand toy**。目标是手算验证 edit-event posterior field、support/margin/conflict/ambiguity gates、Decode 和 Confidence 是否真的可操作，并检查它是否有 bounded constructive correction。

## 不建议做什么

- 不建议写代码。
- 不建议真实数据 dry-run。
- 不建议 reconstruction smoke 或 benchmark。
- 不建议把 BAEPC method-card 写成 algorithm success。
- 不建议把 bounded local DP 扩成 full alignment / full POA / full graph。
- 不建议修改 protected code、original BBS source、EPBSD fork、原始数据或 evaluator。

## 如果交给 Codex，推荐 prompt 文件

`chat_bridge/05_NEXT_ACTION_CN.md` 和 `chat_bridge/06_FILES_FOR_REVIEW.tsv` 可作为下一轮 prompt 的输入索引。

## 如果需要 ChatGPT 审查，推荐打开哪些文件

- chat_bridge/00_README_FIRST.md
- chat_bridge/01_CURRENT_STATE_CN.md
- chat_bridge/02_LATEST_CODEX_RESULT.json
- chat_bridge/04_ACTIVE_CLAIM_BOUNDARY_CN.md
- results/baepc_baseline_aware_method_card_20260704/BAEPC_BASELINE_AWARE_METHOD_CARD_REPORT_CN.md
- results/baepc_baseline_aware_method_card_20260704/BAEPC_METHOD_CARD_GO_NO_GO_CN.md

## 推荐给 ChatGPT 的下一步问题

- BAEPC 的 event posterior field 是否足够原创，还是仍像 medoid + residual correction？
- BAEPC hand toy 应使用哪些 reads 来覆盖 insertion/deletion/substitution/repeat ambiguity？
- 如果 hand toy 只能 low-confidence，是否应立即 stop？
