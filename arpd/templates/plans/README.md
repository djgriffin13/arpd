# Plans

There is one numbered plan per scoped piece of work (`CLAUDE.md` §5). An approved plan is
authoritative for executing its own scope. Priorities and order of work live in `MASTER_PLAN.md`; live progress lives in `STATUS.md`.

- **Naming:** `NNN-kebab-slug.md`. Claim the number with `python arpd/tools/next_plan_number.py`. The
  script scans every branch, so parallel work never collides.
- **Status:** Proposed → Approved → Active → Complete.
- **Approval:**
  - A plan that makes a consequential choice (`CLAUDE.md` §6) needs the PI, unless a standing
    authorization covers it.
  - Other plans are approved by the lead agent within the PI's standing direction, and the approval
    is recorded in the header.
- **Completion:** only the lead agent sets Complete, after the plan's acceptance criteria have
  evidence. Implementers never mark their own plan complete.
- **Size:** a plan should be finishable in one working block. Split anything larger.
- **Not a sprint plan.** A numbered plan is one scoped piece of work. A sprint plan, drafted with
  `/arpd-plan` in `reports/planning/`, is approved by the PI and covers a whole sprint or series.

How an invariant, a requirement and an acceptance criterion differ: `REQUIREMENTS.md`. A plan's acceptance criteria are drawn from its requirements' criteria and close with the plan.

## Template

```markdown
# Plan NNN: <title>

| Field | Value |
|---|---|
| Status | Proposed |
| Approved by | PI ruling R-NN / lead agent under standing direction |
| Owner | role and session |
| Class | Critical / Feature / Bug / Hardening / Maintenance |
| Serves | REQ IDs, and the PARADIGM-SPEC items touched (OP, INV, CLM); or "none" with the reason |
| Why now | the reason this is selected now |
| Outcome | what the PI will be able to see or do afterwards |
| Non-goals | adjacent work deliberately left out (filed as Backlogged) |
| Branch | `plan-NNN-<slug>` |

## Problem
## Scientific invariants this work must respect (INV IDs)
<the INV items this work must respect, and how; "none" is a valid answer, but an empty field is not>
## Design placement
<which component(s); which A-NNN rules apply and why they are not violated>
## Acceptance criteria and evidence
| Criterion (observable) | Evidence that will show it | Software (Verified) or science (Validated)? |
|---|---|---|
## Checklist
1. [ ] ...
## Files expected to change
## Decisions made during execution
<decisions with their route (routine / delegated, citing SA-NN / consult, citing R-NN); discoveries with their category 1-6, filed as Backlogged unless 1-3>
## Review (filled at close)
<what changed, tests and checks with commit, requirement states proposed, follow-ups, risks, anything not checked>
```
