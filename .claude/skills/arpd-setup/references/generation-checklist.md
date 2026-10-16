# Generation checklist (Phase 9)

Write files only after the adoption ruling has been recorded verbatim. In **fresh** and **import**
modes the project root is this repository. In **install** mode it is the target repository. Never
overwrite an existing file: see `import-path.md`.

**IDs.** R-01, SA-01 and DEC-01 below assume an empty ledger. When importing a project that already
has a `DECISIONS.md`, continue its numbering, and fill an inherited placeholder rather than reusing a
given ID (`import-path.md`, *Numbering*).

**Before writing (fresh and import modes):** move the kit's own pre-setup files (`README.md`,
`QUICKSTART.md`, `CLAUDE.md`, `AGENTS.md`) to `docs/arpd-kit/` with `git mv`. They are not project
instructions: never reconcile them or write `.arpd` files beside them. For a starter that lives
inside the kit, then move the starter to the root (`import-path.md`, *Starter projects*).

| # | File | Source | How to fill it |
|---|---|---|---|
| 1 | `CLAUDE.md` | `kit/constitution/CORE.md` | Fill every `{{…}}`, including `{{AUTHORITY_PROFILE}}`, which is the profile name only (for example "Bounded autonomy"); the charter line already says it is recorded as SA-01. Remove the HTML guidance comments. Append the selected modules under Part B in this order: science modules, then `team/team-arrangement.md`, with its two arrangements filled in. Mark draft modules "(draft module, untested)". Under §6, after the routes table, add "This project's examples": routine, delegated and consult choices drawn from Phase 6. |
| 2 | `PARADIGM-SPEC.md` | `kit/templates/PARADIGM-SPEC.md` | All phase 2 and 4 content. The question goes in **verbatim** in §1. Every ID is stable. |
| 3 | `REQUIREMENTS.md` | `kit/templates/REQUIREMENTS.md` | 5–15 requirements from Phase 3, each with a source ID. All start as Planned, except imported Verified evidence (import path, step 6). |
| 4 | `MASTER_PLAN.md` | `kit/templates/MASTER_PLAN.md` | The objective; milestone M1 (its requirement set and walkthrough); the planned order of 3–6 sprints; the cadence from Phase 6; risks from Phase 7. |
| 5 | `DECISIONS.md` | `kit/templates/DECISIONS.md` | SA-01 verbatim, with every field filled. R-01 verbatim. DEC entries for: the platform choice, the team and workspace arrangement, and any import and reconciliation decisions. |
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
| 17 | `START-HERE.md` | (write; for an imported ARPD starter, regenerate it for the new PI and move the old one to `docs/arpd-kit/START-HERE-starter.md`) | For the PI, one screen: what each governing file is for, in one line each; the one command that runs all checks; the exact first prompt; how to check in, rule and amend; what to expect at a sprint boundary. |
| 18 | `.gitignore` | (append; merge with an imported project's) | `logs/`, `output/`, `__pycache__/`, `.claude/settings.local.json`. `logs/` stays uncommitted: each sprint's events are exported to `reports/sprints/` at close (`docs/EVENTS.md`). |

**Then:**

1. Run `python tools/check_governance.py` and fix any generation-caused FAIL.
2. Record the adoption and the authority profile in the event log:
   - `python tools/log_event.py ruling --actor lead --ref R-01 --note "charter adopted at setup"`;
   - `python tools/log_event.py ruling --actor lead --ref SA-01 --note "authority profile set at setup"`.

   (Use the actual IDs if the ledger was inherited.)
3. Check that the kit's pre-setup files are in `docs/arpd-kit/` (moved before writing), so the
   project's own `START-HERE.md` is the entry point. `kit/` stays as the module library.
4. `git add -A`, then commit: "Set up ARPD project (ruling R-NN)", naming the adoption ruling.
5. Do not push without the PI's authorization.
