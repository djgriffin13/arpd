# DECISIONS.md: authorizations, rulings and decisions

**Governs:** the PI's direction and the project's recorded decisions (`CLAUDE.md` §3, §6). It holds
three ledgers:

- **Standing authorizations (SA-NN):** what the PI has delegated, and its scope. This is the only
  place delegation is recorded. The PI can create or change one in any message; a delegation given
  in a ruling is recorded here as an SA that cites the ruling. They persist across sessions until
  the PI changes them.
- **Rulings (R-NN):** the PI's own words, recorded verbatim when given.
- **Decisions (DEC-NN):** choices the project has made, each with its route and the authority it
  used.

**Rules**

- Rulings are quoted exactly. The lead agent's reading of a ruling goes on a separate line.
- A message relayed by another agent binds only once the PI confirms it directly.
- Nothing is edited after adoption. A change is a new entry that supersedes or reopens the old one,
  and the old one keeps its text.
- Every consequential decision records when it was **proposed**, **authorized** and **adopted**. The
  evidence for each date is the decision record and the event log, with git commits as supporting
  evidence. A commit time alone does not establish when a scientific choice was made.
- Authorization given *after* adoption is recorded as ratification, never as prior authorization.

---

## Waiting on the PI

This is the canonical list of open decisions. `STATUS.md` §5 summarizes it and points here; keep no
other tracker. Keep it short, and order it by what each item unblocks. Remove an entry once it is
decided. A decision the PI has deferred by ruling stays listed, marked "deferred (R-NN)", until it is
decided.

- **Affects:** the requirements and work that depend on the decision.
- **Needed by:** the gate: the point where the dependent work cannot go on without it (before
  planning, before implementing <what>, before deployment, or a named sprint or plan). Open items
  from the Project Definition Report arrive here at adoption with their gate.
- **Can continue meanwhile:** the work that does not depend on it. A pending decision blocks only
  the work that depends on it (`kit/docs/INTERACTION.md`, *Dependency screen*).

| # | Decision requested (plain language) | Pack | Affects (requirements, work) | Needed by | Can continue meanwhile | Recommendation |
|---|---|---|---|---|---|---|

---

## Standing authorizations

### SA-01, {{DATE}}: authority profile for this project

> "{{The PI's words from the setup interview, adopting or adjusting the proposed profile}}"

