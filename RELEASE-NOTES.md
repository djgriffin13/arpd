# Release notes: ARPD v0.5.0-rc.1 (release candidate, in preparation)

**Status: in preparation on the branch `setup-revision`. Not yet tagged, and not a final release.**
The tag `v0.5.0-rc.1` will mark the reviewed and tested commit; `git rev-parse v0.5.0-rc.1^{commit}`
will print it. A final release follows only after people have completed the manual tests in
[docs/MANUAL-TESTING.md](docs/MANUAL-TESTING.md) and any blockers they find are fixed.

**Earlier candidates are preserved** under their tags: `v0.4.0-rc.1` (summarized at the end) and
`v0.3.0-rc.1`. This candidate revises setup after the first manual test of v0.4
(`evaluation/manual-tests/MT-2026-10-17-1-findings.md`): its opening and theory questions were
oriented to scientific discovery when the researcher wanted a simple tool, its tutorial mode slowed
the interview, engineering alternatives were barely explored, and its read-back was too short to
serve as a specification.

## What ARPD is

A team-charter kit and four Claude Code skills (`/arpd-setup`, `/arpd-plan`, `/arpd-checkin`,
`/arpd-amend`). A domain researcher who is not a software developer uses them to direct a team of AI
coding agents building a research instrument, while keeping authority over every consequential
scientific decision. See [README.md](README.md).

## Install

Requirements: Claude Code (tested with 2.1.220), Git, and Python 3.8+ on the PATH as `python`. The
March example also needs numpy and pytest.

```bash
git clone <repository URL> my-project
cd my-project
git checkout v0.5.0-rc.1
claude
```

Then type `/arpd-setup` (a new project), `/arpd-setup import <path or URL>` (bring code into this
repository) or `/arpd-setup install <path>` (install into your own repository). When setup is done,
type `/arpd-plan` to plan the first sprint. Details: [QUICKSTART.md](QUICKSTART.md) and
[docs/OPERATIONS.md](docs/OPERATIONS.md).

## Upgrading a project set up with v0.4 or earlier

- A project already set up keeps working. Its charter changes only by your ruling (`/arpd-amend`).
  The new data-semantics rule (`CLAUDE.md` §6) and the SA-01 data-semantics line apply to an
  existing project only if you adopt them that way.
- `/arpd-plan` no longer has a tutorial mode. A mode recorded in `STATUS.md` §8 is ignored, and the
  skill says so once.
- An interrupted setup begun with v0.4 resumes from its working notes: the "Interview mode" line is
  ignored and marked "(obsolete; ignored)", the old phases map to the new ones, and no answer is
  lost (`docs/OPERATIONS.md` §9).

## What changed since v0.4.0-rc.1

**Setup (`/arpd-setup`) is tool-first.**

- Five visible phases: Project → Requirements → Architecture → Team & Governance → Definition Report.
- The first question, after a quick inspection, asks what the researcher would like to build. The
  interview-mode, research-maturity, coding-experience and profile questions are gone; the agent
  infers how much to explain.
- Three scope questions, each asked once: the minimum usable version, the ideal version (features of
  interest named), and nice-to-have features not expected in the first release. They set requirement
  priority (required, desired or future, later).
- Theory is optional. When it is relevant, the researcher chooses how the team treats it: use it to
  guide implementation without evaluating it, identify concerns, help develop it, or leave it aside.
  The full paradigm-specification method applies only when chosen, when correctness depends on it
  (estimators, simulations, models), or on request. A data-collection tool is not taken through
  constructs.
- Requirements discovery covers workflows, functional and nonfunctional requirements, data and
  persistence, and future direction, as a menu of coverage domains, not a questionnaire.
- Architecture: for each material decision, the credible alternatives, their trade-offs, a
  recommendation with reasons, and the consequences. Existing tools that would avoid custom software
  are considered. A claim about a technology is checked in its documentation or marked "not
  verified".
- The short read-back is replaced by the **Project Definition Report**
  (`reports/PROJECT-DEFINITION.md`), described below.
- Setup still ends with planning pending and never builds anything. Expected length: about 20–60
  minutes, depending on complexity.

**The Project Definition Report.** A new template, `kit/templates/reports/PROJECT-DEFINITION.md`:

- versioned, with a DRAFT banner until the researcher adopts a version;
- sections 1–12 (overview, product and workflows, functional and nonfunctional requirements,
  architecture, alternatives and decisions, data and interface contracts, verification, roadmap,
  team, authority and governance, risks and open decisions) and §13 *What adoption authorizes*; a
  section that does not apply is one line, and detail scales with complexity and risk;
- requirements as `REQ-<AREA>-NN` (nonfunctional ones `REQ-NFR-NN`), each with acceptance criteria,
  priority, dependencies, source and status;
