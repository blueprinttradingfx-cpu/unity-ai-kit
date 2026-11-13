# Project / Work Board

This is the low-churn coordination summary, not a task diary. Detailed scope and sub-item progress belong in the relevant phase tracker. Update this file only for ownership, phase status, blockers, priority, milestone, or handoff changes.

Read `ai/coordination-model.md` before coordinating parallel work. Backlog, blocked, and completed work remain in `ai/backlog-tasks.md`, `ai/blocked-tasks.md`, and `ai/done-tasks.md`.

**Session username for the session that last updated this file:** `Gpt`

## Active work

| Phase / task | Status | Owner | Branch / tracker | Current checkpoint / next milestone |
|---|---|---|---|---|
| KIT-008 — Garden Alchemy consumer feedback and CI template adaptation | Ready for review | `Gpt` | `gpt/garden-alchemy-consumer-feedback` / PR #7 | Kit Validation run `43340306384` passed 18 tests, syntax checks, and actionlint; owner review before merge |

## Completed milestones

| Task | Status | Evidence |
|---|---|---|
| KIT-001–KIT-004 — Agent safeguards and CI quality foundation | Done | PR #1 merged into `main`; merge commit `74fe2433a46bce6bb9b63696a03c92b2c74f0238` |
| KIT-005 — Nightly regression and protected release templates | Done | PR #2 merged into `main`; merge commit `39e0f2205b110034645dd21fdbb7ffe3c966e4a5` |
| KIT-006 — Phase-based multi-agent coordination model | Done | PR #3 merged into `main`; merge commit `447b7618cd0bb0051a3c3224d316e3a4a1c6c69f` |
| KIT-007 — Production readiness and validation | Done | PR #5 merged into `main`; merge commit `f814ac41560964ef5abb14ab31f724674cb754bc`; Kit Validation run `43320593384` passed 16 tests, syntax checks, and actionlint |

## Coordination rules at a glance
- Phase or substantial work package is the normal ownership unit; sub-items are grouped inside its tracker.
- One accountable phase owner coordinates the phase. Split work-package ownership only when file boundaries and dependencies are genuinely independent.
- Agents may complete several related sub-items before checkpointing; do not create a shared-board update for every small action.
- Never allow overlapping ownership of the same scene, prefab, asset, API contract, or high-conflict file without an explicit integration plan.
- Session identity is not phase ownership. A session username identifies the agent; the phase tracker records who owns the phase.

## Project context
- **Repository:** reusable Unity AI guidance and inactive CI templates; no Unity game project is hosted here.
- **Base:** `main`; KIT-001 through KIT-007 are merged. KIT-008 is the current feedback/adaptation pass.
- **Consumer validation target:** Garden Alchemy; PR #41 is merged. Hosted Unity activation was skipped by the owner; local Unity compile/EditMode and Phase 10 runtime/device acceptance remain open. Garden Alchemy PRs #45 and #46 are open for owner review.
- **Last known good build:** Not applicable to this documentation/workflow-template repository.

## Handoff
- **Exact stopping point:** KIT-008 changes are on PR #7. The new mainline-only Unity CI template, checkout credential minimization, trust-model docs, path-filter and runner-cleanup guidance, and security regression tests are complete. Kit Validation run `43340306384` passed 18 tests, source/config syntax checks, and actionlint. Garden Alchemy PRs #45 and #46 remain open for owner review; local Unity validation remains with the owner.
- **Next step:** owner reviews and merges PR #7; then return to Garden Alchemy Phase 10 local Unity/runtime acceptance.
- **Verified:** PRs #1–#3 and #5 are merged into `main`; PR #5 merge SHA is recorded above. Garden Alchemy's CI-hardening PR is merged; .NET balance smoke passed.
- **Not verified:** successful hosted Unity Editor import/compile and EditMode tests (run in progress), PlayMode tests, target builds, and real-device behavior.
- **Owner decisions waiting:** Phase 10 runtime flow and Android/device acceptance remain with Garden Alchemy owner.
- **Known risks:** Workflow templates remain opt-in examples. Passing kit-level static checks does not prove they execute successfully in a consuming Unity repository.
