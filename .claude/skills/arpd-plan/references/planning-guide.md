# Planning guide: read-back, draft, versions and review

Detail for Steps A–E of `/arpd-plan`. The shared conventions are in `arpd/docs/INTERACTION.md`.

## 1. Sizing the effort

Judge the size from the work, not from a line count: how many deliverables, how novel, how many
dependencies and unknowns, the risk, the time or compute, and the autonomy the PI wants.

| Project | Steps A–C | Plan |
|---|---|---|
| Small (a utility, one thrust) | One read-back and one question | One sprint, about a page |
| Medium | Read-back, priorities, one or two follow-ups | One sprint, with exit evidence, dependencies and review level |
| Large or uncertain | A short topic list, followed until the scope is clear; the question fuse applies | Several sprints if the PI chooses; the first precise, later ones provisional |

Suggest several sprints when they would help coordinate dependencies. Never impose them.

## 2. The read-back (Steps A and C)

Keep it to one screen. Every claim has a source the PI could check.

- **Done:** the last sprint's close-out (2.1 and 2.2), with the evidence named there.
- **Works now:** only what a record or a check run in this session shows. Quote the checker's
  OVERALL line.
- **Roadmap:** `MASTER_PLAN.md` §2 milestones and §3 order of work. If §3 says planning is pending,
  say so.
- **Blocked or waiting:** `DECISIONS.md` *Waiting on the PI*, with what each row affects and when it
  is needed.
- **Recommended thrust:** what, why now, which milestone and requirements it serves, what you would
  defer, and the main trade-off.

Do not restate the charter or list routine coordination.

## 3. Sprint numbering

The next sprint number is one more than the highest `reports/sprints/SPRINT-NN.md` (an imported
project may start at S00). If there is no sprint record and no imported history, it is S01. Never
renumber or reuse a number. A series takes consecutive numbers; the plan says they are proposed
numbers until each sprint starts.

## 4. The draft (Step D)

Copy `arpd/templates/planning/PLAN.md` to `reports/planning/PLAN-YYYY-MM-DD.md`. Use the date the
draft is first written. A second planning effort on the same day is `PLAN-YYYY-MM-DD-2.md`, and so
on. One file holds one planning effort through all its versions, including any revision after
approval.

The header carries, as the template sets out:

