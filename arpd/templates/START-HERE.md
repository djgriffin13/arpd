<!--
ARPD template: START-HERE.md, the one-screen orientation for a project (written at setup).
Governs nothing (CLAUDE.md §2), except that its "## Map" section is the project's navigation map.
Setup fills the {{...}} fields and removes these comments. /arpd-plan rewrites only "## Next step";
anyone updates "## Map" in the same commit as the change it describes.
-->
# Start here: {{PROJECT_NAME}}

**Governs nothing.** It points to the documents that do. The user's guide is `arpd/docs/GUIDE.md`.

## What each file is for

- `CLAUDE.md`: the team charter, the rules every agent follows.
- `PARADIGM-SPEC.md`: the science: question, constructs, invariants, permitted claims, validation.
- `REQUIREMENTS.md`: what the instrument must do, each requirement's state and evidence.
- `ARCHITECTURE.md`: the design and its conformance rules.
- `MASTER_PLAN.md`: milestones, order of work, backlog, defects, risks.
- `DECISIONS.md`: the PI's rulings, verbatim, and the project's decisions; *Waiting on the PI*.
- `STATUS.md`: right now: readiness, the current sprint, what is in flight, how to pick up.
- `reports/setup/PROJECT-DEFINITION.md` v{{N}} (commit {{SHA of the adoption-first commit}}): the
  report the PI adopted at setup (R-{{NN}}), the record of what was adopted.

**An invariant** (`PARADIGM-SPEC.md`) must always hold, whatever is built. **A requirement**
(`REQUIREMENTS.md`) is something the instrument must do. **An acceptance criterion** is the test
that shows one requirement is met.

## Commands

- Tests: `{{the project's test command, e.g. python -m pytest}}`
- Governance check: `python arpd/tools/check_governance.py` (last run: {{its OVERALL line, verbatim}})
- `/arpd-plan` drafts a sprint plan; you approve a version; work starts only when you say so.
- `/arpd-checkin`: where things stand and what needs you. `/arpd-amend`: change the rules, the
  science, the milestones or what agents may decide.
- At each sprint boundary the lead closes the sprint record, has it reviewed independently, runs the
  checks and brings you what needs a decision.

## Next step

{{The exact next prompt, e.g. "Run /arpd-plan to plan the first sprint." Current state is stated here
only.}}

## Map

<!-- Every top-level entry, one line each, path first in backticks. A path that will exist later:
"pending: <reason>". No empty directories. arpd/ is the kit's copy, never edited here. -->

- `CLAUDE.md`, `AGENTS.md`: the charter, and the pointer to it for other agents
- `PARADIGM-SPEC.md`, `REQUIREMENTS.md`, `ARCHITECTURE.md`, `MASTER_PLAN.md`, `DECISIONS.md`,
  `STATUS.md`: the governing documents (above)
- `START-HERE.md`: this file
- `reports/`: `setup/` (the adopted report, the setup notes{{, the import baseline}}), decision
  packs, walkthroughs
- `reports/sprints/`: one record per sprint (pending: created when the first sprint starts)
- `plans/`: one plan per scoped piece of work (pending: created with the first task plan)
- `arpd/`: the ARPD kit's copy (tools, templates, charter source, event log in `arpd/logs/`,
  git-ignored); never edited here, refreshed with
  `python arpd/tools/install.py update . --kit <kit clone>`
- `.claude/`: Claude Code's skills, settings and agent roles
- {{one line per project path: source, tests, data, outputs}}

## Known gaps

{{Each owed item, with the exact command to run, or "None."}}
