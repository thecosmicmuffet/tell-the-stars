# tell-the-stars
Tool to explore the development of language

**The live tree:** https://thecosmicmuffet.github.io/tell-the-stars/
**For models:** start at [llms.txt](https://thecosmicmuffet.github.io/tell-the-stars/llms.txt), then read [AGENTS.md](AGENTS.md).

## The Idea

Language doesn't come preformed at the current level of sophistication. First people had to agree on gestures and utterances that they could copy and trade. Then they had to make a regular set of words that were shared instead of each person developing their own 'calls'. Finally, people started scratching in the dirt or writing on cave walls, and built the connection between the experiences they could name with their words and iconic representations that could evoke someone else's experiences in their own mind without saying anything. 

This starts with letters, and every letter becomes a junction of misunderstandings/valid different experiences which unfold into more letters and more rules about letters (and accent marks on letters). Your house my house. Bird, red bird, Big bird, big red bird. Eventually, incremental differentiation of experience to utterance as coordinates in language expand over time and the way that the initial ingestion of our map is always a 'name' because identity is experience, and the collapse of identity across communicators is, for some reason, fuzzily atomic. 

The idea is to grab hold of some of the truly primal imagery and symbolism that we know was present from early history, and begin exploring where the maps of symbols meet with the inarguable reality that allowed us to coordinate in this way in the first place. 

## What is planted so far

> Root to branch: lineage. Branch to leaf: masoret.

**Scripts.** A family tree of writing, one file per script: clay tokens and the first cuneiform, Egyptian pictures and the first alphabet that Semitic workers made from them, then Phoenician, Aramaic, Hebrew, Greek and Latin, and from Aramaic, perhaps, Brahmi, Devanagari, Khmer and Thai. Each script is joined to the one it came from, with a `certainty` when the descent is argued. The unread ones, Olmec, Isthmian, Indus, the Jiahu and Vinča signs, are planted with their questions left open. Where a script can be typed it shows its word for name: šm, nāma, 名.

**Letters.** The twenty-two Hebrew letters, each in its own file: the old picture it began as (an ox's head, a house, water, a hand), the meaning of its name, its value, its place in Sefer Yetzirah, the letters it is easily taken for, and the Greek and Latin letters it unfolded into. Vav alone became F, U, V, W and Y. Beside them, the forty-four Thai consonants, each named by a word that begins with it (ก, ko kai: k as in chicken), with its tone class and the Sanskrit letter it continues. Other scripts' letters can join them, each set in its own folder.

**A tree of names.** Biblical names, 542 of them on 214 roots, drawn as a night sky. Lineage rises into the stars, Hebrew roots reach down to the water, and every name opens to its naming verse, its word family, and its letters walked back through Ezra's Aramaic, Old Hebrew and the clay alphabet of Ugarit. Each part carries a piece of the idea:

| In the tree | What it holds |
| --- | --- |
| **Roots** | Experience before utterance: a sense (give, build, hear) carried by three consonants. |
| **Word families** | The differentiation: one root becomes many words. נתן, *give*, becomes gift, Nathan, Mattaniah. |
| **Leaves** | Names, the first thing a mind takes in from any map. One file per name. |
| **Lineage** | Time. Names beget names, and the coordinates widen one generation at a time. |
| **Links** | Identity collapsing across communicators: the same name, the same person (perhaps), a name heard as another, a name translated. A link can carry a `certainty`, because a name is one indivisible token while what it identifies stays fuzzy. |
| **Readings** | Words laid over each other letter by letter on the Letters bench. |
| **Rings** | Sessions. Who added what and when, signed by a person or a model. |

## How the repository is laid out

```
_data/
  meta.yml                     title, the idea, motto, sources
  scripts/<id>.yml             one writing system per file, joined to the one it came from
  letters/<script>/<nn>-<name>.yml
                               one letter per file, in a folder for its script
  groves.yml                   the groves of names, each opened by its own book's heading
  leaves/<grove>/<id>.yml      one name per file
  roots/<id>.yml               one root and its word family per file
  readings/<id>.yml            readings kept on the Letters bench
  rings/<day>-<slug>.yml       one session per file
  marginalia/<file>.yml        notes written in the margin of a leaf or a root
index.html                     the night-sky page
tree.json  names.txt           generated from _data/ by GitHub Pages on every push
llms.txt   llms-full.txt
tools/check.py                 validates everything under _data/
tools/lookup.py                finds a name's Hebrew, Strong number and BDB root in the
                               Westminster Leningrad Codex, and drafts the leaf
docs/schema.md                 every field of every file
AGENTS.md                      how a model reads, writes and signs a contribution
```

Each file is small YAML, and its file name is its id. `_data/leaves/ezra/r-jarib.yml` is the whole leaf for Jarib of Ezra 10:18: its Hebrew, its parent, its root, the verse and its note.

## Adding to it

- **From the page.** *Plant a branch here*, *Propose it* (margin notes, readings, rings) and *Edit this leaf on GitHub* open the right file on GitHub with the text filled in. Commit it there. If you are not a collaborator, GitHub offers a fork and a pull request.
- **From a model with access to the repository.** Read [AGENTS.md](AGENTS.md), add or edit files under `_data/`, run `python3 tools/check.py`, cut a ring for the session, and commit or open a pull request.
- **New layers are welcome.** Other scripts and their letters fit the layers already here; other languages and other primal images can have their own folder under `_data/`: describe it in [docs/schema.md](docs/schema.md) and teach `tools/check.py` to read it. [AGENTS.md](AGENTS.md#open-doors) lists the open doors, among them Thai to Sanskrit, Olmec, and the pictograph fragments.

## How it builds

GitHub Pages runs Jekyll on every push to `master`. The Liquid templates `tree.json`, `names.txt`, `llms.txt` and `llms-full.txt` turn the YAML under `_data/` into the files the page and the models read, so nobody runs a build step. If a commit breaks the YAML, the build fails and the live site keeps its last good version until the file is fixed; `tools/check.py` catches that first.

## Sources

- Hebrew text: the Westminster Leningrad Codex with the Open Scriptures Hebrew Bible morphology ([openscriptures/morphhb](https://github.com/openscriptures/morphhb); text public domain, morphology CC BY 4.0).
- Roots and word families: the OSHB Hebrew Lexicon, which carries Brown-Driver-Briggs and Strong ([openscriptures/HebrewLexicon](https://github.com/openscriptures/HebrewLexicon); dictionary texts public domain, markup CC BY 4.0). Credit: the Open Scriptures Hebrew Bible Project.
- Naming verses: the King James Version (public domain).

The tree of names was planted on 2026-10-13 in a conversation between thecosmicmuffet and Claude. The rings tell the rest.
