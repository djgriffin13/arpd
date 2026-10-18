# CLAUDE.md: the ARPD kit

**This is the ARPD kit, not a project. Run `/arpd-setup` to create a project in its own folder;
never write project files here.**

- To start a project, import existing code or install ARPD into an existing repository, run the
  `/arpd-setup` skill. Setup creates or prepares a separate git repository (by default a sibling
  folder, `../<project-name>`) with `python arpd/tools/install.py`, then asks the user to reopen
  Claude Code there to continue. Do not build anything before setup is complete.
- Setup ends with planning pending. Sprints are planned with `/arpd-plan`, and work starts only from
  a plan the user has approved and their direction to begin.
- The worked example (March, 1991) is in its own repository; it is used through
  `/arpd-setup import <path>`.
- The user's guide is `arpd/docs/GUIDE.md`.

**Developing the kit itself:**

- keep `arpd/` (charter, modules, templates, agents) generic, with no project- or person-specific
  content;
- keep every file free of author, institution or project names and of local paths (the repository
  is anonymous for review);
- modules marked *draft* stay drafts until tested;
- the kit's own tests are in `tests/` (`python -m pytest tests`); evidence goes in `evaluation/`.
