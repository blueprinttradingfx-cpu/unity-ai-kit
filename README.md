# Unity AI Kit — provider-neutral starter for new Unity games

Drop-in guidance files so any AI coding assistant (Claude, Codex, Gemini, Cursor, Copilot, local models, web chat) works the same way on your Unity projects. Plain Markdown, no scripts, no hooks, nothing to install.

Inspired by the ideas in `donchitos/claude-code-game-studios` (path-scoped rules, decision records, definition of done, session state), but without its Claude-only machinery (49 agents, 74 skills, bash hooks), and with the Unity reference rewritten and corrected.

## Set up a new project (10 minutes)
1. Copy everything except `README.md` into the **root of your Unity project repo** (next to `Assets/`).
2. Rename `examples/Unity.gitignore` → `.gitignore` and `examples/Unity.gitattributes` → `.gitattributes` (skip if you already have good ones). In Unity: Editor settings → Asset Serialization = Force Text, Version Control = Visible Meta Files.
3. Edit `AGENTS.md`: game name, platform, folder layout, and the **Commands** section (Unity.exe path). This lets AIs that can run commands verify their work.
4. Fill `ai/project-brief.md` (pillars, device, constraints). Short is fine.
5. Delete the pointer files for tools you do not use (see table). Optional: `examples/claude-settings.json` → `.claude/settings.json`.
6. First commit: "Add AI guidance kit".

## How it works
- `AGENTS.md` is the single source of truth. It stays short: hard rules, a routing table, commands, working style.
- Each tool gets a 1–3 line pointer to it, so you maintain one file.
- Detail is in `ai/rules/*.md`, read only when the work matches (saves context, works in any tool).
- `ai/session-state.md` carries "where we stopped" between sessions and between **different AIs**.
- `ai/decisions/` holds one-page decisions so a new AI doesn't re-open or contradict them.
- `ai/definition-of-done.md` is the checklist that stops "should work" from counting as "works".

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
- **Start:** tell the AI "follow AGENTS.md; read ai/session-state.md".
- **Feature:** use `ai/prompts/new-feature.md` (plan first, then "go").
- **Unsure about a technical choice:** `ai/prompts/spike.md`, then record an ADR.
- **Review:** give the diff to a *different* provider with `ai/prompts/review.md`.
- **End:** ask the AI to rewrite `ai/session-state.md`; commit it.
- **Milestone:** run the 10-minute smoke test at the bottom of `ai/definition-of-done.md` on a real phone.

## Limits (be aware)
- These are instructions, not enforcement. Tools without permission controls can still ignore them; keep the git safety net (commit before AI sessions, work on branches).
- `ai/unity6-reference.md` is a list of common mistakes written from general knowledge, not official docs. Mark "last reviewed" and re-check it when you upgrade Unity. Entries marked Medium need verifying against your installed package versions.
- An AI without editor access cannot compile. The kit makes it say so and hand you a precise check list.
- Keep `AGENTS.md` under ~120 lines. Long instruction files get skimmed and partially ignored.

## Keeping it reusable
Improve the kit in one master repo (`unity-ai-kit`); copy into new projects. When a lesson from a project is general (a Unity gotcha, a better rule), port it back to the master. Project-specific facts stay in that project's `ai/project-brief.md` and ADRs.
