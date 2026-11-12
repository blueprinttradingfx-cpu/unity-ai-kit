#!/usr/bin/env python3
"""Validate tracked source/config syntax without launching the Unity Editor.

Unity YAML scene/prefab/asset files are intentionally not parsed as generic YAML:
Unity uses tagged multi-document YAML. Their integrity belongs to Unity Editor
import/compile and the dedicated .meta validator.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

JSON_SUFFIXES = {".json", ".asmdef", ".asmref"}
YAML_SUFFIXES = {".yml", ".yaml"}
PYTHON_SUFFIXES = {".py"}
JAVASCRIPT_SUFFIXES = {".js", ".mjs"}
TEXT_CHECK_SUFFIXES = {
    ".cs", ".json", ".asmdef", ".asmref", ".yml", ".yaml", ".py",
    ".js", ".mjs", ".sh", ".csproj", ".props", ".targets",
    ".unity", ".prefab", ".asset", ".meta",
}
CONFLICT_MARKERS = re.compile(r"^(<<<<<<<|=======|>>>>>>>)", re.MULTILINE)


def tracked_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z"], check=True, capture_output=True
    )
    return [Path(item.decode("utf-8")) for item in result.stdout.split(b"\0") if item]


def main() -> int:
    files = tracked_files()
    errors: list[str] = []
    counts = {"json": 0, "yaml": 0, "python": 0, "javascript": 0, "conflict": 0}

    for path in files:
        suffix = path.suffix.lower()
        if suffix in JSON_SUFFIXES:
            counts["json"] += 1
            try:
                json.loads(path.read_text(encoding="utf-8-sig"))
            except (OSError, UnicodeError, json.JSONDecodeError) as exc:
                errors.append(f"{path}: invalid JSON: {exc}")
        elif suffix in YAML_SUFFIXES:
            counts["yaml"] += 1
            try:
                import yaml
                list(yaml.safe_load_all(path.read_text(encoding="utf-8-sig")))
            except ImportError:
                errors.append("PyYAML is required (install the pinned CI dependency)")
                break
            except (OSError, UnicodeError, yaml.YAMLError) as exc:
                errors.append(f"{path}: invalid YAML: {exc}")
        elif suffix in PYTHON_SUFFIXES:
            counts["python"] += 1
            try:
                compile(path.read_text(encoding="utf-8-sig"), str(path), "exec")
            except (OSError, UnicodeError, SyntaxError) as exc:
                errors.append(f"{path}: Python syntax error: {exc}")
        elif suffix in JAVASCRIPT_SUFFIXES:
            counts["javascript"] += 1
            result = subprocess.run(
                ["node", "--check", str(path)], capture_output=True, text=True
            )
            if result.returncode:
                errors.append(f"{path}: JavaScript syntax error: {result.stderr.strip()}")

        if suffix in TEXT_CHECK_SUFFIXES:
            try:
                content = path.read_text(encoding="utf-8-sig")
            except (OSError, UnicodeError):
                continue
            if CONFLICT_MARKERS.search(content):
                counts["conflict"] += 1
                errors.append(f"{path}: possible merge-conflict marker found")

    print(
        "Checked syntax: "
        + ", ".join(f"{name}={count}" for name, count in counts.items())
    )
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"FAIL: {len(errors)} issue(s)")
        return 1

    print("PASS: tracked source/config syntax and conflict-marker checks")
    print("NOTE: C# compilation is performed by Unity Editor CI, not this script.")
    print("NOTE: Unity .unity/.prefab/.asset YAML is intentionally not parsed generically.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
