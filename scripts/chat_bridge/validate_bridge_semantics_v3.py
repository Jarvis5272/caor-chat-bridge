#!/usr/bin/env python3
"""Validate Bridge V3 semantics against the locked P0 contract."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


LABEL = "FINAL_RESULT_CROSS_VALIDATION_PASS_AND_NUMBERS_LOCKED"
OUTPUT = "results/final_result_cross_validation_20260711"
STALE = [
    "BBS-free sync dry-run only",
    "active track: missing",
    "selected candidate: missing",
    '"selected_candidate": "missing"',
    '"completed_stages": [\n    "missing"',
    "CHAT_BRIDGE_WORKFLOW_INITIALIZED_WITH_MISSING_CONTEXT",
    "results/final_result_cross_validation_20260711/leakage_audit.tsv\tmissing expected context",
]


def args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--bridge", default="chat_bridge")
    p.add_argument("--out", default="results/chat_bridge_v3_repair_20260711/BRIDGE_V3_SEMANTIC_VALIDATION.tsv")
    return p.parse_args()


def main() -> int:
    a = args(); bridge = Path(a.bridge); out = Path(a.out)
    state = json.loads((bridge / "LATEST_RESULT.json").read_text(encoding="utf-8"))
    active_task = json.loads((bridge / "ACTIVE_TASK.json").read_text(encoding="utf-8"))
    entry = (bridge / "LATEST_FOR_CHATGPT.md").read_text(encoding="utf-8")
    paper = (bridge / "PAPER_SYNC_LATEST.md").read_text(encoding="utf-8")
    active_files = ["LATEST_FOR_CHATGPT.md", "LATEST_RESULT.json", "PAPER_SYNC_LATEST.md", "00_README_FIRST.md", "01_CURRENT_STATE_CN.md", "02_LATEST_CODEX_RESULT.json", "03_RUN_LEDGER.tsv", "04_ACTIVE_CLAIM_BOUNDARY_CN.md", "05_NEXT_ACTION_CN.md", "06_FILES_FOR_REVIEW.tsv", "08_CODEX_FEEDBACK_TO_CHATGPT.md", "12_OPEN_QUESTIONS_CN.md", "13_BRIDGE_USAGE_CN.md"]
    rows = []
    def check(item, ok, expected, observed, notes=""):
        rows.append({"check_item": item, "status": "pass" if ok else "fail", "expected": expected, "observed": observed, "notes": notes})
    check("schema", state.get("schema") == "caor_bridge_v3", "caor_bridge_v3", state.get("schema"))
    check("mode", state.get("mode") == "paper_experiment_pipeline", "paper_experiment_pipeline", state.get("mode"))
    check("final_label", state.get("final_label") == LABEL, LABEL, state.get("final_label"))
    check("output_dir", state.get("output_dir") == OUTPUT, OUTPUT, state.get("output_dir"))
    check("phase", state.get("phase") == "p0_result_lock_complete", "p0_result_lock_complete", state.get("phase"))
    s = state.get("scope", {})
    for key, value in (("conditions",17),("dataset_cluster_pairs",16000),("prefix_rows",82462),("prefix_read_uses",428322)):
        check(f"scope_{key}", s.get(key) == value, value, s.get(key))
    q = state.get("quality", {})
    for key, value in (("accuracy",0.966048954608200),("exact",0.348475661516820),("mean_edit_distance",4.280116902330771)):
        observed=q.get(key); check(f"quality_{key}", isinstance(observed,(int,float)) and abs(observed-value)<=1e-15, value, observed)
    r=state.get("runtime", {})
    for key, value in (("worker_1",90.13),("worker_8",15.02),("worker_16",9.23)):
        observed=r.get(key,{}).get("median_seconds"); check(f"runtime_{key}", observed == value, value, observed)
    retired=state.get("retired_numbers",{}).get("runtime_seconds",{})
    check("retired_runtime", retired == {"worker_1":63.3,"worker_8":9.6,"worker_16":5.3}, "63.3/9.6/5.3 retired", retired)
    check("no_leakage", state.get("no_leakage",{}).get("status") == "pass", "pass", state.get("no_leakage",{}).get("status"))
    check("paper_sync_status", state.get("paper_sync_status") == "ready", "ready", state.get("paper_sync_status"))
    next_action=state.get("next_codex_action","")
    check("next_codex_action", next_action == active_task.get("next_codex_action"), active_task.get("next_codex_action"), next_action)
    check("entry_under_30kb", len(entry.encode()) < 30*1024, "<30720", len(entry.encode()))
    check("paper_sync_p0_pass", "P0 independent cross-validation passed" in paper, "P0 pass", "present" if "P0 independent cross-validation passed" in paper else "missing")
    for name in active_files:
        text=(bridge/name).read_text(encoding="utf-8")
        found=[x for x in STALE if x in text]
        check(f"no_stale_active_claim:{name}", not found, "none", ";".join(found) if found else "none")
    forbidden_keys={"selected_candidate","completed_stages","main_metrics"}
    check("no_candidate_schema_keys", not (forbidden_keys & set(state)), "none", sorted(forbidden_keys & set(state)))
    check("historical_context_not_control", state.get("historical_context",{}).get("controls_current_pipeline") is False, False, state.get("historical_context",{}).get("controls_current_pipeline"))
    out.parent.mkdir(parents=True,exist_ok=True)
    with out.open("w",encoding="utf-8",newline="") as h:
        w=csv.DictWriter(h,delimiter="\t",fieldnames=list(rows[0]),lineterminator="\n");w.writeheader();w.writerows(rows)
    failures=[x for x in rows if x["status"]!="pass"]
    print(json.dumps({"checks":len(rows),"failures":failures},ensure_ascii=False,indent=2))
    return 0 if not failures else 1


if __name__ == "__main__": raise SystemExit(main())
