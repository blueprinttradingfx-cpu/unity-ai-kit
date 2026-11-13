# Project / Work Board

This is the low-churn coordination summary, not a task diary. Detailed scope and sub-item progress belong in the relevant phase tracker. Update this file only for ownership, phase status, blockers, priority, milestone, or handoff changes.

Read `ai/coordination-model.md` before coordinating parallel work. Backlog, blocked, and completed work remain in `ai/backlog-tasks.md`, `ai/blocked-tasks.md`, and `ai/done-tasks.md`.

**Session username for the session that last updated this file:** `Gpt`

## Active work

| Phase / task | Status | Owner | Branch / tracker | Current checkpoint / next milestone |
|---|---|---|---|---|
| KIT-011 — Agent workflow adaptability audit | In Progress | `Gpt` | `gpt/kit-agent-workflow-adaptability` / `ai/phase-KIT-011-agent-workflow-adaptability.md` | Guidance and templates updated; regression coverage added; next validate the PR and review the complete diff |

## Completed milestones

| Task | Status | Evidence |
|---|---|---|
| KIT-001–KIT-004 — Agent safeguards and CI quality foundation | Done | PR #1 merged into `main`; merge commit `74fe2433a46bce6bb9b63696a03c92b2c74f0238` |
| KIT-005 — Nightly regression and protected release templates | Done | PR #2 merged into `main`; merge commit `39e0f2205b110034645dd21fdbb7ffe3c966e4a5` |
| KIT-006 — Phase-based multi-agent coordination model | Done | PR #3 merged into `main`; merge commit `447b7618cd0bb0051a3c3224d316e3a4a1c6c69f` |
| KIT-007 — Production readiness and validation | Done | PR #5 merged into `main`; merge commit `f814ac41560964ef5abb14ab31f724674cb754bc`; Kit Validation run `43320593384` passed 16 tests, syntax checks, and actionlint |
| KIT-008 — Garden Alchemy consumer feedback and CI template adaptation | Done | PR #7 merged into `main`; merge commit `c0b84e768cdd5a66cf089c4e7c30e85739c08b45`; Kit Validation run `43340306384` passed 18 tests, source/config syntax checks, and actionlint |
| KIT-009 — Flexible kit guidance principles | Done | PR #8 merged into `main`; merge commit `b71a570f7630faa48a62268bb3474e180d682068`; Kit Validation run `43343527260` passed |
| KIT-010 — Guidance consistency audit | Done | PR #9 merged into `main`; merge commit `e74588f3ee6e647de6d65098c0a885f928fdbb89`; latest Kit Validation run `43344606497` passed |

## Coordination rules at a glance
- Phase or substantial work package is the normal ownership unit for larger or multi-agent work; solo/small projects may use a lighter task flow.
- One accountable phase owner coordinates a phase. Split work-package ownership only when file boundaries and dependencies are genuinely independent.
- Agents may complete several related sub-items before checkpointing; do not create a shared-board update for every small action.
- Never allow overlapping ownership of the same scene, prefab, asset, API contract, or high-conflict file without an explicit integration plan.
- Session identity is not phase ownership. A session username identifies the agent; the phase tracker records who owns the phase.

## Project context
- **Repository:** reusable Unity AI guidance and optional CI templates; no Unity game project is hosted here.
- **Base:** `main`; KIT-001 through KIT-010 are merged. KIT-011 is the active workflow adaptability audit.
- **Consumer validation target:** Garden Alchemy was the first consumer; PR #41 is merged. Consumer-specific Unity validation remains owned by Garden Alchemy and is not a universal kit completion gate.
- **Last known good build:** Not applicable to this documentation/workflow-template repository.

## Handoff
- **Exact stopping point:** KIT-011 WP1/WP2 guidance and onboarding changes committed; focused workflow regression tests added on `gpt/kit-agent-workflow-adaptability`.
- **Next step:** validate the branch, inspect the full diff, and prepare owner review.
- **Verified:** KIT-010 latest Kit Validation run `43344606497` passed; KIT-011 source changes and test file are committed.
- **Not verified:** KIT-011 tests, syntax checks, actionlint, and full PR review are pending. No Unity Editor execution is applicable to this kit repository.
- **Known risks:** simplify optional workflow ceremony without weakening explicit ownership, safe handoffs, security, or truthful verification.
