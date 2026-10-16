# Generation checklist (Phase 9)

Write files only after the adoption ruling has been recorded verbatim. In **fresh** and **import**
modes the project root is this repository. In **install** mode it is the target repository. Never
overwrite an existing file: see `import-path.md`.

**IDs.** R-01, SA-01 and DEC-01 below assume an empty ledger. When importing a project that already
has a `DECISIONS.md`, continue its numbering, and fill an inherited placeholder rather than reusing a
given ID (`import-path.md`, *Numbering*).

**Before writing (fresh and import modes): move-only commits.** Move the kit's own pre-setup files
(`README.md`, `QUICKSTART.md`, `CLAUDE.md`, `AGENTS.md`) to `docs/arpd-kit/` with `git mv`, and commit
that move alone. For a starter that lives inside the kit, then move the starter to the root and
commit that move alone too. Edit nothing until both commits exist; a move combined with an edit can
cut the files' history (`import-path.md`, *Move-only commits*). The kit's files are not project
instructions: never reconcile them or write `.arpd` files beside them.

**Every generated file:** remove the template's HTML guidance comments (`<!-- … -->`) and fill every
`{{…}}`. The governance check fails on an unfilled placeholder. **Exception:** blocks that start
`<!-- keep:` (the entry formats in `DECISIONS.md`) stay, unfilled, for later entries.

