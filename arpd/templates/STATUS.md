# STATUS.md: right now, and how to pick up

**Governs only what is happening right now.** It never states priorities, milestones or requirement
states; it points to `MASTER_PLAN.md` and `REQUIREMENTS.md` for those (`CLAUDE.md` §2).

**One designated writer: the lead agent.** Other agents report changes to it and never edit this file.
The lead agent rewrites it after every meaningful operational change, at every handoff and at every
sprint boundary. Meaningful changes include work starting or stopping, a session ending, a blocker,
and a resource being assigned. Its history lives in git and in the sprint records.

It is written for a successor who starts with an empty context and nothing else to go on, possibly
after this session has died (`CLAUDE.md` §9). When this file and the repository disagree, the
repository wins.

**Last rewritten:** {{date and time in UTC, e.g. 2026-10-20T14:05Z}} by {{role, session}}. **Base
commit:** {{SHA of the last commit before this rewrite}}. This rewrite is committed after it, so it
cannot name its own commit.

**If you are recovering** (the session that wrote this is gone): run
`git log --oneline <base commit>..HEAD` and
`python arpd/tools/summarize_events.py --since <the Last rewritten time> --sessions`, and quote their
output in a `Recovered:` line at the top of this file (`CLAUDE.md` §9). Never describe the log from
memory. If `arpd/logs/` is absent (a fresh clone or another machine), say so, and use the last exported
`reports/sprints/SPRINT-NN-events.jsonl` (`--log <that file>`) with `git log`.

---

## Readiness

Four lines, each with one value, then the adopted setup report. Setup, planning and execution are
separate: a project can be set up with no sprint planned, and an approved plan does not start work
(`CLAUDE.md` §8). A passing governance check is not readiness to execute. `START-HERE.md` gives the
PI the same next step.

- **Setup:** {{in progress | adopted (R-NN)}}
- **Planning:** {{not started | draft (PLAN-YYYY-MM-DD, vN) | approved (PLAN-YYYY-MM-DD, vN, R-NN)}}
- **Execution:** {{not started | authorized (R-NN or SA-NN, scope) | in progress (S0N) | complete}}
- **Next step:** {{finish setup | run /arpd-plan | review plan | begin implementation | check in | amend}}
- **Adopted report:** `reports/setup/PROJECT-DEFINITION.md` v{{N}} (R-{{NN}}, commit {{SHA of the adoption-first commit}})

## 1. Read first

`CLAUDE.md` → `PARADIGM-SPEC.md` → this file → the current sprint record → the plans in flight.

## 2. Current sprint

Write "No sprint open" when none is.

- **Sprint:** S{{NN}}: {{objective}}. Record: `reports/sprints/SPRINT-{{NN}}.md`.
- **Target requirements:**
- **Progress:** what is done, with evidence; what remains.

## 3. In flight

| Work | Plan | Who | Branch / worktree | State | If that session is gone |
|---|---|---|---|---|---|

## 4. On deck

The next step from *Readiness*. If planning is pending, it is "run `/arpd-plan`". If a sprint is
planned and approved, name it and its plan (`reports/planning/PLAN-…`, version). List anything that
must happen before it starts.

## 5. Waiting on the PI

A short summary of the decisions ahead. The canonical list, with what each decision affects and what
can continue meanwhile, is `DECISIONS.md` *Waiting on the PI*; keep this table in step with it. Do not
decide these yourself. Deferred decisions stay listed, marked "deferred (R-NN)". The open pack is
`reports/DECISION-PACK-{{date, with -2, -3 ... for a second or later pack that day}}.md`.

| # | Decision | Affects | Needed by |
|---|---|---|---|

## 6. Owed

List checks not yet run, reports not yet received, messages sent without an acknowledgement, and
anything setup could not write (for example, `.claude/settings.json`, saying whether the PI declined
or Claude Code's permission prompt did not allow the write), with its commands.
Write "Nothing owed" only when nothing is.

## 7. Team, workspace and runtime resources

- **Team arrangement:** solo / lead with subagents / peers
- **Workspace arrangement:** shared checkout / worktrees
- **Model versions:**

| Agent or session | Role | Worktree or branch | Port(s) | Output and scratch directory | Other shared resources |
|---|---|---|---|---|---|

## 8. The PI's working style

Record the review depth (as SA-01), how the PI likes decisions brought, how often they want
check-ins, how much explanation helps them, and what to avoid.
