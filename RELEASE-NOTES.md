# Release notes: ARPD v0.7.0-rc.2 (release candidate)

**Status: a release candidate, held for manual testing. Not a final release.** It redesigns setup
around the researcher: a research-aware interview in phases, each with defined information needs
and a summary the PI confirms, run in the folder the PI cloned, with a goal-first `/arpd-plan`, and
working without Python. A final release follows only after the manual walkthrough and the usability
protocol ([evaluation/usability-v0.7/](evaluation/usability-v0.7/)) have been run and any blockers fixed.

**rc.2 (after the PI's first walkthrough attempt):** conversion no longer deletes anything. The kit's
files and the clone's old git history move to a backup folder beside the project, with a
`RESTORE.md` to undo it; the dry run has an explicit `--dry-run`; and when Claude Code's auto-mode
safety check blocks the command, setup hands the PI one line to type (`! python …` or, without
Python, `! sh …`) instead of improvising. The local-work bundle is gone (the moved `.git` keeps every
branch, tag and stash). The architecture guide now favours standard scientific libraries (numpy,
scipy, the tidyverse) for computational work, keeps the preference for few dependencies for less
established ones, and sizes the workload with a rough count, never a benchmark, when speed matters. The Development phase now opens with a
choice of how the agents work (one agent with an independent reviewer, a lead with helpers, or
parallel agents), then an open follow-up on anything more about how they run; a very small project
skips the minimum-usable-version question and goes straight to priorities.

## What ARPD is

A team-charter kit and four Claude Code skills (`/arpd-setup`, `/arpd-plan`, `/arpd-checkin`,
`/arpd-amend`). A domain researcher who is not a software developer uses them to direct a team of AI
coding agents building a research instrument, while keeping authority over every consequential
scientific decision. See [README.md](README.md).

## What changed since v0.6.0-rc.1

- **Setup works in place.** Clone or download ARPD, open Claude Code there, type `/arpd-setup`. After
  the first answer setup asks where the project lives; the default turns this folder into the
  project (`install.py convert`): ARPD's own development files are removed (the list is in
  `.arpd-kit`), `arpd/` and the skills stay, every file of the PI's is kept, and the folder gets a
  fresh git history with no remote; the kit's files and old history go to a backup folder, nothing
  deleted. The
  interview continues in the same session. Existing repositories are still installed in place, with
  their history and remote; a new folder or an import is still available.
- **A setup-safe `CLAUDE.md`.** A fresh clone's `CLAUDE.md` says only that setup comes first; the
  kit's development rules moved to `DEVELOPING.md`. During setup the skill governs; after adoption
  the generated charter does. Claude Code documents loading `CLAUDE.md` at session start, with no mid-session
  reload except `/compact`; so setup re-reads the new charter before the handoff, and implementation
  starts only once the charter is loaded (`/compact`, or a fresh session when agent roles were
  installed in the same session) and the agent roles exist: `/arpd-plan` checks this before any
  sprint starts.
- **A phased, research-aware interview:** Intake → Objectives → Constraints → Design → Development →
  Definition Report. Each phase has required items (IN, OB, CS, DS, DV), each marked Confirmed,
  Inferred, Open, Deferred or N.A.; setup asks only for what is open and confirms its inferences in a
  phase summary. Every phase ends with its own closeout (continue / correct / go back). A
  confirmation is not binding; adopting the report remains the only formal setup authorization.
- **Intake restored,** without the v0.4 questionnaire feel: field, coding comfort and involvement
  (kept apart), users and maintainers, location, stage, early constraints, and the agent's **role**
  (build as specified; technical review; technical and theory-alignment review; co-design;
  audit/extend existing code; exploration), recorded on a technical and a scientific axis.
- **Theory when it matters.** Objectives covers the research domain and questions, traced to
  capabilities and requirements, unless the PI asked for a technical-only focus (said once). A
  researcher with no tool in view gets a short tool-opportunity discussion, then a clean exit with a
  ready-to-paste prompt.
- **Constraints and model commitments,** classed Must / Prefer / Model commitment (with epistemic
  status) / Must hold / Open question, ending in a **commitments review** that flags contradictions,
  circularity and questionable assumptions under every role and recommends reframing (a research
  question, an outcome, a configurable model assumption) for the PI to decide. Citations only from
  sources actually checked; otherwise labelled unverified.
- **Design asks for the PI's design first,** adapts its depth to the PI's coding comfort, iterates as
  long as needed, and closes with an explicit readiness question.
- **Development:** the PI's own rules first; the minimum usable version; P1 Core / P2 Next / P3
  Planned / P4 Wanted / P5 Idea, with separate *Feasibility* and *Correctness-critical* flags; the
  agent workflow explained in full (cost included); and the rules Claude will follow, each with its
  provenance (Core ARPD, PI, project-derived, agent-recommended) and status.
- **A 14-section Project Definition Report** (intake, research context and traceability,
  constraints and commitments, scope and priorities, requirements, architecture, decisions, data,
  verification, roadmap, development process and rules, open decisions, what adoption authorizes).
  `check_report.py` checks both the new and the older 13-section layout, and adds the dependency
  and correctness-critical safeguards.
