---
name: arpd-amend
description: Amend an ARPD project's governing documents under the PI's authority. Records a ruling verbatim; records or changes a standing authorization (SA-NN); amends the team charter or paradigm specification; sets a project default (review depth, sprint transition policy, planning cadence); changes roadmap milestones; changes a requirement (including its acceptance criteria) or an architecture decision; adds, retires or changes a module; turns an incident into a rule; reopens a decision with its original rationale. Use when the PI types /arpd-amend or asks to change the rules, the science specification, the milestones, a requirement or design decision, the team arrangement, a project default, or what the agents may decide without asking.
argument-hint: "[ruling | authorization [SA-id] | charter | spec | default | roadmap | requirement <REQ-id> | decision <D-id> | module <name> | incident <id> | reopen <DEC-id>]"
---

# ARPD amendment

Governing documents change **only** by the PI's words (`CLAUDE.md` §3). This skill makes that easy
and auditable.

## What goes where

| The PI asks for | Route |
|---|---|
| A **project default** raised in `/arpd-setup` or `/arpd-plan`: review depth, sprint transition policy, planning cadence ("from now on, …") | An amendment, applied directly from the PI's clear words: the charter (for example §8 *Cadence*) when it changes a charter rule, or an SA when it delegates (for example, continuing across sprint boundaries). A this-time-only preference is not an amendment: it stays in the plan draft or the notes |
| A change to **milestones or the roadmap's direction** | `MASTER_PLAN.md` §2 (and §3 where the order follows), by ruling; the lead updates sprint rows in §3 on its own only as planning and close-outs record |
| A change to a **requirement**: its wording, or its *Requirement details* (acceptance criteria, priority, dependencies) | `REQUIREMENTS.md`, by ruling (a requirement changes only in that file, recorded as a decision): step 4, *Requirement* |
| A change to an **Architecture decisions** row (`ARCHITECTURE.md`): a different choice, a Provisional row confirmed, an Open one decided | By ruling when it is consequential (`CLAUDE.md` §6) and no SA covers it; otherwise a DEC on its route: step 4, *Architecture decision* |
| **Approval of a sprint plan**, or the **start of execution** | Recorded by `/arpd-plan` in its formats (plan-approval R-NN; execution R-NN; continuation SA). Use this skill only for a later change to them: a new ruling or SA that supersedes, narrows, widens or withdraws, never an edit |
| **Continuing across several sprints** without a check-in at each boundary | An SA, under the add-versus-change rules below |
| Everything else in this skill's description | The steps below |

1. **Get the PI's words.** If the PI has not yet stated the change, draft it as a decision pack item:
   - the scientific consequence;
   - the options;
   - a recommendation.

   Ask in a labelled block (`kit/docs/INTERACTION.md`): `APPROVAL REQUIRED` for the change itself,
   saying what a yes changes and in which files; `QUESTION FOR YOU` or `CHOICE FOR YOU` only to
   clarify. The block is last in the turn. Wait for the PI's reply. Never write a ruling the PI did
   not give. If the PI has stated the change,
   that is the ruling and the authorization: do not add a second approval step. Ask before recording
   only if the words could authorize materially different changes. Edge cases the words do not
   settle are recorded in the *Reading* line as the lead's reading, labelled as such, and listed in
   the read-back for the PI to correct; they do not hold up the change.
2. **State the scientific consequence** of a consequential change, before or as you record it, even
   when the PI stated the change directly (for example, a new way of counting a construct). Say:
   - which constructs, operationalizations, invariants and claims change;
   - which requirements and evidence must be re-sourced, or no longer hold;
   - which results, reference calculations or tests must be re-run or reworked ("none yet" if
     nothing has been built).

   This goes in the ruling's *Reading* line and in the read-back to the PI.
3. **Record the ruling verbatim** in `DECISIONS.md`, under the existing *Rulings* section (never a
   new `##` section; the ruling gets its own `### R-NN` heading there), as the next R-NN, typos included, with:
   - a *Given* line (directly in session, or relayed and confirmed on a date);
   - a *Reading* line, including the consequence from step 2;
   - a *Changes* line naming every file touched, with versions.
