# ChatGPT-Codex Bridge Mirror

This is a safe standalone ChatGPT-Codex bridge mirror for the ACOR online reconstruction project.

It contains only project-state summary files and bridge scripts. It does not contain raw data, full results, original BBS source, protected code, or large per-read/per-prefix artifacts.

## Start Here

ChatGPT should first read:

`chat_bridge/00_README_FIRST.md`

## Current Latest Result

- latest result: `results/final_full_17dataset_baseline_benchmark_20260707`
- latest final label: `FINAL_FULL_17DATASET_BASELINE_COMPLETE`

## Claim Boundary

### 可以说 (Can claim):
- On 17 datasets same-scope, our BBS-free realtime method achieves accuracy 0.9660 (between kmer_medoid 0.9663 and BBS 0.9698)
- Our method is 7.6× faster than BBS and 5.5× faster than CGBAPC (796 vs 105 vs 146 prefix/s)
- Our method is BBS-free, reference-free, online-only decode
- 10 of 17 target baselines have same-scope results; 5 external baselines and 2 MSA tools are unavailable

### 不能说 (Cannot claim):
- Cannot claim our method exceeds BBS in quality (Δacc = -0.0038)
- Cannot claim our method exceeds CGBAPC in quality (Δacc = -0.0061)
- Cannot claim our method outperforms MUSCLE/VS/BMALA/ITR/CPL (no same-scope results)
- Cannot claim BBS trio harmful is solved (11.1% harmful in BBS trio rows)
- Cannot claim final algorithm success (harmful 6.9% > 5% gate)
- Cannot use historical 4-dataset results for same-scope comparison

## Next Action

Review latest result artifacts and confirm whether another validation step is warranted.

## If Linking From GitHub

If this mirror is pushed to a public GitHub repository, give ChatGPT the raw link:

`https://raw.githubusercontent.com/<USER>/<REPO>/main/chat_bridge/00_README_FIRST.md`

## If Uploading Directly

Upload `chat_bridge_feedback_package.zip` and tell ChatGPT:

Please read this chat_bridge package and update project state from `00_README_FIRST.md`.
