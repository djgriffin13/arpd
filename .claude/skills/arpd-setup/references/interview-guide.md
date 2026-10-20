# Interview guide

Each phase below lists its **required items**: the answers setup needs before the phase can close.
They are a coverage list, not a questionnaire. Fill them from the folder, the PI's materials and
earlier answers first; ask only for what is still Open (`SKILL.md`, *The interview*). The wording of
each question is a suggestion. Defaults appear in **[brackets]**. The **Feeds** column says what each
item is for: an item that feeds nothing in this project is N.A., not asked.

**Depth follows the project.**

- **Simple tools** (a file converter, a CSV cleaner): most items are filled by the opening answer;
  short phases, one or two architecture decisions, light governance.
- **Ordinary applications and data collection:** workflow, data semantics, persistence and export in
  real detail; the material architecture decisions explored; the rest defaulted.
- **Complex research software** (estimators, simulations, experimental platforms): research
  questions, model commitments, equations, edge cases, validation and performance in depth; several
  design decisions; perhaps parallel streams.

The interview is adaptive; the resulting report is thorough.

---

## Interview principles

1. Ask broad questions early, and targeted ones as the project becomes clear.
2. Do not ask for information already supplied, in the conversation, the folder or the materials.
3. Do not ask the PI to confirm obvious implications one by one. Record them as Inferred; the phase
   summary confirms them together.
4. Explain why a question matters when that is not apparent. Before a sensitive question (ethics
   approval, personal data, institutional access), work out what the answer would change, and say
   so in one sentence. If the PI asks why, explain, and drop or narrow the question.
5. For a technical decision, present meaningful options, with what each means for the PI in practice.
6. Recommend a default when a reasoned one exists, with the reason in one plain sentence.
7. Accept open-ended answers, "please recommend", and changes to earlier answers. A change
   supersedes the earlier answer in the notes; the earlier words stay for provenance. A change may
   reopen an earlier phase: say which items it reopens.
8. Respect requests to narrow scope or move forward, immediately. Keep what was already gathered.
9. Revisit a deferred item only when a later decision needs it, and say which decision.

**Further rules:**

- **"That's it."** This usually marks a scope boundary. Record it as one. It is not a complete
  specification: still raise, briefly, the uncertainties that would change the build, ask about the
  ones that matter, and propose defaults for the rest.
- **Batching.** Group only closely related, low-stakes items into one bounded choice, or state
  defaults ("Unless you say otherwise I will assume X, Y and Z"). Never ask two open questions in
  one turn. When an answer covers only part, record what is settled, and ask only the rest.
- **No empty turns** (`arpd/docs/INTERACTION.md` §5). Never spend a turn on a trivial item: the PI's
  name in the records defaults to "PI".
- **Do not lead.** When asking what would convince the PI, ask it open first. Offer your proposed
  check only if the PI is unsure, and label it as yours.
- **Spend words where they pay:** a paragraph of trade-offs for architecture, data semantics,
  model commitments and the agent workflow; none for trivia. Gloss a term once.
- **Never infer one thing about the PI from another:** coding comfort says nothing about research
  expertise, and neither says how involved the PI wants to be.

---

## Phase 1: Intake

**Objective:** you can say who the PI is (as far as it matters), what is being done at a high level,
what the agent's role is, where the project lives, and what the next phases must explore; enough to
prepare the project folder and to know which kinds of questions follow.

The opening question (`SKILL.md`, *Start*) usually fills IN-01, IN-06 and IN-07, and often more.

| ID | Required item | Feeds | Notes |
|---|---|---|---|
| IN-01 | State of the work: existing documents, code or data, and where they are | What to read and reuse; the mode | From the folder assessment and the PI's answer. Read what the PI points to. |
| IN-02 | Academic field and high-level theoretical scope | How theory-aware the next phases are; vocabulary; modules | One or two sentences is enough. |
| IN-03 | The PI's coding comfort, and how involved they want to be in technical decisions | Depth of the Design phase; how much is proposed versus asked; review depth | Two answers, both Confirmed only from the PI's words. Ask once, plainly, when the PI has not said it ("How comfortable are you with code: do you write it, run scripts others wrote, or prefer not to touch it?"), never as a test; a reading of how the PI writes is at most Inferred, and stated in the Intake summary for the PI to correct. |
| IN-04 | The tool's eventual users, and who will run and maintain it afterwards | Interface, distribution, language and documentation choices | The PI is often not the only user. Ask unless the PI said; never infer users the PI did not mention. |
| IN-05 | Where the project lives | The folder preparation | Asked right after the opening answer (`import-path.md`, *Where the project lives*). |
| IN-06 | The main goal of this effort, and what is to be built, at a high level | Everything after | Build, extend, review or explore. |
| IN-07 | Where the PI is in development: idea, specified, prototype, working code, mature | Which phases are long or short | Usually inferred. |
| IN-08 | The agent's role (*Roles*, below), and from it the scientific axis | How far you go in design and in the science | One choice; the scientific axis is inferred from it and confirmed in the summary. |
| IN-09 | Known constraints or preferences, each marked must or prefer | Early routing; opens the Constraints phase | One open question (below). Not the full constraints interview. |
| IN-10 | Timeline or deadline | Proportionality; the roadmap | Only when the rest suggests it matters, or the PI mentions it. |

