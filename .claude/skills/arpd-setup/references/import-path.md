# Import and install paths

Use these when the project starts from existing code: the PI's own, a published model's code, or a
starter project. **Preserve existing work. Never silently merge or overwrite instructions.**

## Modes

| Mode | Invocation | What happens |
|---|---|---|
| **Import into this repository** | `/arpd-setup import <path-or-git-url>` | The existing codebase is brought into this kit repository, keeping its history when it is a git repo. This repository becomes the project. |
| **Install into an existing repository** | `/arpd-setup install <path>` | The charter, governing documents, tools, hooks and agents are installed **into** the existing repository at `<path>`. The kit's `kit/` folder and the `arpd-*` skills are copied there, so later amendments work. The kit repository is left unchanged. |

- **Import** suits code that is small or not under the PI's control, such as a published model or a
  starter. A starter that already lives inside this kit (for example `examples/march-1991/`) is an
  import.
- **Install** suits the PI's own ongoing repository.
- **Ask the PI which mode, if it is unclear.**

Then decide which kind of project is coming in, because the steps differ:

- **Non-ARPD project:** it has no `PARADIGM-SPEC.md` and governing documents. Follow *Steps for a
  non-ARPD project*.
- **ARPD project (a starter):** it already has `CLAUDE.md`, `PARADIGM-SPEC.md`, `DECISIONS.md` and
  the other governing documents. Follow *Steps for an ARPD starter*. Its `CLAUDE.md` and `AGENTS.md`
  **are its charter**: they are kept and updated in place, never treated as prior instructions.

## The kit's own files are not prior instructions

In fresh and import modes, this repository's root holds the kit's own pre-setup files: `README.md`,
`QUICKSTART.md`, `CLAUDE.md` and `AGENTS.md`. They describe the kit, not the project.

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

## Numbering: never hard-code IDs

Continue every ledger from where it stands: the next free DEC, R and SA numbers in the existing
`DECISIONS.md`. In a new, empty ledger that means DEC-01, R-01 and SA-01.

- **An unfilled placeholder** (for example, an inherited "R-01 (pending)" adoption ruling that was
  never given) is filled by the importing PI's actual ruling, in the PI's words, with the line
  "**Given:** by the importing PI on <date>".
- **Anything already given is never reused.** An ID that holds a real ruling, authorization or
  decision keeps it; the new entry takes the next free number.

---

## Steps for a non-ARPD project (import or install)

1. **Inventory before touching anything.**
   - List the top-level structure, languages and test commands.
   - Run the existing tests and keep the output **verbatim**. It is recorded once, as the baseline,
     in sprint S01's record (Part 1), and the import decision points to it. Never report it as better
     than it is.
   - Find existing instruction files: `CLAUDE.md`, `AGENTS.md`, `.cursorrules`,
     `.github/copilot-instructions.md`, and any README sections giving rules to contributors.
2. **Bring the code in (import mode only).**
   - From a git URL or a local git repo: `git clone` it into a temporary directory, then bring its
     history in as a subdirectory, or at the root if the kit has no conflicting files. Ask the PI
     which.
   - From plain files: copy them and commit with the message "Import <source> as baseline (no
     changes)".
   - Record the source and commit as the next free DEC.
3. **Preserve prior instructions.** This step applies only to a non-ARPD project's own instruction
   files, never to the kit's files or to an ARPD starter's charter.
   - Move each existing instruction file to `docs/prior-instructions/<original-name>`, unchanged, in
     a move-only commit.
   - Record the move as the next free DEC.
   - The new `CLAUDE.md`, built from `kit/constitution/CORE.md`, is the charter.
4. **Reconcile** (non-ARPD only).
   - Compare each prior rule with the charter. Classify it as:
     - *same* (drop it; the charter covers it);
     - *compatible addition* (propose it as a Part B project rule);
     - *conflict*.
   - Put every conflict and every proposed addition in a **decision pack** in the read-back, in
     plain language.
   - The PI rules. Nothing from the prior instructions is silently adopted or discarded.
5. **Read the science out of the code, then confirm it with the PI.**
   - Draft PARADIGM-SPEC items from what the code does: rules, parameters, outputs. Mark each one
     *"inferred from code: confirm"*.
   - In Phase 2, the PI confirms or corrects each. Where the code and the PI's intent differ, that
     is a finding: record it as a defect or an assumption. Never quietly align either one to the
     other.
