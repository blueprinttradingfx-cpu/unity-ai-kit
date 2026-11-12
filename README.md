# Unity AI Kit — provider-neutral starter for new Unity games

Drop-in guidance and optional CI templates so any AI coding assistant (Claude, Codex, Gemini, Cursor, Copilot, local models, web chat) works consistently across Unity projects. Core guidance is plain Markdown; optional examples include GitHub Actions workflows and read-only validators.

Inspired by path-scoped rules, decision records, definition-of-done checks, and session handoffs, without provider-specific agent machinery.

## Set up a new project
1. Copy the kit guidance into the root of your Unity project repo (next to `Assets/`).
2. Rename the example Unity gitignore/gitattributes/editorconfig files as needed. In Unity, use Force Text serialization and Visible Meta Files.
3. Edit `AGENTS.md`: game name, platform, folder layout, and verification commands.
4. Fill `ai/project-brief.md` (pillars, device, constraints).
5. Remove tool pointer files for tools you do not use.
6. Commit the adopted baseline.

## Multi-agent coordination model
The default ownership unit is a **phase or substantial work package**, not an individual micro-task. See `ai/coordination-model.md` and copy `examples/phase-tracker-template.md` when a project needs a phase tracker.

- `ai/session-state.md` is a concise global coordination summary: active phases, owners, blockers, next milestones, and handoffs.
- The phase tracker is the source of truth for scope, work packages, sub-items, dependencies, acceptance criteria, and checkpoint evidence.
- Agents can complete several related sub-items before updating shared coordination state. Update the global summary only when ownership, status, blockers, priority, milestone, or handoff changes.
- Parallel work is allowed only with explicit file/system boundaries and resolved dependencies. Do not assign two agents the same scene, prefab, asset, or high-conflict contract simultaneously.
- Session username identifies the current agent; phase ownership is recorded separately in the tracker.

## GitHub CI/CD setup
The kit includes optional, inactive templates for Unity CI and repository checks:
- Copy `examples/workflows/unity-ci.yml` to `.github/workflows/unity-ci.yml`, then configure the target platform and Unity license secrets.
- Copy `examples/workflows/repository-quality.yml` and the validator scripts for source/config syntax, conflict markers, whitespace, and metadata integrity.
- For separate SDK-style .NET tools/services/tests, optionally copy `examples/workflows/dotnet-validation.yml` and configure project paths.
- Copy the Dependabot and pull-request templates if useful.
- Optionally copy `examples/workflows/unity-nightly.yml` for scheduled EditMode/PlayMode regression and a platform build matrix.
- Optionally copy `examples/workflows/unity-release.yml` for version-tagged test/build artifacts with checksums. Configure protected environment reviewers and project-specific signing before use.
- Read `ai/github-workflows.md` before enabling workflows.

Do not copy templates blindly: configure the project's actual Editor version, project path, build target, license type, and release process. Examples are inactive in the master kit.

## How the guidance is organized
- `AGENTS.md` is the short entry point and source of hard rules.
- Tool-specific pointer files direct assistants to `AGENTS.md`.
- `ai/rules/*.md` contains topic-specific detail.
- `ai/task-lifecycle.md` defines stable task IDs, task status transitions, claims, and handoffs.
- `ai/coordination-model.md` defines phase ownership, concurrency boundaries, and checkpoint cadence.
- `ai/session-state.md` carries only the current global coordination state.
- `ai/decisions/` holds durable decisions; `ai/definition-of-done.md` defines evidence-based completion.

| Tool | Reads | Kit file |
|---|---|---|
| Claude Code | `CLAUDE.md` | `CLAUDE.md` (imports AGENTS.md) |
| Gemini CLI | `GEMINI.md` | `GEMINI.md` (imports AGENTS.md) |
| Cursor | `.cursor/rules`, and AGENTS.md | `.cursor/rules/unity.mdc` |
| GitHub Copilot | `.github/copilot-instructions.md`, and AGENTS.md | same path |
| OpenAI Codex CLI and others | `AGENTS.md` | `AGENTS.md` |
| Web chat / no file support | nothing | paste `ai/prompts/start-session.md` + relevant tracker |

## Daily use
- **Start:** identify session username, read coordination model and session summary, then claim the phase/work package in its tracker.
- **Feature:** use `ai/prompts/new-feature.md` (plan first, then "go").
- **Unsure about a technical choice:** use `ai/prompts/spike.md`, then record an ADR.
- **Review:** use `ai/prompts/review.md` with a different provider for meaningful code or high-risk guidance changes.
- **End:** checkpoint the phase tracker; update the global summary only for a meaningful coordination transition; report checks and evidence.
- **Milestone:** run the 10-minute smoke test in `ai/definition-of-done.md` on a real phone.

## Limits
- Instructions are not enforcement. Keep branches, reviews, and repository permissions as the safety net.
- `ai/unity6-reference.md` is general guidance, not official API documentation. Verify claims against installed Editor/package versions.
- An AI without Editor access cannot compile. It must say "not compiled/tested" and provide precise human checks.
- Keep `AGENTS.md` concise (about 120 lines or fewer).

## Keeping it reusable
Improve the master repo (`unity-ai-kit`). Port general lessons back; keep game-specific facts, phase scope, and ADRs in consumer repositories.
