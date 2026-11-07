# New feature prompt

```
Feature: <name>. Follow AGENTS.md.
Before coding, reply with:
1. Which existing systems/ADRs it touches (read ai/decisions/ and ai/project-brief.md).
2. The data it needs (fields, units, ranges) and where it lives.
3. Files you will add/change (max ~5; if more, propose a split).
4. How I will see it working on device, and how a test will prove the logic.
5. Anything that conflicts with a pillar or earlier decision.
Wait for my "go". Then implement in small steps, tell me what to check after each, and update ai/session-state.md.
```
