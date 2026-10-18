# The Project Definition Report and generation

**Part A** covers the report, from the draft to adoption. **Part B** covers what is written after
adoption, and how. In **fresh** and **import** modes the project root is this repository. In
**install** mode it is the target repository. Never overwrite an existing file (`import-path.md`).

Setup writes **no sprint record**. `/arpd-plan` creates `reports/sprints/SPRINT-01.md` when the first
sprint starts. A project with adopted governance and no sprint is complete and valid.

---

# Part A: the report

## A1. Draft

Write `reports/PROJECT-DEFINITION.md` from `kit/templates/reports/PROJECT-DEFINITION.md`, using the
notes. Set the version line (v1), the Status line (`Draft v1`), the DRAFT banner, and a date read
from `date -u +%Y-%m-%dT%H:%MZ`, marked UTC. Install mode without consent: write it in the OS temp
directory, beside the notes.

**Quality over length.** The report is the full specification the PI reviews. Detail is
proportional to complexity and risk. A simple data-collection tool gets a short, sharp report; an
estimator gets a deep one. A section that does not apply is one line: "Not applicable: <reason>".
No boilerplate, and no forced detail.

| Section | Draws on | Watch for |
|---|---|---|
| 1. Executive overview | Project phase; the PI's purpose, verbatim | Give a project name only if the PI gave one. Otherwise use a working name labelled as yours. |
| 2. Product vision and workflows | Requirements domains 1–2 | Number the workflows step by step. Exclusions keep the PI's words. |
| 3. Functional requirements | Domain 3, data semantics, and the scope answers (Priority) | Each requirement uses the template's fields. Acceptance criteria are checks an independent tester could run. |
| 4. Nonfunctional requirements | Domain 5 | Mark each target as stated by the PI, or as a proposed default, with how it is measured. |
| 5. Proposed architecture | `architecture-guide.md` | A claim about a technology says what was checked, or "not verified". |
| 6. Alternatives and decisions | The notes, *Architecture alternatives explored* | Every material decision lists its alternatives and why each rejected one was rejected. |
| 7. Data and interface contracts | Domain 4 | Never invent an unresolved schema. Give each data-semantics item its decider (the PI's words, or a named policy), or mark it Open with a gate. **Include a concrete example**, such as an output row or a file excerpt, wherever the PI can check semantics directly. |
| 8. Verification and acceptance | *Verification*, under Requirements | Keep implementation correctness apart from scientific validity. |
| 9. Roadmap | The three scope answers | The minimum becomes M1, the ideal becomes later milestones, and the nice-to-haves become deferred features. This is direction only; `/arpd-plan` plans the sprints. |
| 10. Agent team | Team & Governance | Size it to the work. Give the PI's choice, and your recommendation if it differed. |
| 11. Authority and governance | Team & Governance; the notes, *Governance preferences* | Carry forward every earlier preference: review depth, theory-context choice, autonomy, check-ins. Include the data-semantics rule. Give the modules, and why each was selected. |
| 12. Risks and open decisions | All phases | Every item has a gate. |
| 13. What adoption authorizes | The template text | Keep it. Add any project-specific limit. |

**Statuses, honestly.** Use the template's legend.

- A requirement or decision is **Adopted-on-adoption** only when the PI stated it, or accepted it
  in words, and the *Source* quotes them.
- Your derivations and recommendations are **Proposed** or **Provisional**.
- Never mark anything "Adopted" or "Adopted by R-…" in a draft.

## A2. Completeness check

Before showing any version, fill in the template's completeness table. Check for:

- ambiguous functionality;
- inconsistent requirements;
- missing inputs or outputs;
- unclear data semantics;
- unresolved architecture dependencies;
- unsupported assumptions;
- requirements without meaningful verification criteria;
- conflicts with exclusions;
- missing PI decisions;
- anything recorded as adopted too early.

Also check that:

- every data-semantics question raised in the interview is decided by the PI, delegated under a
  policy the PI named, or Open with a gate;
- every earlier PI preference appears in §10 or §11;
- nothing you invented, such as a field, a limit, a name or a "no network" rule, appears without a
  "Lead's" label.

Fix what you can. **Report material gaps to the PI** in the presentation, and never manufacture
detail to look complete. Record the result in the notes, *Report version and state*.

## A3. Present

On a turn with the Definition Report phase current:

- the major design and governance choices, in a few lines each;
- the report's path and version, and that it is the full specification for review; offer to show
  any section in the chat;
- the consequential open decisions, with their gates, and the gaps the completeness check found;
- the lead's proposals awaiting the PI's acceptance: how many, and the consequential ones by name.

Then ask how to proceed (`CHOICE FOR YOU (select one)`):

- A. Accept my proposals as written. I mark them accepted in the next version, then ask you to
  adopt it.
- B. Change something (say what).
- C. Go through the consequential proposals one by one.
- D. Reject this approach.

If no proposals await acceptance and nothing needs changing, go straight to A5.

Picking A is not adoption. It makes the proposals Adopted-on-adoption in the next version, with the
PI's words quoted as their source. The PI may also edit the file directly; read it back before
continuing.

## A4. Review loop

- Every change after a version is shown makes a new version (vN+1), with a *Change history* row.
- Re-run the completeness check, then present again briefly: what changed, and what is still open.
- Any lead proposal the PI has not accepted becomes one of:
  - Adopted-on-adoption, quoting the PI's acceptance;
  - Delegated (SA-NN, with its bounds);
  - Provisional, with what confirms it;
  - Open, with a gate;
  - Excluded;
  - or it is left Proposed, which §13 says is not adopted and goes to the backlog.
- A rejection: ask what to change. Nothing is adopted. The notes keep everything.

## A5. Adoption

Ask with `APPROVAL REQUIRED`. Name the file and version, what a yes adopts, and what it does not
authorize. For example:

```text
────────────────────────────────
APPROVAL REQUIRED
Adopt reports/PROJECT-DEFINITION.md v3? A yes, in your own words, becomes ruling R-01. It adopts
the items marked Adopted-on-adoption and records the delegated, provisional, open and excluded
items as such. I then write the governing documents from it. It does not approve a sprint plan or
start any implementation.
────────────────────────────────
```

Then:

- Record the reply **verbatim** as R-NN, with `Adopts: reports/PROJECT-DEFINITION.md vN` and the
  date read from `date -u`. Add the line `Recorded in: the commit "Record adoption ruling R-NN
  (setup in progress)", with the adopted report`. That commit holds both files (*Commit order*,
  step 2), so the ruling, the file, the version and the commit trace to each other. `STATUS.md` and
  `START-HERE.md` give that commit's SHA.
- A plain assent ("ok", "aproved") is recorded exactly as given, with the line "(PI assented to
  reports/PROJECT-DEFINITION.md vN)".
