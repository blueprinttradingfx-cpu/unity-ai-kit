# Definition of done

A task is done only when every applicable line is true. The AI states which lines it checked.

## All changes
- [ ] Does exactly what was asked; no unrequested extras.
- [ ] Compiles (or: "not compiled — no editor access", with the human check listed).
- [ ] No new console errors/warnings introduced (state what was checked).
- [ ] No hard rule in `AGENTS.md` broken; no `.meta`/scene/prefab hazards.
- [ ] Tuning numbers are in data, not code.
- [ ] Logic changes have a test (or a stated reason there is none).
- [ ] Diff is small and explained in two sentences.

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
- [ ] `ai/session-state.md` updated (stopping point, next step, verified vs not).
- [ ] New decision → ADR added. Old decision contradicted → flagged to the human.
- [ ] Commit message says why.

## Milestone gate smoke test (10 minutes, on device)
1. Fresh install launches to menu without errors.
2. Start → play → finish a round → return to menu.
3. Background the app 30 s and resume; rotate/lock if applicable; press Back at each screen.
4. Kill the app mid-round, relaunch: progress behaves as designed.
5. Airplane mode: game still works as designed.
6. Run 10 minutes: no crash, no visible slowdown, device not hot.
