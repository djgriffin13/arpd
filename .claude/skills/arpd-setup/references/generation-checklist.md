# Generation checklist (Phase 9)

Write files only after the adoption ruling has been recorded verbatim. In **fresh** and **import**
modes the project root is this repository. In **install** mode it is the target repository. Never
overwrite an existing file: see `import-path.md`.

**IDs.** R-01, SA-01 and DEC-01 below assume an empty ledger. When importing a project that already
has a `DECISIONS.md`, continue its numbering, and fill an inherited placeholder rather than reusing a
given ID (`import-path.md`, *Numbering*).

**Before writing (fresh and import modes): move-only commits.** Move the kit's own pre-setup files
(`README.md`, `QUICKSTART.md`, `CLAUDE.md`, `AGENTS.md`, `LICENSE`, `CITATION.cff`, `RELEASE-NOTES.md`) to `docs/arpd-kit/`
with `git mv`, and commit that move alone. The kit's licence and citation file describe the kit, not
the project: the PI chooses the project's own licence (`kit/LICENSE` and `tools/LICENSE` stay with
the kit's materials). For a starter that lives inside the kit, then move the starter to the root and
commit that move alone too. Edit nothing until both commits exist; a move combined with an edit can
cut the files' history (`import-path.md`, *Move-only commits*). The kit's files are not project
instructions: never reconcile them or write `.arpd` files beside them.

**Then, in every mode, record the authority first.** Write `DECISIONS.md` (row 5) with SA-01 and the adoption ruling
before any other governing file, and commit it alone: `git commit -m "Record adoption ruling R-NN
(setup in progress)"`. The ruling must contain the **full read-back text** the PI adopted (row 5),
not only the PI's reply: it is what a resumed session checks the other files against. If the setup is interrupted, a new session resumes from this record
(`SKILL.md`, *Resuming an interrupted setup*). Commit the rest at the end, as usual.

**Every generated file:** remove the template's HTML guidance comments (`<!-- … -->`) and fill every
`{{…}}`. The governance check fails on an unfilled placeholder. **Exception:** blocks that start
`<!-- keep:` (the entry formats in `DECISIONS.md`) stay, unfilled, for later entries.

