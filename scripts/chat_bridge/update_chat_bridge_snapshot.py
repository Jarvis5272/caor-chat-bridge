#!/usr/bin/env python3
"""Build a conservative ChatGPT-Codex synchronization snapshot.

The bridge is intentionally metadata-only: it reads small report/audit files,
records missing context, and never copies raw data or large result artifacts.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import glob
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


EXPECTED_PATTERNS = [
    "FINAL*_REPORT_CN.md",
    "final_decision_matrix.tsv",
    "final_artifact_manifest.tsv",
    "no_protected_files_modified.tsv",
    "original_bbs_unchanged_audit.tsv",
    "leakage_audit.tsv",
    "commands_run.sh",
    "environment_summary.txt",
]

REVIEW_GLOBS = [
    "FINAL*_REPORT_CN.md",
    "*VALIDATION_REPORT_CN.md",
    "*REPORT_CN.md",
    "*GO_NO_GO_CN.md",
    "*gate_matrix.tsv",
    "stage*_gate_decision.md",
    "final_decision_matrix.tsv",
    "final_artifact_manifest.tsv",
    "no_protected_files_modified.tsv",
    "original_bbs_unchanged_audit.tsv",
    "leakage_audit.tsv",
    "environment_summary.txt",
]

BRIDGE_FILES = [
    "00_README_FIRST.md",
    "01_CURRENT_STATE_CN.md",
    "02_LATEST_CODEX_RESULT.json",
    "03_RUN_LEDGER.tsv",
    "04_ACTIVE_CLAIM_BOUNDARY_CN.md",
    "05_NEXT_ACTION_CN.md",
    "06_FILES_FOR_REVIEW.tsv",
    "07_LAST_CHATGPT_PROMPT_TO_CODEX.md",
    "08_CODEX_FEEDBACK_TO_CHATGPT.md",
    "09_SYNC_STATUS.tsv",
    "10_PROTECTED_AUDIT.tsv",
    "11_ORIGINAL_SOURCE_AUDIT.tsv",
    "12_OPEN_QUESTIONS_CN.md",
    "13_BRIDGE_USAGE_CN.md",
]

FORBIDDEN_SUFFIXES = {
    ".fastq",
    ".fq",
    ".fasta",
    ".fa",
    ".bam",
    ".sam",
    ".gz",
    ".chunk",
}
SECRET_NAME_RE = re.compile(
    r"(^|[/_.-])(secret|token|api[-_]?key|credential|password|passwd|id_rsa|id_dsa|id_ed25519|\.env)([/_.-]|$)",
    re.IGNORECASE,
)
SECRET_VALUE_RE = re.compile(
    r"(?i)\b(api[-_]?key|token|secret|password|passwd)\b\s*[:=]\s*([^\s\"']+)"
)
PRIVATE_KEY_RE = re.compile(
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----.*?-----END [A-Z ]*PRIVATE KEY-----",
    re.DOTALL,
)

READ_LIMIT_BYTES = 64 * 1024
LARGE_SKIP_BYTES = 64 * 1024


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).astimezone().isoformat(timespec="seconds")


def rel(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def run_git(root: Path, args: list[str]) -> str:
    try:
        proc = subprocess.run(
            ["git", *args],
            cwd=root,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        )
    except OSError:
        return "missing"
    if proc.returncode != 0:
        return "missing"
    return proc.stdout.strip() or "missing"


def mask_secrets(text: str) -> str:
    text = PRIVATE_KEY_RE.sub("<redacted-private-key>", text)
    return SECRET_VALUE_RE.sub(lambda m: f"{m.group(1)}=<redacted>", text)


def is_forbidden_path(path: Path) -> bool:
    name = path.as_posix()
    return path.suffix.lower() in FORBIDDEN_SUFFIXES or bool(SECRET_NAME_RE.search(name))


def safe_read(path: Path, skipped: list[dict[str, Any]]) -> str | None:
    if not path.exists() or not path.is_file():
        return None
    size = path.stat().st_size
    if is_forbidden_path(path):
        skipped.append({"path": path.as_posix(), "reason": "forbidden_or_secret_name", "size": size})
        return None
    if size > READ_LIMIT_BYTES:
        skipped.append({"path": path.as_posix(), "reason": "large_file_not_read", "size": size})
        return None
    return mask_secrets(path.read_text(encoding="utf-8", errors="replace"))


def read_tsv(path: Path, skipped: list[dict[str, Any]]) -> list[dict[str, str]]:
    text = safe_read(path, skipped)
    if not text:
        return []
    rows = list(csv.DictReader(text.splitlines(), delimiter="\t"))
    return [{k: (v or "") for k, v in row.items()} for row in rows]


def detect_latest_result(root: Path) -> Path | None:
    results = root / "results"
    if not results.exists():
        return None
    candidates = [p for p in results.iterdir() if p.is_dir()]
    if not candidates:
        return None
    return max(candidates, key=lambda p: p.stat().st_mtime)


def glob_one_or_more(latest: Path, pattern: str) -> list[Path]:
    return sorted(Path(p) for p in glob.glob(str(latest / pattern)))


def find_primary_report(latest: Path) -> Path | None:
    for pattern in ["FINAL*_REPORT_CN.md", "*VALIDATION_REPORT_CN.md", "*REPORT_CN.md", "*GO_NO_GO_CN.md"]:
        matches = glob_one_or_more(latest, pattern)
        if matches:
            return matches[0]
    return None


def extract_label(texts: list[str], gate_rows: list[dict[str, str]]) -> str:
    patterns = [
        r"Final(?:\s+sync)?\s+label\s*:\s*\**\s*([A-Z0-9_]+)\s*\**",
        r"final(?:_|\s+)sync(?:_|\s+)label[^\t\n:]*[:\t]\s*([A-Z0-9_]+)",
        r"Final\s+label[^\n]*\b([A-Z0-9_]{8,})\b",
    ]
    for text in texts:
        for pattern in patterns:
            match = re.search(pattern, text, flags=re.IGNORECASE)
            if match:
                return match.group(1)
    for row in gate_rows:
        joined_key = " ".join(str(v).lower() for v in row.values())
        if "final sync label" in joined_key or "final label" in joined_key:
            for value in reversed(list(row.values())):
                if re.fullmatch(r"[A-Z0-9_]{8,}", value.strip()):
                    return value.strip()
    return "missing"


def extract_section(text: str, heading: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    active = False
    heading_lower = heading.lower()
    for line in lines:
        if line.startswith("## ") and heading_lower in line.lower():
            active = True
            continue
        if active and line.startswith("## "):
            break
        if active:
            out.append(line)
    return "\n".join(out).strip()


def extract_metrics(text: str, aggregate_rows: list[dict[str, str]]) -> dict[str, Any]:
    number = r"([0-9]+(?:\.[0-9]+)?)"
    specs = {
        "datasets": rf"Datasets:\s*{number}",
        "clusters_selected": rf"Clusters selected:\s*{number}",
        "prefix_rows": rf"Prefix rows:\s*{number}",
        "prior_tpc_global_search_risk": rf"Prior TPC global_search_risk:\s*{number}",
        "tpc_ocwp_global_search_risk": rf"TPC\+OCWP global_search_risk:\s*{number}",
        "stable_recovery_low_confidence_rate": rf"Stable/recovery/low-confidence rate:\s*{number}",
        "output_length_abnormal_rate": rf"Output length abnormal rate:\s*{number}",
        "high_confidence_wrong_rate": rf"High-confidence wrong rate:\s*{number}",
        "constructive_recovery_rows": rf"Constructive recovery rows:\s*{number}",
        "valid_recovery_rate": rf"Valid recovery rate:\s*{number}",
        "ocwp_pbrw_recovery_rows": rf"OCWP/PBRW recovery rows:\s*{number}",
    }
    metrics: dict[str, Any] = {}
    for key, pattern in specs.items():
        match = re.search(pattern, text)
        if match:
            value = match.group(1)
            metrics[key] = float(value) if "." in value else int(value)
    if aggregate_rows:
        metrics["aggregate_summary"] = aggregate_rows[0]
    return metrics


def extract_completed_stages(report_text: str, latest: Path) -> list[str]:
    stages: list[str] = []
    for line in report_text.splitlines():
        match = re.match(r"^##\s+\d+\.\s+(.+)$", line)
        if match:
            stages.append(match.group(1).strip())
    for stage_file in sorted(latest.glob("stage*_gate_decision.md")):
        stages.append(stage_file.stem)
    return stages or ["missing"]


def parse_environment_task(env_text: str) -> str:
    for line in env_text.splitlines():
        if line.startswith("task="):
            return line.split("=", 1)[1].strip()
    return "missing"


def summarize_gate(gate_text: str, gate_rows: list[dict[str, str]], final_label: str) -> str:
    if gate_text.strip():
        first = " ".join(gate_text.strip().split())
        return first[:240]
    failing = []
    for row in gate_rows:
        status = row.get("status", "").lower()
        gate = row.get("gate", "")
        evidence = row.get("evidence", "")
        if status in {"fail", "stop_or_revise", "skipped"}:
            failing.append(f"{gate}: {status} ({evidence})")
    if failing:
        return "; ".join(failing)[:240]
    if final_label != "missing":
        return final_label
    return "missing"


def target_met(gate_decision: str, final_label: str) -> str:
    lowered = f"{gate_decision} {final_label}".lower()
    if any(word in lowered for word in ["fail", "skipped", "stop", "required", "not allowed"]):
        return "no"
    if "missing" in lowered:
        return "unknown"
    return "yes"


def audit_status(rows: list[dict[str, str]]) -> str:
    if not rows:
        return "unknown"
    clean_statuses = {
        "pass",
        "ok",
        "unchanged",
        "not_modified",
        "not_modified_by_this_task",
        "no_by_this_task",
    }
    for row in rows:
        values = {k.lower(): v.strip().lower() for k, v in row.items()}
        modified = values.get("modified", values.get("modified_by_this_task", "no"))
        status = values.get("status", "")
        if modified not in {"no", "false", "0", ""}:
            return "yes"
        if status and status not in clean_statuses:
            return "unknown"
    return "no"


def scan_latest_files(latest: Path, root: Path) -> tuple[list[dict[str, Any]], int]:
    skipped: list[dict[str, Any]] = []
    for path in latest.rglob("*"):
        if not path.is_file():
            continue
        size = path.stat().st_size
        if is_forbidden_path(path):
            skipped.append({"path": rel(path, root), "reason": "forbidden_or_secret_name", "size": size})
        elif size > LARGE_SKIP_BYTES:
            skipped.append({"path": rel(path, root), "reason": "large_result_file_not_copied", "size": size})
    large_count = sum(1 for item in skipped if "large" in item["reason"])
    return skipped, large_count


def collect_review_files(root: Path, latest: Path, bridge_out: Path, missing_expected: list[str]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    priority = 1
    bridge_review = [
        ("00_README_FIRST.md", "entry point", "current bridge overview"),
        ("01_CURRENT_STATE_CN.md", "state summary", "CN project state"),
        ("02_LATEST_CODEX_RESULT.json", "machine-readable state", "latest result fields"),
        ("04_ACTIVE_CLAIM_BOUNDARY_CN.md", "claim audit", "allowed/disallowed claims"),
        ("05_NEXT_ACTION_CN.md", "next step", "recommended next action"),
        ("09_SYNC_STATUS.tsv", "sync audit", "detected/missing/skipped status"),
    ]
    for name, reason, expected in bridge_review:
        path = bridge_out / name
        rows.append(
            {
                "priority": str(priority),
                "path": rel(path, root),
                "reason_to_review": reason,
                "expected_content": expected,
                "small_enough_for_git": "yes",
                "exists": "yes" if path.exists() else "pending",
                "notes": "generated bridge file",
            }
        )
        priority += 1

    seen: set[str] = set()
    for pattern in REVIEW_GLOBS:
        for path in glob_one_or_more(latest, pattern):
            rpath = rel(path, root)
            if rpath in seen:
                continue
            seen.add(rpath)
            size = path.stat().st_size
            rows.append(
                {
                    "priority": str(priority),
                    "path": rpath,
                    "reason_to_review": "latest result source artifact",
                    "expected_content": pattern,
                    "small_enough_for_git": "yes" if size <= READ_LIMIT_BYTES else "no",
                    "exists": "yes",
                    "notes": f"{size} bytes",
                }
            )
            priority += 1

    for pattern in missing_expected:
        rows.append(
            {
                "priority": str(priority),
                "path": rel(latest / pattern, root),
                "reason_to_review": "missing expected context",
                "expected_content": pattern,
                "small_enough_for_git": "unknown",
                "exists": "no",
                "notes": "missing; do not infer",
            }
        )
        priority += 1
    return rows


def write_tsv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def bullet_lines(items: list[str], max_items: int = 6) -> str:
    if not items:
        return "- missing"
    return "\n".join(f"- {item}" for item in items[:max_items])


def json_dump(data: Any) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def build_snapshot(args: argparse.Namespace) -> dict[str, Any]:
    root = Path.cwd()
    out = Path(args.out)
    if not out.is_absolute():
        out = root / out
    out.mkdir(parents=True, exist_ok=True)

    requested_latest = args.latest_result or "auto"
    auto_detected = False
    explicit_latest_result_used = bool(args.latest_result)
    latest = Path(args.latest_result) if args.latest_result else None
    if args.no_auto_detect and latest is None:
        raise SystemExit("--no-auto-detect requires --latest-result")
    if latest is not None:
        candidate_latest = latest if latest.is_absolute() else root / latest
        if not candidate_latest.exists() or not candidate_latest.is_dir():
            if args.auto_detect_latest and not args.no_auto_detect:
                latest = detect_latest_result(root)
                auto_detected = True
                explicit_latest_result_used = False
            else:
                raise SystemExit(f"Explicit latest result directory does not exist: {candidate_latest}")
        else:
            latest = candidate_latest
            auto_detected = False
    elif args.auto_detect_latest or not args.no_auto_detect:
        latest = detect_latest_result(root)
        auto_detected = True
    if latest is None:
        raise SystemExit("No latest result directory found under results/")
    if not latest.is_absolute():
        latest = root / latest
    if not latest.exists() or not latest.is_dir():
        raise SystemExit(f"Latest result directory does not exist: {latest}")

    timestamp = now_iso()
    read_skipped: list[dict[str, Any]] = []
    scan_skipped, large_count = scan_latest_files(latest, root)

    missing_expected: list[str] = []
    expected_texts: dict[str, str] = {}
    for pattern in EXPECTED_PATTERNS:
        matches = glob_one_or_more(latest, pattern)
        if not matches:
            missing_expected.append(pattern)
            continue
        for path in matches:
            text = safe_read(path, read_skipped)
            if text is not None:
                expected_texts[rel(path, root)] = text

    primary_report = find_primary_report(latest)
    report_text = safe_read(primary_report, read_skipped) if primary_report else ""
    report_text = report_text or ""
    env_path = latest / "environment_summary.txt"
    env_text = safe_read(env_path, read_skipped) or ""
    gate_text = safe_read(latest / "stage9_gate_decision.md", read_skipped) or safe_read(
        latest / "stage0_gate_decision.md", read_skipped
    ) or ""
    gate_matrix_paths = glob_one_or_more(latest, "*gate_matrix.tsv")
    gate_rows = read_tsv(gate_matrix_paths[0], read_skipped) if gate_matrix_paths else []
    aggregate_rows = read_tsv(latest / "real_sync_aggregate_summary.tsv", read_skipped)
    protected_rows = read_tsv(latest / "no_protected_files_modified.tsv", read_skipped)
    original_rows = read_tsv(latest / "original_bbs_unchanged_audit.tsv", read_skipped)

    label_texts = [report_text, gate_text, expected_texts.get(rel(latest / "TPC_OCWP_REAL_SYNC_GO_NO_GO_CN.md", root), "")]
    final_label = args.final_label_override or extract_label(label_texts, gate_rows)
    metrics = extract_metrics(report_text, aggregate_rows)
    completed = extract_completed_stages(report_text, latest)
    gate_decision = summarize_gate(gate_text, gate_rows, final_label)
    candidate = parse_environment_task(env_text)
    if candidate == "missing":
        candidate = "TPC+OCWP real-data synchronization dry-run" if "TPC+OCWP" in report_text else "missing"
    claim_boundary = extract_section(report_text, "Claim boundary") or extract_section(report_text, "Boundary")
    if "BAEPC_TOY_PASS_GO_TO_REAL_DATA_SYNC_DRYRUN" in final_label:
        claim_boundary = (
            "BAEPC toy-only prototype passed on declared toy cases; not real-data proven, "
            "not smoke, not benchmark, and not decoder success on CleanIDS."
        )
    elif not claim_boundary:
        if "HAND_TOY" in final_label:
            claim_boundary = (
                "Method-card candidate is allowed to proceed to hand toy only; "
                "not an effective decoder, not benchmark success, and not real-data proven."
            )
        else:
            claim_boundary = (
                "BBS-free sync dry-run only. No reconstruction benchmark-quality claim; "
                "low-confidence/refusal is not decoder success."
            )
    if "BAEPC_TOY_PASS_GO_TO_REAL_DATA_SYNC_DRYRUN" in final_label:
        next_action = (
            "Real-data synchronization dry-run is allowed next with explicit user approval; "
            "no smoke, benchmark, or algorithm success claim."
        )
    elif "HAND_TOY_PASS_GO_TO_TOY_ONLY_PROTOTYPE" in final_label:
        next_action = (
            "Toy-only prototype is allowed next with explicit user approval; "
            "no real-data dry-run, smoke, or benchmark."
        )
    elif "METHOD_CARD_GO_TO_HAND_TOY" in final_label:
        next_action = (
            "Only the approved hand toy is allowed next; no code, real-data dry-run, smoke, or benchmark."
        )
    elif target_met(gate_decision, final_label) == "no":
        next_action = (
            "Revise the sync/global-search mechanism before any small reconstruction smoke; "
            "review gate matrix and failure taxonomy."
        )
    else:
        next_action = "Review latest result artifacts and confirm whether another validation step is warranted."
    protected_modified = audit_status(protected_rows)
    original_modified = audit_status(original_rows)
    data_modified = "no_by_bridge_task"
    output_dir = rel(latest, root)
    artifact_manifest_path = rel(latest / "final_artifact_manifest.tsv", root) if (latest / "final_artifact_manifest.tsv").exists() else "missing"
    review_rows = collect_review_files(root, latest, out, missing_expected)

    bridge_label = "CHAT_BRIDGE_WORKFLOW_INITIALIZED"
    if missing_expected:
        bridge_label = "CHAT_BRIDGE_WORKFLOW_INITIALIZED_WITH_MISSING_CONTEXT"

    latest_result = {
        "final_label": final_label,
        "bridge_workflow_final_label": bridge_label,
        "output_dir": output_dir,
        "timestamp": timestamp,
        "completed_stages": completed,
        "selected_candidate": candidate,
        "main_metrics": metrics,
        "gate_decision": gate_decision,
        "claim_boundary": claim_boundary,
        "next_action": next_action,
        "protected_files_modified": protected_modified,
        "original_bbs_source_modified": original_modified,
        "data_modified": data_modified,
        "artifact_manifest_path": artifact_manifest_path,
        "files_for_chatgpt_review": [row["path"] for row in review_rows[:12]],
        "missing_expected_files": missing_expected,
        "blocking_missing": False,
        "explicit_latest_result_used": explicit_latest_result_used,
        "auto_detected_latest_result": auto_detected,
        "latest_result_requested": requested_latest,
        "latest_result_used": output_dir,
        "bridge_consistency_status": "generated_pending_validation",
        "large_files_skipped_count": large_count,
    }

    top_review = [row["path"] for row in review_rows if row["exists"] in {"yes", "pending"}][:6]
    metrics_lines = [f"- `{k}`: `{v}`" for k, v in metrics.items() if k != "aggregate_summary"]
    if "aggregate_summary" in metrics:
        metrics_lines.append(f"- `aggregate_summary`: `{metrics['aggregate_summary']}`")
    metrics_text = "\n".join(metrics_lines) if metrics_lines else "- missing"

    readme = f"""# ChatGPT-Codex Bridge Snapshot

