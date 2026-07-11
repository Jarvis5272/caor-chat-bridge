# P0 Paper Sync Latest

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

Generated `2026-07-11T13:35:49+08:00`; marker `caor-bridge-v3-20260711T133549+0800-d6a32e60d575`.
