# The Project Definition Report and generation

**Part A:** the report, from draft to adoption. **Part B:** what is written after adoption. The
project root is this repository (fresh, import) or the target repository (install). Never overwrite
an existing file (`import-path.md`). Setup writes **no sprint record**; `/arpd-plan` creates
`reports/sprints/` when the first sprint starts. Adopted governance with no sprint is valid.

---

# Part A: the report

## A1. Draft

Write `reports/PROJECT-DEFINITION.md` from `kit/templates/reports/PROJECT-DEFINITION.md`, using the
notes. Set the version line (v1), the Status line (`Draft v1`), the DRAFT banner, and a date read
from `date -u +%Y-%m-%dT%H:%MZ`, marked UTC. Install mode without consent: write it in the OS temp
directory, beside the notes.

**Quality over length.** The report is the full specification the PI reviews, proportional to
complexity and risk; the template's guidance says what each section holds. Also:

- §1: a project name only if the PI gave one; otherwise a working name labelled as yours.
- §2–3: the scope tiers, exclusions and workflows keep the PI's words; each requirement's Priority
  follows the scope answers.
- §3: a required requirement always has acceptance criteria; if they depend on an Open decision, say
  so in them ("pending O-01: …").
- §7: every data-semantics item raised in the interview has its decider, or is Open with a gate.
- §11: every earlier PI preference carried forward (review depth, theory-context choice, autonomy,
  check-ins), the data-semantics rule, and the modules with why.

**Statuses** are those of the template's status table. An item is **Adopted-on-adoption** only when
the PI stated it, or accepted it in words, and its *Source* quotes them; your derivations and
recommendations are **Proposed** or **Provisional**. Never write "Adopted" or "Adopted by R-…" in a
draft.

## A2. Completeness check

Before showing **any** version, v2 and later included, run
`python kit/tools/check_report.py reports/PROJECT-DEFINITION.md --stage draft` (install mode: the
kit clone's path) and fix every FAIL. Then run the whole check listed in the notes template
(`kit/templates/discovery/SETUP.md` §10), its consistency items included. Fix what you can.
**Report material gaps to the PI** in the report's *Completeness check: gaps found* and in the
presentation; never manufacture detail to look complete. Record the result in the notes, *Report
version and state*.

## A3. Present

Show: the major design and governance choices, in a few lines each; the report's path and version
(the full specification for review; offer to show any section in the chat); the consequential open
decisions with their gates, and the gaps found; and the proposals awaiting the PI's acceptance (how
many; the consequential ones by ID).

Then ask how to proceed (`CHOICE FOR YOU (select one)`):

- A. Accept my proposals as written, and go to adoption. (Not included: data-semantics proposals,
  which are listed by ID in the approval request for you to accept or not, and Open items, which
  stay open unless you answer them.)
- B. Change something (say what).
- C. Go through the consequential proposals one by one.
- D. Reject this approach.

If no proposals await acceptance and nothing needs changing, go straight to A5. Picking A is not
adoption, and needs no new version: the approval request (A5) states that the proposals are accepted
by the PI's choice A, and the adoption ruling carries that acceptance. The PI may also edit the file
directly; read it back before continuing.

## A4. Review loop

- Every change after a version is shown makes a new version (vN+1), with a *Change history* row.
  Accepting proposals at adoption (A3 choice A, or a named acceptance in the adoption reply) is not a
  change to the report and makes no new version.
- Re-run the whole completeness check (A2) on the new version; present briefly what changed and
  what is still open.
- Resolve each proposal the PI has not accepted to a status in the template's table, or leave it
  Proposed (not adopted; backlog). **Exception: a data-semantics proposal the PI has not accepted
  becomes Open**, gated "before implementing <the feature it affects>", with its own row in
  *Waiting on the PI*. It never goes to the backlog, and nothing that depends on it is built. An O-NN is resolved only by the PI's answer to it; mark it
  "Resolved:" in §12, or move it out. A rejection: ask what to change; nothing is adopted.

## A5. Adoption

Ask with `APPROVAL REQUIRED`. Name the file and version, what a yes adopts, and what it does not
authorize. List each **data-semantics proposal** still unanswered (they were asked during
Requirements) and each **Open item** by ID and one line, and say
that only the proposals the PI names are accepted, and the Open items stay open. The PI may adopt
and accept named proposals in one reply ("adopt v3 with REQ-DATA-02 and D-04 accepted"). For
example:

