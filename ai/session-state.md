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

**Session username for the session that last wrote this file:** `gpt`

## Board

Author = the agent that owns the task, `owner` = the human owner. Every task uses a stable ID (for example `KIT-001`) so handoffs and review comments refer to the same work.

| Status | Task ID | Task | Author | Notes / next step |
|---|---|---|---|---|
| In Progress | KIT-001 | Harden the reusable agent workflow and verification safeguards | `gpt` | Audit the existing kit; add a clear task lifecycle, safer claim/handoff rules, and evidence-based completion checks. Keep changes documentation-only and backward-compatible. |

## Project context
- **Branch / build:** `gpt/harden-agent-workflow` / no Unity project in this reusable guidance repository.
- **Last known good build:** Not applicable; documentation-only kit.

## Handoff
- **In progress (exact stopping point):** Audited AGENTS.md, README.md, session board, task status lists, safety/testing rules, definition of done, Unity reference, and session prompt. Branch created from main commit `bb253bf6b520827b02872bbc57ab0149084b4354`.
- **Next concrete step:** Add the task lifecycle guidance and align startup, board, README, and completion criteria.
- **Known broken:** The current board can be empty but has no explicit user-goal-to-task creation path; task rows lack stable IDs; the Unity reference review date is still a placeholder.
- **Verified (ran it):** Read repository files through GitHub; confirmed main branch commit and created working branch.
- **Not verified (human must check on device/editor):** Not applicable; no Unity project or runtime code is included.
- **Owner decisions waiting:** None for this documentation-only scope.
- **Bug / regression watch:** Keep the master kit project-neutral; do not change game-project repositories.
