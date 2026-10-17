# Quick start

Details for every step are in [docs/OPERATIONS.md](docs/OPERATIONS.md).

## You need

- **Claude Code** (tested with 2.1.220).
- **Git.**
- **Python 3.8 or later**, on the PATH as `python` (`python --version`). The event-logging hooks call
  it.
- For the March example only: numpy and pytest
  (`pip install -r examples/march-1991/requirements.txt`).

## A. Set up a new research-instrument project

```bash
git clone <this repository> my-project
cd my-project
claude
```

Opening this folder in Claude Code makes the skills in `.claude/skills/` available. Type:

```
/arpd-setup
```

**First, choose how you want to work.** Setup asks once, with no default:

- **Standard interview:** questions only, with short explanations when needed.
- **Guided tutorial:** the same questions, with a short explanation of each step the first time it
  comes up.

You can say "tutorial on" or "tutorial off" at any time. Nothing restarts, no answer is lost, and
nothing changes in what needs your approval.

**Four visible phases.** A progress line at the top of each turn shows where you are:

```
SETUP  ✓ Intake → ● Research & Problem → ○ Product & Engineering → ○ Governance & Handoff
```

Under it is a short list of the topics still to understand in the current phase. The list changes as
you answer; one answer can close several topics. Expect **30–60 minutes**, depending on how much
help with the science you ask for.

**One question at a time.** Each turn ends with one labelled block: `QUESTION FOR YOU`,
`CHOICE FOR YOU` or `APPROVAL REQUIRED`. Nothing comes after it. For a choice, every option is
printed in the text (A., B., …) before any pop-up widget, so you can always answer by letter. After a
few questions in a phase, the agent sums up what it heard and asks whether to add more or move on.

**You talk about purpose and science; the agent proposes the engineering.** It first asks what you
want to investigate or accomplish, and separately what you want built. It hears your full vision
before narrowing to a first useful version. How much science it covers depends on what you ask for:
if you only want a tool built, it does not take you through constructs, invariants or causal claims
you did not ask for.

**Working notes are saved as you go**, in `docs/discovery/SETUP.md`. They are **not governing**: they
record what you said so that an interrupted setup can resume, and nothing in them is adopted. If you
install into your own repository, setup asks your consent before saving them there. Notes never hold
secrets or participant data, and are never pushed without your say-so.

**Answering is not authorizing.** Your answers inform the agent; they decide nothing. Near the end,
the agent reads back a plain-language summary under `APPROVAL REQUIRED`. Only when you adopt it, in
your own words, is anything governing written. Your words are recorded verbatim as a ruling.

You also choose an **authority profile**: how much the team decides on its own (consult first,
bounded autonomy, or exploratory autonomy). You can change it at any time.

Near the end, Claude Code asks you to approve two writes into `.claude/`: the event-logging hooks and
the implementer and reviewer roles. The hooks record when things happen (event types, times, tool
names), never what you typed or file contents. If they cannot be approved, setup records them as owed
in `STATUS.md` and `START-HERE.md`, with the commands to finish later.

**Setup ends with planning pending.** It never builds anything and writes no sprint. At the end you
have:

- `CLAUDE.md`: the team charter your agents follow;
- `PARADIGM-SPEC.md`: your science, to the depth you chose;
- `REQUIREMENTS.md`, `MASTER_PLAN.md` (a broad roadmap), `DECISIONS.md`, `STATUS.md`: the plan and
  the record;
- `START-HERE.md`: your next step, which is `/arpd-plan`.

The last question is a choice: plan the first sprint now, or finish and plan later with `/arpd-plan`.

## B. Plan a sprint

```
/arpd-plan
```

It works in a new session, after setup or between sprints. It reads the project's records, so you do
not repeat yourself. Its progress line is
`PLAN  ✓ Review → ● Priorities → ○ Draft → ○ Approval → ○ Handoff`.

1. **Review.** A short read-back of where the project stands, with the governance check's result.
2. **One sprint or several.** You choose. For several, you also choose how the team moves from one
   sprint to the next: your approval each time, a light check-in at agreed points, or continuing
   after independent review and close-out. Every sprint still gets review, tests and a close-out.
3. **Priorities.** The agent proposes a focus; you correct it.
4. **Draft.** A plan file in `reports/planning/PLAN-<date>.md`, marked DRAFT, with a version (v1).
   It decides nothing.
