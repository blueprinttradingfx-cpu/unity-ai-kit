# Consumer project validation checklist

Use this checklist when installing the kit into a real Unity game repository. The kit repository itself is not a Unity project, so passing its source checks does not validate Unity import, compilation, tests, builds, or device behavior.

## 1. Record the consumer baseline

- [ ] Record the consumer repository, default branch, and project path.
- [ ] Record the exact Editor version from `ProjectSettings/ProjectVersion.txt`.
- [ ] Record the render pipeline and relevant package versions from `Packages/manifest.json` and `Packages/packages-lock.json`.
- [ ] Record target platforms, scripting backend, architecture, and build output requirements.
- [ ] Identify EditMode and PlayMode test assemblies and any project-owned validators.
- [ ] Confirm the Unity license type and the required GameCI secret format without copying credentials into issues, PRs, logs, or this checklist.

## 2. Install and configure the kit

- [ ] Copy the kit guidance into the Unity project root; preserve existing project-specific instructions and merge rather than overwrite them.
- [ ] Replace placeholders in `AGENTS.md`, especially project name, Unity version, platforms, folder layout, and executable commands.
- [ ] Complete `ai/project-brief.md`; retain only the AI-tool pointer files the team uses.
- [ ] Apply the Unity `.gitignore`, `.gitattributes`, and `.editorconfig` examples only where the project lacks equivalent configuration.
- [ ] Configure Unity Asset Serialization = Force Text and Version Control = Visible Meta Files in the Editor.
- [ ] Read the relevant rules and record any consumer-specific deviations as ADRs.
- [ ] Follow `ai/coordination-model.md`; assign phase/work-package owners and avoid micro-task churn in session state.

## 3. Configure GitHub workflow security

- [ ] Copy only the workflow templates the project intends to use into `.github/workflows/`.
- [ ] Set `UNITY_PROJECT_PATH` when the Unity project is not at repository root.
- [ ] Configure `unity-pr-validation` with Unity license environment secrets and required reviewers; enable prevent self-review where available.
- [ ] Configure `unity-ci` with Unity license environment secrets and restrict deployments to the default branch.
- [ ] Configure `release` with Unity license secrets and only required signing secrets; require reviewers and restrict deployment refs to intended version tags plus the default branch for manual dispatch.
- [ ] Remove repository-level and organization-level secrets named `UNITY_LICENSE`, `UNITY_EMAIL`, `UNITY_PASSWORD`, or `UNITY_SERIAL` if those credentials are now stored in protected environments. Otherwise they can bypass environment approval.
- [ ] Confirm the PR deployment-ref policy permits the intended pull-request jobs, then test that approval is required before the licensed job starts.
- [ ] Keep fork PRs on repository-quality checks; do not use `pull_request_target` to check out and run untrusted PR code with secrets.
- [ ] Configure a ruleset/branch protection with PR requirement, actual successful required checks, and independent review. Do not require check names before they have reported successfully.
- [ ] Enable secret scanning, push protection, and Dependabot features where available; assign real CODEOWNERS only after maintainers are chosen.

## 4. Validate in increasing cost order

- [ ] Run the repository-quality workflow on a PR, including whitespace, actionlint, source/config syntax, and Unity metadata checks.
- [ ] Run the Unity CI workflow from the default branch and inspect the Unity Editor import/compile and EditMode report.
- [ ] Inspect PlayMode results separately; record skipped or missing test assemblies rather than treating them as passes.
- [ ] Run one representative target build and inspect its artifact.
- [ ] Run the nightly workflow and confirm its platform matrix, timeouts, and artifact retention match the project.
- [ ] Validate release workflow behavior with a non-production test tag before enabling signing or distribution.
- [ ] Confirm release approval gates, source commit metadata, checksums, and artifact retention.
- [ ] Run the milestone smoke test on the lowest-supported real device; record performance, memory, thermal, interruption, install/upgrade, and offline results separately from CI.

## 5. Record evidence and close the handoff

- [ ] Record exact workflow run URLs, commit SHAs, Unity version, target platform, test counts, build result, and artifact links.
- [ ] Record failures, skipped jobs, missing secrets, and human-only checks as blockers; do not relabel them as passed.
- [ ] Request independent review for workflow/security/architecture changes and resolve or explicitly accept each finding.
- [ ] Update the consumer phase tracker and `ai/session-state.md` only for meaningful ownership, status, blocker, priority, milestone, or handoff changes.
- [ ] Mark consumer validation complete only when the required Unity Editor, test, build, and human/device acceptance evidence exists.

## Planned first consumer

Garden Alchemy is the first planned consumer. Its exact Unity Editor version, project path, test assemblies, target platforms, and valid license configuration must be read from that repository at integration time. Do not assume the current kit default (Unity 6.3 LTS) overrides the consumer's checked-in Editor version.