4. **Apply the change.**
   - **Charter:** edit `CLAUDE.md`, and add a version line naming R-NN.
   - **Paradigm spec:** never edit an accepted item. Add the new version, and mark the old one
     "Superseded by <ID> (R-NN)". Add to the spec's Version line a new version naming R-NN, keeping the earlier versions listed.
     - A new item's *PI's wording* column holds the PI's exact words. Any restatement of yours is
       labelled "(restated by the lead)", never put in the PI's mouth.
     - **Then follow the old ID through the repository.** Search for the superseded ID **and** for
       key phrases of the old rule's wording (prose often states a rule without its ID): claims in
       `PARADIGM-SPEC.md` §6, `ARCHITECTURE.md` (its overview as well as its A-rules),
       `REQUIREMENTS.md`, the charter's examples, standing authorizations in force, plans, code
       comments and tests. Update each dependent item you may update, and name it in the *Changes*
       line. **Text that records the PI's words (rulings and standing authorizations) is never
       edited**, even to fix a citation (the only addition ever made to such an entry is a status
       marker, such as "Superseded by SA-NN"); list those, and any accepted item you may not edit, in the
       read-back for the PI. The governance check flags live items that still cite a superseded ID,
       but not prose without the ID.
   - **Open scientific question:** add it to the *Open scientific questions* section of
     `PARADIGM-SPEC.md` (§9 in the kit's template), as the next Q-NN, with what it blocks and any
     default. If the spec has no such section (an older starter), add it at the end, citing R-NN.
     Other documents may refer to the Q-NN; the question itself lives only in the spec. `MASTER_PLAN.md` holds plans, backlog,
     risks and incidents, not open scientific questions.
   - **Module:** add it from `kit/constitution/modules/`, retire it (move its text to
     `docs/retired-rules.md`, citing R-NN), or change its arrangement values.
   - **Incident → rule:** the rule cites its incident ID from `MASTER_PLAN.md` §7.
   - **Reopening a decision:** write a new DEC entry that quotes the original rationale, says what
     changed and why that rationale no longer holds, and names the affected work. Mark the old entry
     "Reopened by DEC-NN".
   - **Requirement:** edit the row and its *Requirement details* entry in place, keeping the ID (a
     dropped requirement becomes Retired, citing R-NN; a requirement now future-priority moves to
     the `MASTER_PLAN.md` backlog and is Retired here), and record a DEC citing R-NN with the old
     and new text. If changed criteria undo existing evidence, return the state to what the
     remaining evidence supports, and name the tests to rework. Name any approved plan or open
     sprint that relied on the old criteria: an open sprint's Part 1 is never edited (its
     scope-change log records the effect); a plan not yet started may need re-planning.
   - **Architecture decision:** never rewrite the row's history. A different choice is a new row
     (next D-NN) and DEC, and the old row is marked "Superseded by D-NN (R-NN or DEC-NN)", keeping
     its text; confirming a Provisional row or deciding an Open item sets its *Status* to Adopted
     (R-NN) and removes its *Waiting on the PI* row. Update the platform table (§2) and any A-rule
     that follows, and follow the consequence into requirements and plans as above.
   - **Project default or milestone:** edit the charter line or `MASTER_PLAN.md` §2 row the PI's
     words change, citing R-NN, and nothing else. If an approved plan or an open sprint depended on
     the old default or milestone, name it in the read-back: an open sprint's Part 1 is never
     edited; its scope-change log records the effect, and a plan not yet started may need
     re-planning through `/arpd-plan`.
5. **Update `STATUS.md`** (you are the lead, its one writer): the current state, its *Readiness*
   block, *Waiting on the PI* and *Owed*, so they reflect the change.
6. **Dependency screen** (`kit/docs/INTERACTION.md` §7): has the change introduced, changed,
   resolved or exposed a dependency? If yes, trace only the affected requirements and work, and
   update their rows in `DECISIONS.md` *Waiting on the PI* (*Affects*, *Needed by*, *Can continue
   meanwhile*); remove a row the ruling decides. If no, say so in the read-back in one line.
