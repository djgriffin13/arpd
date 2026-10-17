# Release notes: ARPD v0.3.0-rc.1 (release candidate)

**Status: a release candidate, held for manual testing. This is not a final release.** The tag
`v0.3.0-rc.1` marks the exact commit described here; `git rev-parse v0.3.0-rc.1^{commit}` prints it.
A final release follows only after people have completed the manual tests in
[docs/MANUAL-TESTING.md](docs/MANUAL-TESTING.md) and any blockers they find are fixed.

## What ARPD is

A team-charter kit and three Claude Code skills (`/arpd-setup`, `/arpd-checkin`, `/arpd-amend`). A
domain researcher who is not a software developer uses them to direct a team of AI coding agents
building a research instrument, while keeping authority over every consequential scientific
decision. See [README.md](README.md).

## Install

Requirements: Claude Code (tested with 2.1.220), Git, and Python 3.8+ on the PATH as `python`. The
March example also needs numpy and pytest.

```bash
git clone <repository URL> my-project
cd my-project
git checkout v0.3.0-rc.1
claude
```

Then type `/arpd-setup` (a new project), `/arpd-setup import <path or URL>` (bring code into this
repository) or `/arpd-setup install <path>` (install into your own repository). Details, hook
permissions, confirming that logging works, owed items and recovery: [QUICKSTART.md](QUICKSTART.md)
and [docs/OPERATIONS.md](docs/OPERATIONS.md).

## Supported workflows and evidence

Every developer test below was a real Claude Code session with **scripted** researcher answers,
audited by an independent tester agent. Scripted responses are not evidence of human usability.
None of these workflows has yet been completed by a researcher.

| Workflow | Evidence | What it shows | Status in this candidate |
|---|---|---|---|
| Fresh setup | [DT-03](evaluation/developer-tests/DT-03-report.md) | Interview through first sprint plan; governing documents generated; owed `.claude/` items recorded | Runs end to end |
| Import, including the March starter | [DT-02](evaluation/developer-tests/DT-02-report.md), [DT-04](evaluation/developer-tests/DT-04-report.md) | Starter records and history kept through move-only commits; inherited decisions carried | Runs end to end |
| Install into an existing repository | [DT-05](evaluation/developer-tests/DT-05-report.md), [DT-08](evaluation/developer-tests/DT-08-report.md) | Prior instructions kept and reconciled by decision; code, tests and data untouched; history kept. DT-05 found that the skills were not installed (fixed). DT-08: an install interrupted after the adoption ruling and resumed in a new session kept everything without duplicating it | Runs end to end; resume tested at one interruption point |
| Check-in | [DT-06](evaluation/developer-tests/DT-06-report.md), [DT-07](evaluation/developer-tests/DT-07-report.md) | DT-06 found that the check-in could report nothing owed while the checker was INCOMPLETE (fixed). DT-07: after the fix, the check-in surfaces the incomplete installation and says when STATUS is out of date | Fixed and re-run |
| Amendment | [DT-06](evaluation/developer-tests/DT-06-report.md), [DT-07](evaluation/developer-tests/DT-07-report.md) | After the fixes, a new delegation adds to SA-01, open questions go to the specification, and a superseded invariant is kept and followed through dependent documents | Fixed and re-run |
| Event logging and recovery after a lost session | [DT-01](evaluation/developer-tests/DT-01-report.md), addendum 2 | Hook capture and the charter's recovery steps, in real sessions | Checked |

## Tested and draft components

| Tested (with the evidence above) | Draft or untested |
|---|---|
| Charter, governing-document templates, the three skills | The interactive interview, and every workflow, with a real researcher |
| Governance checker and event summary: 95 automated tests; seven independent review rounds | Approving the `.claude/` writes interactively (scripted runs cannot approve them) |
| Event-logging hooks and recovery, in real Claude Code sessions | Draft modules: statistical methods, experiment platform, measurement pipeline, agents inside instruments, human-subjects data |
| Modules: computational model; team arrangement | Other agent harnesses than Claude Code |
| The March (1991) worked example: 70 tests; two independent review rounds | The `StopFailure` hook's payload fields, against a real failure |

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

- No researcher has used the kit yet; all workflow evidence is scripted developer testing.
- The governance checker reads records. It does not report PASS for an item it could not check, and
  each run lists what it did not check, but it cannot show that the records are true.
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

Improvements found during this increment that do not block manual testing:

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

## Before a public release

- Complete and record the manual tests in `docs/MANUAL-TESTING.md`.
- Confirm copyright ownership, and the copyright holder named in `LICENSE`. During anonymous review
  it reads "The ARPD authors".
- After review, replace the anonymous author entry in `CITATION.cff` and add the framework paper.
