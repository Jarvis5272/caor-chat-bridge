# CAOR Chat Bridge Schema V3

Bridge V3 serves the paper experiment pipeline. Current state is organized as: experiment phase, latest research result, locked numbers, claim boundary, paper sync status, next Codex action, next paper action, and remote sync status.

Candidate and frozen-history records remain historical evidence only. They do not control the current paper experiment pipeline.

Stable entry points:

1. `LATEST_FOR_CHATGPT.md`
2. `LATEST_RESULT.json`
3. `PAPER_SYNC_LATEST.md`
4. `ACTIVE_TASK.json`
5. `RESULT_POINTERS.tsv`
