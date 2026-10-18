# Import and install paths

Use these when the project starts from existing code: the PI's own, a published model's code, or a
starter project. **Preserve existing work. Never silently merge or overwrite instructions.**

## Modes

| Mode | Invocation | What happens |
|---|---|---|
| **Import into this repository** | `/arpd-setup import <path-or-git-url>` | The existing codebase is brought into this kit repository, keeping its history when it is a git repo. This repository becomes the project. |
| **Install into an existing repository** | `/arpd-setup install <path>` | The charter, governing documents, tools, hooks and agents are installed **into** the existing repository at `<path>`. The kit's `kit/` folder is copied there whole, and the `arpd-*` skills (`arpd-setup`, `arpd-plan`, `arpd-checkin`, `arpd-amend`, each with its `references/`) go to the target's `.claude/skills/`, so later planning, check-ins and amendments work. The skills are a `.claude/` write, done last with the PI's approval (`generation-checklist.md`, row 15); if it is blocked, they are owed. The kit repository is left unchanged. |

- **Import** suits code that is small or not under the PI's control, such as a published model or a
  starter. A starter that already lives inside this kit (for example `examples/march-1991/`) is an
  import.
- **Install** suits the PI's own ongoing repository.
  - The copied `kit/` folder holds the kit's own tests (`kit/tools/test_*.py`). They are not project
    tests: after the copy, run the project's tests as `python -m pytest --ignore=kit` (with pytest),
    and check the count matches the baseline (`generation-checklist.md`, *The project's test
    command*).
  - Never `git mv` anything out of the copied `kit/`: owed `.claude/` items are copied from it, with
    the commands in `generation-checklist.md`, *Commands for owed `.claude/` items*.
- **Ask the PI which mode, if it is unclear.**

Then decide which kind of project is coming in, because the steps differ:

- **Non-ARPD project:** it has no `PARADIGM-SPEC.md` and governing documents. Follow *Steps for a
  non-ARPD project*.
- **ARPD project (a starter):** it already has `CLAUDE.md`, `PARADIGM-SPEC.md`, `DECISIONS.md` and
  the other governing documents. Follow *Steps for an ARPD starter*. Its `CLAUDE.md` and `AGENTS.md`
  **are its charter**: they are kept and updated in place, never treated as prior instructions.

## The kit's own files are not prior instructions

In fresh and import modes, this repository's root holds the kit's own pre-setup files: `README.md`,
`QUICKSTART.md`, `CLAUDE.md`, `AGENTS.md`, `LICENSE`, `CITATION.cff` and `RELEASE-NOTES.md`. They
describe the kit, not
the project. The PI chooses the project's own licence.

- **Move them** to `docs/arpd-kit/` with `git mv`, in a commit of their own (see *Move-only commits*).
- **Never** treat them as project instructions: do not reconcile them, do not move them to
  `docs/prior-instructions/`, and do not write `.arpd` files beside them.
- In install mode they are not copied to the target repository, so the question does not arise.

## Move-only commits (keep the history)

Git follows a file's history through a rename only when it can match the old and new file. A commit
that moves a file **and** edits it can break that match, and then `git log --follow` and `git blame`
lose everything before the move. So:

1. **Commit 1, moves only:** `git mv` the kit's own files to `docs/arpd-kit/`. Commit: "Move kit
   pre-setup files to docs/arpd-kit (no changes)".
2. **Commit 2, moves only** (import of a starter inside the kit): `git mv` the starter's files to the
   project root. Commit: "Move <starter> to the project root (no changes)".
3. **Only then** edit anything.

Do the moves at the start of generation, after the PI has adopted the report. Check each move
commit with `git show --stat --find-renames HEAD`: every line should be a rename with no content
change. The notes and the draft report are untracked at this point. Stage only the moves, so that
neither enters a move commit. The report is committed with the adoption ruling, and the notes alone
after it (`generation-checklist.md`, *Commit order*).

