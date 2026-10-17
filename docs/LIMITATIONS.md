# Known limitations (release candidate v0.4.0-rc.1, in development, 2026-10-17)

These are stated openly so that users and reviewers know what the kit does and does not establish.
Most come from the independent review rounds and the developer tests in `evaluation/developer-tests/`.

## Setup, planning and use

- **No workflow has been run by a researcher.** Every developer test used scripted answers.
  DT-01 to DT-08 were run on v0.3.0-rc.1: real `/arpd-setup` runs in fresh, import and install modes,
  and real `/arpd-checkin` and `/arpd-amend` sessions. The v0.4 developer tests (DT-09 to DT-13) ran the
  adaptive setup and `/arpd-plan` with scripted answers; 3 of 67 waiting turns broke the
  question-last rule, so placement still depends on the model following it. None of this tests the interview's length, clarity or feel, or whether a researcher
  can use the kit (`docs/MANUAL-TESTING.md`).
- **The new parts are untested with people.** The adaptive setup interview, the guided tutorial,
  `/arpd-plan`, the interaction conventions (`kit/docs/INTERACTION.md`) and the v0.4 changes to
  check-in and amendment have been exercised, at most, in scripted developer tests.
- **The setup time is an estimate.** "30–60 minutes, depending on how much scientific help you ask
  for" has not been measured with a researcher.
- **The interaction rules are only partly checkable automatically.** A turn checker for the scripted
  tests (`evaluation/developer-tests/check_turn.py`) checks the form of a turn: that it ends with a
  labelled block, that a choice block's options are printed in the text, and that the setup or plan
  progress line is present. It cannot judge whether the question is the right one, whether the topic
  list is honest, whether the tutorial helps, or whether one answer really closed several topics.
  Those rest on the model following the skill, and on manual testing.
- **Native choice widgets are untested.** The skills print every option in text before opening a
  widget, so the transcript stays readable if the widget vanishes. How the widget itself behaves, in
  the Claude Code terminal and in the Claude app, has not been tested.
- **Symbols may not render everywhere.** The progress lines and dividers use Unicode (✓ ● ○ ◉ ─).
  Some redirected Windows output does not show them. `INTERACTION.md` gives an ASCII form, but the
  agent applies it by judgement; neither form has been checked by a person on both surfaces.
- **Telling an answer from an authorization is a judgement.** The skills distinguish an interview
  answer, a proposal, a ruling, a plan approval and an execution authorization. When the words are
  ambiguous, they record the narrower reading (for example, planning approval only) or ask. Whether
  the agent reads a researcher's words correctly has not been tested with people.
- **Resuming is tested at few points.**
  - An interrupted setup was resumed once, with the interruption just after the adoption ruling was
    committed (DT-08, on v0.3).
  - Resuming before adoption, from the working notes in `docs/discovery/SETUP.md`, is new and under
    test (DT-13).
  - In install mode without consent to save notes, the notes stay outside the repository. A later
    session can resume from them only if the researcher gives their path.
  - Resuming an interrupted plan review from `reports/planning/` has not been tested.
  - Other interruption points are untested.
- **Working notes keep the researcher's words.** In fresh and import modes, and in install mode with
  consent, the notes are committed at adoption, in their own commit. They are never pushed without
  the researcher's authorization, but once committed they stay in the repository's history.
- **Multi-sprint continuation rests on the lead's checks.** Under a continuation SA, the lead checks
  the transition conditions at each sprint boundary. The governance checker does not check them, and
  the SA path has been exercised only in scripted tests.
- **`.claude/` writes need an interactive approval.** Installing the event-logging hooks, the
  implementer and reviewer roles and (in install mode) the skills requires a click on Claude Code's
  permission prompt. A scripted run cannot give it; setup then records the gap as owed and gives the
  researcher the exact commands to run. The approval flow itself has not been exercised live.
- **One harness.** The kit targets Claude Code. The charter is plain Markdown and `AGENTS.md` points
  other tools to it, but other harnesses are untested.
- **Draft modules.** Only the computational-model and team-arrangement modules have been used. The
  statistical-methods, experiment-platform, measurement-pipeline, simulated-agents and
  human-subjects modules are labelled untested drafts.
- **Charter length.** The core charter is about 3,100 words, up from about 2,900 in v0.3. It is meant
  to stay lean, so rules that no longer earn their cost should be retired.

## Governance checker (`tools/check_governance.py`)

- **Timing evidence.** The checker compares ISO 8601 dates recorded in DECISIONS.md. It gives MISSING,
  not a verdict, when:
  - a date is in another format;
  - several dates on one line can't be tied to the authority;
  - same-day order would need times that aren't recorded.

  **It cannot confirm that the recorded dates are true.** That rests on the decision records and the
  event log.
- **Pending wording** is recognised only at the start of an Authorized line.
- **Thin decision entries.** An entry with no Authorized or Adopted line falls back to the sprint row.
  A missing entry is reported as ADVISORY.
- **Several cited authorities.** One given ruling or standing authorization is enough, even if
  another one cited alongside it is still pending.
- **Open sprints are checked only at Part 1.** Decision tracking is checked only in closed sprint
  records. In an open sprint, the checker reads only the Part 1 rows *Approved plan*, *Execution
  authorized by* and *Transition policy*: the rulings and SAs they cite must exist and not be
  pending, and the plan file and version must exist. It does not check that the cited authority
  covers the sprint's scope, or that the plan file still matches the commit its ruling names. Older
  records without these rows get an ADVISORY.
- **Readiness is not checked.** The *Readiness* block in `STATUS.md` (setup, planning, execution,
  next step) is listed under *Not checked*. `/arpd-checkin` cross-checks it against the records, by
  reading them.
- **Records, not facts.** The checker relies on what is recorded in DECISIONS.md, the sprint
  records, REQUIREMENTS.md and INDEX.md. Within the steps it lists, it does not report PASS for an
  item it could not check; it cannot show that the records are true. It does not run the project's
  tests.
- **Installation checks** look at file presence and content. They do not show that the hooks
  actually fired.
- **Charter adoption, plan approvals and start directions** are read from the records. The checker
  cannot confirm that a ruling is in the researcher's own words.

## Event logging

- Hooks capture the events listed in `docs/EVENTS.md`, and only those.
- **Active researcher time cannot be measured from the log.** It comes only from the researcher's own
  `pi_time` entries, or from coded screen recordings in studies.
- The StopFailure payload's field names have not been verified against a real failure.

## The March (1991) worked example

- The model reproduces March's qualitative results **in direction**, not in level. Levels are mostly
  lower, by about 0.1 to 0.2 for equilibrium code knowledge, and higher in places. Several figure
  shapes differ.
- One headline result, the R2 reversal, depends on an incompletely specified update-order choice.
- Its nine assumptions were adopted as the working baseline by the PI's ruling R-01, with their
  discrepancies and limitations retained. Adoption permits use and extension; it does not establish
  exact replication or scientific validation.
- Comparisons with independent reconstructions and a systematic exploration of the assumptions are
  planned exploratory work (backlog B-07 to B-09).

## Evidence about effectiveness

The kit's mechanisms rest on team-science theory, adjacent empirical evidence and practitioner
records (`docs/DESIGN-RATIONALE.md`). **None has yet been shown to improve outcomes compared with
other workflows.** That is the purpose of the planned studies in `evaluation/`.
