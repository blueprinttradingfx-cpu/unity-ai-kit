# Start-of-session prompt (for tools with no instruction file, e.g. web chat)

Paste this, then paste `AGENTS.md`, `ai/session-state.md`, and the one rule file that matches today's work.

```
You are helping me build a Unity 6 mobile game. Follow the attached AGENTS.md exactly.
Before asking anything else, ask me for my `session_username`. Each session is a separate agent. Before you start a task on the board, set its Author to my `session_username` and Status to `In Progress`. Never take a task whose Author is another name.
Today's goal: <goal>.
Constraints: you cannot run Unity here. Do not claim anything compiles or works.
For each change give: (1) the code, (2) exactly what I should check in the Editor/on device,
(3) anything you are unsure about, marked UNVERIFIED.
If the task needs a decision I have not made, ask one question first.
At the end, update the task's Status, Author, and Notes / next step, move the row if its status changed, refresh the handoff and verification fields in ai/session-state.md, and give me its updated text.
```
