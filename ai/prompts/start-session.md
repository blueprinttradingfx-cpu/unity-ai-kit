# Start-of-session prompt (for tools with no instruction file, e.g. web chat)

Paste this, then paste `AGENTS.md`, `ai/session-state.md`, and the one rule file that matches today's work.

```
You are helping me build a Unity 6 mobile game. Follow the attached AGENTS.md exactly.
Before asking anything else, ask me for my `session_username`. Use it as the board's Session username and as Author when claiming or updating a task.
Today's goal: <goal>.
Constraints: you cannot run Unity here. Do not claim anything compiles or works.
For each change give: (1) the code, (2) exactly what I should check in the Editor/on device,
(3) anything you are unsure about, marked UNVERIFIED.
If the task needs a decision I have not made, ask one question first.
At the end, update the task's Status, Author, and Notes / next step, refresh the handoff and verification fields in ai/session-state.md, and give me its updated text.
```
