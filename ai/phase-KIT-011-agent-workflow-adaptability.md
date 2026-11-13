# Phase KIT-011 — Agent Workflow Adaptability Audit

## Outcome

Review the coordination model, task lifecycle, task boards, and consumer-facing agent instructions as one coherent workflow. Keep the useful phase/work-package model for multi-agent projects while making it easy to scale down for solo developers and small teams. Preserve ownership, safe Git behavior, truthful verification, and low-churn shared state.

## Scope

**In scope**
- Audit `ai/coordination-model.md`, `ai/task-lifecycle.md`, task-board templates, `ai/session-state.md`, and relevant onboarding in `AGENTS.md` / `README.md`.
- Clarify the minimum workflow for solo/small projects versus optional multi-agent coordination.
- Clarify when stable task IDs, phase trackers, ownership rows, and checkpoint updates are useful versus unnecessary overhead.
- Ensure the global session file remains a low-churn summary, not a micro-task ledger.
- Check consistency of status transitions, handoffs, review expectations, and authority to take over owned work.
- Add or update focused regression tests if the audit identifies testable workflow invariants.

**Out of scope**
- Weakening security, secret handling, destructive-operation safeguards, Unity asset integrity, or truthful verification.
- Forcing a single team size, agent provider, branch strategy, issue tracker, or workflow tool on all consumers.
- Changing Garden Alchemy project-specific configuration.

## Status and ownership

- Status: In Progress
- Phase owner: Gpt
- Integration owner: Gpt
- Branch: `gpt/kit-agent-workflow-adaptability`
- Base: `main`
- Predecessor: KIT-010 merged as PR #9 (`e74588f3ee6e647de6d65098c0a885f928fdbb89`).

## Work packages

| ID | Outcome | Owner | Status | File/system boundary |
|---|---|---|---|---|
| KIT-011-WP1 | Audit coordination and lifecycle guidance for duplication, rigidity, and unnecessary overhead | Gpt | In Progress | `ai/coordination-model.md`, `ai/task-lifecycle.md` |
| KIT-011-WP2 | Align task-board, session-state, and consumer onboarding templates with scalable workflow choices | Gpt | Planned | `ai/backlog-tasks.md`, `ai/blocked-tasks.md`, `ai/done-tasks.md`, `ai/session-state.md`, `AGENTS.md`, `README.md` |
| KIT-011-WP3 | Add/update regression coverage and validate the integrated guidance | Gpt | Planned | `tests/**`, relevant docs, Kit Validation |

## Acceptance criteria

- [ ] A solo/small project can follow a clear lightweight path without creating a phase tracker or multi-agent board for every task.
- [ ] Multi-agent projects retain explicit phase/work-package ownership and non-overlapping file boundaries.
- [ ] Shared session-state updates remain limited to meaningful ownership, status, blocker, priority, milestone, and handoff changes.
- [ ] Stable IDs and status lists have a clear purpose and do not duplicate detailed phase sub-item tracking.
- [ ] Handoff and takeover rules are clear, practical, and do not imply an agent may seize another owner's work.
- [ ] Safety, Git integrity, secret handling, and evidence-based verification remain firm guardrails.
- [ ] Regression tests and all applicable Kit Validation checks pass.
- [ ] Complete diff is reviewed and a PR is opened for owner review; do not merge without explicit approval.

## Checkpoints

- 2026-11-13 — Started after KIT-010 merge. Initial review confirms the coordination model already has a good lightweight-project allowance, but task lifecycle and startup instructions should be checked for consistency and unnecessary mandatory ceremony.

## Handoff

- Current owner/status: Gpt / In Progress.
- Next: complete WP1 audit, then align task boards and onboarding in WP2.
- Verification: not run yet; documentation and regression changes are pending.
- Risks: avoid weakening explicit ownership or safe-handoff rules while reducing overhead.
