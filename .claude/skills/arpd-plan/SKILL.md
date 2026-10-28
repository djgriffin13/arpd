---
name: arpd-plan
description: Plan the next piece of work for an ARPD project with the PI: a targeted task, a feature, a sprint, a series of sprints, or a bounded feasibility investigation. Reviews where the project stands, asks for the PI's goal first, sizes the effort, drafts a versioned plan in reports/planning/, gets the PI's approval of an exact version, and asks whether to begin implementation now or later. Use when the PI types /arpd-plan, or asks to "plan the next sprint", "plan sprints", re-plan, or resume a planning review.
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

**Every turn that waits for the PI** (`arpd/docs/INTERACTION.md` §2–§4, in short):

- Start with the progress line `**PLAN**  ✅ Review → 🔵 Goal → ⚪ Scope → ⚪ Draft → ⚪ Approval → ⚪ Handoff`
  (`PLAN` in bold, two spaces after it; ✅ done, 🔵 current, ⚪ to come; keep every arrow).
- End with exactly one labelled block, written as plain text, never inside a code fence.
  **Nothing follows its closing divider**: not even a sentence about other options. Offers such as
  "you can also edit it or ask for a review" go inside the block or above it.
- A closing turn that does not wait for the PI ends with the next step and its exact prompt, and no
  block.

**Python.** Before the first `python arpd/tools/...` command in a session, check for Python 3.8+
(`arpd/docs/NO-PYTHON.md` §1). Without it, use `sh arpd/tools/install.sh` in place of
`install.py`, and do what `arpd/docs/NO-PYTHON.md` says for every other tool command; nothing else
in this skill changes, and a read-through is never reported as a checker's PASS.

Read before you start:

- `arpd/docs/INTERACTION.md`: the labelled blocks, choices printed before any widget, the progress
  line, explaining when needed, the dependency screen. Follow it on every turn that waits for the PI.
- `references/planning-guide.md` (this folder): the read-back, sizing, the draft's content,
  versions, review, the dependency screen.
- `references/multi-sprint-and-handoff.md` (this folder): transition policies, recording approvals
  and starts, sprint start, the boundary procedure, the start prompt.

## Entry

1. **Is setup adopted?** `CLAUDE.md`'s Version line must name an adoption ruling (R-NN) that exists
   in `DECISIONS.md`. If `CLAUDE.md` is the kit's own file or the "Setup in progress" stub, or the ruling is missing,
   say so plainly and offer `/arpd-setup`. Never plan execution against an unadopted charter.
2. **Read, in this order:** `CLAUDE.md` and the standing authorizations in `DECISIONS.md`;
   `PARADIGM-SPEC.md` if the work touches the science; `REQUIREMENTS.md`, including *Requirement
   details* (acceptance criteria, priority, dependencies); `MASTER_PLAN.md`; `ARCHITECTURE.md`,
   including *Architecture decisions* (note which are Provisional or Delegated); `DECISIONS.md`
   *Waiting on the PI*, with each row's gate (*Needed by*); `STATUS.md` (Readiness, §5, §6, §8); the
   current or last sprint record and its evidence; existing `plans/` and open decision packs;
   `START-HERE.md` (orientation only); the adopted `reports/setup/PROJECT-BLUEPRINT.md` and the
   notes in `reports/planning/` and `reports/setup/` (`docs/discovery/` in an older project)
   (context only, never authority: where they differ from
   a governing document, the governing document wins). Do not re-ask a preference that is already
   recorded, and never re-ask the project's scope: the minimum usable version and every
   requirement's priority (P1–P5, with its feasibility and correctness-critical flags; required /
   desired / future in a project set up before v0.7) come from the adopted blueprint and
   `REQUIREMENTS.md`.
3. **A draft in progress?** A `reports/planning/PLAN-*.md` is approved only if its current Version
   line is the version an existing approval ruling names (*Approves:* line). Otherwise it is a
   draft: show its file and Version, say plainly that this version is **not approved** (naming any
   earlier version that was, and its ruling), list its open points, and offer to continue it
   (Step E). Log
   `python arpd/tools/log_event.py resume --actor lead --ref PLAN-… --note "planning resumed"`.
4. **An approved plan not yet started?** Do not re-plan it by default. If Readiness already says
   `Execution: authorized (R-NN), not started: waiting for …` (Step G, *Now, a prerequisite
   missing*), the start is already authorized: check the prerequisites (Step G) and, if met, start
   the sprint under R-NN, recording no new ruling; if one is still missing, say what, record
   nothing, and end as a closing turn with what the PI does (as Step G says). Otherwise, if the PI's message gives the start
   (the prompt left in `START-HERE.md`), record it as the execution ruling and go to Step G "now".
   Otherwise offer to start it or to revise it (a new version needs a new approval).
