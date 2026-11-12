# GitHub workflows for Unity projects

This guide defines a practical CI/CD baseline for Unity game repositories. Files under `examples/workflows/` are **templates**: copy and configure them in a game repository. They are deliberately not stored in this kit's active `.github/workflows/`, because this reusable guidance repository is not itself a Unity project.

## Recommended pipeline

| When | Required checks | Why |
|---|---|---|
| Every pull request | Diff/whitespace check, Unity asset metadata integrity, workflow lint; secret/dependency scanning when enabled in repository settings | Catch repository damage and unsafe changes before Unity starts |
| Every trusted pull request | Unity import/compile + EditMode tests; PlayMode tests where runner/time permits | Catch compile, data, logic, and scene integration regressions |
| Merge to main | Full Unity tests + at least one representative target build | Prove the merged commit is buildable |
| Nightly / scheduled | Full platform matrix, longer PlayMode/simulation/soak tests, coverage trend | Catch slower or platform-specific regressions |
| Release tag | Re-run required tests, produce versioned builds, sign in a protected environment, retain artifacts and release notes | Make releases reproducible and auditable |
| Before shipping a milestone | Real-device smoke, performance, memory, thermal, interruption, install/upgrade checks | CI cannot prove touch feel or real-device behaviour |

Do not run every expensive platform build on every PR by default. Start with one representative build on main, then add platforms when the project needs them.

## 1. Unity test and build workflow

Copy `examples/workflows/unity-ci.yml` to `.github/workflows/unity-ci.yml` in the game repository.

The template:
- Imports the project, compiles runtime/editor/test C# assemblies, and runs EditMode tests through GameCI on same-repository PRs only after approval of the protected `unity-pr-validation` environment, and on pushes to main through `unity-ci`.
- Runs PlayMode integration tests in a separate job with the same protected-environment boundary.
- Builds a sample Linux Standalone player after tests pass on main, or on a manual dispatch from the default branch only.
- Caches only the Unity `Library/` import cache, keyed by OS, Unity version file, and Package Manager lockfile.
- Uploads test results and build output as workflow artifacts.
- Skips licensed Unity jobs for fork-originated PRs; the separate repository-quality workflow still runs on those PRs.
- Restricts manual dispatch to the repository default branch. Licensed jobs consume environment-scoped secrets; same-repository PR jobs require explicit environment approval. Do not remove either guard without a documented security review.

### Configure it first

1. If the Unity project is in a subfolder, define the repository variable `UNITY_PROJECT_PATH` (for example `game/`); leave it unset when the project is at the repository root.
2. Change `targetPlatform` from the sample `StandaloneLinux64` to a platform the project actually ships.
3. Set the exact Editor version in `ProjectSettings/ProjectVersion.txt`; GameCI's `auto` mode reads this file.
4. Configure GitHub Environments before adding Unity credentials. Store Unity license values only as environment secrets: remove any repository-level or organization-level secrets with the same names (`UNITY_LICENSE`, `UNITY_EMAIL`, `UNITY_PASSWORD`, `UNITY_SERIAL`) so they cannot bypass environment approval.
   - `unity-pr-validation`: add the required Unity license secrets and configure required reviewers; enable **prevent self-review** where available. Allow the PR deployment refs used by your repository. Every same-repository PR that reaches licensed Unity jobs must be explicitly approved before those secrets are released.
   - `unity-ci`: add the Unity license secrets; restrict deployments to the default branch. Main-branch CI and the default-branch-only nightly workflow use this environment.
   - `release`: add the Unity license secrets plus only the signing credentials required by the project. Configure required reviewers, enable prevent self-review where available, and allow only the intended version tags plus the default branch for manual dispatch. Release tests and builds wait for this protected environment.
   - Fork PRs continue to skip licensed jobs and run repository-quality checks. Never switch to `pull_request_target` to expose secrets to fork code.
5. Run the workflow manually from the default branch and inspect the test report/build artifact before making checks required.

GameCI is community-maintained, not an official Unity service. Review action releases and permissions before adopting it. The examples pin actions to full commit SHAs; update pins deliberately and review upstream changes.

