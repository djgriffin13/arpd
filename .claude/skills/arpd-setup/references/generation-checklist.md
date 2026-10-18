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

- §1: a project name only if the PI gave one; otherwise a working name labelled as yours.
- §2–3: scope tiers, exclusions and workflows in the PI's words; Priority follows the scope
  answers; a required requirement always has acceptance criteria ("pending O-01: …" if they depend
  on an Open decision).
- §7: every data-semantics item raised in the interview has its decider, or is Open with a gate.
- §11: every earlier PI preference carried forward (review depth, theory-context choice, autonomy,
  check-ins), the data-semantics rule, and the modules with why.

**Statuses** are the template's. An item is **Adopted-on-adoption** only when the PI stated or
accepted it in words, quoted in its *Source*; your derivations and recommendations are **Proposed**
or **Provisional**. Never write "Adopted" or "Adopted by R-…" in a draft.

## A2. Completeness check

Before showing **any** version, v2 and later included, run
`python arpd/tools/check_report.py reports/setup/PROJECT-DEFINITION.md --stage draft` and fix every
FAIL. Then run the whole check in the notes template (`arpd/templates/setup/NOTES.md` §10),
consistency items included. **Report material gaps** in the report's *Completeness check: gaps
found* and in the presentation; never manufacture detail. Record the result in the notes.

## A3. Present

Show the major design and governance choices in a few lines each; the report's path and version
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
  O-NN is resolved only by the PI's answer to it ("Resolved:" in §12). A rejection: ask what to
  change; nothing is adopted.

## A5. Adoption

