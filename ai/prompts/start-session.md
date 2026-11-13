# Start-of-session prompt (for tools with no instruction file, e.g. web chat)

Use the smallest useful context for the task. Paste `AGENTS.md` and the relevant rule/project context. Add coordination files only when the work is shared, substantial, or spans sessions.

```
You are helping with a Unity project. Follow the consumer's AGENTS.md and project-owned decisions; do not assume a specific Unity version, genre, platform, architecture, or team size.

Today's goal: <goal>.

For a small, self-contained task, work directly from the request and relevant project instructions. Do not create a task ID, phase tracker, or session-state entry unless it adds real value.

For substantial or shared work, read the coordination model and current shared status. Find or create the appropriate tracked phase/work package, claim ownership in its source of truth before parallel editing, and respect file/system boundaries. Never take another agent's ownership without explicit human approval. If an issue tracker is already the source of truth, do not duplicate it in Markdown.

Group related sub-items and update the owning tracker at meaningful checkpoints. Update the global session summary only when shared ownership/status, blockers, priority, milestone, or handoff changes—not after every edit or tiny action.

Do not claim Unity compile/tests/builds or runtime behavior unless actually verified. End with exact checks and evidence, what remains unverified, and a proportionate handoff when one is useful.
```
