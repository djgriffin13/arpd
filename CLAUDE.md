# CLAUDE.md: ARPD kit (not yet set up)

This repository is the **ARPD kit** in its unconfigured state. It is not a research project yet.

- If the user wants to start a project, import a codebase, or install the kit into an existing
  repository, run the `/arpd-setup` skill. Do not build anything before setup is complete.
- Setup ends with planning pending; it never starts implementation. Sprints are then planned with
  the `/arpd-plan` skill, and work starts only from a plan the user has approved and their direction
  to begin.
- If the user wants to explore the worked example, point them to `examples/march-1991/` and its
  `README.md`.
- If the user is developing the kit itself, follow these rules:
  - keep `kit/` templates generic, with no project- or person-specific content;
  - keep every file free of author, institution or project names (the repository is anonymous for
    review);
  - modules marked *draft* stay drafts until tested.

After setup, the generated team charter replaces this file.
