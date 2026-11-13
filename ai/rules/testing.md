# Testing rules

Applies to: writing tests, fixing bugs, claiming something works.

**How to use this guide:** Test layers, naming, determinism, and regression techniques are recommended defaults. Choose coverage and execution frequency according to project risk, runtime cost, and available infrastructure. Honest reporting is a firm guardrail: distinguish checks that ran, checks that were skipped, and behavior that remains unverified.

## What to test where
- **EditMode tests (Unity Test Framework):** pure logic, data validation, save migration, balance math. Fast; run on every change.
- **PlayMode tests:** scene wiring, spawning, input-to-effect flows. Slower; run before merge and on milestone gates.
- **Simulation / soak tests:** run game logic headless for N simulated minutes with a seeded RNG; assert invariants (no negative currency, no stuck states, no exceptions). Cheap way to catch balance and state-machine bugs.
- **On-device checks:** touch feel, safe area, performance, interruptions. Cannot be automated well — use `ai/definition-of-done.md` and a written checklist, and send screenshots.

## Rules
- Logic bug fix = first write a failing test that reproduces it, then fix, then keep the test.
- Tests are deterministic: seeded RNG, injected clock, no real network, no dependence on frame timing.
- Test names say behaviour: `WaveClear_AwardsBonus_WhenNoLeaks`.
- Do not weaken or delete a test to make it pass. If a test is wrong, say why and change it deliberately.
- Tests live in their own `.asmdef` that references the module under test (EditMode or PlayMode assembly settings).
- A test that was never seen failing is not trusted: confirm it fails when the code is broken.

## Honest reporting
- Say exactly what ran: "EditMode: 42 passed, 0 failed" or "not run (no editor access)".
- If something could not be verified here (device behaviour, build, store flow), list it as a human check. Never write "should work" as if it were "works".

## Regressions
Track current recurring bugs in the `Bug / regression watch` handoff field in `ai/session-state.md`; add a test for each. Keep durable regression history in tests or the project's issue tracker, not the session board.
