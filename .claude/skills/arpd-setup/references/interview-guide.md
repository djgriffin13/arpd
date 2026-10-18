# Interview guide

The interview has five visible phases: Project → Requirements → Architecture → Team & Governance →
Definition Report. Each phase below gives a **menu of coverage domains**, not a questionnaire. Pick
what matters for this project, add your own, and skip what the materials or earlier answers already
settle (say what you found instead). The wording is a suggestion; adapt it. Defaults appear in
**[brackets]**.

Every turn follows `kit/docs/INTERACTION.md` and `SKILL.md`, *Every turn that waits for the PI*:
the progress line, one primary question, all topics re-evaluated after each reply, and the labelled
block last.

**Depth follows the project.**

- **Simple tools,** such as a file converter, a CSV cleaner, or a small form that saves answers:
  - a few questions on the workflow and the data;
  - one or two architecture decisions;
  - a light governance arrangement.

  Typically under a dozen exchanges before the draft report.
- **Ordinary applications and data collection:**
  - the workflow, the data semantics, persistence and export in real detail;
  - the material architecture decisions explored;
  - the rest defaulted.
- **Complex research software,** such as estimators, simulation engines or experimental platforms:
  - equations, assumptions, edge cases, validation and performance;
  - several architecture decisions;
  - possibly parallel work streams.

The interview is adaptive, but the resulting report is thorough. These goals go together.

---

## Interview principles

1. Ask broad questions early, and targeted ones as the project becomes clear.
2. Do not ask for information already supplied, in the conversation or in the materials.
3. Do not ask the PI to confirm obvious implications of earlier answers. Record them as your
   interpretation and move on.
4. Explain why a question matters when that is not apparent. Before a sensitive question (ethics
   approval, personal data, institutional access), work out what the answer would change, and say
   so in one sentence. If the PI asks why, explain, and drop or narrow the question.
5. For a technical decision, present meaningful options.
6. Give enough detail for an informed choice: what each option means for the PI in practice.
7. Recommend a default when a reasoned default exists, with the reason in one plain sentence.
8. Accept open-ended answers, "please recommend", and changes to earlier answers. A change
   supersedes the earlier answer in the notes; the earlier words stay for provenance.
9. Respect requests to narrow scope or move forward, immediately. Keep what was already gathered.
10. Revisit a deferred question only when a later decision needs it, and say which decision.

**Further rules:**

- **"That's it."** This usually marks a scope boundary. Record it as one. It is not a complete
  specification: the uncertainties that would change the build are still yours to raise. Raise them
  briefly, ask about the ones that matter, and propose defaults for the rest.
- **Batching.** Group only closely related, low-stakes items into one bounded choice, or state
  defaults ("Unless you say otherwise I will assume X, Y and Z"). Never ask two open questions in
  one turn. When an answer covers only part, record what is settled, and ask only the rest.
- **No empty turns.** Never spend a turn on a trivial item (the PI's name in the records defaults to
  "PI"), on a pure phase transition, or on "anything else?" alone. Put the synthesis and the offer to
  move on in the same turn as the next real question.
- **Do not lead.** When asking what would convince the PI, ask it open first. Offer your proposed
  check only if the PI is unsure, and label it as yours.
- **Longer explanations where they pay.** Architecture, data semantics and governance choices
  deserve a paragraph of trade-offs. Trivial ones deserve none.
- **Explain when needed, once.** Gloss a technical term the first time it matters. Do not describe
  the interview process on every turn.

---

## Project phase

### Inspection and mode (before the first question)

1. **Detect the mode.**
   - Run `git status` and list the top level.
   - The mode is **fresh** if the repository contains only the kit. That means `kit/`,
     `.claude/skills/arpd-*`, `docs/`, `evaluation/`, `examples/`, and the kit's own `README.md`,
     `QUICKSTART.md`, `CLAUDE.md`, `AGENTS.md`, `LICENSE`, `CITATION.cff`, `RELEASE-NOTES.md` and
     dotfiles. The kit's own files are not prior instructions.
   - Follow `import-path.md` if the PI passed `import <path|url>` or `install <path>`, or if the
     project's own code or instruction files are present. A starter inside the kit (for example
     `examples/march-1991/`) is an import of an ARPD project.
2. **Check for a partial setup** (`import-path.md`, *Resuming an interrupted setup*).
3. **Read the materials** the PI points to: a proposal, a specification, design notes, code,
   earlier decisions. A new repository does not mean the idea is new.
