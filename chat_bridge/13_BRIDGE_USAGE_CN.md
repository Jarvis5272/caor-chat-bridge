# ChatGPT-Codex Bridge Usage

## Codex 每轮跑完执行什么

```bash
python scripts/chat_bridge/update_chat_bridge_snapshot.py --latest-result results/<run_dir> --out chat_bridge
python scripts/chat_bridge/build_feedback_package.py --in chat_bridge --out chat_bridge_feedback_package.zip
zip -T chat_bridge_feedback_package.zip
```

或者：

```bash
bash scripts/chat_bridge/bridge_after_run.sh results/<run_dir> "<FINAL_LABEL>"
```

任务最终收尾必须使用：

```bash
bash scripts/chat_bridge/codex_task_finalize.sh results/<run_dir> "<FINAL_LABEL>"
```

该流程会禁止 finalize 阶段 auto-detect，执行 local validation、push 和 raw validation；任一失败都不能报告 bridge_ok。

## 项目状态源

- 权威状态源：服务器 `results/`、服务器 `chat_bridge/`、GitHub raw bridge。
- 聊天上传附件和旧聊天上下文不保存项目状态，不得覆盖 explicit latest result。
- historical/frozen result 只能作为证据，不能自动恢复为 active frontier。

## 用户给 ChatGPT 发什么

优先上传或链接：

- `chat_bridge_feedback_package.zip`
- 或 `chat_bridge/00_README_FIRST.md`
- 或 `chat_bridge/08_CODEX_FEEDBACK_TO_CHATGPT.md`

## Git 同步怎么做

推荐命令：

```bash
git add chat_bridge chat_bridge_feedback_package.zip scripts/chat_bridge
git commit -m "Update ChatGPT-Codex bridge snapshot"
git push origin HEAD:chat-bridge
```

默认不自动 push。只有 `CHAT_BRIDGE_AUTO_PUSH=1` 且 remote 可用时，外层流程才允许尝试 push。

## Package 上传怎么做

上传 `chat_bridge_feedback_package.zip`。该 zip 只包含 `chat_bridge/` 内的小文件，不包含 `results/`、`data/`、`scripts/`、raw data、大文件或 secret-like 文件。

## 哪些文件不要同步

不要同步 raw data、fastq/fasta/fa、gz/zip、大型 per-prefix/per-read 表、secret/token/ssh key/API key、原始 BBS source、protected code、formal evaluator 或旧 results。
