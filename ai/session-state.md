# Project / Work Board

This is the low-churn coordination summary, not a task diary. Detailed scope and sub-item progress belong in the relevant phase tracker. Update this file only for ownership, phase status, blockers, priority, milestone, or handoff changes.

Read `ai/coordination-model.md` before coordinating parallel work. Backlog, blocked, and completed work remain in their task lists when those lists are used by the project.

**Session username for the session that last updated this file:** `Gpt`

## Active work
| Phase / task | Status | Owner | Branch / tracker | Current checkpoint / next milestone |
|---|---|---|---|---|
| None | — | — | — | KIT-012 is merged; identify the next highest-value kit improvement before starting another phase |

## Completed milestones
| Task | Status | Evidence |
|---|---|---|
| KIT-001–KIT-004 — Agent safeguards and CI quality foundation | Done | PR #1 merged; `74fe2433a46bce6bb9b63696a03c92b2c74f0238` |
| KIT-005 — Nightly regression and protected release templates | Done | PR #2 merged; `39e0f2205b110034645dd21fdbb7ffe3c966e4a5` |
| KIT-006 — Phase-based multi-agent coordination model | Done | PR #3 merged; `447b7618cd0bb0051a3c3224d316e3a4a1c6c69f` |
| KIT-007 — Production readiness and validation | Done | PR #5 merged; `f814ac41560964ef5abb14ab31f724674cb754bc`; run `43320593384` passed |
| KIT-008 — Garden Alchemy consumer feedback and CI template adaptation | Done | PR #7 merged; `c0b84e768cdd5a66cf089c4e7c30e85739c08b45`; run `43340306384` passed |
| KIT-009 — Flexible kit guidance principles | Done | PR #8 merged; `b71a570f7630faa48a62268bb3474e180d682068`; run `43343527260` passed |
| KIT-010 — Guidance consistency audit | Done | PR #9 merged; `e74588f3ee6e647de6d65098c0a885f928fdbb89`; run `43344606497` passed |
| KIT-011 — Agent workflow adaptability audit | Done | PR #10 merged; `0a033205f7b76ea0e58dd6c833f6424db38e2e34`; run `43345762282` passed |
| KIT-012 — Prompt template adaptability audit | Done | PR #11 merged; `8c3a5b57ff4d84993f67955439bf0e2360ad2bf6`; validation run `43346247889` passed all jobs |

## Coordination rules at a glance
- Phase/work-package ownership is for substantial or shared work; small solo tasks may proceed directly.
- One accountable phase owner coordinates a phase. Split ownership only across genuinely independent boundaries.
- Group related sub-items and checkpoint at meaningful milestones; do not update shared state after every small action.
- Never overlap ownership of shared scenes, prefabs, assets, API contracts, or high-conflict files without an integration plan.
- Session identity is not phase ownership.

## Project context
- **Repository:** reusable Unity AI guidance and optional CI templates; no Unity game project is hosted here.
- **Base:** `main`; KIT-001 through KIT-012 are merged.
- **Consumer validation target:** Garden Alchemy was the first consumer; PR #41 is merged. Consumer-specific Unity validation remains separate.
- **Last known good build:** Not applicable to this documentation/workflow-template repository.

## Handoff
- **Exact stopping point:** KIT-012 prompt templates and regression coverage are merged to `main`.
- **Next step:** review the kit backlog and consumer feedback for the next high-value phase; do not start speculative work without a defined outcome.
- **Verified:** PR #11 merged as `8c3a5b57ff4d84993f67955439bf0e2360ad2bf6`; KIT-012 validation run `43346247889` passed all jobs.
- **Not verified:** consumer-specific Unity compilation/runtime validation; that belongs in the consumer project.
- **Known risks:** keep prompts provider-neutral and consumer-adaptable; do not reintroduce mandatory tracking for trivial tasks.
