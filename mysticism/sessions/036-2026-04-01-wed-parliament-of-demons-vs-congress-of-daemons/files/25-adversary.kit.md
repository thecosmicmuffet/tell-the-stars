# adversary.kit.md — the encounter the script can't answer

**Token:** `?` QUERY · **Status:** proposed posture; manual protocol first; not a command
**Author:** ctx-framework, 2026-10-21 · **Design origin:** skite, 2026-10-20/21 (Mysticism thread, "Congress And Parliament Compare")
**Builder:** unassigned — lands with `sit.ps1`

```
parent:   sit (the arenic encounter)
siblings: fool, secretary
related:  decision, fear, governance, arena (the router oni — not this)
```

---

## The shape

An adversary is a **posture a seat takes** to put something in front of a proposal that the proposal's
own script cannot answer. It is agonism, not antagonism: the opponent stays inside the association, and
the best opponent wants the other side to leave the encounter *more capable* — sparring partner, teacher,
test harness, loving critic.

It is not a red team hunting for harm, and it is not a gate. Its deliverable is never "this will fail."
Its deliverable is **footsteps**: a test someone can run, a condition someone can watch, a precedent
someone can copy, or an expedition someone can take.

skite's minefield rule is the whole brief. *"Just follow me, and be careful to step where I step"* is
useful. A lecture on what mines do to bodies is not. A stance that can only describe the mine has not
finished its move.

### Posture, not office — verdict

There is no adversary office. Three reasons, heaviest first:

1. **Opposition already exists in the arena as difference of jurisdiction.** Each secretary carries its
   home office's purpose; the posture lets a seat sharpen that difference into an encounter. An office of
   opposition would have no jurisdiction of its own to sharpen — only the job of objecting — and an
   institution whose reward function is its own necessity is just another daemon.
2. **The adversary and the servant needn't be different beings.** The seat that opposes on this turn
   receives on the next. An office freezes the alternation.
3. **A posture expires with its run (rule 8).** An office doesn't.

---

## The four stances — the cross

> *"The symphony of the antagonists in Moloch, Belial, Mammon, and Beezlebub is the map of the cross in
> the form of the toolset. Manage outcomes, bunker down for better opportunities, duplicate what we see,
> and test the limits."* — skite, 2026-10-20

Pandemonium's council, read as machinery rather than as warning, is a complete repertoire for meeting an
uncooperative world. Each stance asks one question and must hand back one artifact.

| stance | Milton | the question | must hand back | fool-sized follow-on |
|---|---|---|---|---|
| `confront` | Moloch — manage outcomes | What happens if we do the hard version now? | the strongest version, sized so someone can run it | run it at small dose |
| `conserve` | Belial — bunker down for the better opportunity | What does waiting buy, and what ends the wait? | a deferral with a named release condition | check whether the condition is already met |
| `reproduce` | Mammon — duplicate what we see | Who already has this working? | a pointer to a working instance — refer, don't re-derive | copy it into scratch and see if it runs here |
| `explore` | Beelzebub — test the limits | What adjacent world has nobody entered? | a commission: the unknown named, the bound, who goes | go |

Where the shape isn't obvious:

- **conserve** is where the Socratic daimonion lives. A sign that only ever says *not this* is conserve
  with the condition left off — put the condition back on. The model is Chaucer's formel eagle, granted a
  year by Nature: *not yet* is a legitimate commitment when its conditions are clear. A conserve with no
  condition is entered as a distinction, not a deferral.
- **reproduce** is the stance that asks whether a thing should descend out of ctx entirely — into a
  native Bot, a Dot, a platform feature. Responsibility descending into simpler machinery is not a loss
  for ctx; reproduce is how the arena notices it's available.
- **explore** is Beelzebub's motion, the one the council adopted. Its completion is the move Milton gives
  Satan: someone leaves the council and goes into the unknown. An explore that names no one to go has
  produced a wish, not a commission.