## 当前项目一句话目标

在 ACOR / clean IDS / baseline-aware original algorithm 研究中，用小型、可审查的状态快照让 ChatGPT 读取 Codex 的最新结果、claim boundary 和下一步。

## 当前主线状态

最新自动检测结果为 `{output_dir}`；当前最新 Codex label 为 `{final_label}`。当前 bridge 初始化状态为 `{bridge_label}`。

## 最新 Codex final label

`{final_label}`

## 最新输出目录

`{output_dir}`

## ChatGPT 应先读哪些文件

{bullet_lines(top_review)}

## 当前 claim boundary

{claim_boundary}

## 是否有 missing context

`missing_expected_files={missing_expected or []}`。这些缺失项只作为上下文缺口记录；若 required bridge files 全部生成，则不阻塞 bridge 使用。

## 当前下一步

{next_action}

## protected diff 状态

`protected_files_modified={protected_modified}`。本 bridge 任务只写入 `chat_bridge/` 和 `scripts/chat_bridge/`。

## original BBS source 状态

`original_bbs_source_modified={original_modified}`。本 bridge 任务未写入 `../bbs-src` 或 BBS source。
"""

    current_state = f"""# 当前项目状态（Chat Bridge）

## 实时故事状态

最新结果目录 `{output_dir}` 是当前 latest result；最新 label 是 `{final_label}`。

