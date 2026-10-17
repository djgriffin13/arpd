# Interview guide

Follow this order. Skip questions whose answers are already in existing files, and say what you
found instead. The question wording below is a suggestion; adapt it to the PI. Defaults appear in
**[brackets]**. The phase times add up to about 30 minutes; an import of an ARPD starter is usually
shorter, because the science is confirmed rather than elicited.

---

## Phase 0: Orient (about 2 minutes)

1. **Detect the mode.**
   - Run `git status` and list the top level.
   - If the repository contains only the kit (`kit/`, `.claude/skills/arpd-*`, `docs/`,
     `evaluation/`, `examples/`, and the kit's own `README.md`, `QUICKSTART.md`, `CLAUDE.md`,
     `AGENTS.md`, `LICENSE`, `CITATION.cff` and dotfiles), the mode is **fresh**. The kit's own files are not prior instructions.
   - If the PI passed `import <path|url>` or `install <path>`, or if the project's own source code
     or instruction files (`CLAUDE.md`, `AGENTS.md`, `.cursorrules`, `README` with design notes)
     are present, follow `import-path.md`. A starter inside the kit (for example
     `examples/march-1991/`) is an import of an ARPD project: in Phases 2–4, read its existing
     specification to the PI in plain language and ask them to confirm or change it.
2. **Tell the PI in three sentences** what will happen:
   - "I'll ask about your science, then propose how to build it. About 30 minutes."
   - "Nothing is written until you approve a summary."
   - "Afterwards you'll have a team charter, a scientific specification and a first sprint ready
     to start."
3. **State the division of labour (G5).** "The agent team can show that code matches the
   specification and that known answers are reproduced. Only you can judge whether the
   specification captures what you mean scientifically. So I'll ask you about the science and
   propose the engineering."

## Phase 1: The PI (about 2 minutes)

Use AskUserQuestion. Record the answers in `STATUS.md` §8.

- Coding experience: [none / some scripting (R, Python, Stata) / regular programmer].
- AI-tool experience: [chat assistants only / some coding assistants / regular agentic use].
- Time available for this project per week, and how you like decisions brought:
  [batched at sprint boundaries / as they arise / daily digest].
- Name to use as PI in the records (can be a role, e.g. "PI").

**Propose an authority profile.** Do this now, so the PI knows from the start how much the team will
do on its own. Say it in plain words, and use AskUserQuestion:

> "How much should the team decide on its own? I suggest **bounded autonomy**: it works within the
> scientific boundaries we agree today, writes down any material assumption it makes, and reports
> at each checkpoint. The alternatives are **consult first** (it asks you before adopting any
> scientific assumption) and **exploratory autonomy** (it tries and compares plausible alternatives
> on its own, then comes back to you to decide which to adopt). You can change this at any time."

Record the choice. The boundaries are filled in during Phase 6.

## Phase 2: Science (about 8 minutes; the most important phase)

Record the answers verbatim where marked (V). Quote the PI exactly: no recapitalizing, splitting or
tidying.

**Draft wording.** On import, an item marked *"(draft wording, awaiting the PI's words)"* (often the
research question) needs the PI's own words now. If the PI does not give them, the item stays
explicitly pending and goes in *Waiting on the PI*. Adopting the specification "as it stands" does not
clear the marker.

1. **(V)** "In one or two sentences, what question do you want to be able to study?"
2. "What stops you studying it now?"
   - Probe: existing tools or paradigms, and their limits.
   - Probe: data that exist but aren't accessible.
   - Probe: models that exist for a different design.
   - Probe: constructs usually self-reported that should be observed.
3. **(V for definitions) Constructs and mechanisms.** "What are the key constructs or mechanisms?
   For each, how would you define it?"
   - Offer a draft definition from their description and let them correct it.
   - Assign CON-NN IDs.
4. **Operationalizations.** "For each construct, what should the instrument manipulate, record or
   compute? At what level (person, dyad, team, event, round) and timing?" Assign OP-NN IDs.
5. **Candidate invariants.** Using `module-catalog.md`, propose three to eight invariants in
   *scientific* language. Examples:
   - "Conditions differ only in the manipulated feedback."
   - "An unobserved tie is missing, not absent."
   - "The model's agents update only at the end of a period."

   Ask the PI to accept, edit or reject each. Assign INV-NN IDs. Then ask: "Is there anything that,
   if the code got it wrong, would make the results meaningless?" and add those.
6. **Claims.**
   - "What should results from this instrument let you say?" (CLM-NN)
   - Then propose two to four **claims not to make** (NCL-NN). Examples:
     - causal language without identification;
     - generalizing beyond the explored parameter range;
     - treating simulated participants as people.
7. **Assumptions** (for models or replications). Where a source is ambiguous, list the
   interpretations and record the PI's choice (ASM-NN).
8. **Out of scope.** "What should this deliberately *not* do, at least for now?"

## Phase 3: Instrument (about 4 minutes)

