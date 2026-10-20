# Setup working notes: {{project working name}}

> **Working notes — not governing; nothing here is adopted, approved or authorized.**
> These notes record the setup interview as it goes, so that it can resume after an interruption.
> Rulings, requirements and the charter exist only once the PI adopts the Project Definition Report
> (`reports/setup/PROJECT-DEFINITION.md`) by ruling (`DECISIONS.md`). An item here becomes binding only
> through that adoption, never by being written here. A phase confirmation is not adoption.

**Never write here:** credentials, secrets, participant data, private datasets, or content from
other repositories or folders the PI did not point to.

**How to write here:**

- Label every item with its provenance:
  - **PI:** the PI's words, verbatim, in quotation marks;
  - **Normalized:** your tidied wording of the PI's words (the verbatim original stays here);
  - **Derived:** "Lead's derivation:", with what it rests on;
  - **Recommendation:** "Lead's recommendation:";
  - **Approved:** the PI accepted a derivation or recommendation; quote their words.

  Never present an interpretation as a quotation.
- Update the notes after every useful answer, and re-mark every required item from it.
- Keep them short. They are a working aid, not a record of the whole conversation.

**Last updated:** {{date and time in UTC, read from `date -u +%Y-%m-%dT%H:%MZ`, never estimated}}

---

## 1. Folder and consent

- **What the folder held at the start:** {{fresh kit clone / kit clone with the PI's material /
  existing repository / ARPD starter / download without git}}, with what inspection found
- **How it was prepared:** {{convert (in place) / install <repository> / new <path> / import
  <source> → <path>}}; kit used: {{path, version}}; any backup bundle: {{path / none needed}}
- **Project folder:** {{absolute path}}
- **Consent to save these notes in the project:** {{not needed (convert, new, import) / given, PI's
  words and date / declined: kept at <parent of the target>/.arpd-setup-notes/<target name>/}}
- **Commit status:** {{not committed / committed in their own commit <SHA>}}. Never pushed without the
  PI's authorization.

## 1a. Opening answer (verbatim)

The PI's answer to the opening question, exactly as given, with its UTC time.