- If the reply assents but adds something that could change the report, do not record the
  adoption. Revise to vN+1 and ask once more (`kit/docs/INTERACTION.md`, *A reply to an approval
  that also adds something*).
- Choices made during the interview were preferences, and "move on" was not adoption. Only this
  ruling adopts.

---

# Part B: generation (only after the ruling)

**IDs.** R-01, SA-01 and DEC-01 assume an empty ledger. On import, continue the existing numbering,
and fill an inherited placeholder rather than reuse a given ID (`import-path.md`, *Numbering*).

**Every date and time** written in any file is read at that moment with `date -u +%Y-%m-%dT%H:%MZ`
(or `python -c "import datetime; print(datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%MZ'))"`)
and marked UTC. "Proposed" dates come from the notes' recorded times. Never estimate one.

## Commit order

1. **Move-only commits** (fresh and import modes).
   - Move the kit's own pre-setup files (`README.md`, `QUICKSTART.md`, `CLAUDE.md`, `AGENTS.md`,
     `LICENSE`, `CITATION.cff`, `RELEASE-NOTES.md`) to `docs/arpd-kit/` with `git mv`, and commit
     that move alone.
   - The kit's licence and citation file describe the kit; the PI chooses the project's own licence.
   - For a starter inside the kit, then move the starter to the root, and commit that alone
     (`import-path.md`, *Move-only commits*).
   - Stage only the moves. The untracked notes and draft report are in no move commit. Never
     `git add -A` here.
2. **The adoption, first.** Write `DECISIONS.md` (row 5), with R-NN and SA-01. Then make the
   report's only post-adoption edit: set the Status line to `Adopted by R-NN (vN)`, and replace the
   DRAFT banner with the template's ADOPTED banner. Commit the two files together, and nothing else:
   `git add DECISIONS.md reports/PROJECT-DEFINITION.md && git commit -m "Record adoption ruling R-NN (setup in progress)"`.
   - From here on the report is frozen. It is the record of what was adopted. Read this commit's
     SHA (`git rev-parse HEAD`) for `STATUS.md` and `START-HERE.md`.
   - Install mode without consent: copy the adopted report into the target now. Adoption authorizes
     this.
