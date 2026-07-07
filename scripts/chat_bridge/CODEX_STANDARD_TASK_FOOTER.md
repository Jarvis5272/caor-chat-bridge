# Codex Standard Task Footer

任何 Codex goal 的最后必须执行：

```bash
bash scripts/chat_bridge/codex_task_finalize.sh results/<本轮输出目录> "<FINAL_LABEL>"
```

注意：

- final label 必须显式传给 finalize；
- finalize 禁止 auto-detect 覆盖本轮 run_dir；
- bridge finalize 必须 local validation pass、push pass、raw validation pass；
- raw README / JSON / feedback / sync status 必须都包含同一个 output_dir 和 final_label；
- 如果 bridge finalize fail，Codex final label 必须改为：

```text
TASK_COMPLETED_BUT_BRIDGE_FINALIZE_FAILED
```

- 不允许只说 bridge pushed；必须验证 raw latest label/output_dir；
- 不允许把 bridge success 当算法、实验或 benchmark 成果。
- 项目状态源固定为服务器 `results/`、服务器 `chat_bridge/` 和 GitHub raw bridge；聊天附件不得覆盖 explicit latest。
- historical/frozen result 不得自动恢复为 active frontier；BAEPC+FEIW 只能作为 frozen negative evidence。

成功时 `codex_task_finalize.sh` stdout 固定包含：

1. final label
2. output dir
3. bridge status
4. raw README link
5. fallback package
6. local bridge validation
7. raw bridge validation
8. protected files modified?
9. original BBS source modified?
10. message to ChatGPT
