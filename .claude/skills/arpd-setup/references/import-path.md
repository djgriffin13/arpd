# Where the project lives, existing code and resuming

**Preserve existing work. Never silently merge or overwrite instructions, and never remove a file of
the PI's.** Reusable ARPD infrastructure (`arpd/`, `.claude/skills/arpd-*`) stays separate from the
project's own documents.

## Assessing the folder

Before the first question, look (read only) and classify:

| Found | Signs | Then |
|---|---|---|
| **Setup in progress** | `reports/setup/NOTES.md` (or an older `docs/discovery/SETUP.md`) | *Resuming* |
| **Configured ARPD project** | `CLAUDE.md` names an adoption ruling in `DECISIONS.md` | Not setup: offer `/arpd-plan` or `/arpd-amend` |
| **Fresh kit clone or download** | `.arpd-kit` with only the kit's own files | Opening question for a fresh start; recommend converting it here |
| **Kit clone with the PI's material added** | `.arpd-kit`, plus untracked files (`git status`) that are not the kit's | Read them; the opening question names them; converting keeps them |
| **Existing research repository** (ARPD not set up) | Code, documents or history of the PI's, `arpd/` absent or only a stub `CLAUDE.md` | *Existing repository review*; install in place |
| **ARPD starter** | `PARADIGM-SPEC.md` and governing documents from an earlier ARPD project | *Steps for an ARPD starter* |

Also run `git remote -v`: a fresh kit clone's `origin` points at the ARPD repository, and nothing of
the PI's may ever be pushed there. Label findings as claimed by a document, seen by inspection, or
shown by a test run.

## Where the project lives (IN-05)

Ask right after the opening answer, before writing anything, as a `CHOICE FOR YOU (select one)`,
with only the options that fit. In a fresh kit clone, for example:

```text
────────────────────────────────
**🔘 CHOICE FOR YOU (select one)**
Where should the project live?
A. Here, in this folder (recommended). I turn this copy of ARPD into your project: ARPD's own
   development files (its documentation and README) are removed, arpd/ and the
   setup skills stay, every file of yours is kept, and the folder gets a fresh git history with no
   connection to the ARPD repository. Nothing is deleted: ARPD's files and the old git history go
   to a backup folder beside this one, with instructions to undo it.
B. A new folder: <absolute path>. This copy stays as it is; you then open Claude Code there.
C. Your existing repository at <path>: ARPD is added there, keeping its history; you then open
   Claude Code there.
────────────────────────────────
```

- If the PI's existing work is elsewhere: ask where it is (unless they said). **Documents** can be
  read where they are, or copied in on the PI's yes (into `docs/source/`, in a commit of their own,
  "Add the PI's source materials (no changes)"). **A code repository the PI keeps working in** is
  better set up in place there (C), which keeps its history; **code that is small or not the PI's**
  (a published model, an ARPD starter) can be imported as a copy (a new folder, below).
- The folder may hold a fresh download without git: converting it runs `git init`.

## Modes

Without Python, every `python arpd/tools/install.py` below is `sh arpd/tools/install.sh` with the
same arguments (`arpd/docs/NO-PYTHON.md` §3); a plain-folder import then needs Python or a copy by
hand.

| Mode | When | Command (from the current folder) | Result |
|---|---|---|---|
| **Convert** (default in a kit clone) | Choice A | `python arpd/tools/install.py convert .` (dry run), then `... convert . --yes` | This folder becomes the project, in place: the kit's development files removed, `arpd/` and the skills kept, the PI's files kept, a fresh history (branch main, no remote), one commit; setup continues in this session |
| **Install** | An existing repository (choice C), or a session already started in the PI's repository | `python <kit>/arpd/tools/install.py install "<path>"` | ARPD added in place; its history kept; a stub `CLAUDE.md` only if none exists; nothing committed. Continues here if `<path>` is the current folder; otherwise in a new session there |
| **New** | Choice B | `python arpd/tools/install.py new "<path>"` | An empty project repository with `arpd/`, the skills and a stub `CLAUDE.md`, committed; continues in a new session there |
| **Import** | Existing code copied into a new folder (`/arpd-setup import <path-or-url>`) | `python arpd/tools/install.py import <source> "<path>"` | A new repository from existing code: a git source cloned with its history (remote renamed `upstream`, push disabled), or a folder copied after its inventory (`--yes`); committed; continues in a new session there |

