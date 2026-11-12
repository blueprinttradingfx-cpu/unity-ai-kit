# Phase KIT-007 — Production Readiness and Validation

## Outcome
Make the merged Unity AI Kit internally consistent, safer to adopt, and easier to validate. Prepare the kit for a real consumer-project validation pass in Garden Alchemy.

## Status and ownership
- Status: In Progress
- Phase owner: Gpt
- Integration owner: Gpt
- Branch / PR: `gpt/kit-007-ci-secret-isolation` (follow-up to merged PR #4)
- Last checkpoint: PR #4 merged to main; kit validation passed; post-merge audit identified licensed CI secrets exposed to same-repository PR jobs
- Next milestone: isolate licensed workflow credentials, reconcile tracker evidence, and obtain independent review

## Scope
### In scope
- Correct merged task/session records for KIT-001 through KIT-006.
- Protect Unity license credentials from unreviewed same-repository PR code and document required environment setup.
- Align version-sensitive Unity API references with the kit's Unity 6.3 LTS default and state exactly which claims were spot-checked.
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
| KIT-007-WP7 | Align Unity API reference spot-checks with Unity 6.3 LTS | Gpt | In Progress | ai/unity6-reference.md and official Unity 6000.3 docs | WP4 |

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
  - [x] Execute suite in Kit Validation run `43318886327`: 13 tests passed (9 validator tests + 4 licensed-workflow policy tests).

### KIT-007-WP5 — Post-merge reconciliation and consumer handoff
- Owner: Gpt
- Branch: `gpt/kit-007-ci-secret-isolation`
- File/system boundary: KIT-007 tracker, session-state, README and consumer setup guidance.
- Acceptance checks:
  - [x] Reconcile the tracker with PR #4 merge SHA `6e2e4f0` and Kit Validation run `43292788501`.
  - [ ] Record that PR #4 had no independent review; obtain a separate review of PR #5 before phase completion.
  - [x] Provide `ai/consumer-validation-checklist.md` without claiming Unity runtime validation.

### KIT-007-WP6 — Licensed workflow secret isolation
- Owner: Gpt
- Branch: `gpt/kit-007-ci-secret-isolation`
- File/system boundary: `examples/workflows/*.yml`, `ai/github-workflows.md`, focused workflow tests/documentation.
- Acceptance checks:
  - [ ] Same-repository PR code cannot access Unity license secrets without an explicit protected-environment approval.
  - [ ] Fork PRs remain unable to access licensed secrets and continue to receive repository-quality checks.
  - [ ] Push, scheduled, manual, and release-tag triggers have explicit, documented trust boundaries.
  - [ ] Unity CI templates retain compile/EditMode, PlayMode, and configured build coverage.
  - [x] All example workflows pass actionlint and kit validation in run `43318886327` (13 tests, syntax validation, actionlint). Re-run after the final checklist/README commit.

### KIT-007-WP7 — Unity 6.3 reference alignment
- Owner: Gpt
- Branch: `gpt/kit-007-ci-secret-isolation`
- File/system boundary: `ai/unity6-reference.md`; official Unity documentation only.
- Acceptance checks:
  - [x] Replace 6.0 references with official 6.3 (6000.3) links where directly checked.
  - [x] Explicitly distinguish directly checked 6.3 API claims from general migration reminders.
  - [x] Keep the Awaitable 6.0 reference clearly labeled and its 6.3-specific details unverified.
  - [ ] Validate all referenced URLs and rerun kit checks.

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
- [ ] No stale references to PR #1–#3 being open or KIT-001–KIT-006 being in progress.
- [ ] Manual licensed Unity workflow dispatch is default-branch-only.
- [ ] Licensed CI secrets are isolated from unreviewed same-repository pull-request code through protected environments or an equivalent explicit trust gate.
- [ ] Validator tests pass in a clean Python environment with pinned CI dependencies.
- [ ] All optional governance/security behavior is clearly documented as repository settings or project configuration.
- [ ] Unity reference states exactly what was checked and what remains unverified; 6.3-specific links are verified.
- [ ] Full diff reviewed; independent review findings resolved or explicitly recorded.
- [ ] Garden Alchemy consumer-validation checklist handed off; no consumer-project pass is claimed yet.

## Checkpoint log
- 2026-11-13 — PR #4 merged to main as `6e2e4f039562514101373d6b5478fcdad8e5335a`; Kit Validation run passed. PR #4 has no submitted reviews. Post-merge workflow audit identified a same-repository PR secret-exposure gap; follow-up WP5/WP6 opened on `gpt/kit-007-ci-secret-isolation`.

## Handoff
- Current owner/status: Gpt / In Progress
- Exact stopping point: initial changes committed on `gpt/kit-007-production-readiness`.
- Next action: complete remaining templates/docs, run tests/static checks, inspect PR diff, and request independent review.
- Verified: branch created from main; workflow dispatch guards and coordination rules added.
- Not verified: test suite execution, actionlint on all templates, GameCI/Unity compile/tests/builds, Garden Alchemy integration.
- Risks / decisions waiting: confirm Garden Alchemy project settings and secrets during consumer validation.
