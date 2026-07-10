# Experiment Master Plan

## Dependency order

`cross-validation -> number lock -> full-source -> sensitivity / ablation / calibration -> final paper tables`

## Matrix

| phase | experiment | scope | methods | status | dependency |
|---|---|---|---|---|---|
| P0 | result cross-validation | CAPPED_17_MATCHED | current + baselines | planned | none |
| P3 | small sample smoke | tiny full-source sanity | current method only first | planned | P0 pass |
| P3 | full-source small | oligo0 all 1,466 clusters | current 1/8/16 workers + selected baselines | planned | P0 pass |
| P3 | full-source medium | NComms19 365 Dishes all 2,038 clusters | current 1/8/16 + selected baselines | planned | small pass |
| P3 | full-source large | binned_nanopore all 10,000 clusters | current 1/8/16 + feasible baselines | planned | medium pass |
| P5 | parameter sensitivity | representative tiers | K/W/M/certificate grid | planned | full-source pilot |
| P5 | ablation | representative tiers | anchors/evidence/confidence/cross-event | planned | full-source pilot |
| P5 | confidence calibration | representative tiers | current method | planned | ablation data |
| P5 | runtime stability/memory | small/medium/large | current method | planned | P3 |
| Paper | final tables/figures | verified scopes | selected methods | planned | all audits |

## Rules

- No full large experiment before P0 plan is converted to a passing audit.
- No theory-only scaling in place of actual runs.
- No new algorithm candidates in this queue.
