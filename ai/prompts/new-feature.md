# New feature prompt

```
Feature: <name>. Follow the consumer's AGENTS.md and project-owned decisions.

Before coding, reply with:
1. Existing systems/ADRs touched (read the relevant project brief and decision records).
2. Required data/contracts and their source of truth.
3. Likely files/systems to add or change; propose a work-package split only if scope or conflict risk warrants it.
4. How the result will be verified, including tests and any Editor/device checks the human must perform.
5. Conflicts with project pillars, prior decisions, or existing architecture.

For a small, self-contained feature, keep the plan lightweight. For substantial or parallel work, use the phase/work-package ownership model and agree on non-overlapping file boundaries before implementation.

Wait for my "go". Then implement within the approved scope. Give me useful checkpoints, not an update after every tiny edit. Update the owning tracker and global session summary only at their meaningful checkpoint/ownership cadence. Do not claim checks that were not run.
```
