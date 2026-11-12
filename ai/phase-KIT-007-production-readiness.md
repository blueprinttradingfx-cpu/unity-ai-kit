# Phase KIT-007 — Production Readiness and Validation

## Outcome
Make the merged Unity AI Kit internally consistent, safer to adopt, and easier to validate. Prepare the kit for a real consumer-project validation pass in Garden Alchemy.

## Status and ownership
- Status: In Progress
- Phase owner: Gpt
- Integration owner: Gpt
- Branch / PR: `gpt/kit-007-ci-secret-isolation` (follow-up to merged PR #4)
- Last checkpoint: PR #4 merged to main; kit validation passed; post-merge audit identified licensed CI secrets exposed to same-repository PR jobs
- Next milestone: merge the owner-reviewed kit hardening PR, then hand off to consumer-project validation

## Scope
### In scope
- Correct merged task/session records for KIT-001 through KIT-006.
- Protect Unity license credentials from unreviewed same-repository PR code and document required environment setup.
- Align version-sensitive Unity API references with the kit's Unity 6.3 LTS default and state exactly which claims were spot-checked.
- Upgrade every JavaScript-based workflow action to a verified Node 24-compatible release and keep all action references pinned to full SHAs.
- Default standalone .NET validation to a supported LTS SDK and record the current support-policy basis.
- Add phase readiness, integration ownership, bounded concurrency, and tracker ownership rules.
- Restrict manual licensed Unity CI dispatch to the default branch.
- Improve standalone .NET SDK configurability, analyzer formatting, and optional NuGet vulnerability audit.
- Add regression tests for both repository validators.
- Spot-check Unity 6 reference claims against official Unity documentation and make review limits explicit.
- Add optional CODEOWNERS/security/governance starter guidance.
- Document Garden Alchemy as the follow-on consumer validation target.

### Out of scope
- Running licensed Unity Editor/GameCI jobs in this template repository.
- Changing Garden Alchemy or any other consumer repository in this PR.
- Enabling repository rulesets, branch protection, secret scanning, or CODEOWNERS ownership assignments without project-specific owners.
- Claiming Unity compile, PlayMode, platform build, or device validation before Garden Alchemy testing.

## Dependencies and decisions
- Depends on: KIT-001 through KIT-006 merged to main (satisfied).
- Consumer validation requires Garden Alchemy's actual Unity version, project path, build targets, test assemblies, and license configuration.
- Repository governance examples must be configured with real maintainers and required check names by each consumer.

## Work packages

| ID | Outcome | Owner | Status | Allowed files/systems | Depends on |
|---|---|---|---|---|---|
| KIT-007-WP1 | Correct historical coordination state and strengthen phase ownership/readiness | Gpt | Done | ai/session-state.md, ai/coordination-model.md, phase tracker | KIT-006 |
| KIT-007-WP2 | Harden licensed CI dispatch and improve standalone .NET checks | Gpt | Done | examples/workflows, ai/github-workflows.md | KIT-001, KIT-005 |
| KIT-007-WP3 | Add validator regression tests and consumer test instructions | Gpt | Done | tests/, ai/github-workflows.md | KIT-001 |
| KIT-007-WP4 | Review Unity 6 reference and add governance/security templates | Gpt | Done | ai/unity6-reference.md, examples/github/, README.md | KIT-001 |
| KIT-007-WP5 | Reconcile merged implementation, review evidence, and prepare consumer handoff | Gpt | In Progress | complete PR #4 diff, phase tracker, consumer handoff docs | WP1–WP4 |
| KIT-007-WP6 | Harden licensed workflow secret boundaries and verify workflow triggers | Gpt | Done | examples/workflows/*.yml, ai/github-workflows.md, tests/ and workflow validation | WP2, WP3 |
| KIT-007-WP7 | Align Unity API reference spot-checks with Unity 6.3 LTS | Gpt | Done | ai/unity6-reference.md and official Unity 6000.3 docs | WP4 |
| KIT-007-WP8 | Upgrade GitHub Actions pins to Node 24-compatible releases | Gpt | Done | all active/example workflows, action pin tests, workflow docs | WP2, WP6 |
| KIT-007-WP9 | Align standalone .NET SDK default with current LTS support | Gpt | Done | examples/workflows/dotnet-validation.yml, tests, ai/github-workflows.md | WP2, WP8 |

### KIT-007-WP3 — Validator regression tests
- Owner: Gpt
- Branch: `gpt/kit-007-ci-secret-isolation` (tests added after PR #4 merge)
- File/system boundary: `tests/`; validator scripts are exercised but not modified unless a failing test proves a defect.
- Acceptance checks:
  - [x] Tests cover valid metadata, missing/orphan metadata, malformed/duplicate GUIDs.
  - [x] Tests cover valid/invalid JSON, conflict markers, and invalid YAML when PyYAML is installed.
  - [x] Test suite uses temporary repositories and does not mutate a consumer project.
- Sub-items:
  - [x] Add unittest harness.
  - [x] Execute suite in Kit Validation run `43320593384`: 16 tests passed, including workflow secret-gate, default-branch dispatch, action pin, and .NET LTS checks.

### KIT-007-WP5 — Post-merge reconciliation and consumer handoff
- Owner: Gpt
- Branch: `gpt/kit-007-ci-secret-isolation`
- File/system boundary: KIT-007 tracker, session-state, README and consumer setup guidance.
- Acceptance checks:
  - [x] Reconcile the tracker with PR #4 merge SHA `6e2e4f0` and Kit Validation run `43292788501`.
  - [x] Record PR #4's lack of review and PR #5's owner-authored audit review transparently; maintainer decision: owner review is sufficient for this kit, and no independent reviewer is required.
  - [x] Provide `ai/consumer-validation-checklist.md` without claiming Unity runtime validation.

### KIT-007-WP6 — Licensed workflow secret isolation
- Owner: Gpt
- Branch: `gpt/kit-007-ci-secret-isolation`
- File/system boundary: `examples/workflows/*.yml`, `ai/github-workflows.md`, focused workflow tests/documentation.
- Acceptance checks:
  - [x] Same-repository PR jobs use the reviewer-gated `unity-pr-validation` environment; consumer configuration is documented.
  - [x] Fork PRs skip licensed jobs and continue to receive repository-quality checks.
  - [x] Push, scheduled, manual, and release-tag triggers have explicit, documented trust boundaries.
  - [x] Unity CI templates retain compile/EditMode, PlayMode, and configured build coverage.
  - [x] All example workflows pass actionlint and kit validation in run `43320593384` (16 tests, source/config syntax validation, actionlint).

### KIT-007-WP7 — Unity 6.3 reference alignment
- Owner: Gpt
- Branch: `gpt/kit-007-ci-secret-isolation`
- File/system boundary: `ai/unity6-reference.md`; official Unity documentation only.
- Acceptance checks:
  - [x] Replace 6.0 references with official 6.3 (6000.3) links where directly checked.
  - [x] Explicitly distinguish directly checked 6.3 API claims from general migration reminders.
  - [x] Keep the Awaitable 6.0 reference clearly labeled and its 6.3-specific details unverified.
  - [x] Validate all referenced official documentation URLs through Unity's 6000.3 docs index; kit validation passed in run `43319820626`.

### KIT-007-WP8 — GitHub Actions runtime upgrade
- Owner: Gpt
- Branch: `gpt/kit-007-ci-secret-isolation`
- File/system boundary: `.github/workflows/`, `examples/workflows/`, action pin regression tests, `ai/github-workflows.md`.
- Acceptance checks:
  - [x] Replace Node 20 first-party action pins with verified Node 24 releases.
  - [x] Upgrade GameCI test-runner and builder pins to Node 24 releases; verify their `action.yml` declarations.
  - [x] Keep all action references pinned to full commit SHAs verified from upstream tags.
  - [x] Document GitHub's Node 20 removal and current reviewed action versions.
  - [x] Run actionlint and the action-pin regression test on final PR commit `c30ef1be`; run `43319820626` passed 14 tests and workflow lint.

### KIT-007-WP9 — Supported .NET LTS default
- Owner: Gpt
- Branch: `gpt/kit-007-ci-secret-isolation`
- File/system boundary: standalone .NET workflow, SDK support guidance, focused regression test.
- Acceptance checks:
  - [x] Default the standalone .NET workflow to .NET 10 LTS (`10.0.x`).
  - [x] Document why .NET 8/9 are no longer appropriate defaults and link Microsoft's current support policy.
  - [x] Validated in Kit Validation run `43320593384` (16 tests, including .NET SDK default regression test).

### KIT-007-WP4 — Unity reference and governance
- Owner: Gpt
- Branch: `gpt/kit-007-production-readiness`
- File/system boundary: `ai/unity6-reference.md`, `examples/github/`, README.
- Acceptance checks:
  - [x] Add dated spot review and official references for checked Unity APIs.
  - [x] Clearly distinguish spot review from exhaustive 6.3/package audit.
  - [x] Add optional, non-operative CODEOWNERS example and security setup guidance.

## Concurrency and integration
- Safe parallel work: separate documentation, validator test fixtures, and workflow template review can be delegated when file ownership is disjoint.
- Serialized work: session-state, this tracker, and shared workflow files each have one editor at a time.
- Integration sequence: phase owner reviews each work-package diff, integrates, then runs all kit-level checks.

## Phase exit criteria
- [x] No stale references to PR #1–#3 being open or KIT-001–KIT-006 being in progress.
- [x] Manual licensed Unity workflow dispatch is default-branch-only (workflow conditions and regression test).
- [x] Licensed CI secrets are isolated from unreviewed same-repository pull-request code through reviewer-gated environments; consumer configuration is documented.
- [x] Validator and workflow security tests pass in a clean Python environment; run `43320593384` passed 16 tests.
- [x] Optional governance/security behavior is documented as repository settings or project configuration.
- [x] Unity reference states exactly what was checked and what remains unverified; 6.3-specific links are verified.
- [x] Full PR #5 diff reviewed; owner-authored audit comment submitted on commit `1c9b7b38a6a8565dab25b9b6ea1fb7cbc3c3b534` (review ID `5883211309`). The review is a COMMENTED owner review, not an independent approval.
- [x] Garden Alchemy consumer-validation checklist handed off; no consumer-project pass is claimed yet.

## Checkpoint log
- 2026-11-13 — PR #4 merged to main as `6e2e4f039562514101373d6b5478fcdad8e5335a`; Kit Validation run `43292788501` passed. PR #4 has no submitted reviews. Post-merge workflow audit identified a same-repository PR secret-exposure gap; follow-up WP5/WP6 opened on `gpt/kit-007-ci-secret-isolation`.
- 2026-11-13 — PR #5 follow-up now includes protected environment secret gates, explicit default-branch guards, Node 24 action pins, Unity 6.3 reference corrections, .NET 10 LTS defaults, and a consumer checklist. Kit Validation run `43320593384` on `1c9b7b38` passed 16 tests, source/config syntax checks, and actionlint. Owner audit comment `5883211309` was submitted; PR #5 was marked ready for review. The maintainer chose owner review as sufficient for this kit.

## Handoff
- Current owner/status: Gpt / In Progress
- Exact stopping point: PR #5 is ready for maintainer merge consideration on `gpt/kit-007-ci-secret-isolation`; owner audit comment is recorded.
- Next action: merge PR #5 after maintainer authorization, then hand off to the separately scoped Garden Alchemy consumer-validation phase.
- Verified: 16 kit regression tests, source/config syntax validation, actionlint, full PR diff inspection, and owner audit comment.
- Not verified: real consumer GitHub Environment protection settings, licensed GameCI execution, Unity Editor import/compile, EditMode/PlayMode tests, target builds, or device behavior.
- Risks / decisions waiting: confirm Garden Alchemy project settings and secrets during consumer validation.
