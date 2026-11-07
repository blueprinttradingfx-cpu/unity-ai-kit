# Code review prompt (use a different AI/provider than the one that wrote the code)

```
Review this diff for a Unity 6 mobile game. Follow AGENTS.md and ai/rules/*.md.
Report only real problems, ranked by severity, each with: file/line, what breaks, how to trigger it, suggested fix.
Check specifically:
- per-frame allocations and hot-path cost
- event subscribe/unsubscribe pairs, destroyed-object ("fake null") misuse
- hard-coded gameplay numbers
- UI owning or mutating game state
- obsolete Unity APIs (see ai/unity6-reference.md)
- save-format changes without version bump/migration
- anything that touches .meta, scenes, prefabs, ProjectSettings, or packages
- missing tests for logic changes
Do not suggest style-only changes or new features. If the diff looks fine, say so.
```

Tip: reviewing with a second provider catches mistakes the first one is blind to.
