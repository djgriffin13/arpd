# Import and install paths

Use these when the project starts from existing code: the PI's own, a published model's code, or a
starter project. **Preserve existing work. Never silently merge or overwrite instructions.**

## Modes

| Mode | Invocation | What happens |
|---|---|---|
| **Import into this repository** | `/arpd-setup import <path-or-git-url>` | The existing codebase is brought into this kit repository, keeping its history when it is a git repo. This repository becomes the project. |
| **Install into an existing repository** | `/arpd-setup install <path>` | The charter, governing documents, tools, hooks and agents are installed **into** the repository at `<path>`. `kit/` is copied there whole, and the four `arpd-*` skills, with their `references/`, go to its `.claude/skills/` (a `.claude/` write, last, with the PI's approval; `generation-checklist.md`, row 15). The kit repository is left unchanged. |

- **Fresh** is the mode when the repository holds only the kit: `kit/`, `.claude/skills/arpd-*`,
  `docs/`, `evaluation/`, `examples/`, the kit's own root files (*The kit's own files*, below) and
  dotfiles. Otherwise, or when the PI passed `import` or `install`, use this file.
- **Import** suits code that is small or not under the PI's control, such as a published model or a
  starter. A starter that already lives inside this kit (for example `examples/march-1991/`) is an
  import.
- **Install** suits the PI's own ongoing repository.
  - The copied `kit/` folder holds the kit's own tests. After the copy, run the project's tests with
    *The project's test command* (`generation-checklist.md`), and check the count matches the
    baseline.
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
describe the kit, not the project. The PI chooses the project's own licence.

- **Move them** to `docs/arpd-kit/` with `git mv`, in a commit of their own (see *Move-only commits*).
- **Never** treat them as project instructions: do not reconcile them, do not move them to
  `docs/prior-instructions/`, and do not write `.arpd` files beside them.
- In install mode they are not copied to the target repository, so the question does not arise.

## Move-only commits (keep the history)

A commit that moves a file **and** edits it can break git's rename match, and then `git log --follow`
and `git blame` lose everything before the move. So, at the start of generation, after adoption:
commit 1 moves the kit's own files to `docs/arpd-kit/` ("Move kit pre-setup files to docs/arpd-kit
(no changes)"); commit 2, for a starter inside the kit, moves the starter to the root ("Move
<starter> to the project root (no changes)"); only then is anything edited. Check each with
`git show --stat --find-renames HEAD`: every line a rename with no content change. Stage only the
moves; the untracked notes and draft report enter no move commit (`generation-checklist.md`,
*Commit order*).

## Working files

The notes and the draft report are the only files written before adoption, and both are
non-governing (`SKILL.md`, *Working files*).

- **Fresh and import:** the project root is this repository. Write both here, and tell the PI once.
- **Install:** the target is the PI's own repository, which may be shared or public. Before the
  first write, ask once (`CHOICE FOR YOU (select one)`) for consent to save both files there, naming
  the paths, and record the answer in the notes' *Mode and consent*.
  - **With consent:** write them there, uncommitted until adoption.
  - **Without consent:** keep both in the OS temp directory and give the PI the path; a later
    session can resume from them only if the PI gives that path. At adoption the adopted report is
    written into the target (adoption authorizes it); the notes are never added unless the PI asks.
- Writing them authorizes nothing: no move, no installation and no governing file.

## Existing repository review

