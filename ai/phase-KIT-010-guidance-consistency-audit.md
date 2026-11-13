# Phase KIT-010 — Guidance Consistency Audit

## Outcome

Make the detailed rule files and project templates consistently reflect KIT-009: strong defaults, flexible implementation, project-owned decisions. Keep security and integrity guardrails firm while removing accidental assumptions about one Unity version, game architecture, platform, or team workflow.

## Status and ownership

- Status: In Progress
- Phase owner: Gpt
- Integration owner: Gpt
- Branch: `gpt/kit-guidance-consistency-audit`
- Base: `main`
- Predecessor: KIT-009 merged as PR #8 (`b71a570f7630faa48a62268bb3474e180d682068`).

## Work packages

| ID | Outcome | Owner | Status | File/system boundary |
|---|---|---|---|---|
| KIT-010-WP1 | Classify detailed rule files and explain adaptation | Gpt | Done | `ai/rules/*.md`, `ai/github-workflows.md` |
| KIT-010-WP2 | Remove fixed engine/platform assumptions from consumer templates | Gpt | Done | `AGENTS.md`, `ai/project-brief.md` |
| KIT-010-WP3 | Audit remaining examples and validate consistency | Gpt | In Progress | `README.md`, `examples/**`, templates and validation |

## Acceptance criteria

- [x] Detailed rules explain which recommendations are adaptable and which safety constraints remain firm.
- [x] Project brief does not assume Unity 6.3, Android-first, URP, or a specific UI/input stack.
- [x] AGENTS template does not imply a fixed Unity version or Android target.
- [x] Remaining examples are checked for fixed project assumptions and labeled as examples/defaults where appropriate.
- [x] Kit Validation run `43344486573` passes all checks.
- [x] Full diff reviewed and PR #9 opened for owner review.

## Checkpoint log

- 2026-11-13 — Started after KIT-009 merge. Audit found detailed rule files still used mandatory language for architecture, UI technology, data ownership, performance budgets, and test strategy.
- 2026-11-13 — Added adaptation guidance to code style, UI, gameplay/data, performance/mobile, testing, safety/Git, and GitHub workflow guides.
- 2026-11-13 — Changed the project brief and AGENTS header to consumer-selected Unity versions, platforms, render pipeline, UI, and input configuration.
- 2026-11-13 — Labeled Unity workflow sample branch/platform matrices and schedules as configurable. Reviewed the complete 18-file PR diff.
- 2026-11-13 — Kit Validation run `43344486573` passed source/config syntax, regression tests, actionlint, and metadata applicability checks.

## Handoff

- Current owner/status: Gpt / Ready for owner review.
- Next: owner review PR #9; do not merge without explicit approval.
- No Unity Editor validation is applicable; this repository contains reusable guidance and workflow templates, not a Unity game.