## clean IDS 数据状态

最新结果记录的数据状态来自 `{output_dir}`。若报告中的 input scope 不完整，以源 artifact 为准，不在 bridge 中编造。

## EPBSD / BBS acceleration 状态

当前 bridge 只同步状态，不新增 EPBSD/BBS acceleration 实验。latest audit: protected=`{protected_modified}`, original_bbs=`{original_modified}`。

## baseline-aware / independent algorithm 状态

当前 active track: `{candidate}`。根据 latest gate，当前结论是 `{gate_decision}`。

## 当前 active candidate

`{candidate}`

## 当前 gate

{gate_decision}

## 当前最大风险

如果继续把低置信/拒绝、同步失败、method-card 通过或工程加速当作 reconstruction success，会越过当前 claim boundary。

## 当前不建议继续的方向

- 不建议在 gate 未允许时做小 reconstruction smoke。
- 不建议把 method-card、hand-toy 或 sync dry-run 写成 benchmark 质量成功。
- 不建议修改 protected code、原始数据或 original BBS source。
"""

    ledger_rows = [
        {
            "timestamp": timestamp,
            "final_label": final_label,
            "output_dir": output_dir,
            "candidate_or_track": candidate,
            "stage_reached": "; ".join(completed[:6]),
            "gate_decision": gate_decision,
            "target_met": target_met(gate_decision, final_label),
            "claim_boundary": claim_boundary,
            "protected_files_modified": protected_modified,
            "original_bbs_source_modified": original_modified,
            "data_modified": data_modified,
            "notes": f"bridge_label={bridge_label}; auto_detected_latest_result={auto_detected}",
        }
    ]

    claim_md = f"""# Active Claim Boundary