- **Given:** in the setup interview
- **Profile:** Consult first / Bounded autonomy / Exploratory autonomy
- **Purpose:**
- **Scientific boundaries** (what agents may decide within):
- **Permitted assumption changes:**
- **Data semantics** (missing versus zero, duplicates and repeats, identifier meaning, aggregation,
  precision or estimation assumptions, changes to collected variables, replacing unavailable data):
  never delegated unless a named policy: {{"none named" / the PI's policy, verbatim}}. Agents choose
  implementation mechanisms only (`CLAUDE.md` §6).
- **Consult the PI when:**
  - the research objective would change;
  - work would exceed the agreed scope or resource limits;
  - a contested interpretation would be settled;
  - {{project-specific triggers}}.
- **Reporting cadence:**
- **Practical limits:** time, compute, cost.
- **In force until:** changed by the PI.

<!-- keep: format for every later standing authorization (SA-02, ...), or a change to one:
### SA-NN, YYYY-MM-DD: what it covers
> "exact words"
- **Given:** directly in session (id), or in ruling R-NN (an SA may cite the ruling that created it)
- **Supersedes:** the SA-NN this one replaces, narrows, widens or withdraws, as the PI said; "none" for
  a new delegation that adds to those in force without changing any (they all stay in force)
- **Scope:** the work, assumptions or choices it covers, and its boundaries
- **Consult the PI when:** triggers that still go to the PI
- **Reporting cadence:** and **Practical limits:** if they differ from SA-01
- **In force until:** changed by the PI, or a stated end
Never delegate what CLAUDE.md §6 reserves to the PI.
-->

<!-- keep: format for an SA that lets execution continue across several sprints:
### SA-NN, YYYY-MM-DD: execution of sprints S0N–S0M
> "exact words"
- **Given:** directly in session (id), or in ruling R-NN
- **Supersedes:** the SA-NN it changes, or "none"
- **Scope:** sprints S0N–S0M of PLAN-YYYY-MM-DD vN
- **Transition conditions:** the sprint's independent review and close-out are done; no new
  scientific, scope or PI-reserved decision has arisen; any others the PI names
- **Consult the PI when:** a transition condition fails, or on any trigger the PI names
- **In force until:** sprint S0M closes, or the PI changes it
Every sprint boundary still gets its close-out, independent review and checks (CLAUDE.md §8).
-->

---

## Rulings

### R-01, {{DATE}}: adoption of the Project Definition Report and the governing documents

> "{{The PI's words adopting the report version, from the setup session}}"

- **Given:** in the setup session
- **Adopts:** `reports/PROJECT-DEFINITION.md` v{{N}}. The report is committed with this ruling, in
  the adoption-first commit; a ruling cannot name its own commit, so `STATUS.md` records the SHA.
- **Reading:** the report's Adopted-on-adoption items are adopted, with any proposals this ruling
  accepts ({{IDs, and how: "choice A" or named}}); its Delegated, Provisional, Open and Excluded items
  are recorded as such (open items O-NN become *Waiting on the PI* #N: {{mapping}}), and other
  Proposed items are not adopted. CLAUDE.md v1.0 and
  PARADIGM-SPEC.md v1.0 are written from it and are in force. The research question is PARADIGM-SPEC
  §1, verbatim. Adoption authorizes the governing documents only, not implementation.
- **Changes:** CLAUDE.md v1.0, PARADIGM-SPEC.md v1.0, REQUIREMENTS.md v1.0

<!-- keep: format for every ruling:
### R-NN, YYYY-MM-DD: subject
> "exact words"
- **Given:** directly in session (id) / relayed by (role), confirmed on (date)
- **Reading:** how it will be applied
- **Changes:** documents and versions changed, or "none"
-->

<!-- keep: format for the approval of a sprint plan (from /arpd-plan):
### R-NN, YYYY-MM-DD: approval of PLAN-YYYY-MM-DD vN
> "exact words"
- **Given:** directly in session (id)
- **Approves:** `reports/planning/PLAN-YYYY-MM-DD[-n].md`, version vN, commit <SHA>
- **Scope of approval:** planning only / S0N / series S0N–S0M
- **Execution authorized:** no / S0N / series under SA-NN
- **Reading:** how it will be applied, including any decision still in *Waiting on the PI* that
  blocks part of the plan, and which part
- **Changes:** documents and versions changed, or "none"
Approving a plan does not start work. When the PI gives no start direction, Execution authorized is
"no" and the scope is planning only. The PI's later "begin now" is its own ruling (R-NN), unless it
came in the same message as the approval.
-->

---

## Decisions

<!-- keep: format for every decision:
### DEC-NN: title
- **Scientific consequence:** what this changes about what the instrument measures, manipulates or licenses, or "none"
- **Route:** routine / delegated (SA-NN) / consult (R-NN)
- **Status:** proposed / under investigation / deferred by R-NN (still to decide; dependent work stays blocked) / adopted / superseded by DEC-NN / reopened by DEC-NN
- **Proposed:** date, by (role), with a pointer to the event-log entry or report
- **Authorized:** <ISO date>, <R-NN or SA-NN> (SA-NN for the delegated route, R-NN for the consult route); or "pending"; or "<ISO date>, <R-NN>, ratified after adoption (incident I-NN)"
- **Adopted:** <ISO date>, <version (commit or tag)>; or "not yet"
Dates are ISO 8601: YYYY-MM-DD, with a time (YYYY-MM-DDTHH:MMZ) when authorization and adoption fall
on the same day. Put the date first and the authority second, and keep other dates (a proposal date,
history) off the Authorized line. The governance check compares the dates, and cannot check other
formats or an Authorized line with several dates none of which is tied to the authority.
- **Context:** what prompted it, in plain language
- **Options considered:** each with its consequences
- **Decision:**
- **Reversibility:**
- **Evidence:**
-->