Ask with `APPROVAL REQUIRED`. Name the file and version, what a yes adopts, and what it does not
authorize. List each unanswered **data-semantics proposal** and each **Open item** by ID and one
line, and say that only the proposals the PI names are accepted, and the Open items stay open. The
PI may adopt and accept named proposals in one reply ("adopt v3 with REQ-DATA-02 and D-04
accepted"). For example:

```text
────────────────────────────────
APPROVAL REQUIRED
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
4. **The import baseline, alone** (import and install; row 10), right after the notes:
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

Templates are in `arpd/templates/`; `arpd/` itself is never edited. A starter's own files are
updated in place.

| # | File | How to fill it, and check |
|---|---|---|
| 1 | `CLAUDE.md` | From `arpd/constitution/CORE.md`, replacing the "Setup in progress" stub. Fill every `{{…}}` from report §1, §7, §10–11 (`{{AUTHORITY_PROFILE}}`: the name only). Append the selected modules under Part B (science first, then `team/team-arrangement.md` filled in; drafts marked "(draft module, untested)"); kept prior instructions as `B.P-PROJECT: Project rules`, quoted, with their DEC. §6 examples from §11, data semantics as consult unless a named policy delegates them. **Starter:** only the lines `import-path.md` names. |
| 2 | `PARADIGM-SPEC.md` | By the theory-context choice. **Not relevant, or D:** §1 the PI's purpose verbatim; other sections "Not applicable for this project (R-NN)". **A:** the context in the PI's words. **B:** the concerns the PI kept, labelled. **C, or correctness-critical semantics:** the full CON…VAL items, verbatim. §8: report §2's exclusions. Never invent CON, OP or INV items. |
| 3 | `REQUIREMENTS.md` | The requirements the status table sends here, same IDs: requirement, source (R-NN or spec item), state Planned (except imported Verified evidence), evidence; *Requirement details*: acceptance criteria, priority and dependencies from the report. *Check:* every row has details with at least one criterion; nothing Proposed (unless the *Reading* accepts it), Open or future-priority slipped in. |
| 4 | `MASTER_PLAN.md` | Objective (§1); milestones from report §9; the broad order of work, each row "planning pending", no invented sprints; the backlog, each Backlogged and citing the report; risks (§12); cadence (§11). |
| 5 | `DECISIONS.md` | **R-NN:** as A5. **SA-01:** every field from report §11, in the PI's words or "(drafted by the lead; PI assented: '<the PI's exact words>')"; data semantics delegated only under a quoted named policy. **DECs:** each adopted decision of report §6 (citing D-NN), the team arrangement, import, move or removal (citing `reports/setup/IMPORT-BASELINE.md` and the kit commit in `arpd/VERSION`), anything owed. **Waiting on the PI:** a row per Open or gated Provisional item; *Needed by* is the gate. |
| 6 | `ARCHITECTURE.md` | Overview, platform table, components and data flow from report §5; *Architecture decisions*: the §6 rows the status table sends here, labelled; A-rules start as TARGET. *Check:* the platform table agrees with the decisions. |
| 7 | `STATUS.md` | (an imported one is rewritten in this format) **Readiness** as `SKILL.md`, *Closeout*, plus the report version and commit. §2 "No sprint open"; §4 *On deck*: `/arpd-plan`; §5 points to *Waiting on the PI*; base commit, recovery block, UTC time; **§8** the PI's working style and review depth (as SA-01; no interview mode); **§6 *Owed*:** every item not installed, or "Nothing owed". |
| 8 | `START-HERE.md` | From `arpd/templates/START-HERE.md` (a starter's is rewritten; its `INDEX.md` folded into the *Map* and removed), one screen, the template's sections: **Next step** holds the exact prompt `/arpd-plan` (current state only there); **Map** lists every top-level entry, one line each ("pending: <reason>" for a later one); **Known gaps** has exact commands, or "none". *Check:* the checker's map step passes. |
| 9 | `AGENTS.md` | (a starter's is kept) One line: "Read CLAUDE.md in full before doing anything else; it is this project's team charter." |
| 10 | `reports/setup/IMPORT-BASELINE.md` | **Import and install only,** from its template: each command (run as `<command>; echo "exit=$?"`) with its working directory, the printed exit code and the full output **verbatim**, never trimmed; what was not run. Committed alone after the notes (*Commit order* 4), then frozen; cited, never copied. |
| 11 | `arpd/`, `.claude/skills/arpd-*` | Present since bootstrap. Verify that `arpd/VERSION` names the kit version, `arpd/tools/` holds `check_governance.py`, `check_report.py`, `log_event.py`, `summarize_events.py` and `next_plan_number.py`, and the four skills exist. If stale: `python arpd/tools/install.py update . --kit "<kit clone>"` on the PI's yes, recorded by a DEC. |
| 12 | `.gitignore` | Written by `install.py`: verify `arpd/logs/`, `output/`, `__pycache__/`, `.claude/settings.local.json`; the project's own lines are kept. |
| 13 | `reports/setup/NOTES.md` | The final update marks the report adopted by R-NN (vN), and says the ruling and governing documents, not the notes, are the authority. Committed alone (step 3). Never in install mode without consent. |
| 14 | `reports/setup/PROJECT-DEFINITION.md` | Committed with `DECISIONS.md` (step 2); Status line and banner the only changes. Frozen; informative under `CLAUDE.md` §2. |
| 15 | `.claude/settings.json`, `.claude/agents/` | `python arpd/tools/install.py owed .` (*Permission prompts*): the event-logging hooks (into an existing settings file, only the `hooks` key is merged), the agent roles, any missing skill. First check that `python` resolves (`python --version`); if not, say so. |

## Permission prompts for `.claude/`

Last (for an ARPD starter, only its remove-only commit follows), as one step on its own, so a
refusal blocks nothing else.

1. **Tell the PI first** what each item is for, and ask
   (`CHOICE FOR YOU (select one)`: install them now / skip them for now, and they are owed):
   - "Event logging: a small script records, for each event, its time and type (a prompt was sent,
     a tool ran, a turn ended). It records no prompt text and no file contents."
   - "Agent roles: the definitions of the reviewer and implementer the lead delegates to."
2. **Run `python arpd/tools/install.py owed .` only after the PI says yes in the chat,** whatever
   the tool allows; if Claude Code also asks, the PI approves there too. Quote its output, then
   `git add .claude && git commit -m "Install ARPD .claude files"`. Never choose a method because it
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