| # | File | Source | How to fill it |
|---|---|---|---|
| 1 | `CLAUDE.md` | Fresh, install, or a non-ARPD import: `kit/constitution/CORE.md`. An ARPD starter: the starter's own `CLAUDE.md` | **From CORE.md:** fill every `{{…}}`, including `{{AUTHORITY_PROFILE}}`, which is the profile name only (for example "Bounded autonomy"); the charter line already says it is recorded as SA-01. Append the selected modules under Part B in this order: science modules, then `team/team-arrangement.md`, with its two arrangements filled in. Mark draft modules "(draft module, untested)". Prior instructions the PI keeps as project rules go in Part B as a section `B.P-PROJECT: Project rules`, each quoted with the DEC that kept it; a DEC saying a rule was kept is not enough on its own, because agents follow the charter. Under §6, after the routes table, add "This project's examples": routine, delegated and consult choices drawn from Phase 6. **ARPD starter:** keep the starter's charter and update it in place: the Version line (adopted by the importing PI's R-NN), the *Authority profile* line (the profile, recorded as SA-NN), the PI line, and §6's project examples. Change nothing else without a ruling. |
| 2 | `PARADIGM-SPEC.md` | `kit/templates/PARADIGM-SPEC.md`, or the starter's own | All phase 2 and 4 content. The question goes in **verbatim** in §1, and each construct's definition goes in the *PI's wording* column exactly as given. Every ID is stable. An item marked "(draft wording, awaiting the PI's words)" keeps that marker until the PI gives their own words; adopting "as it stands" does not clear it. List any such item in *Waiting on the PI*. Unresolved input gaps from Phase 3 go in §9 *Open scientific questions*. |
| 3 | `REQUIREMENTS.md` | `kit/templates/REQUIREMENTS.md`, or the starter's own | 5–15 requirements from Phase 3, each with a source ID. All start as Planned, except imported Verified evidence (`import-path.md`). |
| 4 | `MASTER_PLAN.md` | `kit/templates/MASTER_PLAN.md`, or the starter's own | The objective; milestone M1 (its requirement set and walkthrough); the planned order of 3–6 sprints; the cadence from Phase 6; risks from Phase 7. |
| 5 | `DECISIONS.md` | `kit/templates/DECISIONS.md`, or the starter's own | The SA and the adoption ruling, verbatim, with every SA field filled. If the PI's reply to a read-back was only an assent ("ok", "adopted"), record the read-back text that was assented to, labelled "(read back by the lead; PI assented: '<the PI's exact words>')". DEC entries for: the platform choice, the team and workspace arrangement, any import and move decisions (pointing to S01's baseline; an install DEC names the kit commit copied, from `git -C <kit folder> rev-parse HEAD`), and anything in this checklist that could not be written (row 13, 14, 15 or other). |
| 6 | `ARCHITECTURE.md` | `kit/templates/ARCHITECTURE.md`, or the starter's own | Overview in plain language, the platform table, components. A-rules start as TARGET. |
| 7 | `STATUS.md` | `kit/templates/STATUS.md` (an imported one is **rewritten** in this format) | Current state: setup complete; S01 on deck. Base commit, the recovery block, and the UTC time, taken from `date -u +%Y-%m-%dT%H:%MZ` (or `python -c "import datetime; print(datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%MZ'))"`), never estimated. Any test command it names excludes the kit (see *The project's test command*). Team, workspace and runtime-resource table. The PI's working style from Phase 1. §6 *Owed* lists every checklist item that could not be written; write "Nothing owed" only when nothing is. |
| 8 | `INDEX.md` | `kit/templates/INDEX.md`, or the starter's own | All top-level paths, including the project's own. List only paths that exist; for one that will exist later, add "pending: <reason>". No empty directories. |
| 9 | `plans/README.md` | `kit/templates/plans/README.md` | Copy as is. |
| 10 | `reports/` | `kit/templates/reports/*` | Copy as templates into `reports/templates/`. Create `reports/sprints/`. |
| 11 | `reports/sprints/SPRINT-01.md` | `reports/templates/SPRINT.md` | Part 1 only: the bounded first sprint from Phase 10. On import, Part 1 also records the inherited baseline (test and checker output), verbatim; this is the only place it is recorded. DEC entries may point to it, never claim to contain it. |
| 12 | `tools/` | `kit/tools/*` | Copy `check_governance.py`, `next_plan_number.py`, `log_event.py`, `summarize_events.py` and `hooks/log_hook.py`, and copy `kit/LICENSE` to `tools/LICENSE` so the MIT notice travels with them, in every mode (in install mode `kit/LICENSE` also arrives with the whole `kit/` folder). An imported starter's differing tools are replaced, and the import DEC says so. |
| 13 | `.claude/settings.json` | `kit/settings/settings.json` | **Tell the PI first** (see *Permission prompts* below). If a settings file exists, merge only the `hooks` key and show the PI the diff. Check that `python` resolves on this machine (`python --version`). If it doesn't, use `python3` or the full path. |
| 14 | `.claude/agents/` | `kit/agents/*` | **Tell the PI first** (below). Copy for lead-with-subagents and peer arrangements. |
| 15 | `.claude/skills/arpd-setup/`, `arpd-checkin/`, `arpd-amend/` | the kit repository's `.claude/skills/arpd-*` | **Install mode only** (in fresh and import modes they are already in this repository). **Tell the PI first** (below). Copy all three folders, in the same final step as rows 13 and 14. |
| 16 | `docs/EVENTS.md` | `kit/docs/EVENTS.md` | Copy. |
| 17 | `AGENTS.md` | (write; an ARPD starter's is kept) | One line: "Read CLAUDE.md in full before doing anything else; it is this project's team charter." |
| 18 | `START-HERE.md` | (write; for an imported ARPD starter, a new one, with the old one moved to `docs/arpd-kit/START-HERE-starter.md`) | For the PI, one screen, with **all** of these: what each governing file is for, in one line each; the commands that run the project's tests and the governance check (see *The project's test command* below); the exact first prompt, matching the team arrangement actually installed (say "brief the implementer" only if `.claude/agents/implementer.md` exists); how to check in, rule and amend (name `/arpd-checkin` and `/arpd-amend` only if `.claude/skills/arpd-checkin/SKILL.md` and `.claude/skills/arpd-amend/SKILL.md` exist; otherwise say they are owed, and point to *Known gaps*); **what to expect at a sprint boundary**, as a bullet list (close-out record, independent review, checks, a check-in with the PI, decisions waiting); and **Known gaps**: every checklist item that could not be written, with the exact commands from *Commands for owed `.claude/` items* below, or "none". |
| 19 | `.gitignore` | (append; merge with an imported project's) | `logs/`, `output/`, `__pycache__/`, `.claude/settings.local.json`. `logs/` stays uncommitted: each sprint's events are exported to `reports/sprints/` at close (`docs/EVENTS.md`). |

## Permission prompts for `.claude/`

Claude Code asks the PI for an interactive approval before any write to `.claude/settings.json` (the
hooks), `.claude/agents/` or `.claude/skills/`, and before a `git mv` into or out of `.claude/`.
Never try to get around this protection. Do these writes **last**, each as its own step, so a
blocked approval cannot stop anything else (in an import, the separate final move in
`import-path.md`, step 3). Before them, tell the PI in plain words:

- "Claude Code will ask your permission for these files. The first turns on event logging: a small
  script records, on each event, its time and type (a prompt was sent, a tool ran, a turn ended). It
  records no prompt text and no file contents. The second defines the implementer and reviewer roles
  the lead agent delegates to." In install mode, add: "The third copies the check-in and amendment
  commands (`/arpd-checkin`, `/arpd-amend`) into your repository."

If the PI declines, or the write is blocked (a non-interactive or scripted run cannot approve it):

- record a DEC titled "event logging not installed", "agent files not installed" or "skills not
  installed", with the reason and the route (routine, or the PI's ruling);
- list the item in `STATUS.md` §6 *Owed* and §7, and under *Known gaps* in `START-HERE.md`, with the
  exact commands below;
- continue. The governance check reports the gap as ADVISORY once the DEC exists, and as MISSING
  until then.

### Commands for owed `.claude/` items

Copy these exactly into *Known gaps* and `STATUS.md` §6; do not improvise others. They copy, never
move: the `kit/` folder is the module library and must stay whole. Run them from the project root,
in Git Bash or any POSIX shell. `cp -n` never overwrites an existing file.

```
# Event logging. If .claude/settings.json already exists, do not run this: merge only the
# "hooks" key of kit/settings/settings.json into it, and show the PI the diff.
mkdir -p .claude && cp -n kit/settings/settings.json .claude/settings.json

# Agent roles (lead-with-subagents and peer arrangements)
mkdir -p .claude/agents && cp -n kit/agents/*.md .claude/agents/

# Check-in and amendment skills (install mode only). Replace <kit folder> with the actual path of
# the kit repository this project was installed from.
mkdir -p .claude/skills && cp -rn "<kit folder>"/.claude/skills/arpd-* .claude/skills/
```

Then `git add .claude && git commit -m "Install ARPD .claude files"`. For an imported ARPD starter
whose own `.claude/` files stayed in the starter folder, use the `git mv` commands in
`import-path.md`, step 3, instead: there a move is intended.

## The project's test command

The `kit/` folder (and, in fresh and import modes, `examples/`) holds the kit's own tests, such as
`kit/tools/test_*.py`. They are not project tests and must not be counted as such. When the project
uses pytest, every test command written in `START-HERE.md`, `STATUS.md` and S01 excludes them:
`python -m pytest --ignore=kit --ignore=examples` (plus the project's own options). Other test
runners are unaffected unless they collect `kit/`.

**Working files.** Helper scripts and notes are written **outside** the repository (the OS temp
directory or the session scratchpad), never in the project. Commit with `git commit -m "…"` (several
`-m` for paragraphs), not with a message file.

**Then:**

1. Run `python tools/check_governance.py` and fix any generation-caused FAIL.
2. **Post-generation search** in the governing documents and `START-HERE.md`:
   - `<!--`: no template guidance comment may remain, except `<!-- keep:` blocks (for example
     `grep -n "<!--" *.md | grep -v "<!-- keep:"` should print nothing);
   - `{{`: no placeholder may remain;
   - on import, phrases the adoption made stale, such as "pending R-01", "Pending adoption", "until
     R-01 is recorded" or "the importing PI": update each one.
3. Record the adoption and the authority profile in the event log:
   - `python tools/log_event.py ruling --actor lead --ref R-01 --note "charter adopted at setup"`;
   - `python tools/log_event.py ruling --actor lead --ref SA-01 --note "authority profile set at setup"`.

   (Use the actual IDs if the ledger was inherited.)
4. Check that the kit's pre-setup files are in `docs/arpd-kit/`, so the project's own
   `START-HERE.md` is the entry point. `kit/` stays as the module library.
5. Run `python tools/check_governance.py` again **after the final edit**, and quote its actual
   OVERALL line (and any non-PASS steps) in `STATUS.md` §4, in `START-HERE.md` and in S01 Part 1.
   Never state a checker result from an earlier run.
6. Run `git status --short` and look for stray untracked files (helper scripts, message files, test
   output). Remove the ones you created; list any you cannot remove in `STATUS.md` §6. Only then
   `git add -A` and commit: `git commit -m "Set up ARPD project (ruling R-NN)"`, naming the adoption
   ruling.
7. Do not push without the PI's authorization.