- the DRAFT banner and `Status: Draft` (after approval, the approved marker the template gives;
  the approved version's text is never edited);
- the *Version* line, and a *Change history* row for each version;
- the sprint(s) covered and the authorization sought (planning only / S0N / a series), in
  *Identity*.

Content per sprint. Write each heading even when the answer is short; "none" is a valid answer.

| Topic | Minimum content |
|---|---|
| Identity | Proposed sprint number; draft file and version; authorization sought |
| Outcome | The objective in one sentence, and what the PI will observe |
| Traceability | Milestone; requirement IDs and target states, with their acceptance criteria (`REQUIREMENTS.md` *Requirement details*); architecture decisions relied on (D-NN, noting any Provisional); paradigm-spec items, if any |
| Scope | Work packages in order, each with the task plans it expects (`plans/NNN` are written at execution, not now) |
| Dependencies | What must exist first; *Waiting on the PI* rows it relies on (cite the row number); work that is unaffected and can proceed |
| Exit | Observable exit criteria (when the sprint is done), each with the test or check that will show it. Task-plan acceptance criteria (`plans/NNN`) are drawn from the requirements' criteria |
| Boundaries | Non-goals; risks; constraints; time, compute or cost limits where relevant |
| Workflow | Team arrangement; independent review and test gates; resources |
| Authority | Decisions reserved to the PI; choices delegated by an SA in force (name it); execution authority sought |
| Handoff | What happens at the close; in a series, the transition policy and the condition for the next sprint |

**Minimal but sufficient.** A simple sprint does not need dozens of subtasks, named agents or
speculative risks. Do not claim certainty about work that depends on unresolved evidence.

**Scientific content.** Cite the scientific invariants the work must respect, and other spec
items, by ID in *Traceability*. Do not draft new constructs or invariants in a plan: a needed
change to the science is a pending decision (a *Waiting on the PI* row) or an `/arpd-amend` item.

**Later sprints in a series** are labelled *provisional*. For each, state:

- what it is expected to deliver;
- what evidence from the earlier sprints it depends on;
- what the lead may adjust at the boundary without a new approval (for example, the order of work
  packages, or splitting a package), recorded in that sprint's Part 1 and the close-out;
- what would need re-planning with the PI (a changed objective, requirement set, exit criterion, or
  anything reserved to the PI).

## 5. The dependency screen (Step D, and at every revision)

Ask the question in `INTERACTION.md` §7 about each work package. For every unresolved decision the
plan relies on:

1. Find its row in `DECISIONS.md` *Waiting on the PI*, or add one (decisions found in the spec's
   §9 *Open scientific questions* get a row that cites the Q-NN).
2. Fill *Affects* (requirements, and the named work packages and sprints), *Needed by* (the gate:
   before planning, before implementing a named work package, before deployment, or a date) and
   *Can continue meanwhile* (the work that does not depend on it). A row from setup keeps its gate;
   sharpen it to the work package, never loosen it.
3. In the plan, cite the row number. Do not copy its content into the plan.
4. Refresh the `STATUS.md` §5 summary, which points to the table.

Updating these columns is routine. Deciding the question is not: a consult-route question goes to
the PI as a decision item, at this planning meeting if it is needed soon, or batched for a later
check-in if it is not. Never invent a default that binds future scientific meaning to make a plan
look complete. A plan may be approved with a decision still open: the approval says which work it
blocks.

## 6. Versions and commits (Steps D and E)

- Commit every version that the PI is shown: `Plan draft PLAN-YYYY-MM-DD vN (not approved)`. The
  approval ruling cites that commit.
- A revision bumps the Version line and adds a *Change history* row. In chat, list what changed
  since the last version.
- The approval ruling, not the plan, is the authoritative record of the approved commit: a file
  cannot name the commit it is part of.
- **A revision after approval** stays in the same file. Bump the Version, add a *Change history*
  row, set the Status line to `Draft vN (vK approved by R-NN; vN not approved)`, and restore the
  DRAFT banner. The earlier approval stays valid only for vK (its cited commit); vN needs its own
  approval ruling. The ruling for vK is never edited.
- **When is a plan approved?** Only when its current Version line is the version an existing
  approval ruling names in its *Approves:* line. Otherwise it is a draft, even if an earlier
  version was approved; say which version was approved, and by which ruling.
- Commit only the plan file and the records Step D updates (`DECISIONS.md` *Waiting on the PI*
  rows, `STATUS.md`, and `START-HERE.md`'s *Map*, which gains a `reports/planning/` line with the
  first draft).
  Check `git status --short` first. Never push.
- No governing change happens during review. If review shows the charter, spec or roadmap
  milestones must change, that is an `/arpd-amend` item for the PI.

## 7. Outside review (Step E)

Offer it; require it only if the PI asks. For a small plan, say it is optional and usually
unnecessary.

When the PI wants one, brief a reviewer who did not write the plan (a fresh subagent or another
agent the PI names), read-only, with the plan file and version and the governing documents. Ask:
does it serve the milestone, requirements and the PI's priorities; is anything missing that the
exit criteria need; are the dependencies and their timing right, and is any work blocked that need
not be; is verification adequate (tests, known answers, independent review); are the instructions
clear enough to execute; what are the main risks, and are they bounded?

Enter each finding in the plan's *Review notes* table, with the version reviewed and your response.
A long report may also be saved as `reports/planning/PLAN-YYYY-MM-DD-review-N.md` (informative).
Log
`python arpd/tools/log_event.py review --actor reviewer --ref PLAN-YYYY-MM-DD --result PASS|FAIL --note "vN"`.
Revise the draft into a new version, and tell the PI which findings you took and which you did not,
and why. The PI may also bring a review from elsewhere: treat it the same way.

## 8. Worth explaining when it first matters

If the PI seems not to know them, say these once, above the block (`INTERACTION.md` §6): the draft
is theirs to examine, revise or have reviewed, and nothing is approved until they say so; several
sprints help when they share dependencies, and the PI chooses how the team moves between them;
every sprint has an independent review and a close-out record; approving the plan does not start
work; choosing "later" leaves a prompt to copy.
