# Setup working notes: {{project working name}}

> **Working notes — not governing; nothing here is adopted, approved or authorized.**
> These notes record the setup interview as it goes, so that it can resume after an interruption.
> Rulings, requirements and the charter exist only once the PI adopts the Project Definition Report
> (`reports/PROJECT-DEFINITION.md`) by ruling (`DECISIONS.md`). An item here becomes binding only
> through that adoption, never by being written here.

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
- Update the notes after every useful answer.
- Keep them short. They are a working aid, not a record of the whole conversation.

**Last updated:** {{date and time in UTC, read from `date -u +%Y-%m-%dT%H:%MZ`, never estimated}}

<!-- Compatibility with notes written by an earlier kit version (read deterministically on resume):
- A line or section "Interview mode" is obsolete, whatever its value. Ignore it, keep it in place,
  and mark it "(obsolete; ignored)". Never ask the PI to choose a mode.
- Old phase labels map to the new phases: Intake -> Project; Research & Problem -> Project (with the
  theory-context choice still to confirm, if relevant); Product & Engineering -> Requirements and
  Architecture; Governance & Handoff -> Team & Governance, then Definition Report.
- An old "PI profile" table is kept as context. Its answers are not re-asked.
- Old sections "Vision", "First useful version" and "Later, wishlist and exclusions" map to Scope:
  ideal version, minimum usable version, and nice-to-have or excluded. Ask only the scope questions
  they do not already answer.
- An old read-back draft is not a report: write reports/PROJECT-DEFINITION.md from these notes. -->

---

## 1. Mode and consent

- **Setup mode:** {{fresh / import <source> / install <repository>}}
- **Consent to save these notes in the project:** {{not needed (fresh or import) / given, PI's words
  and date / declined: kept outside the repository (OS temp), so recovery is limited}}
- **Commit status:** {{not committed / committed in their own commit <SHA>}}. Never pushed without the
  PI's authorization.

## 2. Project classification

Internal routing only; the PI is not asked to pick a category when the description makes it clear.

- **Classification:** {{e.g. new project, broad idea / new project, developed requirements / existing
  repository to extend / computational or statistical method / data collection / simulation or
  experimental platform / general application / integration or automation / mixed}}
- **Rests on:** {{the PI's words, quoted}}
- **What already exists:** {{materials, code or documents the PI pointed to, and what inspection
  found}}

## 3. Theory context

- **Relevant?** {{yes / not relevant: <why>}}
- **Choice:** {{A. use it to guide implementation, without evaluating it / B. identify concerns /
  C. help develop it / D. leave theory aside / not asked (not relevant)}}, PI's words and date.
- **Depth applied:** {{product only / the paradigm-specification items needed for correctness / full
  CON…VAL method (choice C, correctness-critical semantics, or on request)}}

## 4. Phase tracker

Visible phases: Project → Requirements → Architecture → Team & Governance → Definition Report.
**Current phase:** {{phase}}.

One table per phase. Topics are added, merged or retired as the interview goes. A topic's status is
set from everything the PI has said, not only from the question asked.

**Status values:** addressed / partial / open / deferred / n.a.

### {{Phase name}}

| ID | Topic | Status | Source (labelled) | Still unknown | Affects | Updated |
|---|---|---|---|---|---|---|
| T-01 |  | open |  |  |  |  |

## 5. Scope

Asked once each, after the product overview. Quote the PI.

- **Minimum usable version:** what must be there for the tool to be usable at all (Priority
  required).
- **Ideal version and features of interest:** what differs from the minimum, with each feature of
  interest named (Priority desired, or future if beyond the initial release).
- **Nice-to-have, not in the initial release:** filed as later (backlog), not as requirements.
- **Excluded:** what the PI ruled out of scope, in their words.

## 6. Candidate requirements

Candidates only. They become requirements only when the PI adopts the report. Priority follows
the scope tiers (section 5). Status uses the
report's legend (Adopted-on-adoption / Proposed / Provisional / Delegated (SA-NN) / Open (gate) /
Excluded); here it means the status the item will carry in the report.

| Candidate ID | Requirement | Priority (required / desired / future) | Source (labelled) | Status | Acceptance criteria noted |
|---|---|---|---|---|---|

## 7. Architecture alternatives explored

| Decision | Alternatives considered (advantage, disadvantage) | Recommendation and rationale | PI's response (verbatim) | Status |
|---|---|---|---|---|

## 8. Open questions

These move to `DECISIONS.md` *Waiting on the PI* at adoption. Every one has a gate: before planning,
before implementing <what>, or before deployment.

| Question | Affects | Gate (Needed by) | Can continue meanwhile |
|---|---|---|---|

## 9. Governance preferences

The PI's words on review depth, autonomy and check-ins, the agent arrangement, and data-semantics
policy (or "none named"). Record what the PI said; do not ask questions only to fill this.

## 10. Report version and state

- **Report:** `reports/PROJECT-DEFINITION.md`, {{not started / Draft vN, presented on <date> / revision
  requested: <what> / adopted by R-NN (vN)}}
- **Completeness check:** {{not run / run for vN: gaps <list or "none">}}
- **Pending approvals:** {{e.g. adoption of vN}}

## 11. Lead's interpretations

Each one labelled "Lead's interpretation:", with what it rests on. None is adopted.