## 可以说

- 当前结果是 metadata-only 同步快照，latest result 为 `{output_dir}`。
- latest final label 是 `{final_label}`。
- 当前 claim boundary 是：{claim_boundary}

## 不能说

- 不能说当前结果证明 reconstruction benchmark 质量成功。
- 不能把 low-confidence/refusal 计为 decoder success。
- 不能把 method-card 或 hand-toy gate 写成 real-data proven decoder。
- 不能声称 protected code、原始数据或 original BBS source 在本轮被修改。

## 只能作为工程结果

- `chat_bridge/` 是 ChatGPT-Codex 状态同步层。
- 大文件、raw data、secret-like 文件不会被复制进 bridge。

## 只能作为负证据

- gate fail / stop label 只能作为当前路线需要修正的证据。
- missing expected files 只能作为上下文缺失，不能补写结论。

## 需要进一步验证

- 若要继续实验、修改候选机制或进入 reconstruction smoke，需要另行批准并保留新的 result dir。
- 对 latest result 的 claim 应由 ChatGPT 审查 `{rel(out / '06_FILES_FOR_REVIEW.tsv', root)}` 中列出的源文件。
"""

    next_action_md = f"""# Next Action

## 当前建议下一步

{next_action}

## 不建议做什么

- 不建议运行新实验或 benchmark 来填补 bridge 缺口。
- 不建议复制 raw data、large result files、fastq/fasta/bam/gz/chunk 文件。
- 不建议修改 protected code、original BBS source、原始数据或 evaluator。

