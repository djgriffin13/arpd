# INDEX.md: map of the repository

**Governs nothing.** This is a lightweight discovery map (`CLAUDE.md` §2), so a new session or a new
person can find things. Update it in the same commit as the change it describes. List only paths that exist; for one that
will exist later, add "pending: <reason>" to its row. Do not list empty directories: git does not keep
them, so a listed path would not exist in a clone. The governance check reports listed paths that do
not exist.

| Path | What it is | Governing? |
|---|---|---|
| `CLAUDE.md` | Team charter: the rules every agent follows | Yes |
| `PARADIGM-SPEC.md` | The science: question, constructs, invariants, claims, validation plan | Yes |
| `REQUIREMENTS.md` | What the instrument must do, with state and evidence | Yes |
| `MASTER_PLAN.md` | Milestones, order of sprints, backlog, defects, risks, incidents | Yes |
| `DECISIONS.md` | The PI's rulings (verbatim) and the project's decisions | Yes |
| `ARCHITECTURE.md` | Design and conformance rules | Yes |
| `STATUS.md` | Right now: current sprint, in flight, on deck, handoff | Yes, for the present state only |
| `START-HERE.md` | How to work with the team on this project | No |
| `plans/` | One plan per scoped piece of work | Each for its own scope |
| `reports/sprints/` | One audit record per sprint | No (record) |
| `reports/` | Decision packs, walkthroughs, agent reports | No |
| `logs/events.jsonl` | Event log written by hooks and agents (git-ignored by default) | No (data) |
| `tools/` | Governance checker, plan numbering, event logger | No |
| {{project paths}} | {{source, tests, data, outputs}} |  |
