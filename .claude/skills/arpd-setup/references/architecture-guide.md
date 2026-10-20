# Architecture guide

Helping the PI understand the meaningful engineering options is one of setup's main jobs, in the
Design phase. This guide says when a decision deserves exploration, how to explore it, and what to
record. The alternatives below are illustrations, not mandatory lists. Recommend from the project's
actual requirements and constraints (the Constraints phase's Must and Prefer items).

## Start from the PI's design

Before any recommendation, ask whether the PI has a design or architecture in mind
(`interview-guide.md`, Design, DS-01). It is collaborative design, not a verdict:

- **A design from the PI** is the starting point. Read it back, give its strengths and your concerns,
  and run the procedure below on its material decisions with the PI's choice as one alternative,
  described fairly. Recommend a change only where a requirement or constraint calls for it, and say
  which.
- **No design:** propose one, in plain words first (what runs where, what the user sees, where the
  data go), then the procedure for each material decision.
- **Rounds.** Revise in response to the PI's questions and ideas for as many rounds as the PI needs;
  a fixed number of rounds is not the aim, and neither is speed. Close only through the Design
  readiness question.
- **Depth follows the PI's coding comfort (IN-03).** For a proficient coder, discuss components,
  interfaces, persistence and testing strategy directly, and ask about them. Otherwise, propose and
  explain, and ask about consequences the PI can judge (cost, where data live, what users must
  install, what later changes would need).

## Which decisions are material

A decision is **material** if a different choice would noticeably change any of these:

- how users get and run the software (distribution, installation, updates);
- where data live, and who can reach them;
- what it costs, or what it commits the PI to (licences, hosting, maintenance skills);
- what can be built later without a rewrite;
- the data semantics or the scientific results (consequential under CORE §6);
- the effort, risk or time of the first version.

Everything else is **low-consequence**: state the default, or delegate it. Examples are the code
layout, the test framework within the chosen language, formatting tools, internal module names, file
naming inside the project, and logging format. Do not present alternatives just to look thorough. A
small project may have one material decision, the platform, and nothing else.

The converse also holds. Never treat a language or framework as obvious when credible alternatives
have meaningfully different consequences. "The PI said Windows" does not settle "a Python desktop
program".

## The procedure, for each material decision

1. **Requirements and constraints.** Name the requirements and facts that bear on the decision.
   Separate what the PI actually ruled out from what you inferred. For example, "data stay on each
   student's computer" rules out central storage, not a browser interface.
2. **An existing solution.** Ask whether a clear existing solution or architecture applies. That
   includes **configuring an existing tool instead of building**: a survey platform, a spreadsheet
   with validation, an existing package, an automation service. If one fits, say so plainly, even
   when it makes most of the build unnecessary. Describe it fairly: some research survey and
   data-collection platforms are hosted by the institution, not a vendor, and some work offline;
   when unsure, say "not verified" rather than dismiss it. Unless the PI excluded it, an existing
   tool gets its own row in the decision table, with its real advantages. If a constraint seems to
   rule it out (for example, "data stay internal"), ask what the PI means first; never present your
   own reading as the PI's ruling. For a computational method, always weigh
   reusing or wrapping existing libraries before writing new code.
3. **Credible alternatives.** Usually two to four. Each must be something you would defend.
4. **Trade-offs.** For each, the advantages and disadvantages that matter to *this* PI. Cover
   development effort, distribution and updates, data location and safety, cost and licensing,
   maintainability by the people who will maintain it, and fit with the PI's community and tools.
   **When speed is part of the trade-off, size the workload first** with a rough count from what
   the PI said (for a simulation: agents × dimensions × steps × repetitions × parameter settings;
   for an analysis: rows × models × resamples), and say what it implies ("a Figure 1-style sweep is
   on the order of 10^9 updates: hours in pure Python, minutes with numpy"). A count in a sentence
   is enough: never benchmark or time code during the interview.
5. **Recommendation, with reasons** tied to the requirements.
6. **Consequences** for future development: what the choice makes easy, what it makes hard, and
   what would force a change later. For a model, simulation or experiment platform, include what
   the choice means for research: which models, conditions, measurements or analyses it can support
   later, and which it would rule out.
7. **The PI's choice**, when the decision is material. Use a `CHOICE FOR YOU (select one)`, with the
   recommendation marked. Include an option to hear more before deciding. The PI's pick is recorded
   with their words. It is a preference until the report is adopted.
8. **Record** the selected option and the rejected alternatives with their reasons:
   - in the notes, *Architecture alternatives explored*;
   - then in the report §8, with the columns Decision | Alternatives considered | Recommendation |
     Rationale | Status | Consequences;
   - after adoption, in `ARCHITECTURE.md`, *Architecture decisions*.

A recommendation is **not an adopted design**. Its report status is one of:

- **Adopted-on-adoption:** the PI chose it;
- **Proposed:** your recommendation, not yet chosen;
- **Provisional:** a working assumption, to be confirmed by a named check or gate;
- **Delegated (SA-NN):** the team may decide within stated bounds;
- **Open (gate).**

Also record the remaining uncertainty and the dependencies.

**Do not defer the riskiest choice.** If the packaging, distribution or storage mechanism is where
the project could fail, it belongs in the architecture now, as a decision or as an Open item with a
gate before implementing. It does not get pushed silently into sprint planning.

## Evidence for technical claims

- For niche, fast-changing or consequential choices (packaging tools, platform support, a library's
  maintenance status, a hosted service's terms), check current documentation when you have access,
  and cite what you checked.
- Without access, or without checking, say "not verified" next to the claim. Never claim an option
  is supported, maintained or superior without adequate evidence.
- Get the basics right. For example, a browser-based interface does **not** require a server or
  internet access: a single local HTML page, or a small local web app, runs on one machine and can
  save data locally. Hosting is a separate choice.

## Domains to consider (where applicable)

- **Language and frameworks.** Fit with the PI's community: an R package for R users affects
  adoption. Fit with the maintainers' skills.
- **User interface.** Desktop toolkit, browser page, local web app, command line, API, or none.
- **Storage.** Plain files (CSV, JSON), an embedded database (SQLite), or a server database. Crash
  safety, concurrent access, and backup.
- **Local versus centralized.** Where data live, who can see them, and how they are gathered.
- **APIs and external interfaces.** Contracts with other systems, authentication, rate limits, and
  failure handling.
- **Modularity and components.** What must be separable now, for example the estimator core from
  its reporting.
- **Data processing.** Streaming versus batch, and in memory versus on disk.
- **Concurrency and parallelism.** Only when the workload needs it, for example bootstrap resamples
  or many simulation runs.
- **Compute and deployment.** A laptop, a lab server, the cloud, or a cluster.
- **Dependencies.** Prefer few, but weigh them by how established they are:
  - **Standard scientific libraries are favoured** where they fit the work: in Python numpy,
    scipy and pandas (and matplotlib for plots); in R the tidyverse and the standard modelling
    packages; their equivalents elsewhere. They are widely used, tested and maintained, and the
    research community expects them, so "one more dependency" counts against them only very
    weakly: never recommend hand-written numerical code or the standard library alone over them
    just to avoid an install, for computational work they suit.
  - **Untested, little-used or moderately established packages** are where the preference for few
    dependencies applies in full: use one only when it saves real work, and say what it would cost
    to replace.
  - Keep the total small either way, permissively licensed; a dependency with licence or cost
    implications is consequential (CORE §6).
- **Open-source versus proprietary components,** and **licensing or cost.**
- **Distribution and updates:**
  - how users receive the software;
  - whether it runs on managed or locked-down machines, such as school, hospital or corporate
    laptops that block unsigned programs;
  - unsigned-executable and antivirus warnings;
  - how an update (a new version, or changed questions) reaches every user;
  - how each output records which version produced it.

## Illustrative alternatives by project type

### Local data collection on users' own computers

| Alternative | For | Against |
|---|---|---|
| Python desktop program | Straightforward to build; large ecosystem; offline | Packaging into one program needs care; unsigned bundles often trigger security warnings or are blocked on managed machines (verify for the target machines); updates mean redistributing |
| C#/.NET desktop program | Strong Windows integration; mature desktop UI tooling | Mostly Windows-only in the relevant frameworks; fewer researchers can maintain it |
| Local browser page or local web app | Familiar interface; flexible UI; a single HTML file needs no installation | Saving data locally needs a deliberate design (browser storage is easy to lose; file export must be explicit); a local app server must still be installed and started |
| Hosted web application | Central collection, one place to update, no installation | Needs hosting, connectivity, server operations, and attention to security and privacy |
| Existing survey or data-collection software | May remove most custom development; some are institution-hosted or have offline modes | Less control over behaviour and export; licensing, privacy and platform constraints (check what the PI's institution offers) |

### Statistical method or estimator

| Alternative | For | Against |
|---|---|---|
| Pure numpy or scipy package | Full control over the computation; light dependencies | You write and test everything, including the edge cases |
| Built on an established statistics library | Reuses tested routines | Its conventions (variance estimators, defaults) become yours; check them against the PI's definitions |
| R package | Natural for R users; strong statistical tooling | Different testing and distribution conventions; harder to call from Python |
| Wrapping or calling existing implementations | Fastest route to matching known results | Limited by their assumptions and maintenance; a licence check is needed |

Known answers from the literature, or from established implementations, are the acceptance tests in
every case.

### Simulation engine or agent-based model

- a custom Python package (numpy, seeded);
- an existing modelling framework (check that its scheduling and update order match the
  specification exactly, and say "not verified" until checked);
- a compiled core for speed, only if the stated workload needs it.

### Online experiment or interactive platform

- a custom web app (a small server, a browser front end, and a database);
- an existing experiment framework, configured;
- a survey platform with its scripting features.

The trade-offs are control over timing, conditions and logging, against development and hosting
effort.

### Measurement pipeline from existing files

- a command-line pipeline that reads raw files and writes tidy outputs, with a coverage report;
- notebooks, for exploration only (hard to re-run reliably);
- a workflow tool, when there are many steps with dependencies.

### Integration or automation

- a script plus a scheduler;
- an existing automation service, configured;
- a small service with retries and logging.

Look first for a configurable tool, then weigh credential handling, failure recovery and
maintenance.

## Defaults that apply to every platform

These are routine. State them in the report §6 or §7; do not ask about them.

- Git from day one, with small commits that explain *why*.
- One command runs the project's tests (`generation-checklist.md`, *The project's test command*).
- Seeds are recorded for anything random.
- Outputs go to a git-ignored `output/` folder, unless a ruling makes them part of the record.
- No real participant data in the repository.
- Nothing the PI would need a developer to maintain (containers, microservices, GPU, cloud
  deployment), unless the requirements call for it. Standard scientific libraries (numpy, scipy,
  the tidyverse, …) are not in this class: they are listed in a requirements file and installed
  with one command.
