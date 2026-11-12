# Project / Work Board

This board is shared by several agents working at the same time. Read it at the start of every session and update it before you finish. It shows only **Ready** and **In Progress** tasks. Other tasks are in these lists:
- `ai/blocked-tasks.md`: Blocked tasks, and what each one waits on.
- `ai/done-tasks.md`: finished work (built, merged, or accepted).
- `ai/backlog-tasks.md`: not started and not yet Ready.

When a task's status changes, move its row to the list for its new status. Keep this file under ~60 lines. Details live in the tracker log or the project's decision records.

**Rules for every agent, every session:**
1. Each session is one agent. At the start, ask the user for your `session_username`. Do not reuse a name you saw in this file.
2. To start a Ready task, set its Author to your `session_username` and Status to `In Progress`. You own it until it is Done or you hand it back.
3. Never start a task whose Author is another name, or `owner`, unless the user tells you to take it over.
4. When you finish or stop, update Status, Notes / next step, and the Handoff section, and move the row if its status changed. Leave your name in Author only while you still own the task.

**Session username for the session that last wrote this file:** `Gpt`

## Board

Author = the agent that owns the task, `owner` = the human owner. Every task uses a stable ID (for example `KIT-001`) prefixed in its Task text; preserve it when moving the task between lists.

| Status | Task | Author | Notes / next step |
|---|---|---|---|
| In Progress | KIT-001 — Harden the reusable agent workflow and verification safeguards | `gpt` | Implemented task lifecycle, safe claim/handoff guidance, and evidence-based completion checks. Awaiting independent review. |
| In Progress | KIT-002 — Add Unity GitHub Actions and repository quality standards | `gpt` | Implemented configurable GameCI test/build and repository-quality templates, metadata validator, EditorConfig, Dependabot and PR templates, plus CI/CD guidance. YAML parsed and metadata validator fixtures passed; actionlint and independent review remain pending. |
| In Progress | KIT-003 — Add explicit Unity C# compile and standalone .NET checks | `gpt` | Added a dedicated Unity Editor import/C# compile + EditMode job, separate PlayMode job, and optional standalone .NET restore/build/test/format workflow. Full workflow validation and independent review pending. |
| In Progress | KIT-004 — Consolidate reusable checks from the existing game repositories | `gpt` | Audited Garden Alchemy, Weapon Ball Unity, and Heartway. Added generic tracked-source syntax/conflict-marker validation and documented project-owned data/regression validators plus optional backend emulator tests. Full validation pending. |
| In Progress | KIT-005 — Add reusable nightly regression and protected release workflow templates | `Gpt` | Added scheduled EditMode/PlayMode + Linux/Android matrix template and tag-based release test/build template with protected `release` environment, provenance, and SHA-256 checksums. Workflow validation and independent review pending. |

## Project context
- **Branch / build:** `gpt-ci/nightly-release-workflows` (stacked on `gpt/harden-agent-workflow`) / no Unity project in this reusable guidance repository.
- **Last known good build:** Not applicable; documentation and workflow-template kit.

## Handoff
- **In progress (exact stopping point):** KIT-001 through KIT-004 remain on `gpt/harden-agent-workflow` (PR #1). KIT-005 is on `gpt-ci/nightly-release-workflows`, based on that branch (draft PR #2: https://github.com/blueprinttradingfx-cpu/unity-ai-kit/pull/2). Added `examples/workflows/unity-nightly.yml` and `examples/workflows/unity-release.yml`; updated `ai/github-workflows.md`, `README.md`, and `ai/definition-of-done.md`. Nightly runs separate EditMode/PlayMode tests then Linux Standalone + Android builds. Release resolves the version tag once, pins all test/build jobs to that immutable commit SHA, writes provenance/checksums, and gates build access through the `release` GitHub Environment. Signing and store publishing are deliberately project-configured.
- **Next concrete step:** Run YAML parsing/actionlint and shell checks in a network-enabled environment, then request independent review before marking PR #2 ready. Consumer projects must configure their own `release` Environment reviewers/signing secrets and validate the platform matrix.
- **Known broken:** `ai/unity6-reference.md` still has an unfilled review-date placeholder; it is explicitly described as unverified in README and should be reviewed against official docs before being treated as current API guidance.
- **Verified (ran it):** Previous metadata validator fixtures passed/fail as expected; earlier workflow YAML parsed and action references used full SHAs. For KIT-005, checked balanced GitHub expression delimiters, 40-character action pins, and absence of `pull_request_target`/PR triggers. Review found and fixed a mutable-tag race: release tests/builds now checkout the immutable commit SHA resolved by the validation job, and provenance records that SHA through an environment variable. Full YAML parsing/actionlint and consumer Unity build/test have not yet run.
- **Not verified (human must check on device/editor):** No actual Unity project exists in this kit, so Unity compile/tests/build and standalone .NET build cannot run here. Garden Alchemy's retired-Arena symbol checks and Weapon Ball's catalog/save/SQLite rules remain project-owned; Heartway's Firestore emulator tests remain optional backend-specific checks. Consumer setup must supply the actual Unity Editor version, project path, platform, license secrets, and optional `DOTNET_PROJECT_PATHS` variable. Full actionlint execution remains pending.
- **Owner decisions waiting:** Consumer projects must select their platform matrix, license type, release-tag protection, required reviewers for the `release` environment, platform signing configuration, release retention, and any standalone .NET project paths.
- **Bug / regression watch:** Do not activate Unity workflows in this master kit; keep examples under `examples/`. Never expose Unity or signing secrets to fork PRs. Do not run generic `dotnet build` against Unity-generated `.sln/.csproj` files.
