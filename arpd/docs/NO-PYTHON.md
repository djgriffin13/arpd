# Running ARPD without Python

ARPD's tools are Python (standard library only). Everything ARPD is for still works without Python:
the setup interview, preparing the project folder, the Project Blueprint and its adoption,
the governing documents, planning, check-ins and amendments. What is lost is automation: the event
log and its hooks, the two checkers (replaced below by a read-through, which is weaker), and ARPD's
own test suite. This file says what to do instead of each `python arpd/tools/...` command. It is
not a governing document; the charter (`CLAUDE.md`) points here.

## 1. Which mode a session is in

Before the first `python arpd/tools/...` command in a session, run `python --version`, then, if that
fails or is older than 3.8, `python3 --version`.

- **Python 3.8+ found:** use it for every tool command (write `python3` where the text says
  `python`, if only `python3` works). This file does not apply.
- **Neither works:** this session runs **without Python**. Say so once, in the turn in which you found
  it out (usually the first), in one sentence naming all three things skipped (the event log, the
  automated checks, ARPD's own tests) and that the PI can install Python later. Record it: during setup in the notes' §1 (*Python: not available; arpd/docs/NO-PYTHON.md*),
  and after adoption in `STATUS.md` §6 *Owed* (*Python not available: event log not kept;
  checkers replaced by read-throughs; see arpd/docs/NO-PYTHON.md*) and in `START-HERE.md` *Known
  gaps* (*No event log and no automated checks: Python is not available. Records were checked by
  reading, not by the checkers.*). Then follow the sections below.

Never install Python or any package for the PI without asking, and never ask the PI to install it as
a condition of continuing.

## 2. Instead of each tool

| Python command | Without Python |
|---|---|
| `python arpd/tools/install.py <command> ...` | `sh arpd/tools/install.sh <command> ...`, the same arguments (§3) |
| `python arpd/tools/check_report.py <report> --stage draft\|adopted` | The report read-through (§4) |
| `python arpd/tools/check_governance.py` | The governance read-through (§5) |
| `python arpd/tools/log_event.py ...` | Skip it. Nothing is logged; `STATUS.md` §6 says so (§1) |
| `python arpd/tools/summarize_events.py ...` | Skip it; on recovery, use `git log --oneline <base>..HEAD` and the sprint records, and say the event log is not kept |
| `python arpd/tools/next_plan_number.py` | One more than the highest `NNN` among the `plans/NNN-*.md` files in the working tree and on every local and remote branch (001 if none): `ls plans; for r in $(git for-each-ref --format='%(refname)' refs/heads refs/remotes); do git ls-tree --name-only "$r" plans/; done` |
| `python -c "import datetime; ..."` (a UTC time) | `date -u +%Y-%m-%dT%H:%MZ` |
| `python arpd/tools/install.py owed .` | `sh arpd/tools/install.sh owed .`: installs the agent roles and any missing skill, never the hooks (they run Python). Record the DEC "event logging not installed" with the reason "Python not available" |
| The project's tests (`python -m pytest`) | The project's own test command, if its language has one; a Python project needs Python (say so, and record the tests as not run) |

## 3. Preparing the folder: `install.sh`

`arpd/tools/install.sh` is the no-Python twin of `install.py`, in plain shell and git (which Claude
Code already needs). `convert`, `new`, `install`, `import` (git sources only), `update` and `owed`
take the same arguments, print the same plans, warnings and refusals, and leave the same result,
including the backup folder a conversion moves the kit's files and old git history into. Run it as
`sh arpd/tools/install.sh <command> ...` from the same folder the skill names. Differences:

- **No hooks:** `owed` installs the agent roles and skills, and reports the hooks as not installed
  (exit 2).
- **No folder import:** importing a plain folder (not a git repository) is refused; copy the folder
  in by hand, with the PI's agreement after showing what it holds, or install Python.

## 4. The report read-through (instead of `check_report.py`)

Before showing each version of `reports/setup/PROJECT-BLUEPRINT.md`, read it against these rules
and fix every breach; at adoption, read the header again for the adopted form. Record the result
in the notes' §9 and in the blueprint's *Completeness check* as "Structure checked by reading (no
Python), vN: <breaches fixed, or none found>". Never write that `check_report.py` passed.

