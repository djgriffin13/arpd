# Interview guide

Each phase below gives a **menu of coverage domains**, not a questionnaire. Pick what matters for
this project, add your own, and skip what the materials or earlier answers already settle (say what
you found instead). The wording is a suggestion. Defaults appear in **[brackets]**.

**Depth follows the project.**

- **Simple tools** (a file converter, a CSV cleaner): a few questions on the workflow and data, one
  or two architecture decisions, light governance; typically under a dozen exchanges.
- **Ordinary applications and data collection:** workflow, data semantics, persistence and export in
  real detail; the material architecture decisions explored; the rest defaulted.
- **Complex research software** (estimators, simulations, experimental platforms): equations,
  assumptions, edge cases, validation, performance; several decisions; perhaps parallel streams.

The interview is adaptive; the resulting report is thorough.

---

## Interview principles

1. Ask broad questions early, and targeted ones as the project becomes clear.
2. Do not ask for information already supplied, in the conversation or in the materials.
3. Do not ask the PI to confirm obvious implications of earlier answers. Record them as your
   interpretation and move on.
4. Explain why a question matters when that is not apparent. Before a sensitive question (ethics
   approval, personal data, institutional access), work out what the answer would change, and say
   so in one sentence. If the PI asks why, explain, and drop or narrow the question.
5. For a technical decision, present meaningful options, with what each means for the PI in practice.
6. Recommend a default when a reasoned one exists, with the reason in one plain sentence.
7. Accept open-ended answers, "please recommend", and changes to earlier answers. A change
   supersedes the earlier answer in the notes; the earlier words stay for provenance.
8. Respect requests to narrow scope or move forward, immediately. Keep what was already gathered.
9. Revisit a deferred question only when a later decision needs it, and say which decision.

**Further rules:**

- **"That's it."** This usually marks a scope boundary. Record it as one. It is not a complete
  specification: still raise, briefly, the uncertainties that would change the build, ask about the
  ones that matter, and propose defaults for the rest.
- **Batching.** Group only closely related, low-stakes items into one bounded choice, or state
  defaults ("Unless you say otherwise I will assume X, Y and Z"). Never ask two open questions in
  one turn. When an answer covers only part, record what is settled, and ask only the rest.
- **No empty turns** (`kit/docs/INTERACTION.md` §5). Never spend a turn on a trivial item: the PI's
  name in the records defaults to "PI".
- **Do not lead.** When asking what would convince the PI, ask it open first. Offer your proposed
  check only if the PI is unsure, and label it as yours.
- **Spend words where they pay:** a paragraph of trade-offs for architecture, data semantics and
  governance; none for trivia. Gloss a term once. Do not narrate the process.

---

## Project phase

Read the materials the PI points to: a proposal, a specification, design notes, code, earlier
decisions. A new repository does not mean the idea is new.

### Classification and routing

After the opening answer, classify the situation internally and record it in the notes (*Project
classification*). Never ask the PI to pick a class. Several may apply; re-classify as you learn.

| Situation | Emphasize | Usually light or skipped |
|---|---|---|
| New project, broad idea | Purpose, users, one typical session (propose one if the PI is unsure) | Fine performance targets |
| Developed requirements, or an existing project with documents | Read them; summarize; ask only about gaps and contradictions; reach Architecture sooner | Re-eliciting what is written |
| Existing repository to extend or modify | `import-path.md`, *Existing repository review* | Re-deciding valid existing choices |
| Computational or statistical method | *Correctness-critical semantics* (below); known answers; performance; the theory-context choice | UI detail |
| Data collection or research infrastructure | Who enters what, when; form configuration; identifiers; data semantics; persistence; export; privacy; distribution | Theory (the boundary is usually "constructs live in the PI's questions") |
| Simulation or experimental platform | Rules, timing and order; conditions; randomization and seeds; what participants see; logging; validation | Generic UX questions |
| General application | Users and roles, workflows, data, nonfunctional needs, distribution | The theory question (skip it) |
| Integration or automation tool | External interfaces, credentials, scheduling, failures and retries, idempotence; whether an existing tool can be configured instead | UI |
| Mixed | Split it into components, and route each | — |

