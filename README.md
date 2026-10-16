# ARPD: Agentic Research Paradigm Development

**A team-based framework for expanding organizational inquiry.** This is a prototype (v0.2, October
2026), and the research artifact for a proposal to the *Organization Science* special issue
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
| **Setup and import interview** (`/arpd-setup`) | Asks about the science and proposes the engineering. Supports a fresh project, importing a codebase, or installing into an existing repository. Prior instructions are preserved and reconciled by decision, never silently merged. | Built; run end to end in two real scripted developer tests (import and fresh mode; `evaluation/developer-tests/`). The interactive interview has not yet been tested with a researcher. |
| **Team and workspace arrangement** | The team (solo / lead with subagents / peers) and the workspace (shared checkout / worktrees) are chosen separately. Shared runtime resources (ports, output paths) are assigned per agent. | Built |
| **Event logging** (hooks + `tools/`) | Records defined coordination events. It reports elapsed time, agent-working time (prompt to end of turn), subagent time and failed or interrupted turns, separately from the researcher's self-reported active time. Hooks cannot measure the researcher's active time, and the tooling says so. | Built |
| **Governance checker** (`tools/check_governance.py`) | Checks links, requirement evidence and traceability, plan numbering, and whether consequential decisions were authorized before adoption. | Built |
| **Modules** (`kit/constitution/modules/`) | Built: computational model; team arrangement. Drafts, untested: statistical methods, experiment platform, measurement pipeline, agents inside instruments, human-subjects data. | Partial |
| **Worked example** (`examples/march-1991/`) | A checked implementation of March's (1991) mutual-learning model, kept as a complete ARPD project with its records. It is also the starter for the feasibility demonstration. | Built: software verification (48 tests) and directional replication (22 tests), with two independent review rounds. Its assumptions await the researcher's decision. |

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

**Requirements:** Claude Code, Git and Python 3.8+. The charter is plain Markdown. `AGENTS.md`
points other agent tools to it, and adapters for other tools are planned.

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
| `evaluation/` | Protocols for the feasibility demonstration and the planned studies; `developer-tests/` holds the labelled developer-test records (DT-01 to DT-03) and their scripted inputs |
| `docs/` | Design rationale and guidance |

## Evidence status

Known limitations are listed in [docs/LIMITATIONS.md](docs/LIMITATIONS.md).

The kit's rules come from practice: the governing records of three agent-built research instruments,
reorganized around team-science theory. **Their benefits are proposed, not yet tested.** Testing them
is what `evaluation/` is for.

## Licence

To be decided before public release.
