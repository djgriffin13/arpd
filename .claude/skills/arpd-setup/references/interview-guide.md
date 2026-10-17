# Interview guide

The interview has four visible phases. Each phase below gives a **menu of candidate topics**, not a
script. Pick the three to six topics that matter for this project, add your own, and skip any that
existing files or earlier answers already settle (say what you found instead). The wording is a
suggestion; adapt it to the PI. Defaults appear in **[brackets]**.

Every turn follows `kit/docs/INTERACTION.md` and the adaptive-coverage steps in `SKILL.md`: one
primary question, all topics re-evaluated after each reply, a synthesis after about 3–5 substantive
questions, and the labelled block last.

| Visible phase | Internal phases | Typical length |
|---|---|---|
| Intake | 0 Orient, 1 The PI | 3–5 minutes |
| Research & Problem | 2 Science | 5–20 minutes, depending on the scientific help asked for |
| Product & Engineering | 3 Instrument, 4 Evidence, 7 Constraints | 10–15 minutes |
| Governance & Handoff | 5 Team, 6 Authority, 8 Read-back, 9 Generate, 10 Handoff | 10–15 minutes |

An import of an ARPD starter is usually shorter: its science is confirmed, not elicited.

---

## Tutorial hints

In **Guided tutorial** mode, add a short hint above the labelled block the **first time** each
thing comes up. Do not repeat a hint. Taper off as the PI shows familiarity. With tutorial off, give
none. Examples:

- **First turn:** "Setup has four phases. The list under the progress line shows what I still need
  to understand in this phase. It changes as you answer."
- **First open question:** "You can answer roughly, out of order, or ask me to brainstorm with you.
  I'll update the list."
- **First saved note:** "This is an interview question, not an approval. I'll add your answer to
  working notes, not to the charter."
- **First useful version:** "We'll hear the full vision first, then pick the first version that
  would actually be useful. Nothing you mention is lost; later items go on the roadmap."
- **First invariant, requirement or acceptance criterion:** explain the three together, once. Use
  the three-row explanation in `kit/templates/PARADIGM-SPEC.md` §5 (the same text is in
  `kit/templates/plans/README.md`), so the wording matches the project's files. In short:
  - an **invariant** (INV) is what must never break, or the results stop meaning what you intend.
    It lives in `PARADIGM-SPEC.md` §5, and you own it;
  - a **requirement** (REQ) is what the instrument must do. It lives in `REQUIREMENTS.md`, traces to
    a spec item or a ruling, and has a state and evidence;
  - an **acceptance criterion** is how one plan proves it delivered. It lives inside that plan
    (`plans/NNN-…`), and its evidence moves a requirement's state.
- **First read-back:** "This is the first approval. Your reply in your own words becomes a recorded
  ruling, and only then are the governing files written."
- **Handoff:** "Sprint planning is a separate, optional next step. Planning a sprint and starting
  work are also separate: you approve a plan first, then decide when work begins."

---

## Intake (internal Phases 0–1)

### Orient (Phase 0)

1. **Detect the mode.**
   - Run `git status` and list the top level.
   - If the repository contains only the kit (`kit/`, `.claude/skills/arpd-*`, `docs/`,
     `evaluation/`, `examples/`, and the kit's own `README.md`, `QUICKSTART.md`, `CLAUDE.md`,
     `AGENTS.md`, `LICENSE`, `CITATION.cff`, `RELEASE-NOTES.md` and dotfiles), the mode is
     **fresh**. The kit's own files are not prior instructions.
   - If the PI passed `import <path|url>` or `install <path>`, or if the project's own source code
     or instruction files (`CLAUDE.md`, `AGENTS.md`, `.cursorrules`, `README` with design notes)
     are present, follow `import-path.md`. A starter inside the kit (for example
     `examples/march-1991/`) is an import of an ARPD project: read its existing specification to the
     PI in plain language and ask them to confirm or change it.
2. **Inspect materials first.** Read what the PI provides or points to: a proposal, grant text, a
   protocol, design notes, code, earlier decisions. Summarize what is already known. Ask only for
   what is missing.
   - **Existing proposal, no code:** reuse the proposal. Do not treat the project as an unformed
     idea or re-ask what it answers. Focus on the product and on gaps.
   - **Existing code:** follow `import-path.md`. Draft from the code, marked "inferred from code:
     confirm".
   - A new repository does not mean the research is new.
