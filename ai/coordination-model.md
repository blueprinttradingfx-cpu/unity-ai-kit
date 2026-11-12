# Multi-agent coordination model

## Purpose

Coordinate several AI agents without turning a shared session file into a high-frequency micro-task log. The default unit of ownership is a **phase** or a substantial **work package** inside a phase. Sub-items are the execution checklist, not separate global-board tasks.

## Sources of truth

| Artifact | Owns | Update cadence |
|---|---|---|
| `ai/session-state.md` | Global active phases, accountable owners, blockers, priority, next milestone, cross-phase handoff | Only on meaningful coordination changes |
| Phase tracker (for example `ai/phase-<n>-<name>.md`) | Scope, work packages, sub-items, dependencies, acceptance criteria, progress, checkpoint evidence | At meaningful phase/work-package checkpoints |
| `ai/backlog-tasks.md` | Work identified but not ready/prioritized | When readiness changes |
| `ai/blocked-tasks.md` | Work blocked by a concrete dependency | When blocker changes |
| `ai/done-tasks.md` | Accepted work and stable IDs | When accepted |

Do not duplicate detailed sub-item status in the global session summary. Do not create a separate tracker for a tiny task that can be handled directly in an existing phase file.

## Ownership model

1. Each active phase has one accountable **phase owner**. That owner coordinates scope, integration, acceptance, and handoff.
2. The phase owner may execute the whole phase or delegate substantial **work packages** with explicit owners.
3. Sub-items normally remain grouped under their work package; they do not each require a separate owner or session-state row.
4. A session username identifies the current agent session. It is not automatically the phase owner. Record phase/work-package ownership explicitly in the tracker.
5. Claim ownership in the phase tracker before editing. Include agent, branch, scope/file boundary, and status.
6. Do not take another agent's ownership without explicit human approval. On handoff, update ownership and the next step.

## Work package sizing

A useful work package produces a coherent, reviewable result and can be completed without frequent coordination-file edits. Group related sub-items when they:
- contribute to the same acceptance outcome;
- touch the same bounded subsystem or integration path;
- share dependencies and verification; and
- can be safely implemented by one owner.

Split a phase only when it is too large for one owner or when independent work can proceed in parallel. Avoid splitting purely to make a long checklist look smaller.

## Parallel work and file boundaries

Before parallel work begins, the phase owner records:
- each work package owner and expected outcome;
- allowed files/systems and files explicitly excluded;
- dependencies and integration points;
- the order for shared contracts, scenes, prefabs, assets, and composition roots.

Prefer parallelism across isolated systems, tests, documentation, or independent modules. Serialize changes to shared Unity scenes, prefabs, ScriptableObjects, assembly definitions, central bootstrap/composition roots, shared interfaces, and project settings unless an explicit integration strategy exists. Never let two agents silently own overlapping files.

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

A phase is complete only when its exit criteria and acceptance checks are met, all in-scope sub-items are Done, Deferred with explicit owner approval, or Blocked with a named dependency, and evidence is recorded. A phase owner integrates delegated work and reports any remaining risks.

A handoff must identify the phase/work package, outgoing and incoming owner, branch/PR, exact stopping point, next action, file boundaries, verification performed/not performed, known risks, and decisions waiting. Release ownership when handing off.

## Conflict recovery

Before editing a shared tracker, re-read its latest branch version. If another agent has updated it, merge the changes rather than replacing them. Prefer one owner per tracker; delegated agents report checkpoint summaries to the phase owner, who performs the consolidated update when needed.
