# CLAUDE.md

Read [AGENTS.md](AGENTS.md): it is the contract for every model that adds to this tree, Claude included.

For Claude in particular:

- The tree is data under `_data/`. Nothing here needs building; GitHub Pages turns it into `tree.json`, `names.txt`, `llms.txt` and `llms-full.txt` on every push to `master`.
- Run `python3 tools/check.py` before committing, and `python3 tools/lookup.py <ref> <name> --leaf` to draft a leaf from the Westminster Leningrad Codex.
- Sign new files `by: claude` and cut a ring for the session in `_data/rings/`.
- Work on a branch and open a pull request unless thecosmicmuffet asks you to commit to `master`.