3. **Check for a partial setup** (`SKILL.md`, *Resuming an interrupted setup*).
4. **Offer the interview mode** (Standard interview / Guided tutorial, no default), unless a mode is
   already recorded.
5. **Discovery notes.** Fresh and import modes: tell the PI the notes are saved in
   `docs/discovery/SETUP.md`, that they are working notes and decide nothing. Install mode: ask for
   consent first (`SKILL.md`, *Discovery notes*).
6. **Tell the PI in three sentences** what will happen:
   - "We'll talk about what you want to study and what you want built, then I'll propose how to
     build it. About 30–60 minutes, depending on how much scientific help you want."
   - "I save working notes as we go. Nothing governing is written, and nothing is built, until you
     approve a summary."
   - "Afterwards you'll have a team charter, the governing documents and a roadmap. Planning the
     first sprint is the next step."
7. **State the division of labour (G5).** "The agent team can show that code matches the
   specification and that known answers are reproduced. Only you can judge whether the
   specification captures what you mean, and whether a result is scientifically meaningful."

### The PI (Phase 1)

Ask these as bounded choices where the options are natural, printing the options first. Record the
answers in the notes; they go to `STATUS.md` §8 at generation. Candidate topics:

- **Coding experience:** [none / some scripting (R, Python, Stata) / regular programmer].
- **AI-tool experience:** [chat assistants only / some coding assistants / regular agentic use].
- **Research maturity**, asked separately from coding: [idea / developed design / existing proposal
  / existing code]. Often the materials answer this. Never infer low research expertise from low
  coding experience.
- **Adviser role:** how much should the team help with the science? (select one; no default)
  - A. Build only: build from my design; ask only what correctness needs.
  - B. Sounding board: help me brainstorm and clarify when useful.
  - C. Light review: point out gaps and risks.
  - D. Full critique: actively review and challenge the scientific design.
- **Review depth:** how closely the PI wants to review drafts and plans [light / thorough].
- **Time and check-ins:** time per week, and how decisions are brought: [batched at sprint
  boundaries / as they arise / daily digest].
- **Name** to use as PI in the records (a role, such as "PI", is fine).
- **External access** (other data or repositories): only if useful, and only with the PI's say-so.

**Propose an authority profile** early, so the PI knows how much the team will do on its own. Print
the options first, then ask:

> "How much should the team decide on its own? I suggest **bounded autonomy**: it works within the
> scientific boundaries we agree, writes down any material assumption it makes, and reports at each
> checkpoint. The alternatives are **consult first** (it asks you before adopting any scientific
> assumption) and **exploratory autonomy** (it tries and compares plausible alternatives on its own,
> then comes back to you to decide which to adopt). You can change this at any time."

Record the choice in the notes. It becomes SA-01 in Governance & Handoff.

---

## Research & Problem (internal Phase 2)

**Open with two separate questions**, one per turn:

1. "What would you like to investigate, study, or accomplish?" **(V)**
2. "What would you like to have built or available to make that possible?"

Do not demand a fully developed theory. Record the PI's words verbatim where marked (V): no
recapitalizing, splitting or tidying.

**Set the depth from the adviser role and the correctness risk.**

- **Build only (A), and correctness does not hinge on scientific definitions:** learn enough
  domain context to build correctly: the data, its assumptions, and what outputs mean. Do not walk
  the PI through constructs, invariants or causal claims. Requirements may cite the adoption ruling
  (R-NN) as their source. Never invent CON, OP or INV items to satisfy traceability.
- **Sounding board or light review (B, C):** clarify the key ideas and assumptions; propose a few
  candidate invariants and claims not to make only where they protect correctness.
- **Full critique (D), or correctness depends on scientific definitions** (a method, a simulation,
  a measure, a human experiment): use the full method below.