### Converting a kit clone (choice A)

1. Run the dry run: `python arpd/tools/install.py convert . --dry-run`. Show its plan in full: the
   kit files it moves to the backup folder, the PI's files it keeps (including any inside kit
   folders), any kit files the PI changed (kept), data-like and large files, any **local work**
   (commits, branches or a stash on no remote), and the backup: the kit's files and its whole `.git`
   move to `<name>-pre-arpd-backup-<time>` beside the folder, with a `RESTORE.md`; nothing is
   deleted. It refuses a clone with other git
   worktrees: that is a development checkout, not a fresh copy.
2. **Local work** that looks like ARPD development (branches other than the default, commits that
   change `arpd/` or the skills) means this is probably not a fresh copy: recommend a new folder
   (choice B) or a fresh clone, and say why. Local work of the PI's own (their notes committed in
   the clone) is kept in the backup folder's history and converted with `--include-local-work`.
3. End the turn with the conversion choice (`SKILL.md`, *Start*, step 7): convert as shown / change
   something / do not convert. Ask there whether the data-like files the plan lists may be committed;
   each the PI wants kept out becomes `--ignore <path>` (kept on disk, git-ignored, never committed).
   Large files and environments are git-ignored anyway.
4. In the next turn, on the PI's choice A, run `python arpd/tools/install.py convert . --yes` (with
   `--ignore` and `--include-local-work` as decided) and show its output in full. Quote the backup
   folder's path and its `RESTORE.md`. If Claude Code's safety check blocks the command, hand the PI
   the exact `!` line (`SKILL.md`, *Start*, step 7).
5. Write the notes (`SKILL.md`, *Start*, step 8) and continue Intake in this session. Every command
   from now on is project-relative (`python arpd/tools/...`). The kit's `CLAUDE.md` is gone; the stub
   `CLAUDE.md` says setup is in progress.
6. **The PI's own code in the converted folder** (brought in before conversion, or copied in after
   it) gets the same treatment as an install: *Existing repository review* below, and the import
   baseline (*Steps for a non-ARPD project*, step 1) before anything is changed.

A later ARPD update needs a separate, fresh clone of the kit (`install.py update . --kit <clone>`).

### New, import, or install elsewhere (choices B, C)

Propose a short project name and an **absolute** path (for a new folder, by default a sibling of
this folder), showing it in full. **Install mode:** before writing anything, ask the notes-consent
question (*Working files*). Run the command, show its output in full, and write the notes into the
target (`reports/setup/NOTES.md`, or the notes path without consent). Then end as a closing turn, no
block, telling the PI exactly: in a new terminal, `cd "<absolute path>"`, then `claude`, then
`/arpd-setup` (or open the folder in the Claude Code desktop app; accept the folder-trust prompt);
the interview continues there from the notes. If the PI replies here after that turn, repeat the
commands; never continue the interview in this session.

- Install never overwrites a differing file: show the PI the conflicts, and use `--force` only on
  their yes.
- **A project set up with an earlier kit** (no `arpd/`; `update` refuses it) is not set up again:
  `python <kit>/arpd/tools/install.py install "<project>" --force`, then, in the project,
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
the notes. `new`, `import` and `convert` **refuse** without git's `user.name` and `user.email`: the PI runs the two
`git config --global` commands it prints, with their own details, then you rerun. A folder import
first prints an inventory and copies nothing: show it, ask whether the data-like files may be kept in
the repository, and rerun with `--yes` only on the PI's yes.

## Working files

The notes and the draft report are the only writes before adoption, both non-governing; writing
them authorizes nothing.

- **Convert, new and import:** the notes go into the project when it is prepared, committed alone
  ("Setup notes (non-governing)"); later updates and the draft report stay uncommitted until
  adoption.
