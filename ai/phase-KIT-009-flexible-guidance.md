# Phase KIT-009 — Flexible Kit Guidance Principles

## Outcome

Make the kit explicitly reusable across Unity projects by distinguishing safety/integrity guardrails from recommended engineering defaults and consumer-owned decisions. Preserve useful opinions without turning one project's architecture or workflow into universal requirements.

## Status and ownership

- Status: In Progress
- Phase owner: Gpt
- Integration owner: Gpt
- Branch: `gpt/kit-flexible-guidance-principles`
- Base: `main`
- Consumer input: owner clarified that this repository is a reusable kit, not a dev-specific starter pack.

## Work packages

| ID | Outcome | Owner | Status | File/system boundary |
|---|---|---|---|---|
| KIT-009-WP1 | Define reusable guidance categories and adaptation rules | Gpt | Done | `ai/kit-principles.md` |
| KIT-009-WP2 | Align the consumer-facing AGENTS template and onboarding docs | Gpt | Done | `AGENTS.md`, `README.md`, `ai/consumer-validation-checklist.md` |
| KIT-009-WP3 | Validate consistency and open owner-review PR | Gpt | In Progress | Kit docs and validation workflow |

## Acceptance criteria

- [x] Clearly distinguish safety/integrity guardrails, recommended engineering defaults, and consumer-owned decisions.
- [x] Explain how a consumer adapts or replaces a recommendation without weakening safety.
- [x] Avoid implying that one Unity version, architecture, team size, platform, or CI strategy is universal.
- [ ] Kit Validation passes all checks.
- [ ] Full diff reviewed and PR opened.

## Checkpoint log

- 2026-11-13 — Owner clarified the kit should be a reusable development framework rather than a dev-specific starter pack. Adopted the principle: strong defaults, flexible implementation, project-owned decisions.
- 2026-11-13 — Added explicit guidance categories and updated the AGENTS template, README, and consumer validation checklist to make configuration and adaptation first-class.

## Handoff

- Current owner/status: Gpt / In Progress.
- Next: run Kit Validation, review resulting diff, and open a PR.
- No Unity Editor validation is applicable; this repository contains reusable guidance and workflow templates, not a Unity game.
