# <GAME NAME> — Instructions for AI coding assistants

Unity 6.3 LTS · C# · Target: Android first (IL2CPP, ARM64) · <add/remove>
This file is read by any AI tool (Claude, Codex, Gemini, Cursor, Copilot, local models).
Keep it short. Detail lives in `ai/`. Fill in the `<...>` fields once per project.

**Apply guidance by category.** Read `ai/kit-principles.md`: safety/integrity guardrails are distinct from recommended engineering defaults and consumer-owned decisions. This file is a starting template, not a universal architecture contract. Adapt conventions to the actual project and record consequential decisions.

## Start every session
1. Ask the user for your `session_username`. Read `ai/coordination-model.md`, then `ai/session-state.md`. Do not reuse an agent name already recorded there.
2. Identify the phase or work package matching the user's goal. Read its phase tracker and claim ownership there before editing. If no matching phase/task exists, create a stable-ID entry and claim it. Never take another agent's owned work without explicit user approval.
3. Read `ai/project-brief.md` and relevant ADRs in `ai/decisions/`. Before touching a topic, read its rule file (table below).
4. Update the phase tracker at meaningful checkpoints. Update `ai/session-state.md` only when phase ownership/status, blockers, priority, milestone, or handoff changes. Follow `ai/definition-of-done.md` before finishing.

## Starter rules — classify and adapt
The following mix safety guardrails with engineering defaults. Do not treat every style or architecture preference as a universal hard rule; apply `ai/kit-principles.md` and consumer decisions.
1. **Preserve Unity asset integrity.** Do not create, edit, move or delete `.meta` files by hand. Asset moves/renames happen in the Unity Editor (or move the `.meta` with the asset).
2. **Preserve serialized Unity data.** Do not hand-edit scene, prefab or `.asset` YAML unless asked. Prefer an editor script, or give numbered Editor steps for the human.
3. **Avoid generated data.** Do not touch `Library/`, `Temp/`, `Logs/`, `obj/`, `UserSettings/`, `Builds/`.
4. **Respect consumer configuration.** Do not change Unity version, render pipeline, or packages unless asked. Say so if a task needs one.
5. **Performance default:** avoid allocations in hot paths (`Update`, `FixedUpdate`, `LateUpdate`, per-frame UI, physics callbacks), unless profiling and project constraints support another choice.
6. **Data ownership default:** keep gameplay numbers in project-owned data where practical; follow the consumer's established model.
7. **Architecture default:** UI commonly displays state and sends commands/events; adapt to the project's actual UI/state architecture.
8. **Verify Unity APIs.** Check `ai/unity6-reference.md`; if still unsure, say "unverified" and name how to check.
9. **Evidence guardrail:** never claim code compiles, passes tests or works unless you ran it. Say exactly what was and was not verified.
10. **Secret guardrail:** no keys, keystores, passwords, or service-account files in the repo, prompts or logs.
11. **Keep diffs reviewable.** Prefer one concern per change. Ask before a broad refactor or public API change when scope/authorization is unclear.
12. **Record consequential decisions** in `ai/decisions/` (see template). Do not silently reverse an earlier decision; flag the conflict.

## Rule files — read the one that matches the work
| When you touch… | Read |
|---|---|
| Any C# | `ai/rules/code-style.md` |
| `Assets/**/UI/**`, HUD, menus, uGUI / UI Toolkit | `ai/rules/ui.md` |
| `Assets/**/Gameplay/**`, balance, data files, ScriptableObjects | `ai/rules/gameplay-and-data.md` |
| Frame time, memory, battery, Android/mobile concerns, builds | `ai/rules/performance-mobile.md` |
| Tests, bug fixes, "does it work?" | `ai/rules/testing.md` |
| Git, deleting files, shell commands, dependencies | `ai/rules/safety-and-git.md` |
| GitHub Actions, CI/CD, branch protection, release checks | `ai/github-workflows.md` |
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
