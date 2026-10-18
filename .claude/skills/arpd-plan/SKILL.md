---
name: arpd-plan
description: Plan the next sprint, or a series of sprints, for an ARPD project with the PI. Reviews where the project stands, agrees priorities, drafts a versioned plan in reports/planning/, gets the PI's approval of an exact version, and asks whether to begin implementation now or later. Use when the PI types /arpd-plan, or asks to "plan the next sprint", "plan sprints", re-plan, or resume a planning review.
argument-hint: "[one | multiple | resume]"
---

# ARPD sprint planning

You run the planning conversation for the PI. You turn the approved project goals into one or more
sprint plans, get the PI's approval of an exact version, and hand off to execution now or later.

**Planning is not implementation.** Never write project code, tests or `plans/NNN` task plans while
planning. Work starts only in Step G, under an execution authorization.

Three levels of plan, never merged:

| Level | Record | Changed by |
|---|---|---|
| Roadmap: objective, milestones, order of work | `MASTER_PLAN.md` | The lead for sprint rows; milestone changes only by ruling, through `/arpd-amend` |
| Sprint plan: one sprint or a series | this skill → `reports/planning/PLAN-…md` → `reports/sprints/SPRINT-NN.md` Part 1 at start | The PI approves the plan; the lead materializes it |
| Task plan: one scoped piece of work | `plans/NNN-slug.md` (`CLAUDE.md` §5) | Its owner; routine ones approved by the lead |

Approving a sprint plan is a planning gate for the sprint as a package. It does not make every task
plan or technical edit need the PI.

**Every turn that waits for the PI** (`kit/docs/INTERACTION.md` §2–§4, in short):

- Start with the progress line `PLAN  ✓ Review → ● Priorities → ○ Draft → ○ Approval → ○ Handoff`
  (two spaces after `PLAN`; ✓ done, ● current, ○ to come; keep every arrow).
- End with exactly one labelled block, written as plain text, never inside a code fence.
  **Nothing follows its closing divider**: not even a sentence about other options. Offers such as
  "you can also edit it or ask for a review" go inside the block or above it.
- A closing turn that does not wait for the PI ends with the next step and its exact prompt, and no
  block.

Read before you start:

- `kit/docs/INTERACTION.md`: the labelled blocks, choices printed before any widget, the progress
  line, explaining when needed, the dependency screen. Follow it on every turn that waits for the PI.
- `references/planning-guide.md` (this folder): the read-back, sizing, the draft's content,
  versions, review, the dependency screen.
- `references/multi-sprint-and-handoff.md` (this folder): transition policies, the ruling and SA
  formats, sprint start, the boundary procedure, the start prompt.

## Entry

1. **Is setup adopted?** `CLAUDE.md`'s Version line must name an adoption ruling (R-NN) that exists
   in `DECISIONS.md`. If `CLAUDE.md` is the kit's "not yet set up" file, or the ruling is missing,
   say so plainly and offer `/arpd-setup`. Never plan execution against an unadopted charter.
2. **Read, in this order:** `CLAUDE.md` and the standing authorizations in `DECISIONS.md`;
   `PARADIGM-SPEC.md` if the work touches the science; `REQUIREMENTS.md`, including *Requirement
   details* (acceptance criteria, priority, dependencies); `MASTER_PLAN.md`; `ARCHITECTURE.md`,
   including *Architecture decisions* (note which are Provisional or Delegated); `DECISIONS.md`
   *Waiting on the PI*, with each row's gate (*Needed by*); `STATUS.md` (Readiness, §5, §6, §8); the
   current or last sprint record and its evidence; existing `plans/` and open decision packs;
   `START-HERE.md` (orientation only); the adopted `reports/PROJECT-DEFINITION.md` and notes in
   `reports/planning/` and `docs/discovery/` (context only, never authority: where they differ from
   a governing document, the governing document wins). Do not re-ask a preference that is already
   recorded, and never re-ask scope: the minimum usable version, the ideal version and the
   nice-to-haves come from the adopted report and the requirement priorities.
3. **A draft in progress?** A `reports/planning/PLAN-*.md` is approved only if its current Version
   line is the version an existing approval ruling names (*Approves:* line). Otherwise it is a
   draft: show its file and Version, say plainly that this version is **not approved** (naming any
   earlier version that was, and its ruling), list its open points, and offer to continue it
   (Step E). Log
   `python tools/log_event.py resume --actor lead --ref PLAN-… --note "planning resumed"`.
4. **An approved plan not yet started?** Do not re-plan it by default. If the PI's message gives the
   start (the prompt left in `START-HERE.md`), record it as the execution ruling and go to Step G
   "now". Otherwise offer to start it or to revise it (a new version needs a new approval).
5. **An open sprint?** (a `SPRINT-NN.md` with Part 1 and no Part 2 *Closed* line.) Never renumber it
   or edit its Part 1. Offer:

```text
────────────────────────────────
CHOICE FOR YOU (select one)
Sprint S03 is still open. What would you like to plan?
A. The sprint after S03 (S04), while S03 continues.
B. A change to S03's scope, recorded in its scope-change log.
C. Close S03 first, then plan the next sprint.
────────────────────────────────
```

The argument `one` or `multiple` answers Step B in advance and nothing else: Steps A and C
(the read-back and the priorities question) still run before any draft. `resume` goes to 3 or 4.

## The conversation

Show `PLAN  ✓ Review → ● Priorities → ○ Draft → ○ Approval → ○ Handoff` above the block on every
turn that waits for the PI (✓ done, ● current, ○ to come). Add the topic list (priorities, scope,
dependencies, review level, exit evidence) when it helps.

**Explain when needed** (`INTERACTION.md` §6), at the PI's level; there is no mode to ask about. An
interview mode recorded by an earlier kit version (`STATUS.md` §8 or the notes) is ignored: say so
once, and change nothing else.

**Small projects stay small.** For a short utility, Steps A–C can be one read-back and one
question, the plan one page, and the whole run four or five exchanges.

### Step A: Review

Give a short, factual read-back: what was last completed, what demonstrably works (with evidence;
never claim a test ran unless you ran it now or a record shows it), the roadmap, what is blocked,
and the next thrust you recommend. Run `python tools/check_governance.py` and quote its OVERALL
line.

Use the inherited review and autonomy preferences. Ask only whether the PI wants an override for
this planning effort: light or thorough critique, how much brainstorming, an outside review. A
this-time-only preference goes in the draft (non-governing). A new **project default** (review
depth, transition policy, planning cadence) is a governing change: say what it would change, and
record it through `/arpd-amend` from the PI's clear words.

### Step B: One sprint or several

Always ask, explicitly:

```text
────────────────────────────────
CHOICE FOR YOU (select one)
Would you like to plan the next sprint only, or map out several sprints as one coordinated effort?
A. The next sprint only.
B. Several sprints as one coordinated effort.
────────────────────────────────
```

For a complex project, say above the block why several may help (shared dependencies). An approved
project default is shown as "(recommended)", never applied silently.

If several, ask **once** per planning effort how transitions should work (A. PI approval between
sprints; B. a light check-in at agreed boundaries; C. continue after independent review and
close-out, where the PI explicitly authorizes it). Say above it that **every sprint still gets review,
tests and close-out**, whatever is chosen. The answer is planning input. Inherited cadence (`CLAUDE.md`
§8) and SAs in force are never widened by it: continuation becomes authority only by the PI's words
in Step F or G.

### Step C: Priorities

Present: the recommended thrust and the milestone it serves, the intended deliverables, options
and trade-offs, blockers and dependencies, and what you would defer. Then one open question:

```text
────────────────────────────────
QUESTION FOR YOU
Do these priorities match yours? What would you change, and is there anything else we should
consider before I draft the plan?
────────────────────────────────
```

In a complex project, keep a short topic list and follow up until the scope is clear. Use the
question fuse.

### Step D: Draft

Write `reports/planning/PLAN-YYYY-MM-DD.md` (`-2`, `-3` for a later effort the same day) from
`kit/templates/planning/PLAN.md`: minimal but sufficient, the first sprint precise, later sprints
labelled provisional with what may change them (`references/planning-guide.md`). Mark it DRAFT,
`Version: v1`.

**Dependency screen.** For every unresolved decision the plan relies on, add or update its row in
`DECISIONS.md` *Waiting on the PI*: *Affects*, *Needed by*, *Can continue meanwhile*. That table is
canonical; the plan cites the row and does not restate it. Only the dependent work is blocked.
Respect each row's gate: one needed "before planning" is put to the PI before approval (or deferred
by ruling); one needed "before implementing X" is scheduled to be decided before the work package
for X; one needed "before deployment" blocks only release work.
Refresh `STATUS.md` §5's summary and set Readiness `Planning: draft (PLAN-…, v1)`, `Next step:
review plan`.

Commit: `Plan draft PLAN-YYYY-MM-DD v1 (not approved)`. Summarize the plan in chat in one screen;
the detail stays in the file.

### Step E: Review and revise

Tell the PI the draft is theirs to examine: they may edit it, challenge priorities, ask for
re-planning, or send it to an independent agent. Offer an outside review; never require one for a
small plan. Each revision bumps the Version (v2, v3), lists what changed, and is committed with the
same message pattern. No governing file changes during review.

### Step F: Approval

When the PI is satisfied:

```text
────────────────────────────────
APPROVAL REQUIRED
Approve reports/planning/PLAN-2026-10-20.md v3 (commit abc1234)?
A yes approves this plan as the scope of S04 (planning only). It does not start work; I will ask
next whether to begin now or later. Waiting decisions affecting it: DECISIONS Waiting #2 (blocks
WP3 only).
────────────────────────────────
```

Name what a yes covers: planning only, S0N's execution, or a series. Record the PI's words verbatim
as the next R-NN, in the plan-approval format (`references/multi-sprint-and-handoff.md`). When the
PI does not clearly say more, record **planning approval only**. Clear words need no second
confirmation; ask once only if they could mean materially different things. A bare "yes" is
recorded with the block's text as read back: "(read back by the lead; PI assented: '<words>')".
Then set the plan's status marker as its template says ("Approved by R-NN (vN, commit …)"; the
approved version's text is never edited), set its `MASTER_PLAN.md` §3 rows to "planned (PLAN-… vN, R-NN)" and §4 items to
Selected (milestone changes go to `/arpd-amend`),
set Readiness `Planning: approved (PLAN-…, vN, R-NN)`, run the checker, log
`python tools/log_event.py ruling --actor lead --ref R-NN --note "approval of PLAN-… vN"`, and commit
naming R-NN. If not approved, keep the draft and return to Step E.

### Step G: Handoff

Unless the approval already authorized execution:

```text
────────────────────────────────
CHOICE FOR YOU (select one)
Would you like to begin implementation now or later? This choice is an authorization: choosing A
starts work.
A. Now: start S04 only, under PLAN-2026-10-20 v3. Choosing A authorizes S04 and nothing after it;
   I will record your answer as ruling R-08.
