# Phase KIT-012 — Prompt Template Adaptability Audit

## Outcome

Align the reusable prompt library with KIT-009 through KIT-011: prompts should adapt to the consumer's actual project and scale their coordination ceremony to the task. Keep actionable review quality, evidence-based verification, and ownership safeguards.

## Scope
- Audit start-session, new-feature, review, and spike prompts for fixed project assumptions or mandatory coordination steps.
- Make context loading proportional to the task.
- Ensure prompt guidance aligns with AGENTS.md, task lifecycle, and coordination model.
- Add focused regression tests for the prompt invariants.

## Status and ownership
- Status: Awaiting owner review
- Phase owner: Gpt
- Integration owner: Gpt
- Branch: `gpt/kit-prompt-template-adaptability`
- Base: `main`
- Predecessor: KIT-011 merged as PR #10 (`0a033205f7b76ea0e58dd6c833f6424db38e2e34`).

## Work packages
| ID | Outcome | Owner | Status | File/system boundary |
|---|---|---|---|---|
| KIT-012-WP1 | Audit prompt templates for hard-coded project assumptions and excessive coordination ceremony | Gpt | Done | `ai/prompts/*.md` |
| KIT-012-WP2 | Align start-session, feature, and review prompts with scalable workflow principles | Gpt | Done | `ai/prompts/start-session.md`, `new-feature.md`, `review.md` |
| KIT-012-WP3 | Add regression coverage, validate, and prepare owner-review PR | Gpt | Done | `tests/**`, tracker, validation |

## Acceptance criteria
- [x] Small tasks can use prompts without mandatory session identity, phase trackers, or global status updates.
- [x] Larger/shared tasks retain ownership, file-boundary, handoff, and no-takeover safeguards.
- [x] Prompts avoid assumptions about mobile-only targets, fixed Unity versions, or fixed game architecture.
- [x] Regression tests and all applicable Kit Validation checks pass (run `43346247889`).
- [x] Complete diff reviewed and PR #11 opened for owner review; do not merge without explicit approval.

## Checkpoints
- 2026-11-13 — Started after KIT-011 merge. Found start-session and feature prompts still requiring phase claims/global updates for every goal; review prompt assumed a Unity 6 mobile game.
- 2026-11-13 — Updated start-session, feature, and review prompts to use project context and scale coordination to task size. Spike prompt already has no mandatory tracking requirement and remains unchanged.
- 2026-11-13 — Added focused regression tests; Kit Validation run `43346247889` passed source/configuration syntax, regression tests, actionlint, and the Unity metadata applicability check.
- 2026-11-13 — Inspected the complete seven-file PR diff. PR #11 is open and mergeable, awaiting owner review.

## Handoff
- Current owner/status: Gpt / awaiting owner review.
- Next: owner reviews PR #11; merge only after explicit approval.
- Verified: PR #11 head `91a1ec08277e812b27ccdffc93beb1dd95b5ba39`; validation run `43346247889` passed all jobs.
- Not verified: consumer-specific Unity compilation/runtime validation; that belongs in the consumer project.
- Risks: prompt templates are examples; consumers should tailor them to their own tools and project.
