"""Regression tests for reusable prompt template adaptability."""

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PromptTemplateTests(unittest.TestCase):
    def read(self, path: str) -> str:
        return (ROOT / path).read_text(encoding="utf-8")

    def test_start_session_scales_context_and_tracking_to_task(self) -> None:
        text = self.read("ai/prompts/start-session.md")
        self.assertIn("small, self-contained task", text)
        self.assertIn("Do not create a task ID", text)
        self.assertIn("Never take another agent's ownership", text)
        self.assertIn("meaningful checkpoint", text)

    def test_feature_prompt_uses_proportionate_coordination(self) -> None:
        text = self.read("ai/prompts/new-feature.md")
        self.assertIn("For a small, self-contained feature, keep the plan lightweight", text)
        self.assertIn("non-overlapping file boundaries", text)
        self.assertIn("Do not claim checks that were not run", text)

    def test_review_prompt_uses_consumer_project_context(self) -> None:
        text = self.read("ai/prompts/review.md")
        self.assertIn("consuming project's AGENTS.md", text)
        self.assertNotIn("Unity 6 mobile game", text)
        self.assertIn("Distinguish confirmed defects", text)
        self.assertIn("Do not suggest style-only changes", text)


if __name__ == "__main__":
    unittest.main()