> {{the PI's words}}

## 2. Project classification and role

Internal routing; the PI is not asked to pick a category.

- **Classification:** {{e.g. new project, broad idea / developed requirements / existing repository
  to extend / computational or statistical method / data collection / simulation or experimental
  platform / general application / integration or automation / mixed}}
- **Rests on:** {{the PI's words, quoted}}
- **Agent's role (IN-08):** {{A–F or other}}, PI's words and date
- **Technical axis:** {{builder / reviewer and builder / co-designer / auditor / exploration}}
- **Scientific axis:** {{technical only / respect as given / alignment review / co-development}},
  {{Confirmed / Inferred}}
- **Depth applied to the science:** {{none / the paradigm items needed for correctness / full
  CON…VAL method}}

## 3. Phase tracker

Visible phases: Intake → Objectives → Constraints → Design → Development → Definition Report.
**Current phase:** {{phase}}.
**Pending question:** {{none / the question as asked, its recommendation and the alternatives shown}}
**Phase closeouts:** {{e.g. Intake confirmed 2026-10-20T14:05Z ("yes, continue"); Objectives
reopened 2026-10-20T15:10Z for OB-04}}

One table per phase, with every required item of `interview-guide.md` (add rows for anything else
that matters). A status is set from everything the PI has said, not only from the question asked.

**Status values:** Confirmed / Inferred / Open / Deferred / N.A.

### Intake

| ID | Item | Status | Answer (labelled) | Feeds | Updated |
|---|---|---|---|---|---|
| IN-01 | State of the work and existing material | Open |  |  |  |
| IN-02 | Academic field and theoretical scope | Open |  |  |  |
| IN-03 | Coding comfort; involvement in technical decisions | Open |  |  |  |
| IN-04 | Eventual users; who runs and maintains it | Open |  |  |  |
| IN-05 | Where the project lives | Open |  |  |  |
| IN-06 | Main goal; what is to be built | Open |  |  |  |
| IN-07 | Stage of development | Open |  |  |  |
| IN-08 | The agent's role and scientific axis | Open |  |  |  |
| IN-09 | Known constraints and preferences (must / prefer) | Open |  |  |  |
| IN-10 | Timeline or deadline | Open |  |  |  |

### Objectives

| ID | Item | Status | Answer (labelled) | Feeds | Updated |
|---|---|---|---|---|---|
| OB-01 | Research domain | Open |  |  |  |
| OB-02 | Research questions (specific or illustrative) | Open |  |  |  |
| OB-03 | Objectives | Open |  |  |  |
| OB-04 | Capabilities and features | Open |  |  |  |
| OB-05 | Purpose → capability → requirement links | Open |  |  |  |
| OB-06 | How the outputs will be used | Open |  |  |  |
| OB-07 | What would convince the PI it works | Open |  |  |  |
| OB-08 | Exclusions | Open |  |  |  |

### Constraints

| ID | Item | Status | Answer (labelled) | Feeds | Updated |
|---|---|---|---|---|---|
| CS-01 | Platform and environment | Open |  |  |  |
| CS-02 | Resources and cost (credit use included) | Open |  |  |  |
| CS-03 | Technology: languages, versions, libraries, tools | Open |  |  |  |
| CS-04 | Data and institution | Open |  |  |  |
| CS-05 | Use: who, where, when; deadlines | Open |  |  |  |
| CS-06 | Theory constraints | Open |  |  |  |
| CS-07 | Commitments review | Open |  |  |  |

### Design

| ID | Item | Status | Answer (labelled) | Feeds | Updated |
|---|---|---|---|---|---|
| DS-01 | The PI's own design or preferences | Open |  |  |  |
| DS-02 | User workflow, end to end | Open |  |  |  |
| DS-03 | Platform and delivery | Open |  |  |  |
| DS-04 | Language, frameworks, dependencies, licences | Open |  |  |  |
| DS-05 | Storage and persistence | Open |  |  |  |
| DS-06 | Data semantics | Open |  |  |  |
| DS-07 | Inputs, exports, connectivity, interfaces | Open |  |  |  |
| DS-08 | Nonfunctional targets | Open |  |  |  |
| DS-09 | Material decisions explored and chosen | Open |  |  |  |

### Development

| ID | Item | Status | Answer (labelled) | Feeds | Updated |
|---|---|---|---|---|---|
| DV-01 | The PI's rules for the agents | Open |  |  |  |
| DV-02 | Minimum usable version | Open |  |  |  |
| DV-03 | First release: proof of concept / research-useful / validated | Open |  |  |  |
| DV-04 | Priorities P1–P5, feasibility and correctness flags | Open |  |  |  |
| DV-05 | Team arrangement and workspace | Open |  |  |  |
| DV-06 | Sprint autonomy | Open |  |  |  |
| DV-07 | Review depth and check-in cadence | Open |  |  |  |
| DV-08 | Authority profile, data-semantics policy, limits | Open |  |  |  |
| DV-09 | Modules | Open |  |  |  |
| DV-10 | Rules summary confirmed; open decisions gated | Open |  |  |  |

## 4. Constraints and model commitments

| ID | Constraint or commitment | Class (Must / Prefer / Model commitment / Must hold / Open question) | Epistemic status | Source (labelled) | Review finding and PI's decision |
|---|---|---|---|---|---|

## 5. Candidate requirements

Candidates only. They become requirements only when the PI adopts the report. Priorities are set in
Development; until then "not yet placed". Status is the one the item will carry in the report.

| Candidate ID | Requirement | Serves (OB / research question) | Priority (P1–P5) | Feasibility | Correctness-critical | Source (labelled) | Status | Acceptance criteria noted |
|---|---|---|---|---|---|---|---|---|

## 6. Architecture alternatives explored

| Decision | Alternatives considered (advantage, disadvantage) | Recommendation and rationale | PI's response (verbatim) | Status |
|---|---|---|---|---|

## 7. Open questions

These move to `DECISIONS.md` *Waiting on the PI* at adoption. Every one has a gate: before planning,
before implementing <what>, or before deployment.

| Question | Affects | Gate (Needed by) | Can continue meanwhile |
|---|---|---|---|

## 8. Development process and rules

The PI's words on how the agents should work, review depth, autonomy and check-ins, the agent
arrangement, and data-semantics policy (or "none named"); then the rules list as presented.

| Rule | Provenance (Core ARPD / PI / Project-derived / Agent-recommended) | Status | PI's words |
|---|---|---|---|

## 9. Report version and state

- **Report:** `reports/setup/PROJECT-DEFINITION.md`, {{not started / Draft vN, presented <UTC time> / revision
  requested: <what> / adopted by R-NN (vN)}}
- **Completeness check:** {{not run / run for vN: gaps <list or "none">}}. Before showing any
  version, check for: a required item still Open without a gate; ambiguous functionality;
  inconsistent requirements; missing inputs or outputs (does each output's input carry what it
  needs?); unclear data semantics (each decided by the PI, delegated under a policy the PI named, or
  Open with a gate); unresolved architecture dependencies; unsupported assumptions; a model
  commitment without its epistemic status, or a hypothesis recorded as an invariant; a citation not
  verified; requirements without meaningful acceptance criteria; a requirement ranked above one it
  depends on; a correctness-critical item at P4 or P5 without the PI's words; conflicts with the
  exclusions; missing PI decisions (the team arrangement and cadence included); a needed module
  missing from §12; earlier PI preferences missing from report §12; a research question with no
  capability, or a P1 requirement serving nothing; anything marked adopted too early; an unanswered
  item recorded as an assumption or requirement; contradictions between sections (an item Open in
  one and resolved in another; a decision both Delegated and Open; a stale completeness check);
  lead-invented details (a field, a limit, a name, a "no network" rule) without a "Lead's" label. The
  report's *Completeness check: gaps found* gives the result.
- **Pending approvals:** {{e.g. adoption of vN}}
- **Resumed:** {{none / <UTC time>: what was found, what was redone}}

## 10. Lead's interpretations

Each one labelled "Lead's interpretation:", with what it rests on. None is adopted.