## Working files in import and install modes

The working notes (`docs/discovery/SETUP.md`) and the draft report (`reports/PROJECT-DEFINITION.md`)
are the only files written before adoption. Both are non-governing (`SKILL.md`, *Working files
before adoption*).

- **Import:** the project root is this repository. Write both here, and tell the PI once.
- **Install:** the target is the PI's own repository, which may be shared or public. Before the
  first write, ask once for consent to save both files there, naming the paths. Record the answer
  in the notes' *Mode and consent*.
  - **With consent:** write them there, uncommitted until adoption. The report is then committed
    with the adoption ruling, and the notes alone.
  - **Without consent:** keep both in the OS temp directory, and tell the PI the path. Say that a
    later session can resume from them only if the PI gives that path. At adoption, the adopted
    report is written into the target, because adoption authorizes it. The notes are never added
    unless the PI later asks.
- Never commit either file with a move, and never push without the PI's authorization. Never write
  secrets, participant data or content from unrelated repositories in them.
- Writing them authorizes nothing: no move, no installation and no governing file.

## Existing repository review

When the project already exists (an install, or an import of the PI's own code), setup is about the
**requested change**, not a re-creation of the project. In the Project phase, before asking about
the change in detail:

1. **Review what exists:**
   - the architecture: languages, components, data formats, entry points;
   - the tests, and the baseline run;
   - the governance: prior instructions, any `DECISIONS.md`, documented design choices;
   - the users and outputs that depend on current behaviour.

   Summarize this for the PI in plain words.
2. **Identify reusable parts:** what the change can build on unchanged, and what it must modify.
3. **Never overwrite a valid existing decision.**
   - A documented choice, an established output format, or a calculation the PI wants kept is
     recorded as a **retained** capability. It goes in report §3, with a regression acceptance
     criterion, such as "the existing outputs are reproduced exactly on the existing test data".
   - Changing one is a decision for the PI, raised explicitly.
4. **Investigate the requested change.** Use the coverage domains (`interview-guide.md`), but only
   for what the change touches. Do not re-elicit the whole product. The scope sequence
   (`SKILL.md`) applies to the change.
5. **Compatibility and migration:**
   - existing data files and output formats;
   - callers, scripts and users that depend on current behaviour;
   - the existing tests;
   - dependencies and their versions;
   - prior instructions;
   - whether old outputs must still be producible.

   Each concern becomes a requirement, a decision, or an open item with a gate.
6. **A development-oriented modification plan** in the report:
   - §5 describes the existing architecture and what changes;
   - §6 records the decisions about the change;
   - §9 is the modification roadmap: what is changed first, what stays protected by regression
     tests, and the migration steps.

   It sets direction only; `/arpd-plan` plans the sprints.

## Numbering: never hard-code IDs

Continue every ledger from where it stands: the next free DEC, R and SA numbers in the existing
`DECISIONS.md`. In a new, empty ledger that means DEC-01, R-01 and SA-01.

- **An unfilled placeholder** (for example, an inherited "R-01 (pending)" adoption ruling that was
  never given) is filled by the importing PI's actual ruling, in the PI's words, with the line
  "**Given:** by the importing PI on <date>".
- **Anything already given is never reused.** An ID that holds a real ruling, authorization or
  decision keeps it; the new entry takes the next free number.
- **One PI utterance, one R-NN.** If an inherited placeholder bundles several purposes (for example
  R-01 "adopt the charter and rule on the decision pack"), fill it with the adoption utterance only.
  Any separate utterance, such as a deferral of the pack's items, gets the next free R-NN.

---

## Steps for a non-ARPD project (import or install)

**Nothing governing is written before adoption.** Steps 1–4 only read the project. The only files
written are the notes and the draft report (above). Steps 6–9 write, in this order, after the PI
has adopted the report.

**Before adoption (read only)**

1. **Inventory.**
   - From a git URL, `git clone` it into a temporary directory **outside** this repository and read
     it there. From a local path, read it where it is.
   - List the top-level structure, languages and test commands.
   - Run the existing tests and keep each command, its working directory, exit code and output
     **verbatim**, with the source's commit. Until generation, keep them in the OS temp directory or
     the session scratchpad, not in the project and not in the discovery notes (the notes say only
     that the baseline was run, and where it is kept). At generation they are written once to
     `reports/IMPORT-BASELINE-YYYY-MM-DD.md`, from `kit/templates/reports/IMPORT-BASELINE.md`
     (`generation-checklist.md`, row 11). The import decision cites that report; when the first
     sprint starts, its Part 1 cites it too. Never report the baseline as better than it is.
   - Find existing instruction files: `CLAUDE.md`, `AGENTS.md`, `.cursorrules`,
     `.github/copilot-instructions.md`, and any README sections giving rules to contributors.
2. **Read the science out of the code.** Draft PARADIGM-SPEC items from what the code does: rules,
   parameters, outputs. Mark each one *"inferred from code: confirm"*.
3. **Map the existing tests** to draft requirements.
   - Passing tests are *Verified* evidence only where a test genuinely checks the requirement.
   - Tests that cannot fail, or that assert current rather than correct behaviour, are defects.
   - Known-answer tests are tagged as protected: never deleted or weakened.
4. **Reconcile the prior instructions** (the project's own, never the kit's files or an ARPD
   starter's charter). Classify each prior rule against the charter as *same* (drop it; the charter
   covers it), *compatible addition* (propose it as a Part B project rule) or *conflict*.

**The interview and the report**

5. **Interview** (the five phases, with the *Existing repository review* above).
   - Where the inferred behaviour carries scientific meaning, the PI confirms or corrects each
     inferred spec item.
   - Where the code and the PI's intent differ, that is a finding. Record it as a defect or an
     assumption, and never quietly align either one to the other.
   - Every reconciliation conflict and proposed addition goes in the report (§11 and §12), in plain
     language, for the PI to rule on. Nothing from the prior instructions is silently adopted or
     discarded.
   - The report's adoption is the ruling (R-NN).

**After adoption (writes, in this order)**

6. **Move the kit's own files** to `docs/arpd-kit/` in a move-only commit (above; fresh and import
   modes only).