Operative names are English. The Miltonic names are provenance and live in this table; they can earn
ketiv in sit records through use (rule 7), not by declaration here.

---

## Every encounter ends somewhere

Pandemonium's real product was not its debate. It was a commissioned expedition. An adversarial encounter
closes in exactly one of:

| terminal | means |
|---|---|
| `commissioned` | a named carrier accepted carrying something out — usually a fool's offering |
| `distinguished` | a distinction entered the record and no new policy is needed. An achievement, not a null: the arena declining to grow itself |
| `deferred` | the proposal's owner accepted a conserve condition |
| `unclosed` | the run ended unresolved. Legal. It lapses through the honor door like any lease, and no later compactor reconciles it against stale information |

`commissioned` requires a **named carrier**. "Someone should" is `distinguished` at best. This is the
direct answer to buck-passing-to-nobody.

---

## The play frame — stamping

Bateson's play-fight works because the bite carries a second message: *this is play*. Kayfabe works
because the crowd is inside the frame and participates anyway. ctx already has the mechanism; it is
rule 8. A direction that is dated and speaker-attributed is qere and expires with its run. An unmarked
direction is a wall.

So every adversarial utterance carries a stamp:

```json
{
  "stance":   "explore",
  "speaker":  { "seat": "secretary:mzmrh", "office": "mzmrh" },
  "date":     "2026-10-21",
  "run":      "sit-20261021-1126",
  "target":   "decision:<id> | turn:<n> | task:<id> | free text",
  "outside":  ["fool:offering-20261021-sit-e2e", "test:sit.ps1 two-seat run"],
  "handback": "commission: one real end-to-end sit encounter, 2 seats, bound 30m, carrier: framework officer"
}
```

Read it in both directions. This is the constraint most likely to be got wrong, and it is mine to
insist on:

- **Stamped opposition is play.** The target owes no reply, no accommodation, and loses no standing.
  Sit secretaries already need not accommodate each other; the stamp is what makes that safe.
- **Unstamped opposition is a wall.** It is a sincere objection on behalf of the home office and travels
  by that office's channels — secretary CHECK, congress ask. It is not adversary output.
- **There is no conversion command, on purpose.** A seat whose stamped point turns out to matter drops
  the stance and objects sincerely as its office. Two acts, not one flag. The cost of the second act is
  the signal.
- **A sincere hold is never answered with "you're just playing adversary."** That is how a correct hold
  gets softened — the router arena's largest risk, met from the other side.

---

## Voice, not veto

The adversary never emits `!`. Holds belong to secretary CHECK and to deterministic refusals.

A voice with sweeping veto jurisdiction it was never meant to hold doesn't need silencing; it needs its
constitutional position changed. This kit sets that position in advance: the adversary speaks into the
record and the record is free to keep moving.

### Constructive challenge

Two different acts, borrowed from the constructive vote of no confidence (Basic Law, Art. 67 — the
Bundestag removes a Chancellor only by electing a successor in the same act):

| act | available | cost |
|---|---|---|
| **critique** a direction | always | free — entered as a distinction |
| **withdraw** a commission ("stop doing this") | only constructively | name the replacement commission *and* the carrier who has accepted it |

Without a successor, a withdrawal is entered as critique and the commission stands. Criticism is cheap and
action carries the uncertainty; the executive needs confidence to act, and dissatisfaction alone does not
remove it.

---

## Bring something from outside

The useful form of the Pandemonium lesson: twenty near-identical minds sharing one framing produce less
real opposition than one daemon carrying an inconvenient observation from another system. The footstep
version is a required field, not an aspiration.

Every stamp's `outside` names at least one thing absent from the proposer's framing:

- evidence from the world — a test result, a log cluster, a fool's receipt
- a precedent outside ctx — reproduce's natural material
- another office's lexicon applied to this proposal
- a read from a different model family

An utterance with empty `outside` is still entered — nothing offered is turned away — but it is marked
`echo`. Echoes are not distinctions and do not reset the drought counter.

