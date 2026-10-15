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

---

## Requirements

| ID | Requirement (plain language) | Source | State | Evidence |
|---|---|---|---|---|
| REQ-CORE-01 |  | OP-01 | Planned |  |

<!-- The setup skill writes the first 5-15 requirements from the interview. Each is phrased as what
the PI would observe, e.g. "A participant can play a full game against the partner agent and the
game log records every action with its timestamp", not as an implementation task. -->

Milestones (sets of requirements with a walkthrough exit) are defined in `MASTER_PLAN.md` §2, not
here.
