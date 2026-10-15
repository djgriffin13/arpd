# STATUS.md: right now, and how to pick up

**Governs only what is happening right now.** It never states priorities, milestones or requirement
states; it points to `MASTER_PLAN.md` and `REQUIREMENTS.md` for those (`CLAUDE.md` §2).

The lead agent **rewrites** this file at every handoff and every sprint boundary. Its history lives in
git and in the sprint records.

It is written for a successor who starts with an empty context and nothing else to go on, possibly
after this session has died (`CLAUDE.md` §9). When this file and the repository disagree, the
repository wins.

**Last rewritten:** {{date, time}} by {{role, session}} at commit {{SHA}}

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

Do not decide these yourself. The open pack is `reports/DECISION-PACK-{{date}}.md`.

| # | Item | Blocks | Default if silent |
|---|---|---|---|

## 6. Owed

List checks not yet run, reports not yet received, and messages sent without an acknowledgement.

## 7. Team and workspace

- **Arrangement:**
- **Active sessions and roles:**
- **Model versions:**

## 8. The PI's working style

Record how the PI likes decisions brought, how often they want check-ins, and what to avoid.