## 如果交给 Codex，推荐 prompt 文件

`chat_bridge/05_NEXT_ACTION_CN.md` 和 `chat_bridge/06_FILES_FOR_REVIEW.tsv` 可作为下一轮 prompt 的输入索引。

## 如果需要 ChatGPT 审查，推荐打开哪些文件

{bullet_lines(top_review)}

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
"""

    prompt_text = "missing\n"
    if args.prompt_file:
        prompt_path = Path(args.prompt_file)
        if not prompt_path.is_absolute():
            prompt_path = root / prompt_path
        prompt_text = safe_read(prompt_path, read_skipped) or "missing\n"
        if not prompt_text.endswith("\n"):
            prompt_text += "\n"

    feedback = f"""# Codex Feedback To ChatGPT

1. final label: `{final_label}`
2. output dir: `{output_dir}`
3. completed stages: {", ".join(completed[:8])}
4. key metrics:
{metrics_text}
5. gate decision: {gate_decision}
6. claim boundary: {claim_boundary}
7. next recommendation: {next_action}
8. protected files modified? `{protected_modified}`
9. original BBS source modified? `{original_modified}`
10. files for review: `{rel(out / '06_FILES_FOR_REVIEW.tsv', root)}`
11. missing context: `{missing_expected or []}`
12. package expected: `chat_bridge_feedback_package.zip`
13. raw README link: `https://raw.githubusercontent.com/Jarvis5272/caor-chat-bridge/main/chat_bridge/00_README_FIRST.md`
14. transactional raw validation: `required by bridge_after_run.sh`
"""

    detection_reason = (
        "requested latest result missing or --auto-detect-latest requested"
        if auto_detected
        else "requested latest result exists and was used"
    )
    status_rows = [
        {"item": "requested_latest_result", "status": "pass", "details": requested_latest},
        {"item": "used_latest_result", "status": "pass", "details": output_dir},
        {"item": "explicit_latest_result_used", "status": "yes" if explicit_latest_result_used else "no", "details": str(explicit_latest_result_used).lower()},
        {"item": "auto_detected", "status": "yes" if auto_detected else "no", "details": str(auto_detected).lower()},
        {"item": "auto_detected_latest_result", "status": "yes" if auto_detected else "no", "details": str(auto_detected).lower()},
        {"item": "latest_final_label", "status": "pass", "details": final_label},
        {"item": "latest_output_dir", "status": "pass", "details": output_dir},
        {"item": "bridge_consistency_status", "status": "pending_validation", "details": "generated_pending_validation"},
        {"item": "reason", "status": "pass", "details": detection_reason},
        {"item": "latest result requested", "status": "pass", "details": requested_latest},
        {"item": "latest result used", "status": "pass", "details": output_dir},
        {"item": "latest result detection mode", "status": "auto_detected" if auto_detected else "explicit", "details": str(auto_detected)},
        {"item": "latest result detected", "status": "pass", "details": output_dir},
        {"item": "files copied", "status": "pass", "details": "0 source artifact files copied; bridge files generated only"},
        {"item": "files skipped", "status": "pass", "details": str(len(scan_skipped) + len(read_skipped))},
        {"item": "large files skipped", "status": "pass", "details": str(large_count)},
        {"item": "missing expected files", "status": "warn" if missing_expected else "pass", "details": ", ".join(missing_expected) or "0"},
        {"item": "required bridge files present", "status": "pass", "details": f"{len(BRIDGE_FILES)}/{len(BRIDGE_FILES)}"},
        {"item": "package path", "status": "pass", "details": "chat_bridge_feedback_package.zip"},
        {"item": "git branch", "status": "pass", "details": run_git(root, ["rev-parse", "--abbrev-ref", "HEAD"])},
        {"item": "git status summary", "status": "pass", "details": (run_git(root, ["status", "--short"])[:500] or "clean")},
        {"item": "timestamp", "status": "pass", "details": timestamp},
        {"item": "protected files modified", "status": "pass" if protected_modified == "no" else "warn", "details": protected_modified},
        {"item": "original BBS source modified", "status": "pass" if original_modified == "no" else "warn", "details": original_modified},
        {"item": "generated bridge files", "status": "pass", "details": str(len(BRIDGE_FILES))},
        {"item": "read_skipped", "status": "pass", "details": json.dumps(read_skipped, ensure_ascii=False)},
        {"item": "scan_skipped", "status": "pass", "details": json.dumps(scan_skipped, ensure_ascii=False)},
    ]

    protected_out_rows = []
    if protected_rows:
        for row in protected_rows:
            protected_out_rows.append(
                {
                    "protected_path": row.get("protected_path", row.get("path", "")),
                    "modified": row.get("modified", row.get("modified_by_this_task", "")),
                    "status": row.get("status", ""),
                    "notes": row.get("notes", ""),
                }
            )
    else:
        protected_out_rows.append(
            {
                "protected_path": "missing",
                "modified": "unknown",
                "status": "missing",
                "notes": "no_protected_files_modified.tsv missing in latest result",
            }
        )

    original_out_rows = []
    if original_rows:
        for row in original_rows:
            original_out_rows.append(
                {
                    "source_path": row.get("source_path", row.get("path", "")),
                    "modified": row.get("modified", row.get("modified_by_this_task", "")),
                    "status": row.get("status", ""),
                    "notes": row.get("notes", ""),
                }
            )
    else:
        original_out_rows.append(
            {
                "source_path": "missing",
                "modified": "unknown",
                "status": "missing",
                "notes": "original_bbs_unchanged_audit.tsv missing in latest result",
            }
        )

    open_questions = f"""# Open Questions