4. **Ask the opening question** exactly as in `SKILL.md`, *Start*. Ask nothing about interview mode,
   research maturity, coding or AI-tool experience, or adviser role.

### Classification and routing

After the opening answer, classify the situation internally. Record the class in the notes
(*Project classification*). Never ask the PI to pick a class. Several may apply; re-classify as you
learn.

| Situation | Emphasize | Usually light or skipped |
|---|---|---|
| New project, broad idea | Purpose, users, one typical session; propose a workflow if the PI is unsure; a small first version | Fine performance targets |
| New project, developed requirements | Read them; summarize; ask only about gaps and contradictions; reach Architecture sooner | Re-eliciting what is written |
| Existing project with documents | Read the documents; confirm what they settle; ask about gaps | The full fresh discovery |
| Existing repository to extend or modify | `import-path.md`, *Existing repository review*: what exists, what to reuse, the requested change, compatibility and migration | Re-deciding valid existing choices |
| Computational or statistical method | Equations, assumptions, edge cases, inputs and outputs, numerical precision, known answers, performance; the theory-context choice | UI detail |
| Data collection or research infrastructure | Who enters what, when; question or form configuration; identifiers; data semantics; persistence; export; privacy; distribution | Theory (the boundary is usually "constructs live in the PI's questions") |
| Simulation or experimental platform | Rules, timing and order; conditions; randomization and seeds; what participants see; logging; validation | Generic UX questions |
| General application | Users and roles, workflows, data, nonfunctional needs, distribution | The theory question (skip it) |
| Integration or automation tool | The external systems and their interfaces, credentials handling, scheduling, failures and retries, idempotence, logging; whether an existing automation tool can be configured instead | UI |
| Mixed | Split it into components, and route each | — |

### The interview objective

By the end of the Project phase you can say:

1. what is being built;
2. why;
3. who will use it;
4. what it should accomplish;
5. what already exists;
6. which parts are understood, which are uncertain, and which are open to your recommendation.

Do not jump early into theory, languages or implementation detail.

### Theory context (only when relevant)

Ask this only when the description points to a theory, framework, mathematical model or set of
assumptions that could shape the tool. Skip it for general software, and for tools whose scientific
content lives entirely in material the PI supplies.

Suggested wording (above the block, then the choice):

> Is there a scientific theory, research framework, mathematical model or set of theoretical
> assumptions that should inform this tool? If so, you can describe them or point me to documents.

```text
────────────────────────────────
CHOICE FOR YOU (select one)
How should I treat that theory?
A. Use it to guide implementation, without evaluating it.
B. Identify potential theoretical or methodological concerns.
C. Actively help develop or refine the theoretical approach.
D. Focus on the tool itself and leave theoretical questions aside.
────────────────────────────────
```

Give no recommendation unless correctness clearly depends on it. Record the answer in the notes
(*Theory context*). It goes to the report §11 and, after adoption, to `STATUS.md` §8 as the
PI's preference about scientific help.

| Choice | What you do |
|---|---|
| A | Record the context the tool must represent, in the PI's words. Ask only what correctness needs. No critique. |
| B | Raise concerns briefly where they matter for the build or the claims, as labelled lead observations. The PI decides what to do with each one. |
| C | Use the full method below, to the depth the PI wants. |
| D | Record "theory out of scope (PI's choice)". Ask nothing further about it. |

**Ambiguity triage.** Classify each scientific ambiguity you notice:

| Kind | Example | In setup |
|---|---|---|
| 1. Affects the implementation | Which formula, which unit of analysis, whether an item may be skipped | **Pursue** |
| 2. Affects only later analysis | How the PI will model the collected answers | Record it in the notes; do not pursue |
| 3. Prevents a valid design | Two requirements that cannot both hold; an estimator undefined for the stated data | **Pursue** |
| 4. Deferred by the PI | "I'll define that later" | Record it with what it affects and its gate |

**Boundary rule.** The PI may say that the tool only collects data, and that the constructs are
defined in questions they will supply. Then record the boundary in the PI's words, put analysis and
interpretation in the exclusions, and move on to the product. Do not return to the constructs.
Read the signals early. "I want to build the tool to help me do that" means product work now.
Confirm it in passing inside the next product question; do not defer the confirmation, and do not
keep exploring the theory meanwhile.

