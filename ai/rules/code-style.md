# Code style (all C#)

Applies to: every `.cs` file.

**How to use this guide:** These are reusable C# and Unity starting conventions, not a required architecture. Follow the consuming project's existing style, assembly layout, dependency model, and ADRs. Adopt the examples that improve consistency; adapt or omit those that conflict with the project's constraints. Language/API correctness and safe handling of serialized data still matter regardless of style.

## Structure
- One assembly definition per module (`Core`, `Gameplay`, `UI`, `Data`, `Tests`). Dependencies point one way: UI → Gameplay → Core. Gameplay never references UI.
- Namespace = folder path under `Scripts/` (e.g. `Game.Gameplay.Combat`).
- Plain C# classes for logic; `MonoBehaviour` is a thin adapter (input, lifecycle, view). Logic that does not need the engine must be testable without a scene.
- Prefer composition and small interfaces over inheritance chains.
- No static singletons for game state. Pass dependencies in (constructor, `Initialize(...)`, or a small service locator at the composition root only).

## Naming and layout
- `PascalCase` types, methods, properties, events. `camelCase` locals/params. Private fields `_camelCase`. Constants `PascalCase`.
- Files named after the primary type. One public type per file.
- Interfaces start with `I`. Events are verbs in past tense (`WaveCompleted`).

## Unity specifics
- Serialize with `[SerializeField] private`, not `public` fields.
- Renaming a serialized field loses data: add `[FormerlySerializedAs("oldName")]`.
- Cache `GetComponent` results; no `Find*`/`GetComponent` in per-frame code.
- Use `FindFirstObjectByType` / `FindAnyObjectByType` / `FindObjectsByType` (old `FindObjectOfType*` are obsolete). Avoid scene searches in gameplay code anyway.
- Unity objects can be "fake null": use `if (obj)` / `obj == null` on `UnityEngine.Object`, never `?.` / `??` on them.
- Subscribe in `OnEnable`, unsubscribe in `OnDisable`. Every `+=` needs a matching `-=`.
- Prefer `Awaitable` or coroutines for async game flow; do not leave fire-and-forget `async void`. Cancel on destroy.
- `Time.deltaTime` for variable-step, `Time.fixedDeltaTime` only inside `FixedUpdate`. Never assume frame rate.
- Use `Input System` package types, not legacy `Input.*`.
- Strings that players see go through localization (see `ui.md`). Keys/IDs use constants or enums, not scattered literals.

## Errors and logging
- Fail loudly in development: `Debug.Assert` / throw for programmer errors; handle expected runtime failures (missing save, network) explicitly.
- Logs: one prefix per system, no logging inside per-frame code paths in release builds (wrap with `[Conditional("UNITY_EDITOR")]` or a debug flag).

## Comments
- Comment *why*, not what. Link the design note or ADR for non-obvious decisions (`// ADR-0004`).
