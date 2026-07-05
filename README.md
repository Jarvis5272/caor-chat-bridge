# ChatGPT-Codex Bridge Mirror

This is a safe standalone ChatGPT-Codex bridge mirror for the ACOR online reconstruction project.

It contains only project-state summary files and bridge scripts. It does not contain raw data, full results, original BBS source, protected code, or large per-read/per-prefix artifacts.

## Start Here

ChatGPT should first read:

`chat_bridge/00_README_FIRST.md`

## Current Latest Result

- latest result: `results/scc_sparse_consistency_certificate_theory_note_20260705`
- latest final label: `SCC_THEORY_READY_FOR_HAND_TOY`

## Claim Boundary

An event `e` may be accepted only if:

1. paired witness unique；
2. bounded counterfactual delta over no-event and bounded competitors is at least `m`；
3. cross-read order consistency support exceeds `m`；
4. no competing certificate has comparable or stronger dominance；
5. independent support exceeds `m`；
6. all checks stay within `a/W` and the competitor registry remains sparse.

If any condition fails, SCC must output low-confidence/no correction or stop. It cannot widen W, add helper families, use graph/POA/full alignment, or call BBS/EPBSD semantics.


SCC is not guaranteed to cover all useful edits. It has coverage when true edits often have unique sparse identity and positive local counterfactual margin. It becomes refusal-only in repeats, homopolymers, low coverage, cost ties, competing certificate ties, and long-range ambiguity. These cases are not patched; they are reported.

## Next Action

Revise the sync/global-search mechanism before any small reconstruction smoke; review gate matrix and failure taxonomy.

## If Linking From GitHub

If this mirror is pushed to a public GitHub repository, give ChatGPT the raw link:

`https://raw.githubusercontent.com/<USER>/<REPO>/main/chat_bridge/00_README_FIRST.md`

## If Uploading Directly

Upload `chat_bridge_feedback_package.zip` and tell ChatGPT:

Please read this chat_bridge package and update project state from `00_README_FIRST.md`.
