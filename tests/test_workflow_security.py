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

    def test_setup_guide_documents_environment_secret_boundaries(self) -> None:
        guide = (ROOT / "ai" / "github-workflows.md").read_text(encoding="utf-8")
        for environment in ("unity-pr-validation", "unity-ci", "release"):
            self.assertIn("`" + environment + "`", guide)
        self.assertIn("required reviewers", guide.lower())
        self.assertIn("repository-wide secrets", guide.lower())


if __name__ == "__main__":
    unittest.main()
