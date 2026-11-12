# Task lifecycle and agent handoffs

This file defines stable task identity and status transitions. For multi-agent ownership and phase checkpointing, follow `ai/coordination-model.md`.

## Task record
Every task gets a stable, never-reused ID (for example `GAME-001` or `KIT-001`). Keep the ID when moving the task between status lists.

A task must state its observable outcome, acceptance checks, likely scope, verification evidence, and dependencies. Keep the global session summary compact; longer sub-item detail belongs in the owning phase tracker.

## Status flow
`Backlog → Ready → In Progress → Done`

Any active work can become `Blocked` when a concrete dependency prevents progress:
- `ai/session-state.md`: concise global summary of active phases/work packages and owners.
- `ai/backlog-tasks.md`: identified but not ready or not prioritized.
- `ai/blocked-tasks.md`: blocked work with its dependency.
- `ai/done-tasks.md`: accepted/completed work.

For phase-based projects, sub-item status changes stay in the phase tracker. Do not move every sub-item through the global board.

## Claiming work
1. Read the latest global summary and the relevant phase tracker from the branch you are working on.
2. Claim the phase or substantial work package by recording your exact `session_username`, branch, and ownership boundary in the tracker before editing.
3. If the user explicitly asks for a goal with no matching phase/work package, create a stable-ID entry and claim it. Do not invent unrelated work.
4. Never take work owned by another agent or `owner` without explicit user approval. A stale-looking assignment is not permission to take over.
5. Before changing shared ownership/status, re-fetch the latest tracker. Reconcile concurrent changes rather than overwriting them.

## Checkpoint cadence
- Agents may complete several related sub-items before checkpointing.
- Update the phase tracker at a meaningful checkpoint: a coherent work package is complete, a dependency/blocker changes, a design/API decision is made, verification evidence is available, ownership changes, or the agent is handing off.
- Do not record every command, file edit, or tiny subtask in the global session summary.
- Update `ai/session-state.md` only when active phase/work-package ownership, phase status, blocker, priority, milestone, or cross-agent handoff changes.
- Keep chronological detail in the owning tracker only when it helps future execution; avoid diary-style logs.

## Branch and concurrency hygiene
- Work on a descriptive branch; do not commit risky work directly to the default branch.
- A phase should have one accountable owner. Split ownership by work package only when boundaries are explicit and dependencies/file ownership are independent.
- Define file/system ownership before parallel implementation. Unity scenes, prefabs, ScriptableObjects, shared interfaces, assembly definitions, and central composition roots are high-conflict assets; assign one owner or serialize changes.
- Parallel agents must not edit the same file or overlapping Unity asset set. Coordinate integration through the phase owner.
- Never force-push, rewrite shared history, or discard another agent's work.

## Handoff
Before stopping, the tracker and handoff must state: stable ID, owner/status, branch, exact stopping point, next step, changed systems, checks/evidence, checks not run, known risks, and decisions waiting. Release ownership when work is handed off or no longer actively owned.

## Independent review
Use a different AI/provider for meaningful code changes and changes to architecture, save data, security, release/build, or agent safety/workflow rules. Give the reviewer the complete diff and ask for severity-ranked findings. If unavailable, mark review pending; do not call self-review independent.
