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

Author = the agent that owns the task, `owner` = the human owner. Every task uses a stable ID (for example `KIT-001`) prefixed in its Task text; preserve it when moving the task between lists.

| Status | Task | Author | Notes / next step |
|---|---|---|---|
| In Progress | KIT-001 — Harden the reusable agent workflow and verification safeguards | `gpt` | Implemented task lifecycle, safe claim/handoff guidance, and evidence-based completion checks. Acceptance: board workflow is explicit; task IDs persist across lists; verification and independent review are reported honestly. Awaiting independent review. |

## Project context
- **Branch / build:** `gpt/harden-agent-workflow` / no Unity project in this reusable guidance repository.
- **Last known good build:** Not applicable; documentation-only kit.

## Handoff
- **In progress (exact stopping point):** Documentation changes are implemented on `gpt/harden-agent-workflow`. Files changed: `AGENTS.md`, `README.md`, `ai/session-state.md`, `ai/definition-of-done.md`, and new `ai/task-lifecycle.md`.
- **Next concrete step:** Obtain an independent review of PR #1's full diff, resolve findings, then mark the PR ready for owner review.
- **Known broken:** `ai/unity6-reference.md` still has an unfilled review-date placeholder; it is explicitly described as unverified in README and should be reviewed against official docs before being treated as current API guidance.
- **Verified (ran it):** Confirmed the branch is based on current main with no behind commits; inspected the full five-file compare; checked the task workflow references and status-list paths; confirmed the changes are documentation-only. No Unity compilation is applicable.
- **Not verified (human must check on device/editor):** Independent second-provider review is pending. No Unity Editor/device checks apply to this kit-only change.
- **Owner decisions waiting:** None for the current scope; owner review/approval of the eventual PR is required.
- **Bug / regression watch:** Keep the master kit project-neutral; do not change game-project repositories.
