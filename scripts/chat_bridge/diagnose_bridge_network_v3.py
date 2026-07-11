#!/usr/bin/env python3
"""Run bounded, redacted network/auth diagnostics for the bridge remote."""

from __future__ import annotations

import csv
import os
import re
import shutil
import subprocess
import time
from pathlib import Path


ROOT = Path("/home/hanlinxuan/research/ACOR-online-reconstruction")
OUT = ROOT / "results/chat_bridge_v3_repair_20260711/BRIDGE_NETWORK_DIAGNOSTIC.tsv"


TESTS = [
    ("dns_github", ["getent", "hosts", "github.com"], "network"),
    ("dns_raw_github", ["getent", "hosts", "raw.githubusercontent.com"], "network"),
    ("https_github", ["curl", "-I", "--connect-timeout", "10", "--max-time", "20", "https://github.com"], "https"),
    ("https_raw_github", ["curl", "-I", "--connect-timeout", "10", "--max-time", "20", "https://raw.githubusercontent.com"], "https"),
    ("git_https_ls_remote", ["git", "ls-remote", "https://github.com/Jarvis5272/caor-chat-bridge.git"], "https"),
    ("ssh_443", ["ssh", "-T", "-p", "443", "-o", "BatchMode=yes", "-o", "ConnectTimeout=10", "git@ssh.github.com"], "ssh443"),
    ("ssh_22", ["ssh", "-T", "-o", "BatchMode=yes", "-o", "ConnectTimeout=10", "git@github.com"], "ssh22"),
    ("gh_auth", ["gh", "auth", "status", "-h", "github.com"], "https"),
]


def redact(text: str) -> str:
    text = re.sub(r"(https?://)[^/@\s]+@", r"\1<redacted>@", text)
    text = re.sub(r"(?i)(token|oauth_token|authorization)(\s*[:=]\s*)\S+", r"\1\2<redacted>", text)
    return " ".join(text.split())[:500]


def run(name: str, command: list[str], transport: str) -> dict[str, str]:
    if shutil.which(command[0]) is None:
        return {
            "test": name,
            "command_redacted": " ".join(command),
            "dns_status": "not_applicable",
            "connection_status": "tool_missing",
            "auth_status": "unknown",
            "latency_or_timeout": "0.000s",
            "stderr_summary": f"{command[0]} not installed",
            "recommended_transport": "none",
        }
    started = time.monotonic()
    env = os.environ.copy()
    env["GIT_TERMINAL_PROMPT"] = "0"
    try:
        proc = subprocess.run(command, cwd=ROOT, env=env, text=True, capture_output=True, timeout=30)
        elapsed = time.monotonic() - started
        output = f"{proc.stdout}\n{proc.stderr}"
        success = proc.returncode == 0
        # GitHub SSH intentionally returns 1 after successful authentication.
        ssh_auth = "successfully authenticated" in output or "Hi " in output
        auth = "yes" if (name == "gh_auth" and success) or (name.startswith("ssh_") and ssh_auth) else "not_tested"
        if name == "git_https_ls_remote":
            auth = "yes" if success else "no_or_transport_failed"
        if name == "gh_auth" and not success:
            auth = "no"
        dns = "pass" if name.startswith("dns_") and success else ("fail" if name.startswith("dns_") else "not_applicable")
        connection = "pass" if success or ssh_auth else "fail"
        summary = redact(proc.stderr or proc.stdout)
        recommended = transport if connection == "pass" and auth not in {"no", "no_or_transport_failed"} else "none"
        return {
            "test": name,
            "command_redacted": " ".join(command),
            "dns_status": dns,
            "connection_status": connection,
            "auth_status": auth,
            "latency_or_timeout": f"{elapsed:.3f}s",
            "stderr_summary": summary,
            "recommended_transport": recommended,
        }
    except subprocess.TimeoutExpired as exc:
        elapsed = time.monotonic() - started
        return {
            "test": name,
            "command_redacted": " ".join(command),
            "dns_status": "timeout" if name.startswith("dns_") else "not_applicable",
            "connection_status": "timeout",
            "auth_status": "unknown",
            "latency_or_timeout": f"timeout_after_{elapsed:.3f}s",
            "stderr_summary": redact((exc.stderr or "") if isinstance(exc.stderr, str) else "timeout"),
            "recommended_transport": "none",
        }


def main() -> int:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    rows = [run(*test) for test in TESTS]
    fields = [
        "test", "command_redacted", "dns_status", "connection_status", "auth_status",
        "latency_or_timeout", "stderr_summary", "recommended_transport",
    ]
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    print(OUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
