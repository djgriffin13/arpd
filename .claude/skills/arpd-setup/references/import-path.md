# Import and install paths

Use these when the project starts from existing code: the PI's own, a published model's code, or a
starter project. **Preserve existing work. Never silently merge or overwrite instructions.**

## Modes

| Mode | Invocation | What happens |
|---|---|---|
| **Import into this repository** | `/arpd-setup import <path-or-git-url>` | The existing codebase is copied into this kit repository, keeping its history when it is a git repo. This repository becomes the project. |
| **Install into an existing repository** | `/arpd-setup install <path>` | The charter, governing documents, tools, hooks and agents are installed **into** the existing repository at `<path>`. The kit's `kit/` folder and the `arpd-*` skills are copied there, so later amendments work. The kit repository is left unchanged. |

**Ask the PI which mode, if it is unclear.**

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
   - Record the source and commit in `DECISIONS.md` as DEC-01.
3. **Preserve prior instructions.**
   - Move each existing instruction file to `docs/prior-instructions/<original-name>`, unchanged.
   - Record the move in DEC-02.
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
   overwrite existing content. When a file of that name exists, write the new one beside it with a
   `.arpd` suffix and ask.

## Starter projects (e.g. a checked model to be extended)

When the imported project is already an ARPD project (it has `PARADIGM-SPEC.md` and the governing
documents):

- **keep** its records: rulings, decisions, sprint records;
- **add** the new PI as the PI from now on, with a new ruling R-NN that adopts the inherited charter
  and specification, with any changes, and a new standing authorization (SA-NN) for the new PI's
  authority profile;
- **inherited pending decisions:** list them for the new PI in plain language. They may be decided
  now, delegated, or left pending. They block only work that depends on them;
- **first sprint:** run the inherited checks and confirm they pass. Record the result in sprint
  S01 as the inherited baseline;
- the new PI's extension gets new spec items, and its own checks in the extension-evidence slot;
- **inherited checks must keep passing with the extension disabled.**
