# GitHub workflows for Unity projects

This guide defines a practical CI/CD baseline for Unity game repositories. Files under `examples/workflows/` are **templates**: copy and configure them in a game repository. They are deliberately not stored in this kit's active `.github/workflows/`, because this reusable guidance repository is not itself a Unity project.

## Recommended pipeline

| When | Required checks | Why |
|---|---|---|
| Every pull request | Diff/whitespace check, Unity asset metadata integrity, workflow lint, secret/dependency scanning | Catch repository damage and unsafe changes before Unity starts |
| Every trusted pull request | Unity import/compile + EditMode tests; PlayMode tests where runner/time permits | Catch compile, data, logic, and scene integration regressions |
| Merge to main | Full Unity tests + at least one representative target build | Prove the merged commit is buildable |
| Nightly / scheduled | Full platform matrix, longer PlayMode/simulation/soak tests, coverage trend | Catch slower or platform-specific regressions |
| Release tag | Re-run required tests, produce versioned builds, sign in a protected environment, retain artifacts and release notes | Make releases reproducible and auditable |
| Before shipping a milestone | Real-device smoke, performance, memory, thermal, interruption, install/upgrade checks | CI cannot prove touch feel or real-device behaviour |

Do not run every expensive platform build on every PR by default. Start with one representative build on main, then add platforms when the project needs them.

## 1. Unity test and build workflow

Copy `examples/workflows/unity-ci.yml` to `.github/workflows/unity-ci.yml` in the game repository.

The template:
- Runs EditMode and PlayMode tests through GameCI on trusted PRs and pushes to main.
- Builds a sample Linux Standalone player after tests pass on main, or on manual dispatch.
- Caches only the Unity `Library/` import cache, keyed by OS, Unity version file, and Package Manager lockfile.
- Uploads test results and build output as workflow artifacts.
- Skips the licensed Unity job for fork-originated PRs. The separate repository-quality workflow still runs on those PRs.

### Configure it first

1. If the Unity project is in a subfolder, define the repository variable `UNITY_PROJECT_PATH` (for example `game/`); leave it unset when the project is at the repository root. The template uses this variable for the test, build, and Library cache paths.
2. Change `targetPlatform` from the sample `StandaloneLinux64` to a platform the project actually ships.
3. Set the exact Editor version in `ProjectSettings/ProjectVersion.txt` inside the Unity project; GameCI's `auto` mode reads this file.
4. In repository **Settings → Secrets and variables → Actions**, add the license secrets for the license type you use:
   - Unity Personal: `UNITY_LICENSE` (contents of the activated `.ulf` file).
   - Unity Pro/Plus: `UNITY_EMAIL`, `UNITY_PASSWORD`, and `UNITY_SERIAL`.
   - A floating license server can instead be configured with GameCI's `unityLicensingServer` input; protect its URL/configuration as appropriate.
5. Keep signing credentials separate from Unity activation. Add Android keystore or Apple signing secrets only to a protected release job/environment, never to general PR jobs.
6. Run the workflow manually once and inspect the test report and build artifact before making its check required.

GameCI is a community-maintained action suite, not an official Unity service. Review its release and action permissions before adopting it. The examples pin actions to full commit SHAs; update those pins deliberately and review the upstream changes.

### Fork pull requests and secrets

GitHub does not provide repository secrets to workflows triggered from fork PRs. The Unity job therefore skips those PRs; do not "fix" this by switching to `pull_request_target` and checking out/running untrusted PR code with secrets. Keep static checks available to fork PRs. If fork PRs need Unity tests, use a carefully isolated self-hosted runner with no access to production credentials, or require a maintainer to run a trusted workflow after review.

## 2. Repository-quality checks

Copy `examples/workflows/repository-quality.yml` and `examples/scripts/validate_unity_meta.py` into the project.

The quality workflow checks:
- Whitespace errors in the changed Git diff.
- Missing Unity `.meta` sidecars for files/folders under `Assets/`.
- Duplicate or malformed GUIDs in Unity metadata.

The validator is read-only. It does not generate, edit, move, or delete metadata. Fix findings through the Unity Editor or by restoring the correct asset and matching metadata from version control.

Also run `actionlint` against workflow YAML before merging workflow changes. Consider `yamllint` and Markdown linting if the repository has a broader documentation standard.

## 3. Unity-specific checks to add as the project grows

### Code and compilation
- Compile/import the project using the exact Editor version committed in `ProjectVersion.txt`.
- Treat compiler errors as blockers; review new warnings rather than suppressing them globally.
- Add Roslyn analyzers or Unity-compatible analyzers only after verifying compatibility with the project's Unity/C# language version.
- Keep formatting rules in `.editorconfig`; do not use `dotnet format` against generated Unity solution files as a substitute for an Editor compile.

