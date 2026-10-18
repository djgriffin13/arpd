# The ARPD guide for the PI

This guide is for you, the project's owner (the **PI**). It travels with every ARPD project, in
`arpd/docs/`, so it is always next to your work. Commands are run from the project root unless a
step says otherwise.

## 1. What you need

| Need | Why | Check |
|---|---|---|
| Claude Code (tested with 2.1.220) | Runs the agents, the skills and the hooks | `claude --version` |
| Git, with your name and email set | Every project is its own git repository; its history is part of the record | `git --version`, `git config user.name`, `git config user.email` |
| Python 3.8 or later, on the PATH as `python` | The tools and the logging hooks are Python (standard library only) | `python --version` |

If git does not know your name and email, setup stops and prints the two `git config --global`
commands to run. If `python` does not resolve, `install.py owed` writes `python3`, or else the full
path of the Python that ran it, into the hooks in `.claude/settings.json`.

**On Windows:** keep projects outside OneDrive or other synced folders where you can; syncing can
lock or duplicate files while git and the agents work. Put quotes around paths with spaces.
`install.py` warns about OneDrive, about a folder above the project that holds a `CLAUDE.md` or
`AGENTS.md` (Claude Code reads those too), and about a project inside another git repository.

## 2. Starting a project

You clone the ARPD kit once. **The kit clone is never your project.** Each project is a separate
folder with its own git repository, and you can start any number of projects from the same clone.

```bash
git clone <kit repository URL> arpd-kit
cd arpd-kit
claude
```

Then type one of:

| Command | What it does |
|---|---|
| `/arpd-setup` | A new project |
| `/arpd-setup import <path or git URL>` | A new project that starts from existing code |
| `/arpd-setup install <path>` | Adds ARPD to an existing repository, in place |

**A new project.** Setup first asks what you would like to build: an overview of the tool, who
would use it, and what you imagine it doing. A rough idea, a detailed specification or a pointer to
existing documents or code are all fine. Setup then proposes a project folder (by default a sibling
of the kit clone, `../<project-name>`) and, with your agreement, runs
`python arpd/tools/install.py new <folder>`. That creates the folder as a new git repository and
commits a starting point: the `arpd/` folder, the skills in `.claude/skills/arpd-*`, a `.gitignore`
and a stub `CLAUDE.md` saying setup is in progress.

**Then you reopen Claude Code in the project.** Setup prints the commands:

```bash
cd "<project folder>"
claude
```

(Or open the folder in the Claude Code desktop app; accept the folder-trust prompt.) Type
`/arpd-setup` again. The interview continues there, from your first answer. Everything from
here on is written in the project, never in the kit clone.

**Importing existing code.** A git source (a path or a URL) is cloned into the new folder with its
history. Its `origin` remote is renamed `upstream` and its push URL is disabled, so the project can
fetch from the original but never pushes back to it. A plain folder is listed first (large files,
environments, data-like files) and copied only after you agree. Environments such as `.venv` and
`node_modules` are not copied, and files of 50 MB or more are git-ignored. Then you reopen Claude
Code in the new folder, as above. Setup reviews what exists rather than running the full fresh
interview.

**Installing into your own repository.** `install.py install <path>` adds `arpd/`, the skills and
(if you have none) a stub `CLAUDE.md` to the repository in place. It never overwrites an existing
file that differs; it reports it as a conflict. It commits nothing. Then reopen Claude Code in that
repository. Your existing instructions are kept and reconciled with the charter by decision, never
merged silently.

**What a project looks like after setup:**

