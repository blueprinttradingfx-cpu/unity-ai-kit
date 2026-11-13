# Phase KIT-008 — Garden Alchemy Consumer Feedback

## Outcome

Fold reusable lessons from the first real Unity AI Kit consumer, Garden Alchemy, back into the master kit. Keep consumer-specific game code, Unity version, asset layout, and project policy in Garden Alchemy.

## Status and ownership

- Status: In Progress
- Phase owner: Gpt
- Integration owner: Gpt
- Branch: `gpt/garden-alchemy-consumer-feedback`
- Consumer evidence: Garden Alchemy PR #41 (merged), PR #45 and #46 (open for owner review)
- Next milestone: kit validation passes and owner-reviewed PR opened

## Scope

### In scope

- Offer both reviewer-gated licensed PR validation and mainline-only licensed validation.
- Keep fork PRs on unlicensed repository-quality checks; never expose Unity credentials to untrusted PR code.
- Set `persist-credentials: false` on Unity workflow checkouts.
- Preserve full-SHA action pins, job timeouts, and per-ref concurrency controls.
- Document safe, project-specific path filters and optional disk cleanup for GameCI runner constraints.
- Update consumer setup checklist and regression tests for the alternate trust model.

### Out of scope

- Copying Garden Alchemy game code, project settings, catalog, scene structure, or Unity version into the kit.
- Making Garden's exact path filters, disk cleanup configuration, or environment names universal defaults.
- Claiming the kit can prove Unity activation, Editor compilation, EditMode/PlayMode, target build, or device success.
- Replacing the reviewer-gated workflow; both security models remain available for different team structures.

## Work packages

| ID | Outcome | Owner | Status | File/system boundary |
|---|---|---|---|---|
| KIT-008-WP1 | Audit Garden Alchemy consumer changes and identify reusable lessons | Gpt | Done | Read-only consumer PR/workflow audit |
| KIT-008-WP2 | Add mainline-only licensed Unity CI template and security regression tests | Gpt | Done | `examples/workflows/unity-ci-mainline-only.yml`, `tests/test_workflow_security.py` |
| KIT-008-WP3 | Minimize checkout credential persistence across Unity workflows | Gpt | Done | Unity CI, nightly, and release templates |
| KIT-008-WP4 | Document trust-model selection, path filtering, runner cleanup, and local-validation handoff | Gpt | Done | README, `ai/github-workflows.md`, consumer checklist |
| KIT-008-WP5 | Run kit validation, inspect full diff, and prepare owner review | Gpt | In Progress | Kit validation workflow, this tracker, session state |

## Acceptance criteria

- [x] Mainline-only template has no PR trigger and limits licensed jobs to trusted default-branch execution.
- [x] Mainline-only template keeps EditMode, PlayMode, and build jobs behind the `unity-ci` environment.
- [x] Reviewer-gated template remains available and is explicitly documented as requiring an independent approver.
- [x] Unity workflow checkout steps do not persist GitHub credentials.
- [x] Path filters are documented as consumer-specific and must include workflow files and all project inputs.
- [x] Disk cleanup is documented as an opt-in response to observed runner disk pressure, not a default requirement.
- [x] Regression tests cover both trust models and checkout credential settings.
- [ ] Kit Validation passes source/config syntax checks, regression tests, and actionlint on the final PR commit.
- [ ] Full diff is reviewed and PR is opened for owner review.

## Checkpoint log

- 2026-11-13 — Audited Garden Alchemy's merged CI hardening and subsequent PRs. Reusable lessons: mainline-only licensed execution is safer and more operable than self-approval when no independent approver exists; retain unlicensed PR checks; disable persisted checkout credentials; use narrow path filters only when mapped to the actual Unity project layout; treat disk cleanup as an observed-runner mitigation.
- 2026-11-13 — Added the alternate mainline-only Unity CI template, updated the reviewer-gated template and all Unity checkout steps, added security regression tests, and updated README/workflow/consumer guidance.

## Handoff

- Current owner/status: Gpt / In Progress.
- Exact stopping point: template and documentation changes are on `gpt/garden-alchemy-consumer-feedback`; validation is pending.
- Next action: run Kit Validation on the branch, inspect all failures and final diff, then open a PR.
- Verified: consumer changes were reviewed; template changes and tests are committed to the branch.
- Not verified: Kit Validation for this branch; no consumer Unity execution is claimed.
- Risks: the new mainline-only template assumes the default branch is named `main` for push triggers; consumers with another default branch must change the push branch filter while retaining the dynamic manual-dispatch guard.
