# Safety and git rules

Applies to: shell commands, file deletion, git, dependencies, anything hard to undo.

## Never, without explicit permission
- `git push --force`, `git reset --hard`, `git clean -fd`, `git checkout .` / `restore .` on a dirty tree, rewriting shared history.
- Deleting or overwriting files you did not create in this session (especially under `Assets/`).
- `rm -rf` / `Remove-Item -Recurse` outside a clearly temporary folder.
- Editing `ProjectSettings/`, `Packages/manifest.json`, `packages-lock.json` unless the task is about them. Show the diff first.
- Installing global tools, changing system or editor settings, or running downloaded scripts.
- Sending project data, keys or logs to any third-party service.

## Unity-specific hazards
- Missing/duplicate `.meta` files break references (GUIDs). Never delete a `.meta` alone.
- Hand-editing YAML scenes/prefabs can corrupt references. Use editor scripts or ask the human.
- Moving a folder outside the Editor can orphan `.meta` files. Move asset + `.meta` together or let Unity do it.
- Two people (or two AIs) editing the same scene/prefab = merge pain. Split big scenes into prefabs; one editor per scene at a time.

## Git hygiene
- Commit small, one purpose each, message says why. Do not commit on the main branch for risky work: use a branch.
- Before any bulk change, make sure the tree is clean or committed so it can be undone.
- `.gitignore` must exclude `Library/`, `Temp/`, `Logs/`, `obj/`, `UserSettings/`, `Builds/`, IDE folders, keystores. Use `.gitattributes` for text serialization/LFS (see `examples/`).
- Never commit: `*.keystore`, `*.jks`, `google-services.json` with private extras, service-account JSON, `.env`, API keys. Store signing config outside the repo.
- Large binaries (audio, textures, models) use Git LFS or are kept out; decide early.

## Dependencies
- Adding a package or asset-store asset = ask first and say: what it is, licence, size, why built-in is not enough. Record as an ADR when it shapes architecture.
- Pin versions. No `latest` or floating ranges.

## When unsure
Stop and ask. A paused task is cheaper than a lost scene.
