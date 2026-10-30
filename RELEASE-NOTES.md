# Release notes: ARPD v0.7.0-rc.4 (release candidate)

**Status: a release candidate, not a final release.** It has been used by members of its development
team, by two researchers outside it and in 27 logged runs of the tutorial, but not yet evaluated with
researchers outside the author team; see [docs/LIMITATIONS.md](docs/LIMITATIONS.md).

## What ARPD is

A team-charter kit and four Claude Code skills (`/arpd-setup`, `/arpd-plan`, `/arpd-checkin`,
`/arpd-amend`). A domain researcher who is not a software developer uses them to direct a team of AI
coding agents building a research instrument, while keeping authority over every consequential
scientific decision. See [README.md](README.md).

## What v0.7 does

- **Setup works in place.** Clone or download ARPD, open Claude Code there, type `/arpd-setup`. By
  default setup turns this folder into the project: `arpd/` and the skills stay, every file of yours
  is kept, and the folder gets a fresh git history with no remote. ARPD's own files and the clone's
  old history move to a backup folder beside the project, with a `RESTORE.md`; nothing is deleted.
  Existing repositories can be set up in place instead, with their history and remote kept.
- **A research-aware interview in phases** (Intake, Objectives, Constraints, Design, Development),
  each ending in a summary you confirm, then a Project Blueprint you adopt. Only then are the
  governing documents written.
- **Goal-first planning** (`/arpd-plan`): your goal, the effort sized, a versioned plan, approval of
  an exact version, then begin now or later. Work starts only when you say so.
- **Works without Python**, with read-throughs in place of the automated checks
  ([arpd/docs/NO-PYTHON.md](arpd/docs/NO-PYTHON.md)).

## Changes since v0.7.0-rc.3

- **Project Blueprint.** The setup report is now the Project Blueprint
  (`reports/setup/PROJECT-BLUEPRINT.md`); the checkers still accept the older
  `PROJECT-DEFINITION.md`.
- **Clearer turns.** Each message that needs the PI ends in one labelled block (❓ question,
  🔘 choice, ✋ approval), with a progress line, and a ⏳ WORKING line only while something is
  running.
- **Governance check.** A decision left pending in a closed sprint record now counts as settled
  when a later ruling in `DECISIONS.md` names it, so closed records stay unedited.
- **Tutorial.** A web tutorial (`TUTORIAL.html`, with `TUTORIAL.md` built from the same source):
  question cards with suggested replies and real-run examples, help pages, and time and cost
  figures from 27 logged tutorial runs. Links are relative, so the repository and its tutorial
  carry no author information.
