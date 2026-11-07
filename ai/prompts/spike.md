# Spike prompt (answer a technical question with evidence before committing)

```
We need to decide: <question, e.g. "IMGUI vs UI Toolkit for the in-run HUD">.
Plan a spike that takes at most <half a day>:
1. The smallest prototype in each option that exercises the hardest case.
2. What to measure (frame time avg/worst, GC.Alloc/frame, memory, authoring effort) and on which device.
3. The pass/fail threshold decided BEFORE measuring.
4. A draft ADR (ai/decisions/0000-template.md) with blanks for the results.
Do not write production code. Do not pick a winner before the numbers exist.
```
