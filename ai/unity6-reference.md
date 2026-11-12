# Unity 6 reference (for AI assistants whose training data may be older)

Written for Unity 6.x (6000.x), with Unity 6.3 LTS (6000.3) as the kit's current default target.
**Spot-check reviewed: 2026-11-13.** This is not a complete API compatibility audit.
Only the items explicitly linked in the final reference list were spot-checked. Several other rows are general migration reminders, not a claim that every API/package detail was verified against 6.3. Always verify against the exact Editor and package versions in `ProjectSettings/ProjectVersion.txt` and `Packages/manifest.json`.

Treat this as a checklist of common mistakes, not official API documentation. Confidence describes the stability of the general guidance, not compatibility with every package version.

## Renamed or obsolete — verify the installed version
| Old (common in training data) | Current Unity 6 guidance | Confidence |
|---|---|---|
| `FindObjectOfType<T>()` / `FindObjectsOfType<T>()` | Prefer explicit references/dependency injection; if a scene search is genuinely required, use the current `FindFirstObjectByType<T>()`, `FindAnyObjectByType<T>()`, or `FindObjectsByType<T>()` API. | High |
| `Rigidbody.velocity` / `Rigidbody.drag` / `angularDrag` | Unity 6 Rigidbody exposes `linearVelocity`, `linearDamping`, and `angularDamping`. Do not set velocity every physics step as a substitute for forces. | High |
| `Rigidbody2D.velocity` / drag naming | Check the installed Unity 6 2D Physics API and use the matching 2D property names; do not copy 3D Rigidbody examples into 2D code. | Medium |
| Legacy `Input.GetKey*`, `Input.GetAxis`, `Input.touches` | Prefer the Input System package for new projects when the project has it installed and configured. Existing projects may intentionally use the legacy input backend; do not switch project settings/packages without approval. | High |
| `Application.LoadLevel`, `WWW` | Use `SceneManager.LoadScene*` and `UnityWebRequest` for current Unity code. | High |
| Built-in render pipeline for new projects | URP is a common mobile choice, not a mandatory upgrade for an existing project. | High |
| Custom URP passes using older `Execute(...)` patterns | Check the installed URP package's renderer-feature API; RenderGraph integration is version-sensitive. | Medium |
| Legacy uGUI `Text` | Prefer TextMeshPro for uGUI or UI Toolkit `Label`; do not migrate an existing UI stack without a project decision. | High |
| Coroutine-only async flow | Unity 6 provides `Awaitable`; coroutines remain supported. `Awaitable` instances are pooled and must not be awaited multiple times. | High |
| Entities pre-1.0 (`ComponentSystem`, `GameObjectEntity`) | Use APIs from the installed Entities package; 1.x commonly uses `ISystem`, `IComponentData`, and `ComponentLookup<T>`. | High |

## Defaults and behaviours that bite
- **IMGUI (`OnGUI`)**: primarily editor tooling; avoid it for new runtime player UI unless there is a deliberate reason.
- **UI Toolkit** is supported for runtime UI in Unity 6 (`UXML`/`USS`, `UIDocument`). **uGUI** is also supported. Choose and record an ADR rather than mixing UI systems casually.
- **Addressables**: load/instantiate/release behavior depends on the installed Addressables package. Check the package docs and handle status/exceptions; always release handles according to the API contract. Do not assume a failed load always returns null. (Medium.)
- **Domain reload disabled**: static fields and static event subscriptions are not automatically reset on entering Play Mode. Reset static runtime state deliberately; editor-only initialization can use `InitializeOnEnterPlayMode` where appropriate.
- **Fake null**: destroyed `UnityEngine.Object` instances compare equal to null, but C# null-conditional/coalescing operators do not perform Unity's overloaded null check.
- **Serialization**: Unity does not serialize ordinary properties, dictionaries, interfaces, or `readonly` fields by default. Use supported serialization patterns such as `[SerializeField]` and `[SerializeReference]` deliberately.
- **Script execution**: `Awake` → `OnEnable` → `Start` is the usual per-object sequence. Do not rely on cross-object `Awake` ordering; use an explicit initializer or composition root.
- **Time**: `Time.timeScale = 0` stops `FixedUpdate` and scaled waits; UI animation that must continue should use unscaled time.
- **Android**: IL2CPP + ARM64 and App Bundle are common Play Store release choices. Minimum/target API levels and store policies change; verify current Unity and Google Play requirements for each release.
- **Code stripping (IL2CPP)** can remove types only accessed through reflection/serialization. Preserve required types with supported mechanisms such as `[Preserve]` or `link.xml`, then test the actual player build.
- **JsonUtility** is field-oriented and limited compared with general-purpose JSON libraries. For external schemas, snake_case payloads, dictionaries, or top-level arrays, use explicit DTO mapping or an approved JSON library.
- **Burst/Jobs/DOTS**: use when requirements and profiling justify them. They are architectural choices, not default upgrades for an OOP project.