7. **Bring the code in** (import mode only).
   - From a git repo: bring its history in as a subdirectory, or at the root if the kit has no
     conflicting files. Ask the PI which during the interview.
   - From plain files: copy them and commit with the message "Import <source> as baseline (no
     changes)".
8. **Move the prior instruction files** to `docs/prior-instructions/<original-name>`, unchanged, in a
   move-only commit. The new `CLAUDE.md`, built from `kit/constitution/CORE.md`, is the charter.
9. **Generate** the remaining documents per `generation-checklist.md`, never overwriting existing
   content. When a prior file of the same name exists, write the new one beside it with a `.arpd`
   suffix and ask. (This `.arpd` rule is only for a non-ARPD project's own files.) Record the source
   and commit, the moves, and each reconciliation ruling as DECs (next free numbers).

---

## Steps for an ARPD starter

Worked case: importing `examples/march-1991/` into this kit repository.

1. **Inventory before touching anything.** Read the starter's `START-HERE.md`, `STATUS.md`,
   `DECISIONS.md` (*Waiting on the PI*) and `PARADIGM-SPEC.md`. Run its checks where it stands (for
   the March starter: `cd examples/march-1991 && python -m pytest -m "not slow" -q` and
   `python tools/check_governance.py`), and keep the commands and output verbatim, outside the
   project, for the import baseline report.
2. **Interview (the five phases), confirming rather than re-asking.** The science is already
   written down: read it to the PI in plain language and ask them to confirm or change it. The
   report records it with its existing IDs.
   - **Draft wording.** Any item marked *"(draft wording, awaiting the PI's words)"*, such as the
     research question, either gets the importing PI's own words in the interview, or stays
     explicitly pending and is listed in *Waiting on the PI*. Adopting the charter and specification
     "as they stand" does not clear a draft marker. When the PI's own words replace the draft, keep
     the draft under a "Superseded draft wording" note beside them; never delete it.
   - **Inherited pending decisions:** list them for the PI in plain language. They may be decided
     now, delegated (as a standing authorization), deferred by ruling, or left pending. They block
     only work that depends on them.
3. **Move-only commits** (above), at the start of generation. Run these in Git Bash (or any POSIX
   shell); `set -e` and `|| exit 1` stop at the first failure, so a half-done move is never
   committed. Type the commands, or, if you save them as a script, save it **outside** the
   repository (the OS temp directory or the session scratchpad), never in the project.

   First list the collisions: every path the starter uses that already exists at the root. Each
   one must move in commit 1.

   ```
   S=examples/march-1991
   git ls-files "$S" | sed "s#^$S/##" | while read -r t; do [ -e "$t" ] && echo "$t"; done
   ```

   For the March starter this lists `.gitignore`, `AGENTS.md`, `CLAUDE.md` and `README.md`.

   ```
   set -e
   S=examples/march-1991
   # Commit 1: the kit's own files, and every other colliding kit file
   mkdir -p docs/arpd-kit
   for f in README.md QUICKSTART.md CLAUDE.md AGENTS.md LICENSE CITATION.cff RELEASE-NOTES.md; do git mv "$f" docs/arpd-kit/; done
   git mv .gitignore docs/arpd-kit/kit.gitignore
   git commit -m "Move kit pre-setup files to docs/arpd-kit (no changes)"
   # Commit 2: the starter's old START-HERE.md, separately, then everything except .claude/
   git mv "$S/START-HERE.md" docs/arpd-kit/START-HERE-starter.md
   git ls-files "$S" | grep -v "^$S/\.claude/" | while read -r f; do
     t="${f#$S/}"; mkdir -p "$(dirname "$t")"; git mv "$f" "$t" || exit 1
   done
   git commit -m "Move $S to the project root (no changes)"
   ```

   Then, **as a separate command**, the `.claude/` files. Claude Code asks the PI to approve any
   change into or out of `.claude/`, including a `git mv`, so this step runs last and on its own: a
   blocked approval cannot stop the other moves.

   ```
   set -e
   S=examples/march-1991
   # Commit 3: the starter's .claude/ (hooks settings, agent roles); needs the PI's approval
   git ls-files "$S/.claude" | while read -r f; do
     t="${f#$S/}"; mkdir -p "$(dirname "$t")"; git mv "$f" "$t" || exit 1
   done
   git commit -m "Move $S/.claude to the project root (no changes)"
   ```

   If the PI declines, or the run cannot ask (a scripted or non-interactive run), leave those files
   where they are and continue. Record them as owed: a DEC "event logging not installed" and/or
   "agent files not installed", `STATUS.md` §6, and *Known gaps* in `START-HERE.md`, which gives the
   PI the exact commands to run later, for example:

   ```
   git mv examples/march-1991/.claude/settings.json .claude/settings.json
   git mv examples/march-1991/.claude/agents/implementer.md .claude/agents/implementer.md
   git mv examples/march-1991/.claude/agents/reviewer.md .claude/agents/reviewer.md
   git commit -m "Move the starter's .claude files to the project root (no changes)"
   ```

   - **Collisions:** commit 1 moves every colliding kit file, so commit 2 never overwrites. Folders
     that exist on both sides (for example `docs/`) are merged file by file by the loop.
   - **`.gitignore`:** the kit's copy goes to `docs/arpd-kit/kit.gitignore` in commit 1; the
     starter's `.gitignore` arrives at the root in commit 2; the kit's lines are then merged into it
     in the first edit commit (step 4).
   - **The starter's old `START-HERE.md`** goes straight to `docs/arpd-kit/START-HERE-starter.md`,
     by its own `git mv`, before the loop. A new one is written for the PI at generation
     (`generation-checklist.md`, row 18).
   - Untracked or ignored files in the starter (`output/`, caches) are not moved; regenerate them.
   - Re-run the checks at the root and keep the output beside the first run. Both runs go in the
     import baseline report.
4. **Then edit, in place.** The starter's governing documents are updated through recorded rulings
   and standing authorizations, never replaced and never written beside as `.arpd`. Git keeps the
   history, and superseded entries keep their text.
   - `CLAUDE.md` (the starter's charter): update the Version line (adopted by the importing PI's
     R-NN), the *Authority profile* line (the profile, recorded as SA-NN), the PI line, and §6's
     project examples. Nothing else changes without a ruling.
   - `DECISIONS.md`: fill the inherited adoption placeholder or use the next free R; add the new
     SA; record the import and the moves as the next free DEC, citing
     `reports/IMPORT-BASELINE-YYYY-MM-DD.md`.
   - **Inherited decisions the starter already adopted** (by its own ruling, for example the March
     starter's R-01 adopting DEC-01 to DEC-07 as its working baseline) stay adopted. The importing
     PI's adoption of the starter carries them, so the report lists each one by ID and title, as
     adopted by the starter's ruling. Do not mark them pending or deferred. If the PI's words would
     reverse one (for example, "leave them pending"), say that they are already adopted and what
     reversing them would block, and ask once before recording anything. If the PI wants
     to revisit one, that is a reopening (a new DEC quoting the original rationale, charter §5), on
     the consult route.
   - **Inherited pending decisions the PI ruled on:** update each affected DEC entry's Status,
     Authorized and Adopted lines to match the ruling. Dates are ISO 8601 (`YYYY-MM-DD`, with a
     time such as `2026-10-20T14:05Z` when both happen on the same day).
     - **ratified, never adopted before:** a choice implemented as a code default but recorded as
       "not adopted" is a normal consult-route
       adoption: "**Authorized:** <date>, R-NN" and "**Adopted:** <date>, <version>", with
       authorization no later than adoption, and Status "adopted". Its earlier implementation
       before the charter is already covered by the recorded incident (I-01); do not write
       "ratified after adoption";
     - **ratified, genuinely adopted before authority existed:** "**Authorized:** <date>, R-NN,
       ratified after adoption (incident I-NN)", with Adopted giving the original adoption;
     - **deferred:** Status "deferred by R-NN (still to decide; dependent work stays blocked)",
       Adopted "not yet"; it stays in *Waiting on the PI* as "deferred (R-NN)";
     - changed: a new DEC that supersedes the old one, which keeps its text and is marked
       "Superseded by DEC-NN".

     Log each one: `python tools/log_event.py authorized --actor lead --ref DEC-NN --note "R-NN"`,
     and, for an adoption, `python tools/log_event.py adopted --actor lead --ref DEC-NN --note "<version>"`.
   - `STATUS.md`: rewrite it in the current template's format (base commit, the recovery block, a
     UTC time), for the new PI. The inherited content that still applies is carried over.
   - `.gitignore`: merge the kit's lines (from `docs/arpd-kit/kit.gitignore`) into the root file,
     keeping every line of both.
   - `tools/`: if the starter's tools differ from `kit/tools/`, replace them with the kit's and say
     so in the import DEC.
5. **Records are kept as they are:** rulings, decisions, sprint records, reviews and decision packs.
6. **Import baseline:** write `reports/IMPORT-BASELINE-YYYY-MM-DD.md` from
   `kit/templates/reports/IMPORT-BASELINE.md`, once: the provenance, and the checks run in steps 1
   and 3, verbatim (each command, its working directory and exit code, the test and checker
   output). This is the only place the baseline is recorded. DEC entries cite it, but never claim to
   contain it. Setup writes no sprint record: when `/arpd-plan` starts the first sprint, its Part 1
   cites this report. The new PI's extension gets new spec items, and its own checks in later
   sprints. **Inherited checks must keep passing with the extension disabled.**
7. **Post-generation check** (`generation-checklist.md`, *Then*): search the starter's governing
   documents for phrases that the adoption made stale, such as "pending R-01", "Pending adoption",
   "until R-01 is recorded" or "the importing PI", and update each one.

---

## Resuming an interrupted setup

A setup can stop part-way: a lost session, an API error, a turn limit. The record decides what is
authorized. Before anything else, check the project root (in install mode, the target repository):

- `git log --oneline -15` and `git status --short`;
- `docs/discovery/SETUP.md` and `reports/PROJECT-DEFINITION.md`, tracked or untracked. In install
  mode without consent they are outside the repository: ask the PI for their path;
- move-only commits already made (kit files to `docs/arpd-kit/`, prior instructions to
  `docs/prior-instructions/`, a starter to the root);
- the commit "Record adoption ruling R-NN (setup in progress)", and which checklist files exist.

Then:

1. **Tell the PI** what you found, in plain words.
2. **Old-format notes** (written by an earlier kit version) are read deterministically:
   - **"Interview mode" line or section:** obsolete, whatever its value. Leave it in place, mark it
     "(obsolete; ignored)", and never ask the PI to choose a mode or offer one.
   - **Old phase labels** map as follows: Intake → Project; Research & Problem → Project, with the
     theory-context choice still to confirm if relevant; Product & Engineering → Requirements and
     Architecture; Governance & Handoff → Team & Governance, then Definition Report. Topics keep
     their status under the new phase.
   - **An old "PI profile" table:** keep it as context, and do not re-ask its answers. An old
     adviser-role answer is not a theory-context choice. Ask the theory question only if theory is
     relevant, and show the old answer beside it.
   - **An old read-back draft** (never adopted) is not a report. Write
     `reports/PROJECT-DEFINITION.md` v1 from the notes.
3. **If no adoption ruling is recorded,** nothing generated is authorized.
   - Read the notes. Show the PI briefly what was gathered: the phase reached, the topics covered,
     and the open questions. Continue from the next open topic, without re-asking anything settled.
   - Nothing in the notes or the draft report is adopted. The PI's earlier words are discovery, and
     the lead's proposals stay proposals. A choice the PI made during the interview stays a recorded
     preference. Never re-adopt anything on resume.
   - **If a draft report exists,** re-present that version as it is; do not regenerate it. If the
     notes show answers given after that version, write vN+1 and say what changed.
   - Without notes, re-run the interview from where the record leaves off. Earlier answers count
     only if the PI confirms them now.
   - Keep the committed moves, and do not repeat them.
   - Show the PI any uncommitted generated files, and ask before discarding them.
4. **If the adoption ruling is recorded,** it and the report version it cites are the authority.
   - A ruling from an earlier kit version that adopted a read-back keeps that read-back as its
     authority. Do not write a report after the fact as if it had been adopted.
   - Continue the checklist from the first missing or incomplete row. If the notes are in the
     project but uncommitted, commit them alone.
   - Never repeat a move, renumber an ID or rewrite a completed file.
   - Check each existing file against its checklist row, and against the adopted report or
     read-back (for example, the purpose wording, or an unfilled `{{…}}`).
   - Ask the PI only for what the record does not settle.
   - If the ruling cites no report and contains no read-back text, say so. An uncommitted file cannot
     then be checked against what the PI adopted, so show it to the PI and ask them to confirm it
     before you keep it.
5. Record the recovery in `STATUS.md`, in a `Recovered:` line naming what was found and what was
   redone. If `tools/log_event.py` exists, log
   `python tools/log_event.py resume --actor lead --note "setup resumed"`.
6. Finish as usual: the final checker run, the stray-file check, the setup commit and the closeout.
