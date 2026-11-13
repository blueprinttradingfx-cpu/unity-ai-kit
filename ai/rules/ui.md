# UI rules

Applies to: `Assets/**/UI/**`, HUD, menus, dialogs, anything the player taps or reads.

**How to use this guide:** UI Toolkit, uGUI, navigation, localization, layout, and accessibility patterns below are recommendations or prompts for project decisions—not a mandate to rebuild an existing UI stack. Choose based on the target platforms, team experience, project architecture, accessibility needs, and measured performance. Record consequential technology choices in the consumer's ADRs.

## Technology choice (decide once per project, record as an ADR)
- Default for new projects: **UI Toolkit** for menus/screens and tools; **uGUI (Canvas)** is fine for world-space UI, heavy animation, or when the team already has it. Both are supported in Unity 6.
- **Do not use IMGUI (`OnGUI`) for runtime player UI in a new project.** It is intended for editor tooling and allocates per frame. If an existing project uses it, measure first (see "Spike" below) before building more screens on it.
- Never mix two UI technologies for the same screen without an ADR.

## Architecture
- UI never owns or mutates game state. It reads state and raises commands/events.
- One "screen controller" per screen: it binds data, handles taps, and nothing else. No game rules in it.
- Screens open/close through one navigation service (stack: push, pop, replace). Android Back button must work on every screen and every dialog.
- Strings: all player-visible text goes through localization. No hardcoded strings in prefabs/UXML except placeholders.

## Mobile layout
- Support the screen sizes you ship: pick reference resolution, use anchors/flex, test at least one tall (20:9+) and one 16:9 device.
- Respect `Screen.safeArea` (notches, cutouts, rounded corners).
- Touch targets at least ~48dp (about 9 mm). Spacing so thumbs do not mis-tap.
- Text scales with the system setting where possible; never clip text. Test the longest translation.
- Orientation locked per project decision (record it).

## Performance
- No per-frame string building, LINQ, or `new` in UI update paths. Update text only when the value changes.
- Split frequently-changing UI from static UI (separate canvases / elements) so one change does not rebuild everything.
- Disable raycast targets on non-interactive graphics. Pool list items; virtualize long lists.
- Atlas sprites; avoid huge full-screen alpha overdraw.

## Accessibility and feel
- Colour is never the only signal. Provide a text/icon cue.
- Animations are short, skippable, and honour a "reduce motion" setting.
- Every interactive element gives feedback (pressed state, sound via the audio event system, optional haptic).

## Spike template (when unsure which UI tech)
Build the two heaviest screens in each option. Measure on the lowest-end target phone: average and worst frame time, GC.Alloc per frame, memory, and authoring time. Write result as an ADR. Do this *before* building more than two screens.
