# Project Definition Report: {{project working name}}

> **DRAFT. Not adopted. Nothing here is a requirement, decision or authorization until the PI adopts
> it.** The PI adopts an identified version, in their own words, by ruling R-NN (`DECISIONS.md`).

**Version:** v{{N}}, {{date}}.

**Status:** Draft v{{N}}

<!-- Guidance for the lead (remove every guidance comment when filling the report).
- Proportionality first. Detail scales with the project's complexity and risk. A section that does
  not apply is one line: "Not applicable: <reason>". The bullets under each heading are prompts for
  what to cover when it matters, not fields to fill: drop any that do not apply. No boilerplate.
- Write it from the setup notes (docs/discovery/SETUP.md) and present it before anything governing
  is written. It must stand on its own as a specification: turn answers into implementable,
  testable requirements; do not just restate them.
- Never manufacture detail to look complete. A gap is stated as a gap, with a gate (section 12).
- Each revision shown to the PI bumps the Version and adds a Change history row.
- At adoption, in the adoption-first commit, and with no other edit: set the Status line to
  "Adopted by R-NN (vN)", and replace the banner with: "ADOPTED by R-NN (vN). This is the record of
  what was adopted. It is informative: the governing documents carry its content, and where they
  differ the governing document wins and the difference is recorded (CLAUDE.md §2)."
  The adopted text is then frozen. Later changes go through rulings on the governing documents
  (/arpd-amend), never through edits here. -->

## Change history

| Version | Date | What changed | Why (PI request, review, new information) |
|---|---|---|---|
| v1 | {{date}} | First draft |  |

## Status legend

Every requirement, decision and open item carries one of these statuses. They map onto the kit's
existing mechanisms; they are not a second authority model.

| Status | Meaning | Where it goes when this report is adopted |
|---|---|---|
| **Adopted-on-adoption** | The PI stated it, or accepted it in words (quoted in *Source*). It is adopted when R-NN adopts this version, not before. | The governing documents: `REQUIREMENTS.md` (Planned, source R-NN or a spec item), `ARCHITECTURE.md` *Architecture decisions*, `PARADIGM-SPEC.md`, `DECISIONS.md` |
| **Proposed** | The lead recommends it; the PI has not accepted it. | Nothing is adopted. Before adoption the PI accepts, changes or drops it. One left at adoption is filed as Backlogged in `MASTER_PLAN.md` §4 |
| **Provisional** | A working assumption or design preference awaiting confirmation or evaluation. Says what would confirm it. | `ARCHITECTURE.md` *Architecture decisions*, labelled Provisional, with its gate in `DECISIONS.md` *Waiting on the PI*. Never the source of a requirement |
| **Delegated (SA-NN)** | The PI authorized the agents to decide it, within stated bounds. | The standing authorization (SA-01, or a narrower SA-NN) with its bounds; labelled Delegated where it appears |
| **Open (gate)** | Unresolved; needs a decision by a stated gate: before planning, before implementing <what>, or before deployment. | `DECISIONS.md` *Waiting on the PI*, with *Needed by* = the gate |
| **Excluded** | Explicitly outside the agreed scope. | The out-of-scope list (`PARADIGM-SPEC.md` §8); later or wishlist items to the backlog |

## Provenance

The PI's words are quoted verbatim ("PI: ..."). The lead's tidied wording is "Normalized" (the
original stays in the setup notes), an inference is "Lead's derivation", a proposal is "Lead's
recommendation", and a proposal the PI accepted quotes their words ("PI accepted: '...'"). The
research question, construct definitions and the adoption ruling are always verbatim.

---

## 1. Executive project overview

| Item | Content |
|---|---|
| Project name |  |
| Purpose (PI, verbatim) |  |
| Problem being solved |  |
| Intended users |  |
| Target outcome |  |
| Scope | Minimum usable version → ideal version → nice-to-have (section 2) |
| Project classification | {{e.g. new project, broad idea / data collection / statistical method / existing repository to extend}} |
| Theory context | {{A. guide implementation without evaluating / B. identify concerns / C. help develop / D. leave aside / not relevant}}, PI's words |

## 2. Product vision and workflows

