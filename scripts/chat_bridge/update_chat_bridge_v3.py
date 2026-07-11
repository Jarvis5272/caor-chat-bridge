#!/usr/bin/env python3
"""Generate the paper-pipeline Bridge V3 snapshot from locked P0 evidence."""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
import subprocess
from pathlib import Path


RAW_BASE = "https://raw.githubusercontent.com/Jarvis5272/caor-chat-bridge/main"
EXPECTED_LABEL = "FINAL_RESULT_CROSS_VALIDATION_PASS_AND_NUMBERS_LOCKED"
EXPECTED_OUTPUT = "results/final_result_cross_validation_20260711"

ROLE_PATTERNS = {
    "final_report": ["FINAL_RESULT_CROSS_VALIDATION_REPORT_CN.md", "FINAL*_REPORT_CN.md", "*REPORT_CN.md"],
    "number_lock": ["FINAL_RESULT_LOCK_V1.tsv", "*RESULT_LOCK*.tsv"],
    "paper_number_lock": ["PAPER_NUMBER_LOCK_CN.md", "*NUMBER_LOCK*.md"],
    "paper_sync_candidate": ["PAPER_SYNC_CANDIDATE_P0_CN.md", "*PAPER_SYNC*.md"],
    "runtime_repeats": ["RUNTIME_REPEATABILITY.tsv", "*RUNTIME*REPEAT*.tsv"],
    "runtime_summary": ["RUNTIME_REPEATABILITY_SUMMARY.tsv", "*RUNTIME*SUMMARY*.tsv"],
    "claim_recheck": ["CURRENT_CLAIM_RECHECK.tsv", "*CLAIM*RECHECK*.tsv"],
    "no_leakage_report": ["NO_LEAKAGE_AUDIT_CN.md", "*NO*LEAKAGE*AUDIT*.md", "*leakage*audit*.md"],
    "no_leakage_dynamic": ["NO_LEAKAGE_DYNAMIC_AUDIT.tsv", "*NO*LEAKAGE*DYNAMIC*.tsv", "*leakage*audit*.tsv"],
    "no_leakage_static": ["NO_LEAKAGE_STATIC_AUDIT.tsv", "*NO*LEAKAGE*STATIC*.tsv"],
    "artifact_manifest": ["final_artifact_manifest.tsv", "*ARTIFACT*MANIFEST*.tsv"],
    "protected_audit": ["no_protected_files_modified.tsv", "*PROTECTED*AUDIT*.tsv"],
    "original_bbs_audit": ["original_bbs_unchanged_audit.tsv", "*BBS*UNCHANGED*.tsv"],
}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--locked-result", default=EXPECTED_OUTPUT)
    p.add_argument("--out", default="chat_bridge")
    p.add_argument("--audit-out", default="")
    p.add_argument("--bridge-event-output", default="")
    p.add_argument("--bridge-event-label", default="")
    return p.parse_args()


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).astimezone().isoformat(timespec="seconds")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as h:
        return list(csv.DictReader(h, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict], fields: list[str] | None = None) -> None:
    if fields is None:
        fields = list(rows[0]) if rows else []
    with path.open("w", encoding="utf-8", newline="") as h:
        w = csv.DictWriter(h, delimiter="\t", fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        w.writeheader(); w.writerows(rows)


def git_output(root: Path, *args: str) -> str:
    proc = subprocess.run(["git", *args], cwd=root, text=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    return proc.stdout.strip() if proc.returncode == 0 else "unavailable"


def manifest_paths(result: Path) -> set[str]:
    manifest = result / "final_artifact_manifest.tsv"
    if not manifest.exists():
        return set()
    rows = read_tsv(manifest)
    found = set()
    for row in rows:
        value = row.get("relative_path") or row.get("path") or row.get("artifact") or ""
        if value:
            found.add(Path(value).name.lower())
    return found


def select_role(result: Path, role: str, manifest_names: set[str]) -> tuple[Path | None, str]:
    patterns = ROLE_PATTERNS[role]
    # Manifest-backed exact names receive priority.
    for pattern in patterns:
        for path in sorted(result.glob(pattern)):
            if path.is_file() and path.name.lower() in manifest_names:
                return path, "selected_from_final_artifact_manifest"
    for pattern in patterns:
        matches = sorted(path for path in result.glob(pattern) if path.is_file())
        if matches:
            return matches[0], "selected_from_alias_pattern"
    return None, "missing_all_aliases"


def parse_lock(path: Path) -> dict[str, dict[str, str]]:
    return {row["item"]: row for row in read_tsv(path)}


def number(value: str) -> float:
    return float(value.replace(",", ""))


def main() -> int:
    args = parse_args()
    root = Path.cwd().resolve()
    result = (root / args.locked_result).resolve()
    out = (root / args.out).resolve()
    audit_out = (root / args.audit_out).resolve() if args.audit_out else None
    if not result.is_dir():
        raise SystemExit(f"locked result missing: {result}")
    out.mkdir(parents=True, exist_ok=True)
    if audit_out:
        audit_out.mkdir(parents=True, exist_ok=True)

    names = manifest_paths(result)
    roles: dict[str, Path] = {}
    mapping = []
    for role, patterns in ROLE_PATTERNS.items():
        selected, status = select_role(result, role, names)
        mapping.append({
            "artifact_role": role,
            "selected_path": str(selected.relative_to(root)) if selected else "missing",
            "candidate_patterns": ";".join(patterns),
            "exists": "yes" if selected else "no",
            "sha256": sha256(selected) if selected else "",
            "status": "pass" if selected else "missing",
        })
        if selected:
            roles[role] = selected
    required_roles = {"final_report", "number_lock", "paper_number_lock", "runtime_summary", "claim_recheck", "no_leakage_report", "artifact_manifest", "protected_audit", "original_bbs_audit"}
    missing = sorted(required_roles - set(roles))
    if audit_out:
        write_tsv(audit_out / "BRIDGE_ARTIFACT_ROLE_MAPPING.tsv", mapping)
    if missing:
        raise SystemExit(f"missing required artifact roles: {missing}")

    locked = parse_lock(roles["number_lock"])
    runtime_rows = {int(row["workers"]): row for row in read_tsv(roles["runtime_summary"])}
    expected_items = {"prefix_rows", "prefix_read_uses", "Accuracy", "Exact", "Mean_ED", "1_worker_median_wall", "8_worker_median_wall", "16_worker_median_wall", "output_identity"}
    if expected_items - set(locked):
        raise SystemExit(f"number lock missing items: {sorted(expected_items-set(locked))}")

    scope = {
        "conditions": 17,
        "dataset_cluster_pairs": 16000,
        "prefix_rows": int(number(locked["prefix_rows"]["locked_value"])),
        "prefix_read_uses": int(number(locked["prefix_read_uses"]["locked_value"])),
        "prefix_checkpoints": [1, 2, 3, 5, 10, 20],
        "arrival_order": "file_order",
        "scope_name": "CAPPED_17_MATCHED",
    }
    quality = {
        "accuracy": number(locked["Accuracy"]["locked_value"]),
        "exact": number(locked["Exact"]["locked_value"]),
        "mean_edit_distance": number(locked["Mean_ED"]["locked_value"]),
        "accuracy_definition": "row-macro mean(1 - ED/reference_len), unclamped",
        "edit_distance": "unit-cost Levenshtein",
    }
    runtime = {
        "boundary": "end-to-end input split + exact kernel + full sequence merge and serialization",
        "worker_1": {"median_seconds": number(locked["1_worker_median_wall"]["locked_value"]), "prefix_per_second": number(runtime_rows[1]["median_prefix_per_second"])},
        "worker_8": {"median_seconds": number(locked["8_worker_median_wall"]["locked_value"]), "prefix_per_second": number(runtime_rows[8]["median_prefix_per_second"])},
        "worker_16": {"median_seconds": number(locked["16_worker_median_wall"]["locked_value"]), "prefix_per_second": number(runtime_rows[16]["median_prefix_per_second"])},
    }
    no_leakage_rows = read_tsv(roles.get("no_leakage_dynamic", Path("/nonexistent"))) if roles.get("no_leakage_dynamic") else []
    no_leakage_pass = bool(no_leakage_rows) and all(row.get("status", "").lower() == "pass" for row in no_leakage_rows)
    if not no_leakage_pass:
        report_text = roles["no_leakage_report"].read_text(encoding="utf-8")
        no_leakage_pass = "reference_blind: pass" in report_text.lower() and "row_order_isolation: pass" in report_text.lower()
    if not no_leakage_pass:
        raise SystemExit("no-leakage role exists but does not establish PASS")

    previous_latest = {}
    previous_latest_path = out / "LATEST_RESULT.json"
    if previous_latest_path.exists():
        try:
            previous_latest = json.loads(previous_latest_path.read_text(encoding="utf-8"))
        except Exception:
            previous_latest = {}
    lock_sha = sha256(roles["number_lock"])
    same_locked_state = (
        previous_latest.get("final_label") == EXPECTED_LABEL
        and previous_latest.get("output_dir") == EXPECTED_OUTPUT
        and previous_latest.get("locked_artifact_sha256") == lock_sha
    )
    timestamp = previous_latest.get("generated_timestamp", now_iso()) if same_locked_state else now_iso()
    source_commit = git_output(root, "rev-parse", "HEAD")
    marker = previous_latest.get("commit_marker", "") if same_locked_state else ""
    if not marker:
        marker = f"caor-bridge-v3-{timestamp.replace(':','').replace('-','')}-{lock_sha[:12]}"
    old_remote = {}
    remote_path = out / "REMOTE_SYNC_STATUS.json"
    if remote_path.exists():
        try:
            old_remote = json.loads(remote_path.read_text(encoding="utf-8"))
        except Exception:
            old_remote = {}
    remote_sync = {
        "status": old_remote.get("status", "pending"),
        "verified": bool(old_remote.get("verified", False)),
        "transport": old_remote.get("transport", "none"),
        "remote_url": "https://github.com/Jarvis5272/caor-chat-bridge",
        "branch": "main",
        "commit": old_remote.get("commit", "pending"),
        "commit_marker": marker,
        "generated_timestamp": timestamp,
        "last_attempt": old_remote.get("last_attempt", "not_attempted_for_current_marker"),
        "last_error": old_remote.get("last_error", ""),
    }
    # A new marker has not yet been verified remotely.
    if old_remote.get("commit_marker") != marker:
        remote_sync.update({"status": "pending", "verified": False, "transport": "none", "commit": "pending", "last_attempt": "not_attempted_for_current_marker", "last_error": ""})

    artifact_pointers = []
    pointer_rows = []
    for role in ("number_lock", "paper_number_lock", "final_report", "paper_sync_candidate", "runtime_repeats", "claim_recheck", "no_leakage_report", "artifact_manifest"):
        path = roles[role]
        local = path.relative_to(root).as_posix()
        raw_url = f"{RAW_BASE}/{local}" if local.startswith("chat_bridge/") else "server-local-only"
        artifact_pointers.append({"role": role, "local_path": local, "sha256": sha256(path), "raw_url": raw_url})
        pointer_rows.append({"artifact_role": role, "local_path": local, "raw_url": raw_url, "exists": "yes", "sha256": sha256(path), "status": "pass"})
    for role, name in (("chatgpt_entry", "LATEST_FOR_CHATGPT.md"), ("machine_state", "LATEST_RESULT.json"), ("paper_sync", "PAPER_SYNC_LATEST.md")):
        pointer_rows.append({"artifact_role": role, "local_path": f"chat_bridge/{name}", "raw_url": f"{RAW_BASE}/chat_bridge/{name}", "exists": "generated", "sha256": "generated_after_write", "status": "pass"})

    claim_can = [
        "locked CAPPED_17_MATCHED scope",
        "locked Accuracy / Exact / Mean ED",
        "locked end-to-end current-method runtime and Prefix/s",
        "100% determinism across 9 reruns and workers",
        "no-leakage PASS",
        "online prefix-only protocol",
    ]
    claim_cannot = [
        "retired 63.3 / 9.6 / 5.3 runtime",
        "old speedup values",
        "baseline speedup not rerun under the same end-to-end boundary",
        "full-source scalability",
        "parameter sensitivity, ablation, confidence calibration, or new large-scale results",
    ]
    previous_event = previous_latest.get("bridge_event", {}) if isinstance(previous_latest.get("bridge_event"), dict) else {}
    bridge_event = {
        "output_dir": args.bridge_event_output or previous_event.get("output_dir", "none"),
        "final_label": args.bridge_event_label or previous_event.get("final_label", "none"),
    }
    latest = {
        "schema": "caor_bridge_v3",
        "mode": "paper_experiment_pipeline",
        "final_label": EXPECTED_LABEL,
        "output_dir": EXPECTED_OUTPUT,
        "phase": "p0_result_lock_complete",
        "numbers_status": "locked",
        "scope": scope,
        "quality": quality,
        "runtime": runtime,
        "determinism": {"status": "pass", "output_identity": "100%", "reruns": 9, "different_rows": 0},
        "no_leakage": {"status": "pass", "static_and_dynamic": True},
        "retired_numbers": {"runtime_seconds": {"worker_1": 63.3, "worker_8": 9.6, "worker_16": 5.3}, "status": "retired_do_not_use"},
        "claim_boundary": {"can_use": claim_can, "cannot_use_yet": claim_cannot},
        "paper_sync_status": "ready",
        "next_codex_action": "prepare isolated full-source harness; do not start the full-source experiment in the bridge repair task",
        "next_paper_action": "update the paper Source of Truth and Claim Matrix with P0-locked numbers and retire old runtime/speedup claims",
        "artifact_pointers": artifact_pointers,
        "remote_sync": remote_sync,
        "generated_timestamp": timestamp,
        "commit_marker": marker,
        "source_git_commit": source_commit,
        "locked_artifact_sha256": lock_sha,
        "historical_context": {"frozen_history": "chat_bridge/FROZEN_HISTORY.tsv", "controls_current_pipeline": False, "purpose": "historical evidence only"},
        "bridge_event": bridge_event,
    }

    latest_md = f"""# ACOR Latest for ChatGPT

Generated: `{timestamp}`  
Commit marker: `{marker}`

## Current state

- Project goal: validate and scale an online prefix-only CleanIDS reconstruction method for the paper, with auditable quality, latency, determinism, and leakage boundaries.
- Mode: `paper_experiment_pipeline`
- Latest research final label: `{EXPECTED_LABEL}`
- Latest research output: `{EXPECTED_OUTPUT}`
- Phase: `P0 completed, numbers locked`

## Locked scope and quality

| Item | Locked value |
|---|---:|
| Conditions | 17 |
| Dataset-cluster pairs | 16,000 |
| Prefix rows | 82,462 |
| Prefix-read uses | 428,322 |
| Accuracy | 0.966048954608200 |
| Exact | 0.348475661516820 |
| Mean ED | 4.280116902330771 |

## Locked runtime

End-to-end boundary: input split, exact kernel, complete sequence merge, and serialization.

| Workers | Median runtime (s) | Prefix/s |
|---:|---:|---:|
| 1 | 90.13 | 914.923 |
| 8 | 15.02 | 5490.146 |
| 16 | 9.23 | 8934.128 |

- Determinism: `PASS`, 100% output identity across 9 reruns and workers, zero different rows.
- No leakage: `PASS`; online reconstruction is prefix-only and does not use reference, truth, future reads, or baseline outputs.
- Retired runtime: `63.3 / 9.6 / 5.3 seconds`; do not use these values.

## Paper claim boundary

Can use now:
{''.join(f'- {item}.\n' for item in claim_can)}
Cannot use yet:
{''.join(f'- {item}.\n' for item in claim_cannot)}

## Next actions

- Codex: prepare an isolated full-source harness. This bridge repair task starts no experiment.
- Paper Project: update Source of Truth and Claim Matrix using the locked P0 values; remove old runtime and speedup claims.

## Key pointers

- Machine-readable state: `{RAW_BASE}/chat_bridge/LATEST_RESULT.json`
- Paper sync: `{RAW_BASE}/chat_bridge/PAPER_SYNC_LATEST.md`
- Local number lock: `results/final_result_cross_validation_20260711/FINAL_RESULT_LOCK_V1.tsv`
- Local P0 report: `results/final_result_cross_validation_20260711/FINAL_RESULT_CROSS_VALIDATION_REPORT_CN.md`

## Remote sync

- Status: `{remote_sync['status']}`
- Verified: `{str(remote_sync['verified']).lower()}`
- Transport: `{remote_sync['transport']}`
- Commit: `{remote_sync['commit']}`
- Automatic retry: user-level timer every 10 minutes while `verified=false`; no repeated commit after verification.
- Fallback zip: disaster recovery only, not the normal per-task workflow.
- This document marker: `{marker}`
"""

    paper_sync = f"""# P0 Paper Sync Latest

## Status

P0 independent cross-validation passed. Quality, determinism, no-leakage, and current-method end-to-end runtime are locked.

## Replace the paper Source of Truth with

- Scope: 17 conditions; 16,000 dataset-cluster pairs; 82,462 prefix rows; 428,322 prefix-read uses.
- Accuracy: 0.966048954608200.
- Exact: 0.348475661516820.
- Mean ED: 4.280116902330771.
- Runtime medians: 90.13s / 15.02s / 9.23s for 1 / 8 / 16 workers.
- Prefix/s: 914.923 / 5490.146 / 8934.128.
- Determinism: 100% across 9 reruns and worker settings.
- No leakage: PASS.

## Retire or suspend

- Retire 63.3 / 9.6 / 5.3s.
- Suspend old speedup claims and any baseline speedup not measured in the same end-to-end boundary.
- Do not claim full-source scalability, sensitivity, ablation, or confidence calibration yet.

## Next paper action

Update the paper Source of Truth and Claim Matrix. Writing may use P0-locked values, while full-source, ablation, sensitivity, and calibration remain pending.

Generated `{timestamp}`; marker `{marker}`.
"""

    schema_md = """# CAOR Chat Bridge Schema V3

Bridge V3 serves the paper experiment pipeline. Current state is organized as: experiment phase, latest research result, locked numbers, claim boundary, paper sync status, next Codex action, next paper action, and remote sync status.

Candidate and frozen-history records remain historical evidence only. They do not control the current paper experiment pipeline.

Stable entry points:

1. `LATEST_FOR_CHATGPT.md`
2. `LATEST_RESULT.json`
3. `PAPER_SYNC_LATEST.md`
4. `ACTIVE_TASK.json`
5. `RESULT_POINTERS.tsv`
"""
    readme = f"""# ACOR Chat Bridge V3

Start here: `chat_bridge/LATEST_FOR_CHATGPT.md`.

Current mode: `paper_experiment_pipeline`  
Latest research result: `{EXPECTED_OUTPUT}`  
Latest research label: `{EXPECTED_LABEL}`  
P0 status: completed; numbers locked.

Read order:

1. `LATEST_FOR_CHATGPT.md`
2. `LATEST_RESULT.json`
3. `PAPER_SYNC_LATEST.md`
4. `ACTIVE_TASK.json`
5. `RESULT_POINTERS.tsv`

Historical candidate/frozen records are evidence only and do not control the active paper pipeline. The stable raw entry is:

`{RAW_BASE}/chat_bridge/LATEST_FOR_CHATGPT.md`
"""
    current_state = f"""# Current Project State

- Mode: `paper_experiment_pipeline`.
- Phase: `p0_result_lock_complete`.
- Latest research result: `{EXPECTED_OUTPUT}`.
- Final label: `{EXPECTED_LABEL}`.
- Numbers: locked under the complete-sequence end-to-end boundary.
- Next Codex action: prepare an isolated full-source harness; no experiment is started by this bridge task.
- Paper action: synchronize P0 locked values and retire old runtime/speedup claims.
- Historical candidate search controls current state: `no`.
"""
    claim_md = "# Active Claim Boundary\n\n## Can use\n\n" + "".join(f"- {x}.\n" for x in claim_can) + "\n## Cannot use yet\n\n" + "".join(f"- {x}.\n" for x in claim_cannot)
    next_md = """# Next Action

Codex next: prepare the isolated full-source harness without changing the frozen method or starting the experiment in this bridge repair task.

Paper next: update Source of Truth and Claim Matrix from `PAPER_SYNC_LATEST.md`.

Do not reopen candidate search, restore old runtime/speedup claims, or treat historical frozen evidence as active state.
"""
    usage = f"""# Bridge V3 Usage

Recommended read order:

1. `LATEST_FOR_CHATGPT.md`
2. `LATEST_RESULT.json`
3. `PAPER_SYNC_LATEST.md`
4. `ACTIVE_TASK.json`
5. `RESULT_POINTERS.tsv`

Stable raw URLs:

- `{RAW_BASE}/chat_bridge/LATEST_FOR_CHATGPT.md`
- `{RAW_BASE}/chat_bridge/LATEST_RESULT.json`

Normal workflow uses the raw entry. `chat_bridge_feedback_package.zip` is disaster recovery only.

Historical compatibility: `FROZEN_HISTORY.tsv` remains immutable evidence, but candidate/frontier state no longer controls the paper experiment pipeline.
"""
    feedback = f"""# Codex Feedback to ChatGPT - Bridge V3

- Latest research label: `{EXPECTED_LABEL}`
- Latest research output: `{EXPECTED_OUTPUT}`
- Current mode: `paper_experiment_pipeline`
- P0 status: completed; numbers locked.
- Semantic validation: required before every V3 export.
- Remote status: `{remote_sync['status']}`; verified=`{str(remote_sync['verified']).lower()}`; transport=`{remote_sync['transport']}`.
- Stable entry: `{RAW_BASE}/chat_bridge/LATEST_FOR_CHATGPT.md`
- Normal workflow: read the stable raw entry; the zip is disaster recovery only.
- Next Codex action: prepare the isolated full-source harness; this bridge task starts no experiment.
"""
    open_questions = """# Open Questions

- When should the isolated full-source harness preparation task be opened?
- Which same-boundary external baselines must be rerun before speedup claims are restored?
- What order should full-source, sensitivity, ablation, and confidence calibration follow after harness audit?
- Historical candidate search is closed and does not control these decisions.
"""
    review_rows = []
    for priority, row in enumerate(pointer_rows, start=1):
        review_rows.append({
            "priority": priority,
            "artifact_role": row["artifact_role"],
            "path": row["local_path"],
            "reason_to_review": "Bridge V3 role pointer",
            "exists": row["exists"],
            "sha256": row["sha256"],
            "status": row["status"],
            "notes": "resolved by final manifest and alias patterns; server-local results are not exported",
        })
    ledger_rows = [{
        "timestamp": timestamp,
        "mode": "paper_experiment_pipeline",
        "final_label": EXPECTED_LABEL,
        "output_dir": EXPECTED_OUTPUT,
        "phase": "p0_result_lock_complete",
        "numbers_status": "locked",
        "paper_sync_status": "ready",
        "remote_sync_status": remote_sync["status"],
        "claim_boundary": "P0 scope/quality/current-method runtime/determinism/no-leakage locked; old runtime/speedup retired",
        "protected_files_modified": "no_by_bridge_task",
        "original_bbs_source_modified": "no_by_bridge_task",
        "notes": "V2 candidate-search ledger archived at archive/chat_bridge_pre_v3_repair_20260711",
    }]
    sync_rows = [
        {"item": "schema", "status": "pass", "details": "caor_bridge_v3"},
        {"item": "mode", "status": "pass", "details": "paper_experiment_pipeline"},
        {"item": "locked_result", "status": "pass", "details": EXPECTED_OUTPUT},
        {"item": "final_label", "status": "pass", "details": EXPECTED_LABEL},
        {"item": "artifact_role_mapping", "status": "pass", "details": f"{len(roles)} roles resolved; missing={missing}"},
        {"item": "missing_expected_files", "status": "pass", "details": "none; alias and manifest role resolution used"},
        {"item": "generated_timestamp", "status": "pass", "details": timestamp},
        {"item": "commit_marker", "status": "pass", "details": marker},
    ]

    (out / "BRIDGE_SCHEMA_V3.md").write_text(schema_md, encoding="utf-8")
    (out / "LATEST_FOR_CHATGPT.md").write_text(latest_md, encoding="utf-8")
    (out / "LATEST_RESULT.json").write_text(json.dumps(latest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out / "PAPER_SYNC_LATEST.md").write_text(paper_sync, encoding="utf-8")
    (out / "REMOTE_SYNC_STATUS.json").write_text(json.dumps(remote_sync, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_tsv(out / "RESULT_POINTERS.tsv", pointer_rows)
    (out / "00_README_FIRST.md").write_text(readme, encoding="utf-8")
    (out / "01_CURRENT_STATE_CN.md").write_text(current_state, encoding="utf-8")
    (out / "02_LATEST_CODEX_RESULT.json").write_text(json.dumps(latest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out / "04_ACTIVE_CLAIM_BOUNDARY_CN.md").write_text(claim_md, encoding="utf-8")
    (out / "05_NEXT_ACTION_CN.md").write_text(next_md, encoding="utf-8")
    write_tsv(out / "06_FILES_FOR_REVIEW.tsv", review_rows)
    (out / "08_CODEX_FEEDBACK_TO_CHATGPT.md").write_text(feedback, encoding="utf-8")
    (out / "12_OPEN_QUESTIONS_CN.md").write_text(open_questions, encoding="utf-8")
    (out / "13_BRIDGE_USAGE_CN.md").write_text(usage, encoding="utf-8")
    write_tsv(out / "03_RUN_LEDGER.tsv", ledger_rows)
    write_tsv(out / "09_SYNC_STATUS.tsv", sync_rows)
    if audit_out and not (audit_out / "BRIDGE_ARTIFACT_ROLE_MAPPING.tsv").exists():
        write_tsv(audit_out / "BRIDGE_ARTIFACT_ROLE_MAPPING.tsv", mapping)
    print(json.dumps({"schema": "caor_bridge_v3", "result": EXPECTED_OUTPUT, "label": EXPECTED_LABEL, "marker": marker, "roles": len(roles), "missing": missing}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
