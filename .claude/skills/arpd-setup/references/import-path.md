# Modes, existing code and resuming

The project is always its own git repository; the kit clone is never the project. **Preserve
existing work. Never silently merge or overwrite instructions.**

## Modes

| Mode | In the kit | Bootstrap: `python arpd/tools/install.py` | Result |
|---|---|---|---|
| **New** | `/arpd-setup` | `new "<path>"` | An empty project repository with `arpd/`, the skills and a stub `CLAUDE.md`, committed |
| **Import** | `/arpd-setup import <path-or-url>` | `import <source> "<path>"` | A new repository from existing code: a git source cloned with its history (remote renamed `upstream`, push disabled), or a folder copied after its inventory (`--yes`); committed |
| **Install** | `/arpd-setup install <path>` | `install "<path>"` | The PI's existing repository, in place; a stub `CLAUDE.md` only if none exists; nothing committed |

- **Import** suits code that is small or not under the PI's control (a published model, an ARPD
  starter such as the March example). **Install** suits the PI's own ongoing repository. Ask if
  unclear. Install never overwrites a differing file: show the PI the conflicts, and use `--force`
  only on their yes.
- **A project set up with an earlier kit** (no `arpd/`; `update` refuses it) is not set up again:
  `python arpd/tools/install.py install "<project>" --force` from the kit, then, in the project,
  `python arpd/tools/install.py owed .` and `/arpd-amend` for the charter's paths. Then
  remove the old kit leftovers (`docs/arpd-kit/`, `examples/`, `evaluation/`, root `kit/`, `tools/`,
  `reports/templates/`, `docs/EVENTS.md`) in one remove-only commit, recorded by a DEC under the
  PI's upgrade instruction.
- **Non-ARPD project** (no `PARADIGM-SPEC.md` or governing documents): *Steps for a non-ARPD
  project*. **ARPD starter:** *Steps for an ARPD starter*; its `CLAUDE.md` and `AGENTS.md` **are its
  charter**, updated in place, never treated as prior instructions.

## Warnings

