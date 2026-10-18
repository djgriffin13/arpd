# Sprint plan PLAN-{{YYYY-MM-DD[-n]}}: {{short title}}

> **DRAFT — not approved. Nothing here is scheduled or authorized.** This draft binds only once the
> PI approves an identified version by ruling (`DECISIONS.md`, `CLAUDE.md` §5, §8). Approving it does
> not start work: execution needs the PI's start direction or a standing authorization.

**Version:** v{{N}}, {{date}}. Every version is committed before the PI is asked to approve it. A
file cannot name its own commit: the approval ruling records the commit.

**Status:** Draft

<!-- After approval, the only edit to the approved version is the status marker. Set the Status
line to "Approved by R-NN (vN, commit <SHA>)", taking the SHA from the ruling. Replace the banner
with "APPROVED by R-NN (vN). Execution still needs the PI's start direction or a standing
authorization."
A revision after approval stays in this file. Bump the Version, add a Change history row, set the
Status line to "Draft vN (vK approved by R-NN; vN not approved)", and restore the DRAFT banner. The
earlier approval stays valid only for vK (its commit, cited in the ruling); vN needs a new approval
ruling. The plan counts as approved only when its current Version is the version an approval
ruling names. -->

## Change history

| Version | Date | What changed | Why (PI request, review note, new evidence) |
|---|---|---|---|
| v1 | {{date}} | First draft |  |

## Identity

| Field | Value |
|---|---|
| Proposed sprint numbers | {{S0N, or S0N–S0M}} |
| Scope of authorization sought | {{planning only / execution of S0N / execution of series S0N–S0M under an SA}} |
| Based on | `MASTER_PLAN.md` §3 row(s), `STATUS.md` *Readiness*, last sprint record |

## Sprint S{{NN}}: {{objective}}

Keep it minimal but sufficient. A simple sprint needs no long task list or speculative risks.

| Topic | Content |
|---|---|
| Outcome | The objective in plain language, and what the PI will observe afterwards |
| Traceability | Milestone; requirement IDs (their acceptance criteria are in `REQUIREMENTS.md` *Requirement details*); architecture decisions relied on (D-NN); paradigm-spec items, if any |
| Scope | Work packages, in order, with the expected task plans (`plans/NNN-…`) |
| Dependencies | What must exist first; pending decisions (`DECISIONS.md` *Waiting on the PI*); blockers; work that can go ahead regardless |
| Exit | Exit criteria (when the sprint is done), each with the evidence or test expected. Task-plan acceptance criteria (`plans/NNN`) are drawn from the requirements' criteria |
| Boundaries | Non-goals; risks; constraints; time, compute or cost limits where relevant |
| Workflow | Team arrangement; independent review and test gates; resources |
| Authority | Decisions reserved to the PI; choices delegated; the execution authority requested |
| Handoff | The next step; in a series, the review and transition criterion for the next sprint |

## Later sprints (provisional)

Repeat the table above for each later sprint, more briefly. Each one is **provisional**. Say what
could change it.

| Sprint | Objective | Provisional because | It may change if |
|---|---|---|---|

## Transition policy

For a series. The PI chooses one. Every sprint boundary still gets its close-out, independent review
and checks, whatever is chosen.

- **A. PI check-in** before each next sprint starts (the default).
- **B. Light check-in** at {{named points}}; otherwise continue after review and close-out.
- **C. Continue** after review and close-out under a standing authorization (SA-NN) naming the
  sprints, the transition conditions and when to consult the PI. This needs the PI's words.

**Chosen:** {{A / B / C, or "not yet chosen"; a single sprint: "Single sprint: per charter §8 / SA-01"}}

## Review notes

Notes from the PI's own review, and from any independent or third-party review. A third-party review
is optional, and is not needed for a small plan.

| Date | Reviewer (PI / agent / other) | Version reviewed | Finding | Response (changed in vN / not changed, why) |
|---|---|---|---|---|
