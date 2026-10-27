# ARPD: Agentic Research Paradigm Development

**A team-based framework for expanding organizational inquiry.** This is release candidate
v0.7.0-rc.1, held for manual testing ([RELEASE-NOTES.md](RELEASE-NOTES.md)). ARPD is the research artifact
for a proposal to the *Organization Science* special issue "AI-Enabled Frontiers in Organizational
Science."

## What it is for

Which questions organizational researchers can pursue is limited by the cost of building,
validating and maintaining research instruments: experimental platforms, measurement systems,
statistical tools and computational models. AI coding agents can lower those costs. But agent-built
software can pass its own checks while measuring the wrong construct, and those who most need the
help are least able to see that.

ARPD lets a domain researcher who is not a software developer direct a **team** of AI agents to
build and revise a research instrument, **while keeping authority over every consequential
scientific decision**. Testing, review and explicit scientific validation are its core pillars.

The design draws on team science: process phases (Marks, Mathieu & Zaccaro, 2001), team charters
(Mathieu & Rapp, 2009), coordination mechanisms (Okhuysen & Bechky, 2009), functional leadership
(Morgeson, DeRue & Karam, 2010), reflexivity (Schippers, West & Dawson, 2015) and the human–LLM
agent-team guidelines of Yurrita et al. (2026). Evaluations of multi-agent systems report mixed
results (Kim et al., 2026; Gloaguen et al., 2026). **We do not claim the kit overcomes them.** Its
benefits are proposed, not yet tested; the kit doubles as a test bed.
[docs/DESIGN-RATIONALE.md](docs/DESIGN-RATIONALE.md) maps each mechanism to its sources.

## Quick start

You need Claude Code and Git (with your name and email set). Python 3.8+ is recommended: it runs the
automated checks and the event log; without it ARPD still works, with read-throughs in their place
([arpd/docs/NO-PYTHON.md](arpd/docs/NO-PYTHON.md)).

```bash
git clone <this repository> my-project
cd my-project
claude                      # then type /arpd-setup and say what you would like to accomplish
# setup turns this folder into your project, in place (a fresh git history, no remote),
# and interviews you in phases; adopt the Project Definition Report and it writes the
# governing documents
/arpd-plan                  # plan the first piece of work; work starts only when you say so
```

Setup can instead add ARPD to an existing repository in place (its history and remote kept), start
a new folder, or start a new folder from existing code (`/arpd-setup import <path or git URL>`).
Converting a clone moves ARPD's own files (this README, `docs/` and the rest listed in `.arpd-kit`)
to a backup folder beside the project.
The full guide for the PI travels with every project: [arpd/docs/GUIDE.md](arpd/docs/GUIDE.md).

## The parts

| Part | What it does |
|---|---|
| **Team charter** (`arpd/constitution/CORE.md` → the project's `CLAUDE.md`) | Authority by subject; data semantics reserved to the PI; rulings recorded verbatim; decision routes by scientific consequence and delegated authority; requirement states (*Implemented*, *Verified*, *Validated*); sprints with auditable close-outs; a learning loop |
| **Paradigm specification** (`arpd/templates/PARADIGM-SPEC.md`) | Research question → constructs → operationalizations → invariants → claims → validation evidence, to the depth the project needs |
| **Setup** (`/arpd-setup`) | A research-aware interview in phases (Intake, Objectives, Constraints, Design, Development), each with required answers and a summary the PI confirms, ending in a Project Definition Report the PI adopts; only then the governing documents. In place by default |
| **Planning** (`/arpd-plan`) | The PI's goal first; the effort sized (task, feature, sprint, series, feasibility investigation); a versioned draft, approval of an exact version, then begin now or later |
| **Check-in and amendment** (`/arpd-checkin`, `/arpd-amend`) | Where things stand and what needs the PI; rulings, standing authorizations and charter changes |
| **Tools** (`arpd/tools/`) | Project creation and updates (`install.py`), governance and report checkers, event logging and summary |
| **Modules** (`arpd/constitution/modules/`) | Built: computational model, team arrangement. Five untested drafts |

## A project's layout

| Path | Contents |
|---|---|
| `CLAUDE.md`, `AGENTS.md`, `START-HERE.md`, `PARADIGM-SPEC.md`, `REQUIREMENTS.md`, `ARCHITECTURE.md`, `MASTER_PLAN.md`, `DECISIONS.md`, `STATUS.md` | The governing documents, at the root. `START-HERE.md` holds the next step and the project's map |
| `reports/` | `setup/NOTES.md` and `setup/PROJECT-DEFINITION.md`; later `planning/` and `sprints/` |
| `plans/` | Task plans, created with the first one |
| `.claude/` | The `arpd-*` skills, the logging hooks and the agent roles |
| `arpd/` | Everything else from the kit, including the guide and the event log (`arpd/logs/`) |

The researcher's own code sits beside these.

## The worked example

A checked implementation of March's (1991) mutual-learning model is kept as a complete ARPD project
(v0.3-format records) in its own repository, `arpd-example-march1991`. It is local for now and will
be published later. To extend it, import it with `/arpd-setup import <path>`.

## Evidence and limitations

The kit's tools have automated tests, and its workflows have been exercised in scripted developer
runs and one manual test; those development records are kept outside this repository. **No
researcher has yet completed a workflow.** Known limitations are in [docs/LIMITATIONS.md](docs/LIMITATIONS.md).

## Licence

The whole repository is released under the [MIT License](LICENSE): code, documentation, templates,
skills and the governance framework. `arpd/LICENSE` is the same licence, kept in the folder that is
copied into every project; `arpd/README.md` repeats the permission below.

**Documents generated for your project.** The files that ARPD's setup and skills write for your own
project are yours. This covers your team charter (`CLAUDE.md`), `PARADIGM-SPEC.md`,
`REQUIREMENTS.md`, `MASTER_PLAN.md`, `DECISIONS.md`, `ARCHITECTURE.md`, `STATUS.md`,
`START-HERE.md`, the setup notes (`reports/setup/NOTES.md`), the Project Definition Report
(`reports/setup/PROJECT-DEFINITION.md`), your plans, sprint records and other reports, and your
research instrument. You may use, modify, distribute or keep them private, under any terms, without
having to credit ARPD. They are covered even where they are adapted from ARPD's templates.

**The framework itself.** Redistributing ARPD, or substantial portions of its own source materials
(for example the `arpd/` folder, including the copy in a project, or the skills in
`.claude/skills/`), carries the normal MIT condition: keep the copyright and permission notice with
them.

**Exceptions: third-party material.** The repository includes no third-party code. Short quotations
from published works, such as those in `docs/DESIGN-RATIONALE.md`, are quoted for scholarship and
remain their owners'. The MIT License does not cover them.

**Citation (a request, not a licence term).** If ARPD helps your research, please cite it
([CITATION.cff](CITATION.cff)) and, once it is available, the framework paper.