## Packages commonly used (verify installed versions)
Input System (`com.unity.inputsystem`), URP (`com.unity.render-pipelines.universal`), Addressables, Cinemachine 3.x (API differs from 2.x), Unity Test Framework, TextMeshPro, Localization, Mobile Notifications, and Unity Services are optional project dependencies. Do not add or upgrade them without approval.

## Verification procedure
1. Read `ProjectSettings/ProjectVersion.txt` and relevant package versions from `Packages/manifest.json` / `packages-lock.json`.
2. Check the official manual or Scripting API for that exact Editor/package version.
3. Prefer a tiny compile/test experiment in the actual project before applying a broad migration.
4. If docs or editor access are unavailable, label the claim `UNVERIFIED` and state the exact human check needed.
5. Update the review date only after a dated review; list the APIs/packages actually checked. A spot check is not a blanket certification.

## Official Unity references checked for this spot review

- [Rigidbody.linearVelocity — Unity 6.3 (6000.3) Scripting API](https://docs.unity.com/en-us/engine/6000.3/script-reference/unityengine/rigidbody/linearvelocity)
- [Rigidbody.linearDamping — Unity 6.3 (6000.3) Scripting API](https://docs.unity.com/en-us/engine/6000.3/script-reference/unityengine/rigidbody/lineardamping)
- [Rigidbody2D — Unity 6.3 (6000.3) Scripting API](https://docs.unity.com/en-us/engine/6000.3/script-reference/unityengine/rigidbody2d)
- [EnterPlayModeOptions — Unity 6.3 (6000.3) Scripting API](https://docs.unity.com/en-us/engine/6000.3/script-reference/unityeditor/enterplaymodeoptions)
- [InitializeOnEnterPlayModeAttribute — Unity 6.3 (6000.3) Scripting API](https://docs.unity.com/en-us/engine/6000.3/script-reference/unityeditor/initializeonenterplaymodeattribute)
- [RuntimeInitializeOnLoadMethodAttribute — Unity 6.3 (6000.3) Scripting API](https://docs.unity.com/en-us/engine/6000.3/script-reference/unityengine/runtimeinitializeonloadmethodattribute)
- [Domain reload behavior — Unity 6.3 (6000.3) Manual](https://docs.unity.com/en-us/engine/6000.3/manual/programming-environment/code-reload-serialization/code-reloading-editor/domain-reloading)
- [Event function execution order — Unity 6.3 (6000.3) Manual](https://docs.unity.com/en-us/engine/6000.3/manual/scripting/managing-update-order/execution-order)
- [Awaitable — Unity 6.0 (6000.0) Scripting API](https://docs.unity.com/en-us/engine/6000.0/script-reference/unityengine/awaitable)

The Awaitable API link above is the 6000.0 reference, not a 6000.3-specific API page. Its pooled-instance behavior is a known important constraint, but this spot review does not certify every Awaitable API detail for 6.3. Verify against the installed Editor's documentation before relying on version-sensitive behavior.

This list is intentionally limited to the claims spot-checked for this change. Other entries in the tables are prompts to verify against the project's exact Editor and package versions, not a blanket compatibility certification.
