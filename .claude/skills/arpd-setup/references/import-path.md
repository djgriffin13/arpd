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

Do the moves at the start of Phase 9, after the PI has adopted the read-back. Check each move commit
with `git show --stat --find-renames HEAD`: every line should be a rename with no content change.
The discovery notes are untracked at this point: stage only the moves, so the notes never enter a
move commit. They get their own commit after the adoption ruling (`generation-checklist.md`,
*Commit order*).

## Discovery notes in import and install modes

The interview's working notes (`docs/discovery/SETUP.md`, from `kit/templates/discovery/SETUP.md`)
are the one file written before the read-back. They are non-governing (`SKILL.md`, *Discovery
notes*).

- **Import:** the project root is this repository. Write the notes here, and tell the PI once.
- **Install:** the target is the PI's own repository, which may be shared or public. In Intake,
  before the first write, ask once for consent to save the notes there, and name the path
  (`docs/discovery/SETUP.md` in the target). Record the answer in the notes' *Mode and consent*.
  - With consent: write them there, uncommitted until adoption, then commit them alone.
  - Without consent: keep them in the OS temp directory, tell the PI the path, and say that a later
    session can resume from them only if the PI gives that path. They are never added to the
    repository unless the PI later asks.
- Never commit the notes with a move, never push them without the PI's authorization, and never
  write secrets, participant data or content from unrelated repositories in them.
- Writing notes authorizes nothing: no move, no installation and no governing file.

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

**Nothing governing is written before the read-back** (`SKILL.md`, ground rule 8). Steps 1–4 only
read the project; the only file written is the discovery notes (above). Steps 6–9 write, in this
order, after the PI has adopted the read-back.

**Before the read-back (read only)**

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

**The interview and the read-back**

5. **Interview (the four phases; internal Phases 1–8).** In Research & Problem, the PI confirms or corrects each inferred spec item. Where
   the code and the PI's intent differ, that is a finding: record it as a defect or an assumption,
   and never quietly align either one to the other. Every reconciliation conflict and proposed
   addition goes in the read-back, in plain language, for the PI to rule on. Nothing from the prior
   instructions is silently adopted or discarded. The read-back ends with the adoption ruling (R-NN).

**After the read-back (writes, in this order)**

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
2. **Interview (the four phases; internal Phases 1–8), confirming rather than re-asking.** The science is already written
   down: read it to the PI in plain language and ask them to confirm or change it.
   - **Draft wording.** Any item marked *"(draft wording, awaiting the PI's words)"*, such as the
     research question, either gets the importing PI's own words in the interview, or stays
     explicitly pending and is listed in *Waiting on the PI*. Adopting the charter and specification
     "as they stand" does not clear a draft marker. When the PI's own words replace the draft, keep
     the draft under a "Superseded draft wording" note beside them; never delete it.
   - **Inherited pending decisions:** list them for the PI in plain language. They may be decided
     now, delegated (as a standing authorization), deferred by ruling, or left pending. They block
     only work that depends on them.
3. **Move-only commits** (above), at the start of Phase 9. Run these in Git Bash (or any POSIX
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
   - **Inherited pending decisions the PI ruled on:** update each affected DEC entry's Status,
     Authorized and Adopted lines to match the ruling. Dates are ISO 8601 (`YYYY-MM-DD`, with a
     time such as `2026-10-20T14:05Z` when both happen on the same day).
     - **ratified, never adopted before:** a choice implemented as a code default but recorded as
       "not adopted" (as with the March starter's DEC-01 to DEC-07) is a normal consult-route
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
authorized. At Phase 0, check the project root (in install mode, the target repository):

- `git log --oneline -15` and `git status --short`;
- `docs/discovery/SETUP.md`, tracked or untracked (in install mode without consent, the notes are
  outside the repository: ask the PI for their path);
- move-only commits already made (kit files to `docs/arpd-kit/`, prior instructions to
  `docs/prior-instructions/`, a starter to the root);
- the commit "Record adoption ruling R-NN (setup in progress)", and which checklist files exist.

Then:

1. **Tell the PI** what you found, in plain words.
2. **If no adoption ruling is recorded,** nothing generated is authorized.
   - If discovery notes exist, read them. Show the PI briefly what was gathered: the phase reached,
     the topics covered, the PI's words, and the open questions. Restore the coverage map and the
     interview mode, and continue from the next open topic.
   - Nothing in the notes is adopted. The PI's earlier words are discovery; the lead's proposals
     stay proposals. Never treat an earlier proposal as agreed, and never re-adopt it on resume.
   - Without notes, re-run the interview from where the record leaves off. Earlier answers count
     only if the PI confirms them now.
   - Keep the committed moves and do not repeat them.
   - Re-do the read-back. It must be adopted now, in the PI's words.
   - Show the PI any uncommitted generated files, and ask before discarding them.
3. **If the adoption ruling is recorded,** it and its read-back are the authority. Continue the
   checklist from the first missing or incomplete row. If the discovery notes are in the project but
   uncommitted, commit them alone. Never repeat a move, never renumber an ID, and never rewrite a
   completed file. Check each existing file, committed or not, against its checklist row and against
   the recorded read-back (for example, the question and construct wording, or an unfilled `{{…}}`).
   Ask the PI only for what the record does not settle. **If the ruling does not contain the
   read-back text**, say so: an uncommitted file cannot then be checked against what the PI adopted,
   so show it to the PI and ask them to confirm it before you keep it.
4. Record the recovery in `STATUS.md` (a `Recovered:` line naming what was found and what was
   redone). If `tools/log_event.py` exists, log
   `python tools/log_event.py resume --actor lead --note "setup resumed"`.
5. Finish as usual: the final checker run, the stray-file check, the setup commit and the closeout.
