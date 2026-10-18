# Known limitations (release candidate v0.6.0-rc.1)

These are stated openly so that users and reviewers know what the kit does and does not establish.
The evidence behind them is indexed in [evaluation/README.md](../evaluation/README.md).

## Use with people

- **No workflow has been completed by a researcher.** All workflow evidence comes from developer
  tests with scripted answers and one manual test of an earlier version. None of it shows that a
  researcher can use the kit, or how long setup takes ("about 20–60 minutes" is an estimate).
- **Judgement, not checks.** Telling an interview answer from a ruling, a plan approval or a start;
  recognizing that an implementation choice changes data semantics; and asking the right question
  all rest on the model following the skills. When words are ambiguous, the skills record the
  narrower reading or ask.
- **Form checkers, not quality checkers.** The turn checker (`tests/check_turn.py`) checks a turn's
  shape: a labelled block last, choice options in the text, a progress line. The report checker
  (`arpd/tools/check_report.py`) checks a report's form: sections, acceptance criteria and status per
  requirement, a gate per open item, no adoption claimed by a draft. Neither judges whether the
  requirements, criteria or alternatives are good. The progress line is still sometimes omitted.
- **Architecture recommendations rest on the model's knowledge** unless documentation was checked.
  A session without web access cannot check, and must say "not verified".
- **Widgets and symbols.** The native choice widget is untested. The progress symbols may not
  render in some Windows output; the ASCII form is applied by judgement.

## New in v0.6

- **The relaunch step and `install.py` are new.** Creating the project folder, reopening Claude Code
  there and continuing the interview, and the `new`, `import`, `install`, `update` and `owed`
  commands, are covered by unit tests (`tests/test_install.py`). Driven runs with scripted answers covered
  a new project through `/arpd-plan`, check-in and amend, an install, and an import of the worked
  example (`evaluation/developer-tests/v0.6-runs-report.md`); no person has done the relaunch yet.
- **Windows paths and OneDrive.** Synced folders can lock or duplicate files while git and agents
  work; `install.py` warns but does not refuse. Paths with spaces need quotes. A folder above the
  project holding `CLAUDE.md` or `AGENTS.md` adds instructions Claude Code also reads; again a
  warning only.
- **Updates are manual.** `install.py update` copies the kit's current `arpd/` and skills into a
  project and commits nothing. It needs the path of a kit clone, and it never changes the governing
  documents; adopting a new charter rule is a ruling. A project set up before v0.6 has no `arpd/`
  folder and must add it with `install` first.
- **The worked example is local.** It lives in its own repository, not yet published. Its records
  are in the v0.3 format, so the checker reports some steps as "older format".

## Resuming and continuation

- Resuming an interrupted setup has been tested at a few points (just after adoption; before
  adoption from the notes, in three phases, with a draft report and with notes from an older kit).
  Other interruption points, and resuming an interrupted plan review, are untested.
- In install mode without consent to save notes in the repository, they are kept beside it, in
  `../.arpd-setup-notes/<name>/`, which the stub `CLAUDE.md` names; a later session resumes from there.
- The setup interview itself is not logged: the hooks are installed at the end of setup.
- Under a continuation standing authorization, the lead checks the transition conditions at each
  sprint boundary. The governance checker does not.

## Installation and harness

- **`.claude/` writes need an interactive approval.** A non-interactive run cannot give it; setup
  records the items as owed, to be finished with `python arpd/tools/install.py owed .`. The approval
  flow itself has not been exercised live.
- **One harness.** The kit targets Claude Code. The charter is plain Markdown and `AGENTS.md` points
  other tools to it, but other harnesses are untested.
- **Draft modules.** Only the computational-model and team-arrangement modules have been used. The
  statistical-methods, experiment-platform, measurement-pipeline, agents-in-instruments and
  human-subjects modules are untested drafts.

## Governance checker

- **Records, not facts.** It reads what is recorded. It cannot show that a date is true, that a
  ruling is in the PI's own words, or that the hooks fired; it does not run the project's tests.
- **Dates.** It compares ISO 8601 dates in `DECISIONS.md`, and gives MISSING when it cannot tie a
  date to the authority or order same-day events. Pending wording is recognised only at the start of
  an *Authorized* line. One given authority is enough even if another cited beside it is pending.
- **Open sprints** are checked only at Part 1: not whether the cited authority covers the sprint's
  scope, nor whether the approved plan file still matches the commit its ruling names.
- **Readiness** is compared with the records only on its *Execution* line, as an advisory step.

## Event logging

- Hooks capture only the events listed in `arpd/docs/EVENTS.md`.
- The PI's active time cannot be measured from the log; it comes from `pi_time` entries or coded
  recordings.
- The `StopFailure` payload's field names have not been verified against a real failure.

## The worked example

- It reproduces March's (1991) qualitative results in direction, not in level (mostly lower, by
  about 0.1 to 0.2 for equilibrium code knowledge). One headline result, the R2 reversal, depends on
  an incompletely specified update order.
- Its nine assumptions are the working baseline adopted by its ruling R-01. That adoption permits
  use and extension; it does not establish exact replication or scientific validation.

## Deferred backlog

- **Checker:** "Live items cite no superseded spec item" misses strikethrough, ID ranges
  (`CON-01–03`) and VAL rows citing a superseded claim; a "skills not installed" decision is
  accepted whatever its status; skills installed at user level are not detected; the checker does
  not confirm that each prior rule kept by decision appears in the charter.
- **Setup:** template `<!-- keep:` blocks were sometimes dropped.
- **Planning:** resuming an interrupted plan review is untested.
- **Fenced examples:** the skills show block layouts inside code fences, while a real block is plain
  text; the turn checker does not warn about a fenced block.
- **Worked example:** comparison with independent reconstructions and a systematic exploration of
  the assumptions (its backlog B-07 to B-09).
- **Modules:** the five draft modules stay drafts until tested.

## Evidence about effectiveness

The kit's mechanisms rest on team-science theory, adjacent evidence and practitioner records
([DESIGN-RATIONALE.md](DESIGN-RATIONALE.md)). **None has yet been shown to improve outcomes
compared with other workflows.** That is the purpose of the planned studies in `evaluation/`.
