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

**It starts with your project.** After a quick look at the folder, the first question is what you
would like to build: an overview of the tool, who would use it, and what you imagine it doing. A
rough idea, a detailed specification or a pointer to existing documents or code are all fine. There
is no questionnaire about your background or research maturity first.

**Five visible phases.** A progress line at the top of each turn shows where you are:

```
SETUP  ● Project → ○ Requirements → ○ Architecture → ○ Team & Governance → ○ Definition Report
```

Under it is a short list of the topics still to understand in the current phase. The list changes as
you answer; one answer can close several topics. Expect **about 20–60 minutes**, depending on how
complex the project is.

- **Project:** what you want to build and what already exists. If a theory or model should inform the
  tool, you choose how the team treats it: use it to guide implementation without evaluating it,
  identify concerns, help develop it, or leave theory aside. For a tool that only collects data, the
  question is skipped.
- **Requirements:** after your overview, three scope questions, each asked once: the **minimum
  usable version**; the **ideal version**, naming the features you are interested in; and
  **nice-to-have** features you do not expect in the first release. Then workflows, data, and how
  well it must work. Each requirement gets acceptance criteria: how anyone could check it was met.
- **Architecture:** for each material choice (for example, desktop app, browser app, or an existing
  survey tool), the agent explains the credible alternatives and their trade-offs, then recommends
  one. You are not asked to choose a technology cold.
- **Team & Governance:** how the agents are arranged, how much they decide on their own, review
  and check-ins, and the open decisions, each with the point by which it must be settled.
- **Definition Report:** the agent writes `reports/PROJECT-DEFINITION.md` and checks it for gaps.

**One question at a time.** Each turn ends with one labelled block: `QUESTION FOR YOU`,
`CHOICE FOR YOU` or `APPROVAL REQUIRED`. Nothing comes after it. For a choice, every option is
printed in the text (A., B., …) before any pop-up widget, so you can always answer by letter. The
agent explains a concept when a decision depends on it, at your level, without narrating the process.

**Working notes are saved as you go**, in `docs/discovery/SETUP.md`. They are **not governing**: they
record what you said so that an interrupted setup can resume, and nothing in them is adopted. If you
install into your own repository, setup asks your consent before saving them there. Notes never hold
secrets or participant data, and are never pushed without your say-so.

**You adopt the Project Definition Report.** It is the full specification: overview and scope,
numbered requirements with acceptance criteria, architecture and the alternatives considered, data
and interface contracts, verification, a roadmap, the team, governance, and open decisions with
their gates. Each item is marked Adopted-on-adoption, Proposed, Provisional, Delegated, Open or
Excluded. Revise it as often as you like. Only when you adopt a version, in your own words, under
`APPROVAL REQUIRED`, is anything governing written; your words are recorded verbatim as ruling R-01,
citing the report's version. Adoption authorizes the governing documents only, not any
implementation.

**Data semantics stay yours.** What a blank answer means, missing versus zero, duplicates and
repeated submissions, what an identifier means, aggregation, precision: agents choose how to
implement these, never what they mean, unless you name a policy.

You also choose an **authority profile**: how much the team decides on its own (consult first,
bounded autonomy, or exploratory autonomy). You can change it at any time.

Near the end, Claude Code asks you to approve two writes into `.claude/`: the event-logging hooks and
the implementer and reviewer roles. The hooks record when things happen (event types, times, tool
names), never what you typed or file contents. If they cannot be approved, setup records them as owed
in `STATUS.md` and `START-HERE.md`, with the commands to finish later.

**Setup ends with planning pending.** It never builds anything and writes no sprint. At the end you
have:

- `CLAUDE.md`: the team charter your agents follow;
- `PARADIGM-SPEC.md`: your purpose and, where relevant, your science, to the depth you chose;
- `REQUIREMENTS.md` (with each requirement's acceptance criteria), `ARCHITECTURE.md` (with its
  decisions), `MASTER_PLAN.md` (a broad roadmap), `DECISIONS.md`, `STATUS.md`: the plan and the
  record;
- `reports/PROJECT-DEFINITION.md`: the report you adopted, kept as the record;
- `START-HERE.md`: your next step, which is `/arpd-plan`.

The last question is a choice: plan the first sprint now, or finish and plan later with `/arpd-plan`.

## B. Plan a sprint

```
/arpd-plan
```

It works in a new session, after setup or between sprints. It reads the project's records (including
each requirement's acceptance criteria, the architecture decisions and the open decisions' gates),
so you do not repeat yourself. Its progress line is
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

`examples/march-1991/` is a complete ARPD project with v0.3-format records (its ruling R-01 was
given for v0.3.0-rc.1, and the records are carried unchanged): a checked implementation of March's
(1991) organizational-learning model, with its charter, specification, sprint records, decisions and
evidence. Because of the older format, the governance check reports some steps as "older format" and
does not compare them. To extend it, run `/arpd-setup import examples/march-1991` from the kit's
root, then `/arpd-plan`.

```bash
pip install -r examples/march-1991/requirements.txt
cd examples/march-1991
python -m pytest -m "not slow"
python tools/check_governance.py
```

## Words that are easy to mix up

Your project's `START-HERE.md` explains, one line each, how an **invariant** (`PARADIGM-SPEC.md`), a
**requirement** (`REQUIREMENTS.md`) and an **acceptance criterion** (its *Requirement details*)
differ.

There are three levels of plan:

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
| Get an explanation | Ask. The agent explains at your level when a decision depends on it. |
| Check the governance records | `python tools/check_governance.py` (statuses: [OPERATIONS §11](docs/OPERATIONS.md#11-reading-the-governance-check)) |
| See time and activity | `python tools/summarize_events.py` (add `--sessions` for one row per session) |
| Resume after a lost session | Start a new session and say: "Start a new session on this project: follow the charter's recovery steps." ([OPERATIONS §9](docs/OPERATIONS.md#9-resuming-after-a-lost-session)) |
