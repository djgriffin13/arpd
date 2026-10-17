# PARADIGM-SPEC.md: {{PROJECT_NAME}}

**Governs:** the science. That covers the question, the constructs, the mechanisms, the
operationalizations, the invariants, the permitted claims and the validation plan
(`CLAUDE.md` §2).

**Changes only by the PI's ruling.** Agents may draft a change in a decision pack. They never edit
an accepted item. To change one, they add a new version of it and mark the old one *Superseded by
R-NN*.

**Version:** v1.0, {{DATE}}, ruling R-01.

This document is the bridge between the PI's science and the agents' engineering. Every requirement
in `REQUIREMENTS.md` traces back to an item here. Every claim the instrument licenses traces forward
to evidence listed here.

---

## 1. Research question

> {{The PI's own words, verbatim. Never paraphrased.}}

**Theoretical frame:** {{the theory or literature the question comes from, with key citations}}

## 2. Why this needs a new instrument

Explain why existing paradigms, tools or software cannot answer the question, or can answer it only
badly. Examples: the data exist but are not exposed; the model exists but only for a different
design; the construct is usually self-reported but should be observed.

{{...}}

## 3. Constructs and mechanisms

Each construct has a stable ID and a definition the PI accepts. Agents use these names exactly, in
code, interfaces and reports. If a construct needs renaming, that is a ruling, not a refactor.

The *PI's wording* column quotes the PI exactly, as given ("Name: definition"), including
capitalization. The short name is what agents use in code and reports.

| ID | Short name | PI's wording (verbatim) | Source |
|---|---|---|---|
| CON-01 |  |  |  |

## 4. Operationalizations

These state how each construct becomes something the instrument manipulates, records or computes.

| ID | Operationalizes | What the instrument does or records | Unit, timing and level (person, dyad, team, round, event) | Known limits |
|---|---|---|---|---|
| OP-01 | CON-01 |  |  |  |

## 5. Scientific invariants

An invariant is a property that must hold for the instrument to mean what we intend. The tests can
pass while an invariant is broken: plausible code can be silently wrong here. Breaking an invariant
is a defect even if every test passes (`CLAUDE.md` §4).

**Invariant, requirement or acceptance criterion?** Three different things:

| Term | What it says | Where it lives | How it works |
|---|---|---|---|
| Invariant (INV) | What must never break, or the results stop meaning what we intend | `PARADIGM-SPEC.md` §5 | The PI owns it. It holds for the life of the project. |
| Requirement (REQ) | What the instrument must do | `REQUIREMENTS.md` | It traces to a spec item or a ruling. It has a state and evidence. |
| Acceptance criterion | How one plan proves it delivered | Inside its plan, `plans/NNN-…` | It closes with the plan. Its evidence moves a requirement's state. |

| ID | Invariant | Why it matters scientifically | How it is checked |
|---|---|---|---|
| INV-01 |  |  |  |

<!-- Examples, from instruments built with this approach:
- "The partner agent updates its beliefs only at the end of a game, never within one."
- "Network ties are stored receiver-row: W_ij is the tie from j to i. Nothing transposes after import."
- "Missing is not zero: an unobserved tie is never treated as an absent tie."
- "Every event carries an integer millisecond timestamp, and intervals are half-open."
- "Participants in different conditions see identical instructions except for the manipulated text." -->

## 6. Claims

### 6.1 Claims the instrument is meant to support

| ID | Claim | Rests on (OP, INV, VAL) |
|---|---|---|
| CLM-01 |  |  |

### 6.2 Claims that must NOT be made

These are things a user, a report or an agent might be tempted to say, which the instrument cannot
support.

| ID | Claim that must not be made | Why not |
|---|---|---|
| NCL-01 |  |  |

<!-- Example: "That selection and influence estimates are causal effects. The model separates them
statistically, but does not identify them causally without further assumptions." -->

## 7. Validation plan

This is the scientific evidence that turns *Verified* into *Validated* (`CLAUDE.md` §7). Each item
says what evidence is needed, who produces it, and who accepts it. The PI accepts by ruling.

| ID | Validates | Evidence | Kind | Status |
|---|---|---|---|---|
| VAL-01 |  |  | known-answer · parameter recovery · reference calculation · expert walkthrough · pilot with people · comparison with established tool | Planned |

**Development checks are not validation.** A quick run that shows the code does what the design says
belongs in a plan or a test. A study of how well the method or measure works belongs here, as
planned, approved work (`CLAUDE.md` §7).

## 8. Out of scope

These are things this instrument will not do, so that agents do not drift into them.

- {{...}}

## 9. Open scientific questions

These are questions the PI has not yet decided. Agents must not decide them. Work that depends on
one waits, or builds against a clearly labelled placeholder.

| ID | Question | Blocks | Default if any |
|---|---|---|---|
| Q-01 |  |  |  |
