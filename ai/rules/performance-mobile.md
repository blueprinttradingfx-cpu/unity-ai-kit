# Performance and mobile rules

Applies to: anything about frame time, memory, battery, heat, build size, Android.

**How to use this guide:** The budgets and techniques are starting points, not universal pass/fail thresholds. Set targets from the consumer project's supported devices, genre, visual goals, platform requirements, and profiling evidence. Android-specific advice applies only when Android is a target; adapt equivalent checks for other platforms. Measure before treating an optimization as necessary.

## Budgets (set per project; defaults to start from)
- Frame rate target: 60 fps (or 30 for heavy games). Set `Application.targetFrameRate` explicitly and decide VSync; mobile defaults surprise you.
- Per-frame GC allocation in gameplay: **0 bytes** after warm-up.
- Frame time budget: 16.6 ms (60 fps) or 33.3 ms (30 fps) on the **lowest-end supported phone**, not the dev phone.
- Memory: set a ceiling on the lowest device; watch texture and audio memory first.
- Build size: set a limit (Play Store has size limits and users drop off on big downloads).

## Rules
- Measure first: Unity Profiler (deep profile sparingly), Memory Profiler, Frame Debugger, and Android GPU/thermal tools on a real device. Do not optimize from guesses.
- Profile on a **development build on device**, not in the Editor.
- Avoid in hot paths: LINQ, `string` concatenation/formatting, boxing, closures capturing locals, `foreach` over non-struct enumerators, `GetComponent`, `Camera.main` repeated (cache), `Find*`.
- Pool anything spawned often (enemies, projectiles, VFX, UI items). Pre-warm pools during load.
- Physics: layers + collision matrix, simple colliders, `NonAlloc` queries, avoid per-frame raycasts you can batch.
- Rendering (URP is the usual mobile choice): few materials, SRP Batcher, GPU instancing where it fits, atlas sprites, limit transparency overdraw, cheap shaders, bake lighting, avoid real-time shadows unless budgeted.
- Textures: ASTC compression on Android, sensible max sizes, mipmaps for 3D, no read/write unless needed.
- Audio: compress, stream long music, limit simultaneous voices.
- Loading: load assets asynchronously (Addressables or async scene load); show progress; handle load failure (Unity 6 Addressables may throw instead of returning null).
- Heat/battery: test 20+ minute sessions; lower frame rate in menus; no busy loops.

## Android specifics
- Scripting backend IL2CPP, ARM64, App Bundle (AAB) for Play Store. Strip engine code and keep `link.xml` for reflection-used types.
- Check minimum API level and target API level requirements in current Unity and Google Play docs before release; both change.
- Handle: app pause/resume, back button, screen rotation (if allowed), low-memory callbacks, no network, permission denial.
- Keystore and passwords stay out of the repo (see `safety-and-git.md`).
- Test matrix: lowest-end phone, a mid phone, a tall-screen phone, and one with a notch.

## Reporting a performance change
State: baseline number, new number, device, build type, and how it was measured. "Feels faster" does not count.
