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
`python tools/summarize_events.py --since <the Last rewritten time> --sessions`, and quote their
output in a `Recovered:` line at the top of this file (`CLAUDE.md` §9). Never describe the log from
memory. If `logs/` is absent (a fresh clone or another machine), say so, and use the last exported
`reports/sprints/SPRINT-NN-events.jsonl` (`--log <that file>`) with `git log`.

---

## 1. Read first

`CLAUDE.md` → `PARADIGM-SPEC.md` → this file → the current sprint record → the plans in flight.

## 2. Current sprint

- **Sprint:** S{{NN}}: {{objective}}. Record: `reports/sprints/SPRINT-{{NN}}.md`.
- **Target requirements:**
- **Progress:** what is done, with evidence; what remains.

## 3. In flight

| Work | Plan | Who | Branch / worktree | State | If that session is gone |
|---|---|---|---|---|---|

## 4. On deck

The next sprint is S{{NN+1}}, as planned in `MASTER_PLAN.md` §3. List anything that must happen before
it starts.

## 5. Waiting on the PI

Do not decide these yourself. The open pack is `reports/DECISION-PACK-{{date, with -2, -3 ... for a second or later pack that day}}.md`.

| # | Decision requested | Blocks | Recommendation (not adopted until decided) |
|---|---|---|---|

## 6. Owed

List checks not yet run, reports not yet received, and messages sent without an acknowledgement.

## 7. Team, workspace and runtime resources

- **Team arrangement:** solo / lead with subagents / peers
- **Workspace arrangement:** shared checkout / worktrees
- **Model versions:**

| Agent or session | Role | Worktree or branch | Port(s) | Output and scratch directory | Other shared resources |
|---|---|---|---|---|---|

## 8. The PI's working style

Record how the PI likes decisions brought, how often they want check-ins, and what to avoid.