Draft candidate definitions and invariants only after hearing the PI's view. Label each one's origin
(the PI's words, or drafted by the lead), confidence and status (candidate, accepted, rejected).
Silence, or "looks good" about something else, is not consent to a new scientific model.

**Draft wording.** On import, an item marked *"(draft wording, awaiting the PI's words)"* (often the
research question) needs the PI's own words now. If the PI does not give them, the item stays
explicitly pending and goes in *Waiting on the PI*. Adopting the specification "as it stands" does
not clear the marker.

### Candidate topics

- **Purpose** (V): the question or goal, in the PI's words.
- **Obstacle:** "What stops you studying it now?" Probes: existing tools and their limits; data that
  exist but aren't accessible; models built for a different design; constructs usually self-reported
  that should be observed.
- **Domain boundaries:** what is in and out of the science, for now.
- **Known assumptions and evidence:** what the PI already knows or relies on.

### The full paradigm-specification method (only when requested or correctness-critical)

1. **(V for definitions) Constructs and mechanisms.** "What are the key constructs or mechanisms?
   For each, how would you define it?" Offer a draft definition from their description and let them
   correct it. Assign CON-NN IDs.
2. **Operationalizations.** "For each construct, what should the instrument manipulate, record or
   compute? At what level (person, dyad, team, event, round) and timing?" Assign OP-NN IDs.
3. **Candidate invariants.** Using `module-catalog.md`, propose three to eight invariants in
   *scientific* language. Examples:
   - "Conditions differ only in the manipulated feedback."
   - "An unobserved tie is missing, not absent."
   - "The model's agents update only at the end of a period."

   Ask the PI to accept, edit or reject each. Assign INV-NN IDs. Then ask: "Is there anything that,
   if the code got it wrong, would make the results meaningless?" and add those.
4. **Claims.** "What should results from this instrument let you say?" (CLM-NN). Then propose two to
   four **claims not to make** (NCL-NN), for example: causal language without identification;
   generalizing beyond the explored parameter range; treating simulated participants as people.
5. **Assumptions** (for models or replications). Where a source is ambiguous, list the
   interpretations and record the PI's choice (ASM-NN).
6. **Validation** (VAL-NN): see Evidence, below.

---

## Product & Engineering (internal Phases 3, 4 and 7)

**Hear the full vision before narrowing.** In order:

1. "If the full version worked perfectly, what could someone do with it?" Cover the user flow, the
   target users and the capabilities.
2. "What is the first version that would actually be useful to you?"
3. "Which capabilities must come later, which are nice to have, and what should it deliberately
   *not* do?" Later items and the wishlist go to the roadmap; exclusions go to the read-back.

Find out which parts the ask covers: an interaction platform, data capture, a measurement pipeline,
statistical analysis, visualization, simulation, an API integration, or only some of these. Do not
add analyses or validation packages the PI did not ask for.

### Candidate topics

- **Instrument (Phase 3).** "Walk me through how you (or a participant, or a co-author) would use
  it, from start to finish."
  - Draft 5–15 requirements for the first useful version, phrased as things the PI would observe.
  - Assign `REQ-<AREA>-NN` IDs, each with a **source** (OP, INV, CLM, or the adoption ruling for
    product-only work) and its **acceptance evidence** (what would show it works).
- **Data in and out.** Sources, formats, and the analysis software the output must feed (R, Stata,
  SPSS, Python).
- **Input adequacy.** For each operationalization and invariant, check that the input data carry
  every quantity it needs. For example, telling "present but silent" from "absent" needs a roster,
  not only a message log. Ask the PI about each gap. A gap the PI cannot resolve now becomes an open
  question (`PARADIGM-SPEC.md` §9 when the science is in scope), with what it affects, and is read
  back.
- **Evidence (Phase 4).**
  - "What would convince you it works *as software*?" Propose this for the **Verified** state: tests
    of each rule or feature; known-answer tests where any exist.
  - When the science is in scope: "What would convince you it works *as science*?" Propose VAL-NN
    items for the **Validated** state, for example: reproducing a published result; parameter
    recovery on simulated data; reference calculations on a hand-checkable case; a pilot with
    people; the PI's walkthrough; comparison with an established tool.
  - "Are there published results, datasets or reference implementations we can check against?"
    These become known-answer tests.
- **Constraints (Phase 7).** Ask only what is relevant to a specific feature.
  - **Plan and budget.** Practitioner experience suggests light work fits a basic plan and
    sustained development a higher tier. Present this as experience, not a guarantee.
  - **Data and ethics.** Only when the work touches real data about people: where the data live,
    and any ethics approval reference. Ethics approval gates collecting human participant data; it
    does not stop building and testing with synthetic data. Real data about people means adding the
    human-subjects module.
  - **Deadline or milestones.**
  - **Models.** Which model access the PI has. Versions are recorded at the first session.
- **Platform.** Only after the vision and constraints are known: propose one from
  `engineering-defaults.md`, with a one-line reason, and ask for confirmation. A platform that fits
  the PI's community (an R package for R users, for example) affects adoption: treat it as a
  meaningful choice, not a technicality.

---

## Governance & Handoff (internal Phases 5, 6, 8, 9 and 10)

### Team and workspace (Phase 5)

Ask about the **task structure**, not about agents:

- "Can the work be split into parts that are built and tested independently? For example, the
  participant interface vs the data export, or the estimator vs the reporting."
- "How much does one part depend on decisions in another?"

**Recommend** (cite Kim et al. 2026 lightly if asked: whether more agents help depends on the task):

| Situation | Team arrangement | Workspace arrangement |
|---|---|---|
| Mostly sequential, small to medium, or first project | **Lead with subagents** (implementer, reviewer) | Shared checkout |
| Clearly separable parallel streams, PI comfortable with more moving parts | Peers (two or three) | **Worktrees**, with separate ports and output directories |
| Very small and tightly sequential | Solo, with review by a fresh subagent | Shared checkout |

Explain in one sentence: "You'll talk to one lead agent; it delegates and has work independently
reviewed; you see decisions and evidence, not the internal coordination."

### Authority, cadence and modules (Phase 6)

Turn the Intake profile into a concrete standing authorization (SA-01). Draft every field from what
you have heard, and ask the PI only to confirm or adjust it. Use plain words, not internal labels.

1. **Scientific boundaries.** "The team may decide on its own: … (for example, the number of
   replications in quick checks, the layout of outputs). It brings to you: … (for example, how
   'conflict' is coded, dropping a condition, changing a stopping rule)." Use **this project's**
   examples. For product-only work, describe the boundaries in product terms.
