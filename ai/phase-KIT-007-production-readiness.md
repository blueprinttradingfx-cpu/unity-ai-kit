# Phase KIT-007 — Production Readiness and Validation

## Outcome
Make the merged Unity AI Kit internally consistent, safer to adopt, and easier to validate. Prepare the kit for a real consumer-project validation pass in Garden Alchemy.

## Status and ownership
- Status: In Progress
- Phase owner: Gpt
- Integration owner: Gpt
- Branch / PR: `gpt/kit-007-production-readiness`
- Last checkpoint: Initial implementation assembled
- Next milestone: Kit-level checks and independent PR review

## Scope
### In scope
- Correct merged task/session records for KIT-001 through KIT-006.
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
| KIT-007-WP3 | Add validator regression tests and consumer test instructions | Gpt | In Progress | tests/, ai/github-workflows.md | KIT-001 |
| KIT-007-WP4 | Review Unity 6 reference and add governance/security templates | Gpt | In Progress | ai/unity6-reference.md, examples/github/, README.md | KIT-001 |
| KIT-007-WP5 | Integrate, verify full diff, and prepare Garden Alchemy handoff | Gpt | Planned | complete PR diff and evidence | WP1–WP4 |

### KIT-007-WP3 — Validator regression tests
- Owner: Gpt
- Branch: `gpt/kit-007-production-readiness`
- File/system boundary: `tests/`; validator scripts are exercised but not modified unless a failing test proves a defect.
- Acceptance checks:
  - [ ] Tests cover valid metadata, missing/orphan metadata, malformed/duplicate GUIDs.
  - [ ] Tests cover valid/invalid JSON, conflict markers, and invalid YAML when PyYAML is installed.
  - [ ] Test suite uses temporary repositories and does not mutate a consumer project.
- Sub-items:
  - [x] Add unittest harness.
  - [ ] Execute suite and record exact results.

### KIT-007-WP4 — Unity reference and governance
- Owner: Gpt
- Branch: `gpt/kit-007-production-readiness`
- File/system boundary: `ai/unity6-reference.md`, `examples/github/`, README.
- Acceptance checks:
  - [x] Add dated spot review and official references for checked Unity APIs.
  - [ ] Clearly distinguish spot review from exhaustive 6.3/package audit.
  - [ ] Add optional, non-operative CODEOWNERS example and security setup guidance.

## Concurrency and integration
- Safe parallel work: separate documentation, validator test fixtures, and workflow template review can be delegated when file ownership is disjoint.
- Serialized work: session-state, this tracker, and shared workflow files each have one editor at a time.
- Integration sequence: phase owner reviews each work-package diff, integrates, then runs all kit-level checks.

## Phase exit criteria
- [ ] No stale references to PR #1–#3 being open or KIT-001–KIT-006 being in progress.
- [ ] Manual licensed Unity workflow dispatch is default-branch-only.
- [ ] Validator tests pass in a clean Python environment with pinned CI dependencies.
- [ ] All optional governance/security behavior is clearly documented as repository settings or project configuration.
- [ ] Unity reference states exactly what was checked and what remains unverified.
- [ ] Full diff reviewed; independent review findings resolved or explicitly recorded.
- [ ] Garden Alchemy consumer-validation checklist handed off; no consumer-project pass is claimed yet.

## Checkpoint log
- 2026-11-13 — Started KIT-007 from latest main; branch created and first work packages implemented.

## Handoff
- Current owner/status: Gpt / In Progress
- Exact stopping point: initial changes committed on `gpt/kit-007-production-readiness`.
- Next action: complete remaining templates/docs, run tests/static checks, inspect PR diff, and request independent review.
- Verified: branch created from main; workflow dispatch guards and coordination rules added.
- Not verified: test suite execution, actionlint on all templates, GameCI/Unity compile/tests/builds, Garden Alchemy integration.
- Risks / decisions waiting: confirm Garden Alchemy project settings and secrets during consumer validation.