**The objective of the phase:** you can say what is being built, why, for whom, what it should
accomplish, what already exists, and which parts are understood, uncertain, or open to your
recommendation. Do not jump early into theory, languages or implementation detail.

### Theory context (only when relevant)

Ask only when the description points to a theory, framework, mathematical model or set of
assumptions that could shape the tool. Skip it for general software, and for tools whose scientific
content lives entirely in material the PI supplies. Suggested lead-in, above the choice (its four
options are in `SKILL.md`):

> Is there a scientific theory, research framework, mathematical model or set of theoretical
> assumptions that should inform this tool? If so, you can describe them or point me to documents.

Give no recommendation unless correctness clearly depends on it. Record the answer in the notes
(*Theory context*); it goes to report §11 and, after adoption, to `STATUS.md` §8.

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

**Boundary rule.** If the PI says the tool only collects data, and the constructs live in questions
they will supply, record the boundary in the PI's words, put analysis and interpretation in the
exclusions, and move on to the product; do not return to the constructs. Read the signals early: "I
want to build the tool to help me do that" means product work now. Confirm it in passing inside the
next product question; do not defer the confirmation or keep exploring the theory meanwhile.

**Correctness-critical semantics.** For an estimator, a simulation, a measurement pipeline or any
theory-dependent model, the mathematics *is* the specification. Whatever the A–D answer, cover:
equations and definitions; assumptions; edge cases (empty groups, ties, out-of-range values,
non-convergence); numerical precision and tolerances; randomness and seeds; what the method refuses
to compute. Each becomes a requirement with acceptance criteria, usually known-answer or recovery
tests.

### The full paradigm-specification method (C, correctness-critical work, or on request)

1. **Constructs** (CON-NN): "What are the key constructs or mechanisms? How would you define each?"
   Verbatim. Offer a draft only after hearing the PI's view, labelled as yours.
2. **Operationalizations** (OP-NN): what the tool manipulates, records or computes, at what level and
   timing.
3. **Invariants** (INV-NN): propose three to eight from `module-catalog.md`, in scientific language;
   the PI accepts, edits or rejects each. Then ask: "Is there anything that, if the code got it
   wrong, would make the results meaningless?"
4. **Claims** (CLM-NN), and two to four claims not to make (NCL-NN).
5. **Assumptions** (ASM-NN): where a source is ambiguous, list the readings; record the PI's choice.
6. **Validation** (VAL-NN): *Verification*, under Requirements.

Label every item's origin (the PI's words, or drafted by the lead) and status. Silence is not
consent to a new scientific model. Draft wording on import: `import-path.md`, step 2 of *Steps for
an ARPD starter*.

---

## Requirements phase: coverage domains

**Begin with the scope sequence** (`SKILL.md`, *Scope: three questions, once each*) once the product
overview is clear. Record each answer verbatim in the notes, under the three tiers of
`docs/discovery/SETUP.md` §5 *Scope* (minimum usable version; ideal version and features of
interest; nice-to-have, not in the initial release), with any exclusions. Priorities follow
`SKILL.md`.

Then draw topics from the domains below. They are a menu: choose what bears on this project. Do not
invent user groups, features or constraints. A detail you supply is a labelled proposal.

### 1. Purpose and intended users

The problem; the users and their roles; the main scenarios; what users accomplish; the outputs; how
success would be recognized; the kind of use (personal, research, teaching, organizational).

### 2. Workflows and user experience

- **A typical session, end to end.** For a substantial product, ask: "Walk me through one complete
  use, from the moment someone starts it to the moment you have what you need." If the PI is unsure,
  propose a workflow for review, labelled as yours.
