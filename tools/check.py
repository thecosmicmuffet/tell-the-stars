#!/usr/bin/env python3
"""Check the tree before committing.

    pip install pyyaml
    python3 tools/check.py

Errors (exit 1): unreadable YAML, a leaf with no name or a missing parent, the same id in two
groves, a cycle in the lineage, a link or margin note pointing at nothing, a malformed ring.
Warnings: an unusual kind, a reference not in OSIS form, a root named by consonants with no
root file yet, a ring listing ids that are not on the tree.
"""
import os
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit('tools/check.py needs PyYAML: pip install pyyaml')

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA = os.path.join(ROOT, '_data')
ID = re.compile(r'^[a-z0-9][a-z0-9-]*$')
OSIS = re.compile(r'^[1-3]?[A-Z][A-Za-z]+\.\d+\.\d+$')
HEB_LETTERS = re.compile(r'^[א-ת]+$')
KINDS = {'begat', 'son', 'of', 'house', 'people', 'course', 'wife', 'maid', 'built', 'housed', 'supposed'}
ROLES = {'root', 'pun', 'maybe'}

errors, warnings = [], []


def err(path, msg):
    errors.append(f'{os.path.relpath(path, ROOT)}: {msg}')


def warn(path, msg):
    warnings.append(f'{os.path.relpath(path, ROOT)}: {msg}')


def load(path):
    try:
        with open(path, encoding='utf-8') as f:
            data = yaml.safe_load(f)
    except Exception as e:  # noqa: BLE001
        err(path, f'not readable as YAML ({e.__class__.__name__}: {e})')
        return None
    if not isinstance(data, dict):
        err(path, 'must be a YAML mapping (key: value lines)')
        return None
    return data


def files(sub):
    base = os.path.join(DATA, sub)
    out = []
    for dirpath, _, names in os.walk(base):
        for n in sorted(names):
            if n.endswith(('.yml', '.yaml')):
                out.append(os.path.join(dirpath, n))
    return sorted(out)


def stem(path):
    return os.path.splitext(os.path.basename(path))[0]


def letters(s):
    return ''.join(ch for ch in str(s) if 'א' <= ch <= 'ת')


# ------------------------------------------------------------------ roots
roots = {}
by_cons = {}
for path in files('roots'):
    rid = stem(path)
    r = load(path)
    if r is None:
        continue
    if rid not in ('Y', 'E') and not ID.match(rid):
        err(path, 'file name must be lowercase letters, digits and hyphens')
    cons = r.get('cons')
    if not cons or not HEB_LETTERS.match(str(cons)):
        err(path, '`cons` must be Hebrew consonants without points')
    for i, f in enumerate(r.get('family') or []):
        if not isinstance(f, dict) or not f.get('w'):
            err(path, f'family entry {i + 1} needs at least `w`')
    roots[rid] = r
    by_cons.setdefault(str(cons), []).append(rid)

# ------------------------------------------------------------------ leaves
leaves, where = {}, {}
for path in files('leaves'):
    lid = stem(path)
    leaf = load(path)
    if leaf is None:
        continue
    if not ID.match(lid):
        err(path, 'file name must be lowercase letters, digits and hyphens')
    if lid in leaves:
        err(path, f'id `{lid}` is already used by {os.path.relpath(where[lid], ROOT)}')
    leaves[lid], where[lid] = leaf, path

