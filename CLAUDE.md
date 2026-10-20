# CLAUDE.md: a fresh copy of ARPD

This folder is a fresh copy of the ARPD kit, not yet a research project.

- **To start a project, run `/arpd-setup`.** Setup assesses this folder, interviews the researcher (the
  PI), and by default turns this folder into the project in place: it removes ARPD's own development
  files, keeps `arpd/`, the setup skills and every file of the PI's, and starts a fresh git history
  with no remote. It continues in this same session.
- **Do not build, plan or change anything before setup is complete**, and never push this folder to
  the ARPD repository it was cloned from. Until the PI adopts the Project Definition Report, the
  `/arpd-setup` skill governs the work; after adoption, the generated `CLAUDE.md` charter does.
- The PI's guide is `arpd/docs/GUIDE.md`.
- Only if you are asked to change ARPD itself, read `DEVELOPING.md` first.
