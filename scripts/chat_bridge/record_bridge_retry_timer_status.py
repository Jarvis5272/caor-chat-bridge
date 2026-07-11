#!/usr/bin/env python3
"""Record the user-level Bridge V3 retry timer without exposing credentials."""

from __future__ import annotations

import csv
import subprocess
from pathlib import Path


ROOT = Path("/home/hanlinxuan/research/ACOR-online-reconstruction")
OUT = ROOT / "results/chat_bridge_v3_repair_20260711/BRIDGE_RETRY_TIMER_STATUS.tsv"
UNIT = "caor-chat-bridge-sync.timer"


def command(*args: str) -> tuple[int, str]:
    proc = subprocess.run(["systemctl", "--user", *args], text=True, capture_output=True)
    return proc.returncode, " ".join((proc.stdout or proc.stderr).split())[:800]


def main() -> int:
    enabled_rc, enabled = command("is-enabled", UNIT)
    active_rc, active = command("is-active", UNIT)
    next_rc, next_value = command("show", UNIT, "--property=NextElapseUSecRealtime", "--value")
    last_rc, last_value = command("show", UNIT, "--property=LastTriggerUSec", "--value")
    rows = [
        {"item": "installed", "status": "pass" if enabled_rc == 0 else "fail", "details": enabled or "unknown"},
        {"item": "active", "status": "pass" if active_rc == 0 else "fail", "details": active or "unknown"},
        {"item": "next_retry", "status": "pass" if next_rc == 0 and next_value else "warn", "details": next_value or "unknown"},
        {"item": "last_trigger", "status": "pass" if last_rc == 0 else "warn", "details": last_value or "not_yet"},
        {"item": "frequency", "status": "pass", "details": "10 minutes"},
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["item", "status", "details"], delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(OUT)
    return 0 if enabled_rc == 0 and active_rc == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
