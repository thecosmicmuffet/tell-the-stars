# Schema

Every file under `_data/` is YAML. A file's name, without `.yml`, is its id: lowercase `a-z`, `0-9` and hyphens (the root ids `Y` and `E` are the two exceptions). Fields not listed here are kept but not shown.

## Script: `_data/scripts/<id>.yml`

One writing system, or one system of signs that may or may not be writing. Scripts form their own lineage: `parent` is the script a script came from.

| Field | Required | Meaning |
| --- | --- | --- |
| `name` | yes | The script's name in English. |
| `kind` | | `alphabet`, `abjad` (consonants only), `abugida` (consonants carrying vowel marks), `syllabary`, `logo-syllabic`, `logo-consonantal`, `logographic`, `featural`, `symbols` (signs that may not write a language), `counters`, or `unknown`. |
| `status` | | `living` (in use), `read` (no longer used, but read), `partly read`, or `unread`. |
| `parent` | | The id of the script it came from. Leave it out when no ancestor is known. |
| `certainty` | | How sure the join to `parent` is, from 0 to 1. Left out when the join is plain fact. |
| `links` | | Other joins: a list of `{to, kind, certainty}`, such as `{to: cuneiform, kind: wedges from}` or `{to: chinese, kind: signs like, certainty: 0.1}`. |
| `year` | yes | The earliest writing in it, as a whole number, negative for BCE. Approximate; it orders the tree. |
| `when` | | The dates in words, as precise as the evidence allows: `c. 1400–1190 BCE`. |
| `place` | | Where it was written. |
| `dir` | | `ltr`, `rtl`, `ttb` (top to bottom), `boustrophedon`, or `any`. |
| `unicode` | | Its Unicode block, if it has one. |
| `font` | | A Google Fonts family that can show the sample: `Noto Sans Brahmi`. |
| `sample` | | A word written in it, as Unicode text: `{text, says}`. By custom the word for name, where the script can be typed. |
| `note` | | Where it came from and what it carries, cited. |
| `open` | | Questions it leaves open for the next mind: a list of plain sentences. |
| `by`, `at` | for new scripts | Who planted it and when (ISO 8601). |

## Letter: `_data/letters/<script>/<nn>-<name>.yml`

Each script's letters live in a folder named for the script's id: `_data/letters/hebrew/01-alef.yml`. The two-digit prefix keeps the files in alphabet order. Only `char` is required; the other fields are filled as far as they apply to the script.

| Field | Meaning |
| --- | --- |
| `char`, `final` | The letter, and its form at the end of a word if it has one. |
| `position`, `value` | Place in the alphabet, and value when counted. |
| `name`, `name_heb` | The letter's name, in English letters and in Hebrew. |
| `picture` | What the oldest sign shows. A `?` marks a guess. |
| `meaning` | What the name means. |
| `sefer_yetzirah` | Mother (with its element), double, or simple. |
| `greek`, `latin` | The letters it became. |
| `near` | Letters it is easily taken for: a list of `{char, note}`. |
| `note` | What the letter carries, cited. |

Fields the Thai letters add, which other scripts can use where they fit:

| Field | Meaning |
| --- | --- |
| `name_native` | The letter's name in its own script: `ก ไก่`. |
| `meaning` | For a Thai letter, what its name-word means: `chicken`. |
| `class` | The Thai tone class: `mid`, `high` or `low`. |
| `sound`, `ipa` | The sound at the start of a syllable, romanized and in IPA. |
| `final_sound` | The sound at the end of a syllable, if the letter can end one. |
| `sanskrit` | The Sanskrit or Pali letter it continues, in Devanagari with its transliteration: `ग ga`. |
| `obsolete` | `true` for a letter no longer used. |

Describe new fields here when you add them.

## Leaf: `_data/leaves/<grove>/<id>.yml`

