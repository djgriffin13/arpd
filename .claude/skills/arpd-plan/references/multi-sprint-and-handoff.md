# Multi-sprint transitions, records and handoff

Detail for Steps B, F and G of `/arpd-plan`. Record formats are in `arpd/templates/DECISIONS.md` and
`arpd/templates/reports/SPRINT.md`; the templates win.

## 1. Never merged

Plan approval, execution authorization and task-plan approval are separate (`arpd/docs/INTERACTION.md`
§1, kinds 4 and 5; task plans under `CLAUDE.md` §5). A multi-sprint plan can be approved without
authorizing anything beyond its first sprint.

## 2. Transition policies (Step B)

Ask once per planning effort, after the PI chooses several sprints:

```text
────────────────────────────────
CHOICE FOR YOU (select one)
How should the team move from one sprint to the next?
A. Check in with me and get my approval before each next sprint.
B. A light check-in with me at the boundaries we agree (for example, after S03); continue at the
   others after independent review and close-out.
C. Continue after independent review and close-out at every boundary, unless a new scientific,
   scope or PI-reserved decision comes up. (Needs your explicit authorization when we start.)
────────────────────────────────
```

Above the block, say:

- every sprint still gets its close-out record, independent review and tests, whichever is chosen;
- the charter's default (`CLAUDE.md` §8) is a check-in at every sprint boundary, so A changes
  nothing, and B or C take effect only through the PI's words when execution is authorized;
- if an SA in force already authorizes consecutive sprints, show it as "(recommended)".

At a **light check-in**, the lead gives a short check-in (as `/arpd-checkin` does) and waits for the
PI's go-ahead. It is not a re-approval of the plan. Silence is not a go-ahead.

The answer goes into the draft as the proposed *Transition policy*. It is planning input, not
authority. If the PI says it should be the **project default** ("from now on, always …"), that is a
governing change: record it through `/arpd-amend` (charter §8 cadence, or an SA), and change
nothing else.

## 3. Records (Steps F and G)

The formats are in `arpd/templates/DECISIONS.md`: the plan-approval ruling, the general ruling (for
an execution start), and the continuation SA. Log each: `python arpd/tools/log_event.py ruling --actor lead --ref R-NN`
(or `SA-NN`). What the formats leave to you:

- **Plan approval.** *Scope of approval* says what the PI's words approve: the plan only ("planning
  only"), the plan and S0N's execution, or the plan and the series' execution. When the words say
  nothing about starting, write "planning only" and "Execution authorized: no". A plain assent to
  the APPROVAL REQUIRED block is recorded with the block's text as read back: "(read back by the
  lead; PI assented: '<the PI's exact words>')".
- **Execution.** A start given in a later message is its own R-NN ("execution of S0N (PLAN-… vN)"),
  whose *Reading* names the plan, its approval ruling and the transition policy, and whose *Changes*
  names the sprint record. The approval ruling is never edited to show the later start.
- **The now-or-later block** is a `CHOICE FOR YOU` that **says it is an authorization**
  (`arpd/docs/INTERACTION.md` §2): the start option states what it authorizes (one sprint, or the
  series and its transition conditions) and which records it creates (R-NN, and SA-NN for a series).
  Without that statement a letter reply authorizes nothing; ask again. For a series under policy B
  or C, offer a first-sprint-only option alongside one like:

  ```text
  A. Now: start the series S04–S06 under PLAN-2026-10-20 v3. Choosing A authorizes S04 now, and
     S05–S06 after each independent review and close-out under the plan's transition conditions;
     I will record your answer as ruling R-08 and standing authorization SA-03.
  ```

  A bare letter is recorded as `> "A"` with **Given:** "directly in session (read back by the lead;
  PI chose: 'A'): "<the option's full text, including its stated effect>""; a continuation SA the
  option created quotes the same choice and read-back.
- **Continuation SA,** only when the PI's words authorize moving past at least one boundary without
  a new ruling (policy B or C), under `/arpd-amend`'s add-versus-change rules: a first one adds
  ("Supersedes: none"); a change supersedes only that SA. *Consult the PI when* includes a failed
  transition condition, the agreed check-in boundaries (policy B), and a provisional scope change
  beyond what the plan lets the lead adjust. Never widen it beyond the PI's words. It never covers
  what `CLAUDE.md` §6 reserves to the PI (closing a milestone, accepting a validation, real data,
  sharing outside the project, amending governing documents); a series that reaches a milestone
  close pauses there for the PI's walkthrough.

## 4. Starting a sprint (Step G "now", and each later sprint in a series)