- Gate fail/stop 后，是否需要重设计 global search / sync witness 机制？
- `{output_dir}` 缺失的 expected context 是否可接受，还是需要指定另一个 `--latest-result`？
- ChatGPT 是否认可当前 claim boundary：sync dry-run only，不写 benchmark success？
- 下一轮是否需要用户批准启动新实验，或只做报告审查？
"""

    bridge_usage = """# ChatGPT-Codex Bridge Usage

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
"""

    writes: dict[str, str] = {
        "00_README_FIRST.md": readme,
        "01_CURRENT_STATE_CN.md": current_state,
        "02_LATEST_CODEX_RESULT.json": json_dump(latest_result),
        "04_ACTIVE_CLAIM_BOUNDARY_CN.md": claim_md,
        "05_NEXT_ACTION_CN.md": next_action_md,
        "07_LAST_CHATGPT_PROMPT_TO_CODEX.md": prompt_text,
        "08_CODEX_FEEDBACK_TO_CHATGPT.md": feedback,
        "codex_final_feedback.md": feedback,
        "12_OPEN_QUESTIONS_CN.md": open_questions,
        "13_BRIDGE_USAGE_CN.md": bridge_usage,
    }
    for name, content in writes.items():
        (out / name).write_text(content, encoding="utf-8")

    write_tsv(
        out / "03_RUN_LEDGER.tsv",
        ledger_rows,
        [
            "timestamp",
            "final_label",
            "output_dir",
            "candidate_or_track",
            "stage_reached",
            "gate_decision",
            "target_met",
            "claim_boundary",
            "protected_files_modified",
            "original_bbs_source_modified",
            "data_modified",
            "notes",
        ],
    )
    write_tsv(
        out / "06_FILES_FOR_REVIEW.tsv",
        review_rows,
        [
            "priority",
            "path",
            "reason_to_review",
            "expected_content",
            "small_enough_for_git",
            "exists",
            "notes",
        ],
    )
    write_tsv(out / "09_SYNC_STATUS.tsv", status_rows, ["item", "status", "details"])
    write_tsv(out / "10_PROTECTED_AUDIT.tsv", protected_out_rows, ["protected_path", "modified", "status", "notes"])
    write_tsv(out / "11_ORIGINAL_SOURCE_AUDIT.tsv", original_out_rows, ["source_path", "modified", "status", "notes"])

    summary = {
        "final_label": bridge_label,
        "latest_codex_final_label": final_label,
        "chat_bridge_path": rel(out, root),
        "generated_file_count": len(BRIDGE_FILES),
        "latest_result_detected": output_dir,
        "skipped_large_files_count": large_count,
        "missing_expected_files_count": len(missing_expected),
        "protected_files_modified": protected_modified,
        "original_bbs_source_modified": original_modified,
        "next_git_commit_command": 'git add chat_bridge scripts/chat_bridge && git commit -m "Add ChatGPT-Codex bridge workflow"',
    }
    return summary


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--latest-result", help="Path such as results/<run_dir>. If omitted, auto-detect newest results/ directory.")
    parser.add_argument("--final-label-override", help="Force the latest-result final label when the result report is missing or parser-incomplete.")
    parser.add_argument("--prompt-file", help="Optional previous ChatGPT-to-Codex prompt file.")
    parser.add_argument("--auto-detect-latest", action="store_true", help="Auto-detect newest results/ directory, or fall back to it if --latest-result is missing.")
    parser.add_argument("--no-auto-detect", action="store_true", help="Forbid auto-detect/fallback. Requires an existing explicit --latest-result.")
    parser.add_argument("--out", default="chat_bridge", help="Output directory for bridge files.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    summary = build_snapshot(args)
    print(json_dump(summary), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