**IN-09, suggested wording:**

> Are there any important project or system constraints or preferences I should know about at this
> point? For example: programming languages, operating systems, internet access, costs or credit
> use, deadlines, data access, institutional rules, or theoretical frameworks. Please say which are
> requirements and which are preferences.

Do not ask at intake which features are essential and which desirable; that belongs to Development.

### Roles (IN-08)

Ask as one `CHOICE FOR YOU (select one)`, after the PI's goal is clear:

```text
────────────────────────────────
CHOICE FOR YOU (select one)
What role would you like me to play in this project?
A. Build what you specify. I raise only problems that would stop it working.
B. Review your technical plan, then build it. The research ideas are taken as you give them.
C. Review the technical plan and how well it fits the theory or research question, then build it.
D. Help you work out what to build for your research question: design the tool, and help develop
   the science behind it, with you.
E. Audit, repair or extend existing code, and bring it under ARPD's way of working.
F. Explore ideas with you; there is no particular tool in mind yet.
Or describe another role.
────────────────────────────────
```

Print all six options with exactly these letters, in this order, every time: the letters are the
role codes recorded in the notes, the report and the charter, so never reorder, re-letter or drop
one (mark the recommended one instead). Recommend one when the opening answer points to it, with the
reason. Record the role on two axes:

| Role | Technical axis | Scientific axis [inferred default] |
|---|---|---|
| A | Builder | **Technical only** |
| B | Reviewer and builder | **Respect as given**: the science guides the implementation, without critique |
| C | Reviewer and builder | **Alignment review**: labelled concerns where theory and design meet |
| D | Co-designer | **Co-development**: the full paradigm method, to the depth the PI wants |
| E | Auditor and builder | Ask in the summary: usually *respect as given* |
| F | Exploration | Co-development, then *No tool in view* (`SKILL.md`) |
| Other | From the PI's words | From the PI's words |

Whatever the role: correctness-critical semantics are specified, and contradictions and circularity
in the model commitments are flagged (`SKILL.md`, *Science*).

### Classification and routing

After the opening answer, classify the situation internally and record it in the notes (*Project
classification*). Never ask the PI to pick a class. Several may apply; re-classify as you learn.

| Situation | Emphasize | Usually light or skipped |
|---|---|---|
| New project, broad idea | Objectives and research purpose; one typical session (propose one if the PI is unsure) | Fine performance targets |
| Developed requirements, or documents | Read them; summarize; ask only about gaps and contradictions; reach Design sooner | Re-eliciting what is written |
| Existing repository to extend or modify | `import-path.md`, *Existing repository review* | Re-deciding valid existing choices |
| Computational or statistical method | *Correctness-critical semantics*; known answers; performance; model commitments | UI detail |
| Data collection or research infrastructure | Who enters what, when; form configuration; identifiers; data semantics; persistence; export; privacy; distribution | Theory (the boundary is usually "constructs live in the PI's questions") |
| Simulation or experimental platform | Rules, timing and order; conditions; randomization and seeds; what participants see; logging; validation; model commitments | Generic UX questions |
| General application | Users and roles, workflows, data, nonfunctional needs, distribution | Theory |
| Integration or automation tool | External interfaces, credentials, scheduling, failures and retries; whether an existing tool can be configured instead | UI |
| Mixed | Split it into components, and route each | — |

**Intake summary** (the closeout) states, at a minimum: who the PI is as far as it matters (field,
coding comfort, involvement), the tool's users and maintainers, what will be built at a high level,
the state of the work, the role and its scientific axis, where the project lives, the known
constraints (must / prefer), and what Objectives, Constraints and Design will need to explore.

