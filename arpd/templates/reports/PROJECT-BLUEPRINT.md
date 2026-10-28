# Project Blueprint: {{project working name}}

> **DRAFT. Not adopted. Nothing here is a requirement, decision or authorization until the PI adopts
> it.** The PI adopts an identified version, in their own words, by ruling R-NN (`DECISIONS.md`).

**Version:** v{{N}}, {{date}}.

**Status:** Draft v{{N}}

<!-- Guidance (remove every guidance comment when filling the blueprint).
- Proportionality first: short and sharp for a simple tool, deep for an estimator. A section that
  does not apply is one line, "Not applicable: <reason>". Bullets are prompts, not fields.
- The full specification the PI reviews, from the notes: testable requirements, not restated
  answers. Never manufacture detail; state a gap, with a gate (section 13).
- Each version shown to the PI bumps the Version and adds a Change history row.
- At adoption (the adoption-first commit, no other edit): Status "Adopted by R-NN (vN)", and the
  banner becomes: "ADOPTED by R-NN (vN). This is the record of what was adopted. It is
  informative: the governing documents carry its content, and where they differ the governing
  document wins and the difference is recorded (CLAUDE.md §2)." Frozen afterwards (/arpd-amend). -->

## Change history

| Version | Date | What changed | Why (PI request, review, new information) |
|---|---|---|---|
| v1 | {{date}} | First draft |  |

## Statuses and where they go at adoption

Each requirement, decision and open item has one status, mapped onto the kit's existing records.

| Status | At adoption it goes to |
|---|---|
| **Adopted-on-adoption** (the PI stated or accepted it, quoted in *Source*) | `REQUIREMENTS.md` (table and *Requirement details*), `ARCHITECTURE.md` *Architecture decisions*, or `PARADIGM-SPEC.md` / `DECISIONS.md` |
| **Adopted (inherited, R-NN)** (an imported project's own ruling) | Unchanged, cited by ID |
| **Delegated (SA-NN)** (agents decide within its bounds) | That SA; listed as delegated in `ARCHITECTURE.md` or `REQUIREMENTS.md` |
| **Provisional** (says what confirms it) | `ARCHITECTURE.md` *Architecture decisions*, labelled, or *Waiting on the PI* with its gate; never a requirement's source |
| **Open (gate)** | `DECISIONS.md` *Waiting on the PI*, *Needed by* = the gate |
| **Proposed** (the lead's; not accepted) | Not adopted, unless the adoption ruling names it: `MASTER_PLAN.md` §4 backlog. A data-semantics proposal not accepted becomes **Open** instead (gate: before implementing the feature it affects) |
| **Excluded** | The out-of-scope list (`PARADIGM-SPEC.md` §8) |
| Priority **P4** or **P5**, any status | `MASTER_PLAN.md` backlog only, not `REQUIREMENTS.md` |

**Provenance:** the PI's words verbatim ("PI: ..."); otherwise Normalized, Lead's derivation, Lead's
recommendation, or "PI accepted: '...'". Each phase summary the PI confirmed is cited by its time in
the notes; a confirmation is not adoption, accepts no proposal, and is never a requirement's Source.

**Priorities:** P1 Core (the minimum usable version) · P2 Next · P3 Planned · P4 Wanted · P5 Idea.
Two flags apply at any priority: *Feasibility* (established / to investigate: <what> (<gate>)) and
*Correctness-critical* (yes: <why> / no). No requirement is ranked above a requirement it depends on.

---

## 1. Executive overview

| Item | Content |
|---|---|
| Project name |  |
| Purpose (PI, verbatim) |  |
| What will be built, at a high level |  |
| Academic field and theoretical scope |  |
| The PI | {{coding comfort; how involved in technical decisions}}, as far as it matters |
| Intended users; who runs and maintains it afterwards |  |
| State of the work | {{idea / specified / prototype / working code / mature}}; existing material and where |
| Where the project lives | {{this folder (converted from the kit) / installed in <repo> / new folder / imported from <source>}} |
| Agent's role | {{A–F or other, in the PI's words}}; technical axis: {{builder / reviewer and builder / co-designer / auditor}}; scientific axis: {{technical only / respect as given / alignment review / co-development}} |
| Timeline |  |
| Project classification | {{e.g. new project, broad idea / data collection / statistical method / existing repository to extend}} |

## 2. Research context and objectives

