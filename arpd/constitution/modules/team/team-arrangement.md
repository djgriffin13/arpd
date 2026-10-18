## B.T-TEAM: Team and workspace arrangement

*Module: team-arrangement v1.0. Always installed. The setup interview fills in the two choices
below. Either can be changed later, by ruling.*

The **team arrangement** (who does the work) and the **workspace arrangement** (where the work
happens) are separate choices.

- **This project:** team = {{TEAM_ARRANGEMENT}}; workspace = {{WORKSPACE_ARRANGEMENT}}.
- **Why:** {{one line from setup, e.g. "work is mostly sequential, so one lead agent with review
  subagents"}}.

### Team arrangements

| Arrangement | What it is | Use when |
|---|---|---|
| **Solo** | One agent session does the work. Review is done by a fresh subagent or a fresh session that did not write the code. | Small or tightly sequential work; first projects |
| **Lead with subagents** *(default)* | The PI talks to **one lead agent**. The lead plans, briefs and integrates, and delegates bounded tasks to subagents: implementer, reviewer, tester (`.claude/agents/`). Subagents are not visible to the PI; their work is visible in the record. | Most projects. Gives role separation and independent review while the PI has a single point of contact. |
| **Peers** | Several concurrent agent sessions, each with a role. The lead (the "master") coordinates and is the only author of the plan and status files. | Work that genuinely splits into parallel streams with few dependencies, run by a PI comfortable with more moving parts |

### Workspace arrangements

| Arrangement | Default for |
|---|---|
| **Shared checkout** | Solo, and lead with subagents working **one at a time** |
| **Separate worktrees** (one per concurrent agent, each on its own branch) | Any arrangement where agents work **at the same time** |

**Concurrent agents in one shared checkout is discouraged.** It needs a ruling, and per-agent file
ownership stated in `STATUS.md`.

### Shared runtime resources: always configured separately

Worktrees separate files. They do **not** separate ports, OS temp directories, caches, databases or
services. Each concurrently working agent therefore gets its own:

- port range;
- output and scratch directory (for example `output/<agent>/`);
- name for any service or database it starts.

The lead records each assignment in `STATUS.md` §7. An agent never uses a resource assigned to
another, and never deletes output it did not create.

### Roles and their limits (every arrangement)

- **The lead agent:**
  - plans sprints;
  - writes briefs (*Brief format*, below);
  - is the **only writer** of `STATUS.md`, `MASTER_PLAN.md` and requirement states;
  - records rulings;
  - writes the sprint record;
  - brings consult-route decisions to the PI;
  - does not review its own work;
  - does not mark its own plans Verified.
- **Implementer:** works one plan in its own scope. It runs targeted checks only, reports in the format of
  `.claude/agents/implementer.md` (from `arpd/agents/`), and never sets requirement states or marks its own work complete.
- **Reviewer:** did not write the change under review, and opens by saying so. It:
  - checks the change against the plan's acceptance criteria and the paradigm spec's invariants;
  - re-runs the stated checks;
  - sends work back only for a failed check or a broken rule, never on taste.
- **Tester** (optional): writes or runs checks *from the specification*, without reading the
  implementation first, where the plan calls for independent tests.

### Communication (peers and concurrent subagents)

- **Acknowledge every brief or instruction at once** with `10-4 <subject>`. No acknowledgement means
  the message was not received: re-send it and check the address.
- **A wait needs a correctness reason.** An agent waits for another's output only when its own work
  cannot be correct without it. Otherwise it builds against the published shape of that output and
  carries on.
- **Lateral messages only at real dependencies.** Status and decisions go through the lead.

### Brief format

A brief goes from the lead to one team member. It is self-contained (the recipient starts with a
cleared context), directs work, and never grants authority that `CLAUDE.md` does not. It names:

- **To:** the role and session; **acknowledge with** `10-4 <task>`.
- **Intent:** what the work is for, tied to the sprint objective (`STATUS.md` §2) and the
  paradigm-spec items it touches.
- **Task:** the plan path and the commit holding it, the branch, and the base commit.
- **Invariants:** the INV items the work must respect, quoted.
- **Do not:** edit `MASTER_PLAN.md`, `STATUS.md`, `REQUIREMENTS.md`, `DECISIONS.md` or
  `PARADIGM-SPEC.md` (propose changes in the report); pursue discoveries (classify and report
  them); mark the work complete or verified; plus any task-specific fences.
- **Checks you may run,** and the time limit.
- **Waits:** each with its correctness reason; if blocked, take the next queued item and tell the
  lead.
- **Report:** in the role's report format (`.claude/agents/`), saved to a named path.
