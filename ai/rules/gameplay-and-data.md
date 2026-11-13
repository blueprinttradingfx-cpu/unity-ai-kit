# Gameplay and data rules

Applies to: `Assets/**/Gameplay/**`, ScriptableObjects, JSON data, balance, saves.

**How to use this guide:** Data-driven configuration, plain-C# simulation, state machines, event messaging, and save patterns are recommended techniques. Apply them where they solve a real project need; a small game or an established architecture may reasonably use a simpler model. Preserve data integrity, validate untrusted input, and protect online economy/ranking decisions as security requirements.

## Data-driven
- Every tunable number (damage, cost, speed, timers, drop rates) comes from a ScriptableObject or data file. Code holds rules; data holds numbers.
- Each data type has a documented meaning for every field: unit (seconds, tiles, %), valid range, default.
- No orphan data: every entry is referenced by code or other data. Add a validation editor tool/test that fails on missing/duplicate IDs and out-of-range values.
- Stable string or integer IDs for content. Never use array index or asset name as an ID. Never reuse a retired ID.

## Logic vs presentation
- Simulation is plain C# with no `UnityEngine` dependency where possible. Views observe it.
- Explicit state machines: list states and legal transitions in code or a table; illegal transition = logged error.
- Time: fixed-step simulation tick (decide tick rate, record in an ADR) if gameplay must be deterministic or replayable; otherwise `deltaTime`.
- Randomness through one injectable seeded RNG, never `UnityEngine.Random` scattered through logic. This makes bugs reproducible.

## Events
- Cross-system communication via C# events / message bus, not direct references.
- Events carry data, not references to mutable internals.

## Saves and progress
- Versioned save format (`version` field) with explicit migration steps. Never change a field's meaning without bumping the version.
- Write atomically (temp file, then replace). Keep one backup.
- Separate: settings, progress, and in-run checkpoint. Decide which are cloud-synced vs local-only and record it.
- Do not trust saved or cloud data: validate on load.

## Economy / balance changes
- Any balance change states: what changed, expected effect, and which test or sim run checks it.
- Keep durable balance history in the relevant design or decision record; use `ai/session-state.md` only for current task status, ownership, and handoff.

## Security note (online features)
- Anything that affects rankings, currency or purchases is validated server-side or by rules, not trusted from the client. If there is no server, assume the client can lie and keep stakes low.
