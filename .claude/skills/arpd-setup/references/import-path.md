# Import and install paths

Use these when the project starts from existing code: the PI's own, a published model's code, or a
starter project. **Preserve existing work. Never silently merge or overwrite instructions.**

## Modes

| Mode | Invocation | What happens |
|---|---|---|
| **Import into this repository** | `/arpd-setup import <path-or-git-url>` | The existing codebase is copied into this kit repository, keeping its history when it is a git repo. This repository becomes the project. |
| **Install into an existing repository** | `/arpd-setup install <path>` | The charter, governing documents, tools, hooks and agents are installed **into** the existing repository at `<path>`. The kit's `kit/` folder and the `arpd-*` skills are copied there, so later amendments work. The kit repository is left unchanged. |

**Ask the PI which mode, if it is unclear.** A starter that already lives inside this kit (for
example `examples/march-1991/`) is imported into this repository: see *Starter projects* below.

## The kit's own files are not prior instructions

In fresh and import modes, this repository's root holds the kit's own pre-setup files: `README.md`, `QUICKSTART.md`, `CLAUDE.md` and `AGENTS.md`.
They describe the kit, not the project.

- **Move them** to `docs/arpd-kit/` with `git mv`, before generating anything. Do this in every mode
  that uses this repository (fresh and import).
- **Never** treat them as existing project instructions: do not reconcile them, do not move them to
  `docs/prior-instructions/`, and do not write `.arpd` files beside them.
- In install mode they are not copied to the target repository, so the question does not arise.

- **Import** suits code that is small or not under the PI's control, such as a published model or a
  starter.
- **Install** suits the PI's own ongoing repository.

## Steps (both modes)

1. **Inventory before touching anything.**
   - List the top-level structure, languages and test commands.
   - Run the existing tests and record the result **verbatim**, as the baseline. Never report it as
     better than it is.
   - Find existing instruction files: `CLAUDE.md`, `AGENTS.md`, `.cursorrules`,
     `.github/copilot-instructions.md`, and any README sections giving rules to contributors.
2. **Copy the code (import mode only).**
   - From a git URL or a local git repo: `git clone` it into a temporary directory, then bring its
     history in as a subdirectory, or at the root if the kit has no conflicting files. Ask the PI
     which.
   - From plain files: copy them and commit with the message "Import <source> as baseline (no
     changes)".
   - Record the source and commit in `DECISIONS.md` as the next free DEC number (see *Numbering*).
3. **Preserve prior instructions** (the project's own, not the kit's files above).
   - Move each existing instruction file to `docs/prior-instructions/<original-name>`, unchanged.
   - Record the move as the next free DEC number.
   - The new `CLAUDE.md` is the charter.
4. **Reconcile.**
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
7. **Generate** the remaining documents per `generation-checklist.md`, skipping files that would
   overwrite existing content. When a prior, non-ARPD file of that name exists, write the new one
   beside it with a `.arpd` suffix and ask. This rule does not apply to the kit's own files (moved
   above), or to the governing documents of a project that is already an ARPD project (see
   *Starter projects*).

## Numbering: never hard-code IDs

Continue every ledger from where it stands: the next free DEC, R and SA numbers in the existing
`DECISIONS.md`. In a new, empty ledger that means DEC-01, R-01 and SA-01.

- **An unfilled placeholder** (for example, an inherited "R-01 (pending)" adoption ruling that was
  never given) is filled by the importing PI's actual ruling, in the PI's words, with the line
  "**Given:** by the importing PI on <date>".
- **Anything already given is never reused.** An ID that holds a real ruling, authorization or
  decision keeps it; the new entry takes the next free number.

## Starter projects (e.g. a checked model to be extended)

When the imported project is already an ARPD project (it has `PARADIGM-SPEC.md` and the governing
documents):

- **a starter inside this kit** (for example `examples/march-1991/`): first move the kit's own files
  to `docs/arpd-kit/` (above), then `git mv` the starter's contents to the project root, so that
  their history is kept. Where a folder exists on both sides (for example `docs/`), merge it; if two
  files share a path, the kit's file moves to `docs/arpd-kit/`. Merge the two `.gitignore` files
  (keep every line of both). Record the move as the next free DEC;
- **its governing documents are updated in place,** through recorded rulings and standing
  authorizations. Git keeps the history, and superseded entries keep their text. The `.arpd`
  rule does not apply to them;
- **its `START-HERE.md` is regenerated** for the new PI. Move the old one to
  `docs/arpd-kit/START-HERE-starter.md` with `git mv`;

- **keep** its records: rulings, decisions, sprint records;
- **add** the new PI as the PI from now on, with a ruling that adopts the inherited charter and
  specification, with any changes, and a standing authorization for the new PI's authority profile.
  Number them as *Numbering* says: an inherited placeholder such as "R-01 (pending)" is filled;
  otherwise use the next free R and SA numbers;
- **inherited pending decisions:** list them for the new PI in plain language. They may be decided
  now, delegated, or left pending. They block only work that depends on them;
- **first sprint:** run the inherited checks and confirm they pass. Record the result in sprint
  S01 as the inherited baseline;
- the new PI's extension gets new spec items, and its own checks in the extension-evidence slot;
- **inherited checks must keep passing with the extension disabled.**