```text
────────────────────────────────
APPROVAL REQUIRED
Adopt reports/PROJECT-DEFINITION.md v3? A yes, in your own words, becomes ruling R-01. It adopts
the items marked Adopted-on-adoption and my other proposals (your choice A), and records the
delegated, provisional, open and excluded items as such. These data-semantics proposals are
accepted only if you name them: REQ-DATA-02 (a skipped item is exported as an empty cell); D-04 (a
repeated export rewrites the whole file). These stay open: O-01 (entries per student; before
implementing the entry screen). I then write the governing documents from it. It does not approve a
sprint plan or start any implementation.
────────────────────────────────
```

Then:

- Record the reply **verbatim** as R-NN, with `Adopts: reports/PROJECT-DEFINITION.md vN`, the date
  from `date -u`, and `Recorded in: the commit "Record adoption ruling R-NN (setup in progress)",
  with the adopted report` (*Commit order*, step 2), so ruling, file, version and commit trace to
  each other. The *Reading* lists the proposals the ruling accepted (by ID; by choice A, or named),
  and maps each open O-NN to its *Waiting on the PI* row (#N).
- A plain assent ("ok", "aproved") is recorded exactly as given, with the line "(PI assented to
  reports/PROJECT-DEFINITION.md vN, as read back: '<the block's text>')". A plain assent accepts no
  data-semantics proposal: each one becomes Open with its gate and a *Waiting on the PI* row (A4).
- If the reply assents but adds something that could change the report, do not record the
  adoption. Revise to vN+1 and ask once more (`kit/docs/INTERACTION.md`, *A reply to an approval
  that also adds something*).
- Interview choices were preferences, and "move on" was not adoption. Only this ruling adopts.

---

# Part B: generation (only after the ruling)

**IDs.** R-01, SA-01 and DEC-01 assume an empty ledger. On import, continue the existing numbering,
and fill an inherited placeholder rather than reuse a given ID (`import-path.md`, *Numbering*).

**Dates** are read, never estimated (`SKILL.md`, *Every turn*); without `date`, use
`python -c "import datetime; print(datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%MZ'))"`.
"Proposed" dates come from the notes' recorded times.

**Where each item goes** is the report template's status table, the one mapping; a proposal the
ruling accepted counts as Adopted-on-adoption, with the ruling as its source.

## Commit order

1. **Move-only commits** (fresh and import modes): the kit's own files to `docs/arpd-kit/`, then
   any starter to the root, each commit alone (`import-path.md`, *Move-only commits*). Stage only the
   moves; the untracked notes and draft report are in no move commit. Never `git add -A` here.
2. **The adoption, first.** Write `DECISIONS.md` (row 5), with R-NN and SA-01. Then make the
   report's only post-adoption edit: set the Status line to `Adopted by R-NN (vN)`, and replace the
   DRAFT banner with the template's ADOPTED banner. Run `check_report.py` (as A2) with
   `--stage adopted`, and fix every FAIL. Commit the two files together, and nothing else:
   `git add DECISIONS.md reports/PROJECT-DEFINITION.md && git commit -m "Record adoption ruling R-NN (setup in progress)"`.
   The report is then frozen. Read this commit's SHA (`git rev-parse HEAD`) for `STATUS.md` and
   `START-HERE.md`. Install mode without consent: copy the adopted report into the target now
   (adoption authorizes it).
3. **The notes, alone** (row 20), if they are in the project. Make a last update, then
   `git add docs/discovery/SETUP.md && git commit -m "Add setup discovery notes (non-governing)"`.
   They are then frozen; a needed correction gets its own commit, before the final commit:
   `git commit -m "Correct setup discovery notes (non-governing)"`. Install mode without consent:
   skip this; the notes stay outside.
4. **The import baseline** (row 11, import and install), then the remaining files, committed at the
   end.
5. **`.claude/` last,** each on its own (*Permission prompts*, below).

## Every generated file

- Remove the template's HTML guidance comments (`<!-- … -->`), and fill every `{{…}}`. The
  governance check fails on an unfilled placeholder. Blocks starting `<!-- keep:` stay.
- Replace an empty example row with "None yet".
- **Generate from the adopted report only.** A governing document contains no material rule,
  requirement, limit or detail that the report (and the ruling) lacks. Anything new you notice now
  goes to *Waiting on the PI*, or to a DEC on the routine route, never silently into a rule.
- **Check each row** against the report as you write it (and any *Check* a row names). Fix any
  contradiction generation caused. Report one you cannot resolve to the PI and record it in
  `STATUS.md` §6; never silently pick one side.

| # | File | Source | How to fill it, and check |
|---|---|---|---|
| 1 | `CLAUDE.md` | `kit/constitution/CORE.md`; an ARPD starter's own | Fill every `{{…}}`: purpose and instrument from report §1, team and workspace from §10, `{{AUTHORITY_PROFILE}}` (the name only), `{{DATA_RULES}}` from §7 and §11. Append the selected modules under Part B (science first, then `team/team-arrangement.md` filled in; draft ones marked "(draft module, untested)"). Kept prior instructions go in Part B as `B.P-PROJECT: Project rules`, quoted, with their DEC. §6 "This project's examples": the routine, delegated and consult choices from §11, with the data-semantics examples as consult items unless a named policy delegates them. **ARPD starter:** update only the Version line (R-NN), *Authority profile*, PI line and §6's examples. *Check:* matches report §10–11. |
| 2 | `PARADIGM-SPEC.md` | `kit/templates/PARADIGM-SPEC.md`, or the starter's own | Depth follows the theory-context choice. **Not relevant, or D:** §1 is the PI's purpose verbatim; other sections "Not applicable for this project (R-NN)"; no pending research question. **A:** the context in the PI's words, unevaluated. **B:** the concerns the PI kept, in §9 or as ASM items, labelled. **C, or correctness-critical semantics:** the full CON…VAL items, definitions verbatim. §8: report §2's exclusions. Never invent CON, OP or INV items; a draft-wording marker stays until the PI's own words. |
| 3 | `REQUIREMENTS.md` | `kit/templates/REQUIREMENTS.md`, or the starter's own | The requirements the status table sends here, with the same IDs: ID, plain-language requirement, source (R-NN, or the spec item), state Planned (except imported Verified evidence, `import-path.md`) and evidence; *Requirement details* copies each one's acceptance criteria, priority and dependencies from the report. *Check:* every row has a details entry with at least one acceptance criterion, and matches the report's requirement in ID and meaning; nothing Proposed (unless the R-NN *Reading* accepts it by ID), Open or future-priority slipped in. |
| 4 | `MASTER_PLAN.md` | `kit/templates/MASTER_PLAN.md`, or the starter's own | The objective (§1); milestones from report §9 (§2); the broad order of work (§3), each row "planning pending", with no invented sprint plans; the backlog (§4) with what the status table sends there, each Backlogged and citing the report. Risks from report §12; the cadence from §11. *Check:* milestones and order match report §9. |
| 5 | `DECISIONS.md` | `kit/templates/DECISIONS.md`, or the starter's own | **R-NN:** as A5. **SA-01:** every field from report §11, in the PI's words or as "(drafted by the lead; PI assented: '<the PI's exact words>')"; data semantics not delegated unless a named policy is quoted. **DECs:** each adopted material decision of report §6 (citing D-NN), the team arrangement, import or move decisions (citing `reports/IMPORT-BASELINE-<date>.md`; an install DEC names the kit commit, `git -C <kit folder> rev-parse HEAD`), anything owed. **Waiting on the PI:** one row per Open item, and per gated Provisional item, in O-NN order; *Needed by* is the gate. |
| 6 | `ARCHITECTURE.md` | `kit/templates/ARCHITECTURE.md`, or the starter's own | Overview (§1), platform table (§2), components and data flow (§3) from report §5. *Architecture decisions*: the report §6 rows the status table sends here, same columns, each labelled. A-rules start as TARGET. Dependencies from §5. *Check:* the platform table agrees with the decisions; nothing is an unsupported guess. |
| 7 | `STATUS.md` | `kit/templates/STATUS.md` (an imported one is **rewritten** in this format) | **Readiness** as `SKILL.md`, *Closeout*, plus `reports/PROJECT-DEFINITION.md vN, commit <SHA from step 2>`. §2 "No sprint open"; §4 *On deck*: run `/arpd-plan`; §5 a short summary pointing to *Waiting on the PI*. Base commit, recovery block (if setup was resumed, a `Recovered:` line saying so, with the notes as the record), UTC time. Any test command is *The project's test command*. Team, workspace and resources. **§8:** the PI's working style from §11 (review depth, theory-context choice, check-ins); no interview mode. **§6 *Owed*:** every item not written; "Nothing owed" only when nothing is. |
| 8 | `INDEX.md` | `kit/templates/INDEX.md`, or the starter's own | All top-level paths that exist, including `reports/PROJECT-DEFINITION.md` (the adopted setup report) and the project's own. A later path gets "pending: <reason>". List `docs/discovery/` only if the notes are in the project. No empty directories. *Check:* every governing file and the report are listed. |
| 9 | `plans/README.md` | `kit/templates/plans/README.md` | Copy as is. |
| 10 | `reports/templates/` | `kit/templates/reports/*` | Copy as templates. Do not create `reports/sprints/`. |
| 11 | `reports/IMPORT-BASELINE-YYYY-MM-DD.md` | `kit/templates/reports/IMPORT-BASELINE.md` | **Import and install only.** The inherited baseline: source and provenance; each command as run, with its working directory, exit code and output **verbatim**; the test counts; any checker output; what was not run. Written once, then frozen. DECs and the first sprint cite it, and never copy it. |
| 12 | `tools/` | `kit/tools/*` | Copy `check_governance.py`, `check_report.py`, `next_plan_number.py`, `log_event.py`, `summarize_events.py` and `hooks/log_hook.py`, and copy `kit/LICENSE` to `tools/LICENSE` (not the kit's `test_*.py` or `fixtures/`). An imported starter's differing tools are replaced, and the import DEC says so. |
| 13 | `.claude/settings.json` | `kit/settings/settings.json` | *Permission prompts*, below. If a settings file exists, merge only the `hooks` key and show the PI the diff. Check that `python` resolves (`python --version`); otherwise use `python3` or the full path. |
| 14 | `.claude/agents/` | `kit/agents/*` | *Permission prompts*. Copy only the roles the arrangement in report §10 uses (for example, only `reviewer.md` for solo with a fresh-subagent review). |
| 15 | `.claude/skills/arpd-*` | the kit's `.claude/skills/arpd-*` | **Install mode only.** *Permission prompts*. Copy all four folders whole, with their `references/`. |
| 16 | `docs/EVENTS.md` | `kit/docs/EVENTS.md` | Copy. |
| 17 | `AGENTS.md` | (write; an ARPD starter's is kept) | One line: "Read CLAUDE.md in full before doing anything else; it is this project's team charter." |
| 18 | `START-HERE.md` | (write; for an ARPD starter, a new one; the old one is at `docs/arpd-kit/START-HERE-starter.md`) | One screen: (a) each governing file's purpose in one line, plus the adopted report (`reports/PROJECT-DEFINITION.md vN`, commit <SHA>), the record of what was adopted; (b) invariant / requirement / acceptance criterion, one line each (the table is in `REQUIREMENTS.md`); (c) `python -m pytest --ignore=kit --ignore=examples --ignore=evaluation` (*The project's test command*) and `python tools/check_governance.py`; (d) a section of its own, *Next step*, with the exact prompt `/arpd-plan` (current state appears only there; `/arpd-plan` rewrites only it); (e) one line each on `/arpd-plan` (drafts a plan; the PI approves it; work starts only when the PI says so), `/arpd-checkin`, `/arpd-amend`, if installed; (f) what happens at a sprint boundary; (g) *Known gaps*, with the exact commands for owed items, or "none". |
| 19 | `.gitignore` | (append; merge with an imported project's) | `logs/`, `output/`, `__pycache__/`, `.claude/settings.local.json`. |
| 20 | `docs/discovery/SETUP.md` | written during the interview | The final update marks the report as adopted by R-NN (vN), and says that the ruling and the governing documents, not these notes, are the authority. Committed alone (step 3), then frozen. Never in install mode without consent. |
| 21 | `reports/PROJECT-DEFINITION.md` | written during the interview | Committed with `DECISIONS.md` in step 2. The Status line and banner are the only changes from the adopted version. Frozen afterwards; informative under `CLAUDE.md` §2. |

## Permission prompts for `.claude/`

These writes and moves come **last**, each as its own step, so a refusal cannot block anything else.
They cover `.claude/settings.json` (the hooks), `.claude/agents/`, and `.claude/skills/` (install
only), and any `git mv` into or out of `.claude/`.

1. **Tell the PI first,** in plain words, what each item is for, and ask
   (`CHOICE FOR YOU (select one)`: install them now / skip them for now, and they are owed):
   - "Event logging: a small script records, for each event, its time and type (a prompt was sent,
     a tool ran, a turn ended). It records no prompt text and no file contents."
   - "Agent roles: the definitions of the reviewer (and implementer) the lead delegates to."
   - Install mode: "The planning, check-in and amendment commands, copied into your repository."
2. **Proceed only after the PI says yes in the chat,** whatever the tool does. If Claude Code also
   asks for permission, the PI approves there too.
3. **Never choose a method because it avoids a permission prompt.** Do not copy with `cp` through a
   shell instead of a direct write, and do not batch the files into a script.

If the PI declines, or a write is blocked (a non-interactive run cannot approve it):

- record a DEC titled "event logging not installed", "agent files not installed" or "skills not
  installed", with the reason and the route;
- list the item in `STATUS.md` §6 *Owed* and §7, and under *Known gaps* in `START-HERE.md`, with the
  exact commands below, saying which happened: "the PI agreed, but Claude Code's permission prompt
  did not allow the write" or "the PI declined";
- continue. The governance check reports the gap as ADVISORY once the DEC exists, and as MISSING
  until then.

### Commands for owed `.claude/` items

Copy these exactly into *Known gaps* and `STATUS.md` §6, for **the PI** to run later. They copy and
never move: `kit/` stays whole. Run them from the project root, in Git Bash or any POSIX shell.
`cp -n` never overwrites.

```
# Event logging. If .claude/settings.json already exists, do not run this: merge only the
# "hooks" key of kit/settings/settings.json into it, and show the PI the diff.
mkdir -p .claude && cp -n kit/settings/settings.json .claude/settings.json

# Agent roles (copy only the roles the team arrangement uses)
mkdir -p .claude/agents && cp -n kit/agents/*.md .claude/agents/

# Planning, check-in and amendment skills (install mode only), each folder whole, with its
# references/. Replace <kit folder> with the path of the kit repository this was installed from.
mkdir -p .claude/skills && cp -rn "<kit folder>"/.claude/skills/arpd-* .claude/skills/
```

Then `git add .claude && git commit -m "Install ARPD .claude files"`. For an ARPD starter whose
`.claude/` files stayed in the starter folder, use the starter's own commands instead (for the March
starter, `examples/march-1991/IMPORT.md`). While `/arpd-plan` is owed, `START-HERE.md` still names
planning as the next step, and says to run these commands first.

## The project's test command

The `kit/` folder holds the kit's own tests, and in fresh and import modes so do `examples/` and
`evaluation/`. They are not project tests. With pytest, every test command written in
`START-HERE.md`, `STATUS.md` and the import baseline is
`python -m pytest --ignore=kit --ignore=examples --ignore=evaluation`, plus the project's own options
(the same command in every mode; an ignored folder that does not exist is harmless).

**Working files.** Helper scripts and scratch files go outside the repository (the OS temp
directory or the session scratchpad). The notes and the report are the only exceptions. Commit with
`git commit -m "…"`, never with a message file.

## Then

1. Run `python tools/check_governance.py`, and fix any FAIL that generation caused.
2. **Search** the governing documents and `START-HERE.md`: `grep -n "<!--" *.md | grep -v "<!-- keep:"`
   prints nothing; no `{{` remains; on import, phrases the adoption made stale ("pending R-01",
   "Pending adoption", "the importing PI") are updated.
3. Log, with the actual IDs: `python tools/log_event.py ruling --actor lead --ref R-01 --note "Project Definition Report vN adopted at setup"`
   and `python tools/log_event.py ruling --actor lead --ref SA-01 --note "authority profile set at setup"`.
4. Check that the kit's pre-setup files are in `docs/arpd-kit/`, and `kit/` stays as the library.
5. Run `python tools/check_governance.py` again **after the final edit**. Quote its actual OVERALL
   line and any non-PASS or "not checked" lines, verbatim, in `STATUS.md` §4 and `START-HERE.md`.
   Never state a result from an earlier run.
6. Run `git status --short`, and remove any stray files you created. `docs/discovery/` and
   `reports/PROJECT-DEFINITION.md` must not appear, because they were committed in steps 2–3. Only
   then `git add -A` and `git commit -m "Set up ARPD project (ruling R-NN)"`.
7. Do not push without the PI's authorization.
8. Close out per `SKILL.md`, *Closeout and handoff*.