- **Install:** the PI's repository may be shared or public. Before `install.py` runs, ask once
  (`CHOICE FOR YOU (select one)`) for consent to save both files in `reports/setup/`, and record
  the answer in the notes' *Folder and consent*. With consent: there, uncommitted until adoption.
  Without: in `<parent of the target>/.arpd-setup-notes/<target name>/` (`NOTES.md` and the draft;
  never the session scratchpad), passed to `install.py install --notes` so the stub `CLAUDE.md`
  names it (if a `CLAUDE.md` exists, give the PI the printed line); at adoption the adopted report
  is written into the target, and the notes only if the PI asks.

## Existing repository review

When the project already exists (an install, an import of the PI's own code, or a converted folder
holding the PI's code), setup is about the
**requested change**, not a re-creation. During Intake and Objectives:

1. **Review what exists,** in plain words: architecture (languages, components, data formats, entry
   points); the tests and the baseline run; governance (prior instructions, any `DECISIONS.md`,
   documented choices); users and outputs that depend on current behaviour. Name what the change can
   reuse unchanged and what it must modify. Keep apart what the documents claim, what inspection
   shows, what the tests establish, and what the PI confirms: a passing unit test is not parameter
   recovery, construct validity or a reproduced published result.
2. **Never overwrite a valid existing decision.** A documented choice, an established output format
   or a calculation the PI wants kept is a **retained** capability in report §5, with a regression
   criterion ("the existing outputs are reproduced exactly on the existing test data"). Changing one
   is a decision for the PI, raised explicitly. Existing decisions are preserved, not immune from
   criticism: a concern about one is raised as a labelled observation.
3. **Investigate only what the change touches;** Development's minimum usable version and priorities
   apply to the change.
4. **Compatibility and migration** (formats, callers, tests, dependencies, whether old outputs must
   stay producible) each become a requirement, a decision or a gated open item; the report's §7, §8
   and §11 give the modification plan (direction only).

## Numbering: never hard-code IDs

Continue every ledger from its next free DEC, R and SA number (an empty ledger starts at DEC-01,
R-01, SA-01). An **unfilled placeholder** (an inherited "R-01 (pending)") is filled by the importing
PI's actual ruling, with "**Given:** by the importing PI on <date>". **A given ID is never reused.**
**One PI utterance, one R-NN:** a placeholder bundling several purposes takes the adoption utterance
only.

---

## Steps for a non-ARPD project (import or install)

**Nothing governing is written before adoption.** Steps 1–5 only read; steps 6–7 write, after it.

1. **Inventory,** in the project folder, during Intake or Objectives and **before the report is
   drafted**: structure, languages, test commands. Do not open data-like
   files (the inventory lists them) without the PI's permission for that use, and never copy them
   into a scratch folder. Run the existing tests (`<command>; echo "exit=$?"`); keep each command, working directory, printed exit code and
   full output **verbatim**, never trimmed, with the source's
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
5. **Interview** (the phases, with the review above). The PI confirms each inferred spec item
   with scientific meaning; where code and intent differ, record a defect or assumption, never
   quietly align them. Conflicts and additions go in report §12–13 for the PI to rule on.
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
   starter's `python tools/check_governance.py`), each as `<command>; echo "exit=$?"`; keep the full
   output verbatim, outside the project. Do this **before any commit of your own** (adoption
   included), so the baseline shows the starter exactly as received.
2. **Interview, confirming rather than re-asking.** Read the written science to the PI in plain
   language to confirm; the report keeps its IDs. Ask for the research question in the PI's own
   words, and ask the authority boundaries (what to bring back, time and cost limits); never carry
   the starter's SA-01 defaults over without asking.
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
3. **Remove-only commit, the last generation step** (`generation-checklist.md`, *Commit order* 6):
   the starter's `.claude/settings.json` runs `tools/hooks/log_hook.py` until `install.py owed .`
   (the `.claude/` step, on the PI's yes) re-points it, and a hook whose script is missing blocks
   every prompt. After that step, `git rm` the older copies that exist and nothing else, "Remove the
   starter's older ARPD copies; arpd/ replaces them (no other changes)"; `git show --stat HEAD`
   shows deletions only. Re-run the tests (`; echo "exit=$?"`) and quote the output. A DEC, written
   at generation, records the removal; until it happens the *Map* lists `tools/` as "pending:
   removed after the `.claude/` step". If the PI declines the `.claude/` step, keep `tools/hooks/`
   and record that. An old git-ignored root `logs/` (written by the old hook before the re-point)
   moves into `arpd/logs/` (a plain move; it is not tracked).
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
6. **Import baseline** with the runs of step 1, committed after the notes (`generation-checklist.md`,
   row 10). **Inherited checks must keep passing with the
   extension disabled.**
7. **Then** search the governing documents for phrases the adoption made stale ("pending R-01",
   "Pending adoption", "the importing PI") and update each.

---

## Resuming an interrupted setup

A relaunched session resumes; so does one after a lost session or an error. The record decides what
is authorized. Check `git log --oneline -15`, `git status --short`, `reports/setup/NOTES.md` (or the
notes beside an unprepared folder, `<parent>/.arpd-setup-notes/<folder name>/NOTES.md`: then the
folder is still a kit clone, and *Start* steps 5–8 follow once a tool is in view) and
`reports/setup/PROJECT-DEFINITION.md` (tracked or not; install mode without consent: the path the
stub `CLAUDE.md` names), any move- or remove-only commits, the commit "Record adoption ruling R-NN (setup in
progress)", and which checklist files exist. Then:

1. **Tell the PI** what you found, in one or two lines (where the interview stopped: the phase, the
   last confirmed closeout, the pending question), and ask in a `CHOICE FOR YOU (select one)`: A.
   continue from there; B. review the notes' summary first; C. start the interview again (the
   notes are kept, superseded).
