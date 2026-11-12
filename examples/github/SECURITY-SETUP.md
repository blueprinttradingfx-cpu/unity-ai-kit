# Repository security setup checklist

These are optional repository settings, not controls activated by copying this file.

## Before enabling
- Identify maintainers for workflow, build, release, and dependency changes.
- Add real CODEOWNERS entries; the accompanying CODEOWNERS example is intentionally comments-only.
- Install the kit's quality and Unity workflows, run them successfully, and record the exact status-check names before requiring them.

## Recommended GitHub settings
- Protect the default branch with a ruleset or branch protection.
- Require pull requests and at least one independent approval for production repositories.
- Require CODEOWNERS review for workflow, release, and security-sensitive paths where supported.
- Require the actual CI checks that protect the project; do not require checks that have not been installed.
- Restrict who can bypass rulesets and who can push directly to the default branch.
- Enable secret scanning and push protection where available.
- Enable Dependabot alerts and security updates; review update PRs and action pin changes.
- Consider CodeQL for supported languages and meaningful source code.
- Keep Actions permissions read-only by default and grant write permissions only to jobs that need them.
- Keep signing credentials in protected GitHub Environments with required reviewers; never expose them to ordinary pull-request jobs.
- Review third-party action pins against upstream releases before updating full commit SHAs.

## Operational verification
After configuring settings, test with a non-production branch/PR:
1. Confirm direct pushes to the default branch are rejected for ordinary contributors.
2. Confirm required checks appear and block merging when failing.
3. Confirm CODEOWNERS requests the intended reviewers.
4. Confirm fork PR workflows do not receive repository secrets.
5. Confirm release signing secrets are available only after protected-environment approval.

Record the chosen ruleset, required checks, owners, and exceptions in the consumer repository. GitHub settings vary by plan and organization policy; verify availability in the target repository.
