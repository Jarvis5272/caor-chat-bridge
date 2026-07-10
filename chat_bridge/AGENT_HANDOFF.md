# Bridge V2 Agent Handoff Protocol

## Overview

This document defines the startup, execution, and finalize protocol for all agents
(Codex, Claude Code, ChatGPT) working on this project.  Chat context and uploaded
attachments are **NOT authoritative**.  State lives only in:

1. `chat_bridge/ACTIVE_TASK.json`   — what task is active, what is frozen
2. `chat_bridge/FROZEN_HISTORY.tsv` — immutable record of frozen candidates
3. Server `results/`               — actual output and raw data
4. GitHub raw bridge               — remote canonical copy

## Agent Startup Protocol

Every agent MUST follow this sequence on startup:

### Step 1: Read Bridge State

```
Read: chat_bridge/ACTIVE_TASK.json
Read: chat_bridge/FROZEN_HISTORY.tsv
Read: chat_bridge/00_README_FIRST.md
```

### Step 2: Read Controller State

```
Read: <active_output_dir>/controller_state.json
Read: <active_output_dir>/candidate_queue.tsv
Read: <active_output_dir>/frozen_candidates.tsv
Read: <active_output_dir>/final_decision_matrix.tsv
```

### Step 3: Verify Consistency

- ACTIVE_TASK.json `frozen_candidate_count` MUST match row count in FROZEN_HISTORY.tsv.
- ACTIVE_TASK.json `active_output_dir` MUST match controller_state.json `output_dir`.
- ACTIVE_TASK.json `final_label` MUST match controller_state.json `final_label`.
- Every candidate in `frozen_candidates.tsv` MUST have a matching row in FROZEN_HISTORY.tsv.
- Every candidate listed as `tested_*` in `candidate_queue.tsv` MUST be in FROZEN_HISTORY.tsv.

**If any consistency check fails:**
- STOP immediately.
- Do NOT generate algorithm results.
- Do NOT start experiments.
- Report `BRIDGE_V2_STATE_INCONSISTENCY` with the specific mismatch.
- State file names and row counts that disagree.
- Wait for manual resolution.

### Step 4: Determine Action

Based on ACTIVE_TASK.json `task_status`:

| task_status | Action |
|-------------|--------|
| `in_progress` | Resume from `active_frontier`, using `active_output_dir` |
| `resource_checkpoint` | Resume from `active_frontier`, do not re-run frozen |
| `active_research` | Work only on `allowed_candidates` / `active_frontier` and obey the staged gate |
| `frozen_no_admissible_frontier` | Do NOT start new candidates. Report status. Wait for new theory. |
| `target_success` | Do NOT start new work. Report only. |

### Step 5: Restore Active Frontier

- The `active_frontier` array in ACTIVE_TASK.json IS the canonical list of candidates to test.
- Candidates NOT in `active_frontier` and NOT in FROZEN_HISTORY.tsv MUST NOT be created.
- FROZEN_HISTORY.tsv entries are IMMUTABLE — do not modify, do not re-test, do not revise.
- Do NOT restore BAEPC or any historical frozen negative evidence.

## Agent Execution Protocol

During execution, the agent MUST:

1. Write new results to `<active_output_dir>` only (append, never overwrite frozen artifacts).
2. Before implementing a new candidate, verify it is NOT in FROZEN_HISTORY.tsv.
3. Before implementing a new candidate, verify candidate name is NOT a near-duplicate of any frozen name.
4. After generating raw per_prefix data, run anti-degenerate audit vs ALL frozen candidates.
5. If a candidate triggers the duplicate/degenerate rule, freeze it as duplicate and do NOT count as unique.
6. Do NOT modify protected files, BBS source, EPBSD fork, raw data, or evaluator.
7. Do NOT use BBS/EPBSD online, reference online, dataset route, or full alignment.
8. After each candidate completes, update:
   - controller_state.json
   - frozen_candidates.tsv
   - candidate_queue.tsv
   - final_decision_matrix.tsv
   - wave_summary.tsv

## Agent Finalize Protocol

After all work in a session is done:

### Step 1: Pre-Finalize Consistency Check

```
- ACTIVE_TASK.json frozen_candidate_count matches FROZEN_HISTORY.tsv rows
- controller_state.json final_label matches actual last result
- frozen_candidates.tsv row count == ACTIVE_TASK.json frozen_candidate_count
- No gaps between candidate_queue.tsv status and FROZEN_HISTORY.tsv
```

**If any check fails:** Fix state files first, then re-check. Do not finalize with inconsistent state.

### Step 2: Update ACTIVE_TASK.json

Update these fields before finalize:
- `last_agent`: your agent identity
- `last_agent_action`: what you did
- `last_modified_iso`: current ISO 8601 timestamp
- `task_status`: updated status
- `final_label`: updated label
- `active_frontier`: updated (empty if none remaining)
- `frozen_candidate_count`: updated count

### Step 3: Run Bridge Finalize

```bash
bash scripts/chat_bridge/codex_task_finalize.sh results/<run_dir> "<FINAL_LABEL>"
```

This script will:
1. Run automated state consistency check (bridge v2).
2. Regenerate chat_bridge/ snapshot.
3. Local validate.
4. Package.
5. Git push to remote bridge.
6. Raw README verify.
7. If any step fails, exit with error — do NOT claim success.

### Step 4: Report Final Status

Final response MUST include:
- `BRIDGE_V2_CONSISTENCY`: pass/reason
- `FINAL_LABEL`
- `ACTIVE_OUTPUT_DIR`
- `FROZEN_COUNT`
- `ACTIVE_FRONTIER`
- `BRIDGE_PUSH_STATUS`
- `RAW_README_VERIFIED`

## State Conflict Resolution

If two agents produce conflicting ACTIVE_TASK.json states:

1. The agent that detects the conflict MUST stop.
2. Both agents' state files are preserved in `chat_bridge/conflicts/`.
3. Manual resolution by the human user is required.
4. The resolution decision is recorded in `chat_bridge/CONFLICT_RESOLUTION.md`.

## Anti-Patterns (Strictly Forbidden)

- ❌ Reading chat context to determine "what to do next" instead of ACTIVE_TASK.json.
- ❌ Resuming a frozen candidate because "the chat context says so."
- ❌ Modifying FROZEN_HISTORY.tsv (except appending new frozen candidates).
- ❌ Overwriting old results instead of appending.
- ❌ Finalizing with the wrong `run_dir` or `FINAL_LABEL`.
- ❌ Claiming bridge success when raw validation fails.
- ❌ Starting a new candidate without checking FROZEN_HISTORY.tsv for duplicates.
- ❌ Restoring BAEPC or other historical frozen evidence as active.

---

## Migration Event: Current Project Source Refresh (2026-07-10)

- Final label: `CURRENT_PROJECT_SOURCE_REFRESH_AND_UPLOAD_PACKAGE_READY`
- Output dir: `results/current_project_source_refresh_20260710`
- Old STWC project files retired from active ChatGPT Project source package.
- Archive dir: `archive/legacy_stwc_project_context_20260710`
- New upload source dir: `results/current_project_source_refresh_20260710/UPLOAD_TO_CHATGPT_PROJECT`
- New upload zip: `results/current_project_source_refresh_20260710/CURRENT_PROJECT_SOURCE_UPLOAD_PACKAGE_20260710.zip`
- Bridge mirror: `chat_bridge/current_project_source_latest/`
- Next task: run P0 result cross-validation before locking paper numbers or starting full-source large runs.

