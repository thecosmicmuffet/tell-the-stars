#!/usr/bin/env python3
"""Find a name in the Hebrew text and draft its leaf.

    python3 tools/lookup.py Lev.24.11
    python3 tools/lookup.py Lev.24.11 Shelomith --leaf --parent dibri --kind begat

REF is a verse in OSIS form with King James numbering (Gen.30.11, 1Chr.6.15). The tool reads
the Westminster Leningrad Codex with the Open Scriptures Hebrew Bible morphology and the OSHB
Hebrew Lexicon (Brown-Driver-Briggs and Strong), downloading what it needs once into
~/.cache/tell-the-stars (or $TELL_THE_STARS_CACHE). It lists every proper name in the verse
with its pointed Hebrew, transliteration, Strong number, lexicon gloss and BDB root, and the
King James text of the verse. With --leaf it prints a leaf to save as
_data/leaves/<grove>/<id>.yml; fill in the gloss and the note, and check the root.

Credit for the data: the Open Scriptures Hebrew Bible Project (CC BY 4.0 markup; the WLC,
BDB and Strong texts are public domain). The KJV text comes from github.com/thiagobodruk/bible.
"""
import argparse
import datetime
import difflib
import json
import os
import re
import sys
import unicodedata
import urllib.request
import xml.etree.ElementTree as ET

MORPHHB = 'https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/'
LEXICON = 'https://raw.githubusercontent.com/openscriptures/HebrewLexicon/master/'
KJV_URL = 'https://raw.githubusercontent.com/thiagobodruk/bible/master/json/en_kjv.json'
OSIS_NS = '{http://www.bibletechnologies.net/2003/OSIS/namespace}'
LEX_NS = '{http://openscriptures.github.com/morphhb/namespace}'
MAP_NS = '{http://www.APTBibleTools.com/namespace}'
BOOKS = ['Gen', 'Exod', 'Lev', 'Num', 'Deut', 'Josh', 'Judg', 'Ruth', '1Sam', '2Sam', '1Kgs', '2Kgs',
         '1Chr', '2Chr', 'Ezra', 'Neh', 'Esth', 'Job', 'Ps', 'Prov', 'Eccl', 'Song', 'Isa', 'Jer', 'Lam',
         'Ezek', 'Dan', 'Hos', 'Joel', 'Amos', 'Obad', 'Jonah', 'Mic', 'Nah', 'Hab', 'Zeph', 'Hag',
         'Zech', 'Mal']
CACHE = os.environ.get('TELL_THE_STARS_CACHE') or os.path.join(os.path.expanduser('~'), '.cache', 'tell-the-stars')
CANT = re.compile('[֑-ֽ֯׀׃׆͏‌‍]')


def fetch(url, name):
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, name)
    if not os.path.exists(path):
        sys.stderr.write(f'fetching {url}\n')
        with urllib.request.urlopen(url, timeout=60) as r, open(path + '.part', 'wb') as f:
            f.write(r.read())
        os.replace(path + '.part', path)
    return path


def clean(s):
    return CANT.sub('', s or '').replace('/', '').strip()


def cons(s):
    return ''.join(ch for ch in s if 'א' <= ch <= 'ת')


def norm(s):
    s = unicodedata.normalize('NFD', (s or '').lower())
    s = ''.join(ch for ch in s if unicodedata.category(ch) != 'Mn')
    s = re.sub(r'[^a-z]', '', s)
    for a, b in [('ph', 'f'), ('th', 't'), ('sh', 's'), ('ch', 'k'), ('ts', 's'), ('kh', 'k')]:
        s = s.replace(a, b)
    s = s.translate(str.maketrans('cjwzqx', 'kyvsks')).replace('h', '')
    return re.sub(r'(.)\1+', r'\1', s)


def kjv_to_wlc(ref):
    path = fetch(MORPHHB + 'VerseMap.xml', 'VerseMap.xml')
    for v in ET.parse(path).getroot().iter(MAP_NS + 'verse'):
        if v.get('kjv') == ref and v.get('type') == 'full':
            return v.get('wlc')
    return ref


def lexicon():
    li = {}
    for e in ET.parse(fetch(LEXICON + 'LexicalIndex.xml', 'LexicalIndex.xml')).getroot().iter(LEX_NS + 'entry'):
        w, x, d = e.find(LEX_NS + 'w'), e.find(LEX_NS + 'xref'), e.find(LEX_NS + 'def')
        li[e.get('id')] = {
            'w': clean(w.text if w is not None else ''), 'xlit': w.get('xlit') if w is not None else '',
            'def': d.text if d is not None else '', 'bdb': x.get('bdb') if x is not None else None,
        }
    aug = {w.get('aug'): w.text for w in ET.parse(fetch(LEXICON + 'AugIndex.xml', 'AugIndex.xml')).getroot().iter(LEX_NS + 'w')}
    sections = {}
    for sec in ET.parse(fetch(LEXICON + 'BrownDriverBriggs.xml', 'BrownDriverBriggs.xml')).getroot().iter(LEX_NS + 'section'):
        for e in sec.findall(LEX_NS + 'entry'):
            if e.get('type') == 'root':
                w = e.find(LEX_NS + 'w')
                defs = [d.text for d in e.iter(LEX_NS + 'def') if d.text][:2]
                sections[sec.get('id')] = {'cons': cons(clean(w.text if w is not None else '')),
                                           'mod': e.get('mod'), 'def': ', '.join(defs)}
                break
    return li, aug, sections


