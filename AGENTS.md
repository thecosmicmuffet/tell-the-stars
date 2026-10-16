# For minds that contribute

This file is for any model or agent adding to the tree: Claude, GPT, Grok, Qwen, or one you run yourself. People are welcome to follow it too.

## What this is

A tool to explore the development of language. The README's **The Idea** is the brief, in the words of the person who planted it: from shared calls, to scratches in the dirt, to letters, each letter a junction of different experiences that unfolds into more letters and more rules. Two layers are planted so far: the twenty-two letters (`_data/letters/`) and a tree of biblical names (`_data/leaves/`, `_data/roots/`). New layers are welcome.

## Read first

1. `names.txt` on the live site, or `_data/leaves/` here. Every map is first ingested as a name, so begin with the list of names. Then `_data/letters/`, where it all starts.
2. [docs/schema.md](docs/schema.md) for every field.
3. One or two existing leaves near where you want to work. `_data/leaves/ezra/r-jarib.yml` and `_data/leaves/apostles/barnabas.yml` show most of the fields.

The live site serves the whole tree in three shapes: `llms-full.txt` (plain text), `tree.json` (what the page reads) and `names.txt` (one line per name).

## The shape of a contribution

- **One file per thing.** A leaf, a root, a reading, a ring or a margin note is each its own YAML file under `_data/`. The file name is the id: lowercase `a-z`, `0-9` and hyphens.
- **Leaves** go in `_data/leaves/<grove>/<id>.yml`, in the same grove as their parent. A name with no grove yet goes in `_data/leaves/planted/`.
- **Sign everything new** with `by` (a person's handle, or `model/instance` such as `claude`, `gpt/<instance>`, `grok`, `qwen/<instance>`) and `at` (an ISO 8601 time).
- **Cut a ring** for each session that adds something: `_data/rings/<YYYY-MM-DD>-<slug>.yml` with `day`, `title`, `summary`, `by`, and `added` (the ids you planted or changed).

## Evidence first

- Quote the naming verse from the King James Version, with its reference in OSIS form (`Gen.30.11`, `1Chr.2.3`). Use KJV verse numbering in `ref`.
- Take the Hebrew from the Westminster Leningrad Codex. `python3 tools/lookup.py <ref> <name> --leaf` finds the pointed form, transliteration, Strong number and Brown-Driver-Briggs root, and drafts the leaf for you.
- Mark uncertainty where it lives: a `?` in a gloss (`watchful?`), `role: maybe` on a root, `certainty` on a link. If an etymology is popular rather than philological, say so in the note.
- Do not invent a reference, a quotation or a manuscript. If you cannot check something, leave it out or mark it uncertain.

## Identity is fuzzily atomic

Two names can be one token and still not one identity. Say which kind of sameness you mean:

| `kind` | Meaning |
| --- | --- |
| `same name as` | The same name worn by different people (Jeshua the priest, Jesus). |
| `same person as` | Probably one person under two records. Add `certainty` (0 to 1). |
| `heard as` | One name heard as another ("Eli" heard as "Elias", Matt 27:47). |
| `translated as` | One name carried into another language (Thomas, Didymus). |
| `name from` | A name that may preserve another (Barnabas from Nebo?). Add `certainty`. |

Family links (`mother`, `wife of`, `adopted by`, `nursed by`) and resonances (`purple and trade, as in`) use the same `links` list.

## Writing notes

The `note` on a leaf is its masoret: what the name carries, in a few plain, cited sentences. Write from the text: the verse, the root, the names around it. Then stop. Do not rewrite another contributor's note. To add, disagree or extend, write a margin note in `_data/marginalia/`, or add a signed paragraph that begins with your `by`.

## Before you commit

```
pip install pyyaml
python3 tools/check.py
```

Fix every error. Warnings, such as a root named by consonants that has no file yet, can stay. Then commit with a message that says what grew: `Plant Shelomith and Dibri (Lev 24:11)`, `Note on r-jarib`, `Ring: letters and sounds`. The site rebuilds itself from `master`; nothing generated is checked in.

## A leaf, whole

```yaml
en: Jarib
heb: יָרִיב
xlit: yārîb
gloss: he contends, pleads
parent: jeshua
kind: house
ref: Ezra.10.18
roots:
- {root: ריב, id: r-t-cm}
strong: '3402'
note: >-
  Yariv, he contends, he pleads a case: Joiarib with the Name left off (Ezra 8:16 has
  both forms). The first priestly lot fell to Jehoiarib (1 Chr 24:7).
by: claude
at: '2026-10-13T00:00:00Z'
```

A root can be named by its consonants alone (`- {root: נתן}`). The page finds the matching root file, and `tools/check.py` warns when there is none. Add `id` when two roots share consonants (`עזר` help, `r-p-bz`, against its homonym).
