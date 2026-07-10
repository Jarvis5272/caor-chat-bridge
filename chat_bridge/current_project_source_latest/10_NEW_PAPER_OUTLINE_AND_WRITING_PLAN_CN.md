# New Paper Outline and Writing Plan

## Title placeholder

当前方法: Confidence-Aware Streaming Evidence-State Reconstruction for Clean IDS Reads

## Abstract placeholder

We study strict prefix-online per-cluster reconstruction for clean IDS reads. 当前方法 maintains stable anchor evidence, updates anchor-bounded local event state incrementally, and emits confidence-aware consensus outputs without using reference, future reads, or baseline outputs online. CAPPED_17 evidence is promising but provisional until independent validation and full-source scale experiments finish.

## Section outline

1. Introduction
2. Related Work
3. Problem Definition and Streaming Protocol
4. Proposed Method
5. Complexity Analysis
6. Experimental Setup
7. Main Results
8. Scale and Generalization
9. Ablation and Parameter Sensitivity
10. Confidence Calibration
11. Discussion and Limitations
12. Conclusion

## Suggested writing order

Protocol -> Method -> Experiment setup -> Claim boundary -> Related work -> Introduction -> Results after number lock -> Discussion -> Abstract.

## Contributions to preserve

- Realtime per-cluster protocol and strict online boundary.
- Stable-anchor / local-evidence / incremental-state reconstruction structure.
- Fair single-thread vs multi-thread deployment separation.
- Independent validation and full-source scale-depth plan.

## Figure / table plan

- Method flow diagram.
- CAPPED_17 main comparison table.
- Per-dataset quality/runtime table.
- Runtime composite figure.
- 16-panel thread scalability figure.
- Full-source small/medium/large scale curve after actual runs.
- Ablation/sensitivity/calibration tables after actual runs.

## INFOCOM risk

9-page scope is tight. INFOCOM conditional GO requires P0 pass, large full-source actual run, and disciplined claim boundary.

## Forbidden

Do not copy old STWC abstract. Do not write thread/language as contribution. Do not claim full-source scale before actual results.