- the interface (graphical, command line, API, browser, desktop) and its main interactions;
- roles and permissions, where several kinds of user exist;
- errors and exceptions: wrong input, interruption, a crash mid-entry, a lost file;
- interactive, batch, automated or real-time operation.

### 3. Functional requirements

Sort every capability by the scope tiers (`SKILL.md`). Also: an explicitly excluded one goes to
report §2's exclusions; an existing capability to retain gets a regression acceptance criterion; one
that depends on an external system or data names the dependency, and goes to §12 if unresolved.
Avoid vague entries such as "supports data export": each requirement is numbered and testable
(*Requirements quality*, below).

### 4. Data and persistence (when relevant)

Cover, as relevant: the kinds of data, and input and output formats; where data are stored, and what
persists versus what is temporary; entities and relationships, and repeated observations or
sessions; integrity, provenance, versioning and compatibility; backup, recovery and export; privacy
and security.

**Data semantics are consequential** (`kit/constitution/CORE.md` §6). Raise them during
Requirements as ordinary product questions (one per turn, or naturally grouped), never saved for the
adoption block, and never decide them silently. Ask the consequential ones; propose defaults for the
rest. For a data-collection tool, most of these matter:

- **ask these first, whenever they change the data:** when people take part in groups or sessions,
  how a record identifies its class, session, group or site; how often an entry is made, and whether
  one person may make several; timestamps (recorded time versus event time, the time zone);
- missing versus zero versus "not applicable"; required versus optional items, and how a blank is
  stored and exported;
- the question types, and how each is coded in the output;
- duplicate or repeat submissions; editing or deleting saved records;
- identifier semantics: what an identifier means, who assigns it, how it is validated, and what
  happens when it is mistyped;
- aggregation, rounding and numerical precision;
- changes to the collected variables mid-use (a new question version), and how records show which
  version produced them;
- replacing unavailable data;
- shared computers; where data are saved;
- export: who exports, how often, file naming; cumulative or incremental, and whether a repeated
  export duplicates records; the encoding of free text (commas, quotes, line breaks, Unicode); how
  the output reaches the PI.

Not data semantics: reliability behaviours (autosave, crash recovery, export determinism) are
ordinary requirements with acceptance criteria, adopted with the report.

