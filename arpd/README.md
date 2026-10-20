# arpd/: the ARPD kit's copy

This folder is everything a project uses from the ARPD kit: kept in place when a fresh kit clone was
converted into the project, or copied whole by `arpd/tools/install.py` when the project was created,
imported or installed:

- `constitution/`: the charter template (`CORE.md`) and the modules;
- `templates/`: the governing-document, report, plan and setup-notes templates, including
  `START-HERE.md`;
- `tools/`: the governance and report checkers, plan numbering, the event logger and summarizer,
  the hook script, and `install.py`;
- `docs/`: `GUIDE.md` (the user's guide), `EVENTS.md` (what the event log records) and
  `INTERACTION.md` (how the agents talk to you);
- `agents/` and `settings/`: the agent roles and hook settings, installed into `.claude/` by
  `python arpd/tools/install.py owed .`;
- `logs/`: the event log (git-ignored);
- `VERSION`: the kit version and commit this copy came from.

**Never edit it in the project.** Your project's own documents live at its root, in `reports/` and
in `plans/`. To refresh this folder and the `.claude/skills/arpd-*` skills from a newer kit clone,
run `python arpd/tools/install.py update . --kit <path to the kit clone>` from the project root,
review what it lists, and record the update in `DECISIONS.md` (a DEC) when you commit it. The
user's guide is `docs/GUIDE.md`.

## Licence

The kit is released under the MIT License ([LICENSE](LICENSE)). Redistributing the kit, or
substantial portions of it, keeps that copyright and permission notice with it.

**Documents generated for your project.** The files that ARPD's setup and skills write for your own
project are yours. This covers your team charter (`CLAUDE.md`), `AGENTS.md`, `PARADIGM-SPEC.md`,
`REQUIREMENTS.md`, `MASTER_PLAN.md`, `DECISIONS.md`, `ARCHITECTURE.md`, `STATUS.md`,
`START-HERE.md`, `reports/setup/NOTES.md`, `reports/setup/PROJECT-DEFINITION.md`, your plans,
sprint records and reports, and your research instrument. You may use, modify, distribute or keep
them private, under any terms, without having to credit ARPD. They are covered even where they are
adapted from ARPD's templates.

**Citation (a request, not a licence term).** If ARPD helps your research, please cite it. Citation
is encouraged, not a condition of use.
