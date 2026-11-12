# Task lifecycle and agent handoffs

This file defines the workflow used by every AI provider. `AGENTS.md` is the short entry point; this file is the detailed procedure.

## Task record

Every task gets a stable ID that is never reused (for example, `GAME-001` or `KIT-001`). Keep the ID in the task text as a prefix when moving it between the board and status lists, such as `KIT-001 — Harden the agent workflow`.

A task must state:
- **Outcome:** one observable result, not a vague activity.
- **Acceptance checks:** what must be true before it can be marked Done.
- **Scope:** likely files/systems and explicit exclusions when useful.
- **Verification:** tests, commands, editor steps, or review evidence expected.
- **Dependencies:** decisions, assets, owner input, or other tasks it waits on.

Keep the session board compact. Put longer investigation notes in a task-specific tracker only when the work genuinely needs one; link it from the task row. Do not create a tracker just to duplicate the board.

## Status flow

`Backlog → Ready → In Progress → Done`

Any active task can move to `Blocked` when a concrete dependency prevents progress. Use the matching file:
- `ai/session-state.md`: Ready and In Progress only.
- `ai/backlog-tasks.md`: identified but not ready or not yet prioritized.
- `ai/blocked-tasks.md`: cannot proceed until the stated blocker clears.
- `ai/done-tasks.md`: accepted/completed work.

When moving a task, preserve its ID, outcome, author/owner, and the useful next-step context. Remove the old row after adding the new one; do not leave duplicate active copies.

## Claiming work

1. Read the latest board from the branch you are working on. Check both status and Author.
2. Claim only a Ready task by setting Author to your exact `session_username` and Status to `In Progress`. Record the branch and a short next step.
3. If the user explicitly asks for a goal that has no matching task, create a task with a new ID directly as In Progress and assign it to yourself. This is the only normal case where an agent creates and claims work in one step.
4. If the user has not supplied a goal and no Ready task exists, ask what they want prioritized. Do not manufacture work to fill an empty board.
5. Never take a task assigned to another agent or `owner` without explicit user authorization. A stale-looking task is not permission to take it over; ask the user.
6. Before updating a shared board, re-fetch the latest version. If its content changed since your read, reconcile the other agent's updates instead of overwriting them. Use the current file SHA so concurrent edits fail safely.

## Branch and change hygiene

- Start from the current default branch unless the user or repository rules specify another base.
- Use a descriptive branch name tied to the agent/task; do not commit risky work directly to the default branch.
- Keep changes focused. Ask before a change that crosses more than about five files, changes public APIs, or expands beyond the task's acceptance checks.
- Do not force-push, rewrite shared history, or discard another agent's work.
- Do not include secrets, generated Unity folders, or unrequested project-specific changes.

## Handoff

Before stopping, write a handoff that another agent can act on without reconstructing the conversation:
- Task ID and current status/owner.
- Branch and latest commit (if known).
- Exact stopping point and next concrete step.
- Files/systems changed.
- Checks run, results, and evidence/log paths.
- Checks not run and why; list precise human/editor/device steps.
- Known defects, risks, unresolved review findings, and owner decisions waiting.

Release ownership when you move a task out of In Progress. Keep the Author only while the same agent still actively owns the task; do not leave an inactive agent holding work indefinitely.

## Independent review

Use a different AI/provider for meaningful code changes and changes to architecture, save data, security, release/build configuration, or agent safety/workflow rules. Give the reviewer the full diff and ask for severity-ranked findings with file/line, failure mode, reproduction, and fix. The author must resolve findings or record why a finding is not applicable. If a second reviewer is unavailable, label the review as pending rather than claiming it passed.