2. **Notes from an earlier kit version** (no required-item tables): read them, and fill the
   required items from what they record, each as Confirmed (the PI's words) or Inferred; never
   re-ask what they settle. An "Interview mode" line is obsolete and ignored (never ask for a mode).
   - Phases map: v0.5–v0.6 Project → Intake and Objectives; Requirements → Objectives and Design;
     Architecture → Design; Team & Governance → Development. v0.4 Intake, Research & Problem →
     Intake and Objectives; Product & Engineering → Objectives and Design; Governance & Handoff →
     Development.
   - A theory-context choice maps to the scientific axis, never to a role letter (the old letters
     mean something else): old A ("guide implementation without evaluating") → *respect as given*;
     old B ("identify concerns") → *alignment review*; old C ("help develop") → *co-development*; old
     D ("leave theory aside") → *technical only*. The role (IN-08) is then Inferred from the axis and
     the project, and confirmed in the Intake summary; never copy the old letter.
   - The three scope answers become Development input: the minimum usable version → DV-02 and P1
     candidates; the ideal version → P2 or P3 candidates; nice-to-haves → P4 or P5. Confirm the
     placement in the Development summary; never ask the scope questions again.
   - An old `docs/discovery/SETUP.md` is read, then moved to `reports/setup/NOTES.md` by `git mv`
     alone.
   - Confirmed phases are those whose closeout the notes record; earlier notes record none, so each
     phase is summarized and confirmed as it is reached.
3. **No adoption ruling:** nothing generated is authorized and nothing in the notes or a draft is
   adopted. Summarize what the notes gathered and continue from the next Open required item without
   re-asking. Re-present an existing draft as it is (vN+1 only for later answers); a draft in the
   older 13-section layout is redrafted in the current one as vN+1, once Development has set the
   priorities, with a *Change history* row saying so. Without notes,
   earlier answers count only if the PI confirms them. Keep committed moves; ask before discarding
   an uncommitted generated file.
4. **Adoption ruling recorded:** it and the version it cites are the authority. Continue the
   checklist from the first missing or incomplete row; never repeat a move, renumber an ID or
   rewrite a completed file. Ask the PI only what the record does not settle.
5. **Record the recovery:** before adoption in the notes (`Resumed:`), after it in `STATUS.md`'s
   `Recovered:` line; log `python arpd/tools/log_event.py resume --actor lead --note "setup resumed"`.
