# Sprint S{{NN}}: {{objective}}

**This record is the audit trail for one sprint.**

- Part 1 is written at sprint start.
- Part 2 is written at close.
- After close the record is frozen. Corrections go in a later sprint's record.

Auditors reconcile this record against git, `DECISIONS.md`, `REQUIREMENTS.md` and `logs/events.jsonl`.

---

## Part 1: Sprint plan (written at start)

| Field | Value |
|---|---|
| Milestone served | M{{n}} (`MASTER_PLAN.md` §2) |
| Objective | {{one sentence; repeated in every brief}} |
| Target requirements | REQ-… → target state |
| Selected items | backlog IDs, each with why it belongs now |
| Plans | `plans/NNN-…` |
| Exit | the sprint is done when … (observable) |
| Team and workspace arrangement | {{e.g. lead with subagents, shared checkout}} |
| Authorized to continue into the next sprint without a check-in? | No / Yes, by R-NN |
| Start | {{date, time, commit SHA}} |

---

## Part 2: Close-out (written at end)

**Closed:** {{date, time, commit SHA}}

### 2.1 For the PI, in plain language

- **What now works**, as you would observe it:
- **What needs you**, ordered by what it unblocks:
- **What we decided without you** (see 2.3; skim and say "accept all" or name exceptions):
- **What is known to be wrong or not yet checked:**
- **Claims you should not make yet:**

### 2.2 Requirements

| Requirement | State before → after | Evidence (test name / check command / commit) | Not checked |
|---|---|---|---|

### 2.3 Decision tracking

Every decision taken in this sprint is listed here, at every tier, with its scientific consequence.

| ID | Decision | Tier (A/B/C) | Scientific consequence, or "none" | Decided by (PI ruling R-NN / lead agent / implementer) | Before or after commit? | Reversible? | Where recorded |
|---|---|---|---|---|---|---|---|

- **Tier A** decisions are listed in summary, grouped.
- **Tier B** decisions are listed individually and marked PROVISIONAL until the PI accepts them.
- **Tier C** decisions must show a PI ruling taken *before* the commitment.

### 2.4 Verification and review

| Plan | Implementer | Reviewer (did not implement) | Checks run | Result | Failures, with output |
|---|---|---|---|---|---|

### 2.5 Discoveries filed

| Item | Category (1–6) | Class | Filed as |
|---|---|---|---|

### 2.6 Incidents

Record coordination or governance failures, with the rule proposed, if any.

### 2.7 Resource use

Taken from `logs/events.jsonl` and the tooling.

| Measure | Value | Source |
|---|---|---|
| Elapsed sprint time |  | log |
| Autonomous elapsed time (no human prompt pending) |  | log |
| Summed agent session time |  | log |
| Human prompts / interactions |  | log |
| Active human time | *not measurable from logs; from the PI's time note if kept* | PI note |
| Tokens / cost |  | tooling |

### 2.8 Plan updates

List the changes to `MASTER_PLAN.md` §3 (order of work) and the backlog made at this close-out, and
why. Name the next sprint.
