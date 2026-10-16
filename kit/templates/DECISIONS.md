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

Keep this list short, and order it by what each item unblocks. Remove an entry once it is decided.
A decision the PI has deferred by ruling stays listed, marked "deferred (R-NN)", until it is decided.

| # | Decision requested (plain language) | Pack | Blocks | Recommendation |
|---|---|---|---|---|

---

## Standing authorizations

### SA-01, {{DATE}}: authority profile for this project

> "{{The PI's words from the setup interview, adopting or adjusting the proposed profile}}"

- **Given:** in the setup interview
- **Profile:** Consult first / Bounded autonomy / Exploratory autonomy
- **Purpose:**
- **Scientific boundaries** (what agents may decide within):
- **Permitted assumption changes:**
- **Consult the PI when:**
  - the research objective would change;
  - work would exceed the agreed scope or resource limits;
  - a contested interpretation would be settled;
  - {{project-specific triggers}}.
- **Reporting cadence:**
- **Practical limits:** time, compute, cost.
- **In force until:** changed by the PI.

<!-- Format for every later standing authorization (SA-02, ...), or a change to one:
### SA-NN, YYYY-MM-DD: what it covers
> "exact words"
- **Given:** directly in session (id), or in ruling R-NN (an SA may cite the ruling that created it)
- **Supersedes:** SA-NN, or "none"
- **Scope:** the work, assumptions or choices it covers, and its boundaries
- **Consult the PI when:** triggers that still go to the PI
- **Reporting cadence:** and **Practical limits:** if they differ from SA-01
- **In force until:** changed by the PI, or a stated end
Never delegate what CLAUDE.md §6 reserves to the PI.
-->

---

## Rulings

### R-01, {{DATE}}: adoption of the team charter and the paradigm specification

> "{{The PI's words adopting CLAUDE.md v1.0 and PARADIGM-SPEC.md v1.0, from the setup interview}}"

- **Given:** in the setup session
- **Reading:** CLAUDE.md v1.0 and PARADIGM-SPEC.md v1.0 are in force. The research question is
  PARADIGM-SPEC §1, verbatim.
- **Changes:** CLAUDE.md v1.0, PARADIGM-SPEC.md v1.0, REQUIREMENTS.md v1.0

<!-- Format for every ruling:
### R-NN, YYYY-MM-DD: subject
> "exact words"
- **Given:** directly in session (id) / relayed by (role), confirmed on (date)
- **Reading:** how it will be applied
- **Changes:** documents and versions changed, or "none"
-->

---

## Decisions

<!-- Format:
### DEC-NN: title
- **Scientific consequence:** what this changes about what the instrument measures, manipulates or licenses, or "none"
- **Route:** routine / delegated (SA-NN) / consult (R-NN)
- **Status:** proposed / under investigation / deferred by R-NN (still to decide; dependent work stays blocked) / adopted / superseded by DEC-NN / reopened by DEC-NN
- **Proposed:** date, by (role), with a pointer to the event-log entry or report
- **Authorized:** date and authority (SA-NN for the delegated route, R-NN for the consult route), or "pending", or "ratified after adoption (incident I-NN)"
- **Adopted:** date and version (commit or tag)
- **Context:** what prompted it, in plain language
- **Options considered:** each with its consequences
- **Decision:**
- **Reversibility:**
- **Evidence:**
-->
