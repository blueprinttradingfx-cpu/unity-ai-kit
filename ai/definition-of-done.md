# Definition of done

A task or phase is done only when every applicable line is true. State which lines were checked and link evidence in the PR or handoff.

## All changes
- [ ] Does exactly what was asked; no unrequested extras.
- [ ] Relevant validation ran successfully, or is explicitly marked **not run** with the reason and exact human check required.
- [ ] No new console errors/warnings introduced (do not imply a console check if no Editor was run).
- [ ] No hard rule in `AGENTS.md` broken; no `.meta`/scene/prefab hazards.
- [ ] Tuning numbers are in data, not code.
- [ ] Logic changes have a test (or a stated reason there is none); project-specific validators run where relevant.
- [ ] Diff is focused and explained.
- [ ] Task/phase owner, status, next step, and verification evidence are consistent in the owning tracker.

## Phase completion
- [ ] Every in-scope sub-item is Done, explicitly Deferred with owner approval, or moved to Blocked with a concrete dependency.
- [ ] Phase exit criteria and acceptance checks pass; evidence is linked from the phase tracker.
- [ ] Dependencies and integration points are resolved; no hidden work is represented as complete.
- [ ] Shared session summary reflects the phase status/ownership transition.
- [ ] Independent review is complete for architecture, save data, security, build/release, and agent-workflow changes, or clearly marked pending.

## Verification evidence
For each command/test/build, record the exact command or Editor action, Unity/package version when applicable, result and exit code/pass-fail counts, and log/artifact/screenshot path. Never infer a successful result from a command that was not run.

For documentation-only changes, check links, referenced paths, headings/code fences, and the complete diff; Unity compilation is not applicable.

## Unity and CI checks
- [ ] Unity Editor version matches `ProjectSettings/ProjectVersion.txt`; report exact version.
- [ ] Unity Editor import/compile succeeds; EditMode tests cover changed logic/data; PlayMode tests cover affected integration where applicable.
- [ ] Standalone SDK-style .NET projects (if configured) restore/build; test projects run; configured formatting/analyzer checks pass. Generic `dotnet build` is not a substitute for Unity Editor compilation.
- [ ] Relevant target build succeeds, or is marked not run with reason and precise human check.
- [ ] Repository-quality checks pass: diff whitespace, actionlint, tracked JSON/asmdef/asmref/YAML/Python/JavaScript syntax, conflict-marker scan, and Unity metadata validation where configured. Unity scene/prefab YAML is not generically parsed.
- [ ] Package manifest and lockfile changes are reviewed together; no unrequested package upgrades.
- [ ] CI artifacts/logs are linked; skipped jobs are stated rather than described as passed.
- [ ] Signing/release checks use protected environments; no signing secrets are available to ordinary PR jobs.
- [ ] Nightly workflows have deliberate platform matrix, schedule, timeout, and retention.
- [ ] Release workflows test the exact version tag, record source commit/platform metadata, checksum artifacts, and require protected approval before signing/distribution.
- [ ] Real-device checks are recorded separately; a CI build is not evidence of device performance or UX.

See `ai/github-workflows.md` for recommended PR, main, nightly, and release pipelines.

## Review
- [ ] Review the complete diff, not only snippets.
- [ ] Request independent review for architecture, save data, security, release/build, and agent workflow/safety changes. If unavailable, mark pending.
- [ ] Resolve or explicitly record every review finding.

## Anything visible (UI, VFX, animation, layout)
- [ ] Human told exactly which screen/state to open and what "correct" looks like.
- [ ] Screenshot/video from a real device exists for the change (human provides).
- [ ] Check safe area, longest text, smallest/tallest screen, Back button, pressed/disabled states.

## Performance-sensitive
- [ ] No per-frame allocation added (profiler evidence or code reasoning stated).
- [ ] Baseline vs new measurement on the lowest-end device, if performance was the task.

## Data / saves
- [ ] Save version bumped and migration written if the format changed.
- [ ] Validation tool/test passes (IDs unique, ranges valid).

## Wrap-up and coordination
- [ ] Update the owning phase tracker with completed sub-items, checkpoint evidence, blockers, and next step.
- [ ] Update `ai/session-state.md` only if phase ownership/status, blockers, priority, milestone, or handoff changed; do not log each sub-item there.
- [ ] Move completed/blocked/backlog tasks to their matching lists, preserving stable IDs.
- [ ] New decision → ADR added. Old decision contradicted → flagged to the human.
- [ ] Commit/PR message says why and names the task/phase ID.

## Milestone gate smoke test (10 minutes, on device)
1. Fresh install launches to menu without errors.
2. Start → play → finish a round → return to menu.
3. Background the app 30 s and resume; rotate/lock if applicable; press Back at each screen.
4. Kill the app mid-round, relaunch: progress behaves as designed.
5. Airplane mode: game still works as designed.
6. Run 10 minutes: no crash, no visible slowdown, device not hot.
