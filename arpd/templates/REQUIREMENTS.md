# REQUIREMENTS.md: what the instrument must do

**Governs:** each requirement and its state (`CLAUDE.md` §2, §7). Requirement states are changed only
by the lead agent, and only on recorded evidence. *Validated* also needs the PI's ruling.

**IDs:** `REQ-<AREA>-NN`. These are stable and never reused. Areas are set at setup, for example
`CORE`, `DATA`, `UI`, `ANALYSIS`, `EXPORT`.

**States:**

| State | Evidence required |
|---|---|
| Planned | A source in `PARADIGM-SPEC.md` (OP, INV, CLM, VAL) or a ruling |
| Implemented | The commit |
| Verified | A named test shown to fail without the fix, or a recorded check with command and commit |
| Validated | The paradigm spec's VAL evidence, accepted by a ruling |
| Retired | The ruling that retired it |

**Rules**

- *Planned* is not a place for unapproved ideas. Those go to the backlog in `MASTER_PLAN.md`.
- A requirement with an open defect against it is never reported as Verified or Validated.
- A requirement's wording is changed only in this file, and the change is recorded as a decision.
- Every requirement has an entry under *Requirement details*, with at least one acceptance
  criterion, its priority and its dependencies.

**Invariant, requirement or acceptance criterion?** Three different things:

| Term | What it says | Where it lives | How it works |
|---|---|---|---|
| Invariant (INV) | What must never break, or the results stop meaning what we intend | `PARADIGM-SPEC.md` §5 | The PI owns it. It holds for the life of the project. |
| Requirement (REQ) | What the instrument must do | `REQUIREMENTS.md` | It traces to a spec item or a ruling. It has a state and evidence. |
| Acceptance criterion | An observable check that something was delivered | A requirement's criteria: `REQUIREMENTS.md` *Requirement details*. A plan's: inside the plan, `plans/NNN-…` | A plan's criteria come from its requirements' criteria and close with the plan. Their evidence moves a requirement's state. |

---

## Requirements

| ID | Requirement (plain language) | Source | State | Evidence |
|---|---|---|---|---|
| REQ-CORE-01 |  | OP-01 | Planned |  |

<!-- The setup skill writes the requirements that the adopted Project Definition Report
(reports/setup/PROJECT-DEFINITION.md, sections 3 and 4) sends here under its status table, with the same
IDs. Each is phrased as what the PI would observe, e.g. "A participant can play a
full game against the partner agent and the game log records every action with its timestamp", not
as an implementation task. -->

## Requirement details

One entry per requirement in the table above, with the same ID. The table holds the state; this
section holds what each requirement must satisfy. A change to an entry is recorded as a decision,
like a change to the requirement's wording.

<!-- Format for every entry (the setup skill copies it from the adopted report):
### REQ-AREA-NN: short name
- **Acceptance criteria:**
  - an observable check an independent tester could run
- **Priority:** required / desired (a future-priority item is in MASTER_PLAN.md, not here)
- **Dependencies:** REQ IDs, architecture decisions (D-NN), Waiting on the PI rows, or "none"
-->

### REQ-CORE-01: {{short name}}

- **Acceptance criteria:**
  - {{an observable check}}
- **Priority:** {{required / desired}}
- **Dependencies:** {{REQ IDs, D-NN, Waiting on the PI rows, or "none"}}

Milestones (sets of requirements with a walkthrough exit) are defined in `MASTER_PLAN.md` §2, not
here.
