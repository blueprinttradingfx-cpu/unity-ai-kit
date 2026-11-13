# Kit principles: strong defaults, flexible implementation

The Unity AI Kit is a reusable development framework, not a game-specific starter project. It should help teams make good decisions without pretending every Unity game has the same architecture, workflow, platform, team structure, or production constraints.

## Three levels of guidance

### 1. Safety and integrity guardrails

Treat these as defaults that should not be bypassed casually:

- Protect credentials, signing material, personal data, and production secrets.
- Do not run untrusted pull-request code with privileged secrets.
- Avoid destructive Git, filesystem, asset, or release actions without clear authorization and a recovery path.
- Never claim compilation, tests, builds, or runtime behavior passed without evidence.
- Preserve Unity asset metadata and serialized references; use the Editor for operations that require Unity to maintain them.

A project may strengthen these guardrails. Relaxing one requires an explicit, documented risk decision by the project owner.

### 2. Recommended engineering defaults

The kit may provide opinionated starting points for architecture, coding style, testing, performance, data ownership, agent coordination, and CI/CD. These are recommendations, not universal laws.

For each recommendation, explain the problem it addresses and the context in which it is useful. A consuming project may adapt or replace it when its existing architecture, genre, team, tooling, or performance profile calls for a different approach.

Examples include:

- UI command/state separation and domain boundaries.
- ScriptableObject, JSON, or other data-driven configuration.
- Allocation avoidance in frequently executed code.
- Phase-based agent ownership and parallel work limits.
- Which Unity tests run on pull requests, mainline, nightly, or release.

### 3. Consumer-owned decisions

The consuming project owns its:

- Unity Editor version, packages, render pipeline, platforms, build targets, and folder layout.
- Game architecture, domain boundaries, naming, coding conventions, and data model.
- Test strategy, required checks, CI trust model, runner selection, and release process.
- Agent count, coordination cadence, task sizing, and review/approval policy.

The kit should surface trade-offs and offer safe options, not silently impose a particular consumer's configuration.

## How to adapt a recommendation

1. Identify whether the instruction is a safety guardrail, recommended default, or consumer-owned choice.
2. Check the consumer's existing architecture and project instructions before introducing a new convention.
3. Keep the recommendation when it fits; otherwise adapt it to the project's needs.
4. Record consequential or cross-agent decisions in the consumer's ADRs or project brief.
5. Keep reusable improvements in this kit generic. Keep game-specific facts, paths, values, and policies in the consuming repository.

## Authoring test for kit changes

Before adding or tightening a rule, ask:

- Is this a genuine security/integrity requirement, or just one reasonable engineering style?
- Does it work across different Unity versions, genres, platforms, team sizes, and CI providers?
- Can it be expressed as a configurable example rather than a mandatory convention?
- Does the documentation say what the rule protects against and when an alternative is reasonable?

Prefer **strong defaults, flexible implementation, and project-owned decisions**.
