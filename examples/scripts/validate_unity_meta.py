#!/usr/bin/env python3
"""Read-only checks for Unity .meta sidecars and GUID uniqueness under Assets/."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ASSETS = Path("Assets")
GUID_PATTERN = re.compile(r"^guid:\s*([0-9a-fA-F]{32})\s*$", re.MULTILINE)


def main() -> int:
    if not ASSETS.is_dir():
        print("SKIP: Assets/ directory not found.")
        return 0

    errors: list[str] = []
    seen_guids: dict[str, Path] = {}

    # Unity assigns metadata to folders as well as files. Check every filesystem
    # entry except .meta files themselves; this script never modifies the project.
    for entry in sorted(ASSETS.rglob("*")):
        if entry.name.endswith(".meta"):
            continue
        sidecar = entry.with_name(entry.name + ".meta")
        if not sidecar.is_file():
            errors.append(f"Missing metadata sidecar: {sidecar.as_posix()}")

    for meta_file in sorted(ASSETS.rglob("*.meta")):
        asset_path = Path(str(meta_file)[:-5])
        if not asset_path.exists():
            errors.append(f"Orphan metadata file with no matching asset/folder: {meta_file.as_posix()}")

        try:
            content = meta_file.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"Cannot read {meta_file.as_posix()}: {exc}")
            continue

        match = GUID_PATTERN.search(content)
        if not match:
            errors.append(f"Missing or malformed 32-character GUID: {meta_file.as_posix()}")
            continue

        guid = match.group(1).lower()
        previous = seen_guids.get(guid)
        if previous is not None:
            errors.append(
                f"Duplicate GUID {guid}: {previous.as_posix()} and {meta_file.as_posix()}"
            )
        else:
            seen_guids[guid] = meta_file

    if errors:
        print("Unity metadata validation failed:")
        for error in errors:
            print(f" - {error}")
        print(
            "Restore or repair metadata using Unity Editor/version control; "
            "do not generate replacement GUIDs blindly."
        )
        return 1

    print(f"Unity metadata validation passed ({len(seen_guids)} GUIDs checked).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
