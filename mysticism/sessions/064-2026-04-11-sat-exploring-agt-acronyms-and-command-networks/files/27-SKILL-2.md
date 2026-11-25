---
name: ctx
description: Context navigation framework. Run `ctx chart` to orient — it shows your fleet and projects when outside a project, your project state when inside one. Use ctx commands for all context operations. Orient first, then work.
license: MIT
---

# ctx Skill

**Before starting any task in this project, run `ctx chart` to orient.** This framework provides deterministic, command-based context management. All context queries go through ctx commands — never read `.ctx/` files directly.

## Context Storage: @ctx Centralization

**Context now lives in a centralized `@ctx/` directory**, not scattered `.ctx/` folders per project. This solves:
- Same repo cloned to multiple locations
- Git worktrees pointing to same project
- Related artifacts in external folders (OneDrive, Downloads)
- Cross-machine context sharing via OneDrive sync

### Where Context Lives

```
.copilot/skills/ctx/
├── SKILL.md          ← you are here
├── @ctx/             ← CENTRALIZED CONTEXT STORE
│   ├── README.md     # Documentation for @ctx
│   ├── registry.json # Project identity resolution
│   └── projects/     # Context per project
│       └── my-project/
│           ├── chart        # Navigational state
│           ├── state.md     # Project state
│           ├── history.md   # Session history
│           └── *.json       # Structured data
└── framework/        ← add this directory to PATH
    ├── ctx.ps1       # PowerShell router
    ├── ctx           # Bash router
    └── ...
```

### Resolution Order