- statuses mapped onto the kit's existing mechanisms: Adopted-on-adoption, Proposed, Provisional,
  Delegated (SA-NN), Open (with a gate: before planning, before implementing something named, or
  before deployment), Excluded;
- a completeness check, filled in before the report is presented.

Adoption is a ruling, R-01, in the researcher's words, with `Adopts: reports/PROJECT-DEFINITION.md
vN`; the report is committed with it in the adoption-first commit. Adoption authorizes the governing
documents only. Implementation still needs an approved plan and a start direction (`/arpd-plan`).
After adoption the report is kept as the record; the governing documents carry its content and win
where they differ.

**Charter (`CORE.md`).** §6 lists **data semantics** as consequential: missing versus zero,
duplicate or repeated observations, identifier meaning, aggregation, numerical precision or
estimation assumptions, changes to collected variables, replacement of unavailable data. Agents
choose implementation mechanisms, never these semantics, unless a ruling or an SA names the policy.
§2 lists the setup report as deciding nothing.

**Templates.**

- `REQUIREMENTS.md`: a *Requirement details* section (acceptance criteria, priority, dependencies
  per requirement); the requirements table is unchanged.
- `ARCHITECTURE.md`: an *Architecture decisions* table, in the report's columns; only Adopted,
  Delegated or Provisional rows, each labelled.
- `DECISIONS.md`: R-01 cites the adopted report version; SA-01 has a data-semantics line ("never
  delegated unless a named policy"); *Needed by* is the open item's gate.
- `STATUS.md`: no interview mode in §8; *Readiness* names the adopted report.
- `MASTER_PLAN.md`: the roadmap comes from the report.
- Setup working notes: the new phases, classification, theory context, the three scope tiers,
  architecture alternatives, candidate requirements with status, governance preferences, report
  version and state, and the compatibility rules for older notes.
- "Acceptance criterion" is explained the same way in `PARADIGM-SPEC.md`, `REQUIREMENTS.md`,
  `plans/README.md` and QUICKSTART: each requirement has its own; a task plan's are drawn from them.

**Interaction conventions (`kit/docs/INTERACTION.md`).** The tutorial overlay is removed kit-wide.
In its place, "Explain when needed": language suited to the researcher, engineering concepts
explained when a decision depends on them, trade-offs and a recommendation for consequential choices,
no repeated narration of the process, no questions just to establish expertise. The setup progress
line and its ASCII form are updated.

**Sprint planning (`/arpd-plan`).** No tutorial mode. At entry it reads the requirement details, the
architecture decisions and the adopted report (as context), and it respects each open item's gate
when planning. It does not re-ask scope.

**Documentation.** QUICKSTART, README, OPERATIONS and LIMITATIONS describe the new setup.
`docs/MANUAL-TESTING.md` is rewritten around two projects: a simple data-collection app (Scenario A)
and a computational estimator (Scenario B), plus checks for interruption and a change of scope.

**Developer-test tooling.** The turn checker accepts the new setup progress line. A report checker
(`evaluation/developer-tests/check_report.py`) checks a report's form: sections, acceptance criteria
and status per requirement, a gate per open item, no adoption claimed by a draft. Contract tests check
the skills and templates against the interface. Counts and results: to be filled.

## Supported workflows and evidence

Every developer test is a real Claude Code session with **scripted** researcher answers, audited by
an independent tester agent. Scripted responses are not evidence of human usability. None of these
workflows has yet been completed by a researcher.

| Workflow | Evidence | Status in this candidate |
|---|---|---|
| v0.5 setup: Scenario A (data-collection app, the manual test replayed), B (estimator), C (existing repository), D (scope correction), E (governance checks inside A–D), F (interrupt and resume, including old-format notes), G (report checks), H (handoff to `/arpd-plan`) | v0.5 scripted scenarios A–H: to be filled | Not yet run |
| `/arpd-plan`, check-in, amendment, import and install moves, owed `.claude/` items, event logging and recovery | DT-01 to DT-13 on v0.3 and v0.4 ([DT-09–13](evaluation/developer-tests/DT-09-13-report.md)) | Unchanged in their mechanics; the setup interviews in those tests are evidence for the earlier flows only |

## Tested and draft components

| Tested (with the evidence above) | Draft or untested |
|---|---|
| Charter, governing-document templates and the v0.3 and v0.4 skills, in scripted developer tests | Every workflow with a real researcher, including the v0.5 setup |
| Governance checker and event summary: automated tests in `kit/tools/`; independent review rounds 1 to 8b | The v0.5 setup and report (scripted scenarios to be filled) |
| Event-logging hooks and recovery, in real Claude Code sessions | Approving the `.claude/` writes interactively; native choice widgets and symbol rendering |
| Modules: computational model; team arrangement | Draft modules: statistical methods, experiment platform, measurement pipeline, agents inside instruments, human-subjects data |
| The March (1991) worked example: 70 tests; two independent review rounds | Other agent harnesses than Claude Code; the `StopFailure` hook's payload fields |

## The March (1991) starter, qualified

`examples/march-1991/` is a software-verified implementation of March's (1991) mutual-learning model.
The PI adopted its current documented implementation as the starter baseline for this candidate
(ruling R-01 in its `DECISIONS.md`), with its existing assumptions, discrepancies and limitations
retained. In that ruling's terms, adoption permits use and extension. It does not establish exact
replication, authenticate March's original implementation, or convert software verification into
scientific validation.

- It reproduces March's qualitative results in direction, not in level: levels are mostly lower, by
  about 0.1 to 0.2 for equilibrium code knowledge.
- One headline result, the R2 reversal, depends on an incompletely specified update order (ASM-02).
- Its nine assumptions (ASM-01 to ASM-09) are the adopted working baseline. Whether they match March's
  own program is exploratory work in its backlog (B-07 to B-09), not part of this candidate.

## Known limitations

The full list is in [docs/LIMITATIONS.md](docs/LIMITATIONS.md). The most important:

- No researcher has used the kit yet; all workflow evidence is scripted developer testing, and the
  v0.5 scenarios are still to be run.
- The turn and report checkers check form, not quality: not whether a question was the right one,
  whether the requirements and acceptance criteria are meaningful, or whether the alternatives were
  credible.
- Architecture recommendations rest on the model's knowledge unless documentation was checked.
- Telling an answer from a ruling, a plan approval or a start, and recognizing a data-semantics
  choice, are the agent's judgement, guided by the skills.
- The governance checker reads records. It cannot show that the records are true.
- Installing the hooks, agent roles and (in install mode) skills needs an interactive approval in
  Claude Code. When that is not given, setup records the items as owed with exact commands.
- The kit's benefits are proposed from team science and practice, not yet shown to improve outcomes.

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

## Deferred to the backlog (not in this candidate)

Carried from earlier candidates:

- **Checker:** the advisory step "Live items cite no superseded spec item" does not catch
  strikethrough, ID ranges (`CON-01–03`), or VAL rows citing a superseded claim; a "skills not
  installed" decision is accepted whatever its status; skills installed at user level are not
  detected; for an open sprint, it does not check that the cited ruling or SA covers the sprint's
  scope, or that the approved plan file still matches the commit its ruling names; the readiness
  block is not checked against the records.
- **Setup:** template `<!-- keep:` blocks were sometimes dropped (DT-05).
- **Install mode:** a bare `python -m pytest` rule still collects the kit's own tests (`START-HERE`
  gives `python -m pytest --ignore=kit`); installing owed skills later needs a kit clone's path; the
  checker does not confirm that each prior rule kept by decision appears in the charter.
- **Planning:** resuming an interrupted plan review has not been tested.
- **Fenced examples:** the skills show block layouts inside code fences, while a real block is plain
  text; `check_turn.py` does not warn about a fenced block.
- **March:** comparison with independent reconstructions and a systematic exploration of the
  assumptions (B-07 to B-09).
- **Modules:** the five draft modules stay drafts until tested.

## Before a public release

- Run and record the v0.5 scripted scenarios, review the diff independently, then tag `v0.5.0-rc.1`
  and complete the manual tests in `docs/MANUAL-TESTING.md`.
- Confirm copyright ownership, and the copyright holder named in `LICENSE`. During anonymous review
  it reads "The ARPD authors".
- After review, replace the anonymous author entry in `CITATION.cff` and add the framework paper.

---

## Earlier: v0.4.0-rc.1 (tagged; superseded by this candidate)

v0.4 made setup adaptive and separated it from planning:

- setup ended with planning pending, wrote no sprint record, and saved non-governing working notes
  (`docs/discovery/SETUP.md`) that let an interrupted setup resume before adoption;
- the new `/arpd-plan` skill: review, one sprint or several, priorities, a versioned draft in
  `reports/planning/`, approval of an exact version, then begin now or later; plan approval,
  execution authority and task-plan approval kept separate; continuation across sprints only by a
  standing authorization;
- the shared interaction conventions (`kit/docs/INTERACTION.md`): one labelled block last, choices
  printed before any widget, progress lines, five kinds of information and action, a dependency
  screen;
- check-in reported readiness and decisions ahead; amendment routed project defaults and milestones;
- `STATUS.md` *Readiness*; *Waiting on the PI* as the one list of open decisions, with *Affects*,
  *Needed by* and *Can continue meanwhile*; the sprint record's Part 1 rows *Approved plan*,
  *Execution authorized by* and *Transition policy*; the import baseline report;
- the checker's "ARPD skills installed" and "Open sprints: plan approval and execution authority
  cited" steps; a turn checker for scripted tests.

Its evidence was scripted developer tests DT-09 to DT-13 (75 turns), on top of DT-01 to DT-08 from
v0.3, and 150 automated tests. Its tutorial overlay and four-phase interview are replaced in v0.5.