- **`/arpd-plan` asks the PI's goal first** (or recommends one on request), then sizes the effort:
  a targeted task, a feature, a sprint, several sprints, or a **bounded feasibility investigation**
  whose deliverable is a finding, not product code. A goal that departs from the roadmap is said to,
  with what it displaces; the roadmap is the record of direction, not proof it is right.
- **Python is optional.** Without Python 3.8+, `arpd/tools/install.sh` (a shell twin of
  `install.py`) does the file work, the agents read the report and records instead of running the
  checkers (and say so, never reporting a PASS), and the event log is not kept
  ([arpd/docs/NO-PYTHON.md](arpd/docs/NO-PYTHON.md)).
- **Resuming older notes:** v0.4–v0.6 notes are mapped onto the new phases; an old theory choice
  becomes the scientific axis; old scope answers become the starting point for priorities, never
  asked again.

## Install

Requirements: Claude Code (tested with 2.1.220) and Git with `user.name` and `user.email` set.
Python 3.8+ is recommended (the automated checks and the event log), not required.

```bash
git clone <repository URL> my-project
cd my-project
claude
```

Then type `/arpd-setup`. Details: [arpd/docs/GUIDE.md](arpd/docs/GUIDE.md).

## Upgrading a project set up with v0.6

Nothing forces a change: an adopted v0.6 project keeps working, and its 13-section report still
passes `check_report.py`. To take the new skills and templates, run
`python <a fresh kit clone>/arpd/tools/install.py update <project>` and commit; the charter changes
only by the PI's ruling, through `/arpd-amend` (for example to add the sprint-autonomy line). A setup
interrupted under v0.6 resumes under v0.7 from its notes.

## Upgrading a project set up with v0.5 or earlier

- **Keep the old layout.** Nothing forces a change. The project's own `tools/` and `logs/` keep
  working. The v0.6 tools also accept the older layout: they fall back to `logs/events.jsonl`, to
  `INDEX.md` when `START-HERE.md` has no *Map*, and to hooks in `tools/hooks/`.
- **Or move to the v0.6 layout.** Add the folder with
  `python <kit>/arpd/tools/install.py install <project>` (it reports the older skills as conflicts;
  add `--force` to replace them; later refreshes use `update`), run
  `python arpd/tools/install.py owed .` to point the hooks at `arpd/tools/`, then use `/arpd-amend`
  to change the paths the charter names. The charter changes only by your ruling. Commit, then
  remove the old kit leftovers (`docs/arpd-kit/`, `examples/`, `evaluation/`, root `kit/`, `tools/`,
  `reports/templates/`, `docs/EVENTS.md`) in one remove-only commit, recorded by a DEC under your
  upgrade instruction.

## Known limitations

See [docs/LIMITATIONS.md](docs/LIMITATIONS.md). New in this candidate: the phased interview has
been exercised only in scripted driven runs (`evaluation/developer-tests/v0.7-runs-report.md`), not
yet by a researcher; the no-Python path's read-throughs are weaker than the checkers they replace;
Claude Code documents no mid-session reload of `CLAUDE.md` except `/compact`, so `/arpd-plan` makes the
loaded charter (and the agent roles) a prerequisite for implementation; this was checked in scripted
runs, where each turn is a new process, and still needs the interactive walkthrough.

## Licence

The repository is released under the [MIT License](LICENSE), one licence for the original code,
documentation, templates, charter text and skills. The README's licence section gives the scoped
permission for documents ARPD generates for a researcher's project, and the exceptions: short
quotations from published works, which remain their owners'. There is no third-party code. Citation
is requested in [CITATION.cff](CITATION.cff), separately from the licence terms.

### The PI's licence ruling (verbatim)

> I choose the standard MIT licence for the repository’s original code, documentation, templates,
> charter text, and skills. Use one licence across those materials rather than splitting them
> between MIT and Creative Commons.
> Add the standard LICENSE file and update the README and release documentation. Preserve any
> applicable third-party notices and identify exceptions if they exist.
> Include a brief request for academic citation using confirmed information. Keep that request
> separate from the standard MIT terms. Respect the current anonymous-review requirements.
> Record this as my licence ruling. No additional confirmation is needed.

## Before a public release

- Complete the manual walkthrough and the v0.7 usability protocol with at least one researcher.
- Run the no-Python path end to end on a machine without Python.
- Confirm copyright ownership and the holder named in `LICENSE` (during anonymous review, "The ARPD
  authors"); then replace the anonymous author in `CITATION.cff` and add the framework paper.

## History

Each earlier candidate is preserved under its tag.

- `v0.3.0-rc.1` (2026-10-16): the charter, governing documents, setup in three modes, check-in,
  amendment, event logging and the governance checker; developer tests DT-01 to DT-08.
- `v0.4.0-rc.1` (2026-10-17): adaptive setup ending with planning pending; `/arpd-plan`; shared
  interaction conventions; readiness; developer tests DT-09 to DT-13.
- `v0.5.0-rc.1` (2026-10-18): tool-first setup with scope questions, architecture alternatives and an
  adopted Project Definition Report; data semantics reserved to the PI; driven scenarios A to H.
- `v0.6.0-rc.1` (2026-10-18): every project its own repository (setup in the kit, then a relaunch);
  one `arpd/` payload folder; `install.py`; the example extracted; driven runs N, I, M, M2.