When you run `ctx chart`, the router resolves your project:
1. **@ctx/registry.json** — matches git remote URL or path
2. **.ctxconfig** — legacy pointer file (deprecated)
3. **.ctx/** — fallback directory walk (deprecated)

### Project Registration

Projects are registered in `@ctx/registry.json`:
```json
{
  "projects": {
    "my-project": {
      "remotes": ["https://github.com/org/my-project"],
      "paths": ["D:\\code\\my-project", "/home/user/my-project"],
      "worktree_roots": []
    }
  }
}
```

The router checks your git remote against registered projects first.

## What Is This Package

This skill is **self-contained**. The `framework/` subdirectory alongside this `SKILL.md` contains everything needed — the router scripts, commands, kits, and libraries. No external clone or install is required.

```
.copilot/skills/ctx/
├── SKILL.md          ← you are here
├── @ctx/             ← centralized context store
└── framework/        ← add this directory to PATH
    ├── ctx.ps1       # PowerShell router
    ├── ctx           # Bash router
    ├── bootstrap.ps1 # Initialize a new project's .ctx/ folder
    ├── bootstrap.sh
    ├── registry.json # Command registry (implemented | kit | requested)
    ├── validate.ps1  # Framework self-check (file integrity + bootstrap smoke test)
    ├── commands/     # Runnable command scripts
    ├── kits/         # Build specs for unimplemented commands
    └── lib/          # Shared libraries
```

## Environment Setup

### VS Code / GitHub Copilot (PowerShell)

The skill file is discovered automatically from `.copilot/skills/ctx/SKILL.md`.
Add the framework to PATH so `ctx` can be called directly:

```powershell
# Check if ctx is already in PATH
Get-Command ctx.ps1 -ErrorAction SilentlyContinue

# If not found, add for session:
$env:PATH = "$PWD/.copilot/skills/ctx/framework;$env:PATH"

# Or from any subdirectory (use absolute path):
$env:PATH = (Resolve-Path ".copilot/skills/ctx/framework").Path + ";$env:PATH"
```

### Claude Code (Bash / `.claude/` directory)

Claude Code reads agent instructions from `.claude/`. To install ctx there:

```bash
# Option A: symlink (preferred — single source of truth)
ln -s ../.copilot/skills/ctx .claude/skills/ctx

# Option B: copy framework directly
cp -r .copilot/skills/ctx/framework .claude/skills/ctx/framework

# Add to PATH (bash)
export PATH="$(pwd)/.copilot/skills/ctx/framework:$PATH"
```

Add the export to your project's `.claude/CLAUDE.md` or `~/.bashrc` so it persists.

### Claude.ai Web App

Containers reset each conversation. Unpack from project knowledge base:

```bash
bash /mnt/project/ctx-unpack-YYYY-MM-DD.txt
export CTX_HOME="/mnt/skills/user/ctx/framework"
```

### Verify Setup

```bash
ctx chart    # fast orientation (preferred)
ctx start    # full orientation (when chart is absent)
```

## Machine Setup: Daemon + Loom + Widget

The ctx framework includes a **persistent heartbeat daemon**, **terminal workspace loom**, and an optional **Game Bar widget**. These keep the cerebellum alive between sessions.

### Start the Daemon (required on each machine)

```powershell
ctx daemon start     # registers Windows Scheduled Task, runs every 5 min
ctx daemon status    # verify heartbeat is alive
```

The daemon runs silently (no console window). It performs:
- **Trust labeling** — labels context files for polyculture training (hourly)
- **Burndown updates** — recalculates goal priorities (every 6h)
- **Inbox processing** — picks up Congress task dispatches, questions, results (every 15 min)
- **Agent spawning** — launches autonomous `agency copilot` sessions for complex tasks
- **ADO PR checks** — polls PR status changes (every 30 min)

All machines share the same `@ctx/` via OneDrive. Each writes its own heartbeat file. Run `ctx daemon status` to see all machines.

### Launch a Loom (terminal workspace)

```powershell
ctx loom list            # show available loom configurations
ctx loom start congress  # open Congress workspace (Congress Floor + Scent Feed)
```

Available looms are JSON configs in `@ctx/looms/`. The **congress** loom provides a 2-pane split: interactive session on the left, auto-refreshing scent feed + congress status on the right.

### Deploy the Game Bar Widget (optional)

```powershell
ctx widget deploy    # builds UWP project + sideloads (requires VS + UWP workload)
ctx widget status    # check installation
```

Opens via **Win+G** → widget menu → "ctx Cerebellum".

### Stop/Remove

```powershell
ctx daemon stop      # removes scheduled task
ctx widget remove    # uninstalls Game Bar widget
```

## Core Philosophy

**Commands grow through use. Never bypass routinized operations.**

The ctx framework is an **inverted cone**. The root is unknown — the pre-distinction state where all tokens intersect. The periphery is maximally specific — a shell script poking a particular CI system. Between sits the **interference layer**: kits that represent tokens whose meaning has stabilized enough to survive some environments but not all. Commands grow at the periphery; kits change only through deliberate ascent (tighten, widen, or branch).

1. **Three states of territory:**
   - **Unmapped** → Explore (search, read files)
   - **Mapped** → Routinize (implement command from kit)
   - **Routinized** → Execute deterministically (use command)

2. **Read is the on-ramp to execute:**
   - Investigation leads to routinization
   - Rewrite functions to handle new cases
   - Progress toward deterministic execution

3. **Avoid regression:**
   - Every bypass (reading `.ctx` files directly) returns you to unmapped state
   - Use commands, not file reads: `ctx state` not `cat .ctx/state.md`
   - Extend commands when they lack features, don't work around them

## If You Find Yourself Doing These Things

**If you're reading or editing JSON files in `@ctx/` directly:**
The equivalent ctx command carries constraints other agents negotiated.
`ctx state` not `cat @ctx/projects/X/state.md`. `ctx goals` not editing `goals.json`.
`ctx congress dispatch` not creating inbox files by hand. The router is the interface.

**If you're editing chart files:**
Chart is computed output, not input. Update the sources: goals, project state, dock entries.
`ctx chart --set "> new goal"` updates the field. `ctx chart --dock` checkpoints.

**If you're doing build/deploy work on an executive terminal:**
Check your senator identity with `ctx chart`. If you're on DT (executive), your role is
to dispatch work to fleet senators, not to build or test locally. `ctx congress fleet`
shows who can do the work. `ctx congress dispatch <senator> "<task>"` sends it.

**If a command doesn't exist:**
That's information, not a failure. Run it anyway — the router registers it as requested.
Check `kits/` for a spec. If the kit exists, you can implement it. If not, register the
need and continue with what you have.

## Every Session Workflow

### 0. Descent Path (New Iteration)

When you are a fresh context — new session, new machine, or resuming after a break — you start at the **root of the cone** (unknown). You must reason outward before acting at the periphery.

```
SKILL.md → you are here. You know the vocabulary but not the terrain.

ctx chart → where am I?
  If chart shows > goal : focus → you have orientation. Skip to step 1.
  If chart shows @ ? → cold start. Continue descent:

ctx scent read → what did other sessions/machines leave behind?
  Scent trails are the freshest signal. They expire (12-48h TTL).
  Look for: session-dock, result-arrived, dispatch signals.

ctx history → what happened recently?
  Shows ~5 recent chart entries with timestamps. Establishes narrative.

Look for briefs:
  Session files (session-state/*/files/*-brief.md)
  @ctx/projects/<project>/ctx-evolution-brief.md
  Three-streams-brief or equivalent iteration handoff.

Now follow chart tokens outward:
  > goal → what this periphery is doing
  : focus → what's currently engaged
  ; next → what specific peripheral work to execute
  ? questions → what's unresolved
  + completed → what ascended recently
  ! alerts → interference events needing attention
```

**The cardinal rule of descent:** Do not edit ctx files directly. Do not write to .json or .md by hand. Use ctx commands to interact. If a command doesn't exist, that's information — the kit tells you what the command should do. If no kit exists, register the need (`ctx <commandname>` auto-registers it as requested).

**Why this matters:** A naive iteration that reads files and edits them directly has descended past the interference layer straight to the periphery without learning what the kits negotiated. It will make changes that conflict with what other sessions/machines have established. The commands ARE the interference layer — they carry the constraints and conventions that survived across environments.

### 1. Orient via Chart

```bash
ctx chart
```

The chart is 8 lines, ~60 tokens. Any mind reads it instantly:

```
CTX 1.0
@ /project/.ctx (5f 3d)
> what you're trying to accomplish
: what you're doing right now
; what comes next
? what's blocking or needed
+ other active goals
~ tokens remaining / budget
```

If no chart exists (cold start), `ctx chart` scans for signals — packed state, git roots, project markers — and suggests actions.

### 2. Work Using Commands

```bash
ctx state          # : query current state
ctx todos          # : list pending tasks
ctx decision       # + view architectural decisions
ctx search term    # ? search .ctx files
ctx topic auth     # : wedge into a topic area
ctx index          # @ list context files with staleness
```

### 2b. Leave Notes for Other Agents (Scent Trails)

When you discover something other agents should know, emit a scent trail:

```bash
ctx scent emit "pr-1234 needs reviewer attention" --salience 0.8 --affordance act-on
ctx scent emit "dependency X updated, verify compat" --salience 0.6 --project myproject
ctx scent read   # see what other agents left for you
```

Scent trails appear in `ctx chart` output as `!` lines when salience ≥ 0.5. They expire automatically (default 12h). Use them for:
- Progress updates between sessions
- Warnings about things that changed
- Requests for attention from other agents/sessions
- Refresh signals for daemon self-updates

### 3. Checkpoint via Dock

```bash
ctx dock
```

Dock replaces the finish+start seam. It emits the chart (~60 tokens), saves it, appends a one-line history entry. The next session reads the chart and begins immediately.

**When to dock:** context window >70% full, switching goals, before human interrupts, end of productive segment.

**When to use finish instead:** goal actually complete, archiving work, restructuring projects.

### Summary

```
chart → work → dock → [next session] → chart → work → dock → ...
```

Start and finish are ceremony for special occasions (cold starts and goal completion). Chart and dock are the heartbeat.

### 4. When a Command Doesn't Exist

```bash
ctx newcommand
# → "Not implemented. Kit exists at: kits/newcommand.kit.md"
```

If a kit exists, implement it:
1. Read the kit: `cat .copilot/skills/ctx/framework/kits/newcommand.kit.md`
2. Create the command: `.copilot/skills/ctx/framework/commands/newcommand.sh` (and/or `.ps1`)
3. Update `registry.json` — change `"status": "kit"` to `"status": "implemented"`
4. Use: `ctx newcommand`

If no kit exists, the command is registered as "requested". Create a kit spec, then implement it.

### 5. Growing Existing Commands

When a command exists but lacks a needed feature, extend it — don't create a new one:

```bash
# Original: ctx todos (lists todos)
# Need: ctx todos --complete 7
# Extend: edit commands/todos.ps1 to handle --complete flag
```

## Token Identity System

Commands cluster by their relationship to chart tokens. Each token represents a kind of operation in the navigational lifecycle. Token identity helps with routing, disambiguation, and understanding which commands govern related processes.

```
@  ANCHOR    — where things are
>  HEADING   — where you're going
:  FOCUS     — what you're doing now
;  SEQUENCE  — transitions between states
?  QUERY     — discovery and scanning
+  RECORD    — accumulation of knowledge
~  ASSESS    — evaluation and approximation
!  BIND      — commitment and constraint
.  EMIT      — the chart format itself
```

## Available Commands

### Implemented

| Token | Command | Usage | Purpose |
|-------|---------|-------|---------|
| `.` | `chart` | `ctx chart [--write\|--dock\|--set "> g"]` | Compressed navigational state (~60 tokens) |
| `;` | `dock` | `ctx dock` | Checkpoint: emit chart + save + history entry |
| `>` | `start` | `ctx start` | Full orientation (when chart absent or stale) |
| `:` | `state` | `ctx state [--filter <tag>]` | Query project state |
| `:` | `todos` | `ctx todos` | List/manage pending tasks |
| `:` | `topic` | `ctx topic <n>` | Progressive context expansion (save-point) |
| `?` | `search` | `ctx search <term>` | Wedge-style text search across `.ctx` files |
| `@` | `index` | `ctx index` | List context files with sizes and staleness |
| `+` | `decision` | `ctx decision [--tag <tag>]` | Query architectural decisions |
| `>` | `plan` | `ctx plan` | Command discovery and planning funnel |
| `~` | `fear` | `ctx fear` | Autonomous loop breakout via project rotation |
| `;` | `pack` | `ctx pack` | Create portable handoff archive |
| `;` | `unpack` | `ctx unpack [--merge\|--force]` | Restore context from archive |
| `~` | `trust` | `ctx trust [--label\|--detail]` | Report FRESH/AGING/STALE confidence; emit training labels |
| `!` | `stake` | `ctx stake <decision>` | Map decisions to responsibility concerns |
| `@` | `register` | `ctx register` | Register current directory as project in @ctx |
| `;` | `migrate` | `ctx migrate` | Absorb orphaned .ctx/ into @ctx/projects/ |
| `@` | `loom` | `ctx loom <name>` | Multi-pane workspace orchestration |
| `>` | `daemon` | `ctx daemon start\|stop\|status\|run-once` | Persistent heartbeat loop (trust labels, burndown, PR checks) |
| `+` | `label` | `ctx label <path> [--review\|--pending\|--stats]` | Agent/user labeling for polyculture training |
| `~` | `polyculture` | `ctx polyculture train\|classify\|status` | Micro-classifier pipeline (train, inference, SPRT gating) |
| `?` | `scent` | `ctx scent emit\|read\|clear` | Cross-agent signal protocol with TTL expiry |
| `!` | `congress` | `ctx congress dispatch\|ask\|answer\|read\|status` | Cross-machine task dispatch and result collection |
| `?` | `widget` | `ctx widget deploy\|remove\|status` | Build and sideload Game Bar cerebellum widget |

### Kits (Ready to Implement)

| Token | Command | Kit file | Purpose |
|-------|---------|----------|---------|
| `;` | `finish` | `kits/finish.kit.md` | Formal goal completion and archival |
| `;` | `continue` | `kits/continue.kit.md` | Resume after interruption without finishing |
| `?` | `find` | `kits/find.kit.md` | Find files/symbols in codebase |
| `@` | `codebase` | `kits/codebase.kit.md` | Query `codebase.json` location map |
| `@` | `locate` | `kits/locate.kit.md` | Project identity / git root resolution |
| `~` | `summarize` | `kits/summarize.kit.md` | Agent-maintained summaries at varying depth |
| `~` | `forgive` | `kits/forgive.kit.md` | Acknowledge drift, reset baseline |
| `+` | `honor` | `kits/honor.kit.md` | Archive with extracted lessons |
| `!` | `contract` | `kits/contract.kit.md` | Generate lean agent contracts |
| `>` | `phase` | `kits/phase.kit.md` | PRAY cycle state tracking |
| `+` | `narrative` | `kits/narrative.kit.md` | History as story, not archive |

### Command Clusters by Token

**`@` ANCHOR** — Where am I?
- `index` — what files exist, how stale
- `locate` — which project, which git root (kit)
- `codebase` — where things live in code (kit)

**`>` HEADING** — Where am I going?
- `chart` (via `>` field) — active goal
- `start` — full orientation ceremony
- `plan` — command discovery funnel
- `phase` — PRAY cycle tracking (kit)

**`:` FOCUS** — What am I doing right now?
- `state` — project state detail
- `todos` — pending tasks
- `topic` — progressive expansion into an area

**`;` SEQUENCE** — Transitions between states
- `dock` — lightweight checkpoint (the normal case)
- `finish` — formal goal completion (kit)
- `continue` — resume after interruption (kit)
- `pack` / `unpack` — portable archives

**`?` QUERY** — Discovery and scanning
- `chart` (cold start) — scan for signals
- `search` — text search across .ctx files
- `find` — find files/symbols in codebase (kit)

**`+` RECORD** — Accumulation of knowledge
- `decision` — architectural decisions
- `honor` — archive with lessons (kit)
- `narrative` — history as story (kit)

**`~` ASSESS** — Evaluation and approximation
- `trust` — confidence levels (kit)
- `forgive` — acknowledge drift (kit)
- `summarize` — variable-depth summaries (kit)
- `fear` — autonomous loop breakout

**`!` BIND** — Commitment and constraint
- `contract` — lean agent contracts (kit)
- `stake` — responsibility mapping (kit)

### Command Disambiguation

- `chart` — emits **compressed navigational state** (~60 tokens, any mind)
- `start` — **full orientation** ceremony (state + history + todos)
- `dock` — **lightweight checkpoint** (chart + save + history line)
- `finish` — **formal completion** (archive, handoff, goal restructure)
- `find` — searches the **codebase** map (`codebase.json`) for files/symbols
- `search` — searches **.ctx text files** for a term
- `locate` — determines **project identity** (which repo/clone/branch you are in)
- `topic` — **progressive expansion** into a knowledge area, with save-point semantics

## Chart Format

The chart is ctx's compressed navigational state. ~60 tokens, 8 lines max. Any mind — from 343M SLM to 1M-context orchestrator — can read and act on it.

```
CTX 1.0
@ <location> (<file_count>f <staleness_days>d)
> <active_goal>
: <current_step>
; <next_step>
? <need_or_blocker>
+ <other_goals> (<staleness>)
~ <remaining>/<budget>
```

### Token vocabulary is consonantal

Tokens are polyvalent punctuation — each carries multiple valid readings. Position disambiguates. No definitions needed. Every tokenizer on earth already knows these symbols.

### Cold start chart

When nothing exists:
```
CTX 1.0
@ ?
> ?
```

Two question marks. Invitation, not error. "Where are you?" and "What are you doing?" — the only two questions that matter for orientation.

## Implementation Guidelines

### Creating a Command from a Kit

1. **Read the kit** (paths use `/` throughout; use `\` on Windows PowerShell):
   ```bash
   cat .copilot/skills/ctx/framework/kits/<commandname>.kit.md
   ```

2. **Create the implementation:**
   - Bash: `.copilot/skills/ctx/framework/commands/<commandname>.sh`
     - Begin with `#!/usr/bin/env bash`
     - Prefer bash for new commands (broader compatibility)
   - PowerShell: `.copilot/skills/ctx/framework/commands/<commandname>.ps1`
     - Begin with `#!/usr/bin/env pwsh`
     - Accept `[Parameter(ValueFromRemainingArguments)]` for flags
   - Exit 0 on success; non-zero on error

3. **Update registry** — `.copilot/skills/ctx/framework/registry.json`:
   ```json
   "<commandname>": {
     "status": "implemented",
     "token": ";",
     "description": "Brief description",
     "implemented": "YYYY-MM-DD",
     "added_by": "agent-name"
   }
   ```

4. **Test:**
   ```bash
   ctx <commandname>
   ```

### Extending Existing Commands

Grow commands rather than creating new ones:

```bash
# Need: ctx todos --complete <id>
# Edit: commands/todos.ps1 (or todos.sh)
# Add parameter handling for --complete, then use: ctx todos --complete 7
```

## Anti-Patterns

### ❌ Bypassing Commands
```bash
# WRONG
cat .ctx/state.md
grep "TODO" .ctx/TODOS.md

# RIGHT
ctx state
ctx todos
```

### ❌ Using start when chart suffices
```bash
# WRONG (burns tokens on ceremony when orientation exists)
ctx start  # reads 3 files, emits 500+ tokens

# RIGHT (chart provides orientation in ~60 tokens)
ctx chart
```

### ❌ Using finish for routine context boundaries
```bash
# WRONG (ceremony at worst possible time — context nearly full)
ctx finish --continue-mission  # writes handoff, updates history, generates prompt

# RIGHT (checkpoint in ~60 tokens)
ctx dock
```

### ❌ Creating Duplicate Commands
```
WRONG: creating todos-complete.ps1
RIGHT: extend todos.ps1 to handle --complete
```

### ❌ Hardcoding Absolute Paths
```bash
# WRONG
state=$(cat "/home/user/project/.ctx/state.md")

# RIGHT — ctx router walks up tree to find .ctx
ctx state
```

### ❌ Referencing Old Locations
The framework was previously expected at `scripts/ctx/` or `D:\skite.Tools\projects\ctx`.
Those locations are obsolete. The canonical location is `.copilot/skills/ctx/framework/`
(or `.claude/skills/ctx/framework/` for Claude Code installs).

## Troubleshooting

### `ctx` Not Found

```bash
# bash — add to PATH for current session
export PATH="$(pwd)/.copilot/skills/ctx/framework:$PATH"
which ctx             # verify
```

```powershell
# PowerShell — add to PATH for current session
$env:PATH = (Resolve-Path ".copilot/skills/ctx/framework").Path + ";$env:PATH"
Get-Command ctx.ps1   # verify
```

### Cold Start: No .ctx/ Found

```bash
ctx chart    # scans for signals, suggests actions
# → shows packed state, git roots, project markers
# → suggests: unpack, bootstrap, or describe your goal
```

### Command Not Found in Registry

```bash
cat .copilot/skills/ctx/framework/registry.json
ls .copilot/skills/ctx/framework/kits/
```

If a kit exists, implement it. If not, run `ctx <commandname>` once — it will be auto-registered as "requested".

### Command Returns Kit Instructions
```
ctx finish
# → "Not implemented. Kit exists: kits/finish.kit.md"
```
This is expected. Read the kit, implement the command, update registry, then use it.

### Execution Policy (PowerShell)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Example Workflows

### Arriving at Empty Dock (cold start)

```bash
ctx chart
# CTX 1.0
# @ ? (scanning)
#   pack @ /mnt/project/ctx-unpack-2026-03-10.txt
#   .git @ /home/user/project (main)
# > ?
#
# ACTIONS:
#   unpack: bash /mnt/project/ctx-unpack-2026-03-10.txt
#   bootstrap: ctx bootstrap
#   goal: tell me what you're working on

bash /mnt/project/ctx-unpack-2026-03-10.txt
ctx chart
# now oriented
```

### Routine Work Session

```bash
ctx chart                     # orient (~60 tokens)
ctx state --filter active     # detail on current work if needed
# ... do work ...
ctx dock                      # checkpoint before context fills
```

### Mid-Session Goal Switch

```bash
ctx chart --set "> new goal"
ctx chart --set ": first step of new goal"
ctx chart --set "; second step"
# work continues on new heading
```

### Implementing a Missing Command

```bash
ctx finish                    # see what feedback you get
# → "Not implemented. Kit exists: kits/finish.kit.md"

cat .copilot/skills/ctx/framework/kits/finish.kit.md
# create commands/finish.sh (or finish.ps1)
# update registry.json: "status": "implemented", "token": ";"

ctx finish --archive
```

### Wedge-Style Investigation

```bash
ctx search authentication        # ? search .ctx files
ctx decision --tag authentication # + why auth works this way
ctx topic auth                    # : expand into auth area
ctx state --filter security       # : security-tagged work items
```

### Dispatching Work to Another Machine (Congress)

```powershell
# Dispatch a bugfix to a devbox — daemon spawns an autonomous agent session
ctx congress dispatch cpc-skite-t130h "Investigate bug 60076941 in OSClient. Check if previous UTC/FolderModal fixes resolved it. If not, create a PR with the fix." --workspace "c:\oscl_2" --bugid 60076941 --project osclient

# Check status — see inbox, outbound tasks, and results
ctx congress status

# Read a result when it arrives back
ctx congress read

# Ask a question that surfaces on all machines with running daemons
ctx congress ask "Which branch should the fix target?" --project osclient

# Answer a question from a remote agent
ctx congress answer task-20260401-150335-0fe654b3 "Target release/main"
```

The congress loop: **dispatch → OneDrive sync → daemon pickup → agent spawn → work → result syncs back → read**.

## ADO Interaction Policy

Agents interact with Azure DevOps according to a two-layer model. **ADO is the public record.** Internal coordination uses ctx (scent, labels, congress). Never mix the two.

### What goes in ADO (visible to team and process)
- **Draft PR as workspace**: Create early with work item attached + task understanding in description. Use PR comments as conversation space. Publish when implementation is ready.
- **Attachments on work items**: Test plans, reports, screenshots, generated docs. Artifacts that demonstrate work.
- **Status comments on work items**: Only at phase transitions — dispatched, completed, blocked, PR ready. Never heartbeats, debug, or daemon chatter.
- **Source control links**: PR ↔ work item ↔ branch. Always link.

### What stays in ctx (user-private partnership)
- Scent trails, trust labels, fleet heartbeats, session state
- Congress dispatch/inbox messages
- Shepherd internal state and iteration notes
- Polyculture training data

### Rules
1. Every shepherded item should reference a work item (create if needed)
2. Never create orphan PRs — always attach work item
3. PR descriptions explain *what* and *why*, not just "fixes bug"
4. No automated comments that clutter human-readable threads
5. Attachments > inline text for large artifacts
6. Draft PRs are workspaces; published PRs are proposals

### Archetype ADO Responsibilities
| Archetype | ADO Surface |
|-----------|-------------|
| **Gatherer** | Attaches research docs to work items |
| **Tester** | Creates test result attachments, links test plans |
| **Author** | Owns PR description, responds to review comments |
| **Witness** | Validates PR quality before publish, status comments |
| **Caseworker** | Manages work item state transitions, links |
| **Reporter** | Summarizes in work item comments (phase transitions only) |

## Success Criteria

You're using ctx correctly when:

- ✅ Every session starts with `ctx chart` (not `ctx start` unless chart is absent)
- ✅ Context boundaries hit `ctx dock` (not `ctx finish` unless goal is complete)
- ✅ Context queries use commands, not file reads
- ✅ Missing commands get implemented from kits
- ✅ Existing commands grow to handle new cases
- ✅ No bypassing with grep/cat for `.ctx` files
- ✅ Token identity guides which commands relate to current work

## Vessel/Harbor Model

- **Vessel** = context window (ephemeral, arrives empty)
- **Harbor** = persistent layer (project KB, filesystem, .ctx/)
- **Chart** = compressed navigational intent (the bridge between them)
- **Harbormaster** = index/routing layer (future: SLM for fast triage)
- **Crew** = orchestrating model doing real work

The chart is what survives between vessels. Everything else is cargo — loaded on demand.

## References

All paths below are relative to the directory where this skill package is installed.

- Skill file: `.copilot/skills/ctx/SKILL.md`
- Framework: `.copilot/skills/ctx/framework/`
- Router (PowerShell): `.copilot/skills/ctx/framework/ctx.ps1`
- Router (bash): `.copilot/skills/ctx/framework/ctx`
- Command registry: `.copilot/skills/ctx/framework/registry.json`
- Command implementations: `.copilot/skills/ctx/framework/commands/`
- Kit specifications: `.copilot/skills/ctx/framework/kits/`
- Bootstrap: `.copilot/skills/ctx/framework/bootstrap.ps1` / `bootstrap.sh`

For Claude Code installs, substitute `.copilot/` with `.claude/` in all paths above.
For Claude.ai web app, ctx framework is at `/mnt/skills/user/ctx/framework/`.

---

**Remember:** Chart is the heartbeat. Dock is the checkpoint. Commands grow through use. Never bypass. Always extend.
