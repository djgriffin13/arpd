# The ARPD guide for the PI

This guide is for you, the project's owner (the **PI**). It travels with every ARPD project, in
`arpd/docs/`, so it is always next to your work. Commands are run from the project root unless a
step says otherwise.

## 1. What you need

| Need | Why | Check |
|---|---|---|
| Claude Code (tested with 2.1.220) | Runs the agents, the skills and the hooks | `claude --version` |
| Git, with your name and email set | Every project is a git repository; its history is part of the record | `git --version`, `git config user.name`, `git config user.email` |
| Python 3.8 or later, on the PATH as `python` or `python3` (recommended, not required) | The tools, the automated checks and the logging hooks are Python (standard library only). Without it, ARPD still works: see below | `python --version` |

If git does not know your name and email, setup stops and prints the two `git config --global`
commands to run. If `python` does not resolve, `install.py owed` writes `python3`, or else the full
path of the Python that ran it, into the hooks in `.claude/settings.json`.

**Without Python.** Setup, planning, check-ins and amendments all work. The file work is done by a
shell twin of the installer (`arpd/tools/install.sh`), the two automated checks are replaced by a
read-through the agent does and reports as such, and the event log is not kept. The agents say so
once at the start of a session and record it in `STATUS.md`. Details: `arpd/docs/NO-PYTHON.md`. If
you install Python later, run `python arpd/tools/install.py owed .` to add the logging hooks.

**On Windows:** keep projects outside OneDrive or other synced folders where you can; syncing can
lock or duplicate files while git and the agents work. Put quotes around paths with spaces.
`install.py` warns about OneDrive, about a folder above the project that holds a `CLAUDE.md` or
`AGENTS.md` (Claude Code reads those too), and about a project inside another git repository.

## 2. Starting a project

Clone or download the ARPD kit, open Claude Code in that folder, and run the setup skill:

```bash
git clone <kit repository URL> my-project
cd my-project
claude
```

Then type `/arpd-setup` (or open the folder in the Claude Code desktop app, accept the folder-trust
prompt, and type it there). Setup first looks at the folder, then asks what you would like to
accomplish and whether you have existing documents, code or notes it should build on.

**Where the project lives.** Right after your first answer, setup asks where the project should be.
The usual answer is **here**: the copy of ARPD you just cloned becomes your project, in place, and
the interview continues in the same session. Setup runs `python arpd/tools/install.py convert .`
(or, without Python, `sh arpd/tools/install.sh convert .`), shows you its plan, and acts only on your
yes:

- **nothing is deleted:** ARPD's own development files (its documentation and
  README) and the clone's old git history (every
  branch, tag and stash, including anything you committed) move to a backup folder beside this one,
  `<folder>-pre-arpd-backup-<time>`, with a `RESTORE.md` saying how to undo the conversion; delete
  that folder whenever you no longer want it;
- `arpd/` and the skills in `.claude/skills/arpd-*` stay, and every file of yours is kept, including
  files you put inside the kit's folders;
- the folder gets a **fresh git history with no remote**, so nothing of yours can be pushed to the
  ARPD repository;
- a short `CLAUDE.md` says setup is in progress, until setup writes your project's charter.

Setup shows you the full plan first and converts only on your yes, in a turn of its own. You can
keep files out of git (for example participant data you put in the folder): they stay on disk but
are never committed. If the clone holds work of yours that is on no remote, setup lists it and
converts only after you agree (it goes to the backup folder with the old history). Claude Code's own
safety check may block the conversion command when it runs in auto mode; then setup gives you one
line to type at the prompt (it starts with `!`), and carries on from its output. If you have no tool in mind yet, setup converts nothing: it keeps its
notes beside the folder, discusses what tool might serve your question, and picks up from those
notes when you come back.

The other answers:

| Choice | What happens |
|---|---|
| **Your existing repository** | `install.py install <path>` adds `arpd/`, the skills and (if you have none) a stub `CLAUDE.md`, in place. Your history, code, remote and instructions are kept; an existing file that differs is never overwritten (it is reported as a conflict); nothing is committed. Your instructions are reconciled with the charter by decision, never merged silently. If the repository is not the current folder, you then open Claude Code there and type `/arpd-setup` again |
| **A new folder** | `install.py new <folder>` creates an empty project repository; this copy of ARPD stays as it is. You then open Claude Code there |
| **A new folder from existing code** (`/arpd-setup import <path or git URL>`) | A git source is cloned with its history (its remote renamed `upstream`, push disabled); a plain folder is listed first (large files, environments, data-like files) and copied only after you agree. You then open Claude Code there |

