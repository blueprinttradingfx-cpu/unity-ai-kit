"""Regression tests for reusable coordination/task guidance."""

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class WorkflowGuidanceTests(unittest.TestCase):
    def read(self, path: str) -> str:
        return (ROOT / path).read_text(encoding="utf-8")

    def test_coordination_supports_lightweight_and_multi_agent_modes(self) -> None:
        text = self.read("ai/coordination-model.md")
        self.assertIn("Solo / small project", text)
        self.assertIn("Small team / multi-agent project", text)
        self.assertIn("up to three active work-package owners", text)
        self.assertIn("Do not take another agent's ownership without explicit human approval", text)
        self.assertIn("Do not update the global summary for every file edit", text)

    def test_task_ids_are_for_tracked_work_not_every_action(self) -> None:
        text = self.read("ai/task-lifecycle.md")
        self.assertIn("No task ID, backlog row, or phase tracker is required", text)
        self.assertIn("Do not assign IDs to every small action", text)
        self.assertIn("Never take work owned by another agent", text)

    def test_agent_startup_allows_direct_small_tasks(self) -> None:
        text = self.read("AGENTS.md")
        self.assertIn("For a small self-contained request, proceed directly", text)
        self.assertIn("Never take another agent's owned work without explicit user approval", text)
        self.assertIn("Evidence guardrail", text)
        self.assertIn("Secret guardrail", text)

    def test_readme_explains_optional_coordination(self) -> None:
        text = self.read("README.md")
        self.assertIn("The coordination model is optional", text)
        self.assertIn("Do not create a phase tracker, task ID, or status-board row for every small change", text)
        self.assertIn("Update shared state only when", text)


if __name__ == "__main__":
    unittest.main()
