# The Project Definition Report and generation

**Part A:** the report, from draft to adoption. **Part B:** what is written after adoption. The
session runs in the project folder; every path is relative to it. Never overwrite an existing file
(`import-path.md`). Setup writes **no sprint record** and creates no empty folder: `plans/` comes
with the first task plan, `reports/sprints/` with the first sprint.

---

# Part A: the report

## A1. Draft

Write `reports/setup/PROJECT-DEFINITION.md` from `arpd/templates/reports/PROJECT-DEFINITION.md`,
using the notes. Set the version line (v1), the Status line (`Draft v1`), the DRAFT banner, and a
date read from `date -u +%Y-%m-%dT%H:%MZ`, marked UTC. Install mode without consent: write it beside the
notes, outside the repository.

**Quality over length:** the full specification, proportional to complexity and risk (the
template's guidance says what each section holds). Also:

- §1: a project name only if the PI gave one; otherwise a working name labelled as yours. The
  intake answers (role and both axes, the PI, users and maintainers, where the project lives).
- §2: the research domain and questions in the PI's words (or "technical only, by the PI's
  choice"), and the traceability table: every research question or objective has a capability and
  requirements, and every P1 requirement serves one.
- §3: every constraint by class; every model commitment with its epistemic status; the
  commitments review's findings and the PI's decisions. Never a hypothesis as a Must hold, unless
  the PI kept it so after the review flagged it ("kept by the PI after the commitments review:
  '<words>'", with the consequence stated).
- §4–5: the minimum usable version, first-release type, exclusions and workflows in the PI's
  words; each requirement's Priority from Development (P1–P5), with Feasibility and
  Correctness-critical where they apply; a P1 requirement always has acceptance criteria ("pending
  O-01: …" if they depend on an Open decision); no requirement ranked above one it depends on.
- §9: every data-semantics item raised in the interview has its decider, or is Open with a gate.
- §12: every earlier PI preference carried forward (review depth, the role and scientific axis,
  sprint autonomy, check-ins), the PI's rules, the rules list with provenance and status, the
  data-semantics rule, and the modules with why.
- Citations: only sources actually checked; anything else labelled "unverified", with no invented
  bibliographic detail.
- **Existing code** (install, import, or a converted folder holding the PI's code): the baseline run
  (`import-path.md`, *Steps for a non-ARPD project*, step 1) is done before the first version is
  shown, and §10 states its result in one or two lines (what ran, what passed or failed, what was
  not run and why); the PI never adopts without seeing it. Its record names the commit it ran at.

**Statuses** are the template's. An item is **Adopted-on-adoption** only when the PI stated or
accepted it in words, quoted in its *Source*; your derivations and recommendations are **Proposed**
or **Provisional**. Never write "Adopted" or "Adopted by R-…" in a draft.

## A2. Completeness check

Before showing **any** version, v2 and later included, run
`python arpd/tools/check_report.py reports/setup/PROJECT-DEFINITION.md --stage draft` and fix every
FAIL (it reports the layout it detected: a new report is v0.7, 14 sections). Then run the whole
check in the notes template (`arpd/templates/setup/NOTES.md` §9),
consistency items included. **Report material gaps** in the report's *Completeness check: gaps
found* and in the presentation; never manufacture detail. Record the result in the notes.

## A3. Present

Before presenting, classify every proposal awaiting acceptance once, and use the same
classification in this turn and the approval request: **data semantics** (anything that decides what
a recorded or exported value means: blanks, duplicates, identifiers, timestamps, aggregation,
precision, a changed variable) or **other**. Option A below names the data-semantics proposals by ID
in its "Not included" note; if there are none, it says so.

Whenever this step or the review loop asks the PI to place or change a priority, the question
carries the one-line scale (on a five-point scale: P1 critical to the first working version, P2 needed next, P3 committed for later, P4 if time allows, P5 an idea) (`interview-guide.md`, Phase 5).

Show the major research, design and governance choices in a few lines each (the phase summaries
the PI confirmed are the basis; say what changed since); the report's path and version
(offer to show any section); the consequential open decisions with their gates; the gaps; and the
proposals awaiting acceptance (how many; the consequential ones by ID). Then ask
(`CHOICE FOR YOU (select one)`):

- A. Accept my proposals as written, and go to adoption. (Not included: data-semantics proposals,
  which are listed by ID in the approval request for you to accept or not, and Open items, which
  stay open unless you answer them.)
- B. Change something (say what).
- C. Go through the consequential proposals one by one.
- D. Reject this approach.

If no proposals await acceptance and nothing needs changing, go straight to A5. Picking A is not
adoption and needs no new version: the approval request states that the proposals are accepted by
choice A, and the ruling carries that acceptance. If the PI edits the file directly, read it back.

## A4. Review loop

- Every change after a version is shown makes a new version (vN+1), with a *Change history* row.
  Accepting proposals at adoption is not a change and makes no new version.
- Re-run A2 on the new version; present briefly what changed and what is still open.
- Resolve each proposal the PI has not accepted to a status in the template's table, or leave it
  Proposed (not adopted; backlog). **Exception: a data-semantics proposal the PI has not accepted
  becomes Open**, gated "before implementing <the feature it affects>", with its own row in
  *Waiting on the PI*; it never goes to the backlog, and nothing that depends on it is built. An
  O-NN is resolved only by the PI's answer to it ("Resolved:" in §13). A rejection: ask what to
  change; nothing is adopted.

## A5. Adoption

Ask with `APPROVAL REQUIRED`. Name the file and version, what a yes adopts, and what it does not
authorize. List each unanswered **data-semantics proposal** and each **Open item** by ID and one
line, and say that only the proposals the PI names are accepted, and the Open items stay open. The
PI may adopt and accept named proposals in one reply ("adopt v3 with REQ-DATA-02 and D-04
accepted"). For example:

```text
────────────────────────────────
**✋ APPROVAL REQUIRED**
Adopt reports/setup/PROJECT-DEFINITION.md v3? A yes, in your own words, becomes ruling R-01. It
adopts the items marked Adopted-on-adoption and my other proposals (your choice A), and records the
delegated, provisional, open and excluded items as such. These data-semantics proposals are
accepted only if you name them: REQ-DATA-02 (a skipped item is exported as an empty cell); D-04 (a
repeated export rewrites the whole file). These stay open: O-01 (entries per student; before
implementing the entry screen). I then write the governing documents from it. It does not approve a
sprint plan or start any implementation.
────────────────────────────────
```

For an ARPD starter, the block also names the path updates and removals the import makes
(`import-path.md`, *Steps for an ARPD starter*, step 2), so that the adoption authorizes them.

Then:

- Record the reply **verbatim** as R-NN, with `Adopts: reports/setup/PROJECT-DEFINITION.md vN`, the
  date from `date -u`, and `Recorded in: the commit "Record adoption ruling R-NN (setup in
  progress)", with the adopted report`. The *Reading* lists the proposals the ruling accepted (by
  ID; by choice A, or named), and maps each open O-NN to its *Waiting on the PI* row (#N).
- A plain assent ("ok", "aproved") is recorded exactly as given, with the line "(PI assented to
  reports/setup/PROJECT-DEFINITION.md vN, as read back: '<the block's text>')". It accepts no
  data-semantics proposal: each becomes Open with its gate and a *Waiting on the PI* row (A4).
- If the reply assents but adds something that could change the report, do not record the
  adoption: revise to vN+1 and ask once more (`arpd/docs/INTERACTION.md`, *A reply to an approval
  that also adds something*).
- Interview choices were preferences, and "move on" was not adoption. Only this ruling adopts.

---

# Part B: generation (only after the ruling)

**IDs** continue the existing ledger (`import-path.md`, *Numbering*). **Dates** are read, never
estimated (without `date`:
`python -c "import datetime; print(datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%MZ'))"`).
**Where each item goes** is the report template's status table; a proposal the ruling accepted
counts as Adopted-on-adoption, with the ruling as its source.

## Commit order

1. **Move-only commits** (import and install): prior instruction files to
   `docs/prior-instructions/`. Each alone, staging only those paths; `git show --stat
   --find-renames HEAD` shows renames with no content change.
2. **The adoption, first.** Write `DECISIONS.md` (row 5), with R-NN and SA-01. Make the report's
   only post-adoption edit: the Status line `Adopted by R-NN (vN)` and the template's ADOPTED banner
   in place of DRAFT. Run `check_report.py` (as A2) with `--stage adopted` and fix every FAIL. Commit
   the two files together, and nothing else:
   `git add DECISIONS.md reports/setup/PROJECT-DEFINITION.md && git commit -m "Record adoption ruling R-NN (setup in progress)"`.
   The report is then frozen; its SHA (`git rev-parse HEAD`) goes in `STATUS.md` and
   `START-HERE.md`. Install mode without consent: copy the adopted report into the target first.
3. **The notes, alone** (row 13), if in the project: a last update, then
   `git add reports/setup/NOTES.md && git commit -m "Setup notes (non-governing)"`. Then frozen; a
   correction gets its own commit ("Correct setup notes (non-governing)").
4. **The import baseline, alone** (import, install, or a conversion that kept code of the PI's; row 10), right after the notes:
   `git add reports/setup/IMPORT-BASELINE.md && git commit -m "Import baseline (non-governing)"`.
   Then the remaining files, committed at the end (*Then*).
5. **`.claude/`** (*Permission prompts*).
6. **An ARPD starter's remove-only commit, last** (`import-path.md`, starter step 3): only after
   step 5 has re-pointed the starter's hooks to `arpd/tools/hooks/`, because a hook whose script is
   missing blocks every prompt. If the PI declined step 5, keep `tools/hooks/` and say so in the
   "event logging not installed" DEC. `git show --stat HEAD` shows deletions only.

## Every generated file

- Remove guidance comments (`<!-- … -->`, except `<!-- keep:`), fill every `{{…}}`; an empty
  example row becomes "None yet".
- **Generate from the adopted report only:** no material rule, requirement, limit or detail the
  report and ruling lack; anything new goes to *Waiting on the PI* or a routine DEC.
- **Check each row** against the report; a contradiction you cannot resolve goes to the PI and
  `STATUS.md` §6.

**Without Python** (`arpd/docs/NO-PYTHON.md`): `check_report.py` and `check_governance.py` become
the read-throughs of its §4 and §5, quoted as such; `log_event.py` steps are skipped; `install.py
owed .` is `sh arpd/tools/install.sh owed .`, which installs the agent roles and skills but not the
hooks (record "event logging not installed", reason "Python not available"); `STATUS.md` §6 records
that Python is not available.

Templates are in `arpd/templates/`; `arpd/` itself is never edited. A starter's own files are
updated in place.

| # | File | How to fill it, and check |
|---|---|---|
| 1 | `CLAUDE.md` | **A prior `CLAUDE.md` that is not the setup stub is moved first** (*Commit order* 1: `git mv CLAUDE.md docs/prior-instructions/CLAUDE.md` in a move-only commit; check `git show --stat --find-renames HEAD`), and only then is the charter written. From `arpd/constitution/CORE.md`, replacing the "Setup in progress" stub. Fill every `{{…}}` from report §1, §2, §9, §12 (`{{AUTHORITY_PROFILE}}`: the name only; `{{AGENT_ROLE}}`: the role in the PI's words, with both axes; `{{SCIENTIFIC_AXIS_MEANING}}`: the axis named, in one phrase). Append the selected modules under Part B (science first, then `team/team-arrangement.md` filled in; drafts marked "(draft module, untested)"); then `B.P-PROJECT: Project rules`: every accepted rule of report §12 that is not a Core ARPD rule, each with its provenance (PI rules quoted), and kept prior instructions, quoted, with their DEC. Proposed or excluded rules are not written. §6 examples from §12, data semantics as consult unless a named policy delegates them; `{{SPRINT_AUTONOMY}}` (§8) from the sprint autonomy in the PI's words ("several sprints" stays a check-in at each boundary until an SA authorizes a series through `/arpd-plan`). **Starter:** only the lines `import-path.md` names. |
| 2 | `PARADIGM-SPEC.md` | By the scientific axis. **Technical only:** §1 the PI's purpose verbatim; other sections "Not applicable for this project (R-NN)", except correctness-critical semantics. **Respect as given:** the domain, questions and commitments in the PI's words. **Alignment review:** also the concerns the PI kept, labelled. **Co-development, or correctness-critical semantics:** the full CON…VAL items, verbatim. Model commitments from report §3 as ASM items with their epistemic status; Must hold items as INV; open questions as research questions, never invariants. §8: report §4's exclusions and §3's framing choices. Never invent CON, OP or INV items, or citations. |
| 3 | `REQUIREMENTS.md` | The requirements the status table sends here (P1–P3), same IDs: requirement, source (R-NN or spec item), state Planned (except imported Verified evidence), evidence; *Requirement details*: acceptance criteria, priority, feasibility, correctness-critical flag, the research question served, and dependencies from the report. *Check:* every row has details with at least one criterion; nothing Proposed (unless the *Reading* accepts it), Open, P4 or P5 slipped in. |
| 4 | `MASTER_PLAN.md` | Objective (§1–2); milestones from report §11 (M1 = the P1 requirements to the first-release standard); the broad order of work, feasibility investigations before what depends on them, each row "planning pending", no invented sprints; the backlog (P4, P5 and unaccepted proposals), each Backlogged with its priority and citing the report; risks (§13); cadence (§12). |
| 5 | `DECISIONS.md` | **R-NN:** as A5. **SA-01:** every field from report §12, in the PI's words or "(drafted by the lead; PI assented: '<the PI's exact words>')"; data semantics delegated only under a quoted named policy. **DECs:** each adopted decision of report §8 (citing D-NN), the team arrangement, the folder's preparation (conversion, import, install, move or removal; citing `reports/setup/IMPORT-BASELINE.md` where one exists and the kit commit in `arpd/VERSION`), each reframing of a model commitment the PI accepted, anything owed. **Waiting on the PI:** a row per Open or gated Provisional item and per feasibility investigation; *Needed by* is the gate. |
| 6 | `ARCHITECTURE.md` | Overview, platform table, components and data flow from report §7; *Architecture decisions*: the §8 rows the status table sends here, labelled; A-rules start as TARGET. *Check:* the platform table agrees with the decisions. |
| 7 | `STATUS.md` | (an imported one is rewritten in this format) **Readiness** as `SKILL.md`, *Closeout*, plus the report version and commit. §2 "No sprint open"; §4 *On deck*: `/arpd-plan`; §5 points to *Waiting on the PI*; base commit, recovery block, UTC time; **§8** the PI's working style, role and scientific axis (as in the charter §1), sprint autonomy and review depth (as SA-01; no interview mode); **§6 *Owed*:** every item not installed, or "Nothing owed". |
| 8a | `README.md` | Only if the project has none (a converted clone has none): a few lines, the project's name and purpose (report §1, the PI's words), "Start at START-HERE.md", and the test command. Never overwrite an existing README. |
| 8 | `START-HERE.md` | From `arpd/templates/START-HERE.md` (a starter's is rewritten; its `INDEX.md` folded into the *Map* and removed), one screen, the template's sections: **Next step** holds the exact prompt `/arpd-plan` (current state only there); **Map** lists every top-level entry, one line each ("pending: <reason>" for a later one); **Known gaps** has exact commands, or "none". *Check:* the checker's map step passes. |
| 9 | `AGENTS.md` | (a starter's is kept) One line: "Read CLAUDE.md in full before doing anything else; it is this project's team charter." |
| 10 | `reports/setup/IMPORT-BASELINE.md` | **Import, install, or a conversion that kept code of the PI's, only,** from its template: each command (run as `<command>; echo "exit=$?"`) with its working directory, the printed exit code and the full output **verbatim**, never trimmed; what was not run. Committed alone after the notes (*Commit order* 4), then frozen; cited, never copied. |
| 11 | `arpd/`, `.claude/skills/arpd-*` | Present since bootstrap. Verify that `arpd/VERSION` names the kit version, `arpd/tools/` holds `check_governance.py`, `check_report.py`, `log_event.py`, `summarize_events.py` and `next_plan_number.py`, and the four skills exist. If stale: `python arpd/tools/install.py update . --kit "<kit clone>"` on the PI's yes, recorded by a DEC. |
| 12 | `.gitignore` | Written by `install.py`: verify `arpd/logs/`, `output/`, `__pycache__/`, `.claude/settings.local.json`; the project's own lines are kept. |
| 13 | `reports/setup/NOTES.md` | The final update marks the report adopted by R-NN (vN), and says the ruling and governing documents, not the notes, are the authority. Committed alone (step 3). Never in install mode without consent. |
| 14 | `reports/setup/PROJECT-DEFINITION.md` | Committed with `DECISIONS.md` (step 2); Status line and banner the only changes. Frozen; informative under `CLAUDE.md` §2. |
| 15 | `.claude/settings.json`, `.claude/agents/` | `python arpd/tools/install.py owed .` (*Permission prompts*): the event-logging hooks (into an existing settings file, only the `hooks` key is merged), the agent roles, any missing skill. First check that `python` resolves (`python --version`); if not, say so. |

## Permission prompts for `.claude/`

Last (for an ARPD starter, only its remove-only commit follows), as one step on its own, so a
refusal blocks nothing else.

1. **Tell the PI first** what each item is for, and that both are plain files ARPD already ships in
   `arpd/`, copied into `.claude/`: nothing is downloaded or installed. Do not call this step
   "installing" to the PI (`arpd/docs/INTERACTION.md` §6). Then ask, for example:

   ```text
   ────────────────────────────────
   **🔘 CHOICE FOR YOU (select one)**
   Approve including the event-logging and agent-role files in this project? (Plain files ARPD
   already has, copied from arpd/ into .claude/; nothing is downloaded or installed.)
   A. Yes, include both now.
   B. Not now: I note them as still to add, with the command for you to run later.
   ────────────────────────────────
   ```

   - "Event logging: a small script that is already in the project records, for each event, its
     time and type (a prompt was sent, a tool ran, a turn ended). It records no prompt text and no
     file contents. It needs Python; without Python it is left out."
   - "Agent roles: plain-text definitions of the reviewer, implementer and tester the lead delegates
     to." Say which ones the team arrangement uses.
2. **Run `python arpd/tools/install.py owed .` only after the PI says yes in the chat,** whatever
   the tool allows; if Claude Code also asks, the PI approves there too. Quote its output, then
   `git add .claude && git commit -m "Add ARPD .claude files (logging settings, agent roles)"`. Never choose a method because it
   avoids a permission prompt.

If the PI declines, or the command is blocked or exits 2: record a DEC titled "event logging not
installed", "agent files not installed" or "skills not installed", with the reason and route; list
the item in `STATUS.md` §6–7 and `START-HERE.md` *Known gaps* with the command for **the PI** to run
later (`python arpd/tools/install.py owed .`, plus `--kit "<kit clone>"` for a missing skill, then
the commit) and which happened ("the PI agreed, but Claude Code's permission prompt did not allow
the write" or "the PI declined"); continue. The checker then reports ADVISORY, not MISSING.

## The project's test command

The kit's tests are not in the project: the test command in `START-HERE.md`, `STATUS.md` and the
import baseline is the project's own (with pytest, `python -m pytest` plus its options). Helper and
scratch files go outside the repository (OS temp or the session scratchpad). Commit with
`git commit -m "…"`, never a message file.

## Then

1. Run `python arpd/tools/check_governance.py`, and fix any FAIL that generation caused.
2. `grep -n "<!--" *.md | grep -v "<!-- keep:"` prints nothing and no `{{` remains; on import,
   stale phrases ("pending R-01", "the importing PI") are updated.
3. Log, with the actual IDs: `python arpd/tools/log_event.py ruling --actor lead --ref R-01 --note "Project Definition Report vN adopted at setup"`
   and `python arpd/tools/log_event.py ruling --actor lead --ref SA-01 --note "authority profile set at setup"`.
4. `arpd/` is unedited: `git status --short arpd` prints nothing (install mode: only `?? arpd/`,
   committed in step 6).
5. Run `python arpd/tools/check_governance.py` again **after the final edit**, and quote its actual
   OVERALL line and any non-PASS or "not checked" lines verbatim in `STATUS.md` §4 and
   `START-HERE.md`. Never state a result from an earlier run.
6. `git status --short`: remove any stray files you created; the notes and the report must not
   appear. Only then `git add -A && git commit -m "Set up ARPD project (ruling R-NN)"`.
7. Do not push without the PI's authorization. Close out per `SKILL.md`, *Closeout and handoff*.
