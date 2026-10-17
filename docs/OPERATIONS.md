# Operating ARPD: installation, logging, recovery and checks

This is the detail behind [QUICKSTART.md](../QUICKSTART.md). Commands are run from the project root.

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
| `/arpd-setup` | Fresh project: the interview, then the governing documents, tools and first sprint, in this repository |
| `/arpd-setup import <path or git URL>` | Brings existing code into this repository, and sets it up |
| `/arpd-setup install <path>` | Installs the charter, governing documents, tools, hooks and agents into your existing repository at `<path>`. It also copies the `arpd-*` skills and the `kit/` folder there, so check-ins and amendments work from that repository |
| `/arpd-checkin` | A plain-language check-in: what works, what needs you, what was decided without you |
| `/arpd-amend` | Records a ruling or a standing authorization verbatim, or amends the charter or the specification |

## 3. Your authority, and your words

- **Authority profile.** At setup you choose how much the team decides on its own: *consult first*
  (it asks before adopting any consequential scientific assumption), *bounded autonomy* (the
  default: it works within agreed boundaries and reports at checkpoints) or *exploratory autonomy*
  (it tries and compares alternatives, then brings you the decision to adopt). It is recorded as a
  standing authorization (SA-01) and you can change it at any time, in any message.
- **Your own words authorize.** No fixed phrase is needed. The lead agent records your words
  verbatim as a ruling (R-NN), with its reading on a separate line. A message relayed by another
  agent binds only once you confirm it yourself.

## 4. Hook permissions: what is logged, and why you are asked

Setup installs two things into `.claude/`:

- **`.claude/settings.json`**: hooks that run `tools/hooks/log_hook.py` on each Claude Code event.
- **`.claude/agents/`**: the implementer and reviewer roles the lead agent delegates to.

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
non-interactive run cannot approve it; the items are then recorded as owed (section 6).

## 5. Confirming that installation and logging worked

1. Run `python tools/check_governance.py`. The step **"Event logging and agent roles installed"**
   should be **PASS**.
2. Start a Claude Code session in the project, do one small thing (for example, ask
   "Where are we?"), and end the turn.
3. Run `python tools/summarize_events.py --sessions`. The session table should show a row for that
   session, with its start and end times.

The checker looks at files only. Step 3 is what shows that the hooks actually fired.

## 6. When installation is incomplete

Anything setup could not write (usually the two `.claude/` items) is recorded in three places:

- a decision in `DECISIONS.md`, titled "event logging not installed" or "agent files not
  installed";
- `STATUS.md` §6 *Owed*;
- *Known gaps* in `START-HERE.md`, with the exact commands to finish. For a fresh project these copy
  `kit/settings/settings.json` to `.claude/settings.json` and `kit/agents/*` to `.claude/agents/`; for
  an import they are `git mv` commands for the starter's `.claude/` files.

Until a decision records the gap, the checker reports it as MISSING; once recorded, as ADVISORY.
After you run the commands, confirm as in section 5.

## 7. Resuming after a lost session

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

## 8. Reading the governance check

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

Within the steps it lists, the checker does not report PASS for an item it could not check. It
checks what is **recorded**: it cannot show that a recorded date is true or that a ruling is in your
own words, it checks decision tracking only in closed sprint records, and it does not run the
project's tests. The *Not checked* block lists these limits for each run; `docs/LIMITATIONS.md` in
the kit lists them in full.