<!-- As relevant: primary use cases, user roles, inputs and outputs, the interaction model (GUI,
command line, API, browser, batch...). -->

- **Scope**, in the PI's three tiers (quote the PI):
  - **Minimum usable version:** its requirements have Priority required; the initial release
    delivers at least this.
  - **Ideal version and features of interest:** what differs from the minimum, each feature named;
    Priority desired, or future if beyond the initial release.
  - **Nice-to-have, not in the initial release:** later; not requirement entries. Filed as
    Backlogged at adoption.
  - **Excluded** (with the PI's words):
- **End-to-end workflows:** one numbered sequence per main workflow, from start to result.

## 3. Functional requirements

<!-- One entry per requirement, in this exact format. IDs are REQ-<AREA>-NN (areas set here, e.g.
CORE, DATA, UI, EXPORT); the same IDs move one to one into REQUIREMENTS.md. Every requirement has
at least one acceptance criterion that an independent tester could check, and a Status from the
legend. A requirement whose Source is only the lead's (derivation or recommendation) is Proposed or
Provisional, never Adopted-on-adoption, unless the PI's acceptance is quoted. A simple requirement
keeps to a line per field and omits Behaviour, Inputs/outputs and Constraints when they add
nothing; Acceptance criteria, Priority, Source and Status are always present. -->

#### REQ-{{AREA}}-01: {{name}}

- **Description:**
- **Behaviour:**
- **Inputs/outputs:**
- **Constraints:**
- **Acceptance criteria:**
  - {{an observable check}}
- **Priority:** {{required (minimum usable version) / desired (ideal version) / future (ideal, beyond the initial release)}}
- **Dependencies:** {{REQ IDs, decisions (D-NN, section 6), open items (O-NN, section 12), or "none"}}
- **Source:** {{PI: "<verbatim>" / Lead's derivation from <what> / Lead's recommendation; PI accepted: "<words>"}}
- **Status:** {{Adopted-on-adoption / Proposed / Provisional / Delegated (SA-NN) / Open (gate) / Excluded}}

## 4. Nonfunctional requirements

<!-- Same format as section 3, with IDs REQ-NFR-NN, plus a Target line. Cover only what is relevant:
performance, reliability, portability, usability, security and privacy, reproducibility,
maintainability, extensibility, distribution and deployment. List the others on one line as
"Not applicable: <reason>". Never demand a number the PI has no basis for: propose a default and
say how it will be measured. -->

#### REQ-NFR-01: {{name}}

- **Description:**
- **Target:** {{stated target (PI: "<words>") / proposed default (lead's recommendation)}}; measured by {{how}}
- **Acceptance criteria:**
  - {{an observable check}}
- **Priority:** {{required / desired / future}}
- **Dependencies:** {{as in section 3}}
- **Source:** {{as in section 3}}
- **Status:** {{as in section 3}}

## 5. Proposed architecture

<!-- A substantive recommendation, plain language first: what runs where, what the user sees, where
data go, how results come out. Then, as relevant: components and their responsibilities, stack,
persistence, interfaces and dependencies (licence, cost), deployment, principal trade-offs. A claim
that a technology supports something is marked "checked in <documentation>, <date>" or "not
verified". -->

## 6. Alternatives and design decisions

<!-- One row per material decision; trivial ones are delegated or resolved by a stated default and
listed briefly at the end. Start the Decision cell with an ID (D-NN). Alternatives considered names
each credible alternative with its main advantage and disadvantage, and why a rejected one was
rejected. Status from the legend. Rows that are Adopted-on-adoption, Delegated or Provisional move to
ARCHITECTURE.md "Architecture decisions" at adoption, labelled; Open rows go to Waiting on the PI. -->

| Decision | Alternatives considered | Recommendation | Rationale | Status | Consequences |
|---|---|---|---|---|---|
| D-01: {{e.g. delivery platform}} |  |  |  |  |  |

## 7. Data and interface contracts

<!-- As relevant: entities and relationships, inputs, outputs, storage, versioning, external
integrations. Do not invent a schema that has not been resolved: write "Schema provisional: <what
remains to decide>" with an open item and its gate. Data semantics are the PI's (CLAUDE.md §6): for
each, record who decided it (the PI's words, R-NN, a named SA policy) or mark it Open. -->

- **Missing-data behaviour:** for each field that can be absent, what blank, missing, zero and "not
  shown" mean, and who decided it.
- **Duplicates, repeats and identifiers:** what an identifier means; what happens to a repeated
  submission or observation.

## 8. Verification and acceptance

<!-- As relevant: unit, integration and regression tests; independent review; the PI's manual
walkthrough; when the first version is ready. -->

- **Implementation correctness (Verified):** the software does what the requirements say.
- **Scientific or computational validity (Validated):** the instrument does what the science needs,
  with the evidence the PI will accept (known-answer recovery, reference calculations, a pilot). For
  a data-collection tool this may be "Not applicable: <reason>"; accurate capture, persistence,
  export, recovery and integrity still need verification.

## 9. Proposed development roadmap

<!-- Direction, not a sprint plan: /arpd-plan writes the executable plan. Follow the scope tiers:
M1 (the initial release) delivers at least the minimum usable version; later milestones the
ideal-version features; nice-to-have features are deferred. This becomes MASTER_PLAN.md §2 (milestones), §3 (order
of work, "planning pending") and §4 (deferred features, Backlogged). Add, as relevant: dependencies
between workstreams and a provisional sprint sequence. -->

| Milestone | What the PI will be able to do | Requirements | Walkthrough |
|---|---|---|---|
| M1 |  |  |  |

## 10. Agent team arrangement

<!-- Proportionate to the project, and respecting the PI's stated preference. A single agent with an
independent reviewer is often enough; parallel implementers or separate testers only when the work
justifies them. Say who leads, implements, reviews, tests and integrates; shared checkout or
worktrees; and why this suits the project. -->

## 11. Authority and governance

- **Authority profile (SA-01):** {{consult first / bounded autonomy / exploratory autonomy}}, in the
  PI's words, with what the agents may decide and its bounds.
- **Data semantics:** never delegated unless the PI names a policy: {{"no policy named" / the PI's
  policy, verbatim}}. Agents choose implementation mechanisms only.
- **Decisions requiring the PI:**
- **Review, cadence and limits:** the review depth and scientific critique wanted (the theory-context
  choice), check-ins, and limits on autonomous work (time, compute, cost).

## 12. Risks, assumptions and open decisions

<!-- Every item has a gate. An open decision is never "non-blocking" without one. Gates: before
planning / before implementing <what> / before deployment. Open decisions move to DECISIONS.md
Waiting on the PI at adoption, with Needed by = the gate. -->

| ID | Item | Kind | Affects | Gate | Can continue meanwhile | Recommendation |
|---|---|---|---|---|---|---|
| O-01 |  | {{risk / assumption / external dependency / open decision}} |  | {{before planning / before implementing <what> / before deployment}} |  |  |

## 13. What adoption authorizes

Adopting this version, by the PI's ruling (R-NN, in the PI's words), authorizes **the governing
documents only**: writing `CLAUDE.md`, `PARADIGM-SPEC.md`, `REQUIREMENTS.md`, `ARCHITECTURE.md`,
`MASTER_PLAN.md`, `DECISIONS.md`, `STATUS.md`, `INDEX.md` and `START-HERE.md` from it. It adopts the
items marked Adopted-on-adoption and records the Delegated, Provisional, Open and Excluded items as
such.

It does **not** adopt Proposed items, settle Open items, approve a sprint plan, or authorize any
implementation. Implementation needs an approved plan and the PI's start direction, through
`/arpd-plan`.

---

## Completeness check (before presenting)

<!-- Fill this in before showing any version to the PI. Report each material gap plainly, with
where it is handled; do not hide one behind a status. -->

| Check | Result | Where handled |
|---|---|---|
| Ambiguous functionality |  |  |
| Inconsistent requirements |  |  |
| Missing inputs or outputs |  |  |
| Unclear data semantics |  |  |
| Unresolved architectural dependencies |  |  |
| Unsupported assumptions |  |  |
| Requirements lacking meaningful verification criteria |  |  |
| Conflicts with exclusions |  |  |
| Missing user decisions |  |  |
| Decisions prematurely recorded as adopted |  |  |