5. **An open sprint?** (a `SPRINT-NN.md` with Part 1 and no Part 2 *Closed* line.) Never renumber it
   or edit its Part 1. Offer:

```text
────────────────────────────────
**🔘 CHOICE FOR YOU (select one)**
Sprint S03 is still open. What would you like to plan?
A. The sprint after S03 (S04), while S03 continues.
B. A change to S03's scope, recorded in its scope-change log.
C. Close S03 first, then plan the next sprint.
────────────────────────────────
```

The argument `one` or `multiple` answers the one-or-several choice (Step C) in advance and nothing
else: the read-back, the goal and the scope still come before any draft. `resume` goes to 3 or 4.
Any other text after `/arpd-plan` is the PI's goal (Step B).

## The conversation

Add the topic list (goal, scope, dependencies, review level, exit evidence) under the progress
line when it helps. **Explain when needed** (`INTERACTION.md` §6), at the PI's level. There is no mode to ask about; an
interview mode an earlier kit version recorded is ignored (say so once; change nothing else).

**Priorities, when asked:** a question that asks the PI to place or change a requirement's priority
carries the scale in one line (on a five-point scale: P1 critical to the first working version, P2 needed next, P3 committed for later, P4 if time allows, P5 an idea).

**Small efforts stay small** (`references/planning-guide.md` §1): for a targeted task, Steps A–C
are one read-back, the goal (often already given) and one scope block; the plan is half a page; the
whole run four or five exchanges.

### Step A: Review

Give a short, factual read-back: what was last completed, what demonstrably works (with evidence;
never claim a test ran unless you ran it now or a record shows it), the roadmap, what is blocked,
and any feasibility investigation the requirements are waiting on. Run
`python arpd/tools/check_governance.py` and quote its OVERALL line. Do not lead with your own
priorities: the PI's goal comes first (Step B).

Use the inherited review and autonomy preferences (sprint autonomy, `CLAUDE.md` §8); do not ask about
overriding them. If the PI raises one, a this-time-only preference goes in the draft (non-governing);
a new **project default** (review depth, transition policy, planning cadence) is a governing change:
say what it would change, and record it through `/arpd-amend` from the PI's clear words.

### Step B: The PI's goal

Unless the invoking message already says what the PI wants next, ask, below the read-back:

```text
────────────────────────────────
**❓ QUESTION FOR YOU**
Do you know what you would like to build or accomplish next? Or would you like me to examine the
roadmap, the open requirements and where the project stands, and recommend the next priorities?
────────────────────────────────
```

- **The PI names a goal:** record it verbatim in the draft's notes; go to Step C.
- **The PI asks for a recommendation:** present the recommended thrust and the milestone it serves,
  the intended deliverables, options and trade-offs, blockers and dependencies, what you would defer
  (`references/planning-guide.md` §2), then go to Step C with it as the proposed goal.

### Step C: Scope

**Classify the effort** from the goal and the records (`references/planning-guide.md` §1), and say
in a sentence which kind it is and why:

| Effort | What it is | The plan |
|---|---|---|
| **Targeted task** | One scoped change: a fix, a small addition | One sprint of one work package; about half a page |
| **Feature** | A bounded capability: a few related work packages | One sprint |
| **Sprint** | A milestone's worth of work, or a mix | One sprint, with exit evidence, dependencies and review level |
| **Several sprints** | A thrust larger than one sprint, with shared dependencies | A series, the first precise and later ones provisional |
| **Feasibility investigation** | A question the build depends on (a requirement's *Feasibility: to investigate*, a new idea's viability, whether data carry what is needed) | One bounded sprint whose deliverable is a finding with its evidence, not product code (*Feasibility investigations*, below) |

**Check alignment with `MASTER_PLAN.md`.** If the goal departs from the roadmap or a milestone, say
plainly what it would displace or delay, which dependencies change, and whether it needs a
milestone change (`/arpd-amend`, by ruling). The roadmap is the record of the current direction, not
proof that the direction is right: new findings can justify changing it, and the PI decides. Never
rewrite the roadmap silently.

