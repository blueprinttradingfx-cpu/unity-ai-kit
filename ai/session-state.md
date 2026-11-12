# Project / Work Board

This is the low-churn coordination summary, not a task diary. Detailed scope and sub-item progress belong in the relevant phase tracker. Update this file only for ownership, phase status, blockers, priority, milestone, or handoff changes.

Read `ai/coordination-model.md` before coordinating parallel work. Backlog, blocked, and completed work remain in `ai/backlog-tasks.md`, `ai/blocked-tasks.md`, and `ai/done-tasks.md`.

**Session username for the session that last updated this file:** `Gpt`

## Active work

| Phase / task | Status | Owner | Branch / tracker | Current checkpoint / next milestone |
|---|---|---|---|---|
| KIT-001–KIT-004 — Agent safeguards and CI quality foundation | In Progress | `gpt` | PR #1: `gpt/harden-agent-workflow` | Draft implementation; full workflow validation and independent review pending |
| KIT-005 — Nightly regression and protected release templates | In Progress | `Gpt` | PR #2: `gpt-ci/nightly-release-workflows` | Draft implementation; actionlint/YAML validation and consumer run pending |
| KIT-006 — Phase-based multi-agent coordination model | In Progress | `Gpt` | PR #3: `gpt/phase-based-coordination` | Add phase ownership rules, low-churn session summary, and reusable tracker template |

## Coordination rules at a glance
- Phase or substantial work package is the normal ownership unit; sub-items are grouped inside its tracker.
- One accountable phase owner coordinates the phase. Split work-package ownership only when file boundaries and dependencies are genuinely independent.
- Agents may complete several related sub-items before checkpointing; do not create a shared-board update for every small action.
- Never allow overlapping ownership of the same scene, prefab, asset, API contract, or high-conflict file without an explicit integration plan.
- Session identity is not phase ownership. A session username identifies the agent; the phase tracker records who owns the phase/work package.

## Project context
- **Repository:** reusable Unity AI guidance and inactive CI templates; no Unity game project is hosted here.
- **Current base:** `gpt-ci/nightly-release-workflows`, stacked on PR #1 and PR #2; this change is a separate draft PR.
- **Last known good build:** Not applicable to this documentation/workflow-template repository.

## Handoff
- **Exact stopping point:** KIT-006 coordination model and template are being added on `gpt/phase-based-coordination`.
- **Next step:** inspect the complete diff, run documentation/source checks available here, and request independent review. Then migrate Garden Alchemy's live coordination summary to phase-level ownership without deleting phase history.
- **Verified:** Existing PR #1 and #2 remain open and unmerged. PR #2 head used as the base for this branch.
- **Not verified:** Unity compile/tests are not applicable; workflow validation still belongs to PR #1/#2 and consumer repositories.
- **Owner decisions waiting:** None for the coordination model; projects choose their own phase boundaries and concurrency limits.
- **Known risks:** A tracker can become a second noisy board if agents log every micro-action. Keep sub-item updates inside the owning phase file and use checkpoints.
