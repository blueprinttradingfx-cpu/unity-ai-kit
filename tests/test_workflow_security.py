"""Security regression tests for licensed Unity workflow environment boundaries."""
from __future__ import annotations

import unittest
from pathlib import Path

try:
    import yaml
except ImportError:  # The kit CI installs the pinned PyYAML dependency.
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / "examples" / "workflows"


@unittest.skipIf(yaml is None, "PyYAML is required for workflow policy tests")
class LicensedWorkflowSecurityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.workflows = {
            name: yaml.load((WORKFLOWS / name).read_text(encoding="utf-8"), Loader=yaml.BaseLoader)
            for name in ("unity-ci.yml", "unity-nightly.yml", "unity-release.yml")
        }

    def test_unity_ci_pull_requests_use_reviewer_gated_environment(self) -> None:
        workflow = self.workflows["unity-ci.yml"]
        jobs = workflow["jobs"]
        pr_environment = "${{ github.event_name == 'pull_request' && 'unity-pr-validation' || 'unity-ci' }}"
        for job_name in ("compile", "playmode"):
            job = jobs[job_name]
            self.assertEqual(job["environment"], pr_environment)
            self.assertTrue(any("UNITY_LICENSE" in step.get("env", {}) for step in job["steps"]))
            self.assertIn("github.event.pull_request.head.repo.full_name == github.repository", job["if"])
        self.assertEqual(jobs["build"]["environment"], "unity-ci")
        self.assertNotIn("pull_request_target", workflow)

    def test_nightly_jobs_use_default_branch_unity_environment(self) -> None:
        jobs = self.workflows["unity-nightly.yml"]["jobs"]
        self.assertEqual(set(jobs), {"editmode", "playmode", "platform-builds"})
        for job in jobs.values():
            self.assertEqual(job["environment"], "unity-ci")
            self.assertTrue(any("UNITY_LICENSE" in step.get("env", {}) for step in job["steps"]))

    def test_release_jobs_use_protected_release_environment(self) -> None:
        jobs = self.workflows["unity-release.yml"]["jobs"]
        for job_name in ("editmode", "playmode", "build"):
            self.assertEqual(jobs[job_name]["environment"], "release")
            self.assertTrue(any("UNITY_LICENSE" in step.get("env", {}) for step in jobs[job_name]["steps"]))
        self.assertIn("workflow_dispatch", self.workflows["unity-release.yml"]["on"])

    def test_manual_licensed_runs_are_default_branch_guarded(self) -> None:
        ci = self.workflows["unity-ci.yml"]["jobs"]
        default_branch_guard = "github.event_name != 'workflow_dispatch' || github.ref == format('refs/heads/{0}', github.event.repository.default_branch)"
        for job_name in ("compile", "playmode"):
            self.assertIn(default_branch_guard, ci[job_name]["if"])
        self.assertIn("github.ref == format('refs/heads/{0}', github.event.repository.default_branch)", ci["build"]["if"])

        nightly = self.workflows["unity-nightly.yml"]["jobs"]
        for job_name in ("editmode", "playmode"):
            self.assertIn(default_branch_guard, nightly[job_name]["if"])
        self.assertEqual(nightly["platform-builds"]["needs"], ["editmode", "playmode"])

        release = self.workflows["unity-release.yml"]["jobs"]
        validation_steps = release["validate-tag"]["steps"]
        self.assertTrue(any("PUSH_REF" in step.get("run", "") and "DEFAULT_BRANCH" in step.get("run", "") for step in validation_steps))
        self.assertNotIn("environment", release["validate-tag"])

    def test_first_party_and_gameci_actions_are_sha_pinned_to_node24_releases(self) -> None:
        expected = {
            "actions/checkout": "3d3c42e5aac5ba805825da76410c181273ba90b1",
            "actions/cache": "55cc8345863c7cc4c66a329aec7e433d2d1c52a9",
            "actions/upload-artifact": "cf430e030ddbb5b0abf93d22962f4752f3646cd9",
            "actions/setup-dotnet": "0f4a354dd5547a28c70b7853dbd95d5b67886e73",
            "game-ci/unity-test-runner": "fa6ced25861c16ef56187828c43f76d00df43a23",
            "game-ci/unity-builder": "eb1b9fba120c6e62c9fb7a7a81d6c107ce004c45",
        }
        found = set()
        workflow_paths = list((ROOT / ".github" / "workflows").glob("*.yml"))
        workflow_paths += list(WORKFLOWS.glob("*.yml"))
        for path in workflow_paths:
            workflow = yaml.load(path.read_text(encoding="utf-8"), Loader=yaml.BaseLoader)
            for job in workflow.get("jobs", {}).values():
                for step in job.get("steps", []):
                    action = step.get("uses")
                    if not action:
                        continue
                    name, ref = action.rsplit("@", 1)
                    self.assertRegex(ref, r"^[0-9a-f]{40}$", msg=f"{path}: {action} is not pinned to a full SHA")
                    if name in expected:
                        self.assertEqual(ref, expected[name], msg=f"{path}: update reviewed pin for {name}")
                        found.add(name)
        self.assertEqual(found, set(expected))

    def test_dotnet_template_defaults_to_supported_lts_sdk(self) -> None:
        workflow = yaml.load((WORKFLOWS / "dotnet-validation.yml").read_text(encoding="utf-8"), Loader=yaml.BaseLoader)
        sdk = workflow["jobs"]["dotnet"]["env"]["DOTNET_SDK_VERSION"]
        self.assertIn("10.0.x", sdk)
        self.assertNotIn("8.0.x", sdk)
        guide = (ROOT / "ai" / "github-workflows.md").read_text(encoding="utf-8")
        self.assertIn(".NET 10 LTS", guide)
        self.assertIn("November 2028", guide)
        self.assertIn("official .NET support policy", guide)

    def test_setup_guide_documents_environment_secret_boundaries(self) -> None:
        guide = (ROOT / "ai" / "github-workflows.md").read_text(encoding="utf-8")
        for environment in ("unity-pr-validation", "unity-ci", "release"):
            self.assertIn("`" + environment + "`", guide)
        self.assertIn("required reviewers", guide.lower())
        self.assertIn("repository-level or organization-level secrets", guide.lower())
        self.assertIn("prevent self-review", guide.lower())


if __name__ == "__main__":
    unittest.main()
