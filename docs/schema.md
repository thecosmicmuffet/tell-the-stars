# Schema

Every file under `_data/` is YAML. A file's name, without `.yml`, is its id: lowercase `a-z`, `0-9` and hyphens (the root ids `Y` and `E` are the two exceptions). Fields not listed here are kept but not shown.

## Letter: `_data/letters/<nn>-<name>.yml`

The two-digit prefix keeps the files in alphabet order.

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

`day` (`YYYY-MM-DD`, quoted), `title`, `summary`, `by`, and `added`: the ids planted or changed in that session.

## Margin note: `_data/marginalia/<file>.yml`

`target` (`p:<leaf id>` or `r:<root id>`), `text`, `by`, `at`.

## Meta and groves

`_data/meta.yml` holds the title, motto, the frame (`thesis`, `thesis_by`), the epigraph verse, `repo`, `branch` and the sources. `_data/groves.yml` lists the groves in order, each with `id`, `label`, the `heading` its own book gives it, and that heading's `ref`.
