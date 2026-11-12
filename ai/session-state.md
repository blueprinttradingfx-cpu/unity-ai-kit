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
| In Progress | KIT-001 — Harden the reusable agent workflow and verification safeguards | `gpt` | Implemented task lifecycle, safe claim/handoff guidance, and evidence-based completion checks. Awaiting independent review. |
| In Progress | KIT-002 — Add Unity GitHub Actions and repository quality standards | `gpt` | Add configurable GameCI test/build templates, license/fork safety guidance, repository hygiene checks, meta integrity validation, and recommended branch/security/release checks. Keep templates inactive in the kit repository. |

## Project context
- **Branch / build:** `gpt/harden-agent-workflow` / no Unity project in this reusable guidance repository.
- **Last known good build:** Not applicable; documentation and workflow-template kit.

## Handoff
- **In progress (exact stopping point):** KIT-001 is implemented on `gpt/harden-agent-workflow` and included in draft PR #1. KIT-002 has just been claimed; no CI template files have been written yet.
- **Next concrete step:** Add reusable, inactive Unity CI and repository-quality workflow examples plus setup/security guidance; inspect the complete PR diff and validate YAML/script syntax.
- **Known broken:** `ai/unity6-reference.md` still has an unfilled review-date placeholder; it is explicitly described as unverified in README and should be reviewed against official docs before being treated as current API guidance.
- **Verified (ran it):** Read current repository instructions/testing/Git rules and existing example Git attributes/ignore files. Checked current GameCI v4 action inputs and retrieved full commit SHAs for the pinned actions.
- **Not verified (human must check on device/editor):** No actual Unity project exists in this kit repository, so CI templates cannot execute Unity here. They require project-specific Unity version/path/build target and GitHub license secrets. Independent review of PR #1 remains pending.
- **Owner decisions waiting:** None for the template/documentation scope; consumers must select their platform, license type, and release policy when adopting the templates.
- **Bug / regression watch:** Do not activate Unity workflows in this master kit; keep examples under `examples/` so they only run after a game project copies/configures them. Never expose Unity or signing secrets to fork PRs.