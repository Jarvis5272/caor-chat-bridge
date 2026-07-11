# ACOR Latest for ChatGPT

Generated: `2026-07-11T13:35:49+08:00`  
Commit marker: `caor-bridge-v3-20260711T133549+0800-d6a32e60d575`

## Current state

- Project goal: validate and scale an online prefix-only CleanIDS reconstruction method for the paper, with auditable quality, latency, determinism, and leakage boundaries.
- Mode: `paper_experiment_pipeline`
- Latest research final label: `FINAL_RESULT_CROSS_VALIDATION_PASS_AND_NUMBERS_LOCKED`
- Latest research output: `results/final_result_cross_validation_20260711`
- Phase: `P0 completed, numbers locked`
- Latest task event: `CAPPED17_BASELINE_LOCK_BLOCKED` at `results/capped17_unified_baseline_lock_20260711`.

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
- locked CAPPED_17_MATCHED scope.
- locked Accuracy / Exact / Mean ED.
- locked end-to-end current-method runtime and Prefix/s.
- 100% determinism across 9 reruns and workers.
- no-leakage PASS.
- online prefix-only protocol.

Cannot use yet:
- retired 63.3 / 9.6 / 5.3 runtime.
- old speedup values.
- baseline speedup not rerun under the same end-to-end boundary.
- full-source scalability.
- parameter sensitivity, ablation, confidence calibration, or new large-scale results.


## Next actions

- Codex: review split quality/runtime locks; do not start baselines or further runtime reruns automatically.
- Paper Project: update Source of Truth and Claim Matrix using the locked P0 values; remove old runtime and speedup claims.

## Key pointers

- Machine-readable state: `https://raw.githubusercontent.com/Jarvis5272/caor-chat-bridge/main/chat_bridge/LATEST_RESULT.json`
- Paper sync: `https://raw.githubusercontent.com/Jarvis5272/caor-chat-bridge/main/chat_bridge/PAPER_SYNC_LATEST.md`
- Local number lock: `results/final_result_cross_validation_20260711/FINAL_RESULT_LOCK_V1.tsv`
- Local P0 report: `results/final_result_cross_validation_20260711/FINAL_RESULT_CROSS_VALIDATION_REPORT_CN.md`

## Remote sync

- Status: `verified`
- Verified: `true`
- Transport: `ssh22`
- Commit: `7b944f1ff5377875fb5613c2a26a18216d54165f`
- Automatic retry: user-level timer every 10 minutes while `verified=false`; no repeated commit after verification.
- Fallback zip: disaster recovery only, not the normal per-task workflow.
- This document marker: `caor-bridge-v3-20260711T133549+0800-d6a32e60d575`
