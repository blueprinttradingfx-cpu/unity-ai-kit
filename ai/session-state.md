# Project / Work Board

This is the low-churn coordination summary, not a task diary. Detailed scope and sub-item progress belong in the relevant phase tracker. Update this file only for ownership, phase status, blockers, priority, milestone, or handoff changes.

Read `ai/coordination-model.md` before coordinating parallel work. Backlog, blocked, and completed work remain in `ai/backlog-tasks.md`, `ai/blocked-tasks.md`, and `ai/done-tasks.md`.

**Session username for the session that last updated this file:** `Gpt`

## Active work

| Phase / task | Status | Owner | Branch / tracker | Current checkpoint / next milestone |
|---|---|---|---|---|
| KIT-010 — Guidance consistency audit | In Progress | `Gpt` | `gpt/kit-guidance-consistency-audit` / `ai/phase-KIT-010-guidance-consistency-audit.md` | Detailed rules and project templates now classify defaults vs guardrails; review remaining examples and validate |

## Completed milestones

| Task | Status | Evidence |
|---|---|---|
| KIT-001–KIT-004 — Agent safeguards and CI quality foundation | Done | PR #1 merged into `main`; merge commit `74fe2433a46bce6bb9b63696a03c92b2c74f0238` |
| KIT-005 — Nightly regression and protected release templates | Done | PR #2 merged into `main`; merge commit `39e0f2205b110034645dd21fdbb7ffe3c966e4a5` |
| KIT-006 — Phase-based multi-agent coordination model | Done | PR #3 merged into `main`; merge commit `447b7618cd0bb0051a3c3224d316e3a4a1c6c69f` |
| KIT-007 — Production readiness and validation | Done | PR #5 merged into `main`; merge commit `f814ac41560964ef5abb14ab31f724674cb754bc`; Kit Validation run `43320593384` passed 16 tests, syntax checks, and actionlint |
| KIT-008 — Garden Alchemy consumer feedback and CI template adaptation | Done | PR #7 merged into `main`; merge commit `c0b84e768cdd5a66cf089c4e7c30e85739c08b45`; Kit Validation run `43340306384` passed 18 tests, source/config syntax checks, and actionlint |
| KIT-009 — Flexible kit guidance principles | Done | PR #8 merged into `main`; merge commit `b71a570f7630faa48a62268bb3474e180d682068`; Kit Validation run `43343527260` passed |

## Coordination rules at a glance
- Phase or substantial work package is the normal ownership unit; sub-items are grouped inside their tracker.
- One accountable phase owner coordinates the phase. Split work-package ownership only when file boundaries and dependencies are genuinely independent.
- Agents may complete several related sub-items before checkpointing; do not create a shared-board update for every small action.
- Never allow overlapping ownership of the same scene, prefab, asset, API contract, or high-conflict file without an explicit integration plan.
- Session identity is not phase ownership. A session username identifies the agent; the phase tracker records who owns the phase.

## Project context
- **Repository:** reusable Unity AI guidance and optional CI templates; no Unity game project is hosted here.
- **Base:** `main`; KIT-001 through KIT-009 are merged. KIT-010 is the active guidance consistency audit.
- **Consumer validation target:** Garden Alchemy was the first consumer; PR #41 is merged. Consumer-specific Unity validation remains owned by Garden Alchemy and is not a universal kit completion gate.
- **Last known good build:** Not applicable to this documentation/workflow-template repository.

## Handoff
- **Exact stopping point:** KIT-009 is merged. KIT-010 adds category/adaptation notes to the detailed rule files, makes the project brief engine/platform-neutral, and removes fixed Unity/Android assumptions from the AGENTS template.
- **Next step:** review the remaining examples and template defaults, run Kit Validation, inspect the diff, and open an owner-review PR.
- **Verified:** KIT-009 PR #8 is merged; Kit Validation run `43343527260` passed.
- **Not verified:** KIT-010 validation has not yet run. No Unity Editor execution is applicable to this kit repository.
- **Known risks:** Individual example recommendations may still need consumer-side tuning; the kit should avoid presenting them as mandatory unless they protect security or data integrity.