1. "Walk me through how you (or a participant, or a co-author) would use it, from start to finish."
   - Draft 5–15 requirements, phrased as things the PI would observe.
   - Assign `REQ-<AREA>-NN` IDs, each with a source (OP, INV, CLM or ruling).
2. "What goes in and what comes out?" Cover data sources, formats, and the analysis software the
   output must feed (R, Stata, SPSS, Python).
3. **Propose a platform** from `engineering-defaults.md`, with a one-line reason. Ask for
   confirmation. Note: choosing a platform that fits the PI's community (an R package for R users,
   for example) affects adoption. Treat it as a meaningful choice, not a technicality.
4. **Input adequacy.** For each operationalization and invariant, check that the input data carry
   every quantity it needs. For example, telling "present but silent" from "absent" needs a roster,
   not only a message log. Ask the PI about each gap. A gap the PI cannot resolve now becomes an open
   scientific question (`PARADIGM-SPEC.md` §9), and is read back in Phase 8.

## Phase 4: Evidence (about 3 minutes)

1. "What would convince you it works *as software*?" Propose this for the **Verified** state:
   - tests of each rule or feature;
   - known-answer tests where any exist.
2. "What would convince you it works *as science*?" Propose VAL-NN items for the **Validated**
   state, for example:
   - reproducing a published result;
   - parameter recovery on simulated data;
   - reference calculations on a hand-checkable case;
   - a pilot with people;
   - the PI's walkthrough;
   - comparison with an established tool.
3. "Are there published results, datasets or reference implementations we can check against?"
   These become known-answer tests.

## Phase 5: Team and workspace (about 3 minutes)

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

## Phase 6: Authority and cadence (about 3 minutes)

Turn the Phase 1 profile into a concrete standing authorization (SA-01). Draft every field from what
you have already heard, and ask the PI only to confirm or adjust it. Use plain words, not internal
labels.

1. **Scientific boundaries.** "The team may decide on its own: … (for example, the number of
   replications in quick checks, the layout of outputs). It brings to you: … (for example, how
   'conflict' is coded, dropping a condition, changing a stopping rule)." Use **this project's**
   examples.
2. **Permitted assumption changes.** Under bounded autonomy, list the assumptions the team may set
   or change and must document. Under exploratory autonomy, describe the alternatives it may
   implement and compare. Under consult first, say "none without asking".
3. **When to come back.** Always include: a change to the research objective, exceeding agreed
   scope or resource limits, and settling a contested interpretation. Then add any
   project-specific triggers.
4. **Cadence.** [Check in at every sprint boundary.] The PI can ask for more frequent check-ins, or
   later authorize several sprints in a row.
5. **Practical limits.** Time, compute and cost limits per sprint, if any.
6. "Should the team ever run while you're away?" [No. This can be turned on later in words.]

Read SA-01 back in two or three sentences. Record the PI's reply verbatim as SA-01 (on import, the
next free SA number: see `import-path.md`, *Numbering*). If the reply is only an assent ("ok",
"adopted"), record the read-back text that was assented to, labelled "(read back by the lead; PI
assented: '<the PI's exact words>')". Never present your draft as the PI's words.

## Phase 7: Constraints (about 2 minutes)

- **Plan and budget.** Practitioner experience suggests that light work fits a basic plan and
  sustained development a higher tier. Present this as experience, not a guarantee.
- **Data.** Real participant data? Where do they live? Any ethics approval reference? If yes, add
  the human-subjects module.
- **Deadline or milestones.**
- **Models.** Which model access does the PI have? Record versions at the first session.

## Phase 8: Read-back (about 3 minutes)

Present a **plain-language summary** of at most one screen:

- the question (verbatim);
- what will be built;
- the invariants;
- the claims not to make;
- what Verified and Validated will mean;
- the team arrangement;
- the authority arrangement (SA-01), in plain words, with this project's examples;
- the cadence;
- the first milestone;
- open scientific questions (including input gaps from Phase 3) and any item still in draft wording.

Ask: "If this is right, please say so in your own words (for example 'Adopted' plus any changes).
That sentence becomes ruling R-01" (on import: the inherited placeholder, or the next free R number).

Record the reply **verbatim**. If the PI asks for changes, revise and read back again.

## Phase 9: Generate

Follow `generation-checklist.md` exactly.

## Phase 10: Start

1. Write sprint S01: a **bounded first sprint**, one to three requirements, ideally a "walking
   skeleton". That is the thinnest end-to-end path, plus its first known-answer check.
2. In `START-HERE.md`, give the exact first prompt, matching the team arrangement actually
   installed. With the implementer role installed, for example: *"Start sprint S01. Plan it per the
   charter, brief the implementer, and stop for my check-in at the sprint boundary."* Without it, do
   not mention the implementer: *"Start sprint S01. Plan it per the charter, and stop for my check-in
   at the sprint boundary."*
3. Tell the PI how to check in (`/arpd-checkin`), how to rule (just say it; the lead agent records
   it verbatim), and how to amend the charter (`/arpd-amend`).
