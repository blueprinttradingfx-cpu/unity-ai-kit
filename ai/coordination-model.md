# Multi-agent coordination model

## Purpose

Coordinate several AI agents without turning a shared session file into a high-frequency micro-task log. The default unit of ownership is a **phase** or a substantial **work package** inside a phase. Sub-items are the execution checklist, not separate global-board tasks.

This is a recommended coordination model, not a requirement to run multiple agents or create phase trackers for every small project. A single-agent or small project can use a lighter version. Keep the ownership boundaries, truthful handoffs, and protection against conflicting edits; tune the concurrency limit, checkpoint cadence, and artifact set to the team.

## Sources of truth

| Artifact | Owns | Update cadence |
|---|---|---|
| `ai/session-state.md` | Global active phases, accountable owners, blockers, priority, next milestone, cross-phase handoff | Only on meaningful coordination changes |
| Phase tracker (for example `ai/phase-<n>-<name>.md`) | Scope, work packages, sub-items, dependencies, acceptance criteria, progress, checkpoint evidence | At meaningful phase/work-package checkpoints |
| `ai/backlog-tasks.md` | Work identified but not ready/prioritized | When readiness changes |
| `ai/blocked-tasks.md` | Work blocked by a concrete dependency | When blocker changes |
| `ai/done-tasks.md` | Accepted work and stable IDs | When accepted |

Do not duplicate detailed sub-item status in the global session summary. Do not create a separate tracker for a tiny task that can be handled directly in an existing phase file.

## Phase readiness gate

A phase may be marked **Ready** only when all of the following are true:
1. Its outcome is observable and bounded; in-scope and out-of-scope work are explicit.
2. Required predecessor phases/work packages are Done, or an approved parallel integration plan documents the dependency.
3. Required human decisions, assets, access, APIs, and environments are available or explicitly listed as non-blocking.
4. Acceptance criteria and verification approach are written before implementation.
5. A phase owner and integration owner are named. They may be the same person for a small phase.
6. Initial work-package boundaries identify allowed files/systems, excluded shared files, and dependencies.

Do not start a dependent phase because it merely exists on the board. If a prerequisite is incomplete, keep the phase Planned or Blocked and name the exact dependency.

## Ownership model

1. Each active phase has one accountable **phase owner**. That owner coordinates scope, integration, acceptance, and handoff.
2. Each phase has one named **integration owner**, responsible for integrating delegated work, resolving conflicts, reviewing cross-package compatibility, and ensuring acceptance evidence is consolidated. This may be the phase owner.
3. The phase owner may execute the whole phase or delegate substantial **work packages** with explicit owners.
4. Sub-items normally remain grouped under their work package; they do not each require a separate owner or session-state row.
5. A session username identifies the current agent session. It is not automatically the phase owner. Record phase/work-package ownership explicitly in the tracker.
6. Claim ownership in the phase tracker before editing. Include agent, branch, scope/file boundary, and status.
7. Do not take another agent's ownership without explicit human approval. On handoff, update ownership and the next step.
8. One agent owns each tracker file at a time. Delegated agents report checkpoint summaries to the tracker owner; they do not concurrently rewrite the shared tracker.

## Work package sizing and concurrency

A useful work package produces a coherent, reviewable result and can be completed without frequent coordination-file edits. Group related sub-items when they:
- contribute to the same acceptance outcome;
- touch the same bounded subsystem or integration path;
- share dependencies and verification; and
- can be safely implemented by one owner.

Split a phase only when it is too large for one owner or when independent work can proceed in parallel. Avoid splitting purely to make a long checklist look smaller.

Default concurrency is **up to three active work-package owners per phase**, including the phase owner when they are implementing a package. A project may set a lower or higher limit in its project brief. The phase owner must queue excess packages rather than create more concurrent assignments. Concurrency is a ceiling, not a target: use fewer agents when integration cost or shared-file risk outweighs parallel speed.

## Parallel work and file boundaries

Before parallel work begins, the phase owner records:
- each work package owner and expected outcome;
- allowed files/systems and files explicitly excluded;
- dependencies and integration points;
- the order for shared contracts, scenes, prefabs, assets, and composition roots.

Prefer parallelism across isolated systems, tests, documentation, or independent modules. Serialize changes to shared Unity scenes, prefabs, ScriptableObjects, assembly definitions, central bootstrap/composition roots, shared interfaces, project settings, and shared trackers unless an explicit integration strategy exists. Never let two agents silently own overlapping files.

## Checkpoints and shared-state updates

Agents may finish multiple sub-items before writing a checkpoint. Update the phase tracker when one or more of these occurs:
- a coherent work package or milestone is complete;
- a dependency or blocker appears, clears, or changes;
- an architecture/API/data decision is made;
- meaningful verification evidence becomes available;
- ownership changes or work is handed off;
- phase acceptance criteria are met.

Update `ai/session-state.md` only when:
- a phase/work package starts, completes, becomes blocked, or changes owner;
- priority or the next cross-phase milestone changes;
- a blocker affects other work;
- a cross-agent handoff or material project risk needs to be visible globally.

Do not update the global summary for every file edit, command, test case, or sub-item. Keep implementation chronology out of the global summary.

## Completion and handoff

A phase is complete only when its exit criteria and acceptance checks are met, all in-scope sub-items are Done, Deferred with explicit owner approval, or Blocked with a named dependency, and evidence is recorded. Implementation complete is not the same as phase complete: compile, tests, integration, review, and human/device acceptance must be marked separately where applicable.

The integration owner verifies that delegated branches are based on the intended integration point, checks their diffs, resolves conflicts, runs cross-package checks, and records the integrated commit/PR evidence. A work package is not integrated merely because its owner says it is finished.

A handoff must identify the phase/work package, outgoing and incoming owner, branch/PR, exact stopping point, next action, file boundaries, verification performed/not performed, known risks, and decisions waiting. Release ownership when handing off.

## Conflict recovery

Before editing a shared tracker, re-read its latest branch version. If another agent has updated it, merge the changes rather than replacing them. Prefer one owner per tracker; delegated agents report checkpoint summaries to the phase owner, who performs the consolidated update when needed.
