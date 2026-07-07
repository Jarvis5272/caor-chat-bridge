# ChatGPT-Codex Bridge Mirror

This is a safe standalone ChatGPT-Codex bridge mirror for the ACOR online reconstruction project.

It contains only project-state summary files and bridge scripts. It does not contain raw data, full results, original BBS source, protected code, or large per-read/per-prefix artifacts.

## Start Here

ChatGPT should first read:

`chat_bridge/00_README_FIRST.md`

## Current Latest Result

- latest result: `results/final_full_17dataset_baseline_benchmark_20260707`
- latest final label: `FINAL_BENCHMARK_AUDIT_SCOPE_MISMATCH_EXTERNAL_PENDING`

## Claim Boundary

### Can claim:
- OUR_REALTIME_METHOD accuracy 0.9660 on CAPPED_17_MATCHED (82,462 rows)
- Wall-clock runtime 103.53s, 796 prefix/s, BBS-free online decode
- Row keys verified (SHA256: 7ac2b177...)
- CAPPED_17_MATCHED is the defined fair comparison scope for ALL methods

### Cannot claim:
- Cannot claim speedup vs BBS/CGBAPC/kmer_medoid until they are rerun on same keys
- Cannot claim position vs MUSCLE/VS/BMALA/ITR/CPL until they complete
- Cannot claim FULL_17 (495K) scope completion
- Cannot use historical 495K metrics for direct comparison with 82K scope

## Next Action

Review latest result artifacts and confirm whether another validation step is warranted.

## If Linking From GitHub

If this mirror is pushed to a public GitHub repository, give ChatGPT the raw link:

`https://raw.githubusercontent.com/<USER>/<REPO>/main/chat_bridge/00_README_FIRST.md`

## If Uploading Directly

Upload `chat_bridge_feedback_package.zip` and tell ChatGPT:

Please read this chat_bridge package and update project state from `00_README_FIRST.md`.