B. Later: nothing starts. I record the plan as ready and give you the exact prompt to start it.
────────────────────────────────
```

The start option always says what it authorizes and which record it creates; for a series it
names the series and the SA (`references/multi-sprint-and-handoff.md` §3).

- **Now.** The PI's words are the execution authorization: record them verbatim as an R-NN (the
  approval ruling, if given in the same message). A bare letter is recorded as "(read back by the
  lead; PI chose: 'A')" followed by the chosen option's full text and its stated effect. For a
  series continuing without a new ruling at each boundary, also record the continuation SA, with
  the same read-back. Then, at sprint start, write
  `reports/sprints/SPRINT-NN.md` Part 1 from the approved plan, with the rows *Approved plan*,
  *Execution authorized by* and *Transition policy*, the start time (`date -u +%Y-%m-%dT%H:%MZ`)
  and commit; log `sprint_start`; rewrite `STATUS.md`. From there follow the charter: task plans
  under `CLAUDE.md` §5, independent review, close-out.
- **Later.** Set Readiness `Execution: not started`, `Next step: begin implementation`. Put the
  exact copyable start prompt in `START-HERE.md` and in chat. Log `handoff`, commit, and stop.

In a series under an SA, later sprints start without a new ruling, each boundary with its Part 2
close-out, independent review, checks, a dependency screen and a check of the transition
conditions. Pause for a new scientific, scope or PI-reserved decision, or a PI checkpoint.

## Authorization matrix

| The PI says | Result | Execution permitted? |
|---|---|---|
| "Draft the next three sprints." | A draft | **No** |
| "I approve this three-sprint plan." | Planning approval (R-NN) | **No.** Ask now or later, and what scope |
| "Start Sprint 1 now; check with me before Sprint 2." | Execution ruling for S1; gated boundary | **Sprint 1 only** |
| "Start this approved sequence; proceed after independent review and close-out if no new scientific or scope decisions arise." | Execution ruling plus continuation SA for the series | **Yes**, within the charter and the stated limits |
| "Use autonomous transitions as the project default from now on." | A governing change | Through `/arpd-amend` (charter §8 cadence, or an SA); nothing else is relaxed |

A continuation SA never covers what `CLAUDE.md` §6 reserves to the PI: closing a milestone,
accepting a validation, real data, sharing outside the project, amending governing documents.

## Recovery and change

- **Interrupted review:** recover the last committed version; it is not approved; continue Step E.
- **Approved, not started:** keep the approval as recorded. Never treat it as a start without a start
  direction or an SA that covers it.
- **Change after approval:** revise in the same file. Bump the Version, set the Status line to
  "Draft vN (vK approved by R-NN; vN not approved)" and restore the DRAFT banner. The approval
  stays valid only for vK; vN needs a new approval. The old ruling is never edited. A sprint
  already started under vK changes only through its scope-change log.
- **Change after start:** classify it: within task discretion (routine); a sprint scope change
  (the scope-change log, authorized as the log says); or a governing change (`/arpd-amend`).
- **New technical options:** compare them if an SA allows; adopt nothing consequential without
  the route `CLAUDE.md` §6 requires.
- **A sprint in a series closes:** run the boundary procedure. If any condition is unmet, ask the PI.

## Never

- Never implement, or write task plans, during planning.
- Never treat a draft, silence, or "sounds good" about a nearby draft as approval.
- Never treat plan approval as a start.
- Never widen a cadence or SA implicitly.
- Never edit a started Part 1, a closed sprint record, or recorded PI words.
- Never create a second roadmap, decision list or next-steps file.
- Never push without the PI's authorization.
