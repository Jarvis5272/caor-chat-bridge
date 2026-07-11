# Bridge V3 Remote Retry Setup

正常工作流使用用户级 systemd timer 每 10 分钟检查一次。`retry_remote_sync.sh` 使用 `flock` 防止重入；若 raw 状态已经 verified，会直接退出，不创建重复 commit。

安装：

```bash
bash scripts/chat_bridge/install_bridge_retry_timer.sh
```

卸载：

```bash
bash scripts/chat_bridge/uninstall_bridge_retry_timer.sh
```

若 `systemd --user` 不可用，安装脚本只打印用户 crontab 建议，不修改系统级 cron。
