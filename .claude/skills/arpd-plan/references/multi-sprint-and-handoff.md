# Multi-sprint transitions, records and handoff

Detail for Steps B, F and G of `/arpd-plan`. Formats follow `kit/templates/DECISIONS.md` and
`kit/templates/reports/SPRINT.md`; if a template there differs, the template wins and this file is
out of date.

## 1. Three things that are never merged

| Thing | What it is | Recorded as |
|---|---|---|
| Plan approval | The PI approves an exact plan version as the scope of a sprint or series | R-NN in the plan-approval format |
| Execution authorization | The PI's direction to start: one sprint, or a series | R-NN (it may be the same ruling as the approval), plus an SA-NN for a series |
| Task-plan approval | A `plans/NNN` plan approved under `CLAUDE.md` §5 | The plan's own status; routine ones by the lead |

A multi-sprint plan can be approved without authorizing anything beyond its first sprint.

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

## 3. Record formats

### Plan approval (Step F)

The next R-NN under *Rulings* in `DECISIONS.md`:

```text
### R-NN, YYYY-MM-DD: approval of PLAN-YYYY-MM-DD vN
> "the PI's exact words"
- **Given:** directly in session
- **Approves:** reports/planning/PLAN-YYYY-MM-DD.md, vN, commit <sha>
- **Scope of approval:** planning only / S0N / series S0N–S0M
- **Execution authorized:** no / S0N / series under SA-NN
- **Reading:** the lead's reading, including any waiting decision that still blocks part of the plan
- **Changes:** reports/planning/PLAN-YYYY-MM-DD.md (status marker); MASTER_PLAN.md §3–4 rows
```

- *Scope of approval* says what the PI's words approve: the plan only ("planning only"), the plan
  and S0N's execution, or the plan and the series' execution.
- When the words say nothing about starting, write "planning only" and "Execution authorized: no".
- If the PI simply assents to the APPROVAL REQUIRED block, record the block's text as read back:
  "(read back by the lead; PI assented: '<the PI's exact words>')".

### Execution (Step G)

If the start comes in a later message, record it as its own R-NN:

```text
### R-NN, YYYY-MM-DD: execution of S0N (PLAN-YYYY-MM-DD vN)
> "the PI's exact words"
- **Given:** directly in session
- **Reading:** starts S0N under PLAN-YYYY-MM-DD vN, approved by R-MM; transition policy: …
- **Changes:** reports/sprints/SPRINT-0N.md (Part 1 cites this ruling)
```

The approval ruling is never edited to show the later start; the execution ruling cites it.

The now-or-later block is a `CHOICE FOR YOU` that **says it is an authorization**
(`kit/docs/INTERACTION.md` §2): the start option states what it authorizes (one sprint, or the
series and its transition conditions) and which records it creates (R-NN, and SA-NN for a series).
Without that statement a letter reply authorizes nothing; ask again. For a series under policy B
or C, offer a first-sprint-only option alongside one like:

```text
A. Now: start the series S04–S06 under PLAN-2026-10-20 v3. Choosing A authorizes S04 now, and
   S05–S06 after each independent review and close-out under the plan's transition conditions;
   I will record your answer as ruling R-08 and standing authorization SA-03.
```

A bare letter is recorded as:

```text
> "A"
- **Given:** directly in session (read back by the lead; PI chose: 'A'): "<the option's full text,
  including its stated effect>"
```

The continuation SA, if the option created one, quotes the same choice and read-back.

### Continuation across a series (SA)

Only when the PI's words authorize the team to move past at least one boundary without a new ruling
(policy B or C). Record it under *Standing authorizations*, following `/arpd-amend`'s add-versus-change
rules: a first continuation SA adds to those in force ("Supersedes: none"); a change to an earlier
continuation SA supersedes only that SA.

```text
### SA-NN, YYYY-MM-DD: execution of sprints S0N–S0M
> "the PI's exact words"
- **Given:** directly in session, or in ruling R-NN
- **Supersedes:** none / SA-KK
- **Scope:** sprints S0N–S0M of PLAN-YYYY-MM-DD vN, as approved by R-MM
- **Transition conditions:** independent review and close-out done; no new scientific, scope or
  PI-reserved decision; <the PI's own conditions, e.g. all known-answer tests pass>
- **Consult the PI when:** a transition condition fails; at the agreed check-in boundaries (policy
  B); a sprint's provisional scope must change beyond what the plan lets the lead adjust
- **In force until:** the close of S0M, or changed by the PI
```

Never widen it beyond the PI's words. It never covers what `CLAUDE.md` §6 reserves to the PI
(closing a milestone, accepting a validation, real data, sharing outside the project, amending
governing documents). A series that reaches a milestone close pauses there for the PI's walkthrough.

Log each ruling and SA: `python tools/log_event.py ruling --actor lead --ref R-NN` (or `SA-NN`).

## 4. Starting a sprint (Step G "now", and each later sprint in a series)

1. Confirm that an execution ruling or a continuation SA covers this sprint, and that the plan
   version is the approved one. If the file has since moved to a later, unapproved version, work
   from the approved version's commit (`git show <sha>:reports/planning/PLAN-….md`), or stop and
   ask the PI to approve the new version first.
2. Create `reports/sprints/` if it does not exist yet (setup does not create it). Copy
   `reports/templates/SPRINT.md` to `reports/sprints/SPRINT-NN.md`. Fill Part 1 from the
   approved plan: milestone, objective, target requirements, selected items, plans (the task plans
   expected per work package; numbers are claimed as each is written), exit, team and workspace,
   and the three rows:
   - `Approved plan | PLAN-YYYY-MM-DD vN, approved by R-NN`
   - `Execution authorized by | R-NN or SA-NN`
   - `Transition policy | PI check-in / light check-in at … / continue after review and close-out under SA-NN`

   In an imported project's first sprint, Part 1 also cites the inherited baseline,
   `reports/IMPORT-BASELINE-YYYY-MM-DD.md`; never re-record the baseline in the sprint record.
3. `Start`: the time from `date -u +%Y-%m-%dT%H:%MZ`, and the commit SHA Part 1 is written on.
4. Rewrite `STATUS.md`: Readiness `Execution: in progress (S0N)` and `Next step: check in`; §2
   Current sprint. Set the sprint's `MASTER_PLAN.md` §3 row to In progress.
   Rewrite `START-HERE.md`'s next step too: S0N is in progress, how to check in, and no start
   prompt (remove the old one).
5. Commit Part 1 with STATUS (and, at the first sprint, `INDEX.md` with "pending" removed from its
   `reports/sprints/` row); log
   `python tools/log_event.py sprint_start --actor lead --ref S0N --note "PLAN-… vN; R-NN"`.
6. **Part 1 is now preserved.** Later changes go in its scope-change log.
7. Work proceeds by the charter: `plans/NNN` per `CLAUDE.md` §5, an implementer and a reviewer who
   did not implement, tests, decision tracking, close-out (Part 2).

## 5. At each boundary in a series

1. Close the sprint: Part 2 in full, independent review, checks (`python tools/check_governance.py`
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
- Log `python tools/log_event.py handoff --actor lead --note "PLAN-… vN approved; execution later"`,
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
