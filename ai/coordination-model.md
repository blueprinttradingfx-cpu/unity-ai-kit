# Multi-agent coordination model

## Purpose

Coordinate multiple AI agents without turning shared state into a micro-task log. The normal ownership unit for substantial parallel work is a **phase** or a coherent **work package** inside a phase. Sub-items are execution checklists, not separate global-board tasks.

This is an optional coordination model, not a requirement to run multiple agents or create a phase tracker for every task. Choose the lightest workflow that protects the work:
- **Solo / small project:** use the project brief and relevant rules; keep a short session note only when work spans sessions. A phase tracker, task IDs, and separate status lists are optional. A short task can be handled directly without creating coordination artifacts.
- **Small team / multi-agent project:** use a shared session summary and explicit ownership for concurrently active work. Add phase trackers for substantial work that needs scope, acceptance criteria, dependencies, or handoffs.
- **Larger / parallel project:** use the full phase readiness gate, work-package boundaries, integration owner, and checkpoint model below.

Keep ownership boundaries, truthful handoffs, and protection against conflicting edits in every mode. Tune concurrency, checkpoint cadence, and artifacts to the team; do not treat the suggested defaults as a universal process mandate.

## Sources of truth

Use only the artifacts the project actually needs.

| Artifact | Owns | Update cadence |
|---|---|---|
| `ai/session-state.md` | Global active phases, accountable owners, blockers, priority, next milestone, cross-phase handoff | Only on meaningful coordination changes; optional for solo work |
| Phase tracker (for example `ai/phase-<n>-<name>.md`) | Scope, work packages, sub-items, dependencies, acceptance criteria, progress, checkpoint evidence | For substantial phases; at meaningful checkpoints |
| `ai/backlog-tasks.md` | Tracked work identified but not ready/prioritized | When readiness changes; optional |
| `ai/blocked-tasks.md` | Tracked work blocked by a concrete dependency | When blocker changes; optional |
| `ai/done-tasks.md` | Accepted tracked work and stable IDs | When accepted; optional |

Do not duplicate detailed sub-item status in the global session summary. Do not create a separate tracker for a tiny task that can be handled directly. A project may use GitHub Issues, a ticket system, or another existing board instead of duplicating it in Markdown; document the source of truth once.

## Phase readiness gate

For substantial work using phases, mark a phase **Ready** only when:
1. Its outcome is observable and bounded; in-scope and out-of-scope work are explicit.
2. Required predecessor phases/work packages are Done, or an approved parallel integration plan documents the dependency.
3. Required human decisions, assets, access, APIs, and environments are available or explicitly listed as non-blocking.
4. Acceptance criteria and verification approach are written before implementation.
5. A phase owner and integration owner are named. They may be the same person for a small phase.
6. Initial work-package boundaries identify allowed files/systems, excluded shared files, and dependencies.

For a small, self-contained task, do not impose this gate or create a phase merely to satisfy process. Do not start dependent work while a real prerequisite is incomplete; name the exact dependency.

## Ownership model

1. Each active shared phase has one accountable **phase owner** who coordinates scope, integration, acceptance, and handoff.
2. For delegated parallel work, name one **integration owner** responsible for integrating packages, resolving conflicts, reviewing compatibility, and consolidating acceptance evidence. This may be the phase owner.
3. The phase owner may execute the whole phase or delegate substantial **work packages** with explicit owners.
4. Sub-items normally remain grouped under their work package; they do not each require a separate owner or session-state row.
5. A session username identifies the current agent session. It is not automatically the phase owner. Record phase/work-package ownership explicitly when work is shared.
6. Before parallel editing, claim ownership in the tracker or agreed coordination system. Include agent, branch, scope/file boundary, and status.
7. Do not take another agent's ownership without explicit human approval. On handoff, update ownership and the next step.
8. One agent owns each shared tracker file at a time. Delegated agents report checkpoint summaries to the tracker owner; they do not concurrently rewrite the shared tracker.

## Work package sizing and concurrency

A useful work package produces a coherent, reviewable result and can be completed without frequent coordination-file edits. Group related sub-items when they contribute to the same acceptance outcome, touch a bounded subsystem, share dependencies/verification, and can safely be implemented by one owner.

Split a phase only when it is too large for one owner or independent work can proceed in parallel. Avoid splitting merely to make a long checklist look smaller.

Suggested concurrency is **up to three active work-package owners per phase**, including the phase owner when implementing a package. This is a starting ceiling, not a target or universal limit. A project may choose fewer or more based on team size, integration cost, and file-conflict risk. Queue excess packages rather than silently over-assigning them.

## Parallel work and file boundaries

Before parallel work begins, record:
- each work package owner and expected outcome;
- allowed files/systems and files explicitly excluded;
- dependencies and integration points;
- the order for shared contracts, scenes, prefabs, assets, and composition roots.

Prefer parallelism across isolated systems, tests, documentation, or independent modules. Serialize changes to shared Unity scenes, prefabs, ScriptableObjects, assembly definitions, central bootstrap/composition roots, shared interfaces, project settings, and shared trackers unless an explicit integration strategy exists. Never let two agents silently own overlapping files.

## Checkpoints and shared-state updates

Agents may finish multiple related sub-items before writing a checkpoint. Update the phase tracker when a coherent work package/milestone completes, a dependency or blocker changes, a consequential decision is made, meaningful verification becomes available, ownership changes, or a handoff occurs.

Update `ai/session-state.md` only when:
- a shared phase/work package starts, completes, becomes blocked, or changes owner;
- priority or the next cross-phase milestone changes;
- a blocker affects other work;
- a cross-agent handoff or material project risk needs global visibility.

Do not update the global summary for every file edit, command, test case, or sub-item. Keep implementation chronology out of the global summary. Solo projects may use a short handoff note or no session file when there is no cross-session coordination need.

## Completion and handoff

For tracked phases, completion requires exit criteria and acceptance checks, all in-scope work packages resolved as Done, Deferred with explicit owner approval, or Blocked with a named dependency, and evidence recorded. Implementation complete is not the same as phase complete: compile, tests, integration, review, and human/device acceptance must be marked separately where applicable.

The integration owner verifies delegated branches are based on the intended integration point, checks their diffs, resolves conflicts, runs cross-package checks, and records integrated commit/PR evidence. A work package is not integrated merely because its owner says it is finished.

A handoff should identify the work, outgoing/incoming owner when applicable, branch/PR, exact stopping point, next action, file boundaries, verification performed/not performed, known risks, and decisions waiting. Release ownership when handing off. Scale the handoff detail to the risk and duration of the work; do not manufacture a formal handoff for a trivial completed task.

## Conflict recovery

Before editing a shared tracker, re-read its latest branch version. If another agent has updated it, reconcile changes rather than replacing them. Prefer one owner per tracker; delegated agents report checkpoint summaries to the phase owner, who performs the consolidated update when needed.
