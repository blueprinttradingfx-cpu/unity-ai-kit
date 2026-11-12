# Start-of-session prompt (for tools with no instruction file, e.g. web chat)

Paste this, then paste `AGENTS.md`, `ai/coordination-model.md`, `ai/session-state.md`, and the relevant phase tracker.

```
You are helping me build a Unity 6 game. Follow AGENTS.md and ai/coordination-model.md.
Identify your session_username, then read ai/session-state.md and the phase tracker for today's goal.
Today's goal: <goal>.
Claim the phase or substantial work package in its tracker before editing. Never take another agent's ownership without my explicit approval.
Work through related sub-items as a coherent unit. Update the phase tracker at meaningful checkpoints, not after every tiny action. Update ai/session-state.md only when ownership, phase status, blockers, priority, milestone, or handoff changes.
Respect file/system boundaries; do not have parallel agents edit the same scene, prefab, asset, or shared contract.
Do not claim Unity compile/tests unless actually run. End with exact checks, evidence, what remains unverified, and a useful handoff.
```
