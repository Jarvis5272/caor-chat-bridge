# Bridge V3 Agent Handoff

## Current operating mode

The active mode is `paper_experiment_pipeline`. The current research source of truth is:

- `chat_bridge/LATEST_FOR_CHATGPT.md`
- `chat_bridge/LATEST_RESULT.json`
- `chat_bridge/PAPER_SYNC_LATEST.md`
- `chat_bridge/ACTIVE_TASK.json`
- `chat_bridge/RESULT_POINTERS.tsv`

The latest research result is `FINAL_RESULT_CROSS_VALIDATION_PASS_AND_NUMBERS_LOCKED` at `results/final_result_cross_validation_20260711`.

## Startup protocol

1. Read `LATEST_FOR_CHATGPT.md`.
2. Read `LATEST_RESULT.json`.
3. Read `PAPER_SYNC_LATEST.md`.
4. Read `ACTIVE_TASK.json`.
5. Read `RESULT_POINTERS.tsv`.
6. Verify `BRIDGE_V3_SEMANTIC_VALIDATION.tsv` when working locally.

## Execution boundary

- The current method and P0 lock are frozen.
- The next Codex action is isolated full-source harness preparation.
- A bridge repair task must not start an experiment.
- Plans are not completed results.
- Locked and retired numbers must not be mixed.
- Every research run writes to a fresh result directory and ends with V3 finalize.

## Finalize protocol

```bash
bash scripts/chat_bridge/codex_task_finalize_v3.sh results/<bridge-event-dir> "<FINAL_LABEL>"
```

The old `codex_task_finalize.sh` and `bridge_after_run.sh` delegate to V3.

## Remote workflow

Normal operation uses the stable raw URL:

`https://raw.githubusercontent.com/Jarvis5272/caor-chat-bridge/main/chat_bridge/LATEST_FOR_CHATGPT.md`

The feedback zip is disaster recovery only. If remote sync is unavailable, the user-level retry timer checks every 10 minutes and exits without a new commit once raw verification succeeds.

## Historical compatibility

`FROZEN_HISTORY.tsv` is immutable historical evidence. Historical candidate/frontier records do not control the paper experiment pipeline and must not be restored as current work.

## Protected boundary

Do not modify protected code, original BBS source, raw data, baseline source, evaluator, or P0 locked artifacts during bridge work.

