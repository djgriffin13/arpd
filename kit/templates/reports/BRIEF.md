# Brief: {{task}}

*From the lead agent to one team member. Self-contained: the recipient starts with a cleared context
and nothing else to go on. A brief directs work. It never grants authority that `CLAUDE.md` does not.*

- **To:** role and session
- **Acknowledge at once with:** `10-4 {{task}}`

## Intent

What this is for, in one or two sentences, tied to the current sprint objective (`STATUS.md` §2) and the
paradigm-spec items it touches.

## Task

The plan path and the commit that contains it, the branch name, and the base commit to start from.

## Scientific constraints

The INV items this work must respect, quoted.

## Do not

- Do not edit `MASTER_PLAN.md`, `STATUS.md`, `REQUIREMENTS.md`, `DECISIONS.md` or `PARADIGM-SPEC.md`. Propose changes in
  your report.
- Do not pursue discoveries. Classify and report them.
- Do not mark your own work complete or verified.
- {{task-specific fences}}

## Checks you may run

Name the checks and the time limit.

## Waits

List each wait with its correctness reason. Wait for nothing else. If blocked, take the next item in
your queue and tell the lead agent.

## Report

Use `reports/AGENT-REPORT.md`, saved to `{{path}}`.