5. **Review and revise.** Edit it, challenge it, or have another agent review it. Each revision is a
   new version.
6. **Approval.** You approve a **specific version** (`APPROVAL REQUIRED`). Approving a plan does
   **not** start work.
7. **Begin now or later.** "Now" starts the first sprint: its record,
   `reports/sprints/SPRINT-NN.md`, is written from the approved plan. "Later" puts the exact start
   prompt in `START-HERE.md`; sending it is your start instruction.

A small project can do all of this in four or five exchanges.

## C. Bring in existing code

- **Copy a codebase into this repository:** `/arpd-setup import <path or git URL>`
- **Install ARPD into your own existing repository:** `/arpd-setup install <path>`. This also copies
  the skills and the `kit/` folder into that repository.

Existing work and instruction files are preserved. Any conflict with the charter is brought to you as
a decision, never merged silently. The imported project's test results before any change are kept in
`reports/IMPORT-BASELINE-<date>.md`.

## D. Confirm it worked

1. `python tools/check_governance.py`: the steps "Event logging and agent roles installed" and
   "ARPD skills installed" (check-in, amend and plan) should be **PASS**. Anything still owed is
   listed in `STATUS.md` §6 and in *Known gaps* in `START-HERE.md`. A project with setup done and no
   sprint yet can pass: planning pending is a valid state.
2. Start a session, do one small thing, then run `python tools/summarize_events.py --sessions`: you
   should see a row for that session.

A passing check is not permission to start work. Where setup, planning and execution stand is in the
*Readiness* block at the top of `STATUS.md`.

## E. Look at the worked example first

`examples/march-1991/` is a complete ARPD project: a checked implementation of March's (1991)
organizational-learning model, with its charter, specification, sprint records, decisions and
evidence.

```bash
pip install -r examples/march-1991/requirements.txt
cd examples/march-1991
python -m pytest -m "not slow"
python tools/check_governance.py
```

## Words that are easy to mix up

| Term | What it says | Where it lives |
|---|---|---|
| **Invariant** (INV) | What must never break, or the results stop meaning what you intend. You own it, for the life of the project. | `PARADIGM-SPEC.md` §5 |
| **Requirement** (REQ) | What the instrument must do. It traces to a spec item or a ruling, and has a state and evidence. | `REQUIREMENTS.md` |
| **Acceptance criterion** | How one task plan proves it delivered. It closes with the plan; its evidence moves a requirement's state. | Inside the plan, `plans/NNN-…` |

There are also three levels of plan:

| Level | What it is | Where it lives |
|---|---|---|
| **Roadmap** | The objective, milestones and broad order of work. Milestones change only by your ruling. | `MASTER_PLAN.md` |
| **Sprint plan** | One sprint or a series. Drafted with `/arpd-plan`; you approve a version. At sprint start it becomes the sprint record's Part 1. | `reports/planning/PLAN-<date>.md`, then `reports/sprints/SPRINT-NN.md` |
| **Task plan** | One scoped piece of work inside a sprint. Routine ones are approved by the lead agent. | `plans/NNN-<slug>.md` |

## While you work

| You want to… | Do this |
|---|---|
| Plan the next sprint, or several | `/arpd-plan` |
| Start or continue work | Use the prompt in `START-HERE.md`. Work starts only from an approved plan and your start direction. |
| See where things stand, and what decisions are coming | `/arpd-checkin` |
| Decide something | Just say it. The lead agent records your words verbatim as a ruling. |
| Change the rules, the science spec, a project default, the milestones, or what the team may decide alone | `/arpd-amend`. A direct instruction is enough; you are not asked to approve your own words again. |
| Turn the guided tutorial on or off | Say "tutorial on" or "tutorial off". |
| Check the governance records | `python tools/check_governance.py` (statuses: [OPERATIONS §11](docs/OPERATIONS.md#11-reading-the-governance-check)) |
| See time and activity | `python tools/summarize_events.py` (add `--sessions` for one row per session) |
| Resume after a lost session | Start a new session and say: "Start a new session on this project: follow the charter's recovery steps." ([OPERATIONS §9](docs/OPERATIONS.md#9-resuming-after-a-lost-session)) |