| # | File | Source | How to fill it |
|---|---|---|---|
| 1 | `CLAUDE.md` | Fresh, install, or a non-ARPD import: `kit/constitution/CORE.md`. An ARPD starter: the starter's own `CLAUDE.md` | **From CORE.md:** fill every `{{…}}`, including `{{AUTHORITY_PROFILE}}`, which is the profile name only (for example "Bounded autonomy"); the charter line already says it is recorded as SA-01. Append the selected modules under Part B in this order: science modules, then `team/team-arrangement.md`, with its two arrangements filled in. Mark draft modules "(draft module, untested)". Under §6, after the routes table, add "This project's examples": routine, delegated and consult choices drawn from Phase 6. **ARPD starter:** keep the starter's charter and update it in place: the Version line (adopted by the importing PI's R-NN), the *Authority profile* line (the profile, recorded as SA-NN), the PI line, and §6's project examples. Change nothing else without a ruling. |
| 2 | `PARADIGM-SPEC.md` | `kit/templates/PARADIGM-SPEC.md`, or the starter's own | All phase 2 and 4 content. The question goes in **verbatim** in §1, and each construct's definition goes in the *PI's wording* column exactly as given. Every ID is stable. An item marked "(draft wording, awaiting the PI's words)" keeps that marker until the PI gives their own words; adopting "as it stands" does not clear it. List any such item in *Waiting on the PI*. Unresolved input gaps from Phase 3 go in §9 *Open scientific questions*. |
| 3 | `REQUIREMENTS.md` | `kit/templates/REQUIREMENTS.md`, or the starter's own | 5–15 requirements from Phase 3, each with a source ID. All start as Planned, except imported Verified evidence (`import-path.md`). |
| 4 | `MASTER_PLAN.md` | `kit/templates/MASTER_PLAN.md`, or the starter's own | The objective; milestone M1 (its requirement set and walkthrough); the planned order of 3–6 sprints; the cadence from Phase 6; risks from Phase 7. |
| 5 | `DECISIONS.md` | `kit/templates/DECISIONS.md`, or the starter's own | The SA and the adoption ruling, verbatim, with every SA field filled. If the PI's reply to a read-back was only an assent ("ok", "adopted"), record the read-back text that was assented to, labelled "(read back by the lead; PI assented: '<the PI's exact words>')". DEC entries for: the platform choice, the team and workspace arrangement, any import and move decisions (pointing to S01's baseline), and anything in this checklist that could not be written (row 13, 14 or other). |
| 6 | `ARCHITECTURE.md` | `kit/templates/ARCHITECTURE.md`, or the starter's own | Overview in plain language, the platform table, components. A-rules start as TARGET. |
| 7 | `STATUS.md` | `kit/templates/STATUS.md` (an imported one is **rewritten** in this format) | Current state: setup complete; S01 on deck. Base commit, the recovery block, and a UTC time. Team, workspace and runtime-resource table. The PI's working style from Phase 1. §6 *Owed* lists every checklist item that could not be written; write "Nothing owed" only when nothing is. |
| 8 | `INDEX.md` | `kit/templates/INDEX.md`, or the starter's own | All top-level paths, including the project's own. List only paths that exist; for one that will exist later, add "pending: <reason>". No empty directories. |
| 9 | `plans/README.md` | `kit/templates/plans/README.md` | Copy as is. |
| 10 | `reports/` | `kit/templates/reports/*` | Copy as templates into `reports/templates/`. Create `reports/sprints/`. |
| 11 | `reports/sprints/SPRINT-01.md` | `reports/templates/SPRINT.md` | Part 1 only: the bounded first sprint from Phase 10. On import, Part 1 also records the inherited test baseline, verbatim; this is the only place it is recorded. |
| 12 | `tools/` | `kit/tools/*` | Copy `check_governance.py`, `next_plan_number.py`, `log_event.py`, `summarize_events.py` and `hooks/log_hook.py`. An imported starter's differing tools are replaced, and the import DEC says so. |
| 13 | `.claude/settings.json` | `kit/settings/settings.json` | **Tell the PI first** (see *Permission prompts* below). If a settings file exists, merge only the `hooks` key and show the PI the diff. Check that `python` resolves on this machine (`python --version`). If it doesn't, use `python3` or the full path. |
| 14 | `.claude/agents/` | `kit/agents/*` | **Tell the PI first** (below). Copy for lead-with-subagents and peer arrangements. |
| 15 | `docs/EVENTS.md` | `kit/docs/EVENTS.md` | Copy. |
| 16 | `AGENTS.md` | (write; an ARPD starter's is kept) | One line: "Read CLAUDE.md in full before doing anything else; it is this project's team charter." |
| 17 | `START-HERE.md` | (write; for an imported ARPD starter, a new one, with the old one moved to `docs/arpd-kit/START-HERE-starter.md`) | For the PI, one screen, with **all** of these: what each governing file is for, in one line each; the one command that runs all checks; the exact first prompt, matching the team arrangement actually installed (say "brief the implementer" only if `.claude/agents/implementer.md` exists); how to check in, rule and amend; **what to expect at a sprint boundary**, as a bullet list (close-out record, independent review, checks, a check-in with the PI, decisions waiting); and **Known gaps**: every checklist item that could not be written, or "none". |
| 18 | `.gitignore` | (append; merge with an imported project's) | `logs/`, `output/`, `__pycache__/`, `.claude/settings.local.json`. `logs/` stays uncommitted: each sprint's events are exported to `reports/sprints/` at close (`docs/EVENTS.md`). |

## Permission prompts for `.claude/`

Claude Code asks the PI for an interactive approval before any write to `.claude/settings.json` (the
hooks) or `.claude/agents/`. Never try to get around this protection. Before those two writes, tell
the PI in plain words:

- "Claude Code will ask your permission for two files. The first turns on event logging: a small
  script records, on each event, its time and type (a prompt was sent, a tool ran, a turn ended). It
  records no prompt text and no file contents. The second defines the implementer and reviewer roles
  the lead agent delegates to."

If the PI declines, or the write is blocked (a non-interactive or scripted run cannot approve it):

- record a DEC titled "event logging not installed" or "agent files not installed", with the reason
  and the route (routine, or the PI's ruling);
- list the item in `STATUS.md` §6 *Owed* and §7, and under *Known gaps* in `START-HERE.md`;
- continue. The governance check reports the gap as ADVISORY once the DEC exists, and as MISSING
  until then.

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
5. `git add -A`, then commit: "Set up ARPD project (ruling R-NN)", naming the adoption ruling.
6. Do not push without the PI's authorization.