7. **Read it back** to the PI in plain words: what changed, the consequence from step 2, any
   dependency it touched, and any dependent item you could not update.
8. **Check:** run `python tools/check_governance.py` and report the result verbatim.
9. **Log:** `python tools/log_event.py ruling --actor lead --ref R-NN --note "<one line>"`.
10. **Commit** with the ruling ID in the message.

## Recording or changing a standing authorization (SA-NN)

Delegation is recorded **only** as a standing authorization (`CLAUDE.md` §6). The PI can create or
change one in any message; no separate ruling is needed. If the PI delegates inside a ruling, record
the ruling as above **and** record the delegation as an SA that cites it.

1. **Get the PI's words.** If the scope is unclear, ask. Never widen a delegation beyond what the PI
   said, and never record as delegated anything §6 reserves to the PI.
2. **Record it verbatim** in `DECISIONS.md`, under *Standing authorizations*, as the next SA-NN,
   in the template's format (`kit/templates/DECISIONS.md`):
   - the PI's exact words, quoted;
   - **Given:** the session, or the ruling R-NN that created it (an SA may cite the ruling that
     created it);
   - **Supersedes:** the SA it changes or replaces, or "none" (step 3);
   - **Scope:** the work, assumptions or choices it covers, and its boundaries;
   - **Consult the PI when:** the triggers that still go to the PI;
   - **Reporting cadence** and **Practical limits**, if they differ from SA-01;
   - **In force until:** changed by the PI, or a stated end.

   An SA that sets or changes the authority profile (SA-01, or its replacement) uses SA-01's full
   field set instead: profile, purpose, scientific boundaries, permitted assumption changes,
   consultation triggers, reporting cadence and practical limits.
3. **Add, or change?** Decide from the PI's words.
   - **A new delegation that adds to those in force without changing any** (for example, "you may
     also choose the output file names") is a new SA with "Supersedes: none". Every SA in force,
     including SA-01's profile and its boundaries, stays in force unchanged.
   - **The PI changes an SA in force:** replaces it, narrows it, widens it or withdraws it (for
     example, "stop choosing column names without asking"). Record a new SA, or for a plain
     withdrawal a short SA entry quoting the PI, that **supersedes the one it changes**, and only
     that one. Carry over unchanged whatever the PI did not change. Never treat a new delegation as
     withdrawing or narrowing an existing one unless the PI said so.
   - **The profile changes** only when the PI changes it. The new SA supersedes SA-01 (or the SA
     that carries the profile), and the charter's *Authority profile* line is updated by the same
     route as any charter change.
   - Never edit an SA in force. A superseded SA is marked "Superseded by SA-NN" and keeps its text.
   - **Continuing across sprints.** An SA letting the team move past sprint boundaries without a
     new ruling uses the continuation fields (*Scope:* sprints S0N–S0M of PLAN-… vN; *Transition
     conditions*; *Consult the PI when*; the continuation format in `kit/templates/DECISIONS.md`).
     A first one adds ("Supersedes: none"); extending, narrowing or ending one supersedes only
     that SA. It never covers what `CLAUDE.md` §6 reserves to the PI, and it never changes the
     review, tests and close-out every sprint boundary keeps. A **project default** for transitions
     ("from now on, always continue after review") is either a charter §8 amendment or a standing
     SA, as the PI's words say; ask only if they could mean either.
4. **Read it back** to the PI in two or three plain sentences: what agents may now decide without
   asking, what still comes to the PI, and every SA now in force.
5. **Dependency screen**, as in step 6 above.
6. **Update `STATUS.md`, check, log and commit:** refresh STATUS's current state; run
   `python tools/check_governance.py`; log
   `python tools/log_event.py ruling --actor lead --ref SA-NN --note "<one line>"`; commit with the
   SA ID in the message.

**Pruning is welcome.** Ask the PI whether any rule no longer earns its cost. A charter should get
shorter as well as longer.

**When you wait for the PI:** end with exactly one labelled block (`kit/docs/INTERACTION.md` §2), as
plain text, not in a code fence. Nothing follows its closing divider.
