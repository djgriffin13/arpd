# Generation checklist (Phase 9)

Write files only after ruling R-01 has been recorded verbatim. In **fresh** and **import** modes the
project root is this repository. In **install** mode it is the target repository. Never overwrite an
existing file: see `import-path.md`.

| # | File | Source | How to fill it |
|---|---|---|---|
| 1 | `CLAUDE.md` | `kit/constitution/CORE.md` | Fill every `{{…}}`. Remove the HTML guidance comments. Append the selected modules under Part B in this order: science modules, then `team/team-arrangement.md`, with its two arrangements filled in. Mark draft modules "(draft module, untested)". Replace the Tier B and C rows' generic examples with this project's examples from Phase 6. |
| 2 | `PARADIGM-SPEC.md` | `kit/templates/PARADIGM-SPEC.md` | All phase 2 and 4 content. The question goes in **verbatim** in §1. Every ID is stable. |
| 3 | `REQUIREMENTS.md` | `kit/templates/REQUIREMENTS.md` | 5–15 requirements from Phase 3, each with a source ID. All start as Planned, except imported Verified evidence (import path, step 6). |
| 4 | `MASTER_PLAN.md` | `kit/templates/MASTER_PLAN.md` | The objective; milestone M1 (its requirement set and walkthrough); the planned order of 3–6 sprints; the cadence from Phase 6; risks from Phase 7. |
| 5 | `DECISIONS.md` | `kit/templates/DECISIONS.md` | R-01 verbatim. DEC entries for: the platform choice, the team and workspace arrangement, and any import and reconciliation decisions. |
| 6 | `ARCHITECTURE.md` | `kit/templates/ARCHITECTURE.md` | Overview in plain language, the platform table, components. A-rules start as TARGET. |
| 7 | `STATUS.md` | `kit/templates/STATUS.md` | Current state: setup complete; S01 on deck. Team, workspace and runtime-resource table. The PI's working style from Phase 1. |
| 8 | `INDEX.md` | `kit/templates/INDEX.md` | All top-level paths, including the project's own. |
| 9 | `plans/README.md` | `kit/templates/plans/README.md` | Copy as is. |
| 10 | `reports/` | `kit/templates/reports/*` | Copy as templates into `reports/templates/`. Create `reports/sprints/`. |
| 11 | `reports/sprints/SPRINT-01.md` | `reports/templates/SPRINT.md` | Part 1 only: the bounded first sprint from Phase 10. |
| 12 | `tools/` | `kit/tools/*` | Copy `check_governance.py`, `next_plan_number.py`, `log_event.py`, `summarize_events.py` and `hooks/log_hook.py`. |
| 13 | `.claude/settings.json` | `kit/settings/settings.json` | If a settings file exists, merge only the `hooks` key and show the PI the diff. Check that `python` resolves on this machine (`python --version`). If it doesn't, use `python3` or the full path. |
| 14 | `.claude/agents/` | `kit/agents/*` | Copy for lead-with-subagents and peer arrangements. |
| 15 | `docs/EVENTS.md` | `kit/docs/EVENTS.md` | Copy. |
| 16 | `AGENTS.md` | (write) | One line: "Read CLAUDE.md in full before doing anything else; it is this project's team charter." |
| 17 | `START-HERE.md` | (write) | For the PI, one screen: what each governing file is for, in one line each; the one command that runs all checks; the exact first prompt; how to check in, rule and amend; what to expect at a sprint boundary. |
| 18 | `.gitignore` | (append) | `logs/`, `output/`, `__pycache__/`, `.claude/settings.local.json` |

**Then:**

1. Run `python tools/check_governance.py` and fix any generation-caused FAIL.
2. Record the adoption in the event log: `python tools/log_event.py ruling --actor lead --ref R-01 --note "charter adopted at setup"`.
3. Remove the kit's pre-setup `README.md` and `QUICKSTART.md` from the project root by moving them to
   `docs/arpd-kit/`, so the project's own `START-HERE.md` is the entry point. `kit/` stays as the
   module library.
4. `git add -A`, then commit: "Set up ARPD project (ruling R-01)".
5. Do not push without the PI's authorization.
