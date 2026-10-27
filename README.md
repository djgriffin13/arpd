# ARPD: Agentic Research Paradigm Development

ARPD lets a researcher who is not a software developer direct a team of AI coding agents (in Claude
Code) to build a research tool, **while keeping authority over every consequential decision**. It is
a team charter, document templates and four Claude Code skills (`/arpd-setup`, `/arpd-plan`,
`/arpd-checkin`, `/arpd-amend`). It is the research artifact for a proposal to the *Organization
Science* special issue "AI-Enabled Frontiers in Organizational Science." This is a release
candidate ([RELEASE-NOTES.md](RELEASE-NOTES.md)).

**To try it:** follow **Start here** below (about 15 minutes), then **[TUTORIAL.md](TUTORIAL.md)**,
which walks you prompt by prompt through using ARPD to build a small Spades card game.

## Start here

### 1. What you need

- A Claude **Pro, Max, Team or Enterprise** plan, or a **Claude Console (API)** account. The free
  Claude plan does not include Claude Code.
- Windows 10 or later, macOS 13 or later, or a recent Linux.
- Time for the tutorial: *[to be measured]*, much of it the agents working while you wait.
  Agent use: *[to be measured]*.

### 2. Install Git

- **Windows:** download and install Git for Windows from <https://git-scm.com/downloads/win>
  (the default options are fine). Claude Code also uses the Git Bash it includes.
- **macOS:** open Terminal and run `git --version`. If Git is missing, macOS offers to install the
  command-line tools; accept.
- **Linux:** install `git` with your package manager.

Then tell Git your name and email (any values you like; they label your own commits):

```bash
git config --global user.name "Your Name"
```

```bash
git config --global user.email "you@example.com"
```

### 3. Install Claude Code

Use Anthropic's installer. Commands from <https://code.claude.com/docs/en/setup>:

- **macOS / Linux** (Terminal):

  ```bash
  curl -fsSL https://claude.ai/install.sh | bash
  ```

- **Windows** (PowerShell):

  ```powershell
  irm https://claude.ai/install.ps1 | iex
  ```

Open a **new** terminal window and check that it worked:

```bash
claude --version
```

If `claude` is not found, see <https://code.claude.com/docs/en/troubleshoot-install>.

### 4. Check Python and its window toolkit

The tutorial builds a small windowed game in Python with Tkinter, which comes with most Python
installations.

- **Windows** (PowerShell): run `py --version`, then `py -m tkinter`.
- **macOS / Linux**: run `python3 --version`, then `python3 -m tkinter`.

The second command should open a small test window; close it. If Python is missing, install it
from <https://www.python.org/downloads/>. Some Linux and Homebrew Pythons ship without Tkinter; add
it with your package manager (for example `python3-tk` on Ubuntu, `python-tk` on Homebrew).

*Without Python (untested):* you can still follow the tutorial, but in your first message to ARPD
replace "Use Python with its built-in Tkinter" with a language you have (for example R). The game
will then be built differently, and the run commands later in the tutorial will not apply.

### 5. Get ARPD

Clone the repository into a new folder named `spades-demo` and go into it:

```bash
git clone <URL of this repository> spades-demo
```

```bash
cd spades-demo
```

If you have a ZIP download instead, unzip it, rename the folder `spades-demo` if you like, and
open a terminal in that folder. ARPD works the same either way.

### 6. Start Claude Code

In that folder, run:

```bash
claude
```

The first time, Claude Code opens your browser to log in. When it asks whether you trust the files
in this folder, answer **Yes**. You now see Claude Code's prompt.

### 7. Open the tutorial

Open **[TUTORIAL.md](TUTORIAL.md)** in your web browser (on the repository's page) and keep it open
beside the terminal. Read it there, not in the folder: early in the tutorial, ARPD turns this folder
into your project and moves its own files, including this README and the tutorial, into a backup
folder beside it.

## What ARPD is for

Which questions organizational researchers can pursue is limited by the cost of building,
validating and maintaining research instruments: experimental platforms, measurement systems,
statistical tools and computational models. AI coding agents can lower those costs. But agent-built
software can pass its own checks while measuring the wrong construct, and those who most need the
help are least able to see that. ARPD's answer is to organize the agents as a team the researcher
leads: a charter, explicit decision authority, independent review and testing, and scientific
validation as core pillars.

The design draws on team science: process phases (Marks, Mathieu & Zaccaro, 2001), team charters
(Mathieu & Rapp, 2009), coordination mechanisms (Okhuysen & Bechky, 2009), functional leadership
(Morgeson, DeRue & Karam, 2010), reflexivity (Schippers, West & Dawson, 2015) and the human–LLM
agent-team guidelines of Yurrita et al. (2026). Evaluations of multi-agent systems report mixed
results (Kim et al., 2026; Gloaguen et al., 2026). **We do not claim the kit overcomes them.** Its
benefits are proposed, not yet tested. [docs/DESIGN-RATIONALE.md](docs/DESIGN-RATIONALE.md) maps
each mechanism to its sources.

## Using ARPD for your own project

The tutorial's steps work for any project: run `/arpd-setup` in a fresh copy and describe what you
want to build. Setup can also add ARPD to an existing repository in place (its history and remote
kept), start a new folder, or start from existing code (`/arpd-setup import <path or git URL>`).
The full guide travels with every project: [arpd/docs/GUIDE.md](arpd/docs/GUIDE.md).

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

A checked implementation of March's (1991) mutual-learning model, built as an ARPD project, is kept
in its own repository and is not part of this one.

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
