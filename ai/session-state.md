# Project / Work Board

This is the low-churn coordination summary, not a task diary. Detailed scope and sub-item progress belong in the relevant phase tracker. Update this file only for ownership, phase status, blockers, priority, milestone, or handoff changes.

Read `ai/coordination-model.md` before coordinating parallel work. Backlog, blocked, and completed work remain in `ai/backlog-tasks.md`, `ai/blocked-tasks.md`, and `ai/done-tasks.md`.

**Session username for the session that last updated this file:** `Gpt`

## Active work

| Phase / task | Status | Owner | Branch / tracker | Current checkpoint / next milestone |
|---|---|---|---|---|
| KIT-007 — Production readiness and validation | In Progress | `Gpt` | `gpt/kit-007-ci-secret-isolation` / `ai/phase-KIT-007-production-readiness.md` | Owner audit recorded; PR #5 ready for maintainer merge; then hand off to Garden Alchemy consumer validation |

## Completed milestones

| Task | Status | Evidence |
|---|---|---|
| KIT-001–KIT-004 — Agent safeguards and CI quality foundation | Done | PR #1 merged into `main`; merge commit `74fe2433a46bce6bb9b63696a03c92b2c74f0238` |
| KIT-005 — Nightly regression and protected release templates | Done | PR #2 merged into `main`; merge commit `39e0f2205b110034645dd21fdbb7ffe3c966e4a5` |
| KIT-006 — Phase-based multi-agent coordination model | Done | PR #3 merged into `main`; merge commit `447b7618cd0bb0051a3c3224d316e3a4a1c6c69f` |

## Coordination rules at a glance
- Phase or substantial work package is the normal ownership unit; sub-items are grouped inside its tracker.
- One accountable phase owner coordinates the phase. Split work-package ownership only when file boundaries and dependencies are genuinely independent.
- Agents may complete several related sub-items before checkpointing; do not create a shared-board update for every small action.
- Never allow overlapping ownership of the same scene, prefab, asset, API contract, or high-conflict file without an explicit integration plan.
- Session identity is not phase ownership. A session username identifies the agent; the phase tracker records who owns the phase.

## Project context
- **Repository:** reusable Unity AI guidance and inactive CI templates; no Unity game project is hosted here.
- **Base:** `main`; KIT-001 through KIT-006 are merged.
- **Consumer validation target:** Garden Alchemy, after KIT-007 is reviewed and merged.
- **Last known good build:** Not applicable to this documentation/workflow-template repository.

## Handoff
- **Exact stopping point:** PR #5 is ready for maintainer merge consideration. It contains protected Unity environment gates, workflow/security regression coverage, Node 24 action pins, Unity 6.3 reference corrections, .NET 10 LTS default, and a consumer validation checklist. Owner audit comment `5883211309` is recorded; latest Kit Validation run `43320593384` passed 16 tests, source/config syntax checks, and actionlint.
- **Next step:** merge PR #5 after maintainer authorization, then begin a separately scoped Garden Alchemy consumer-validation phase. Garden Alchemy remains deferred until the kit is merged.
- **Verified:** PRs #1, #2, and #3 are merged into `main` (merge SHAs recorded above); PR #5 owner audit comment submitted and PR marked ready for review.
- **Not verified:** Unity Editor import/compile, EditMode/PlayMode tests, target builds, licensed GameCI jobs, and real-device behavior; these require the Garden Alchemy consumer project and its configuration.
- **Owner decisions waiting:** Garden Alchemy's exact Unity Editor version, target platforms, license configuration, required checks, and release environment must be confirmed during consumer setup.
- **Known risks:** Workflow templates remain opt-in examples. Passing kit-level static checks does not prove they execute successfully in a consuming Unity repository.