---

## Phase 2: Objectives

**Objective:** a list of specific objectives, capabilities and candidate requirements, and, unless
the role is technical only, a description of the research domain and the research questions the tool
serves, each linked to what it requires of the tool.

**Technical only:** open the phase by saying once that research questions and theoretical alignment
are out of focus because the PI asked for a technical tool, and that they can ask for more attention
to the theoretical foundations at any time. OB-01 and OB-02 are then N.A.

**Opening question** (adapt it; skip what is already known):

> Tell me about the project in your own words. What do you want to do with this tool? What research
> or theoretical questions should it help answer, and how? What do you want me to accomplish, and
> what tool or tools do you picture?

Then narrow: objective and feature questions, and research-domain and research-question questions,
one at a time, until the items are filled.

| ID | Required item | Feeds |
|---|---|---|
| OB-01 | The research domain: phenomena, constructs or problems the tool is about | `PARADIGM-SPEC.md` §1; report §2 |
| OB-02 | Research questions: specific ones, or, for a general platform, illustrative ones it must support | The capabilities; the claims the tool may support |
| OB-03 | Objectives: what the PI wants to achieve with the tool, in their words | Milestones; the roadmap |
| OB-04 | Capabilities and features: what users must be able to do | Functional requirements |
| OB-05 | The links: research purpose → capability → requirement | Traceability (report §2); priorities later |
| OB-06 | How the outputs will be used: exploration, teaching, publication, operations, decisions | Validation, reproducibility, provenance and versioning requirements |
| OB-07 | What would convince the PI it works | Acceptance criteria; report §10 |
| OB-08 | What the tool will not do (exclusions): ask, unless the PI named them; a policy on something else is not an exclusion | Scope boundary; `PARADIGM-SPEC.md` §8 |

- **Questions are not requirements.** A research question says why a capability matters; a
  requirement says what must be implemented and how it is checked. Keep the three levels apart and
  linked: "When does decentralized coordination outperform centralized coordination?" (question) →
  "set up teams with different communication structures and decision rights" (capability) → "the
  simulator implements both information-sharing rules and logs every decision with its condition and
  seed" (requirement).
- **Do not force a narrow question onto a general platform.** A statistical package or experiment
  platform may serve many studies; illustrative questions are enough unless the design depends on a
  particular one.
- **Turn intended use into requirements.** "For publication" usually means reproducible runs,
  recorded versions and seeds, and outputs a reader can check; "for teaching" may mean defaults and
  explanations. Say what the use implies, as proposals.
- **Brainstorming is welcome here,** within the role: possible capabilities, alternative ways a tool
  could address the question, what different theories would need it to represent. Label what is
  established (with a verified source), what is a plausible but unverified idea, and what is your
  speculation (`SKILL.md`, *Sources*).
- **Verification, asked openly first** (OB-07): "What would convince you that it works?" Then keep
  two things apart:
  - **Implementation correctness (Verified):** unit, integration and regression tests; known
    answers; round trips for data; independent review; a walkthrough.
  - **Scientific validity (Validated), only when the science is in scope:** a published result
    reproduced; parameter recovery; a hand-checkable reference calculation; comparison with an
    established implementation; a pilot.

  When validation comes up, say once: "The team can show the code matches the specification and
  reproduces known answers. Only you can judge whether the specification captures what you mean, and
  whether a result is meaningful." Keep four things distinct throughout: the PI's **intent**, the
  **specification**, the **implementation**, and **empirical validation**.

