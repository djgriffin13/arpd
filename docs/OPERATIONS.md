# Operating ARPD: installation, planning, logging, recovery and checks

This is the detail behind the kit's `QUICKSTART.md` (at the kit's root, or in `docs/arpd-kit/` after setup). Commands are run from the project root.

## 1. Prerequisites

| Need | Why | Check |
|---|---|---|
| Claude Code (tested with 2.1.220) | Runs the agents, the skills and the hooks | `claude --version` |
| Git | The project's history is part of its record | `git --version` |
| Python 3.8 or later, on the PATH as `python` | The hooks call `python tools/hooks/log_hook.py`; the tools are Python | `python --version` |
| numpy and pytest (only for the March example) | The example model and its tests | `pip install -r examples/march-1991/requirements.txt` |

The kit itself needs nothing else. If `python` does not resolve on your machine, setup uses `python3`
or the full path in `.claude/settings.json` instead.

## 2. Installing and invoking the skills

The skills live in this repository's `.claude/skills/`. Opening the cloned kit folder in Claude Code
(`cd <kit folder>` then `claude`) makes them available:

| Command | What it does |
|---|---|
| `/arpd-setup` | Fresh project: the interview and the Project Definition Report, then, once you adopt the report, the governing documents and tools, in this repository. Ends with planning pending; writes no sprint and builds nothing |
| `/arpd-setup import <path or git URL>` | Brings existing code into this repository, and sets it up |
| `/arpd-setup install <path>` | Installs the charter, governing documents, tools, hooks and agents into your existing repository at `<path>`. It also copies the `arpd-*` skills and the `kit/` folder there, so planning, check-ins and amendments work from that repository |
| `/arpd-plan` | Plans the next sprint, or a series, with you: review, priorities, a versioned draft, your approval of one version, then begin now or later. Arguments: `one`, `multiple`, `resume` |
| `/arpd-checkin` | A plain-language check-in: readiness, what works, what needs you, decisions ahead, what was decided without you |
| `/arpd-amend` | Records a ruling or a standing authorization verbatim; amends the charter, the specification, a project default or the milestones |

All four follow the same conventions for turns that wait for you (`kit/docs/INTERACTION.md`): one
labelled block (`QUESTION FOR YOU`, `CHOICE FOR YOU`, `APPROVAL REQUIRED`) last in the turn, choice
options printed as text before any widget, and a progress line in setup and planning. Where Unicode
does not render, an ASCII form is used (`[x]`, `[>]`, `[ ]`, `->`, a line of `-`).

## 3. Your authority, and your words

