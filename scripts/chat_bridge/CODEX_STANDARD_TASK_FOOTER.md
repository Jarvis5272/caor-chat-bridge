# Codex Standard Task Footer

任何 Codex goal 最后必须执行：

```bash
bash scripts/chat_bridge/codex_task_finalize.sh results/<本轮输出目录> "<FINAL_LABEL>"
```

Codex final response 必须只输出：

1. final label
2. output dir
3. completed stages
4. key metrics
5. gate decision
6. claim boundary
7. next recommendation
8. bridge status
9. chat_bridge_feedback_package path
10. bridge raw link if pushed
11. protected files modified?
12. original BBS source modified?

如果未执行 bridge finalize，final label 必须改为：

```text
TASK_COMPLETED_BUT_BRIDGE_NOT_FINALIZED
```

Bridge finalize 不是算法成果，也不是 benchmark。它只是 ChatGPT-Codex 状态同步基础设施。
