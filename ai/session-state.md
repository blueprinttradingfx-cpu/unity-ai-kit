# Project / Work Board

This board is shared by several agents working at the same time. Read it at the start of every session and update it before you finish. It shows only **Ready** and **In Progress** tasks. Other tasks are in these lists:
- `ai/blocked-tasks.md`: Blocked tasks, and what each one waits on.
- `ai/done-tasks.md`: finished work (built, merged, or accepted).
- `ai/backlog-tasks.md`: not started and not yet Ready.

When a task's status changes, move its row to the list for its new status. Keep this file under ~60 lines. Details live in the tracker log or the project's decision records.

**Rules for every agent, every session:**
1. Each session is one agent. At the start, ask the user for your `session_username`. Do not reuse a name you saw in this file.
2. To start a Ready task, set its Author to your `session_username` and Status to `In Progress`. You own it until it is Done or you hand it back.
3. Never start a task whose Author is another name, or `owner`, unless the user tells you to take it over.
4. When you finish or stop, update Status, Notes / next step, and the Handoff section, and move the row if its status changed. Leave your name in Author only while you still own the task.

**Session username for the session that last wrote this file:** `git_copilot_blue` (a record, not your name, unless the user tells you it is).

## Board

Author = the agent that owns the task (a `session_username`), `owner` = the human owner.

| Status | Task | Author | Notes / next step |
|---|---|---|---|
| — | No Ready or In Progress tasks. | — | Add a row when work is ready to start. |

## Project context
- **Branch / build:**
- **Last known good build:** <date, commit>

## Handoff
- **In progress (exact stopping point):**
- **Next concrete step:**
- **Known broken:**
- **Verified (ran it):**
- **Not verified (human must check on device/editor):**
- **Owner decisions waiting:** see `ai/blocked-tasks.md`.
- **Bug / regression watch:**
