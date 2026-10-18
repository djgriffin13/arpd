# Release notes: ARPD v0.6.0-rc.1 (release candidate, in preparation)

**Status: a release candidate in preparation. Not a final release.** It restructures the kit so that
every project is its own repository and everything copied from the kit sits in one `arpd/` folder.
The setup interview, planning, check-in and amendment work as in v0.5; their paths change. A final
release follows only after people have completed the manual tests
([evaluation/manual-tests/GUIDE.md](evaluation/manual-tests/GUIDE.md)) and any blockers are fixed.

## What ARPD is

A team-charter kit and four Claude Code skills (`/arpd-setup`, `/arpd-plan`, `/arpd-checkin`,
`/arpd-amend`). A domain researcher who is not a software developer uses them to direct a team of AI
coding agents building a research instrument, while keeping authority over every consequential
scientific decision. See [README.md](README.md).

## What changed since v0.5.0-rc.1

- **The project is always a separate git repository.** The kit clone is never the project and can
  be reused. `/arpd-setup` asks what you would like to build, proposes a project folder (by default
  a sibling, `../<project-name>`), creates it, and asks you to reopen Claude Code there; the
  interview continues in the project. The v0.5 machinery that moved the kit's own files aside
  (`docs/arpd-kit/`, kit-file lists, fresh-mode detection by inventory) is gone.
- **Import starts a new repository.** A git source is cloned with its history; its `origin` remote
  is renamed `upstream`, with push disabled, so the project never pushes back. A plain folder is
  listed first and copied only with the PI's agreement. Install still works in place.
- **One `arpd/` folder.** The kit's `kit/` folder is renamed `arpd/` and copied whole into each
  project: constitution, templates, tools, agents, settings, docs, and the event log
  (`arpd/logs/`). There are no `tools/` or `reports/templates/` copies at the project root.
- **`arpd/tools/install.py`** (standard library only) does the file work: `new`, `import`,
  `install`, `update` (refresh a project's `arpd/` and skills from the kit, nothing committed) and
  `owed` (install the hook settings, agent roles and missing skills). It writes `arpd/VERSION`. It
  warns about OneDrive folders, instruction files in a parent folder, and nesting inside another
  repository.
- **`START-HERE.md` holds the map.** `INDEX.md` is gone; the governance checker reads the *Map*
  section of `START-HERE.md`.
- **Setup records in `reports/setup/`:** the working notes (`NOTES.md`) and the Project Definition
  Report (`PROJECT-DEFINITION.md`), in place of `docs/discovery/SETUP.md` and
  `reports/PROJECT-DEFINITION.md`.
- **The guide travels.** `QUICKSTART.md` and `docs/OPERATIONS.md` are merged into
  `arpd/docs/GUIDE.md`, which every project carries.
- **The worked example is extracted** to its own repository, with its history. It is local for now
  and is used through `/arpd-setup import <path>`.
- **The kit's tests** moved out of the payload to `tests/`. A project's test command is plain
  `python -m pytest`.
- **Documentation.** The README is shorter; evidence is indexed in
  [evaluation/README.md](evaluation/README.md); the manual-testing guide moved to
  `evaluation/manual-tests/GUIDE.md` and covers the new flow.

## Install

Requirements: Claude Code (tested with 2.1.220), Git with `user.name` and `user.email` set, and
Python 3.8+ on the PATH as `python`.

```bash
git clone <repository URL> arpd-kit
cd arpd-kit
claude
```

Then type `/arpd-setup`, `/arpd-setup import <path or URL>` or `/arpd-setup install <path>`, and
follow it into the project folder. Details: [arpd/docs/GUIDE.md](arpd/docs/GUIDE.md).

## Upgrading a project set up with v0.5 or earlier

- **Keep the old layout.** Nothing forces a change. The project's own `tools/` and `logs/` keep
  working. The v0.6 tools also accept the older layout: they fall back to `logs/events.jsonl`, to
  `INDEX.md` when `START-HERE.md` has no *Map*, and to hooks in `tools/hooks/`.
- **Or move to the v0.6 layout.** Add the folder with
  `python <kit>/arpd/tools/install.py install <project>` (it reports the older skills as conflicts;
  add `--force` to replace them; later refreshes use `update`), run
  `python arpd/tools/install.py owed .` to point the hooks at `arpd/tools/`, then use `/arpd-amend`
  to change the paths the charter names. The charter changes only by your ruling. Commit, then
  remove the old kit leftovers (`docs/arpd-kit/`, `examples/`, `evaluation/`, root `kit/`, `tools/`,
  `reports/templates/`, `docs/EVENTS.md`) in one remove-only commit, recorded by a DEC under your
  upgrade instruction.

## Known limitations

See [docs/LIMITATIONS.md](docs/LIMITATIONS.md). New in this candidate: the relaunch step and
`install.py` are covered by unit tests only, until the driven runs are recorded.

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

## Before a public release

- Record the v0.6 driven runs and an independent review, then tag `v0.6.0-rc.1`.
- Complete the manual tests.
- Confirm copyright ownership and the holder named in `LICENSE` (during anonymous review, "The ARPD
  authors"); then replace the anonymous author in `CITATION.cff` and add the framework paper.

## History

Each earlier candidate is preserved under its tag.

- `v0.3.0-rc.1` (2026-10-16): the charter, governing documents, setup in three modes, check-in,
  amendment, event logging and the governance checker; developer tests DT-01 to DT-08.
- `v0.4.0-rc.1` (2026-10-17): adaptive setup ending with planning pending; `/arpd-plan`; shared
  interaction conventions; readiness; developer tests DT-09 to DT-13.
- `v0.5.0-rc.1` (2026-10-18): tool-first setup with scope questions, architecture alternatives and an
  adopted Project Definition Report; data semantics reserved to the PI; driven scenarios A to H.