| Path | What it is |
|---|---|
| `CLAUDE.md` | The team charter every agent follows. `AGENTS.md` points other tools to it |
| `START-HERE.md` | One screen: what each file is for, the map of the project (its *Map* section), and your next step with its exact prompt |
| `PARADIGM-SPEC.md`, `REQUIREMENTS.md`, `ARCHITECTURE.md`, `MASTER_PLAN.md`, `DECISIONS.md`, `STATUS.md` | The other governing documents |
| `reports/setup/` | `NOTES.md` (the interview's working notes), `PROJECT-DEFINITION.md` (the report you adopted) and, after an import or install, `IMPORT-BASELINE.md` |
| `reports/planning/`, `reports/sprints/`, `plans/` | Plan drafts, sprint records and task plans, as they are created |
| `.claude/` | The skills, and (once approved) the logging hooks and the agent roles |
| `arpd/` | Everything else from the kit: templates, tools, this guide, and the event log in `arpd/logs/` |

Your own code sits beside these. The project's test command is plain `python -m pytest`.

## 3. The setup interview

**Five visible phases.** A progress line at the top of each turn shows where you are:

```
SETUP  ● Project → ○ Requirements → ○ Architecture → ○ Team & Governance → ○ Definition Report
```

Under it is a short list of the topics still open in the current phase. One answer can close
several. Expect about 20–60 minutes, depending on the project.

- **Project:** what you want to build and what already exists. If a theory or model should inform
  the tool, you choose how the team treats it: use it to guide implementation without evaluating
  it, identify concerns, help develop it, or leave theory aside. For a tool that only collects data,
  the question is skipped.
- **Requirements:** three scope questions, each asked once: the **minimum usable version**, the
  **ideal version** (naming the features you care about), and **nice-to-have** features you do not
  expect in the first release. Then workflows, data, and how well it must work. Each requirement
  gets acceptance criteria: how anyone could check it was met.
- **Architecture:** for each material choice, the credible alternatives and their trade-offs,
  including existing tools that might avoid custom software, then a recommendation. You are not
  asked to choose a technology cold.
- **Team & Governance:** how the agents are arranged, how much they decide on their own, review and
  check-ins, and the open decisions, each with the point by which it must be settled.
- **Definition Report:** the agent writes the report and checks it for gaps.

**One question at a time.** Each turn that waits for you ends with one labelled block:
`QUESTION FOR YOU`, `CHOICE FOR YOU` or `APPROVAL REQUIRED`. Nothing comes after it. For a choice,
every option is printed in the text (A., B., …) before any pop-up widget, so you can always answer
by letter. Where symbols do not render, an ASCII form is used (`[x]`, `[>]`, `[ ]`, `->`, a line of
`-`). The conventions are in `arpd/docs/INTERACTION.md`.

**Working notes are saved as you go,** in `reports/setup/NOTES.md`. They are **not governing**: they
record what you said so that an interrupted setup can resume, and nothing in them is adopted. They
never hold secrets or participant data, and are never pushed without your say-so. In install mode,
setup asks your consent before saving them in your repository; without it they are kept beside
it, in `../.arpd-setup-notes/<repository name>/`.

**Data semantics stay yours.** What a blank answer means, missing versus zero, duplicates and
repeated submissions, what an identifier means, aggregation, numerical precision, changes to
collected variables: agents choose how to implement these, never what they mean, unless you name a
policy (recorded in SA-01 or a ruling).

**Authority profile.** You choose how much the team decides on its own: *consult first* (it asks
before adopting any consequential scientific assumption), *bounded autonomy* (the suggested default:
it works within agreed bounds and reports at checkpoints) or *exploratory autonomy* (it tries and
compares alternatives, then brings you the decision). It is recorded as SA-01, and you can change it
at any time.

**Setup ends with planning pending.** It never builds anything and writes no sprint. The last
question is a choice: plan the first sprint now, or finish and plan later with `/arpd-plan`.

## 4. What you adopt

**The Project Definition Report** (`reports/setup/PROJECT-DEFINITION.md`) is the full
specification: overview and scope, numbered requirements (`REQ-<AREA>-NN`, nonfunctional ones
`REQ-NFR-NN`) with acceptance criteria, priority and status, the architecture and the alternatives
considered, data and interface contracts, verification, a roadmap, the team, governance, and open
decisions with their gates (before planning, before implementing something named, before
deployment). Setup checks its form with `arpd/tools/check_report.py` before showing each version.

Each item has a status:

| Status | Meaning |
|---|---|
| Adopted-on-adoption | You stated or accepted it; adopted with the report |
| Proposed | The lead's recommendation; not adopted unless you accept it |
| Provisional | A working assumption, with a gate |
| Delegated | Within a standing authorization's bounds |
| Open | A decision with a gate; it goes to *Waiting on the PI* in `DECISIONS.md` |
| Excluded | Out of scope |

Revise the report as often as you like; each revision is a new version. Only when you adopt a
version, in your own words, under `APPROVAL REQUIRED`, is anything governing written. Your words are
recorded verbatim as ruling R-01, naming the version. **Adoption authorizes the governing documents,
not development.** After adoption the report is kept as the record; the governing documents carry
its content and win where they differ.

**Your own words authorize.** No fixed phrase is needed. The lead records your words verbatim as a
ruling (R-NN), with its reading on a separate line. A message relayed by another agent binds only
once you confirm it yourself. There are five kinds of thing you might say:

| Kind | Example | Effect |
|---|---|---|
| An interview answer | "I want a chat window for two players." | Informs the lead; decides nothing |
| A proposal or draft | A requirement the lead suggests; a plan draft | Nothing adopted, scheduled or authorized |
| A ruling or standing authorization | "Make light-touch review the default." | Binds within its scope |
| An approved plan | "I approve PLAN-2026-10-20 v3." | Approves that version's scope. Starts nothing |
| An execution authorization | "Begin sprint 1 now." | Starts the work it names |

Silence, "sounds good" about a nearby draft, or a choice that only moves the interview on is never a
ruling, an approval or a start.

Your project's `START-HERE.md` explains, one line each, how an **invariant** (`PARADIGM-SPEC.md`), a
**requirement** (`REQUIREMENTS.md`) and an **acceptance criterion** (its *Requirement details*)
differ.

## 5. Readiness: where setup, planning and execution stand

`STATUS.md` has a *Readiness* block above its numbered sections:

- **Setup:** in progress, or adopted (R-NN);
- **Planning:** not started, draft (PLAN-…, vN), or approved (PLAN-…, vN, R-NN);
- **Execution:** not started, authorized (R-NN or SA-NN, scope), in progress (S0N), or complete;
- **Next step:** finish setup, run `/arpd-plan`, review plan, begin implementation, check in, or
  amend.

`START-HERE.md` gives the same next step, with the exact prompt. `/arpd-checkin` cross-checks these
lines against the records; when they disagree, the records win.

## 6. Planning, and plan approval versus execution

Type `/arpd-plan` (in any session, after setup or between sprints). It reads the project's records,
so you do not repeat yourself. Its progress line is
`PLAN  ✓ Review → ● Priorities → ○ Draft → ○ Approval → ○ Handoff`.

1. **Review:** where the project stands, with the governance check's result.
2. **One sprint or several:** you choose. For several, you also choose how the team moves from one
   sprint to the next.
3. **Priorities:** the agent proposes a focus; you correct it.
4. **Draft:** `reports/planning/PLAN-<date>.md`, marked DRAFT, with a version. It decides nothing.
5. **Revise:** each revision is a new, committed version.
6. **Approval:** you approve a **specific version**. Approving a plan does **not** start work.
7. **Begin now or later:** "now" starts the first sprint and writes its record,
   `reports/sprints/SPRINT-NN.md`; "later" puts the exact start prompt in `START-HERE.md`.

Three things are kept apart:

| Thing | What it is | Recorded as |
|---|---|---|
| **Plan approval** | You approve an exact version of a sprint plan | A ruling, R-NN, citing file, version and commit, with *Scope of approval* and *Execution authorized* lines |
| **Execution authority** | Your direction to start one sprint, or a series | A ruling, R-NN (it can be the same ruling). For a series, also a standing authorization (SA-NN) |
| **Task-plan approval** | A scoped `plans/NNN-<slug>.md` inside a sprint | The plan's own status. Routine ones are approved by the lead |

- **Sprint start.** The sprint record's Part 1 is written from the approved plan, with the rows
  *Approved plan*, *Execution authorized by* and *Transition policy*, and is then preserved.
- **Several sprints.** By default there is a check-in with you at every sprint boundary. To let the
  team continue without a new ruling each time, your words become an SA naming the sprints, the
  transition conditions and when to consult you. Every boundary still gets a close-out, independent
  review and checks. A continuation SA never covers what the charter reserves to you.
- **Project defaults.** "From now on, always …" about review depth (how much you read and approve:
  light-touch, standard or comprehensive, defined in `arpd/docs/INTERACTION.md` §1), transition policy or planning
  cadence is a governing change. `/arpd-amend` applies it from your clear words, without asking you
  to approve them again.

There are three levels of plan: the **roadmap** (`MASTER_PLAN.md`; milestones change only by your
ruling), the **sprint plan** (`reports/planning/`, then the sprint record's Part 1) and the **task
plan** (`plans/`).

## 7. Permissions and logging

Setup installs two things into `.claude/`, with your approval:

- **`.claude/settings.json`:** hooks that run `arpd/tools/hooks/log_hook.py` on each Claude Code
  event;
- **`.claude/agents/`:** the implementer and reviewer roles the lead delegates to.

**Why you are asked.** Claude Code asks before any write to `.claude/`, because files there can run
commands and define agents. Approve if you want event logging and delegation. Setup never works
around the prompt. A non-interactive run cannot approve it; the items are then owed (section 8).

**What the logging records** (`arpd/logs/events.jsonl`, one line per event, git-ignored): the time;
the event type (session start or end, prompt submitted, tool call finished, subagent start or stop,
turn ended or failed, compaction, notification); session and subagent IDs; tool name, duration and
outcome; the length of a prompt in characters; and, where Claude Code supplies them, the start
reason, the model and an error type.

**What it never records:** prompt text (unless you set `ARPD_LOG_PROMPT_TEXT=1`), tool inputs and
outputs, file contents, or model reasoning. It cannot measure your active time; record that yourself
with `python arpd/tools/log_event.py pi_time --actor pi --minutes N`. Details: `arpd/docs/EVENTS.md`.

**Confirm that it works:**

1. `python arpd/tools/check_governance.py`: the steps "Event logging and agent roles installed" and
   "ARPD skills installed" should be **PASS**.
2. Do one small thing in a session (for example, ask "Where are we?").
3. `python arpd/tools/summarize_events.py --sessions` should show a row for that session.

The checker looks at files only; step 3 shows that the hooks actually fired.

## 8. Owed items

Anything setup could not install (usually the `.claude/` items) is recorded in `DECISIONS.md` (for
example "event logging not installed"), in `STATUS.md` §6 *Owed*, and under *Known gaps* in
`START-HERE.md`. To finish, run from the project root:

```bash
python arpd/tools/install.py owed .
```

It installs `.claude/settings.json` (into an existing one, only the `hooks` key is merged), the agent
roles, and any missing skill. Missing skills come from the kit, so add `--kit <path to the kit
clone>` if it says so. Then confirm as in section 7. Until a decision records a gap, the checker
reports it as MISSING; once recorded, as ADVISORY.

## 9. Resuming after a lost session

If a session ends unexpectedly, start a new one in the project and say:

> Start a new session on this project: follow the charter's recovery steps.

The new session becomes the lead. It reads `STATUS.md` and the base commit it names; runs
`git log --oneline <base>..HEAD` and
`python arpd/tools/summarize_events.py --since <the time STATUS.md was last rewritten> --sessions`;
**quotes their output** rather than describing history from memory; writes a `Recovered:` line in
`STATUS.md`; and logs a `resume` event. If the log is absent (a fresh clone or another machine), it
says so and uses the last exported `reports/sprints/SPRINT-NN-events.jsonl`. Unfinished work from the
lost session is treated as unreviewed.

**If setup was interrupted,** open Claude Code in the project folder, run `/arpd-setup` again and
say the earlier session was lost. (If it was lost before the project folder existed, start again
from the kit clone.)

- **Before you adopted the report:** nothing generated is authorized. The session shows what the
  notes gathered and continues from the next open topic, without re-asking settled ones. A draft
  report is shown again as the draft it is. Without notes, earlier answers count only if you
  confirm them.
- **After you adopted it:** your ruling and the version it names are the authority. Setup continues
  from the first missing file, without renumbering or rewriting completed work.
- **Notes from an earlier kit version** are read the same way: an old "Interview mode" line is
  ignored, and old phase names are mapped to the new ones.

**If a plan draft was interrupted,** run `/arpd-plan resume`. A plan without an "Approved by R-NN"
marker is shown to you as a draft. An approved plan that has not started stays approved; it is never
treated as a start.

## 10. The import baseline

When you import or install into existing code, setup runs the project's own tests (and its
governance check, if it has one) before changing anything. After you adopt the report, it records
the results **verbatim** in `reports/setup/IMPORT-BASELINE.md`: the source and commit, each
command with its working directory, exit code and output, and what was not run. It is written once,
then frozen. Failures are recorded as they are. The import decision and the first sprint cite it.

## 11. Reading the governance check

`python arpd/tools/check_governance.py` prints one line per step, a *Not checked* block, and an
overall result.

| Status | Meaning |
|---|---|
| **PASS** | The step found nothing wrong in what is recorded |
| **FAIL** | Something recorded breaks a rule (for example, a consequential decision adopted without the authority its route requires) |
| **MISSING** | The step could not check something (a file or a date is missing, or a date is not ISO 8601) |
| **PENDING** | Something awaits your decision (for example, the charter is not yet adopted) |
| **ADVISORY** | A note that does not change the result (for example, a gap recorded as owed) |

Overall: **FAIL** if any step failed; otherwise **INCOMPLETE** if any step is MISSING or PENDING;
otherwise **PASS**.

- **No sprint yet is fine.** Planning pending is a valid state.
- **Open sprints** are checked only at Part 1: the plan approval and execution authority it cites
  must exist and not be pending. Older records without these rows get an ADVISORY.
- **The map.** Every top-level entry should be listed in the *Map* section of `START-HERE.md`.
- **A PASS is not authorization to execute.** Only an approved plan and your start direction start
  work.

The checker reads records. It cannot show that a date is true or that a ruling is in your own words,
and it does not run the project's tests; run `python -m pytest` for those. The *Not checked* block
lists its limits on each run.

## 12. Updating the `arpd/` folder

To bring a project's copy of the kit up to date, pull the kit clone, then run its copy of the tool:

```bash
python <kit clone>/arpd/tools/install.py update <project folder>
```

`arpd/VERSION` records which kit version and commit the project's copy came from. The update
refreshes `arpd/` (keeping `arpd/logs/`) and `.claude/skills/arpd-*`, and prints what changed.
Files no longer in the kit are listed, and removed only with `--prune`. Nothing is committed: review
the changes and commit them yourself. If it says the settings or agent roles changed, run
`python arpd/tools/install.py owed .` as well. An update never changes your governing documents;
adopting a new charter rule is a ruling, through `/arpd-amend`. A project set up before v0.6 has no
`arpd/` folder; see the kit's release notes for its options.

## 13. While you work

| You want to… | Do this |
|---|---|
| Plan the next sprint, or several | `/arpd-plan` |
| Start or continue work | Use the prompt in `START-HERE.md`. Work starts only from an approved plan and your start direction |
| See where things stand, and what decisions are coming | `/arpd-checkin` |
| Decide something | Say it. The lead records your words verbatim as a ruling |
| Change the rules, the specification, a project default, the milestones, or what the team may decide alone | `/arpd-amend`. A clear instruction is enough |
| Get an explanation | Ask. The agent explains at your level when a decision depends on it |
| Check the governance records | `python arpd/tools/check_governance.py` (section 11) |
| See time and activity | `python arpd/tools/summarize_events.py` (add `--sessions` for one row per session) |
| Resume after a lost session | "Start a new session on this project: follow the charter's recovery steps." (section 9) |
