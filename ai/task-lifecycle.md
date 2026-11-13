# Task lifecycle and agent handoffs

This file describes an optional lightweight task lifecycle and the stronger ownership practices needed for shared work. For multi-agent coordination, also follow `ai/coordination-model.md`.

## Choose the right amount of tracking

- **Small, self-contained request:** work directly from the user's request. No task ID, backlog row, or phase tracker is required.
- **Work spanning sessions or needing prioritization:** create a tracked task with a stable ID and a clear outcome.
- **Substantial or multi-agent initiative:** use a phase tracker; group related sub-items into work packages rather than promoting every checklist item to a global task.
- **Existing issue tracker:** use it as the task source of truth instead of duplicating every ticket in Markdown.

## Tracked task record

Give each task that enters a shared board a stable, never-reused ID (for example `GAME-001` or `KIT-001`). Keep the ID when moving the task between status lists. Do not assign IDs to every small action or checklist item.

A tracked task should state its observable outcome, acceptance checks, likely scope, verification approach/evidence, and dependencies. Keep the global session summary compact; longer sub-item detail belongs in the owning phase tracker.

## Status flow

`Backlog → Ready → In Progress → Done`

Any active tracked work can become `Blocked` when a concrete dependency prevents progress. Use the status lists only when the project benefits from them:
- `ai/session-state.md`: concise global summary of active shared phases/work packages and owners.
- `ai/backlog-tasks.md`: identified but not ready or not prioritized.
- `ai/blocked-tasks.md`: blocked work with its dependency.
- `ai/done-tasks.md`: accepted tracked work.

For phase-based projects, sub-item status changes stay in the phase tracker. Do not move every sub-item through the global board. A project using GitHub Issues or another tracker may map these statuses there instead.

## Claiming shared work

1. Read the latest relevant project instructions and coordination source. For a shared initiative, read the global summary and relevant phase tracker from the branch you are working on.
2. Before parallel editing, claim the phase or substantial work package by recording your session identity, branch, ownership boundary, and status in the agreed coordination source.
3. If the user explicitly asks for a substantial goal with no matching tracked work, create a stable-ID entry or phase and claim it. For a small direct task, proceed without creating a board entry.
4. Never take work owned by another agent or the human owner without explicit user approval. A stale-looking assignment is not permission to take over.
5. Before changing shared ownership/status, re-fetch the latest tracker. Reconcile concurrent changes rather than overwriting them.

## Checkpoint cadence

- Agents may complete several related sub-items before checkpointing.
- Update the phase tracker at a meaningful checkpoint: a coherent work package is complete, a dependency/blocker changes, a design/API decision is made, verification evidence is available, ownership changes, or the agent is handing off.
- Do not record every command, file edit, or tiny subtask in the global session summary.
- Update `ai/session-state.md` only when active shared phase/work-package ownership, phase status, blocker, priority, milestone, or cross-agent handoff changes.
- Keep chronological detail in the owning tracker only when it helps future execution; avoid diary-style logs.

## Branch and concurrency hygiene

- Work on a descriptive branch for changes that need review or could affect shared work; direct commits may be appropriate for low-risk solo changes when the project permits them.
- A substantial shared phase should have one accountable owner. Split ownership by work package only when boundaries are explicit and dependencies/file ownership are independent.
- Define file/system ownership before parallel implementation. Unity scenes, prefabs, ScriptableObjects, shared interfaces, assembly definitions, and central composition roots are high-conflict assets; assign one owner or serialize changes.
- Parallel agents must not edit the same file or overlapping Unity asset set. Coordinate integration through the phase owner.
- Never force-push, rewrite shared history, or discard another agent's work.

## Handoff

For work that spans sessions or owners, record the stable task/phase ID when one exists, owner/status, branch, exact stopping point, next step, changed systems, checks/evidence, checks not run, known risks, and decisions waiting. Release ownership when handing off or when no longer actively owned. Keep handoffs proportionate to the work; a small completed task needs no formal handoff artifact.

## Independent review

Use a different AI/provider for meaningful code changes and changes to architecture, save data, security, release/build, or agent safety/workflow rules. Give the reviewer the complete diff and ask for severity-ranked findings. If unavailable, mark review pending; do not call self-review independent.