def kjv_text(ref):
    try:
        data = json.load(open(fetch(KJV_URL, 'en_kjv.json'), encoding='utf-8-sig'))
    except Exception:  # noqa: BLE001
        return None
    order = BOOKS + ['Matt', 'Mark', 'Luke', 'John', 'Acts', 'Rom', '1Cor', '2Cor', 'Gal', 'Eph', 'Phil', 'Col',
                     '1Thess', '2Thess', '1Tim', '2Tim', 'Titus', 'Phlm', 'Heb', 'Jas', '1Pet', '2Pet',
                     '1John', '2John', '3John', 'Jude', 'Rev']
    b, c, v = ref.split('.')
    try:
        return data[order.index(b)]['chapters'][int(c) - 1][int(v) - 1]
    except (ValueError, IndexError):
        return None


def names_in(wref, li, aug, sections):
    book = wref.split('.')[0]
    root = ET.parse(fetch(MORPHHB + book + '.xml', book + '.xml')).getroot()
    verse = next((v for v in root.iter(OSIS_NS + 'verse') if v.get('osisID') == wref), None)
    if verse is None:
        sys.exit(f'{wref} is not in the Westminster Leningrad Codex')
    found, pending = [], None
    for w in verse.iter(OSIS_NS + 'w'):
        morph, lemma, text = w.get('morph') or '', w.get('lemma') or '', w.text or ''
        segs_m, segs_l, segs_t = morph[1:].split('/'), lemma.split('/'), text.split('/')
        for i, m in enumerate(segs_m):
            if not (m.startswith('Np') or m.startswith('Ng')):
                continue
            a = (segs_l[i] if i < len(segs_l) else segs_l[-1]).replace(' ', '')
            heb = clean(segs_t[i] if i < len(segs_t) else segs_t[-1])
            if a.endswith('+'):
                pending = heb
                continue
            if pending:
                heb, pending = pending + '־' + heb, None
            lid = aug.get(a) or aug.get(re.sub(r'[a-z]$', '', a))
            e = li.get(lid or '', {})
            sec = '.'.join((e.get('bdb') or '').split('.')[:2])
            found.append({'heb': heb, 'strong': re.sub(r'[a-z]$', '', a), 'li': lid, 'xlit': e.get('xlit', ''),
                          'def': (e.get('def') or '').split('.')[0], 'section': sec, 'root': sections.get(sec)})
    return found


def main():
    ap = argparse.ArgumentParser(description='Find a name in the Hebrew text and draft its leaf.')
    ap.add_argument('ref', help='verse in OSIS form, KJV numbering: Gen.30.11')
    ap.add_argument('name', nargs='?', help='the name as the KJV spells it')
    ap.add_argument('--leaf', action='store_true', help='print a leaf for the best match')
    ap.add_argument('--parent', default='', help='parent id for --leaf')
    ap.add_argument('--kind', default='begat', help='how it joins its parent, for --leaf')
    ap.add_argument('--by', default='', help='who is planting it, for --leaf')
    args = ap.parse_args()

    if not re.match(r'^[1-3]?[A-Z][A-Za-z]+\.\d+\.\d+$', args.ref):
        sys.exit('REF must look like Gen.30.11')
    if args.ref.split('.')[0] not in BOOKS:
        sys.exit('lookup.py reads the Hebrew Bible; New Testament names are written by hand')
    wref = kjv_to_wlc(args.ref)
    li, aug, sections = lexicon()
    found = names_in(wref, li, aug, sections)
    verse = kjv_text(args.ref)
    print(f'{args.ref}' + (f' (Hebrew {wref})' if wref != args.ref else ''))
    if verse:
        print(f'KJV: {verse}')
    print()
    if not found:
        print('No proper names are tagged in this verse.')
        return
    print(f"    {'name in the lexicon':<18} {'Hebrew':<14} {'sound':<16} {'Strong':<13} BDB root (the section it is filed under; check it)")
    for i, f in enumerate(found, 1):
        r = f['root']
        rtxt = f"{r['cons']}{' ' + r['mod'] if r and r.get('mod') else ''} ({r['def']})" if r else 'no BDB root'
        print(f"{i:>2}. {f['def'] or '?':<18} {f['heb']:<14} {f['xlit']:<16} Strong {f['strong']:<6} root {rtxt}")

    if args.name:
        def score(f):
            return max(difflib.SequenceMatcher(None, norm(args.name), norm(f['def'])).ratio(),
                       difflib.SequenceMatcher(None, norm(args.name), norm(f['xlit'])).ratio())
        best = max(found, key=score)
        print(f"\nbest match for {args.name}: {best['def']} {best['heb']} ({score(best):.2f})")
    else:
        best = found[0]

    if args.leaf:
        r = best['root']
        leaf = {
            'en': args.name or best['def'],
            'heb': best['heb'],
            'xlit': best['xlit'],
            'gloss': '',
            'parent': args.parent,
            'kind': args.kind,
            'ref': args.ref,
        }
        if wref != args.ref:
            leaf['wref'] = wref
        lines = [f'{k}: {json.dumps(v, ensure_ascii=False)}' for k, v in leaf.items()]
        if r and r['cons']:
            rid = 'r-' + best['section'].replace('.', '-')
            lines.append(f"roots:\n- {{root: {r['cons']}, id: {rid}}}   # check: BDB files it under {r['cons']} ({r['def']})")
        lines.append(f"strong: '{best['strong']}'")
        if best['li']:
            lines.append(f"li: {best['li']}")
        if verse:
            lines.append(f"naming:\n- {{ref: {args.ref}, text: {json.dumps(verse, ensure_ascii=False)}}}   # keep only if the verse gives the reason for the name")
        lines.append('note: >-\n  ')
        lines.append(f'by: {json.dumps(args.by)}')
        lines.append(f"at: '{datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')}'")
        print('\n# save as _data/leaves/<grove>/<id>.yml, then write the gloss and the note\n' + '\n'.join(lines))


if __name__ == '__main__':
    main()