When setup needs another folder, it prints the exact commands (`cd "<folder>"`, `claude`,
`/arpd-setup`) and the interview continues there from its notes.

**What a project looks like after setup:**

| Path | What it is |
|---|---|
| `CLAUDE.md` | The team charter every agent follows. `AGENTS.md` points other tools to it |
| `START-HERE.md` | One screen: what each file is for, the map of the project (its *Map* section), and your next step with its exact prompt |
| `PARADIGM-SPEC.md`, `REQUIREMENTS.md`, `ARCHITECTURE.md`, `MASTER_PLAN.md`, `DECISIONS.md`, `STATUS.md` | The other governing documents |
| `reports/setup/` | `NOTES.md` (the interview's working notes), `PROJECT-DEFINITION.md` (the report you adopted) and, when existing code was brought in, `IMPORT-BASELINE.md` |
| `reports/planning/`, `reports/sprints/`, `plans/` | Plan drafts, sprint records and task plans, as they are created |
| `.claude/` | The skills, and (once approved) the logging hooks and the agent roles |
| `arpd/` | Everything else from the kit: templates, tools, this guide, and the event log in `arpd/logs/` |

Your own code and documents sit beside these. The project's test command is plain `python -m pytest`.

**Which instructions apply when.** Before setup, the kit's short `CLAUDE.md` (or the "setup in
progress" stub) says only that setup comes first. During setup, the `/arpd-setup` skill governs the
interview and keeps the working notes. Once you adopt the Project Definition Report, setup writes
your project's charter as `CLAUDE.md`; from then on it governs planning and implementation.
Claude Code's documentation describes `CLAUDE.md` as loaded when a session starts, with no
mid-session reload except `/compact`, and newly installed agent roles as waiting for a new session.
So after an in-place setup the setup session reads the new charter explicitly, and planning can
continue in it. Implementation starts only once the charter is loaded as project memory and, if the
team uses subagents, the agent roles are available: `/arpd-plan` tells you what to do, either type
`/compact` (which reloads `CLAUDE.md`) or, when the agent roles were installed in the same session,
start a fresh session, with the exact prompt.

## 3. The setup interview

**Six visible phases.** A progress line at the top of each turn shows where you are:

```
**SETUP**  🔵 Intake → ⚪ Objectives → ⚪ Constraints → ⚪ Design → ⚪ Development → ⚪ Definition Report
```

Each phase has a list of things setup needs to know (shown under the progress line). Setup fills
them from what you have already said and from your documents, and asks only about the rest; one
answer can fill several. Expect about 30–90 minutes, depending on the project.

- **Intake:** what you want to accomplish and what already exists; your field; how comfortable you
  are with code and how involved you want to be in technical decisions; who will use and maintain
  the tool; where the project lives; any constraints or preferences you already know of; and the
  **role** you want the agent to play: build what you specify; review your technical plan, then
  build; review the technical plan and its fit with the theory, then build; help you work out what to
  build for a research question; audit or extend existing code; or explore ideas.
- **Objectives:** the research domain and questions the tool serves (skipped if you asked for a
  technical-only focus; setup says so), your objectives, the capabilities you need, how the outputs
  will be used, and what would convince you it works. Setup can brainstorm with you here. If no tool
  emerges, it says so: ARPD is for building research tools.
- **Constraints:** technical and practical limits (platforms, internet, cost and agent credit use,
  languages and versions, data and institutional rules), then, unless you chose a technical focus,
  constraints on the theory. Each is sorted into *must*, *prefer*, *model commitment*, *must hold*
  (an invariant the code may never break) or *open question*. Setup reviews model commitments
  critically: it flags contradictions, assumptions that would build in the answer the tool is meant
  to find, and questionable assumptions, and suggests treating them as hypotheses, research
  questions or configurable model assumptions. You decide each one.
- **Design:** setup first asks whether you have a design in mind, then works through the
  architecture and the technical details with you (data, workflow, export, platform, language),
  with alternatives and trade-offs, for as many rounds as you need. Its depth follows your comfort
  with code.
- **Development:** first a choice of how the agents work (one agent with an independent reviewer,
  a lead with helpers, or several in parallel), then anything more you want to set about how they
  run; the **minimum usable version** (skipped for a very small tool, which is its own minimum) and
  the priority of everything else; how much the agents do on their own, review and check-ins; and
  the list of rules the agents will follow, each marked as ARPD's, yours, derived from the project,
  or recommended.
- **Definition Report:** the agent writes the report and checks it for gaps; you adopt it.

**Every phase ends with a summary for you to confirm.** You can confirm it, correct it, or go back
to an earlier phase. A confirmation means "you have understood me"; it is not an approval of
anything, and any phase can be reopened later. The only formal approval in setup is adopting the
report.

**Priorities.** Each feature or research question gets one: **P1 Core** (in the minimum usable
version), **P2 Next**, **P3 Planned** (committed, for a later milestone), **P4 Wanted** (only if time
allows) or **P5 Idea**. Two flags apply at any priority: *feasibility to investigate* (the team must
first find out whether or how it can be done) and *correctness-critical* (data integrity, scientific
semantics or protections). Nothing is ranked above something it depends on.

**Sources.** Setup never invents a reference. A source it cites was checked; anything else is
labelled unverified.

**One question at a time.** Each turn that waits for you ends with one labelled block:
`QUESTION FOR YOU`, `CHOICE FOR YOU` or `APPROVAL REQUIRED`. Nothing comes after it. For a choice,
every option is printed in the text (A., B., …) before any pop-up widget, so you can always answer
by letter. Where symbols do not render, an ASCII form is used (`[x]`, `[>]`, `[ ]`, `->`, a line of
`-`). The conventions are in `arpd/docs/INTERACTION.md`.

**Working notes are saved as you go,** in `reports/setup/NOTES.md`. They are **not governing**: they
record what you said so that an interrupted setup can resume, and nothing in them is adopted. They
never hold secrets or participant data, and are never pushed without your say-so. In an existing
repository, setup asks your consent before saving them there; without it they are kept beside it,
in `../.arpd-setup-notes/<repository name>/`.

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
question is a choice: plan the first piece of work now, or finish and plan later with `/arpd-plan`.

## 4. What you adopt

**The Project Definition Report** (`reports/setup/PROJECT-DEFINITION.md`) is the full
specification: the intake summary, research context and objectives (traced to the capabilities
and requirements they need), constraints and model commitments, scope and priorities, numbered
requirements (`REQ-<AREA>-NN`, nonfunctional ones `REQ-NFR-NN`) with acceptance criteria,
priority and status, the architecture and the alternatives considered, data and interface
contracts, verification, a roadmap, the development process and its rules, and open decisions with
their gates (before planning, before implementing something named, before
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
`**PLAN**  ✅ Review → 🔵 Goal → ⚪ Scope → ⚪ Draft → ⚪ Approval → ⚪ Handoff`.

1. **Review:** where the project stands, with the governance check's result.
2. **Goal:** you say what you would like to build or accomplish next, or ask the agent to examine
   the roadmap, the open requirements and the project's state and recommend priorities. (Text
   after `/arpd-plan` is taken as your goal.)
3. **Scope:** the agent sizes the effort (a targeted task, a feature, a sprint, several sprints, or
   a **feasibility investigation**: a bounded piece of work that answers whether or how something
   can be done, with a written finding rather than product code) and says if it departs from the
   roadmap and what it would displace. For a sprint-sized effort or larger you choose one sprint or
   several; for several, also how the team moves from one sprint to the next.
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
say the earlier session was lost. (If it was lost before the folder was prepared, simply start
again.)

- **Before you adopted the report:** nothing generated is authorized. The session shows what the
  notes gathered and continues from the next open item, without re-asking settled ones; phases you
  already confirmed stay confirmed. A draft
  report is shown again as the draft it is. Without notes, earlier answers count only if you
  confirm them.
- **After you adopted it:** your ruling and the version it names are the authority. Setup continues
  from the first missing file, without renumbering or rewriting completed work.
- **Notes from an earlier kit version** are read the same way: an old "Interview mode" line is
  ignored, old phase names are mapped to the new ones, an old theory choice becomes the matching
  role, and old scope answers become the starting point for priorities (never asked again).

**If a plan draft was interrupted,** run `/arpd-plan resume`. A plan without an "Approved by R-NN"
marker is shown to you as a draft. An approved plan that has not started stays approved; it is never
treated as a start.

## 10. The import baseline

When you bring existing code into the project (import, install, or a converted folder that holds your code), setup runs the project's own tests (and its
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

To bring a project's copy of the kit up to date, clone (or pull) a copy of the kit somewhere else,
then run its copy of the tool. (A folder converted in place no longer has the kit's history or
remote, so it is not itself a kit to pull.)

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