**Correctness-critical semantics.** For an estimator, a simulation, a measurement pipeline or any
theory-dependent model, the mathematics *is* the specification. Whatever the A–D answer, cover:

- equations and definitions;
- assumptions;
- edge cases (empty groups, ties, out-of-range values, non-convergence);
- numerical precision and tolerances;
- randomness and seeds;
- what the method refuses to compute.

Each becomes a requirement with acceptance criteria, usually known-answer or recovery tests.

### The full paradigm-specification method (C, correctness-critical work, or on request)

1. **Constructs and mechanisms.** "What are the key constructs or mechanisms? How would you define
   each?" Record each definition verbatim (CON-NN). Offer a draft only after hearing the PI's view,
   labelled as yours.
2. **Operationalizations.** What the tool manipulates, records or computes, at what level and timing
   (OP-NN).
3. **Candidate invariants.** Using `module-catalog.md`, propose three to eight in scientific
   language. The PI accepts, edits or rejects each (INV-NN). Then ask: "Is there anything that, if the
   code got it wrong, would make the results meaningless?"
4. **Claims.** What results should let the PI say (CLM-NN), and two to four claims not to make
   (NCL-NN).
5. **Assumptions** (ASM-NN). Where a source is ambiguous, list the interpretations and record the
   PI's choice.
6. **Validation** (VAL-NN): see *Verification*, under Requirements.

Label every item's origin (the PI's words, or drafted by the lead) and status. Silence is not
consent to a new scientific model.

**Draft wording on import.** An item marked *"(draft wording, awaiting the PI's words)"* needs the
PI's own words. Otherwise it stays pending, with a gate, in the report §12. Adopting "as it stands"
does not clear the marker. For product-only work, do not create a pending research question; the
PI's purpose, verbatim, is enough.

---

## Requirements phase: coverage domains

**Begin with the scope sequence** (`SKILL.md`, *Scope: three questions, once each*), once the
product overview is clear:

1. the minimum usable version;
2. the ideal version, with the features named;
3. the nice-to-haves not expected in the initial release.

Ask each once, as its own question, and skip any already answered. Record each answer verbatim in
the notes (*First useful version*, *Vision*, *Later, wishlist and exclusions*). Then:

- **minimum** features are priority **required**;
- **ideal** features beyond the minimum are **desired**, or **future** when the PI places them after
  the first release;
- **nice-to-haves** are **later**: report §9 deferred features, and the backlog.

Never ask about scope, vision or a wishlist again in another form. Ask about a single feature's
placement only when it is genuinely unclear and matters now.

Then draw topics from the domains below. They are a menu: choose what bears on this project. Do not
invent user groups, features or constraints. A detail you supply is a labelled proposal.

### 1. Purpose and intended users

- the problem being addressed;
- the intended users and their roles;
- the primary usage scenarios;
- what users should be able to accomplish;
- the expected outputs and deliverables;
- how success would be recognized;
- whether the use is personal, research, educational, commercial or organizational, when relevant.

### 2. Workflows and user experience

- **A typical session, end to end.** For a substantial product, ask: "Walk me through one complete
  use, from the moment someone starts it to the moment you have what you need." If the PI is unsure,
  propose a workflow for review, labelled as yours.
- the main interactions, inputs and outputs;
- the interface: graphical, command line, API, browser, desktop, or a combination;
- roles and permissions, where several kinds of user exist;
- common errors and exceptions: wrong input, interruption, a crash mid-entry, a lost file;
- interactive, batch, automated or real-time operation.

### 3. Functional requirements

Sort every capability:

| Kind | Where it goes in the report |
|---|---|
| Required (the minimum usable version) | §3, priority "required" |
| Desired (the ideal version) | §3, priority "desired" |
| Possible future (ideal, after the first release; or nice-to-have) | §3 priority "future", or §9 deferred features |
| Explicitly excluded | §2 scope exclusions |
| Existing capability to retain | §3, with a regression acceptance criterion |
| Dependent on an external system or data | §3, with the dependency named; §12 if unresolved |

Avoid vague entries such as "supports data export". Each requirement is eventually numbered and
testable (*Requirements quality*, below).

### 4. Data and persistence (when relevant)

Cover, as relevant:

- the kinds of data, and the input and output formats;
- where data are stored, and what persists versus what is temporary;
- entities and relationships, and repeated observations or sessions;
- integrity and provenance, versioning and compatibility;
- backup, recovery and export;
- privacy and security.