**No tool in view:** `SKILL.md`. **Objectives summary:** the domain and questions (or "technical
only, by the PI's choice"), the objectives, the capabilities with their links, the intended use and
what it implies, the success evidence, and the exclusions.

---

## Phase 3: Constraints

**Objective:** a clear, classified list of every constraint, stated or inferred, on the system, the
tool's use and (unless technical only) the theory, with contradictions resolved or recorded.

**Part A: system and tool.** Open from IN-09 ("You mentioned X and Y"), then ask once, broadly:

> Please give me as complete a picture as you can of the constraints you know about. For example:
> must it work offline or can it use the internet? Must it be free to use? Is there a required
> language or version (say, Python 3.8)? Must it run on Windows and Mac? Are there limits on cost,
> computing or agent credit use? Where may data be stored? Are there institutional, ethics or licence
> rules?

Then follow up: open ("You said ___; can you say more?") or bounded ("This looks like a constraint.
Should I A. treat it as a requirement, B. treat it as a preference, C. drop it?").

**Part B: theory** (skipped, and said to be skipped, when technical only; then CS-06 is N.A. by the
PI's choice, and CS-07 still runs on any invariant or commitment that correctness-critical semantics
or the PI's own words introduce):

> Are there constraints on the theoretical side of this project? For example, frameworks or bodies of
> work it should draw on or avoid, assumptions the model must make, or things it must not try to
> represent.

| ID | Required item | Feeds |
|---|---|---|
| CS-01 | Platform and environment: operating systems, offline or online, managed machines | Platform decision; distribution |
| CS-02 | Resources and cost: free to use, budget, compute, agent credit use | Architecture; the team arrangement and review depth (Development) |
| CS-03 | Technology: required or preferred languages, versions, libraries, existing tools | Architecture alternatives |
| CS-04 | Data and institution: where data may live, privacy, ethics approval, licences, institutional rules | Storage; modules; gates |
| CS-05 | Use: who uses it, where, when, how often; deadlines | Workflow; nonfunctional targets; roadmap |
| CS-06 | Theory: frameworks to draw on or avoid, required assumptions, what not to model | Model commitments; `PARADIGM-SPEC.md` |
| CS-07 | The commitments review, done and decided (below) | Invariants, assumptions and research questions |

**Classes shown to the PI:**

| Class | Meaning | Example |
|---|---|---|
| **Must** | A hard constraint: the design may not violate it | Runs offline on Windows and macOS |
| **Prefer** | A preference: alternatives may be discussed | Python, because students know it |
| **Model commitment** | An assumption, framework or exclusion the model adopts, with its epistemic status: *established* (with a verified source), *assumed for this model*, or *a hypothesis to test* | Actors use only information available at the time; personality is not modelled |
| **Must hold** | An invariant the code must never violate (INV-NN); never a hypothesis | Future observations never influence earlier decisions |
| **Open question** | Something the project will investigate, not a rule | Whether coordination emerges from local rules |

A theoretical exclusion ("does not model personality") is a scope boundary, not a claim that the
excluded thing is irrelevant. A preference to draw on or avoid a body of work is a **framing choice**:
record it as such, and say once that it delimits the model; it is not an instruction to ignore
relevant contrary evidence when the PI asks what the literature says.

### Commitments review (before the Constraints closeout)

Review every model commitment, invariant and theory constraint critically, at the depth the role
allows, and present the result as labelled observations:

1. **Contradiction:** two commitments that cannot both hold, or a commitment that conflicts with a
   requirement or constraint. *Flagged under every role.*
2. **Circularity:** the tool would build in the answer it is meant to find, for example a hypothesis
   ("more communication always improves performance") written as a fixed rule or invariant of a
   simulation meant to study it. *Flagged under every role.*
3. **Questionable assumption:** unsupported, much stronger than needed, or at odds with established
   findings (cite only a verified source; otherwise say "unverified"). Under *respect as given*,
   raised only where it affects the build or the claims.

For each, recommend where appropriate a **reframing**, for the PI to accept or decline: a hypothesis
becomes a **research question** or an **outcome the tool measures**; a fixed rule becomes a
**configurable model assumption** (a parameter or condition, with a sensitivity analysis available);
an invariant that is really an assumption becomes a Model commitment. Nothing is reframed without
the PI's words; a declined recommendation is recorded with the PI's reason. If the PI keeps a
flagged commitment as it is (for example as a fixed rule of the model), it keeps the class the PI
chose, its row says "kept by the PI after the commitments review: '<the PI's words>'", and the
report's §3 and *Completeness check* name the consequence (what the tool can no longer find out);
it is never silently reclassified either way.

**Constraints summary:** every constraint by class, stated ones with the PI's words and inferred ones
marked "proposed"; the commitments review's findings and the PI's decisions; anything unresolved,
with what it affects.

---

## Phase 4: Design

**Objective:** a design the PI agrees with, or an explicitly provisional one, covering architecture
and the technical specifics, with every material decision explored (`architecture-guide.md`).

**Ask first, before proposing anything** (unless DS-01 is already settled; for a simple tool it may
be a stated default inside the first design question, `SKILL.md`, *Fast lane*):

> Do you already have a design or architecture in mind: languages, frameworks, platforms, how the
> parts fit together? You can describe one, give your preferences, or ask me to propose one.

- **The PI has a design:** read it back as you understand it, say what is strong about it and what
  concerns you, and discuss credible alternatives without trying to replace it by default.
- **No design:** "Based on the requirements, here is a design that makes sense to me," with the
  alternatives and trade-offs (`architecture-guide.md`); then "Any questions or thoughts on this?"
- **Iterate** as long as the PI needs: a round is a revision of the design in response to the PI.
  Do not fix a number of rounds, and do not move on while the PI is still exploring.
- **Depth follows IN-03.** A proficient coder gets specific architecture questions (components,
  interfaces, persistence, testing strategy); a PI less comfortable with code gets clear proposals,
  explained in plain words, and is asked about consequences, not mechanisms.

| ID | Required item | Feeds |
|---|---|---|
| DS-01 | The PI's own design or preferences (asked first) | The starting point |
| DS-02 | The user's workflow, end to end: one complete use, start to result | Workflows; functional requirements |
| DS-03 | Platform and delivery: where it runs, how users get it and its updates | Architecture decision |
| DS-04 | Language, frameworks, dependencies, licences | Architecture decision; costs |
| DS-05 | Data storage and persistence | Architecture; recovery |
| DS-06 | Data semantics (*Data and persistence*, below) | Data contracts (report §9) |
| DS-07 | Inputs, exports, connectivity and interfaces to other systems | Interface contracts |
| DS-08 | Nonfunctional targets, where relevant: performance, reliability, reproducibility | Nonfunctional requirements |
| DS-09 | Every material decision: alternatives, recommendation, the PI's choice or a gate | Report §8; `ARCHITECTURE.md` |

**Design closeout = the readiness gate.** The phase summary (the design in plain words, each
decision with its status, what is provisional and how it will be settled) ends with the closeout
choice phrased explicitly: "Are you ready to move on from the design to how the agents will build
it, or would you like to explore or revise any part first?" A provisional part is allowed; it
becomes an Open item with a gate.

### Data and persistence (when relevant)

Cover, as relevant: the kinds of data, and input and output formats; where data are stored, and what
persists versus what is temporary; entities and relationships, and repeated observations or
sessions; integrity, provenance, versioning and compatibility; backup, recovery and export; privacy
and security.

**Data semantics are consequential** (`arpd/constitution/CORE.md` §6). Raise them as ordinary product
questions (one per turn, or naturally grouped), never saved for the adoption block, and never
decided silently. Ask the consequential ones; propose defaults for the rest. For a data-collection
tool, most of these matter:

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
ordinary requirements with acceptance criteria; storage location, file names and similar mechanics
are implementation defaults (delegable).

**Input adequacy.** Check that the inputs carry every quantity each output needs ("present but
silent" versus "absent" needs a roster, not only a log). An unresolved gap is an open item with a gate.

**Sensitive data.** Raise ethics or approval questions only when real data about people are
involved, and only once you know what the answer changes. Ethics approval gates collecting real
data, not building and testing with synthetic data. Real data about people means selecting the
human-subjects module.

**Performance and reliability.** Never demand numbers the PI has no basis for: propose a
**provisional target and how to measure it** ("10,000 records exported in under 5 seconds, by a timed
test"), labelled a proposed default.

---

## Phase 5: Development

**Objective:** the first version and the priority of everything else, and how the agent team will
work: arrangement, autonomy, review, authority and the rules it will follow, all agreed.

**Open with how the agents will work (DV-05), as a bounded choice,** unless the PI already said.
Above the block, describe each arrangement in plain words, as *The agent workflow* (below) says: who
writes the code, who reviews and tests it, whether agents work one at a time or in parallel, and what
each costs in agent credit use and in the PI's attention. Recommend one from the task structure and
the PI's constraints (CS-02), with the reason in a sentence:

```text
────────────────────────────────
CHOICE FOR YOU (select one)
How should the agents work on this project?
A. One agent builds; a fresh reviewer agent that did not write the code checks each change.
   Simplest and cheapest.
B. A lead agent with helpers: an implementer writes, a separate reviewer checks, and a tester
   writes tests from the specification when the science needs it. More independent checking;
   more credit use.
C. Several agents in parallel on separate parts, each in its own copy of the project, under a lead,
   with an independent tester. For large work that splits cleanly; the most to keep track of.
D. Recommend one for me.
────────────────────────────────
```

Mark the recommended option "(recommended)"; for a simple tool, A. Then **one open follow-up (DV-01)**,
before proposing anything else:

> Is there anything more you want to set about how the agents run? For example: rules they must
> follow, how changes are reviewed or tested, what needs your approval, how far they may go on
> their own, or a limit on credit use.

Record the answer in the PI's words; "nothing more" is an answer. For a simple tool, the follow-up
may be a stated default inside the next question ("Unless you want to add rules, I'll use ARPD's
standard ones").

| ID | Required item | Feeds |
|---|---|---|
| DV-05 | Team arrangement and workspace (asked first, as a choice) | Report §12; charter |
| DV-01 | The PI's rules and preferences for the agents' work (the open follow-up) | The rules summary; SA-01 |
| DV-02 | The minimum usable version: the simplest version the PI could actually use. It keeps every requirement the PI already called firm, required or a must; list those before asking, and never move one out without the PI's words. Not asked for a very small project (the whole tool is the minimum, Inferred) | P1; milestone M1 |
| DV-03 | What the first release is: a proof of concept, a research-useful version, or a validated release | Exit evidence of M1; verification depth |
| DV-04 | The priority of every other feature and research question (P1–P5), with feasibility and correctness-critical flags | Requirements; roadmap |
| DV-06 | Sprint autonomy: one task at a time as planned, one sprint at a time, or several sprints with a full post-action review and decision log | Charter §8 cadence; `/arpd-plan` |
| DV-07 | Review depth and check-in cadence | SA-01; `STATUS.md` §8 |
| DV-08 | Authority profile (SA-01), the data-semantics policy, and limits on time, compute and cost | SA-01 |
| DV-09 | Modules | Charter Part B |
| DV-10 | The rules summary, reviewed and confirmed; open decisions with their gates | Charter; *Waiting on the PI* |

### The minimum usable version and priorities

**If the proposed project is already very small** (one tool doing one job, nothing to stage), do not
ask about a minimum usable version or the first-release type at all: record the whole tool as the
minimum (DV-02 and DV-03 Inferred, stated in the Development summary for the PI to correct) and go
straight to placing anything else the PI mentioned on the priority scale. Otherwise, for a
substantial project, say it plainly: "You have described a tool that ___. This is a
substantial build and is best developed in stages. What is the simplest version of it that you could
actually use?" Then: "These features and research questions fit that version: ___. These do not:
___. Please correct the split, and place each of the rest on this scale." Ask once (DV-03) whether the
first release should be a proof of concept, a research-useful version, or a validated release;
a working prototype is not yet a scientific instrument.

**The first time you use the scale, show it to the PI in full, in plain words,** above the question
that asks them to place items, as a short table like this one (adapted to the project's words), and
say that two flags can be added to any item:

| Level | What it means for you | What happens to it |
|---|---|---|
| **P1 Core** | The tool is not usable without it | Built first, in the first version |
| **P2 Next** | Needed soon, but the first version works without it | Built right after the first version |
| **P3 Planned** | You are committed to it, just not yet | Kept as a requirement for a later stage |
| **P4 Wanted** | You would like it if there is time | Kept on the wish list; built only if time allows |
| **P5 Idea** | Worth remembering; no commitment | Kept on the wish list as an idea |

- *Needs checking first* (feasibility to investigate): the team must find out whether or how it can
  be done before building it, whatever its level.
- *Correctness-critical*: a mistake in it would corrupt data or results; it is never ranked below
  anything that depends on it.

Give a one-line example from this project for P1 and P4 when it helps. Afterwards, the level names
alone are enough. The record keeps this mapping:

| Priority | Meaning | Goes to at adoption |
|---|---|---|
| **P1 Core** | In the minimum usable version | `REQUIREMENTS.md`, milestone M1 |
| **P2 Next** | The first work after the minimum | `REQUIREMENTS.md`, the next milestone |
| **P3 Planned** | Committed, for a later milestone | `REQUIREMENTS.md`, a later milestone |
| **P4 Wanted** | Wanted; scheduled only if time allows | `MASTER_PLAN.md` backlog |
| **P5 Idea** | Worth keeping; not committed | `MASTER_PLAN.md` backlog |

Two flags apply at **any** priority:

- **Feasibility: to investigate** (what, and its gate): the team must first establish whether it can
  be done or how; `/arpd-plan` schedules a bounded feasibility investigation before building it.
  Otherwise **established**.
- **Correctness-critical: yes** (why): data integrity, scientific semantics, protections. Never
  ranked below a feature that depends on it; a correctness-critical item at P4 or P5 is questioned.

**Safeguards:** a requirement is never ranked above a requirement it depends on; scientific
correctness, data integrity and necessary protections are never demoted because they are not
visible features. A feature hierarchy is not a correctness standard.

### The agent workflow

Describe the proposed workflow **in full and in plain words** before the PI chooses: who plans, who
writes code, who reviews and tests, whether agents work one at a time in a shared checkout or in
parallel in separate worktrees, what the PI sees and approves, and what it costs (agent credit use,
the PI's attention). Say how the PI's constraints (for example, "keep credit use low", CS-02) shaped
the recommendation.

Judge the **task structure** for the recommendation: can the work split into parts built and tested
independently? The arrangement is asked first (above). Sprint autonomy, review depth, check-in
cadence, the authority profile and each proposed module come later in the phase, in one bounded
choice (or two, for a complex project), not left to the adoption assent. Never adopt an arrangement,
review depth or profile the PI was not asked about.

| Situation | Team arrangement | Workspace |
|---|---|---|
| Simple or tightly sequential; or cost must stay low | **Solo**, with review by a fresh subagent that did not write the code | Shared checkout |
| Most projects | **Lead with subagents** (implementer, reviewer; tester when the specification is rich) | Shared checkout, one subagent at a time |
| Clearly separable parallel streams, and a PI comfortable with more moving parts | **Peers** (two or three) under the lead, plus an independent tester when justified | **Worktrees**, with separate ports and output directories |

Never recommend a large team for a simple tool; say in one sentence why the arrangement suits the
task structure. If the PI chooses differently, record that it differs from your recommendation.
Roles and coordination: `arpd/constitution/modules/team/team-arrangement.md`.

**Sprint autonomy (DV-06)** sets the project default that `/arpd-plan` starts from:

- **One task at a time:** the team does only the specific tasks planned and approved, and stops.
- **One sprint at a time [default]:** a check-in at every sprint boundary before the next is planned.
- **Several sprints:** the team may plan and carry out a series of sprints the PI approves as a
  package, with independent review, a close-out record, a post-action review and a decision log at
  every boundary, and pauses for a new scientific, scope or PI-reserved decision. It takes effect only
  through the PI's words when execution is authorized (`/arpd-plan`).

### Authority and governance (report §12)

Draft SA-01 from what you heard, in plain words with this project's examples, and ask the PI only to
confirm or adjust it. Its fields are the `arpd/templates/DECISIONS.md` SA-01 entry; the profiles are
defined in `arpd/constitution/CORE.md` §6 (propose one, [bounded autonomy], with each alternative in
one line). In particular:

- **Delegated:** implementation *mechanisms* only (code structure, libraries within the approved
  stack, file layout, test design, error-message wording).
- **Reserved:** data semantics are never delegated by default. Name this project's examples. Delegate
  one only if the PI names a policy, and quote it. Add the standard triggers: a changed objective,
  exceeded scope or resource limits, a contested interpretation.
- **Review, cadence, limits:** review follows the PI's review depth (`arpd/docs/INTERACTION.md` §1).
  Sprint plans are approved by the PI, changes independently reviewed, milestones closed with the
  PI's walkthrough; anything outside the adopted report needs a ruling. [The team does not run
  while the PI is away]; note any time, compute or cost limits.

**Modules:** select only those this project needs (`module-catalog.md`), and say why; human-subjects
data whenever the tool collects data from or about people.

### The rules summary (DV-10, the Development closeout)

Before the closeout, run an internal **consistency and proportionality check** over every rule the
team would follow: rules that conflict (approval of every change, yet full autonomy across sprints),
rules the available agents cannot follow, and rules whose overhead outweighs their value for this
project. Propose a workable reading for each conflict.

Then present the **overall workflow summary** (the arrangement, how a piece of work moves from plan to
review to the PI, autonomy, cadence, what the PI decides) and the **list of rules Claude will
follow**, each with:

| Provenance | Meaning |
|---|---|
| **Core ARPD** | A framework rule from `arpd/constitution/CORE.md` (for example: planning is not execution; the PI's words are recorded verbatim) |
| **PI** | The PI's own rule, in their words |
| **Project-derived** | Proposed because of this project's characteristics |
| **Agent-recommended** | An improvement you suggest |

and a status: accepted, proposed, provisional, excluded or unresolved. A recommended rule stays
proposed until the PI accepts it. Push back selectively: explain the consequence of removing a
safeguard that protects correctness, data or the PI's authority; accept routine preferences without
ceremony. Core ARPD rules are not removed in setup (a change goes through `/arpd-amend` later).

### Open decisions and gates (report §13)

For every unresolved item, record what it affects, its **gate** (before planning: before any plan
that includes the work it affects; before implementing <a named feature>; or before deployment), what can continue meanwhile, and your
recommendation. An item without a gate is not allowed. Never invent a binding default to get a
clean list.

---

## The paradigm specification (theory and correctness)

### Ambiguity triage

| Kind | Example | In setup |
|---|---|---|
| 1. Affects the implementation | Which formula, which unit of analysis, whether an item may be skipped | **Pursue** |
| 2. Affects only later analysis | How the PI will model the collected answers | Record it in the notes; do not pursue |
| 3. Prevents a valid design | Two requirements that cannot both hold; an estimator undefined for the stated data | **Pursue** |
| 4. Deferred by the PI | "I'll define that later" | Record it with what it affects and its gate |

**Boundary rule.** If the PI says the tool only collects data, and the constructs live in questions
they will supply, record the boundary in the PI's words, put analysis and interpretation in the
exclusions, and move on to the product.

**Correctness-critical semantics.** For an estimator, a simulation, a measurement pipeline or any
theory-dependent model, the mathematics *is* the specification. Whatever the role, cover: equations
and definitions; assumptions; edge cases (empty groups, ties, out-of-range values, non-convergence);
numerical precision and tolerances; randomness and seeds; what the method refuses to compute. Each
becomes a requirement with acceptance criteria (usually known-answer or recovery tests), marked
correctness-critical.

### The full paradigm-specification method (co-development, correctness-critical work, or on request)

Across Objectives and Constraints:

1. **Constructs** (CON-NN): "What are the key constructs or mechanisms? How would you define each?"
   Verbatim. Offer a draft only after hearing the PI's view, labelled as yours.
2. **Operationalizations** (OP-NN): what the tool manipulates, records or computes, at what level and
   timing.
3. **Invariants** (INV-NN): propose three to eight from `module-catalog.md`, in scientific language;
   the PI accepts, edits or rejects each. Then ask: "Is there anything that, if the code got it
   wrong, would make the results meaningless?" Each passes the commitments review: never a
   hypothesis.
4. **Claims** (CLM-NN), and two to four claims not to make (NCL-NN).
5. **Assumptions** (ASM-NN): where a source is ambiguous, list the readings; record the PI's choice
   and its epistemic status.
6. **Validation** (VAL-NN): Objectives, OB-07.

Label every item's origin (the PI's words, or drafted by the lead) and status. Silence is not
consent to a new scientific model. Draft wording on import: `import-path.md`, step 2 of *Steps for
an ARPD starter*.

---

## Requirements quality (every phase that produces requirements)

Turn answers into an implementable specification, not a restatement. "It exports the answers as
CSV" is insufficient. Better:

```markdown
#### REQ-EXPORT-01: Export stored records

- **Description:** The tool exports every locally stored record to one CSV file, without altering
  the recorded content.
- **Acceptance criteria:**
  - every required field appears, with the header row in the order given in §9;
  - identifiers are preserved exactly;
  - each stored record appears once: none duplicated, none omitted, across repeated exports;
  - free text containing commas, quotation marks, line breaks and non-ASCII characters survives
    intact;
  - a test export, re-imported, matches the stored records field by field.
- **Priority:** P1 Core
- **Correctness-critical:** yes: a lost or duplicated record corrupts the analysis
- **Dependencies:** REQ-DATA-01
- **Source:** Lead's derivation from the PI's "export as a CSV file"
- **Status:** Proposed (the column layout stays provisional until the PI approves it, or delegates
  it with bounds)
```

Detail is proportional to complexity and risk; do not pad trivial requirements. Candidate
requirements accumulate from Objectives on; their priorities are set in Development. You may propose
requirements and acceptance criteria, but **never silently convert a proposal into a PI-approved
requirement**: it stays Proposed until the PI accepts it in words. Every requirement that serves a
research question names it (OB-05).

---

## Definition Report phase

Follow `generation-checklist.md`, Part A (draft, completeness check, presentation, review,
adoption), then Part B (generation), then `SKILL.md`, *Closeout and handoff*.