- **The Project Definition Report** (`reports/PROJECT-DEFINITION.md`). Setup ends by writing this
  report from the interview: overview and scope (minimum usable version, ideal version,
  nice-to-have), numbered requirements (`REQ-<AREA>-NN`, nonfunctional ones `REQ-NFR-NN`) with
  acceptance criteria, priority and status, the architecture with the alternatives considered, data
  and interface contracts, verification, roadmap, team, governance, and open decisions, each with a
  gate (before planning, before implementing something named, before deployment). It is a draft,
  with a version, until you adopt a version in your own words. That ruling (R-01) names the version
  it adopts. Adoption authorizes writing the governing documents from the report, not development:
  only an approved plan and your start direction start work (section 5). After adoption the report
  is kept as the record; the governing documents carry its content and win where they differ.
  Setup checks its form with `check_report.py` (`kit/tools/`, copied to the project's `tools/`)
  before showing each version.
- **Statuses in the report.** *Adopted-on-adoption* (you stated or accepted it; adopted with the
  report), *Proposed* (the lead's recommendation; not adopted unless you accept it), *Provisional* (a
  working assumption with a gate), *Delegated* (within a standing authorization's bounds), *Open*
  (a decision with a gate; it goes to `DECISIONS.md` *Waiting on the PI*) and *Excluded* (out of
  scope).
- **Data semantics stay yours.** Missing versus zero, duplicate or repeated observations, what an
  identifier means, aggregation, numerical precision or estimation assumptions, changes to collected
  variables and replacing unavailable data are consequential (`CLAUDE.md` §6). Agents choose how to
  implement them, never what they mean, unless you name a policy (recorded in SA-01 or a ruling).
- **Authority profile.** At setup you choose how much the team decides on its own: *consult first*
  (it asks before adopting any consequential scientific assumption), *bounded autonomy* (the
  suggested default: it works within agreed boundaries and reports at checkpoints) or *exploratory autonomy*
  (it tries and compares alternatives, then brings you the decision to adopt). It is recorded as a
  standing authorization (SA-01) and you can change it at any time, in any message.
- **Your own words authorize.** No fixed phrase is needed. The lead agent records your words
  verbatim as a ruling (R-NN), with its reading on a separate line. A message relayed by another
  agent binds only once you confirm it yourself.
- **Five kinds of thing you might say** (`kit/docs/INTERACTION.md` §1):

| Kind | Example | Effect |
|---|---|---|
| An interview answer | "I want a chat window for two players." | Informs the lead; decides nothing. Saved in working notes |
| A proposal or draft | A requirement the lead suggests; a plan draft | Nothing adopted, scheduled or authorized |
| A ruling or standing authorization | "Make light-touch review the default." | Binds within its scope. `/arpd-amend` records it with no second approval |
| An approved plan | "I approve PLAN-2026-10-20 v3." | Approves that version's scope. Starts nothing |
| An execution authorization | "Begin sprint 1 now." | Starts the work it names |

  Silence, "sounds good" about a nearby draft, or a choice that only moves the interview on is never
  a ruling, an approval or a start. When you approve a plan without saying more, only planning
  approval is recorded.

## 4. Readiness: where setup, planning and execution stand

`STATUS.md` has a *Readiness* block above its numbered sections:

- **Setup:** in progress, or adopted (R-NN);
- **Planning:** not started, draft (PLAN-…, vN), or approved (PLAN-…, vN, R-NN);
- **Execution:** not started, authorized (R-NN or SA-NN, scope), in progress (S0N), or complete;
- **Next step:** finish setup, run `/arpd-plan`, review plan, begin implementation, check in, or
  amend.

`START-HERE.md` gives you the same next step, with the exact prompt. Right after setup, readiness is
"Setup: adopted, Planning: not started, Execution: not started, Next step: run /arpd-plan".

`/arpd-checkin` cross-checks these lines against the records: the adoption ruling, the plan files
and their approval rulings, the sprint records. When they disagree, the records win and the check-in
says STATUS is out of date.

**A checker PASS is not authorization to execute.** The governance check compares only the
readiness block's *Execution* line with the sprint records, as an advisory step ("Readiness agrees
with the sprint records"): an open sprint record while it says "not started", or "in progress" with
no open record. The *Setup*, *Planning* and *Next step* lines are listed under *Not checked*. Work
starts only from an approved plan and an execution authorization (section 5).

## 5. Plan approval, execution authority and multi-sprint authorizations

Three things are kept apart:

| Thing | What it is | Recorded as |
|---|---|---|
| **Plan approval** | You approve an exact version of a sprint plan (`reports/planning/PLAN-…md`, vN) | A ruling, R-NN, citing the file, version and commit, with *Scope of approval* and *Execution authorized* lines |
| **Execution authority** | Your direction to start: one sprint, or a series | A ruling, R-NN (it can be the same ruling, if you approve and start in one message). For a series, also a standing authorization (SA-NN) |
| **Task-plan approval** | A scoped `plans/NNN` plan inside a sprint | The plan's own status. Routine ones are approved by the lead (`CLAUDE.md` §5) |

- **A draft decides nothing.** Plan drafts live in `reports/planning/`, marked DRAFT, with a
  version. Each version is committed. After approval, the only edit a plan gets is its status
  marker; a change is a new version and needs a new approval.
- **Sprint start.** When a sprint starts, its record `reports/sprints/SPRINT-NN.md` gets Part 1,
  written from the approved plan, with three rows: *Approved plan* (PLAN-… vN, approved by R-NN),
  *Execution authorized by* (R-NN or SA-NN) and *Transition policy*. Part 1 is then preserved.
- **Several sprints.** By default (`CLAUDE.md` §8) there is a check-in with you at every sprint
  boundary. To let the team continue across boundaries without a new ruling each time, your words
  are recorded as an SA naming the sprints, the transition conditions (independent review and
  close-out done; no new scientific, scope or PI-reserved decision) and when to consult you. Every
  boundary still gets its close-out, independent review and checks. A continuation SA never covers
  what the charter reserves to you, such as closing a milestone or accepting a validation.
- **Project defaults.** "From now on, always …" about review depth, transition policy or planning
  cadence is a governing change. `/arpd-amend` applies it from your clear words, without asking you
  to approve them again. A this-time-only preference stays in the plan draft.

## 6. Hook permissions: what is logged, and why you are asked

Setup installs two things into `.claude/`:

- **`.claude/settings.json`**: hooks that run `tools/hooks/log_hook.py` on each Claude Code event.
- **`.claude/agents/`**: the implementer and reviewer roles the lead agent delegates to.

In install mode it also copies the `arpd-*` skills (setup, plan, check-in, amend) into the target
repository's `.claude/skills/`.

**What the logging records** (`logs/events.jsonl`, one line per event): the time; the event type (a
session started or ended, a prompt was submitted, a tool call finished, a subagent started or
stopped, a turn ended or failed, context was compacted, a notification); the session and subagent
IDs; the tool name, duration and outcome; the length of a prompt in characters; and, where Claude
Code supplies them, the session's start reason, the model, and an error type.

**What it never records:** prompt text (unless you set `ARPD_LOG_PROMPT_TEXT=1` for your own
project), tool inputs and outputs, file contents, and model reasoning. The full list is in
`docs/EVENTS.md` of your project.

**Why you are asked.** Claude Code asks for your approval before any write to `.claude/`, and before
any `git mv` into or out of it, because files there can run commands (hooks) and define agents.
Approve if you want event logging and delegation. Setup never works around this prompt. A scripted or
non-interactive run cannot approve it; the items are then recorded as owed (section 8).

## 7. Confirming that installation and logging worked

1. Run `python tools/check_governance.py`. The steps **"Event logging and agent roles installed"**
   and **"ARPD skills installed"** should be **PASS**. The skills step looks for
   `arpd-checkin`, `arpd-amend` and `arpd-plan`.
2. Start a Claude Code session in the project, do one small thing (for example, ask
   "Where are we?"), and end the turn.
3. Run `python tools/summarize_events.py --sessions`. The session table should show a row for that
   session, with its start and end times.

The checker looks at files only. Step 3 is what shows that the hooks actually fired.

## 8. When installation is incomplete

Anything setup could not write (usually the `.claude/` items) is recorded in three places:

- a decision in `DECISIONS.md`, titled "event logging not installed", "agent files not
  installed" or "skills not installed";
- `STATUS.md` §6 *Owed*;
- *Known gaps* in `START-HERE.md`, with the exact commands to finish. These copy, never move:
  `kit/settings/settings.json` to `.claude/settings.json`, `kit/agents/*.md` to `.claude/agents/`
  and, in install mode, the kit repository's `.claude/skills/arpd-*` (each folder whole, with its
  `references/`) to `.claude/skills/`. Only for an imported starter whose own `.claude/` files stayed
  behind are they `git mv` commands.

Until a decision records the gap, the checker reports it as MISSING; once recorded, as ADVISORY.
While `/arpd-plan` is owed, `START-HERE.md` still names planning as the next step and says to run the
commands first. After you run them, confirm as in section 7.

## 9. Resuming after a lost session

If a session ends unexpectedly (a crash, a lost connection, a context reset), start a new session in
the project and say:

> Start a new session on this project: follow the charter's recovery steps.

The new session becomes the lead. Following the charter (§9), it:

1. reads `STATUS.md` and notes the base commit it names;
2. runs `git log --oneline <base commit>..HEAD` and
   `python tools/summarize_events.py --since <the time STATUS.md was last rewritten> --sessions`, and
   **quotes their output**, never describing the history or the log from memory. If `logs/` is
   absent (a fresh clone or another machine), it says so and uses the last exported
   `reports/sprints/SPRINT-NN-events.jsonl`;
3. writes a `Recovered:` line at the top of `STATUS.md`, with that output;
4. logs a `resume` event.

Unfinished work from the lost session is treated as unreviewed.

**If setup itself was interrupted**, run the same `/arpd-setup` command again and say the earlier
session was lost. The new session checks `git log`, `git status`, the working notes in
`docs/discovery/SETUP.md`, any move-only commits, and the commit
"Record adoption ruling R-NN (setup in progress)". Then:

- **Before you adopted the report** (no adoption ruling): nothing generated is authorized. If the
  working notes exist, it shows you what they gathered (the phase reached, the topics, your words,
  the open questions) and continues from the next open topic, without re-asking settled ones. A
  draft report that exists is shown again as the draft it is, not rewritten from scratch. Nothing in
  the notes or the draft counts as adopted: you adopt a version of the report. Without notes,
  earlier answers count only if you confirm them. Committed moves are kept, not repeated. In install
  mode without consent, the notes are outside the repository, and the new session needs their path
  from you.
- **After you adopted it:** your ruling and the report version it names are the authority. Setup
  continues from the first missing file, without repeating moves, renumbering IDs or rewriting
  completed work.
- **Notes from an earlier kit version** are read the same way. An "Interview mode" line is ignored
  and marked "(obsolete; ignored)"; you are not asked to choose a mode. The old phases map to the new
  ones: Intake and Research & Problem to Project; Product & Engineering to Requirements and
  Architecture; Governance & Handoff to Team & Governance, then Definition Report.

**If a plan draft was interrupted**, run `/arpd-plan` (or `/arpd-plan resume`). A file in
`reports/planning/` without an "Approved by R-NN" marker is shown to you as a draft, **not
approved**, with its version and open points, and the review continues from the last committed
version. An approved plan that has not started stays approved; it is never treated as a start. To
start it, send the prompt `START-HERE.md` gives.

## 10. The import baseline report

When you import or install into existing code, setup runs the project's own tests (and its
governance check, if it has one) before changing anything. After you adopt the report, it records
the results **verbatim** in `reports/IMPORT-BASELINE-<date>.md`: the source and commit, each command with its working directory,
exit code and output, the test counts, and what was not run, and why. It is written once and then
frozen. Failures are recorded as they are.