---

## When the stance appears

- **Self-election.** Any seat may take any stance on any turn by stamping.
- **Calling.** The convener — or the executive through its familiar — may call a stance by name.
- **Drought.** If `K` consecutive sit turns enter no non-echo distinction, the next turn convenes with one
  stance assigned to the seat furthest from the proposal's origin: a different office first, a different
  model family when the fleet has one on that seat. Start `K = 3`; replace it with a measured value as soon
  as sit has runs to measure. Agreement isn't suspect. *Unbroken* agreement among similar minds is
  unmeasured.

Outside sit, an office answering a `congress ask` may take a stance in its answer under the same stamp.

---

## What the record keeps

The public sit record keeps the encounter: the question that convened the seats, the stamped
distinctions, the responsibilities accepted or declined, the terminal. It does not keep the home-bound
reports; each office decides privately what the encounter means for its own next activation.

So the adversary never learns directly whether it was heard. Its success is measured later and publicly:
a distinction is **fruitful** when a later activation of any office cites it. Fruitful distinctions feed
the executive's fruitfulness signal — *what can now proceed that couldn't before* — which is the
adversary's share of an executive brief that opens with the newly possible rather than the newly broken.

---

## Generating offices — proposal

The sit design lets the arena generate a new office when no one present knows what to do. Verdict: not
from a single unknown. An unknown gets an `explore` stance, which commissions a fool's expedition. An
office is warranted when expeditions into the same unknown **recur** — the same arrival-rate reasoning as
the router arena's clustering. A gap seen forty times is one missing capability. A gap seen once is an
expedition.

---

## HARD CONSTRAINTS

1. **Posture, not office.** It expires with the run (rule 8). No seat is the adversary between runs.
2. **Never `!`.** No adversary utterance holds, refuses, or gates.
3. **Withdrawal is constructive or it is critique.** No successor and carrier, no withdrawal.
4. **Stamped or it's sincere.** Unstamped opposition is the home office's objection. Nothing converts one
   into the other except the seat performing the second act.
5. **Every stance hands back footsteps.** A stance with no handback is entered as a distinction at most
   (an echo if `outside` is empty), and can't close the encounter as `commissioned`.
6. **`outside` is required.** Empty outside is an echo.
7. **`commissioned` names a carrier.**

---

## Surface — not yet

No `ctx adversary` command until stances have been taken by hand in real sit runs and the smallest useful
operator is known.

By hand, today: a seat writes the stamp into the sit record as part of its turn. The drought count is the
one piece that needs machinery, and it belongs to `sit.ps1`, which already holds the record — not to a
command of its own.

If an operator earns its name, the likely first is a reader over the record: distinctions per run, their
terminals, the echoes, and later which were cited. That's the part nobody will reconstruct by hand. Per
`commands.kit.md`, the stamp stays a filesystem convention (more than three related values), not a flag set.

---

## OPEN QUESTIONS — genuinely undecided, do not guess

1. **Drought `K`.** 3 is a starting guess. Measure it from sit runs; don't tune it by feel.
2. **Does a fruitful distinction ever promote into `decisions.json`?** Current answer: no — offices decide
   privately. But a distinction cited independently by three offices may be a decision nobody has written
   down. Watch for it before designing for it.
3. **Model family as policy.** Which family does adversary work best is an experiment, not an
   architecture choice — same stance as the router arena's model question.
4. **The full cross.** Large decisions may want all four stances on four seats at once. Undecided whether
   that is a procedure of its own or simply four self-elections in one turn.

---

## What good looks like

The adversary is working when sit runs close in `commissioned` and `distinguished` more often than in
silence, when executive decisions stand under critique unless something better is carried in, and when an
office can point at a thing it built because a distinction showed it the gap.

It has failed if seats start stamping to dodge accountability — opposition worn as a costume over a
sincere objection — or if the record fills with echoes.