for lid, leaf in leaves.items():
    path = where[lid]
    if not leaf.get('en'):
        err(path, '`en` (the name) is required')
    parent = leaf.get('parent')
    if lid != 'god':
        if not parent:
            err(path, '`parent` is required')
        elif parent not in leaves:
            err(path, f'parent `{parent}` is not on the tree')
    kind = leaf.get('kind')
    if kind and kind not in KINDS:
        warn(path, f'kind `{kind}` is not one of {", ".join(sorted(KINDS))}')
    ref = leaf.get('ref')
    if ref and not OSIS.match(str(ref)):
        warn(path, f'ref `{ref}` is not in OSIS form, like Gen.30.11')
    flags = str(leaf.get('flags') or '')
    if set(flags) - set('fgnu'):
        err(path, '`flags` may only contain f, g, n, u')
    for r in leaf.get('roots') or []:
        if isinstance(r, str):
            r = {'root': r}
        if not isinstance(r, dict):
            err(path, 'each root must be a mapping like {root: נתן}')
            continue
        role = r.get('role', 'root')
        if role not in ROLES:
            err(path, f'root role `{role}` must be pun or maybe (or left out)')
        rid = r.get('id')
        if rid:
            if rid not in roots:
                err(path, f'root id `{rid}` has no file in _data/roots/')
            elif r.get('root') and letters(r['root']) and roots[rid].get('cons') != letters(r['root']) and rid not in ('Y', 'E'):
                warn(path, f'root `{r.get("root")}` does not match the consonants of `{rid}` ({roots[rid].get("cons")})')
        else:
            c = letters(r.get('root', ''))
            if r.get('root') in ('יה', 'אל'):
                continue
            if not c:
                err(path, 'a root needs `root` (consonants) or `id`')
            elif c not in by_cons:
                warn(path, f'root `{c}` has no file in _data/roots/ yet')
            elif len(by_cons[c]) > 1:
                warn(path, f'root `{c}` matches {", ".join(by_cons[c])}; add `id` to choose')
    for k in leaf.get('links') or []:
        if not isinstance(k, dict) or not k.get('to'):
            err(path, 'each link needs `to`')
            continue
        if k['to'] not in leaves:
            err(path, f'link to `{k["to"]}` points at nothing')
        c = k.get('certainty')
        if c is not None and not (isinstance(c, (int, float)) and 0 <= c <= 1):
            err(path, '`certainty` must be a number from 0 to 1')

# cycles
for lid in leaves:
    seen, cur = set(), lid
    while cur and cur in leaves:
        if cur in seen:
            err(where[lid], f'lineage loops back on itself at `{cur}`')
            break
        seen.add(cur)
        cur = leaves[cur].get('parent')

# ------------------------------------------------------------------ readings, rings, margins
for path in files('readings'):
    r = load(path)
    if r is None:
        continue
    words = r.get('words')
    if not isinstance(words, list) or not words:
        err(path, '`words` must be a list of one to three words')
    if not r.get('title'):
        warn(path, '`title` is missing')

for path in files('rings'):
    r = load(path)
    if r is None:
        continue
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', str(r.get('day', ''))):
        err(path, "`day` must be a quoted date like '2026-10-15'")
    for f in ('title', 'by'):
        if not r.get(f):
            err(path, f'`{f}` is required')
    missing = [a for a in (r.get('added') or []) if a not in leaves]
    if missing:
        warn(path, f'`added` lists ids not on the tree: {", ".join(missing[:8])}')

for path in files('marginalia'):
    m = load(path)
    if m is None:
        continue
    t = str(m.get('target', ''))
    if not re.match(r'^[pr]:', t):
        err(path, '`target` must be p:<leaf id> or r:<root id>')
    elif t.startswith('p:') and t[2:] not in leaves:
        err(path, f'`target` {t} is not on the tree')
    elif t.startswith('r:') and t[2:] not in roots:
        err(path, f'`target` {t} is not a root file')
    for f in ('text', 'by'):
        if not m.get(f):
            err(path, f'`{f}` is required')

letters_seen = set()
for path in files('letters'):
    l = load(path)
    if l is None:
        continue
    ch = str(l.get('char', ''))
    if len(ch) != 1 or not HEB_LETTERS.match(ch):
        err(path, '`char` must be a single Hebrew letter')
    elif ch in letters_seen:
        err(path, f'letter {ch} has two files')
    letters_seen.add(ch)
    if not isinstance(l.get('value'), int):
        err(path, '`value` must be a whole number')
    for n in l.get('near') or []:
        if not isinstance(n, dict) or not n.get('char'):
            err(path, 'each `near` entry needs `char`')

for w in warnings:
    print('warning:', w)
for e in errors:
    print('error:  ', e)
print(f'\n{len(files("letters"))} letters, {len(leaves)} leaves, {len(roots)} roots, {len(files("readings"))} readings, '
      f'{len(files("rings"))} rings, {len(files("marginalia"))} margin notes: '
      f'{len(errors)} errors, {len(warnings)} warnings')
sys.exit(1 if errors else 0)
