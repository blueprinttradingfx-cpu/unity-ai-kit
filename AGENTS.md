# <GAME NAME> — Instructions for AI coding assistants

Unity 6.3 LTS · C# · Target: Android first (IL2CPP, ARM64) · <add/remove>
This file is read by any AI tool (Claude, Codex, Gemini, Cursor, Copilot, local models).
Keep it short. Detail lives in `ai/`. Fill in the `<...>` fields once per project.

## Start every session
1. Ask the user for your `session_username`. Read `ai/task-lifecycle.md`, then `ai/session-state.md`. Do not reuse an agent name already recorded there.
2. Find a Ready task matching the user's goal. Claim it by setting Author to your username and Status to `In Progress` before editing. Never take another agent's task. If the user gave a clear goal but no matching task exists, create a stable-ID task on the board and claim it; if the goal is unclear, ask before inventing work.
3. Read `ai/project-brief.md` and the relevant ADRs in `ai/decisions/`. Before touching a topic, read its rule file (table below).
4. Work on a branch, keep the diff focused, and re-check the latest board before changing ownership or handoff. Follow `ai/definition-of-done.md` before finishing; move completed/blocked/backlog tasks to the matching list and update the handoff.

## Hard rules (never break without asking)
1. **Never create, edit, move or delete `.meta` files by hand.** Asset moves/renames happen in the Unity Editor (or move the `.meta` with the asset).
2. **Do not hand-edit scene, prefab or `.asset` YAML** unless asked. Prefer an editor script, or give numbered Editor steps for the human.
3. **Do not touch** `Library/`, `Temp/`, `Logs/`, `obj/`, `UserSettings/`, `Builds/`.
4. **No Unity version, render pipeline, or package changes** unless asked. Say so if a task needs one.
5. **No allocations in hot paths** (`Update`, `FixedUpdate`, `LateUpdate`, per-frame UI, physics callbacks).
6. **Gameplay numbers live in data** (ScriptableObject / JSON), never as magic numbers in code.
7. **UI displays state; it never owns or mutates it.** UI sends commands/events.
8. **Do not guess Unity APIs from memory.** Unity 6 changed many. Check `ai/unity6-reference.md`; if still unsure, say "unverified" and name how to check.
9. **Never claim code compiles, passes tests or works unless you ran it.** Say exactly what was and was not verified.
10. **No secrets** (keys, keystores, passwords, service-account files) in the repo, prompts or logs.
11. **Small diffs.** One concern per change. Ask before a refactor touching more than ~5 files or any public API.
12. **Record decisions** in `ai/decisions/` (see template). Do not silently reverse an earlier decision; flag the conflict.

## Rule files — read the one that matches the work
| When you touch… | Read |
|---|---|
| Any C# | `ai/rules/code-style.md` |
| `Assets/**/UI/**`, HUD, menus, uGUI / UI Toolkit | `ai/rules/ui.md` |
| `Assets/**/Gameplay/**`, balance, data files, ScriptableObjects | `ai/rules/gameplay-and-data.md` |
| Frame time, memory, battery, Android/mobile concerns, builds | `ai/rules/performance-mobile.md` |
| Tests, bug fixes, "does it work?" | `ai/rules/testing.md` |
| Git, deleting files, shell commands, dependencies | `ai/rules/safety-and-git.md` |
| Any Unity API, package, or setting | `ai/unity6-reference.md` |

## Project layout (edit to match)
```
Assets/_Project/
  Scripts/<Module>/   one assembly definition (.asmdef) per module
  Data/               ScriptableObjects, JSON
  Art/  Audio/  Prefabs/  Scenes/  UI/
ai/                   AI guidance (this kit)
Tests/                EditMode + PlayMode
```

## Commands (fill in, so the AI can verify instead of guessing)
- Unity editor path: `<C:\Program Files\Unity\Hub\Editor\6000.x.x\Editor\Unity.exe>`
- EditMode tests: `Unity.exe -batchmode -nographics -projectPath . -runTests -testPlatform EditMode -testResults ai/out/editmode.xml`
- PlayMode tests: same with `-testPlatform PlayMode`
- Compile check: `Unity.exe -batchmode -nographics -quit -projectPath . -logFile ai/out/compile.log`
- Build (Android): `<Unity.exe ... -executeMethod Build.Android>` (define once, then reuse)

If the AI cannot run Unity (cloud chat, no editor), it must say "not compiled/tested" and list what the human should check.

## How to work with me
- Short answers. Lead with the result, then the one thing I must decide or check.
- If the request is ambiguous and a wrong guess is expensive, ask one question; otherwise pick the sensible default and state it.
- When you change UI or anything visible, tell me what to look at on device (I will send screenshots).
- Do not add features, abstractions, or "nice to have" cleanup I did not ask for.