`install.py` warns, without refusing, when the folder is under OneDrive (syncing can lock or
duplicate files), inside another git repository (a nested repository), or below a folder holding
`CLAUDE.md` or `AGENTS.md` (Claude Code would mix those instructions with the project's). Quote each,
recommend a folder without the problem, go on only if the PI chooses to, and record the choice in
the notes. It **refuses** without git's `user.name` and `user.email`: the PI runs the two
`git config --global` commands it prints, with their own details, then you rerun. A folder import
first prints an inventory and copies nothing: show it, ask whether the data-like files may be kept in
the repository, and rerun with `--yes` only on the PI's yes.

## Working files

The notes and the draft report are the only writes before adoption, both non-governing; writing
them authorizes nothing.

- **New and import:** the notes go into the new project at bootstrap, committed alone ("Setup notes
  (non-governing)"); later updates and the draft report stay uncommitted until adoption.
- **Install:** the PI's repository may be shared or public. Before `install.py` runs, ask once
  (`CHOICE FOR YOU (select one)`) for consent to save both files in `reports/setup/`, and record
  the answer in the notes' *Mode and consent*. With consent: there, uncommitted until adoption.
  Without: in `<parent of the target>/.arpd-setup-notes/<target name>/` (`NOTES.md` and the draft;
  never the session scratchpad), passed to `install.py install --notes` so the stub `CLAUDE.md`
  names it (if a `CLAUDE.md` exists, give the PI the printed line); at adoption the adopted report
  is written into the target, and the notes only if the PI asks.

## Existing repository review

When the project already exists (an install, or an import of the PI's own code), setup is about the
**requested change**, not a re-creation. In the Project phase:

1. **Review what exists,** in plain words: architecture (languages, components, data formats, entry
   points); the tests and the baseline run; governance (prior instructions, any `DECISIONS.md`,
   documented choices); users and outputs that depend on current behaviour. Name what the change can
   reuse unchanged and what it must modify.
2. **Never overwrite a valid existing decision.** A documented choice, an established output format
   or a calculation the PI wants kept is a **retained** capability in report §3, with a regression
   criterion ("the existing outputs are reproduced exactly on the existing test data"). Changing one
   is a decision for the PI, raised explicitly.
3. **Investigate only what the change touches;** the scope sequence applies to the change.
4. **Compatibility and migration** (formats, callers, tests, dependencies, whether old outputs must
   stay producible) each become a requirement, a decision or a gated open item; the report's §5, §6
   and §9 give the modification plan (direction only).

## Numbering: never hard-code IDs

Continue every ledger from its next free DEC, R and SA number (an empty ledger starts at DEC-01,
R-01, SA-01). An **unfilled placeholder** (an inherited "R-01 (pending)") is filled by the importing
PI's actual ruling, with "**Given:** by the importing PI on <date>". **A given ID is never reused.**
**One PI utterance, one R-NN:** a placeholder bundling several purposes takes the adoption utterance
only.

---

## Steps for a non-ARPD project (import or install)

**Nothing governing is written before adoption.** Steps 1–5 only read; steps 6–7 write, after it.

1. **Inventory,** in the project folder: structure, languages, test commands. Run the existing
   tests; keep each command, working directory, exit code and output **verbatim**, with the source's
   commit (`arpd/VERSION`, *Imported from*), outside the repository (OS temp or the session
   scratchpad), for `reports/setup/IMPORT-BASELINE.md` at generation. Never report the baseline as
   better than it is. Find the instruction files: `CLAUDE.md` (not `install.py`'s "Setup in
   progress" stub, which the charter replaces), `AGENTS.md`, `.cursorrules`,
   `.github/copilot-instructions.md`, contributor rules in the README.
2. **Read the science out of the code:** draft PARADIGM-SPEC items from what it does, each marked
   *"inferred from code: confirm"*.
3. **Map the tests** to draft requirements. A passing test is *Verified* evidence only where it
   genuinely checks the requirement; one that cannot fail, or asserts current rather than correct
   behaviour, is a defect; known-answer tests are never deleted or weakened.
4. **Reconcile the prior instructions:** each rule is *same* (dropped), a *compatible addition*
   (proposed as a Part B project rule) or a *conflict*.
5. **Interview** (the five phases, with the review above). The PI confirms each inferred spec item
   with scientific meaning; where code and intent differ, record a defect or assumption, never
   quietly align them. Conflicts and additions go in report §11–12 for the PI to rule on.
6. **Move the prior instruction files** to `docs/prior-instructions/<original-name>` in a move-only
   commit (`generation-checklist.md`, *Commit order*). The charter is the new `CLAUDE.md`.
7. **Generate** (`generation-checklist.md`); where a prior file of the same name exists, write the
   new one beside it with a `.arpd` suffix and ask. Record the source and commit, the moves and each
   reconciliation ruling as DECs.

---

## Steps for an ARPD starter

Worked case: the March example, from its own repository (`/arpd-setup import <its path>`).

1. **Inventory first.** Read `START-HERE.md`, `STATUS.md`, `DECISIONS.md` (*Waiting on the PI*),
   `PARADIGM-SPEC.md` and any import notes. Run its tests and its own checker as it stands (an older
   starter's `python tools/check_governance.py`); keep the output verbatim, outside the project.
2. **Interview, confirming rather than re-asking.** Read the written science to the PI in plain
   language to confirm; the report keeps its IDs.
   - An item marked *"(draft wording, awaiting the PI's words)"* gets the PI's own words or stays
     pending in *Waiting on the PI*; adopting "as they stand" does not clear it. Keep a replaced
     draft under "Superseded draft wording".
   - Inherited pending decisions: decide now, delegate (an SA), defer by ruling, or leave pending;
     they block only dependent work.
   - **The approval request names the path updates,** so that adoption authorizes them: in the
     charter and governing documents, `tools/` → `arpd/tools/`, `docs/EVENTS.md` →
     `arpd/docs/EVENTS.md`, `logs/` → `arpd/logs/`; the older copies (`tools/`, `docs/EVENTS.md`,
     `reports/templates/`) removed, since `arpd/` replaces them; `INDEX.md` folded into
     `START-HERE.md`'s *Map*.
3. **Remove-only commit,** first after adoption: `git rm` the older copies that exist and nothing
   else, "Remove the starter's older ARPD copies; arpd/ replaces them (no other changes)";
   `git show --stat HEAD` shows deletions only. Re-run the tests. A DEC records the removal. The
   starter's `.claude/settings.json` runs the old hook until `install.py owed .` (the `.claude/`
   step).
4. **Then edit in place,** through rulings and authorizations; superseded entries keep their text.
   - `CLAUDE.md`: the Version line (R-NN), *Authority profile* (SA-NN), the PI line, §6's examples,
     and the named path updates. Nothing else without a ruling.
   - `DECISIONS.md`: fill the placeholder or use the next free R; the new SA; DECs for the import
     (source and commit from `arpd/VERSION`) and the removal, citing
     `reports/setup/IMPORT-BASELINE.md`.
   - **Inherited adopted decisions** stay adopted ("Adopted (inherited, R-NN)" in the report). If
     the PI's words would reverse one, say so and what it would block, and ask once. Revisiting one
     is a reopening (a new DEC quoting the original rationale).
   - **Inherited pending decisions ruled on** (the DECISIONS template's format, ISO dates):
     ratified and never adopted: "**Authorized:** <date>, R-NN", "**Adopted:** <date>, <version>";
     adopted before authority existed: "**Authorized:** <date>, R-NN, ratified after adoption
     (incident I-NN)"; deferred: Status "deferred by R-NN (still to decide; dependent work stays
     blocked)", still in *Waiting on the PI*; changed: a new DEC, the old one "Superseded by
     DEC-NN". Log each (`python arpd/tools/log_event.py authorized --actor lead --ref DEC-NN --note "R-NN"`;
     `adopted` for an adoption).
   - `STATUS.md` and `START-HERE.md` rewritten in the current format, carrying over what applies;
     `INDEX.md` removed by `git rm` once its entries are in the *Map*.
5. **Records are kept as they are:** rulings, decisions, sprint records, reviews, decision packs.
6. **Import baseline** with the runs of steps 1 and 3. **Inherited checks must keep passing with the
   extension disabled.**
7. **Then** search the governing documents for phrases the adoption made stale ("pending R-01",
   "Pending adoption", "the importing PI") and update each.

---

## Resuming an interrupted setup

A relaunched session resumes; so does one after a lost session or an error. The record decides what
is authorized. Check `git log --oneline -15`, `git status --short`, `reports/setup/NOTES.md` and
`reports/setup/PROJECT-DEFINITION.md` (tracked or not; install mode without consent: the path the
stub `CLAUDE.md` names), any move- or remove-only commits, the commit "Record adoption ruling R-NN (setup in
progress)", and which checklist files exist. Then:

1. **Tell the PI** what you found (on a first relaunch, one line).
2. **Notes from an earlier kit version:** an "Interview mode" line is obsolete and ignored (never ask
   for a mode); old phases map (Intake, Research & Problem → Project; Product & Engineering →
   Requirements and Architecture; Governance & Handoff → Team & Governance, then Definition Report);
   an old `docs/discovery/SETUP.md` is read, then moved to `reports/setup/NOTES.md` by `git mv` alone.
3. **No adoption ruling:** nothing generated is authorized and nothing in the notes or a draft is
   adopted. Summarize what the notes gathered and continue from the next open topic without
   re-asking. Re-present an existing draft as it is (vN+1 only for later answers). Without notes,
   earlier answers count only if the PI confirms them. Keep committed moves; ask before discarding
   an uncommitted generated file.
4. **Adoption ruling recorded:** it and the version it cites are the authority. Continue the
   checklist from the first missing or incomplete row; never repeat a move, renumber an ID or
   rewrite a completed file. Ask the PI only what the record does not settle.
5. **Record the recovery:** before adoption in the notes (`Resumed:`), after it in `STATUS.md`'s
   `Recovered:` line; log `python arpd/tools/log_event.py resume --actor lead --note "setup resumed"`.
