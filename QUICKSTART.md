# Quick start

Details for every step are in [docs/OPERATIONS.md](docs/OPERATIONS.md).

## You need

- **Claude Code** (tested with 2.1.220).
- **Git.**
- **Python 3.8 or later**, on the PATH as `python` (`python --version`). The event-logging hooks call
  it.
- For the March example only: numpy and pytest
  (`pip install -r examples/march-1991/requirements.txt`).

## A. Start a new research-instrument project

```bash
git clone <this repository> my-project
cd my-project
claude
```

Opening this folder in Claude Code makes the skills in `.claude/skills/` available. Type:

```
/arpd-setup
```

The interview takes about 30 minutes. You are asked about your **science**: your question,
constructs, what must never go wrong, and what would convince you it works. The agent proposes the
**engineering**, with reasons, and you confirm or correct. Nothing is written until you approve a
plain-language summary.

You also choose an **authority profile**: how much the team decides on its own (consult first,
bounded autonomy, or exploratory autonomy). You can change it at any time. **Your own words
authorize**; no fixed phrase is needed. The lead agent records them verbatim.

Near the end, Claude Code asks you to approve two writes into `.claude/`: the event-logging hooks and
the implementer and reviewer roles. The hooks record when things happen (event types, times, tool
names), never what you typed or file contents. Approve them if you want logging and delegation. If
they cannot be approved, setup records them as owed in `STATUS.md` and `START-HERE.md`, with the
commands to finish later.

At the end you have:

- `CLAUDE.md`: the team charter your agents follow;
- `PARADIGM-SPEC.md`: your science, in a form agents can't drift from;
- `REQUIREMENTS.md`, `MASTER_PLAN.md`, `DECISIONS.md`, `STATUS.md`: the plan and the record;
- `START-HERE.md`: the exact prompt to begin your first sprint.

## B. Bring in existing code

- **Copy a codebase into this repository:** `/arpd-setup import <path or git URL>`
- **Install ARPD into your own existing repository:** `/arpd-setup install <path>`. This also copies
  the skills and the `kit/` folder into that repository.

Existing work and instruction files are preserved. Any conflict with the charter is brought to you as
a decision, never merged silently.

## C. Confirm it worked

1. `python tools/check_governance.py`: the steps "Event logging and agent roles installed" and
   "Check-in and amend skills installed" should be **PASS**. Anything still owed is listed in `STATUS.md` §6 and in *Known gaps* in `START-HERE.md`.
2. Start a session, do one small thing, then run `python tools/summarize_events.py --sessions`: you
   should see a row for that session.

## D. Look at the worked example first

`examples/march-1991/` is a complete ARPD project: a checked implementation of March's (1991)
organizational-learning model, with its charter, specification, sprint records, decisions and
evidence.

```bash
pip install -r examples/march-1991/requirements.txt
cd examples/march-1991
python -m pytest -m "not slow"
python tools/check_governance.py
```

## While you work

| You want to… | Do this |
|---|---|
| Start or continue work | Use the prompt in `START-HERE.md`, or "Start the next sprint." |
| See where things stand | `/arpd-checkin` |
| Decide something | Just say it. The lead agent records your words verbatim as a ruling. |
| Change the rules, the science spec, or what the team may decide alone | `/arpd-amend` |
| Check the governance records | `python tools/check_governance.py` (statuses: [OPERATIONS §8](docs/OPERATIONS.md#8-reading-the-governance-check)) |
| See time and activity | `python tools/summarize_events.py` (add `--sessions` for one row per session) |
| Resume after a lost session | Start a new session and say: "Start a new session on this project: follow the charter's recovery steps." ([OPERATIONS §7](docs/OPERATIONS.md#7-resuming-after-a-lost-session)) |
