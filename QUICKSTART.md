# Quick start

**You need:**

- Claude Code;
- Git;
- Python 3.8 or later (`python --version`).

No other installation is needed for the kit itself.

## A. Start a new research-instrument project

```bash
git clone <this repository> my-project
cd my-project
claude
```

Then type:

```
/arpd-setup
```

The interview takes about 30 minutes. You will be asked about your **science**: your question,
constructs, what must never go wrong, and what would convince you it works. The agent proposes the
**engineering**, with reasons, and you confirm or correct. Nothing is written until you approve a
plain-language summary.

At the end you have:

- `CLAUDE.md`: the team charter your agents follow;
- `PARADIGM-SPEC.md`: your science, in a form agents can't drift from;
- `REQUIREMENTS.md`, `MASTER_PLAN.md`, `DECISIONS.md`, `STATUS.md`: the plan and the record;
- `START-HERE.md`: the exact prompt to begin your first sprint.

## B. Bring in existing code

- **Copy a codebase into this repository:** `/arpd-setup import <path or git URL>`
- **Install ARPD into your own existing repository:** `/arpd-setup install <path>`

Existing work and instruction files are preserved. Any conflict with the charter is brought to you as
a decision, never merged silently.

## C. Look at the worked example first

`examples/march-1991/` is a complete ARPD project: a checked implementation of March's (1991)
organizational-learning model, with its charter, specification, sprint records, decisions and
evidence. Run its checks:

```bash
cd examples/march-1991
python -m pytest -m "not slow"
```

## While you work

| You want to… | Do this |
|---|---|
| Start or continue work | Use the prompt in `START-HERE.md`, or "Start the next sprint." |
| See where things stand | `/arpd-checkin` |
| Decide something | Just say it. The lead agent records your words verbatim as a ruling. |
| Change the rules or the science spec | `/arpd-amend` |
| Check the governance | `python tools/check_governance.py` |
| See time and activity | `python tools/summarize_events.py` |
