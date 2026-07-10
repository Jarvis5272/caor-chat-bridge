# Codex / ChatGPT Workflow

## Role split

ChatGPT:
- task decomposition;
- Codex prompt writing;
- result review;
- paper organization;
- claim boundary enforcement.

Codex:
- code inspection;
- command execution;
- artifact generation;
- boundary/leakage/protected audits;
- bridge finalize.

User:
- copy instructions to Codex;
- upload package / bridge link to ChatGPT;
- decide whether to start next phase.

## Source of truth

`chat_bridge/` is the local state bridge. It must include ACTIVE_TASK, FROZEN_HISTORY, AGENT_HANDOFF, final label, output path, and next action. Plans are not results; theory is not experiment; provisional numbers are not locked.

## Finalize rule

Every Codex task should end with:

```bash
bash scripts/chat_bridge/codex_task_finalize.sh <output_dir> "<FINAL_LABEL>"
```

and the final response should include paths, package/link, protected status, original BBS source status, and caveats.

## Current migration result

This migration creates `results/current_project_source_refresh_20260710/UPLOAD_TO_CHATGPT_PROJECT/` and a zip for manual ChatGPT Project upload. It does not run experiments.