**Data semantics are consequential** (`kit/constitution/CORE.md` §6). Raise them as product
questions, and never decide them silently:

- missing versus zero versus "not applicable";
- required versus optional items, and how a blank is stored and exported;
- duplicate or repeat submissions, and edits or deletions of saved records;
- identifier semantics: what an identifier means, who assigns it, how it is validated, and what
  happens when it is mistyped;
- timestamps: recorded time versus event time, and the time zone;
- aggregation, rounding and numerical precision;
- changes to the collected variables mid-use (a new question version), and how records show which
  version produced them;
- replacing unavailable data.

**For a data-collection tool,** these topics usually matter. Ask the consequential ones, and
propose defaults for the rest:

- how often an entry is made;
- how a session, class, site or occasion is identified;
- the question types and how each is coded in the output;
- which items are required and which optional;
- timestamps;
- identifier validation;
- editing or deleting entries;
- shared computers;
- where and how data are saved, and what happens on a crash;
- who exports, how often, and how files are named;
- whether exports are cumulative or incremental, and whether a repeated export duplicates records;
- the encoding for free text (commas, quotes, line breaks, Unicode);
- how the output reaches the PI.

**Input adequacy.** For each output, check that the inputs carry every quantity it needs. For
example, telling "present but silent" from "absent" needs a roster, not only a log. A gap the PI
cannot resolve now becomes an open item with a gate.

**Sensitive data.** Raise ethics or approval questions only when real data about people are
involved, and only once you know what the answer changes (for example, whether a consent screen is
in scope). Ethics approval gates collecting real data. It does not stop building and testing with
synthetic data. Real data about people means selecting the human-subjects module.

### 5. Performance, reliability and operating constraints (only where relevant)

Cover only what bears on this project:

- workload or dataset size, runtime or responsiveness, and the number of users;
- memory, storage and compute limits;
- offline versus online operation, operating systems, and managed or locked-down machines;
- availability, error recovery and reproducibility;
- portability and maintainability.

Do not demand numbers the PI has no basis for. Propose a **provisional target and how to measure
it**, for example: "export of 10,000 records in under 5 seconds on a typical laptop, measured by a
timed test". Label it a proposed default, distinct from a target the PI stated.

### 6. Future direction

The three scope answers already give the direction. Do not ask about it again. Use them for one
architecture question only: which flexibility is genuinely needed now, for example a data format
that must survive the ideal version's features. Keep the first version tractable.

### Verification

Ask openly first: "What would convince you that it works?" Then distinguish two things:

- **Implementation correctness (Verified):**
  - unit and integration tests;
  - regression tests;
  - known-answer tests where they exist;
  - round-trip checks for data (write, export, re-import, compare);
  - independent review;
  - a manual acceptance walkthrough.
- **Scientific or computational validity (Validated), only when the science is in scope:**
  - reproducing a published result;
  - parameter recovery on simulated data;
  - reference calculations on a hand-checkable case;
  - comparison with an established implementation;
  - a pilot with people.

For a data-collection tool, model validation usually does not apply. Accurate capture,
persistence, export, recovery and integrity still do.

When validation comes up, say once: "The team can show the code matches the specification and
reproduces known answers. Only you can judge whether the specification captures what you mean, and
whether a result is meaningful."

### Requirements quality

Turn answers into an implementable specification, not a restatement. For example, "it exports the
answers as CSV" is insufficient. Better:

> **REQ-EXPORT-01: Export stored records.** The tool exports every locally stored record to one
> CSV file, without altering the recorded content.
> Acceptance criteria:
> - every required field appears, with the header row in the order given in §7;
> - identifiers are preserved exactly;
> - each stored record appears once: none duplicated, none omitted, across repeated exports;
> - free text containing commas, quotation marks, line breaks and non-ASCII characters survives
>   intact;
> - a test export, re-imported, matches the stored records field by field.
>
> Status: Proposed (the lead's derivation from the PI's "export as a CSV file"). The column layout
> stays provisional until the PI approves it, or delegates it with bounds.

- Detail is proportional to complexity and risk. Do not pad trivial requirements.
- You may propose requirements and acceptance criteria. **Never silently convert a proposal into a
  PI-approved requirement.** Its status stays Proposed until the PI accepts it in words.

---