**Then settle the scope,** in one block when the effort is small (for example: "This is a targeted
task: one sprint of one work package. Does this scope match what you want?"). For a sprint-sized
effort or larger, present the deliverables, dependencies and what you would defer, and ask whether
they match; in a complex project keep a short topic list and follow up until the scope is clear
(question fuse).

**One sprint or several: the PI always chooses, explicitly, when several are plausible.** A targeted
task, a feature or a feasibility investigation is one sprint: state it, do not ask. Otherwise:

```text
────────────────────────────────
**🔘 CHOICE FOR YOU (select one)**
Would you like to plan the next sprint only, or map out several sprints as one coordinated effort?
A. The next sprint only.
B. Several sprints as one coordinated effort.
────────────────────────────────
```

For a complex project, say above the block why several may help (shared dependencies). The project's
sprint autonomy default (`CLAUDE.md` §8, SA-01) is shown as "(recommended)" where it applies, never
applied silently.

If several, ask **once** per planning effort how transitions should work
(`references/multi-sprint-and-handoff.md` §2). The answer is planning input: inherited cadence
(`CLAUDE.md` §8) and SAs in force are never widened by it, and continuation becomes authority only
by the PI's words in Step F or G. For a single sprint, the plan's transition policy is the
charter's default cadence ("per charter §8 / SA-01"), not recorded as a PI choice.

### Feasibility investigations

A feasibility investigation answers a stated question within a stated bound, so that a later plan
can commit, or not, on evidence:

- **The question and why it matters:** the requirement or idea it unblocks (its *Feasibility* field).
- **The bound:** a time or effort limit in the plan; the investigation ends at the bound with what
  was found, never extended without the PI.
- **The deliverable:** a short finding (`reports/sprints/SPRINT-NN.md` Part 2, with any evidence
  files beside it): what was tried, what the evidence shows, the answer (feasible / not feasible /
  feasible with conditions / still unknown), and the recommendation.
- **Prototype code** written to investigate is not product code: it lives where the plan says (for
  example `spikes/`), and becomes product code only through a later plan, with tests and review.
- **What follows:** the requirement's *Feasibility* becomes "established (S0N)" or stays "to
  investigate", recorded as routine; any change to scope or priority the finding suggests goes to the
  PI.

### Step D: Draft

Write `reports/planning/PLAN-YYYY-MM-DD.md` (`-2`, `-3` for a later effort the same day) from
`arpd/templates/planning/PLAN.md`: minimal but sufficient, the first sprint precise, later sprints
labelled provisional with what may change them (`references/planning-guide.md`). Mark it DRAFT,
`Version: v1`.

**Dependency screen** (`references/planning-guide.md` §5): the plan cites *Waiting on the PI* rows
and does not restate them; only dependent work is blocked. Respect each row's gate: one needed
"before planning" blocks approval of a plan whose work depends on it: put it to the PI before
approval (or defer it by ruling); a plan whose work does not depend on it may be approved while it
stays open, and the plan says so, citing the row ("Waiting #3: open; this plan does not depend on
it"); one needed "before
implementing X" is scheduled to be decided before X's work package; one needed "before deployment"
blocks only release work. Decisions put to the PI (a decision pack included) end with a labelled
block, `CHOICE FOR YOU` or `APPROVAL REQUIRED` (`INTERACTION.md` §2), never in prose. Set
Readiness `Planning: draft (PLAN-…, v1)`, `Next step: review plan`.

Commit: `Plan draft PLAN-YYYY-MM-DD v1 (not approved)`. Summarize the plan in chat in one screen;
the detail stays in the file.

### Step E: Review and revise

Tell the PI the draft is theirs to examine: they may edit it, challenge priorities, ask for
re-planning, or send it to an independent agent. Ask whether to have an outside review as an option
inside the block that ends the draft turn, not only in prose; never require one for a small plan.
Each revision bumps the Version (v2, v3), lists what changed, and is committed with the same
message pattern. No governing file changes during review.

### Step F: Approval

When the PI is satisfied, ask in an `APPROVAL REQUIRED` block (never `CHOICE FOR YOU`):

```text
────────────────────────────────
**✋ APPROVAL REQUIRED**
Approve reports/planning/PLAN-2026-10-20.md v3 (commit abc1234)?
A yes approves this plan as the scope of S04 (planning only). It does not start work; I will ask
next whether to begin now or later. Waiting decisions affecting it: DECISIONS Waiting #2 (blocks
WP3 only).
────────────────────────────────
```

Name what a yes covers: planning only, S0N's execution, or a series. Record the PI's words verbatim
as the next R-NN, in the plan-approval format (`arpd/templates/DECISIONS.md`; `references/multi-sprint-and-handoff.md` §3). When the
PI does not clearly say more, record **planning approval only**. Clear words need no second
confirmation; ask once only if they could mean materially different things. Then set the plan's status marker as its template says ("Approved by R-NN (vN, commit …)"; the
approved version's text is never edited), set its `MASTER_PLAN.md` §3 rows to "planned (PLAN-… vN, R-NN)" and §4 items to
Selected (milestone changes go to `/arpd-amend`),
set Readiness `Planning: approved (PLAN-…, vN, R-NN)`, run the checker, log
`python arpd/tools/log_event.py ruling --actor lead --ref R-NN --note "approval of PLAN-… vN"`, and commit
naming R-NN. If not approved, keep the draft and return to Step E.

### Step G: Handoff

If the approval in Step F already authorized execution (the PI's words covered S0N's execution), do
not ask now or later again and record no new ruling: check the prerequisite below, then go to *Now*
(prerequisites met, or a prerequisite missing) under that ruling.

**Prerequisite for implementation: first, before the block below,** check that the adopted charter
and the agent roles are live in this session. Before starting any sprint (Now, or a later start
prompt), check both:

1. **The charter** is in this session's project memory, not only a file you read: the session
   started after the charter was written, or the PI has run `/compact` since (Claude Code's
   documentation says `/compact` re-reads `CLAUDE.md` from disk). You can tell: the charter's text
   appears in your loaded project memory.
2. **The agent roles,** when the team arrangement uses subagents (*Lead with subagents*, *Peers*;
   not *Solo*, whose fresh-subagent reviewer needs no installed role): the roles it uses
   (`implementer`, `reviewer`, and `tester` if a tester is named) exist as files in `.claude/agents/`
   **and** appear among the agents available to you now, not only as files (the documentation says roles added during a session usually
   appear only in a new session). Judge both items by what you can see loaded, never by when you
   think the conversation began. If they do not exist at all (declined or owed at setup), say so and offer the owed step
   first (`python arpd/tools/install.py owed .`, on the PI's yes; `CLAUDE.md` §9 without Python): a
   new session alone will not help. If the PI declines, implementation needs a changed arrangement
   (`/arpd-amend`, for example to *Solo*); say so, and start nothing.

**Say the result in one line before you record or start anything**, every time (also on a resumed
or waiting start), for example: "Prerequisites: the charter is loaded in this session; implementer
and reviewer are available." When the sprint starts, the same line goes into Part 1's progress log.
After an in-place setup, setup and planning usually ran in one session, so one of these is often
missing. Say in two sentences what is missing, if anything, then show the block, adapted:

```text
────────────────────────────────
**🔘 CHOICE FOR YOU (select one)**
Would you like to begin implementation now or later? This choice is an authorization: choosing A
starts work.
A. Now: start S04 only, under PLAN-2026-10-20 v3. Choosing A authorizes S04 and nothing after it;
   I will record your answer as ruling R-08.
B. Later: nothing starts. I record the plan as ready and give you the exact prompt to start it.
────────────────────────────────
```

When a prerequisite is missing, option A reads instead: "A. Authorize S04 now; it starts once
<what is missing> is done (type `/compact` / start a fresh session), from the prompt I give you.
I will record your answer as ruling R-08." and the line "choosing A starts work" becomes "choosing A
authorizes the start". The start option always says what it authorizes and which record it creates;
for a series it names the series and the SA (`references/multi-sprint-and-handoff.md` §3).

- **Now, prerequisites met.** The PI's words are the execution authorization: record them verbatim
  as an R-NN (with the approval ruling, if given in the same message), unless already recorded
  (Entry 4, or an approval that authorized execution), plus the continuation SA for a
  series, as `references/multi-sprint-and-handoff.md` §3 says (including a bare letter's
  read-back). Then start the sprint (§4 there: Part 1 of `reports/sprints/SPRINT-NN.md` from the
  approved plan, STATUS, `sprint_start`) and follow the charter: task plans under `CLAUDE.md` §5,
  independent review, close-out.
- **Now, a prerequisite missing.** Record the execution ruling exactly as above, but start nothing.
  Set Readiness `Execution: authorized (R-NN), not started: waiting for <"/compact" | a fresh
  session | the owed agent roles>`, `Next step: begin implementation`; put the exact start prompt in
  `START-HERE.md` *Next step* ("/arpd-plan resume. Start S04 under PLAN-… vN, authorized by R-NN.");
  commit; and end as a
  closing turn with exactly what the PI does: type `/compact`, then that prompt (when only the
  charter is missing); or quit and start a fresh session (`claude`, then that prompt) when the agent
  roles were installed in this session. Never start implementation with the charter only read as a
  file, and never substitute a general subagent for a missing installed role. The session that
  receives the prompt checks both again, then starts the sprint under the recorded ruling (*Entry*
  4): it records no new ruling.
- **Whenever you change `STATUS.md`** (approval, a start, a waiting start, Later), also update its
  *Last rewritten* line (from `date -u`) and its base commit, so a recovering session starts from
  the right point.
- **Later.** Set Readiness `Execution: not started`, `Next step: begin implementation`. Put the
  exact copyable start prompt in `START-HERE.md` and in chat. Log `handoff`, commit, and stop (§6
  there).

Either way, refresh `STATUS.md` §4 *On deck* with the handoff (the sprint now open, or the start
prompt); never leave it at "Run /arpd-plan".

In a series under an SA, later sprints start without a new ruling, after the boundary procedure (§5
there); pause for a new scientific, scope or PI-reserved decision, or a PI checkpoint.

**What the PI's words authorize** (a draft, a plan approval, an execution start, a continuation SA,
a governing change) follows `arpd/docs/INTERACTION.md` §1 and `references/multi-sprint-and-handoff.md`
§3.

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
