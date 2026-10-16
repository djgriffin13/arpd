# MASTER_PLAN.md: objective, milestones, order of work and backlog

**Governs:** priorities, milestones, the planned order of development, the backlog, known defects,
risks and incidents (`CLAUDE.md` §2).

- The lead agent is the only author.
- Changes to milestones need the PI's ruling.
- Sprint-level changes are recorded at sprint planning and close-out.
- Requirement *states* live in `REQUIREMENTS.md`. The *current* sprint's live progress lives in
  `STATUS.md`. Neither is restated here.

---

## 1. Objective

{{One paragraph, in the PI's terms: what the instrument will let the PI study that they cannot study
now. Cite PARADIGM-SPEC §1–2.}}

## 2. Milestones

A milestone is a set of requirements plus a walkthrough. It is **done** when every listed requirement
reaches its target state with evidence, and the PI records PASS on the walkthrough. Only the PI
closes a milestone.

| Milestone | What the PI will be able to do | Requirements and target state | Walkthrough | State |
|---|---|---|---|---|
| M1 | {{first usable version}} | REQ-…: Verified; REQ-…: Validated | `reports/WALKTHROUGH-M1.md` | Open |

## 3. Planned order of development

This is the roadmap: the sprints expected next, in order. Each sprint is sized to finish in one
working block. The order is revised at each sprint close-out, and the revision is recorded in the
sprint record.

| Sprint | Objective (one sentence) | Target requirements | Depends on | State |
|---|---|---|---|---|
| S01 | {{first bounded task from setup}} |  |  | Planned |

**Cadence** (`CLAUDE.md` §8): {{check-in after every sprint (default) / after every N sprints, as
authorized by ruling R-NN}}. Even when several sprints run without a check-in, each sprint boundary
keeps its planning, review, testing and plan-update steps.

## 4. Backlog

New items enter as Backlogged. Filing does not schedule them (`CLAUDE.md` §5). An item is pulled into
a sprint only by a recorded decision that names the requirement it serves and why it matters now.

| ID | Item | Class | Discovery category (1–6) | Serves | State |
|---|---|---|---|---|---|

**Class:**

- **Critical:** a wrong scientific result, data loss, or a privacy exposure.
- **Feature:** a capability named by a requirement.
- **Bug:** supported functionality is wrong.
- **Hardening:** robustness against unusual input.
- **Maintenance:** cleanup, docs or tooling.

**State:** Backlogged · Selected · In progress · Blocked · Done.

## 5. Known defects

| ID | Defect | Affects (REQ, INV) | Severity | State |
|---|---|---|---|---|

## 6. Risks

| ID | Risk | Likelihood and impact | Mitigation | Owner |
|---|---|---|---|---|

## 7. Incidents and process lessons

These are coordination or governance failures, as opposed to code bugs. Examples: a false "done", a
lost instruction, a drifting construct, two agents writing one file, or a consequential decision
adopted without authority. A rule follows only by PI ruling, and it cites the incident (`CLAUDE.md` §10).

| ID | Date | What happened | Effect | Rule proposed | Ruling |
|---|---|---|---|---|---|
