# Code review prompt (use a different AI/provider than the one that wrote the code)

```
Review this diff in the context of the consuming project's AGENTS.md, project brief, relevant rule files, and ADRs. Do not assume a mobile game, a specific Unity version, render pipeline, architecture, or target platform unless the project says so.

Report only actionable problems, ranked by severity. For each finding include: file/line, impact, conditions to trigger it, and a concrete suggested fix. Distinguish confirmed defects from questions or risks that need verification.

Check relevant areas, including:
- correctness, lifecycle, event subscription/unsubscription, and destroyed-object handling
- allocations and hot-path performance against the project's targets and budgets
- data ownership, serialization, save compatibility, and migration behavior
- UI/state boundaries and project architecture
- Unity/API/package compatibility with the project's actual Editor and package versions
- tests and verification coverage for changed behavior
- Unity metadata, scenes, prefabs, ProjectSettings, packages, build/release, security, and secrets when touched

Do not suggest style-only changes or unrequested features. Do not infer a defect solely because the project differs from a generic convention. If the diff looks sound, say so and list any important checks that remain unverified.
```

Tip: a second provider can catch mistakes the implementation provider is blind to. Review the complete diff and relevant project context.