<!-- Technical only: one line, "Research questions and theoretical alignment: out of focus by the
PI's choice (<the PI's words>)", then the objectives. Keep four things distinct: the PI's intent,
the specification, the implementation, and empirical validation. -->

- **Research domain:** the phenomena, constructs or problems the tool is about.
- **Research questions:** specific, or illustrative for a general platform (say which).
- **Objectives** (the PI's words):
- **Intended use of the outputs** (exploration, teaching, publication, operations) and what it
  requires (reproducibility, provenance, versioning):
- **Traceability:** one row per research question or objective.

| Research question or objective | Capability it needs | Requirements |
|---|---|---|
|  |  |  |

## 3. Constraints and model commitments

<!-- Every constraint, stated (the PI's words) or inferred (marked "proposed"). Model commitments
carry their epistemic status. The theory part is "Not applicable: technical only (PI's choice)"
when so. -->

| ID | Constraint or commitment | Class | Status or epistemic status | Source | Affects |
|---|---|---|---|---|---|
| C-01 |  | {{Must / Prefer / Model commitment / Must hold / Open question}} |  |  |  |

- **Commitments review:** each contradiction, circularity or questionable assumption found, the
  reframing recommended (hypothesis, research question, configurable model assumption), and the
  PI's decision; or "None found".
- **Framing choices** (bodies of work drawn on or set aside), recorded as delimiting the model.

## 4. Scope, priorities and workflows

- **Minimum usable version** (the PI's words; P1):
- **First release:** {{proof of concept / research-useful version / validated release}}, the PI's
  words.
- **Priorities:** each feature and research question by P1–P5, with feasibility and
  correctness-critical flags (the details are in §5–6).
- **Excluded** (the PI's words):
- **End-to-end workflows:** one numbered sequence per main workflow, from start to result. As
  relevant: user roles, inputs and outputs, the interaction model.

## 5. Functional requirements

<!-- IDs REQ-<AREA>-NN, the same in REQUIREMENTS.md. Drop Behaviour, Inputs/outputs and Constraints
when they add nothing; Acceptance criteria (checks an independent tester could run), Priority,
Source and Status are always present; Feasibility and Correctness-critical when they apply. A
requirement sourced only by the lead is Proposed or Provisional. One status per requirement: if parts
differ, split it. Criteria that wait on an open decision are still bullets: "- pending O-NN: <what
will be checked>". A requirement serving a research question names it. -->

#### REQ-{{AREA}}-01: {{name}}

- **Description:**
- **Behaviour:**
- **Inputs/outputs:**
- **Constraints:**
- **Acceptance criteria:**
  - {{an observable check}}
- **Priority:** {{P1 Core / P2 Next / P3 Planned / P4 Wanted / P5 Idea / open (O-NN), while the PI leaves it open}}
- **Feasibility:** {{established / to investigate: <what> (<gate>)}}
- **Correctness-critical:** {{yes: <why> / no}}
- **Dependencies:** {{REQ IDs, D-NN (section 8), O-NN (section 13), or "none"}}
- **Source:** {{PI: "<verbatim>" / Lead's derivation from <what> / Lead's recommendation; PI accepted: "<words>"}}
- **Status:** {{a status from the table above}}

## 6. Nonfunctional requirements

<!-- As section 5, IDs REQ-NFR-NN, plus a Target. Only what is relevant; the rest on one line, "Not
applicable: <reason>". No number the PI has no basis for: propose a default and its measure. -->

#### REQ-NFR-01: {{name}}

- **Description:**
- **Target:** {{stated (PI: "<words>") / proposed default (lead's recommendation)}}; measured by {{how}}
- **Acceptance criteria:**
  - {{an observable check}}
- **Priority:** {{P1 Core / P2 Next / P3 Planned / P4 Wanted / P5 Idea}}
- **Dependencies:** {{as in section 5}}
- **Source:** {{as in section 5}}
- **Status:** {{as in section 5}}

## 7. Proposed architecture

<!-- Plain language first: what runs where, what the user sees, where data go, how results come
out. Then components, stack, persistence, dependencies (licence, cost), deployment, as relevant.
Say whether it started from the PI's design. A technology claim says "checked in <documentation>,
<date>" or "not verified". -->

## 8. Alternatives and design decisions

<!-- One row per material decision (D-NN); trivial ones listed briefly after the table. Each
credible alternative with its main advantage and disadvantage, and why it was rejected. -->

| Decision | Alternatives considered | Recommendation | Rationale | Status | Consequences |
|---|---|---|---|---|---|
| D-01: {{e.g. delivery platform}} |  |  |  |  |  |

## 9. Data and interface contracts

<!-- As relevant: entities, inputs, outputs, storage, versioning, integrations. An unresolved schema
is "Schema provisional: <what remains>", with an O-NN. Data semantics are the PI's (CLAUDE.md §6):
for each, who decided it (the PI's words, or a named SA policy), or Open. Include a concrete example
the PI can check: an output row, a file excerpt, a screen outline. -->

- **Missing-data behaviour:** for each field that can be absent, what blank, missing, zero and "not
  shown" mean, and who decided it.
- **Duplicates, repeats and identifiers:** what an identifier means; what a repeated submission does.

## 10. Verification and acceptance

- **Implementation correctness (Verified):** the tests, review and walkthrough that show the
  software does what the requirements say.
- **Scientific validity (Validated):** the evidence the PI will accept, or "Not applicable: <reason>".
- **What would convince the PI** (the PI's words):

## 11. Development roadmap

<!-- Direction, not a sprint plan (/arpd-plan writes that). M1 delivers the P1 requirements (the
minimum usable version) to the first-release standard; P2 next; P3 later milestones; P4 and P5 are
backlog. Feasibility investigations come before what depends on them. Becomes MASTER_PLAN.md §2-4. -->

| Milestone | What the PI will be able to do | Requirements | Walkthrough |
|---|---|---|---|
| M1 |  |  |  |

## 12. Development process, rules and authority

- **The PI's rules for the agents** (the PI's words), or "none named".
- **Team arrangement:** who leads, implements, reviews, tests and integrates; shared checkout or
  worktrees; why it suits the task structure and the PI's constraints (cost included).
- **Workflow:** how a piece of work moves from plan to review to the PI.
- **Sprint autonomy:** {{one task at a time / one sprint at a time / several sprints with a
  post-action review and decision log}}, in the PI's words.
- **Authority profile (SA-01):** {{consult first / bounded autonomy / exploratory autonomy}}, in the
  PI's words, with what the agents may decide and its bounds.
- **Data semantics:** never delegated unless the PI names a policy: {{"no policy named" / the PI's
  policy, verbatim}}. Agents choose implementation mechanisms only.
- **Decisions requiring the PI:**
- **Review, cadence and limits:** review depth, check-ins, limits on autonomous work (time, compute,
  cost).
- **Modules:** {{each selected module and why; human-subjects data whenever the tool collects data
  from or about people}}.
- **Rules Claude will follow:** after the consistency and proportionality check.

| Rule | Provenance | Status |
|---|---|---|
|  | {{Core ARPD / PI / Project-derived / Agent-recommended}} | {{accepted / proposed / provisional / excluded / unresolved}} |

## 13. Risks, assumptions and open decisions

Every item has a gate: before planning, before implementing <what>, or before deployment. At
adoption each open O-NN becomes a row of `DECISIONS.md` *Waiting on the PI* (O-01 → #1, and so on,
in this order), with *Needed by* = its gate; the adoption ruling's *Reading* records the mapping.
An item the PI has answered starts with "Resolved:" (in a table, the first cell: "Resolved: O-04"),
saying where it now lives, or moves out of this section.

| ID | Item | Kind | Affects | Gate | Can continue meanwhile | Recommendation |
|---|---|---|---|---|---|---|
| O-01 |  | {{risk / assumption / external dependency / open decision / feasibility investigation}} |  | {{before planning / before implementing <what> / before deployment}} |  |  |

## 14. What adoption authorizes

Adopting this version, by the PI's ruling (R-NN, in the PI's words), authorizes writing the
governing documents from it (`CLAUDE.md`, `PARADIGM-SPEC.md`, `REQUIREMENTS.md`, `ARCHITECTURE.md`,
`MASTER_PLAN.md`, `DECISIONS.md`, and `STATUS.md` for the present state), and the non-governing
orientation file `START-HERE.md`. It adopts the items marked Adopted-on-adoption, and
any proposal the ruling names as accepted, and records the other items as their status says.

It does **not** adopt other Proposed items, settle Open items, approve a sprint plan, or authorize
any implementation. Implementation needs an approved plan and the PI's start direction, through
`/arpd-plan`.

---

## Completeness check: gaps found

<!-- Two to four lines: the material gaps the check found (reports/setup/NOTES.md §9 lists what is
checked), and where each is handled; or "None found". Never hide a gap behind a status. -->
