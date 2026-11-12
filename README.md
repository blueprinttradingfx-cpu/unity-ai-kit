# Unity AI Kit — provider-neutral starter for new Unity games

Drop-in guidance and optional CI templates so any AI coding assistant (Claude, Codex, Gemini, Cursor, Copilot, local models, web chat) works the same way on your Unity projects. The core guidance is plain Markdown; optional examples include GitHub Actions workflows and a read-only Unity metadata validator.

Inspired by the ideas in `donchitos/claude-code-game-studios` (path-scoped rules, decision records, definition of done, session state), but without its Claude-only machinery (49 agents, 74 skills, bash hooks), and with the Unity reference rewritten and corrected.

## Set up a new project (10 minutes)
1. Copy everything except `README.md` into the **root of your Unity project repo** (next to `Assets/`).
2. Rename `examples/Unity.gitignore` → `.gitignore`, `examples/Unity.gitattributes` → `.gitattributes`, and `examples/Unity.editorconfig` → `.editorconfig` (skip any you already have good equivalents for). In Unity: Editor settings → Asset Serialization = Force Text, Version Control = Visible Meta Files.
3. Edit `AGENTS.md`: game name, platform, folder layout, and the **Commands** section (Unity.exe path). This lets AIs that can run commands verify their work.
4. Fill `ai/project-brief.md` (pillars, device, constraints). Short is fine.
5. Delete the pointer files for tools you do not use (see table). Optional: `examples/claude-settings.json` → `.claude/settings.json`.
6. First commit: "Add AI guidance kit".

## GitHub CI/CD setup
The kit includes optional, inactive templates for Unity CI and repository checks:
- Copy `examples/workflows/unity-ci.yml` to `.github/workflows/unity-ci.yml`, then configure the target platform and Unity license secrets.
- Copy `examples/workflows/repository-quality.yml` to `.github/workflows/repository-quality.yml` and `examples/scripts/validate_unity_meta.py` to `examples/scripts/` in the project. This runs without Unity licensing secrets and checks metadata integrity.
- For separate SDK-style .NET tools/services/tests, optionally copy `examples/workflows/dotnet-validation.yml` and configure the newline-separated `DOTNET_PROJECT_PATHS` repository variable. It runs restore, Release build, tests, and `dotnet format` verification.
- Copy `examples/github/dependabot.yml` to `.github/dependabot.yml` and `examples/github/PULL_REQUEST_TEMPLATE.md` to `.github/PULL_REQUEST_TEMPLATE.md`.
- Read `ai/github-workflows.md` before enabling workflows. It covers fork PR secret safety, Unity Editor C# compilation, EditMode/PlayMode tests, standalone .NET checks, branch protection, platform/release checks, and action pinning.

Do not copy the templates blindly: set the project's actual Editor version, project path, build target, license type, and protected release process. The examples are not active in this master kit repository.

## How it works
- `AGENTS.md` is the single source of truth. It stays short: hard rules, a routing table, commands, and working style.
- Each tool gets a 1–3 line pointer to it, so you maintain one file.
- Detail is in `ai/rules/*.md`, read only when the work matches (saves context, works in any tool).
- `ai/session-state.md` carries "where we stopped" between sessions and between **different AIs**.
- `ai/task-lifecycle.md` defines how tasks are created, claimed, handed off, and closed; task IDs stay with a task as it moves between status lists.
- `ai/decisions/` holds one-page decisions so a new AI doesn't re-open or contradict them.
- `ai/definition-of-done.md` requires evidence, not an unsupported "done" claim.

| Tool | Reads | Kit file |
|---|---|---|
| Claude Code | `CLAUDE.md` | `CLAUDE.md` (imports AGENTS.md) |
| Gemini CLI | `GEMINI.md` | `GEMINI.md` (imports AGENTS.md) |
| Cursor | `.cursor/rules`, and AGENTS.md | `.cursor/rules/unity.mdc` |
| GitHub Copilot | `.github/copilot-instructions.md`, and AGENTS.md | same path |
| OpenAI Codex CLI and others that support it | `AGENTS.md` | `AGENTS.md` |
| Web chat / no file support | nothing | paste `ai/prompts/start-session.md` + `AGENTS.md` |

Tool conventions change often. If a tool ignores its pointer, open its docs and look for "custom instructions" / "context file", or paste `AGENTS.md` into its instructions field. Windows note: the kit uses small pointer files instead of symlinks, because symlinks are unreliable on Windows git.

## Daily use
- **Start:** identify your session username, read `ai/task-lifecycle.md` and `ai/session-state.md`, then claim the matching Ready task before editing. If the user's explicit goal has no board row, create and claim one; do not invent unrelated work.
- **Feature:** use `ai/prompts/new-feature.md` (plan first, then "go").
- **Unsure about a technical choice:** use `ai/prompts/spike.md`, then record an ADR.
- **Review:** use `ai/prompts/review.md` with a different provider for meaningful code changes and high-risk guidance/architecture changes.
- **End:** report the exact checks and evidence, update the handoff, and move the task to `ai/done-tasks.md`, `ai/blocked-tasks.md`, or `ai/backlog-tasks.md` as appropriate.
- **Milestone:** run the 10-minute smoke test at the bottom of `ai/definition-of-done.md` on a real phone.

## Limits (be aware)
- These are instructions, not enforcement. Tools without permission controls can still ignore them; keep the git safety net (commit before AI sessions, work on branches).
- `ai/unity6-reference.md` is a list of common mistakes written from general knowledge, not official docs. Its review date is intentionally a placeholder until someone checks the claims against official docs and the project's installed package versions. Entries marked Medium need verifying; do not treat this file as authoritative API documentation.
- An AI without editor access cannot compile. The kit makes it say so and hand you a precise check list.
- Keep `AGENTS.md` under ~120 lines. Long instruction files get skimmed and partially ignored.

## Keeping it reusable
Improve the kit in one master repo (`unity-ai-kit`); copy into new projects. When a lesson from a project is general (a Unity gotcha, a better rule), port it back to the master. Project-specific facts stay in that project's `ai/project-brief.md` and ADRs.