6. **Existing tests become evidence.**
   - Map passing tests to requirements as *Verified* evidence, but only where a test genuinely
     checks the requirement.
   - Tests that cannot fail, or that assert current rather than correct behaviour, are recorded as
     defects.
   - Known-answer tests are tagged as protected: never deleted or weakened.
7. **Generate** the remaining documents per `generation-checklist.md`, never overwriting existing
   content. When a prior file of the same name exists, write the new one beside it with a `.arpd`
   suffix and ask. (This `.arpd` rule is only for a non-ARPD project's own files.)

---

## Steps for an ARPD starter

Worked case: importing `examples/march-1991/` into this kit repository.

1. **Inventory before touching anything.** Read the starter's `START-HERE.md`, `STATUS.md`,
   `DECISIONS.md` (*Waiting on the PI*) and `PARADIGM-SPEC.md`. Run its checks where it stands (for
   the March starter: `cd examples/march-1991 && python -m pytest -m "not slow" -q` and
   `python tools/check_governance.py`), and keep the output verbatim.
2. **Interview (Phases 1–8), confirming rather than re-asking.** The science is already written
   down: read it to the PI in plain language and ask them to confirm or change it.
   - **Draft wording.** Any item marked *"(draft wording, awaiting the PI's words)"*, such as the
     research question, either gets the importing PI's own words in the interview, or stays
     explicitly pending and is listed in *Waiting on the PI*. Adopting the charter and specification
     "as they stand" does not clear a draft marker.
   - **Inherited pending decisions:** list them for the PI in plain language. They may be decided
     now, delegated (as a standing authorization), deferred by ruling, or left pending. They block
     only work that depends on them.
3. **Move-only commits** (above): first the kit's files to `docs/arpd-kit/`; then the starter's
   tracked files to the root. A loop that keeps dotfiles and nested folders:

   ```
   git ls-files examples/march-1991 | while read -r f; do
     t="${f#examples/march-1991/}"; mkdir -p "$(dirname "$t")"; git mv "$f" "$t"; done
   ```

   - **Collisions:** any kit file at a path the starter also uses (for example `.gitignore`) moves
     to `docs/arpd-kit/` in commit 1, so commit 2 never overwrites. Folders that exist on both sides
     (for example `docs/`, `.claude/`) are merged file by file.
   - **The starter's old `START-HERE.md`** moves straight to `docs/arpd-kit/START-HERE-starter.md`
     in commit 2. A new one is written for the PI in Phase 10.
   - Untracked or ignored files in the starter (`output/`, caches) are not moved; regenerate them.
   - The starter's `.claude/settings.json` and `.claude/agents/` arrive by this move. Claude Code may
     still ask the PI to approve changes under `.claude/`; if it is declined or blocked, follow
     *Permission prompts* in `generation-checklist.md`.
   - Re-run the checks at the root and keep the output beside the first run.
4. **Then edit, in place.** The starter's governing documents are updated through recorded rulings
   and standing authorizations, never replaced and never written beside as `.arpd`. Git keeps the
   history, and superseded entries keep their text.
   - `CLAUDE.md` (the starter's charter): update the Version line (adopted by the importing PI's
     R-NN), the *Authority profile* line (the profile, recorded as SA-NN), the PI line, and §6's
     project examples. Nothing else changes without a ruling.
   - `DECISIONS.md`: fill the inherited adoption placeholder or use the next free R; add the new
     SA; record the import and the moves as the next free DEC, pointing to S01's baseline.
   - `STATUS.md`: rewrite it in the current template's format (base commit, the recovery block, a
     UTC time), for the new PI. The inherited content that still applies is carried over.
   - `.gitignore`: merge the kit's lines (now in `docs/arpd-kit/`) into the root file, keeping every
     line of both.
   - `tools/`: if the starter's tools differ from `kit/tools/`, replace them with the kit's and say
     so in the import DEC.
5. **Records are kept as they are:** rulings, decisions, sprint records, reviews and decision packs.
6. **First sprint (S01):** its Part 1 records the inherited baseline once: the checks run in steps 1
   and 3, verbatim. The new PI's extension gets new spec items, and its own checks in the
   extension-evidence slot. **Inherited checks must keep passing with the extension disabled.**
7. **Post-generation check** (`generation-checklist.md`, *Then*): search the starter's governing
   documents for phrases that the adoption made stale, such as "pending R-01", "Pending adoption",
   "until R-01 is recorded" or "the importing PI", and update each one.