When the project already exists (an install, or an import of the PI's own code), setup is about the
**requested change**, not a re-creation of the project. In the Project phase, before asking about
the change in detail:

1. **Review what exists,** and summarize it for the PI in plain words: the architecture (languages,
   components, data formats, entry points); the tests and the baseline run; the governance (prior
   instructions, any `DECISIONS.md`, documented design choices); the users and outputs that depend
   on current behaviour.
2. **Identify reusable parts:** what the change can build on unchanged, and what it must modify.
3. **Never overwrite a valid existing decision.** A documented choice, an established output
   format, or a calculation the PI wants kept is a **retained** capability in report §3, with a
   regression acceptance criterion ("the existing outputs are reproduced exactly on the existing
   test data"). Changing one is a decision for the PI, raised explicitly.
4. **Investigate the requested change** with the coverage domains, but only for what it touches;
   the scope sequence applies to the change. Do not re-elicit the whole product.
5. **Compatibility and migration:** existing data files and output formats; callers, scripts and
   users; the existing tests; dependencies and versions; prior instructions; whether old outputs
   must still be producible. Each becomes a requirement, a decision, or an open item with a gate.
6. **A modification plan** in the report: §5 the existing architecture and what changes; §6 the
   decisions; §9 the modification roadmap (what changes first, what regression tests protect, the
   migration steps). Direction only; `/arpd-plan` plans the sprints.

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

**Nothing governing is written before adoption.** Steps 1–4 only read (the notes and the draft
report are the only writes); steps 6–9 write, in this order, after adoption.

1. **Inventory.**
   - From a git URL, `git clone` it into a temporary directory **outside** this repository and read
     it there. From a local path, read it where it is.
   - List the top-level structure, languages and test commands.
   - Run the existing tests and keep each command, its working directory, exit code and output
     **verbatim**, with the source's commit, in the OS temp directory or the session scratchpad (the
     notes say only that the baseline was run, and where). At generation they are written once to
     the import baseline report (`generation-checklist.md`, row 11). Never report the baseline as
     better than it is.
   - Find existing instruction files: `CLAUDE.md`, `AGENTS.md`, `.cursorrules`,
     `.github/copilot-instructions.md`, and README sections giving rules to contributors.
2. **Read the science out of the code.** Draft PARADIGM-SPEC items from what the code does (rules,
   parameters, outputs), each marked *"inferred from code: confirm"*.
3. **Map the existing tests** to draft requirements. A passing test is *Verified* evidence only
   where it genuinely checks the requirement; a test that cannot fail, or asserts current rather
   than correct behaviour, is a defect; known-answer tests are protected, never deleted or weakened.
4. **Reconcile the prior instructions** (the project's own, never the kit's files or an ARPD
   starter's charter): each prior rule is *same* (dropped; the charter covers it), a *compatible
   addition* (proposed as a Part B project rule) or a *conflict*.
5. **Interview** (the five phases, with the *Existing repository review*). The PI confirms or
   corrects each inferred spec item that carries scientific meaning. Where the code and the PI's
   intent differ, record a defect or an assumption; never quietly align one to the other. Every
   reconciliation conflict and proposed addition goes in report §11–12 for the PI to rule on;
   nothing from the prior instructions is silently adopted or discarded.
6. **Move the kit's own files** to `docs/arpd-kit/` (move-only commit; fresh and import only).
7. **Bring the code in** (import only): from a git repo, its history as a subdirectory, or at the
   root if nothing conflicts (ask the PI which during the interview); from plain files, a copy
   committed as "Import <source> as baseline (no changes)".
8. **Move the prior instruction files** to `docs/prior-instructions/<original-name>`, unchanged, in a
   move-only commit. The new `CLAUDE.md`, from `kit/constitution/CORE.md`, is the charter.
9. **Generate** per `generation-checklist.md`, never overwriting existing content: when a prior file
   of the same name exists, write the new one beside it with a `.arpd` suffix and ask (only for a
   non-ARPD project's own files). Record the source and commit, the moves, and each reconciliation
   ruling as DECs (next free numbers).

---

## Steps for an ARPD starter

Worked case: importing `examples/march-1991/` into this kit repository (its exact commands:
`examples/march-1991/IMPORT.md`).

1. **Inventory before touching anything.** Read the starter's `START-HERE.md`, `STATUS.md`,
   `DECISIONS.md` (*Waiting on the PI*), `PARADIGM-SPEC.md` and any import notes. Run its tests and
   `python tools/check_governance.py` where it stands, and keep the commands and output verbatim,
   outside the project, for the import baseline report.
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
3. **Move-only commits** (above), at the start of generation, in a POSIX shell, stopping at the
   first failure so a half-done move is never committed. A script, if you save one, goes
   **outside** the repository. A starter may give its exact commands (the March starter:
   `examples/march-1991/IMPORT.md`, read before anything moves). In general:
   - **Commit 1:** list the collisions (every starter path that already exists at the root) and move
     each colliding kit file, with the kit's own files, to `docs/arpd-kit/` (the kit's
     `.gitignore` as `docs/arpd-kit/kit.gitignore`), so commit 2 never overwrites.
   - **Commit 2:** the starter's old `START-HERE.md` (and any import notes it carries) to
     `docs/arpd-kit/` by their own `git mv` (`START-HERE-starter.md`); then every tracked starter
     file except `.claude/` to the same path at the root, folders merged file by file. Untracked or
     ignored files (`output/`, caches) are not moved; regenerate them.
   - **Commit 3, as a separate command:** the starter's `.claude/` files. Claude Code asks the PI to
     approve any change into or out of `.claude/`, including a `git mv`, so this runs last and on
     its own; a blocked approval cannot stop the other moves. If the PI declines, or the run cannot
     ask, leave them in place and record them as owed (`generation-checklist.md`, *Permission
     prompts*), with the exact `git mv` commands in *Known gaps*.
   - The starter's `.gitignore` arrives in commit 2; the kit's lines are merged into it in the first
     edit commit (step 4). Re-run the checks at the root and keep the output beside the first run;
     both go in the import baseline report.

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
     PI's adoption of the starter carries them, so the report lists each one by ID and title, with
     status "Adopted (inherited, R-NN)". Do not mark them pending or deferred. If the PI's words would
     reverse one (for example, "leave them pending"), say that they are already adopted and what
     reversing them would block, and ask once before recording anything. If the PI wants
     to revisit one, that is a reopening (a new DEC quoting the original rationale, charter §5), on
     the consult route.
   - **Inherited pending decisions the PI ruled on:** update each affected DEC entry's Status,
     Authorized and Adopted lines to match the ruling, with ISO 8601 dates (the DECISIONS template's
     format):
     - **ratified, never adopted before** (a code default recorded as "not adopted"): a normal
       consult-route adoption, "**Authorized:** <date>, R-NN" and "**Adopted:** <date>, <version>",
       Status "adopted"; its earlier implementation is already covered by the recorded incident
       (I-01), so do not write "ratified after adoption";
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
6. **Import baseline** (`generation-checklist.md`, row 11), with the checks of steps 1 and 3. It is
   the only place the baseline is recorded; DECs and the first sprint's Part 1 cite it. The new PI's
   extension gets new spec items and its own checks in later sprints. **Inherited checks must keep
   passing with the extension disabled.**
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
2. **Old-format notes** (written by an earlier kit version) are converted to the current notes
   template at once, before the next question: the phase tracker rewritten under the new phases,
   old profile answers moved to *Governance preferences*, the PI's words kept verbatim. They are
   read deterministically:
   - **"Interview mode" line or section:** obsolete, whatever its value. Leave it in place, mark it
     "(obsolete; ignored)", and never ask the PI to choose a mode or offer one. The same holds for
     an interview mode recorded in an old `STATUS.md` §8 (`/arpd-plan` ignores it too).
   - **Old phase labels** map as follows: Intake → Project; Research & Problem → Project, with the
     theory-context choice still to confirm if relevant; Product & Engineering → Requirements and
     Architecture; Governance & Handoff → Team & Governance, then Definition Report. Topics keep
     their status under the new phase.
   - **Old scope sections** "First useful version", "Vision" and "Later, wishlist and exclusions"
     map to the *Scope* tiers: minimum usable version, ideal version, and nice-to-have or excluded.
     Ask only the scope questions they leave unanswered.
   - **An old "PI profile" table:** its answers (autonomy bounds, review depth, check-ins) are
     settled: never re-ask them; confirm them in the read-back. An old
     adviser-role answer is not a theory-context choice. Ask the theory question only if theory is
     relevant, and show the old answer beside it.
   - **An old read-back draft** (never adopted) is not a report. Write
     `reports/PROJECT-DEFINITION.md` v1 from the notes.
3. **If no adoption ruling is recorded,** nothing generated is authorized.
   - Show the PI briefly what the notes gathered (the phase reached, the topics covered, the open
     questions), and continue from the next open topic without re-asking anything settled.
   - Nothing in the notes or the draft report is adopted: earlier words are discovery, proposals
     stay proposals, interview choices stay preferences. Never re-adopt anything on resume.
   - **If a draft report exists,** re-present that version as it is; do not regenerate it. If the
     notes show answers given after that version, write vN+1 and say what changed.
   - Without notes, re-run the interview from where the record leaves off. Earlier answers count
     only if the PI confirms them now.
   - Keep the committed moves, and do not repeat them.
   - Show the PI any uncommitted generated files, and ask before discarding them.
4. **If the adoption ruling is recorded,** it and the report version it cites are the authority (a
   ruling from an earlier kit version that adopted a read-back keeps that read-back; never write a
   report after the fact as if it had been adopted).
   - Continue the checklist from the first missing or incomplete row; commit uncommitted notes
     alone. Never repeat a move, renumber an ID or rewrite a completed file.
   - Check each existing file against its row and the adopted text (the purpose wording, an
     unfilled `{{…}}`). Ask the PI only for what the record does not settle.
   - If the ruling cites no report and holds no read-back text, say so: show any uncommitted file
     to the PI and ask them to confirm it before you keep it.
5. Record the recovery: before adoption, in the notes (*Report version and state*, a `Resumed:`
   line naming what was found and what was redone), since `STATUS.md` does not exist yet; after
   adoption, in `STATUS.md`'s `Recovered:` line (`generation-checklist.md`, row 7). If
   `tools/log_event.py` exists, log
   `python tools/log_event.py resume --actor lead --note "setup resumed"`.
6. Finish as usual: the final checker run, the stray-file check, the setup commit and the closeout.