| Field | Required | Meaning |
| --- | --- | --- |
| `en` | yes | The name as the King James Version spells it. |
| `heb` | | The pointed Hebrew (Westminster Leningrad Codex), or a Hebrew/Aramaic form for New Testament names. |
| `xlit` | | Transliteration. |
| `greek` | | The Greek form, for New Testament names. |
| `forms` | | Other forms across languages: a list of `{lang, text}` (`lang` as a BCP 47 code: `grc`, `la`, `arc`, `akk`, `non`...). |
| `gloss` | | What the name means. A `?` marks uncertainty. |
| `parent` | yes, except `god` | The id of the leaf this one branches from. |
| `kind` | | How it is joined to its parent: `begat`, `son` (son or daughter of), `of`, `house` (of the house of), `people` (of the people of), `course` (priestly family of), `wife`, `maid`, `built`, `housed`, `supposed` (son, as was supposed, of). |
| `ref` | | The verse, OSIS form with KJV numbering: `Gen.30.11`, `1Chr.2.3`, `Acts.13.9`. |
| `wref` | | The Hebrew-Bible verse number when it differs from the KJV's (`1Chr.5.41` for KJV `1Chr.6.15`). |
| `order` | | Sorts siblings; lower comes first (birth order). Optional. |
| `flags` | | Letters: `f` a woman, `g` a house or group, `n` a people, `u` unnamed in the text. |
| `roots` | | A list of `{root, id, role}`. `root` is the consonants (`נתן`; `יה` for Yah, `אל` for El); `id` names the root file and is needed only when consonants are shared; `role` is `pun` (wordplay) or `maybe`, and is left out for an ordinary root. |
| `aliases` | | Other names: a list of `{en, heb, ref, by, note}`. `by` is who gave the name (Pharaoh, the prophet, herself). |
| `naming` | | Verses that give the reason for the name: a list of `{ref, text}`, quoted from the KJV. |
| `kq` | | Written and read (ketiv/qere): `{k, q, ref, note}`. |
| `links` | | Joins beyond the parent: a list of `{to, kind, certainty}`. See below. |
| `years` | | `{beget, total}`: age at begetting the named son and years lived (Masoretic numbers). |
| `strong`, `li` | | Strong number and OSHB Lexical Index id. |
| `note` | | The masoret: what the name carries, cited. |
| `by`, `at` | for new leaves | Who planted it (a handle, or `model/instance`) and when (ISO 8601). |

### Links and the certainty of identity

`links` holds the joins that are not the parent edge. Family joins: `mother`, `wife of`, `adopted by`, `nursed by`, `cousin of`, `son-in-law of`, `mother's father`, `son of` (a second genealogy), `from the people of`. Identity joins: `same name as`, `same person as`, `heard as`, `translated as`, `name from`. Resonances: anything else, in plain words (`purple and trade, as in`, `not related to`).

`certainty` runs from 0 to 1 and is left out when the join is plain fact. The page marks any link under 1 with a `?`.

## Root: `_data/roots/<id>.yml`

| Field | Meaning |
| --- | --- |
| `cons` | The consonants, without points: `נתן`. |
| `w` | The root as Brown-Driver-Briggs heads it: `נָתַן`. |
| `def` | Its sense in a few words. |
| `homonym` | `I`, `II`, `III` when BDB separates roots with the same consonants. |
| `bdb` | BDB section id in the OSHB lexicon (`n.gg`). Planted roots use ids `r-<section>` with the dot as a hyphen. |
| `element` | `true` for Yah (`Y`) and El (`E`), the two elements of the Name. |
| `note` | What the root carries. |
| `family` | The word family: a list of `{w, x, p, d, r, li}`: word, transliteration, part of speech, meaning, first reference, Lexical Index id. |

## Reading: `_data/readings/<id>.yml`

`title`, `words` (one to three Hebrew words, pointed or not), `note`, `by`, `at`.

## Ring: `_data/rings/<YYYY-MM-DD>-<slug>.yml`

`day` (`YYYY-MM-DD`, quoted), `title`, `summary`, `by`, and `added`: the ids planted or changed in that session (leaves, roots, scripts or readings).

## Margin note: `_data/marginalia/<file>.yml`

`target` (`p:<leaf id>` or `r:<root id>`), `text`, `by`, `at`.

## Meta and groves

`_data/meta.yml` holds the title, motto, the frame (`thesis`, `thesis_by`), the epigraph verse, `repo`, `branch` and the sources. `_data/groves.yml` lists the groves in order, each with `id`, `label`, the `heading` its own book gives it, and that heading's `ref`.
