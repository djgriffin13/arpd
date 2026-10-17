# Release notes: ARPD v0.4.0-rc.1 (release candidate, in preparation)

**Status: a release candidate in preparation. Once tagged, it is held for manual testing. This is
not a final release.** The tag `v0.4.0-rc.1` will mark the exact commit described here; once it
exists, `git rev-parse v0.4.0-rc.1^{commit}` prints it. A final release follows only after people
have completed the manual tests in [docs/MANUAL-TESTING.md](docs/MANUAL-TESTING.md) and any blockers
they find are fixed.

**The previous candidate, `v0.3.0-rc.1`, is preserved** under its tag, with its regression baseline.
Its manual walkthrough was skipped by the PI's decision, because this candidate changes the setup
flow it would have tested. Manual testing moves to this candidate.

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
git checkout v0.4.0-rc.1
claude
```

Then type `/arpd-setup` (a new project), `/arpd-setup import <path or URL>` (bring code into this
repository) or `/arpd-setup install <path>` (install into your own repository). When setup is done,
type `/arpd-plan` to plan the first sprint. Details, hook permissions, readiness, confirming that
logging works, owed items and recovery: [QUICKSTART.md](QUICKSTART.md) and
[docs/OPERATIONS.md](docs/OPERATIONS.md).

## Upgrading a project set up with v0.3

A project set up with an earlier version keeps working. If you copy in the new
`tools/check_governance.py`, its "ARPD skills installed" step reports `arpd-plan` as MISSING until
you copy the kit's `.claude/skills/arpd-plan/` folder (with its `references/`) into the project's
`.claude/skills/`, or record a "skills not installed" decision. Older sprint records without the new
Part 1 rows are reported as ADVISORY, never FAIL. The charter (`CLAUDE.md`) changes only by your
ruling (`/arpd-amend`).

## What changed since v0.3.0-rc.1

**Setup (`/arpd-setup`) is adaptive, and ends before any sprint.**

- Four visible phases: Intake, Research & Problem, Product & Engineering, Governance & Handoff. The
  internal phases 0–10 still apply underneath.
- On first use, a choice between a standard interview and a guided tutorial, with no default. "Tutorial
  on" or "tutorial off" works at any time without changing what is asked or approved.
- Each phase keeps a working list of three to six topics, re-evaluated after every reply. One
  question at a time; a summary after about three to five questions, with a choice to add more or
  move on.
- It opens with two separate questions: what the researcher wants to investigate or accomplish, and
  what they want built. Coding experience, research maturity and the role wanted on the science are
  asked separately. The full vision comes before the first useful version.
- Science is scaled to the request. Product-only work is not taken through constructs, invariants or
  causal claims; its requirements can cite the adoption ruling.
- Working notes are saved as the interview goes, in `docs/discovery/SETUP.md`. They are
  non-governing. In install mode, setup asks consent before saving them in the researcher's
  repository. They are committed alone at adoption and never pushed without authorization.
- An interrupted setup can now resume **before** adoption, from the working notes. Nothing in them
  counts as adopted.
- Setup writes **no sprint record** and never offers to begin implementation. It ends with planning
  pending, `START-HERE.md` pointing to `/arpd-plan`, and a choice: plan now or later.
- Expected length: 30–60 minutes, depending on how much scientific help is asked for.

**New skill: `/arpd-plan`.**

- Works after setup, between sprints, or in a new session, from the project's records.
- Steps: review where the project stands; one sprint or several (always asked); priorities; a draft
  in `reports/planning/PLAN-<date>.md`, versioned and committed; review and revision, with an
  optional outside review; the PI's approval of an exact version; then begin now or later.
- Plan approval, execution authority and task-plan approval stay separate. Approval alone starts
  nothing; when the PI says nothing about starting, planning approval only is recorded. "Later"
  leaves an exact start prompt in `START-HERE.md`.
- For a series, the PI chooses how sprints follow each other. Continuing across boundaries without a
  new ruling needs a standing authorization naming the sprints, the transition conditions and when to
  consult the PI. Every boundary still gets close-out, independent review and checks.

**Shared interaction conventions** (`kit/docs/INTERACTION.md`), used by all four skills: one
labelled block (`QUESTION FOR YOU`, `CHOICE FOR YOU`, `APPROVAL REQUIRED`) last in every turn that
waits for the PI; choice options printed as text before any widget; progress lines; the tutorial
overlay; five kinds of information and action (an answer is not an authorization); a quick
dependency screen; an ASCII fallback.

**Check-in and amendment.**

- `/arpd-checkin` reports readiness (setup, planning, execution) and cross-checks it against the
  records; lists decisions ahead, grouped by the work they block; runs the dependency screen; and
  gives the exact next prompt.
- `/arpd-amend` routes project defaults (review depth, transition policy, planning cadence) and
  milestone changes, applied from the PI's clear words with no second approval, and records
  continuation authorizations across sprints.

**Charter and templates.**

- `CORE.md`: working notes and plan drafts are listed as deciding nothing; a sprint plan is approved
  by the PI, unlike routine task plans; planning is not starting; multi-sprint continuation is an SA;
  a dependency screen at set points; `STATUS.md` carries a readiness block.
- `STATUS.md`: a *Readiness* block (setup, planning, execution, next step); §5 summarizes the
  decisions ahead.
- `DECISIONS.md`: *Waiting on the PI* is the one canonical list of open decisions, with *Affects*,
  *Needed by* and *Can continue meanwhile* columns; formats for plan approval and for a continuation
  SA.
- Sprint record Part 1: the rows *Approved plan*, *Execution authorized by* and *Transition policy*
  replace "Authorized to continue into the next sprint without a check-in?". Older records keep the
  old row.
- `MASTER_PLAN.md`: a broad roadmap that can say "planning pending".
- New templates: the setup working notes, the sprint-plan draft, and the import baseline report.
- Invariant, requirement and acceptance criterion are explained in the same three rows in
  `PARADIGM-SPEC.md`, `REQUIREMENTS.md`, `plans/README.md` and the project's `START-HERE.md`. The
  task-plan heading "Scientific constraints" is now "Scientific invariants this work must respect
  (INV IDs)".

**Import baseline.** An imported or installed project's test and checker results before any change
are recorded once, verbatim, in `reports/IMPORT-BASELINE-<date>.md`. The import decision cites it,
and so does the first sprint's Part 1. Before, they were recorded in the first sprint's Part 1.

**Governance checker.**

- The skills step is renamed "ARPD skills installed" and includes `arpd-plan`.
- A project with setup adopted and no sprint passes.
- New step "Open sprints: plan approval and execution authority cited": in an open sprint's Part 1,
  the cited rulings and SAs must exist and not be pending, and the plan file and version must exist.
  Records in the older format get an ADVISORY, never a FAIL.
- The readiness block is listed under *Not checked*. Closed-sprint checks are unchanged.

**Developer-test tooling.** A turn checker, `evaluation/developer-tests/check_turn.py`, checks the
form of a saved turn in scripted tests: the labelled block last, choice options in the text, the
progress line, and that an approval names what it approves.

## Supported workflows and evidence

Every developer test below is, or will be, a real Claude Code session with **scripted** researcher
answers, audited by an independent tester agent. Scripted responses are not evidence of human
usability. None of these workflows has yet been completed by a researcher.

DT-01 to DT-08 were run on v0.3.0-rc.1. They remain the evidence for what v0.4 did not change. The
setup interview and its handoff changed, so the setup tests (DT-02 to DT-05, DT-08) are evidence for
the earlier interview only; the moves, history and owed-item handling they show are unchanged.

| Workflow | Evidence | What it shows | Status in this candidate |
|---|---|---|---|
| Adaptive fresh setup, ending with planning pending | (DT-09–DT-13: to be filled) | (to be filled) | New; scripted tests in progress |
| `/arpd-plan`: one sprint, approved, started later | (DT-09–DT-13: to be filled) | (to be filled) | New; scripted tests in progress |
| `/arpd-plan`: a series with a gated transition | (DT-09–DT-13: to be filled) | (to be filled) | New; scripted tests in progress |
| Import of the March starter, with the import baseline report | (DT-09–DT-13: to be filled) | (to be filled) | Regression test in progress |
| Setup interrupted before adoption, resumed from the working notes | (DT-09–DT-13: to be filled) | (to be filled) | New; scripted test in progress |
| Fresh setup, v0.3 interview | [DT-03](evaluation/developer-tests/DT-03-report.md) | Interview through first sprint plan; governing documents generated; owed `.claude/` items recorded | Superseded flow; generation and owed-item handling unchanged |
| Import, including the March starter | [DT-02](evaluation/developer-tests/DT-02-report.md), [DT-04](evaluation/developer-tests/DT-04-report.md) | Starter records and history kept through move-only commits; inherited decisions carried | Ran end to end on v0.3 |
| Install into an existing repository | [DT-05](evaluation/developer-tests/DT-05-report.md), [DT-08](evaluation/developer-tests/DT-08-report.md) | Prior instructions kept and reconciled by decision; code, tests and data untouched; history kept. DT-05 found that the skills were not installed (fixed). DT-08: an install interrupted after the adoption ruling and resumed in a new session kept everything without duplicating it | Ran end to end on v0.3; resume tested at one interruption point. The consent prompt for working notes is new and untested |
| Check-in | [DT-06](evaluation/developer-tests/DT-06-report.md), [DT-07](evaluation/developer-tests/DT-07-report.md) | After a fix, the check-in surfaces an incomplete installation and says when STATUS is out of date | Ran on v0.3; the readiness and decisions-ahead additions are untested |
| Amendment | [DT-06](evaluation/developer-tests/DT-06-report.md), [DT-07](evaluation/developer-tests/DT-07-report.md) | A new delegation adds to SA-01; open questions go to the specification; a superseded invariant is kept and followed through dependent documents | Ran on v0.3; the routes for project defaults and milestones are untested |
| Event logging and recovery after a lost session | [DT-01](evaluation/developer-tests/DT-01-report.md), addendum 2 | Hook capture and the charter's recovery steps, in real sessions | Checked on v0.3; unchanged |

## Tested and draft components

| Tested (with the evidence above) | Draft or untested |
|---|---|
| Charter, governing-document templates and the v0.3 skills, in scripted developer tests | Every workflow with a real researcher |
| Governance checker and event summary: automated tests (95 at v0.3.0-rc.1; count for this candidate to be filled); seven independent review rounds on v0.3 | The adaptive setup, `/arpd-plan`, the interaction conventions and the v0.4 check-in and amendment changes: scripted tests in progress (DT-09–DT-13: to be filled); none tested by people |
| Event-logging hooks and recovery, in real Claude Code sessions | Approving the `.claude/` writes interactively (scripted runs cannot approve them) |
| Modules: computational model; team arrangement | Native choice widgets, and symbol rendering, in the Claude Code terminal and the Claude app |
| The March (1991) worked example: 70 tests; two independent review rounds | Draft modules: statistical methods, experiment platform, measurement pipeline, agents inside instruments, human-subjects data |
|  | Other agent harnesses than Claude Code; the `StopFailure` hook's payload fields, against a real failure |

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

- No researcher has used the kit yet; all workflow evidence is scripted developer testing. The new
  setup interview, `/arpd-plan` and the interaction conventions have not been used by people.
- The turn checker checks the form of a turn, not whether the question was a good one, how the
  tutorial feels, or how native widgets behave. Those need the manual tests.
- Telling an interview answer from a ruling, a plan approval or a start is the agent's judgement,
  guided by the skills. The checker cannot confirm that any of them is in the PI's own words.
- The governance checker reads records. It does not report PASS for an item it could not check, and
  each run lists what it did not check, but it cannot show that the records are true. It does not
  check the readiness block, or whether a cited authority covers an open sprint's scope.
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

Carried from v0.3.0-rc.1:

- **Checker, advisory step "Live items cite no superseded spec item":** it does not yet catch
  supersession written as strikethrough, ID ranges (`CON-01–03`), or VAL rows citing a superseded
  claim.
- **Checker:** a "skills not installed" decision is accepted whatever its status; skills installed
  at user level (`~/.claude/skills`) are not detected.
- **Setup:** template `<!-- keep:` blocks were sometimes dropped (DT-05); a setup decision recorded
  as "consult" with no scientific consequence (DT-05).
- **Install mode:** a project whose kept rule is a bare `python -m pytest` still collects the kit's
  own tests (`START-HERE` gives `python -m pytest --ignore=kit`); a pytest configuration written at
  install would fix this. Installing the owed skills later needs the path of a kit clone, because
  the skills are not inside `kit/`. The checker does not yet confirm that each prior rule kept by
  decision appears in the charter.
- **March:** comparison with independent reconstructions and a systematic exploration of the
  assumptions (B-07 to B-09); no further March work in this candidate.
- **Modules:** the five draft modules stay drafts until tested.

New in this candidate:

- **Checker:** for an open sprint, it does not check whether the cited ruling or SA covers that
  sprint's scope, or whether the approved plan file still matches the commit its ruling names. The
  readiness block is not checked against the records.
- **Planning:** resuming an interrupted plan review has not been tested.

## Before a public release

- Fill in the DT-09 to DT-13 evidence above, and the automated test counts.
- Tag `v0.4.0-rc.1`, then complete and record the manual tests in `docs/MANUAL-TESTING.md`.
- Confirm copyright ownership, and the copyright holder named in `LICENSE`. During anonymous review
  it reads "The ARPD authors".
- After review, replace the anonymous author entry in `CITATION.cff` and add the framework paper.