It is informative evidence, not a governing document. The import decision in `DECISIONS.md` cites it,
and so does the first sprint's Part 1 when that sprint starts. Neither copies it. Later test runs go
in sprint records.

## 11. Reading the governance check

`python tools/check_governance.py` prints one line per step, a *Not checked* block, and an overall
result.

| Status | Meaning |
|---|---|
| **PASS** | The step's checks found nothing wrong in what is recorded |
| **FAIL** | Something recorded breaks a rule (for example, a consequential decision adopted without the authority its route requires) |
| **MISSING** | The step could not check something (a file or a date is missing, or a date is not in ISO 8601) |
| **PENDING** | Something awaits your decision (for example, the charter is not yet adopted) |
| **ADVISORY** | A note that does not change the result (for example, a gap recorded as owed) |

Overall: **FAIL** if any step failed; otherwise **INCOMPLETE** if any step is MISSING or PENDING;
otherwise **PASS**.

- **No sprint yet is fine.** A project with setup adopted and no sprint record passes the sprint
  step: planning pending is a valid state.
- **Open sprints.** The step "Open sprints: plan approval and execution authority cited" checks only
  the Part 1 rows *Approved plan*, *Execution authorized by* and *Transition policy*: each ruling or
  SA they cite must exist and must not be pending, and the plan file and version must exist. Older
  records without these rows get an ADVISORY ("older format"), never a FAIL. Decision tracking is
  still checked only in closed sprint records.

Within the steps it lists, the checker does not report PASS for an item it could not check. It
checks what is **recorded**: it cannot show that a recorded date is true, that a ruling, plan
approval or start direction is in your own words, or that the readiness block is right beyond its
Execution line; and it does not run the project's tests. Run those separately with the project's
test command, `python -m pytest --ignore=kit --ignore=examples --ignore=evaluation`, which leaves out
the kit's own tests, the worked example and the evaluation materials. The *Not checked* block lists
these limits for each run; `docs/LIMITATIONS.md` in the kit lists them in full.