1. **Header:** a `Version: vN` line and a `Status:` line. A draft says `Draft vN` (same N), carries
   the DRAFT banner, and never says "Adopted by R-NN" in the header. An adopted blueprint says `Adopted
   by R-NN (vN)` with the Version line's N.
2. **Sections 1–14,** in order, each with content or "Not applicable: <reason>"; no `{{...}}` left
   outside comments.
3. **Every requirement** (`#### REQ-<AREA>-NN: <name>`, unique IDs, heading level 4) has Acceptance
   criteria with at least one bullet; a Priority of P1–P5 (or "open (O-NN)"); a Source; one Status
   (Adopted on adoption only with the PI's quoted words or "PI accepted: '...'"; never "Adopted" in
   a draft except "Adopted (inherited, R-NN)"; Proposed; Provisional; Delegated (SA-NN); Open
   (before <stage>); Excluded). *Feasibility*, if present, is "established" or "to investigate:
   <what>" with a gate; *Correctness-critical*, if present, is "yes: <why>" or "no".
4. **Priorities respect dependencies:** no requirement has a lower P number (higher priority) than a
   requirement it lists in *Dependencies*. A correctness-critical requirement at P4 or P5 is
   questioned with the PI.
5. **§8** has the table Decision | Alternatives considered | Recommendation | Rationale | Status |
   Consequences; every row names alternatives (or "none credible: <reason>"); an Open row names a
   gate.
6. **§13:** every open item names a gate ("before" plus a stage); a closed one starts with
   "Resolved:", "Closed:" or "Excluded:". An item gated "before planning" (not "before planning
   <a later milestone or sprint>") was asked, or says "deferred by the PI".
6a. **§3:** no row classed Must hold (an invariant) is a hypothesis, unless it says it was "kept by
   the PI after the commitments review".
7. **§14** says adoption does not authorize implementation.
8. A *Completeness check* section exists.

## 5. The governance read-through (instead of `check_governance.py`)

Where a skill says to run the checker and quote its OVERALL line (including `START-HERE.md`'s
*Governance check* line and an older starter's `python tools/check_governance.py`), read the records
instead and quote this line exactly: "`check_governance.py` not run (no Python). Read-through: <what was checked>;
<problems found, or 'no problem found'>." Never write PASS, FAIL or INCOMPLETE as if the checker ran.
Check, in proportion to what changed:

1. `CLAUDE.md`'s Version line names an adoption ruling R-NN that exists in `DECISIONS.md` and is
   not pending; no `{{...}}` left in any governing document (outside comments and code).
2. `REQUIREMENTS.md`: valid states; Verified and Validated rows carry evidence; Validated rows cite
   a ruling; every requirement in the table has a *Requirement details* entry with at least one
   acceptance criterion.
3. `plans/`: unique numbers.
4. Each closed sprint record: a decision-tracking table whose every row has a route (routine /
   delegated / consult); each consequential decision cites its authority (SA-NN for delegated,
   R-NN for consult), which exists in `DECISIONS.md` and is not pending, and records whether it was
   authorized before adoption. A row still pending in a closed record is settled when a later
   ruling (or the DEC-NN it creates) names the record and the row's ID or Waiting #.
5. Each open sprint record's Part 1: the *Approved plan* and *Execution authorized by* rows cite
   rulings that exist and are not pending, and the plan file and version they name exist.
6. `START-HERE.md`'s *Map* lists every top-level entry, and every path it lists exists (or is marked
   "pending:").
7. The skills `arpd-plan`, `arpd-checkin` and `arpd-amend` are in `.claude/skills/`; the agent roles
   are in `.claude/agents/` when the team uses subagents; event logging is recorded as not installed.

## 6. When Python becomes available later

Run `python arpd/tools/install.py owed .` (the hooks), commit, and run
`python arpd/tools/check_governance.py`; quote its output. Update `STATUS.md` §6 to remove the
"Python not available" item. Nothing else changes: the records written without Python are the same
records.