3. **The notes, alone** (row 20), if they are in the project. Make a last update, then
   `git add docs/discovery/SETUP.md && git commit -m "Add setup discovery notes (non-governing)"`.
   - From then on they are frozen for the rest of setup. A needed correction gets its own commit,
     before the final commit: `git commit -m "Correct setup discovery notes (non-governing)"`.
   - Install mode without consent: skip this; the notes stay outside.
4. **The import baseline** (row 11, import and install), then the remaining files, committed at the
   end.
5. **`.claude/` last,** each on its own (*Permission prompts*, below).

## Every generated file

- Remove the template's HTML guidance comments (`<!-- … -->`), and fill every `{{…}}`. The
  governance check fails on an unfilled placeholder. The exception is blocks starting `<!-- keep:`,
  which stay.
- Replace an empty example row with "None yet".
- **Generate from the adopted report only.** A governing document contains no material rule,
  requirement, limit or detail that the report lacks. Anything new that you notice now goes to
  *Waiting on the PI*, or to a DEC on the routine route, never silently into a rule.

| # | File | Source | How to fill it |
|---|---|---|---|
| 1 | `CLAUDE.md` | Fresh, install, or a non-ARPD import: `kit/constitution/CORE.md`. An ARPD starter: its own `CLAUDE.md` | **From CORE.md:** fill every `{{…}}`. The one-line purpose and instrument come from report §1. The team and workspace come from §10. `{{AUTHORITY_PROFILE}}` is the profile name only. `{{DATA_RULES}}` comes from §7 and §11. Append the selected modules under Part B: science modules first, then `team/team-arrangement.md`, with its two arrangements filled in. Mark draft modules "(draft module, untested)". Prior instructions the PI keeps go in Part B as `B.P-PROJECT: Project rules`, each quoted, with the DEC that kept it. Under §6, add "This project's examples": routine, delegated and consult choices from §11, including this project's data-semantics examples as consult items unless a named policy delegates them. **ARPD starter:** update in place only the Version line (R-NN), the *Authority profile* line, the PI line and §6's examples. |
| 2 | `PARADIGM-SPEC.md` | `kit/templates/PARADIGM-SPEC.md`, or the starter's own | Depth follows the theory-context choice. **Theory not relevant or D:** §1 holds the PI's purpose verbatim, and the other sections say "Not applicable for this project (R-NN)". Create no pending research question. **A:** record the context in the PI's words, with no evaluation. **B:** the concerns the PI chose to keep go in §9 or as ASM items, labelled. **C, or correctness-critical semantics:** the full CON…VAL items, with definitions verbatim. §8 lists the exclusions from report §2. Never invent CON, OP or INV items. A draft-wording marker stays until the PI gives their own words. |
| 3 | `REQUIREMENTS.md` | `kit/templates/REQUIREMENTS.md`, or the starter's own | **Only the Adopted-on-adoption requirements** from report §3–4, with the same IDs. The table holds ID, plain-language requirement, source (R-NN, or the spec item), state Planned (except imported Verified evidence, `import-path.md`) and evidence. *Requirement details* holds each one's acceptance criteria, priority and dependencies, copied from the report. Proposed ones go to the backlog (row 4); Open ones go to *Waiting on the PI* (row 5). |
| 4 | `MASTER_PLAN.md` | `kit/templates/MASTER_PLAN.md`, or the starter's own | The objective (§1); milestones from report §9 (§2); the broad order of work (§3), each row "planning pending", with no invented sprint plans. The backlog (§4) holds deferred features, future-priority items and Proposed items left at adoption, each Backlogged and citing the report. Risks come from report §12. The cadence comes from §11. |
| 5 | `DECISIONS.md` | `kit/templates/DECISIONS.md`, or the starter's own | **R-NN:** the PI's words verbatim, `Adopts: reports/PROJECT-DEFINITION.md vN`, Given, Reading, Changes. **SA-01:** every field filled from report §11, in the PI's words or as "(drafted by the lead; PI assented: '<the PI's exact words>')". It states that data semantics are not delegated unless a named policy is quoted. **DEC entries:** each adopted material decision from report §6 (citing D-NN), the team arrangement, any import or move decisions (an import or install DEC cites `reports/IMPORT-BASELINE-<date>.md`, and an install DEC names the kit commit, `git -C <kit folder> rev-parse HEAD`), and anything owed. **Waiting on the PI:** one row per Open item in report §12, and per Provisional item with a gate, in its seven columns. *Needed by* is the gate. |
| 6 | `ARCHITECTURE.md` | `kit/templates/ARCHITECTURE.md`, or the starter's own | The overview (§1) and platform table (§2) come from report §5, and components and data flow (§3) likewise. *Architecture decisions* takes report §6's Adopted-on-adoption, Delegated and Provisional rows, with the same columns, each labelled; Proposed and Open rows are not copied. A-rules start as TARGET. Dependencies come from §5. |
| 7 | `STATUS.md` | `kit/templates/STATUS.md` (an imported one is **rewritten** in this format) | The **Readiness** block: `Setup: adopted (R-NN)`, `Planning: not started`, `Execution: not started`, `Next step: run /arpd-plan`. Add a line naming the adopted report: `reports/PROJECT-DEFINITION.md vN, commit <SHA from step 2>`. §2: "No sprint open". §4 *On deck*: run `/arpd-plan`. §5: a short summary of *Waiting on the PI*, pointing to `DECISIONS.md`. Base commit, the recovery block, and the UTC time from `date -u`. Any test command it names excludes the kit (*The project's test command*). The team, workspace and runtime-resource table. **§8:** the PI's working style from §11: review depth, theory-context choice, check-ins, how decisions are brought. No interview mode. **§6 *Owed*:** every item that could not be written; "Nothing owed" only when nothing is. |
| 8 | `INDEX.md` | `kit/templates/INDEX.md`, or the starter's own | All top-level paths that exist, including `reports/PROJECT-DEFINITION.md` (the adopted setup report) and the project's own. A later path gets "pending: <reason>". List `docs/discovery/` only if the notes are in the project. No empty directories. |
| 9 | `plans/README.md` | `kit/templates/plans/README.md` | Copy as is. |
| 10 | `reports/templates/` | `kit/templates/reports/*` | Copy as templates. Do not create `reports/sprints/`. |
| 11 | `reports/IMPORT-BASELINE-YYYY-MM-DD.md` | `kit/templates/reports/IMPORT-BASELINE.md` | **Import and install only.** The inherited baseline: source and provenance; each command as run, with its working directory, exit code and output **verbatim**; the test counts; any checker output; what was not run. Written once, then frozen. DECs and the first sprint cite it, and never copy it. |
| 12 | `tools/` | `kit/tools/*` | Copy `check_governance.py`, `next_plan_number.py`, `log_event.py`, `summarize_events.py` and `hooks/log_hook.py`, and copy `kit/LICENSE` to `tools/LICENSE`. An imported starter's differing tools are replaced, and the import DEC says so. |
| 13 | `.claude/settings.json` | `kit/settings/settings.json` | *Permission prompts*, below. If a settings file exists, merge only the `hooks` key and show the PI the diff. Check that `python` resolves (`python --version`); otherwise use `python3` or the full path. |
| 14 | `.claude/agents/` | `kit/agents/*` | *Permission prompts*. Copy only the roles the arrangement in report §10 uses (for example, only `reviewer.md` for solo with a fresh-subagent review). |
| 15 | `.claude/skills/arpd-*` | the kit's `.claude/skills/arpd-*` | **Install mode only.** *Permission prompts*. Copy all four folders whole, with their `references/`. |
| 16 | `docs/EVENTS.md` | `kit/docs/EVENTS.md` | Copy. |
| 17 | `AGENTS.md` | (write; an ARPD starter's is kept) | One line: "Read CLAUDE.md in full before doing anything else; it is this project's team charter." |
| 18 | `START-HERE.md` | (write; for an ARPD starter, a new one, with the old one moved to `docs/arpd-kit/START-HERE-starter.md`) | One screen for the PI, with: (a) each governing file's purpose in one line, plus the adopted report (`reports/PROJECT-DEFINITION.md vN`, commit <SHA>), described as the record of what was adopted; (b) the invariant / requirement / acceptance-criterion distinction, one line each; (c) the commands for the project's tests and the governance check; (d) a section of its own, *Next step*, with the exact prompt `/arpd-plan`. Current state appears only there, because `/arpd-plan` rewrites only that section. (e) One line each on `/arpd-plan` (drafts a plan; the PI approves it; work starts only when the PI says so), `/arpd-checkin` and `/arpd-amend`, naming a skill only if it exists; (f) what to expect at a sprint boundary; (g) *Known gaps*, with the exact commands for owed items, or "none". |
| 19 | `.gitignore` | (append; merge with an imported project's) | `logs/`, `output/`, `__pycache__/`, `.claude/settings.local.json`. |
| 20 | `docs/discovery/SETUP.md` | written during the interview | The final update marks the report as adopted by R-NN (vN), and says that the ruling and the governing documents, not these notes, are the authority. It is committed alone (step 3), then frozen. Never in install mode without consent. |
| 21 | `reports/PROJECT-DEFINITION.md` | written during the interview | Committed with `DECISIONS.md` in step 2. The Status line and banner are the only changes from the adopted version. Frozen afterwards; it is informative under `CLAUDE.md` §2. |

## Consistency check (after generating, before the final checker run)

Check across the documents, and against the adopted report:

- **`REQUIREMENTS.md`:**
  - every row has a *Requirement details* entry with at least one acceptance criterion;
  - every row matches an Adopted-on-adoption requirement in the report, with the same ID and the
    same meaning;
  - no Proposed requirement slipped in.
- **`ARCHITECTURE.md`:**
  - the decisions table matches report §6, with labels intact;
  - the platform table agrees with the decisions;
  - nothing in it is an unsupported guess.
- **`DECISIONS.md`:**
  - R-NN cites the report and its version;
  - SA-01 matches report §11, including the data-semantics rule;
  - *Waiting on the PI* holds every Open item, each with its gate.
- **`MASTER_PLAN.md`:** milestones and order match report §9, and the backlog holds the deferred and
  left-over Proposed items.
- **`CLAUDE.md`:** the team arrangement, authority profile, data rules and modules match report §10
  and §11.
- **`PARADIGM-SPEC.md`:** §8 matches report §2's exclusions, and the theory depth matches the
  choice.
- **`INDEX.md`** lists every governing file and the report. **`STATUS.md`** readiness says planning
  is pending.

Fix any contradiction that generation caused. Report any you cannot resolve to the PI, and record it
in `STATUS.md` §6. Never silently pick one side.

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
  exact commands below;
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
`.claude/` files stayed in the starter folder, use the `git mv` commands in `import-path.md`, step
3, instead. While `/arpd-plan` is owed, `START-HERE.md` still names planning as the next step, and
says to run these commands first.

## The project's test command

The `kit/` folder (and, in fresh and import modes, `examples/`) holds the kit's own tests. They are
not project tests. With pytest, every test command written in `START-HERE.md`, `STATUS.md` and the
import baseline is `python -m pytest --ignore=kit --ignore=examples`, plus the project's own
options.

**Working files.** Helper scripts and scratch files go outside the repository (the OS temp
directory or the session scratchpad). The notes and the report are the only exceptions. Commit with
`git commit -m "…"`, never with a message file.

## Then

1. Run `python tools/check_governance.py`, and fix any FAIL that generation caused.
2. **Search** the governing documents and `START-HERE.md`:
   - `<!--` must not remain, except `<!-- keep:` blocks; `grep -n "<!--" *.md | grep -v "<!-- keep:"`
     should print nothing;
   - `{{` must not remain;
   - on import, phrases the adoption made stale, such as "pending R-01", "Pending adoption" or "the
     importing PI", must be updated.
3. Log the adoption and the authority profile, using the actual IDs:
   - `python tools/log_event.py ruling --actor lead --ref R-01 --note "Project Definition Report vN adopted at setup"`;
   - `python tools/log_event.py ruling --actor lead --ref SA-01 --note "authority profile set at setup"`.
4. Check that the kit's pre-setup files are in `docs/arpd-kit/`, and that `kit/` stays as the module
   library.
5. Run `python tools/check_governance.py` again **after the final edit**. Quote its actual OVERALL
   line and any non-PASS or "not checked" lines, verbatim, in `STATUS.md` §4 and `START-HERE.md`.
   Never state a result from an earlier run.
6. Run `git status --short`, and remove any stray files you created. `docs/discovery/` and
   `reports/PROJECT-DEFINITION.md` must not appear, because they were committed in steps 2–3. Only
   then `git add -A` and `git commit -m "Set up ARPD project (ruling R-NN)"`.
7. Do not push without the PI's authorization.
8. Close out per `SKILL.md`, *Closeout and handoff*.
