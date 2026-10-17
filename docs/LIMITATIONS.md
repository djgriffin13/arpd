# Known limitations (as of 2026-10-16)

These are stated openly so that users and reviewers know what the kit does and does not establish.
Most come from the independent review rounds and the developer tests in `evaluation/developer-tests/`.

## Setup and use

- **The interactive interview has not been run with a person.** The four developer tests used
  scripted answers. Two real `/arpd-setup` runs (DT-02 to DT-04) exercised the skill end to end, but
  not the interview's length, clarity or feel.
- **`.claude/` writes need an interactive approval.** Installing the event-logging hooks and the
  implementer and reviewer roles requires a click on Claude Code's permission prompt. A scripted run
  cannot give it; setup then records the gap as owed and gives the researcher the exact commands to
  run. The approval flow itself has not been exercised live.
- **One harness.** The kit targets Claude Code. The charter is plain Markdown and `AGENTS.md` points
  other tools to it, but other harnesses are untested.
- **Draft modules.** Only the computational-model and team-arrangement modules have been used. The
  statistical-methods, experiment-platform, measurement-pipeline, simulated-agents and
  human-subjects modules are labelled untested drafts.
- **Charter length.** The core charter is about 2,900 words. It is meant to stay lean, so rules
  that no longer earn their cost should be retired.

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
- **Open sprints are not checked.** Decision tracking is checked only in closed sprint records. Each
  run lists the open sprint records it found under *Not checked*.
- **Records, not facts.** The checker relies on what is recorded in DECISIONS.md, the sprint
  records, REQUIREMENTS.md and INDEX.md. Within the steps it lists, it does not report PASS for an
  item it could not check; it cannot show that the records are true. It does not run the project's
  tests.
- **Installation checks** look at file presence and content. They do not show that the hooks
  actually fired.
- **Charter adoption** is read from the charter's Version line and the existence of the ruling it
  names. The checker cannot confirm that the ruling is in the researcher's own words.

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