### Tests
- **EditMode:** pure domain logic, formulas, deterministic random systems, data validation, serialization, save migration.
- **PlayMode:** scene composition, prefab wiring, lifecycle, spawning, input-to-gameplay flows, UI integration.
- **Build smoke:** build at least one target after merge; launch it in a controlled smoke environment where practical.
- **Simulation/soak:** deterministic seeded runs for economy, wave progression, state machines, and invariants.
- **Device matrix:** low/mid/high target devices, safe areas, frame pacing, memory, thermal behaviour, suspend/resume, offline mode, and install/update flows.
- **Coverage:** collect coverage as a trend and use thresholds only after the baseline is stable. Do not make coverage percentage a substitute for meaningful assertions.

### Asset and project integrity
- Commit every relevant `.meta` file. Never regenerate metadata to silence a duplicate-GUID or missing-file check.
- Commit `Packages/manifest.json` and `Packages/packages-lock.json` together. Review package changes and pin Git dependencies to immutable revisions.
- Use Git LFS for large binary assets and verify LFS objects are available before release.
- Keep `Library/`, `Temp/`, `Logs/`, `obj/`, local IDE files, builds, and signing keys out of Git.
- Keep scenes/prefabs serialized as text and use UnityYAMLMerge where appropriate; avoid concurrent edits to the same scene or prefab.
- For asset moves/renames, use the Unity Editor or move the asset and its matching `.meta` together.

### Security and dependency checks
- Enable GitHub secret scanning and push protection where available.
- Enable Dependabot for GitHub Actions; review action updates rather than auto-merging them blindly.
- Unity Package Manager dependencies are primarily defined by `Packages/manifest.json` and `packages-lock.json`; verify each proposed version and package source. Dependabot does not automatically manage every Unity Registry/Git package pattern.
- Use CodeQL for C# where the repository's plan and project setup support it; triage findings rather than suppressing whole query categories.
- Never put credentials, keystores, service account files, tokens, or production endpoints in the repository or logs.

## 4. GitHub Actions security baseline

Apply these to every workflow:
- Set workflow-level `permissions: contents: read`; grant additional permissions only to the job that needs them.
- Pin third-party actions to full 40-character commit SHAs and leave a version comment. Keep a process for reviewing and updating pins.
- Use `concurrency` with cancellation for superseded PR runs.
- Set reasonable `timeout-minutes`; avoid unbounded jobs.
- Do not print secrets or dump the full environment into logs.
- Do not interpolate untrusted PR titles, branch names, commit messages, or issue text directly into shell scripts. Pass values through environment variables and quote them.
- Do not use `pull_request_target` to run code from an untrusted PR with secrets or write permissions.
- Keep deployment/signing jobs separate, restricted to protected branches/tags and GitHub Environments with required reviewers.
- Keep artifacts short-lived unless release retention is required; label artifacts with commit SHA, Unity version, and target platform.

## 5. Branch protection and pull-request policy

Recommended `main` protection:
- Require pull requests; block direct pushes for normal contributors/agents.
- Require the repository-quality check and Unity test check. Make the Unity check required only after the license-backed workflow is configured and the fork-PR skip policy is understood.
- Require at least one human review for gameplay, architecture, save-data, build/release, and security changes.
- Dismiss stale approvals when new commits materially change the diff.
- Require conversation resolution and prevent force pushes/deletion of `main`.
- Use CODEOWNERS for sensitive areas (build pipelines, signing/release configuration, save migrations) if the team has maintainers for them.
- Consider a merge queue when several PRs land concurrently.

A skipped Unity job on a fork PR may not provide a required success check. Choose a repository policy deliberately: use static checks as required for all PRs and require a maintainer-triggered trusted Unity run before merge, or use a secure isolated runner design. Do not weaken secret handling just to make a status green.

## 6. Release pipeline

A release workflow should be separate from PR CI:
1. Trigger from a protected version tag or approved manual dispatch.
2. Verify the tag points to the intended commit and that required tests pass.
3. Build each shipping platform with a recorded Unity version and build settings.
4. Sign only inside a protected GitHub Environment; never expose signing secrets to PR jobs.
5. Upload immutable build artifacts with checksums and commit metadata.
6. Require human approval before publishing to stores or distributing externally.
7. Preserve release notes, build logs, test reports, and the exact source commit.

Do not auto-publish store builds from a normal pull request or every push to main.

## References

- [GameCI getting started](https://game.ci/docs/github/getting-started/)
- [GameCI activation](https://game.ci/docs/github/activation/)
- [GameCI test runner](https://game.ci/docs/github/test-runner/)
- [GameCI builder](https://game.ci/docs/github/builder/)
- [GitHub Actions secure use](https://docs.github.com/en/actions/reference/security/secure-use)
- [GitHub workflow permissions and security hardening](https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)