## Architecture phase

Follow `architecture-guide.md`. Start only when the requirements that drive a decision are known.
That often happens mid-Requirements for the platform, because distribution and storage depend on
it. Each material decision gets one turn with real trade-offs and a recommendation, ending in a
`CHOICE FOR YOU (select one)`. Record the PI's choice in the notes (*Architecture alternatives
explored*), with the PI's words. It is a preference until the report is adopted.

---

## Team & Governance phase

Carry forward what the PI has already said about review depth, autonomy, check-ins and scientific
help. Draft from it; do not re-ask it. Ask only what is missing, preferably as one bounded choice
with defaults.

### Agent team arrangement (report §10)

Ask about the **task structure**, not about agents: can the work split into parts built and tested
independently, and how much do the parts depend on each other? Then recommend in proportion:

| Situation | Team arrangement | Workspace |
|---|---|---|
| Simple or tightly sequential | **Solo**, with review by a fresh subagent that did not write the code | Shared checkout |
| Most projects | **Lead with subagents** (implementer, reviewer; tester when the specification is rich) | Shared checkout, one subagent at a time |
| Clearly separable parallel streams, and a PI comfortable with more moving parts | **Peers** (two or three) under the lead, plus an independent tester when justified | **Worktrees**, with separate ports and output directories |

- Never default to a large team for a simple tool. Explain in one sentence why the arrangement suits
  the task structure.
- If the PI chooses differently, respect it, and record that it differs from your recommendation.
- Describe the roles and the coordination flow from `kit/constitution/modules/team/team-arrangement.md`:
  - the lead plans, briefs, integrates, and is the only writer of status;
  - implementers work one plan each;
  - reviewers did not write the change;
  - who integrates, and how the PI sees decisions and evidence, not the internal coordination.

### Authority and governance (report §11)

Draft SA-01 from what you heard, and ask the PI only to confirm or adjust it. Use plain words and
this project's examples.

1. **Profile.** Propose one, and explain the alternatives in one line each:
   - **bounded autonomy** [default]: works within the agreed boundaries, records material
     assumptions, and reports at checkpoints;
   - **consult first**: asks before adopting any consequential assumption;
   - **exploratory autonomy**: tries and compares alternatives, then returns for adoption.
2. **Delegated decisions.** List what the team decides alone. These are implementation
   *mechanisms*: code structure, libraries within the approved stack, file layout, test design,
   error-message wording.
3. **Reserved to the PI.**
   - **Data semantics are never delegated by default** (CORE §6). Name this project's examples:
     how a blank answer is stored and exported, duplicate handling, identifier meaning, aggregation,
     precision, changes to collected variables, and replacing unavailable data.
   - Delegate one only if the PI names a policy, and quote that policy in the SA.
   - Add the standard triggers: a changed objective, exceeded scope or resource limits, a contested
     interpretation.
4. **Review expectations.** These follow the PI's review depth. If the PI wants to read full drafts,
   the report must be the full specification, and plans come in full.
5. **Cadence and reporting.** [A check-in at every sprint boundary.] The PI may ask for more
   frequent ones, or authorize several sprints in a row later. Ask once only if the PI has not said.
6. **Approval and merge gates.** Each sprint plan is approved by the PI. Each change is
   independently reviewed before it merges. Each milestone closes with the PI's walkthrough.
7. **Scope changes.** Anything outside the adopted report needs a ruling. Discoveries are filed to
   the backlog, not built.
8. **Autonomy limits.** [The team does not run while the PI is away.] Note any time, compute or
   cost limits.

Record the PI's reply verbatim. If it is only an assent, record the drafted text with "(drafted by
the lead; PI assented: '<the PI's exact words>')". Never present your draft as the PI's words. SA-01
is written to `DECISIONS.md` only at generation.

**Modules.** Select only the modules this project needs (`module-catalog.md`), and say why in §11.

### Open decisions and gates (report §12)

For every unresolved item, record:

- what it affects;
- its **gate**: before planning, before implementing <a named feature>, or before deployment;
- what can continue meanwhile;
- your recommendation.

An item without a gate is not allowed: "non-blocking" alone conceals it. Never invent a binding
default to get a clean list.

---

## Definition Report phase

Follow `generation-checklist.md`, Part A (draft, completeness check, presentation, review,
adoption), then Part B (generation), then `SKILL.md`, *Closeout and handoff*.