**Input adequacy.** Check that the inputs carry every quantity each output needs ("present but
silent" versus "absent" needs a roster, not only a log). An unresolved gap is an open item with a gate.

**Sensitive data.** Raise ethics or approval questions only when real data about people are
involved, and only once you know what the answer changes (for example, whether a consent screen is
in scope). Ethics approval gates collecting real data, not building and testing with synthetic
data. Real data about people means selecting the human-subjects module.

### 5. Performance, reliability and operating constraints (only where relevant)

Workload, runtime, number of users; memory, storage and compute limits; offline or online,
operating systems, managed or locked-down machines; recovery and reproducibility; maintainability.

Never demand numbers the PI has no basis for: propose a **provisional target and how to measure
it** ("10,000 records exported in under 5 seconds, by a timed test"), labelled a proposed default.

### 6. Future direction

The three scope answers already give the direction; do not ask about it again. Use them for one
architecture question only: which flexibility is genuinely needed now (for example, a data format
that must survive the ideal version's features). Keep the first version tractable.

### Verification

Ask openly first: "What would convince you that it works?" Then keep two things apart:

- **Implementation correctness (Verified):** unit, integration and regression tests; known answers;
  round trips for data (write, export, re-import, compare); independent review; a walkthrough.
- **Scientific validity (Validated), only when the science is in scope:** a published result
  reproduced; parameter recovery; a hand-checkable reference calculation; comparison with an
  established implementation; a pilot. For data collection it usually does not apply; accurate
  capture, persistence, export, recovery and integrity still do.

When validation comes up, say once: "The team can show the code matches the specification and
reproduces known answers. Only you can judge whether the specification captures what you mean, and
whether a result is meaningful."

### Requirements quality

Turn answers into an implementable specification, not a restatement. "It exports the answers as
CSV" is insufficient. Better:

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

Detail is proportional to complexity and risk; do not pad trivial requirements. You may propose
requirements and acceptance criteria, but **never silently convert a proposal into a PI-approved
requirement**: it stays Proposed until the PI accepts it in words.

---

## Architecture phase

Follow `architecture-guide.md`. Start a decision once the requirements that drive it are known; for
the platform that is often mid-Requirements, because distribution and storage depend on it.

---

## Team & Governance phase

Carry forward what the PI has already said about review depth, autonomy, check-ins and scientific
help. Draft from it; do not re-ask it. Ask only what is missing, preferably as one bounded choice
with defaults.

### Agent team arrangement (report §10)

Ask about the **task structure**, not about agents: can the work split into parts built and tested
independently? The arrangement is the **PI's choice**: put the recommended one (sized to the work,
from the table) and one short alternative in a `CHOICE FOR YOU`, with the check-in cadence (if the
PI has not stated it) and each proposed module (for example, human-subjects data) in the same block,
not left to the adoption assent. Never adopt an arrangement the PI was not asked about.

| Situation | Team arrangement | Workspace |
|---|---|---|
| Simple or tightly sequential | **Solo**, with review by a fresh subagent that did not write the code | Shared checkout |
| Most projects | **Lead with subagents** (implementer, reviewer; tester when the specification is rich) | Shared checkout, one subagent at a time |
| Clearly separable parallel streams, and a PI comfortable with more moving parts | **Peers** (two or three) under the lead, plus an independent tester when justified | **Worktrees**, with separate ports and output directories |

Never recommend a large team for a simple tool; say in one sentence why the arrangement suits the
task structure. If the PI chooses differently, record that it differs from your recommendation.
Roles and coordination: `kit/constitution/modules/team/team-arrangement.md`.

### Authority and governance (report §11)

Draft SA-01 from what you heard, in plain words with this project's examples, and ask the PI only to
confirm or adjust it. Its fields are the `kit/templates/DECISIONS.md` SA-01 entry; the profiles are
defined in `kit/constitution/CORE.md` §6 (propose one, [bounded autonomy], with each alternative in
one line). In particular:

- **Delegated:** implementation *mechanisms* only (code structure, libraries within the approved
  stack, file layout, test design, error-message wording).
- **Reserved:** data semantics are never delegated by default. Name this project's examples (how a
  blank is stored and exported, duplicates, identifier meaning, and so on). Delegate one only if the
  PI names a policy, and quote it. Add the standard triggers: a changed objective, exceeded scope or
  resource limits, a contested interpretation.
- **Review, cadence, limits:** review follows the PI's review depth (a PI who reads full drafts
  gets full plans). [A check-in at every sprint boundary], asked with the arrangement.
  Sprint plans are approved by the PI, changes independently reviewed, milestones closed with the
  PI's walkthrough; anything outside the adopted report needs a ruling. [The team does not run
  while the PI is away]; note any time, compute or cost limits.

Never present your draft as the PI's words; how an assent is recorded is in
`generation-checklist.md`, row 5. **Modules:** select only those this project needs
(`module-catalog.md`), and say why in §11; human-subjects data whenever the tool collects data from
or about people.

### Open decisions and gates (report §12)

For every unresolved item, record what it affects, its **gate** (before planning, before
implementing <a named feature>, or before deployment), what can continue meanwhile, and your
recommendation. An item without a gate is not allowed: "non-blocking" alone conceals it. Never
invent a binding default to get a clean list.

---

## Definition Report phase

Follow `generation-checklist.md`, Part A (draft, completeness check, presentation, review,
adoption), then Part B (generation), then `SKILL.md`, *Closeout and handoff*.