### Fork pull requests and secrets

GitHub does not provide repository secrets to workflows triggered from fork PRs. The Unity job skips those PRs; do not switch to `pull_request_target` and check out/run untrusted PR code with secrets. Keep static checks available to fork PRs. If fork PRs need Unity tests, use a carefully isolated self-hosted runner with no access to production credentials, or require a maintainer to run a trusted workflow after review.

## 2. Repository-quality checks

Copy `examples/workflows/repository-quality.yml` and the validators under `examples/scripts/` into the project. The checks are read-only and do not generate, edit, move, or delete Unity metadata. Fix findings through the Unity Editor or by restoring the correct asset and matching metadata from version control.

The syntax validator checks tracked JSON, Unity .asmdef/.asmref, YAML, Python, and JavaScript syntax and scans selected text files for conflict markers. Unity scene/prefab/asset YAML is deliberately not parsed as generic YAML. The workflow also runs actionlint and checks missing/orphan Unity .meta sidecars and duplicate/malformed GUIDs.

Run the validator regression suite from the kit with:
```sh
python -m unittest discover -s tests -v
```
It uses temporary repositories/fixtures and does not modify the consumer project's assets.

## 3. Standalone .NET checks

For separate SDK-style .NET tools, services, or test projects, optionally copy `examples/workflows/dotnet-validation.yml`. Configure:
- `DOTNET_PROJECT_PATHS`: newline-separated `.sln`, `.slnx`, or SDK-style `.csproj` paths.
- `DOTNET_TEST_PROJECT_PATHS`: optional newline-separated test project paths.
- `DOTNET_SDK_VERSION`: optional SDK version (defaults to `.NET 10 LTS` via `10.0.x`). .NET 8 and .NET 9 reached end of support on 10 November 2026; .NET 10 LTS is supported through November 2028. The kit deliberately defaults to LTS rather than the newly released .NET 11 STS. See the [official .NET support policy](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core).
- `DOTNET_RUN_VULNERABILITY_AUDIT`: optional `true`/`false` (defaults to `true`).

The workflow restores, builds Release, runs configured tests, verifies whitespace and analyzer formatting, and optionally reports vulnerable NuGet packages. Review audit output and update dependencies deliberately; do not assume a warning is automatically safe to ignore.

**Never point this workflow at Unity-generated solution/project files.** Unity projects must be compiled by the matching Unity Editor via GameCI; generic `dotnet build` does not reproduce Unity's generated references, platform defines, packages, or editor compilation pipeline. For standalone .NET projects, pin SDK and dependency policy to the needs of that codebase. Analyzer coverage depends on analyzers configured by the project.

