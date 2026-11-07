# Unity 6 reference (for AI assistants whose training data may be older)

Written against Unity 6.x (6000.x), target 6.3 LTS. **Last reviewed: <date>.**
Treat this as a checklist of *common mistakes*, not as official documentation. Confidence is marked.
When it matters, check the official Unity manual / package docs for the exact installed version
(`ProjectSettings/ProjectVersion.txt`, `Packages/manifest.json`). If you cannot check, say "unverified".

## Renamed or obsolete — do not generate the old form
| Old (common in training data) | Use now | Confidence |
|---|---|---|
| `FindObjectOfType<T>()` / `FindObjectsOfType<T>()` | `FindFirstObjectByType<T>()` / `FindAnyObjectByType<T>()` / `FindObjectsByType<T>(FindObjectsSortMode.None)` | High |
| `Rigidbody.velocity` / `angularVelocity` | `Rigidbody.linearVelocity` / `angularVelocity` (2D: `Rigidbody2D.linearVelocity`) | High |
| `Rigidbody.drag` / `angularDrag` | `linearDamping` / `angularDamping` | High |
| Legacy `Input.GetKey*`, `Input.GetAxis`, `Input.touches` | Input System package (`InputAction`, `Touchscreen.current`, `EnhancedTouch`) | High (project must set Active Input Handling) |
| `Application.LoadLevel`, `WWW` | `SceneManager.LoadScene*`, `UnityWebRequest` | High |
| Built-in render pipeline for new projects | URP (usual for mobile) | High |
| Custom URP passes using `Execute(...)` / `ScriptableRenderContext` directly | RenderGraph API (`RecordRenderGraph`) | Medium — check URP version docs |
| `Text` (legacy uGUI) | TextMeshPro (uGUI) or UI Toolkit `Label` | High |
| Coroutine-only async flow | `Awaitable` (`await Awaitable.NextFrameAsync()`, `WaitForSecondsAsync`) is available; coroutines still fine | High |
| Entities pre-1.0 (`ComponentSystem`, `GameObjectEntity`) | Entities 1.x (`ISystem`, `IComponentData`, `ComponentLookup<T>`) | High |

## Defaults and behaviours that bite
- **IMGUI (`OnGUI`)**: editor tooling. Avoid for runtime player UI in new work; allocates and is hard to skin/accessibility. See `ai/rules/ui.md`.
- **UI Toolkit** is a supported runtime UI system in Unity 6 (UXML/USS, `UIDocument`). **uGUI** is still supported. Choose and record an ADR.
- **Addressables**: failed loads may throw rather than return null in newer versions — use try/catch or check `handle.Status`; always `Release` handles. (Medium — check package version.)
- **Domain reload / Enter Play Mode options**: with domain reload disabled, **static fields keep values between plays**. Reset statics explicitly (`[RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.SubsystemRegistration)]`).
- **Fake null**: destroyed `UnityEngine.Object`s compare equal to null but `?.`/`??` bypass that check.
- **Serialization**: Unity does not serialize properties, dictionaries, interfaces, or `readonly` fields by default; `[SerializeReference]` for polymorphic managed refs; `[SerializeField]` on private fields.
- **Script execution**: `Awake` → `OnEnable` → `Start`. Do not rely on cross-object `Awake` order; use an explicit initializer.
- **Time**: `Time.timeScale = 0` stops `FixedUpdate` and scaled coroutines; UI animation needs unscaled time.
- **Android**: IL2CPP + ARM64 for release; App Bundle for Play Store. Minimum and target API levels are raised over time by Unity and Google Play — check both current docs before a release build. (High that they change; exact numbers: verify.)
- **Code stripping (IL2CPP)** can remove types used only via reflection/JSON: use `[Preserve]` or `link.xml`.
- **JsonUtility** binds by exact field name, no dictionaries, no top-level arrays. For snake_case keys or richer JSON use a DTO mapping layer or a JSON library with naming policies (add as an ADR).
- **Burst/Jobs/DOTS**: use only when profiling shows a CPU bottleneck. Do not introduce DOTS into an OOP project casually; it is an architectural fork.

## Packages commonly used (verify installed versions)
- Input System (`com.unity.inputsystem`), URP (`com.unity.render-pipelines.universal`), Addressables, Cinemachine 3.x (API differs from 2.x), Unity Test Framework, TextMeshPro (built into uGUI package in Unity 6), Localization, Mobile Notifications, Unity Services (opt-in).

## How to verify an API without an editor
1. Ask the human for the package version and the exact compile error text.
2. Check the official manual/scripting API for that version.
3. Prefer a tiny test script over a large untested change.
4. If you are guessing, label it: `// UNVERIFIED API: check against 6.x docs`.
