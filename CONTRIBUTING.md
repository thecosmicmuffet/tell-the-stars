# Contributing

Anyone may propose a name, a root, a reading, a ring or a note in the margin. Models are welcome; see [AGENTS.md](AGENTS.md).

## The easy way: from the page

Open the live tree, tap a name, and use **Plant a branch here**, **Edit this leaf on GitHub**, or the **Propose it** buttons under Marginalia, the Letters bench and Rings. Each opens the right file on GitHub with the text filled in. Commit it. If you are not a collaborator, GitHub forks the repository for you and opens a pull request.

## The direct way: files

1. Add or edit YAML under `_data/` ([docs/schema.md](docs/schema.md) lists every field).
2. `pip install pyyaml && python3 tools/check.py`.
3. Add a ring in `_data/rings/` if you planted or changed something.
4. Open a pull request.

## What gets merged

Cited, careful work. A naming verse quoted from the King James Version with its reference; Hebrew from the Westminster Leningrad Codex; uncertainty marked where it lives. Disagreement goes in the margin, signed, rather than over someone else's note.
