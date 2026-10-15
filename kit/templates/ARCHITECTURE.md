# ARCHITECTURE.md: how the instrument is built

**Governs:** the design: components, data flow, technical constraints and conformance rules
(`CLAUDE.md` §2).

- The lead agent proposes changes.
- A change that affects a scientific invariant, the data that are collected, or what a participant
  experiences is Tier C, and needs the PI's ruling.
- Other design changes are recorded as decisions in `DECISIONS.md`.

**Version:** v1.0, {{DATE}}.

## 1. Overview in plain language

{{Two or three paragraphs the PI can read. Cover what runs where, what the user or participant sees,
where data goes, and how results come out.}}

## 2. Platform and stack

| Choice | Value | Why (and alternatives considered) |
|---|---|---|
| Delivery | {{web app / desktop / R package / Python package / CLI / ...}} |  |
| Language(s) |  |  |
| Data storage |  |  |
| Output format(s) |  |  |
| Hosting / running |  |  |

## 3. Components and data flow

{{List each component, its responsibility, and what it reads and writes. A simple diagram is welcome.}}

## 4. Rules (A-NNN)

Each rule has a conformance state:

- **ENFORCED:** the code conforms, and an automated check guards it.
- **PARTIAL:** the code partly conforms, or no check exists.
- **TARGET:** agreed, but not yet built.

A rule is never weakened to match the code (`CLAUDE.md` §4). A state may be demoted by an audit, and
promoted only with evidence.

| ID | Rule | Protects (INV, REQ) | State | Guard |
|---|---|---|---|---|
| A-001 |  |  | TARGET |  |

## 5. Dependencies

New dependencies need approval (Tier C if they carry licence, cost or data implications). Record why
each was chosen.

| Dependency | Why | Licence | Approved by |
|---|---|---|---|