2. **Permitted assumption changes.** Under bounded autonomy, list the assumptions the team may set
   or change and must document. Under exploratory autonomy, describe the alternatives it may
   implement and compare. Under consult first, say "none without asking".
3. **When to come back.** Always include: a change to the research objective, exceeding agreed
   scope or resource limits, and settling a contested interpretation. Then add any project-specific
   triggers.
4. **Cadence.** [Check in at every sprint boundary.] The PI can ask for more frequent check-ins, or
   later authorize several sprints in a row. Every sprint boundary keeps its review and close-out.
5. **Practical limits.** Time, compute and cost limits per sprint, if any.
6. "Should the team ever run while you're away?" [No. This can be turned on later in words.]

Read SA-01 back in two or three sentences. Record the PI's reply verbatim as SA-01 (on import, the
next free SA number: see `import-path.md`, *Numbering*). If the reply is only an assent ("ok",
"adopted"), record the read-back text that was assented to, labelled "(read back by the lead; PI
assented: '<the PI's exact words>')". Never present your draft as the PI's words.

**Modules.** Select only the modules this project needs (`module-catalog.md`), and say why each one.

**Open questions and their dependencies.** For each unresolved question, note: what it **affects**
(requirements, work), when it is **needed by**, and what **can continue meanwhile**. These become
rows of the *Waiting on the PI* table in `DECISIONS.md`. An open question blocks only the work that
depends on it. Never invent a default that binds future scientific meaning to get a clean list.

### Read-back (Phase 8)

First ask whether the PI wants to discuss anything else. Add new topics and continue if they do.

Then present a **plain-language summary** of at most one screen:

- the purpose (verbatim) and what will be built;
- the first useful version and its essential requirements; later items; exclusions;
- the invariants and claims not to make, if the science is in scope;
- what Verified (and, if applicable, Validated) will mean;
- the platform and the team arrangement;
- the authority arrangement (SA-01), in plain words, with this project's examples, and the cadence;
- the modules selected;
- the broad roadmap: the first milestone, and later capabilities, provisional;
- open questions with what they affect and when they are needed, and any item still in draft
  wording.

Ask with `APPROVAL REQUIRED`, saying what a yes adopts: "If this is right, please say so in your own
words (for example 'Adopted' plus any changes). That sentence becomes ruling R-01, and the governing
files are then written from this summary" (on import: the inherited placeholder, or the next free R
number).

Record the reply **verbatim**. If the PI asks for changes, revise and read back again.

### Generate (Phase 9)

Follow `generation-checklist.md` exactly.

### Handoff (Phase 10)

Follow `SKILL.md`, *Closeout and handoff*. Setup writes no sprint record and never offers to begin
implementation.
