"""Regression tests for the kit's read-only repository validators.

Run with: python -m unittest discover -s tests -v
Tests use temporary Git repositories and never touch a consumer project's files.
"""
from __future__ import annotations

import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "examples" / "scripts"


class ValidatorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.repo = Path(self.temp.name)
        (self.repo / "examples" / "scripts").mkdir(parents=True)
        shutil.copy2(SCRIPTS / "validate_source_syntax.py", self.repo / "examples/scripts/")
        shutil.copy2(SCRIPTS / "validate_unity_meta.py", self.repo / "examples/scripts/")
        subprocess.run(["git", "init", "-q"], cwd=self.repo, check=True)
        subprocess.run(["git", "add", "."], cwd=self.repo, check=True)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write(self, relative: str, content: str) -> Path:
        path = self.repo / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        subprocess.run(["git", "add", relative], cwd=self.repo, check=True)
        return path

    def run_script(self, relative: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["python3", str(self.repo / relative)],
            cwd=self.repo,
            text=True,
            capture_output=True,
            check=False,
        )

    def add_asset(self, relative: str, guid: str) -> None:
        asset = self.write(relative, "fixture")
        self.write(relative + ".meta", f"fileFormatVersion: 2\nguid: {guid}\n")

    def test_metadata_validator_accepts_valid_sidecars(self) -> None:
        (self.repo / "Assets").mkdir()
        self.write("Assets/Scripts.meta", "fileFormatVersion: 2\nguid: " + "a" * 32 + "\n")
        self.add_asset("Assets/Scripts/Example.cs", "b" * 32)
        result = self.run_script("examples/scripts/validate_unity_meta.py")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_metadata_validator_reports_missing_sidecar(self) -> None:
        self.write("Assets/Loose.cs", "class Loose {}")
        result = self.run_script("examples/scripts/validate_unity_meta.py")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Missing metadata sidecar", result.stdout)

    def test_metadata_validator_reports_orphan_sidecar(self) -> None:
        (self.repo / "Assets").mkdir()
        self.write("Assets/Orphan.cs.meta", "fileFormatVersion: 2\nguid: " + "c" * 32 + "\n")
        result = self.run_script("examples/scripts/validate_unity_meta.py")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Orphan metadata file", result.stdout)

    def test_metadata_validator_reports_malformed_guid(self) -> None:
        self.write("Assets/Broken.cs", "class Broken {}")
        self.write("Assets/Broken.cs.meta", "fileFormatVersion: 2\nguid: not-a-guid\n")
        result = self.run_script("examples/scripts/validate_unity_meta.py")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("malformed 32-character GUID", result.stdout)

    def test_metadata_validator_reports_duplicate_guids(self) -> None:
        self.add_asset("Assets/A.cs", "d" * 32)
        self.add_asset("Assets/B.cs", "d" * 32)
        result = self.run_script("examples/scripts/validate_unity_meta.py")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Duplicate GUID", result.stdout)

    def test_source_validator_accepts_valid_tracked_json(self) -> None:
        self.write("config/settings.json", '{"enabled": true}')
        subprocess.run(["git", "add", "."], cwd=self.repo, check=True)
        result = self.run_script("examples/scripts/validate_source_syntax.py")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_source_validator_rejects_invalid_tracked_json(self) -> None:
        self.write("config/settings.json", '{"enabled": }')
        subprocess.run(["git", "add", "."], cwd=self.repo, check=True)
        result = self.run_script("examples/scripts/validate_source_syntax.py")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid JSON", result.stderr)

    def test_source_validator_detects_conflict_markers(self) -> None:
        self.write("src/example.cs", "<<<<<<< HEAD\nclass A {}\n=======\nclass B {}\n>>>>>>> branch\n")
        subprocess.run(["git", "add", "."], cwd=self.repo, check=True)
        result = self.run_script("examples/scripts/validate_source_syntax.py")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("merge-conflict marker", result.stderr)

    def test_source_validator_rejects_invalid_yaml_when_pyyaml_available(self) -> None:
        try:
            import yaml  # noqa: F401
        except ImportError:
            self.skipTest("PyYAML is not installed; CI installs the pinned dependency")
        self.write("config/broken.yml", "key: [unterminated")
        subprocess.run(["git", "add", "."], cwd=self.repo, check=True)
        result = self.run_script("examples/scripts/validate_source_syntax.py")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid YAML", result.stderr)


if __name__ == "__main__":
    unittest.main()
