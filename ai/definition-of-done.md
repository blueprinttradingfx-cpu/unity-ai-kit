# Definition of done

A task is done only when every applicable line is true. The AI states which lines it checked and links the evidence in its PR or handoff.

## All changes
- [ ] Does exactly what was asked; no unrequested extras.
- [ ] The relevant validation ran successfully, or is explicitly marked **not run** with the reason and exact human check required.
- [ ] No new console errors/warnings introduced (state what was checked; do not imply a console check if no Editor was run).
- [ ] No hard rule in `AGENTS.md` broken; no `.meta`/scene/prefab hazards.
- [ ] Tuning numbers are in data, not code.
- [ ] Logic changes have a test (or a stated reason there is none).
- [ ] Diff is small and explained in two sentences.
- [ ] Task ID, owner, status, next step, and verification evidence are consistent across the board and handoff.

## Verification evidence (record what applies)
For each command/test/build, record:
- Exact command or Unity UI action.
- Unity Editor version and relevant package version(s), when applicable.
- Result and exit code / pass-fail counts.
- Log or artifact path, plus any relevant commit or screenshot link.

Do not invent a successful result from a command that was not run. For documentation-only changes, state the checks performed (for example: links and referenced paths checked, headings/code fences reviewed, and diff inspected); Unity compilation is not applicable.

## Unity and CI checks
- [ ] Unity Editor version matches `ProjectSettings/ProjectVersion.txt`; report the exact version.
- [ ] Unity Editor import/compile succeeds using the exact project Editor version; EditMode tests run for changed logic/data; PlayMode tests run for affected scene/gameplay integration where applicable.
- [ ] Standalone SDK-style .NET projects (if present/configured) restore and build; test projects run; configured formatting/analyzer checks pass. Do not use generic `dotnet build` as a substitute for Unity Editor compilation.
- [ ] The relevant target build succeeds, or is explicitly marked not run with the reason and a precise human check.
- [ ] Repository-quality checks pass: diff whitespace, workflow lint, and Unity metadata sidecar/GUID validation where configured.
- [ ] Package manifest and lockfile changes are reviewed together; no unrequested package upgrades.
- [ ] CI artifacts/logs are linked; state skipped jobs (including fork-PR Unity jobs) rather than describing them as passed.
- [ ] Signing/release checks use protected environments; no signing secrets are available to ordinary PR jobs.
- [ ] Real-device checks are recorded separately; a CI build is not evidence of device performance or UX.

See `ai/github-workflows.md` for the recommended PR, main-branch, nightly, and release pipeline.

## Review
- [ ] Review the complete diff, not only the edited snippets.
- [ ] For changes to architecture, save data, security, build/release, or agent safety/workflow rules, request an independent review when another reviewer is available. If unavailable, mark the review as pending; do not call a self-review independent.
- [ ] Resolve or explicitly record every review finding; do not silently ignore a blocker.

## Anything visible (UI, VFX, animation, layout)
- [ ] Human told exactly which screen/state to open and what "correct" looks like.
- [ ] **Screenshot or short video from a real device** exists for the change (human provides). No visual change is "done" on description alone.
- [ ] Checked: safe area, longest text, smallest and tallest screen, Back button, pressed/disabled states.

## Performance-sensitive
- [ ] No per-frame allocation added (profiler evidence or code reasoning stated).
- [ ] Baseline vs new measurement on the lowest-end device, if the task was about performance.

## Data / saves
- [ ] Save version bumped and migration written if the format changed.
- [ ] Validation tool/test passes (IDs unique, ranges valid).

## Wrap-up
- [ ] `ai/session-state.md` updated with exact stopping point, next step, known issues, verified vs not verified, and owner decisions waiting.
- [ ] Completed tasks moved to `ai/done-tasks.md`; blocked tasks moved to `ai/blocked-tasks.md`; work not yet ready moved to `ai/backlog-tasks.md`. Preserve the task ID when moving it.
- [ ] New decision → ADR added. Old decision contradicted → flagged to the human.
- [ ] Commit/PR message says why and names the task ID.

## Milestone gate smoke test (10 minutes, on device)
1. Fresh install launches to menu without errors.
2. Start → play → finish a round → return to menu.
3. Background the app 30 s and resume; rotate/lock if applicable; press Back at each screen.
4. Kill the app mid-round, relaunch: progress behaves as designed.
5. Airplane mode: game still works as designed.
6. Run 10 minutes: no crash, no visible slowdown, device not hot.
