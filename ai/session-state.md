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

**Session username for the session that last wrote this file:** `gpt`

## Board

Author = the agent that owns the task, `owner` = the human owner. Every task uses a stable ID (for example `KIT-001`) prefixed in its Task text; preserve it when moving the task between lists.

| Status | Task | Author | Notes / next step |
|---|---|---|---|
| In Progress | KIT-001 — Harden the reusable agent workflow and verification safeguards | `gpt` | Implemented task lifecycle, safe claim/handoff guidance, and evidence-based completion checks. Awaiting independent review. |
| In Progress | KIT-002 — Add Unity GitHub Actions and repository quality standards | `gpt` | Implemented configurable GameCI test/build and repository-quality templates, metadata validator, EditorConfig, Dependabot and PR templates, plus CI/CD guidance. YAML parsed and metadata validator fixtures passed; actionlint and independent review remain pending. |
| In Progress | KIT-003 — Add explicit Unity C# compile and standalone .NET checks | `gpt` | Added a dedicated Unity Editor import/C# compile + EditMode job, separate PlayMode job, and optional standalone .NET restore/build/test/format workflow. Workflow validation and PR update pending. |

## Project context
- **Branch / build:** `gpt/harden-agent-workflow` / no Unity project in this reusable guidance repository.
- **Last known good build:** Not applicable; documentation and workflow-template kit.

## Handoff
- **In progress (exact stopping point):** KIT-001 through KIT-004 changes are on `gpt/harden-agent-workflow`. Latest work (latest work adds `examples/scripts/validate_source_syntax.py` and extends repository-quality CI) adds `examples/workflows/dotnet-validation.yml`, `examples/scripts/validate_source_syntax.py`, splits `examples/workflows/unity-ci.yml` into an explicit Unity Editor import/C# compile + EditMode job and a PlayMode job, and updates `ai/github-workflows.md`, `README.md`, and `ai/definition-of-done.md`, and incorporates reusable audit findings from Garden Alchemy, Weapon Ball Unity, and Heartway.
- **Next concrete step:** Validate all workflow YAML and shell snippets, verify every action reference is pinned to a full SHA, update PR #1 body, then inspect GitHub checks. Run actionlint in a network-enabled environment and request independent review before marking PR #1 ready.
- **Known broken:** `ai/unity6-reference.md` still has an unfilled review-date placeholder; it is explicitly described as unverified in README and should be reviewed against official docs before being treated as current API guidance.
- **Verified (ran it):** Previous metadata validator fixtures passed/fail as expected; prior workflow YAML parsed; previous action references used full SHAs. New workflow has not yet been validated in GitHub Actions.
- **Not verified (human must check on device/editor):** No actual Unity project exists in this kit, so Unity compile/tests/build and standalone .NET build cannot run here. Garden Alchemy's retired-Arena symbol checks and Weapon Ball's catalog/save/SQLite rules remain project-owned; Heartway's Firestore emulator tests remain optional backend-specific checks. Consumer setup must supply the actual Unity Editor version, project path, platform, license secrets, and optional `DOTNET_PROJECT_PATHS` variable. Full actionlint execution remains pending.
- **Owner decisions waiting:** Consumer projects must select their platform, license type, release policy, and any standalone .NET project paths; no choice is needed for this reusable kit change.
- **Bug / regression watch:** Do not activate Unity workflows in this master kit; keep examples under `examples/`. Never expose Unity or signing secrets to fork PRs. Do not run generic `dotnet build` against Unity-generated `.sln/.csproj` files.