1. Confirm that an execution ruling or a continuation SA covers this sprint, and that the plan
   version is the approved one. If the file has since moved to a later, unapproved version, work
   from the approved version's commit (`git show <sha>:reports/planning/PLAN-….md`), or stop and
   ask the PI to approve the new version first.
2. Create `reports/sprints/` if it does not exist yet (setup does not create it). Copy
   `arpd/templates/reports/SPRINT.md` to `reports/sprints/SPRINT-NN.md`. Fill Part 1 from the
   approved plan: milestone, objective, target requirements, selected items, plans (the task plans
   expected per work package; numbers are claimed as each is written), exit, team and workspace,
   and the three rows:
   - `Approved plan | PLAN-YYYY-MM-DD vN, approved by R-NN`
   - `Execution authorized by | R-NN or SA-NN`
   - `Transition policy | PI check-in / light check-in at … / continue after review and close-out under SA-NN`

   In an imported project's first sprint, Part 1 also cites the inherited baseline,
   `reports/setup/IMPORT-BASELINE.md`; never re-record the baseline in the sprint record.
3. `Start`: the time from `date -u +%Y-%m-%dT%H:%MZ`, and the commit SHA Part 1 is written on.
4. Rewrite `STATUS.md`: Readiness `Execution: in progress (S0N)` and `Next step: check in`; §2
   Current sprint. Set the sprint's `MASTER_PLAN.md` §3 row to In progress.
   Rewrite `START-HERE.md`'s *Next step* section too: S0N is in progress, how to check in, and
   no start prompt (remove the old one). Correct any other sentence in it that states the old
   state (for example "nothing has been planned yet").
5. Commit Part 1 with STATUS (and, at the first sprint, `START-HERE.md`'s *Map* with "pending"
   removed from its `reports/sprints/` line); log
   `python arpd/tools/log_event.py sprint_start --actor lead --ref S0N --note "PLAN-… vN; R-NN"`.
6. **Part 1 is now preserved.** Later changes go in its scope-change log.
7. Work proceeds by the charter: `plans/NNN` per `CLAUDE.md` §5, an implementer and a reviewer who
   did not implement, tests, decision tracking, close-out (Part 2).

## 5. At each boundary in a series

1. Close the sprint: Part 2 in full, independent review, checks (`python arpd/tools/check_governance.py`
   and the project's tests, quoted), events exported, plan updates (2.8). Log `sprint_close`.
2. Run the dependency screen (`INTERACTION.md` §7) against the next sprint's provisional scope.
3. Check the transition: the policy in Part 1; the SA's conditions; whether the next sprint's scope
   is still within the approved plan and what the lead may adjust; any new scientific, scope or
   PI-reserved decision; any milestone close.
4. **If every condition holds** and no check-in is due, start the next sprint (§4), citing the SA.
   Its Part 1 names the same approved plan.
5. **Otherwise pause.** Write `STATUS.md` (`Next step: check in`) and `START-HERE.md`, and bring the
   PI a short check-in naming the unmet condition and the decision needed. Unrelated authorized work
   may continue.

## 6. Handoff "later"

- `STATUS.md` Readiness:
  - `Planning: approved (PLAN-YYYY-MM-DD, vN, R-NN)`
  - `Execution: not started`
  - `Next step: begin implementation`
- `START-HERE.md`: replace the old next step with the copyable prompt, and say that sending it is
  the start instruction. For example:

```text
/arpd-plan resume. Begin sprint S04 now under PLAN-2026-10-20 v3 (approved by R-07). Check in with me before S05.
```

  For a series under policy C, write the PI's continuation words into the prompt only if the PI
  chose them; otherwise give the first-sprint prompt and tell the PI how to add a continuation.
- Log `python arpd/tools/log_event.py handoff --actor lead --note "PLAN-… vN approved; execution later"`,
  commit, and stop. Do not start anything.

When the prompt arrives, `/arpd-plan` (Entry step 4) records the PI's words as the execution ruling
and starts the sprint (§4). If the plan was revised after approval, the prompt is stale: set
Readiness back to `Planning: draft (PLAN-…, vN)` and `Next step: review plan`, and replace the
prompt in `START-HERE.md`.

## 7. Handoff truth

`STATUS.md`, `START-HERE.md`, `DECISIONS.md` and the planning and sprint records must agree on
readiness and the next step. **Rewrite STATUS Readiness and START-HERE's next step together, in the same
commit, at every change:** a draft, an approval, a revision after approval, a start, a pause at a
boundary, and a close. The checker compares STATUS's Execution line with the sprint records; it
cannot read START-HERE, so this is yours to keep true. A passing checker does not mean "ready to execute". A project with an
adopted setup and no sprint plan is valid; its next step is `/arpd-plan`, not implementation.
