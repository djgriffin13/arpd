# ARPD: Agentic Research Paradigm Development

**A team-based framework for expanding organizational inquiry.** This is a release candidate (v0.3.0-rc.1,
October 2026), held for manual testing ([RELEASE-NOTES.md](RELEASE-NOTES.md)), and the research artifact for a proposal to the *Organization Science* special issue
"AI-Enabled Frontiers in Organizational Science."

## What it is for

Which questions organizational researchers can pursue is limited by the cost of developing,
validating, maintaining and coordinating research instruments: experimental platforms, measurement
systems, statistical tools and computational models. AI coding agents can lower those costs. But
agent-built software can pass its own checks while measuring the wrong construct, and those who most
need the help are least able to see that.

ARPD lets a domain researcher who is not a software developer direct a **team** of AI agents to
build and revise a research instrument, **while keeping authority over every consequential
scientific decision**. Testing, review and explicit scientific validation are its core pillars.

## The parts

| Part | What it does | Status |
|---|---|---|
| **Team charter** (`kit/constitution/CORE.md` → the project's `CLAUDE.md`) | A short governing document every agent reads each session. It covers: authority by subject; the PI's rulings recorded verbatim; decision routes set by scientific consequence and by the authority the researcher has delegated, with an authority profile (consult first, bounded autonomy, or exploratory autonomy) agreed at setup; requirement states that separate *Implemented*, *Verified* (software evidence) and *Validated* (scientific evidence the researcher accepts); sprints with auditable close-outs; and a learning loop that adds and retires rules. | Built |
| **Paradigm specification** (`kit/templates/PARADIGM-SPEC.md`) | Traces the research question → constructs → operationalizations → invariants → claims, and claims not to make → validation evidence. | Built |
| **Setup and import interview** (`/arpd-setup`) | Asks about the science and proposes the engineering. Supports a fresh project, importing a codebase, or installing into an existing repository. Prior instructions are preserved and reconciled by decision, never silently merged. | Built; run end to end in real scripted developer tests of fresh mode (DT-03), import mode (DT-02, DT-04) and install mode (DT-05, and DT-08 for an interrupted install). The interactive interview has not yet been tested with a researcher. |
| **Team and workspace arrangement** | The team (solo / lead with subagents / peers) and the workspace (shared checkout / worktrees) are chosen separately. Shared runtime resources (ports, output paths) are assigned per agent. | Built |
| **Event logging** (hooks + `tools/`) | Records defined coordination events. It reports elapsed time, agent-working time (prompt to end of turn), subagent time and failed or interrupted turns, separately from the researcher's self-reported active time. Hooks cannot measure the researcher's active time, and the tooling says so. | Built |
| **Governance checker** (`tools/check_governance.py`) | Checks, from what is recorded: links, requirement evidence and traceability, plan numbering, charter adoption, installation files, and whether consequential decisions in closed sprints were authorized before adoption. Within the steps it lists, it does not report PASS for an item it could not check; each run prints what it did not check. It cannot show that the records themselves are true. | Built |
| **Modules** (`kit/constitution/modules/`) | Built: computational model; team arrangement. Drafts, untested: statistical methods, experiment platform, measurement pipeline, agents inside instruments, human-subjects data. | Partial |
| **Worked example** (`examples/march-1991/`) | A checked implementation of March's (1991) mutual-learning model, kept as a complete ARPD project with its records. It is also the starter for the feasibility demonstration. | Built: software verification (48 tests) and directional replication (22 tests), with two independent review rounds. Its assumptions were adopted as the working baseline by the PI's ruling R-01; whether they match March's own program remains open (backlog B-07 to B-09). |

## Why a team, and why a charter

The design draws on team science:

- team process phases (Marks, Mathieu & Zaccaro, 2001);
- team charters (Mathieu & Rapp, 2009);
- coordination mechanisms (Okhuysen & Bechky, 2009);
- functional leadership (Morgeson, DeRue & Karam, 2010);
- team reflexivity (Schippers, West & Dawson, 2015);
- the human–LLM agent-team guidelines of Yurrita et al. (2026). `docs/DESIGN-RATIONALE.md` maps the
  kit's mechanisms to them.

Evaluations of multi-agent AI systems report mixed results. Whether added agents help depends on the
task (Kim et al., 2026), and added governance can cost more than it returns (Gloaguen et al., 2026).
Those evaluations test particular architectures, not a researcher-directed arrangement built on team
science.

**We do not claim the kit explains or overcomes those results.** We treat it as a hypothesis, and
the kit doubles as a **test bed**: the same task can be run solo or with several agents, with or
without the charter, and with lean or full configurations. See `evaluation/`.

## Quick start

See [QUICKSTART.md](QUICKSTART.md). In short: clone, open in Claude Code, and type `/arpd-setup`.
Installation, hook permissions, confirming that logging works, recovery after a lost session, and how
to read the governance check are in [docs/OPERATIONS.md](docs/OPERATIONS.md).

**Requirements:** Claude Code (tested with 2.1.220), Git, and Python 3.8+ on the PATH as `python`.
The March example also needs numpy and pytest. The charter is plain Markdown. `AGENTS.md` points
other agent tools to it, and adapters for other tools are planned.

## Supported workflows and evidence

The developer tests are labelled developer evidence with scripted inputs, not demonstrations with a
researcher. Records are in [`evaluation/developer-tests/`](evaluation/developer-tests/).

| Workflow | Evidence | Status |
|---|---|---|
| Fresh setup (`/arpd-setup`) | DT-03 | Run end to end; `.claude/` writes needed an interactive approval and were recorded as owed |
| Import (`/arpd-setup import`), including a starter inside the kit | DT-02, DT-04 | Run end to end |
| Install into an existing repository (`/arpd-setup install`) | DT-05, DT-08 | Run end to end; DT-05's missing-skills defect fixed; DT-08 resumed an interrupted install in a new session |
| Check-in and amendment (`/arpd-checkin`, `/arpd-amend`) | DT-06, DT-07 | DT-06's defects fixed and re-run in DT-07 |
| Event logging and recovery after a lost session | DT-01, addendum 2 | Real sessions; hook capture and recovery checked |

## Tested and draft components

| Tested | Draft or untested |
|---|---|
| Charter, governing-document templates and the three skills (setup in all three modes, check-in, amendment), in scripted developer tests | Every workflow with a real researcher, and approving the `.claude/` writes interactively |
| Governance checker and event summary: 95 automated tests in `kit/tools/`, and seven independent review rounds | The interactive interview with a real researcher |
| Event-logging hooks and recovery, in real Claude Code sessions | Draft modules: statistical methods, experiment platform, measurement pipeline, agents inside instruments, human-subjects data |
| Modules: computational model; team arrangement | Other agent harnesses than Claude Code |
| The March (1991) worked example: 70 tests, two independent review rounds | The `StopFailure` hook's payload fields, against a real failure |

Known limitations are listed in [docs/LIMITATIONS.md](docs/LIMITATIONS.md).

## Layout

| Path | Contents |
|---|---|
| `.claude/skills/` | `arpd-setup` (interview and import), `arpd-checkin`, `arpd-amend` |
| `kit/constitution/` | `CORE.md` (charter template) and `modules/` |
| `kit/templates/` | Governing-document and report templates |
| `kit/agents/` | Implementer and reviewer role definitions |
| `kit/tools/` | Governance checker, plan numbering, event logging and summary, hook script |
| `kit/settings/` | Hook configuration installed into projects |
| `kit/docs/EVENTS.md` | What the event log captures, and what it cannot |
| `examples/march-1991/` | The worked example |
| `evaluation/` | Protocols for the feasibility demonstration and the planned studies; `developer-tests/` holds the labelled developer-test records and their scripted inputs |
| `docs/` | Operations guide (`OPERATIONS.md`), manual-testing guide (`MANUAL-TESTING.md`), known limitations (`LIMITATIONS.md`), design rationale and references |

## Evidence status

The kit's rules come from practice: the governing records of three agent-built research instruments,
reorganized around team-science theory. **Their benefits are proposed, not yet tested.** Testing them
is what `evaluation/` is for.

## Licence

The whole repository is released under the [MIT License](LICENSE): code, documentation, templates,
skills, the governance framework and the worked example. `kit/LICENSE` is the same licence, kept
with the kit so that copies of it carry the notice; `kit/README.md` repeats the permission below for
generated documents, so it travels with every installed project.

**Documents generated for your project.** The files that ARPD's setup and skills write for your own
project are yours. This covers your team charter (`CLAUDE.md`), `PARADIGM-SPEC.md`,
`REQUIREMENTS.md`, `MASTER_PLAN.md`, `DECISIONS.md`, `ARCHITECTURE.md`, `STATUS.md`, `INDEX.md`,
`START-HERE.md`, your sprint records and reports, and your research instrument. You may use, modify,
distribute or keep them private, under any terms, without having to credit ARPD. They are covered
even where they are adapted from ARPD's templates.

**The framework itself.** Redistributing ARPD, or substantial portions of its own source materials
(for example `kit/`, the skills in `.claude/skills/`, or the tools copied into a project's `tools/`),
carries the normal MIT condition: keep the copyright and permission notice with them.

**Exceptions: third-party material.** The repository includes no third-party code. Short quotations
from published works, for example March (1991) and the other sources quoted in
`examples/march-1991/SOURCES.md` and `docs/DESIGN-RATIONALE.md`, are quoted for
scholarship and remain their owners'. The MIT License does not cover them. Dependencies such as
numpy and pytest are installed separately, under their own licences, and are not distributed here.

**Citation (a request, not a licence term).** If ARPD helps your research, please cite it
([CITATION.cff](CITATION.cff)) and, once it is available, the framework paper. Citation is
encouraged, not a condition of use.