The optional `dotnet list package --vulnerable --include-transitive` step is a report, not a vulnerability-fail gate by itself. NuGet restore also performs auditing when enabled by the project/SDK. To make selected severities block CI, configure `WarningsAsErrors` in the project or `Directory.Build.props`; for example, append `NU1903;NU1904` to fail on high/critical advisories, or include `NU1901;NU1902` to fail on all severities. .NET 10 projects default NuGet audit mode to `all` (including transitive dependencies). See [NuGet package auditing](https://learn.microsoft.com/en-us/nuget/concepts/auditing-packages) for audit-source and severity policy details.

## 4. Project-owned validators

Reusable CI should provide a stable place for each game to add domain checks. Keep validators in the game repository (for example `tools/validate_catalog.py`, `tools/validate_save_defaults.py`, or `scripts/check-pr-static.py`) and invoke them explicitly from that game's workflow. They should be offline/read-only where possible, return a non-zero exit code on contract violations, explain intentional exceptions, and clearly state what they do not prove.

Do not automatically execute every `validate_*.py` file discovered in a repository: scripts may require arguments, modify data, or be unrelated. Explicit commands are safer and make required checks reviewable. Never treat JSON/schema validation as proof that Unity scenes, prefabs, or runtime behavior work.

## 5. Nightly regression

Copy `examples/workflows/unity-nightly.yml`. It runs EditMode and PlayMode suites separately in the `unity-ci` environment, then builds the configured sample platform matrix only after both test jobs pass. Restrict `unity-ci` deployments to the default branch; scheduled runs execute from the default branch and manual dispatch is guarded likewise. Adjust schedule, platform matrix, timeout, and retention to match the project. Long deterministic simulations, soak tests, coverage collection, and project-owned validators should be added explicitly.

## 6. Release build

Copy `examples/workflows/unity-release.yml`. It validates a version tag, resolves it to an immutable commit SHA, tests and builds that exact SHA, and produces artifacts with source metadata and SHA-256 checksums.

The EditMode, PlayMode, and build jobs use the GitHub Environment named `release`. Configure required reviewers, allow only intended release tags and the default branch for manual dispatch, and store Unity license plus only the platform-specific signing secrets needed by the project in that environment. Add actual keystore/provisioning/signing steps inside that protected job; this generic template intentionally does not invent signing commands or store credentials. Artifacts are uploaded to the workflow run only; publishing to GitHub Releases, app stores, or external distribution remains a separately reviewed/manual step. Apple platforms need a macOS runner and platform-specific setup.

Manual release dispatch must be restricted to the default branch, validate the tag, and build the resolved commit SHA rather than resolving the tag again downstream.

## 7. Repository governance and security

The kit includes optional starter material under `examples/github/`. Apply only after choosing real maintainers/teams:
- Add a `CODEOWNERS` file with actual GitHub usernames or teams for high-risk paths such as `.github/workflows/`, `ai/`, build scripts, and release configuration. The example contains comments only and intentionally grants no ownership.
- Protect the default branch with a ruleset or branch protection: require PRs, required status checks from the actual workflow names, up-to-date branches where appropriate, and at least one independent review. Consider CODEOWNERS approval for workflow/security paths.
- Enable GitHub secret scanning and push protection where available; enable Dependabot alerts and security updates. Review alerts rather than blindly auto-merging.
- Use CodeQL or an equivalent security scanner for supported languages when the repository has meaningful code to analyze. Keep game-specific static analysis and supply-chain controls proportionate.
- Keep workflow permissions least-privilege, pin third-party actions to reviewed full commit SHAs, and periodically review pins and dependencies.
- For standalone .NET repositories, configure NuGet vulnerability review and SDK pinning. Do not run generic .NET builds against Unity-generated projects.

Branch protection/rulesets are repository settings and cannot be activated by copying files. Configure and verify them in GitHub Settings, then document which checks are required. Never make a required check name mandatory before its workflow is installed and has reported successfully.


## 8. GitHub Actions runtime compatibility

GitHub removed the Node 20 runtime from hosted Actions runners on 23 September 2026. The kit's pins were checked on 13 November 2026 and use Node 24-compatible releases:
- `actions/checkout` v7.0.1
- `actions/cache` v6.1.0
- `actions/upload-artifact` v7.0.2
- `actions/setup-dotnet` v6.1.0
- `game-ci/unity-test-runner` v4.3.2
- `game-ci/unity-builder` v6.0.0

The GameCI actions were checked against their `action.yml` runtime declarations; all listed actions declare Node 24. All action references are pinned to full commit SHAs. Do not downgrade to older Node 20 pins. Self-hosted runners must meet the current minimum runner version required by each action. See the [GitHub Node 20 removal notice](https://github.blog/changelog/2026-09-23-node-20-is-no-longer-available-in-github-actions/).

## 9. Reusable patterns from game repositories

| Observed pattern | Kit treatment |
|---|---|
| Garden Alchemy: PR diff checks, full history, Unity asset/.meta pairing, retired API/symbol regression checks | General metadata validation is included; retired-symbol assertions remain project-owned. |
| Weapon Ball Unity: offline catalog schema, unique IDs, bounds, JSON/SQLite parity, behavior manifest, save defaults, Python tests | Documented as project-owned data-contract validation. |
| Heartway: YAML/JSON/JavaScript/Python syntax and conflict checks | Generic source/config syntax and conflict checks are included. |
| Heartway: Firestore rules tests using a local emulator | Keep backend-specific emulator tests optional and run when backend rules/config change. |

The templates are not active workflows in this kit repository. Validate them in a real consumer Unity project before making them required.
