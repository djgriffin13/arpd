---
name: arpd-checkin
description: Give the PI a plain-language check-in on an ARPD project. Covers readiness (setup, planning, execution), what works now, what needs the PI, decisions ahead and what they block, what was decided without the PI, known problems, resource use, and the exact next prompt. Use when the PI types /arpd-checkin or asks "where are we?", "what do you need from me?" or "what happened while I was away?".
---

# ARPD check-in

Write a short, plain-language check-in for the PI. It should fit on one screen.

**Python.** Before the first `python arpd/tools/...` command in a session, check for Python 3.8+
(`arpd/docs/NO-PYTHON.md` §1). Without it, use `sh arpd/tools/install.sh` in place of
`install.py`, and do what `arpd/docs/NO-PYTHON.md` says for every other tool command; nothing else
in this skill changes, and a read-through is never reported as a checker's PASS.

**A check-in changes no governing file except recording a ruling the PI gives in `DECISIONS.md`**
(last section). Otherwise it only reads and runs the two tools below.

Read these first:

- `STATUS.md`, including its *Readiness* block, §5 *Waiting on the PI* and §6 *Owed*;
- `DECISIONS.md`: *Waiting on the PI* (the canonical list of open decisions, with what each
  *Affects*, when it is *Needed by*, and what *Can continue meanwhile*); the decisions and rulings
  recorded since the last check-in; and the standing authorizations in force;
- the current or most recent sprint record in `reports/sprints/`;
- plans in `reports/planning/`. A plan is approved only if its current Version line is the version
  an existing approval ruling names (its *Approves:* line); otherwise report it as a draft, saying
  which earlier version, if any, was approved and by which ruling;
- open decision packs in `reports/`.

Then run both tools, every time:

- `python arpd/tools/check_governance.py`. Keep its actual OVERALL line and every step that is not PASS.
  Never state a checker result from memory or from an earlier run. If the checker cannot be run (it
  is missing, or it fails), say so plainly under "What needs you", with the error, and do not report
  the project as complete.
- **Reconcile the checker with `STATUS.md`.** If the checker reports a gap that STATUS does not list
  (for example, STATUS says "Nothing owed" while a file is MISSING), say that STATUS is out of date,
  and name each gap.
- `python arpd/tools/summarize_events.py --since <sprint start>`. If it reports no event log, or no events
  in the window, say so in plain words. Never invent figures. The `ruling` count includes standing
  authorizations (SA-NN), which are logged as rulings too.

**Reconcile readiness too.** Take *Setup*, *Planning*, *Execution* and *Next step* from `STATUS.md`
*Readiness*, and cross-check each against the records:

- Setup: `CLAUDE.md`'s Version line names an adoption ruling that exists in `DECISIONS.md`;
- Planning: a draft or approved plan in `reports/planning/`, and its approval ruling;
- Execution: an execution ruling or continuation SA, and an open or closed sprint record whose Part
  1 cites them.

If they disagree (for example, STATUS says "planning approved" but no ruling cites that plan, or a
sprint is open while STATUS says "not started"), say so and name each difference. The records win;
STATUS is out of date. The checker compares only the *Execution* line with the sprint records, as
an advisory; it does not check *Setup*, *Planning* or *Next step*, so never cite it as proof of
those.

**Open with a progress checklist**, one line per stage, before anything else, so the PI sees the
whole picture at a glance (✅ done, 🔵 in progress, ⚪ to come, ⚠️ blocked or failing):

```text
**Progress**
✅ Setup: blueprint adopted (R-01)
✅ Plan: PLAN-2026-10-27 v1 approved (R-02)
✅ S01, the game without the window: closed, review PASS
🔵 S02, the window: in progress, 2 of 4 work packages done
⚪ Your walkthrough of the first version
**Right now:** ⏳ a reviewer agent is checking S02 (nothing needed from you)
```

Take every line from the records you reconciled below; name each sprint of the approved plan, and
the milestone walkthrough when the plan has one. The *Right now* line is one of: ⏳ agents working
(nothing needed), ❓ waiting for your answer (to what), or ⏸️ idle (the next prompt to type). Write
the checklist as plain text, not in a code fence (the example is fenced only to show the layout).

Then cover:

1. **Readiness**, in one or two lines: setup, planning, execution, with the ruling or plan behind
   each. Name any plan draft awaiting review (file and version, "not approved"), and any approved
   plan not yet started.
2. **What now works**, as the PI would observe it, with the evidence in brackets (test name or check).
3. **What needs you**, ordered by what it unblocks. It includes:
   - every open item in *Waiting on the PI* that is needed now;
   - everything listed in `STATUS.md` §6 *Owed*;
   - every checker step that is not PASS, in plain words, with what the PI can do about it (for
     example, approve a file write, or run the commands listed under *Known gaps* in
     `START-HERE.md`);
   - a plan draft waiting for the PI's review or approval.

   For each decision, give:
   - the scientific consequence;
   - the options;
   - a recommendation;
   - the decision requested.

   Nothing consequential is adopted until the PI answers, or a standing authorization covers it.
   Do not present as routine a change to an accepted specification item, a standing authorization in
   force, or the charter: those change only by the PI's words (`/arpd-amend`). Installing `.claude/`
   files needs the PI's approval of Claude Code's permission prompt; say so.
   **Never say nothing is needed** while the checker's OVERALL line is not PASS, or §6 lists
   anything owed.
4. **Decisions ahead.** The open *Waiting on the PI* items not yet needed, grouped by the work they
   block (a sprint, work package or requirement), soonest *Needed by* first, each with what can
   continue meanwhile. Then the **quick dependency screen** (`arpd/docs/INTERACTION.md` §7): has
   recent work introduced, changed, resolved or exposed a dependency? If yes, name it, and say which
   *Waiting on the PI* row is missing or stale (updating it is routine work for the lead after the
   check-in, not part of it). If no, say so in one line.
5. **What was decided without you.** List delegated decisions individually, each with the standing
   authorization it used, and routine ones as a count. The PI may question or reverse any of them.
6. **Known problems and things not checked.** Also list any claims the PI should not make yet.
7. **Checks.** Quote the checker's OVERALL line exactly, and each step that is not PASS.
8. **Resource use.** Paste the summary table, keeping its labels, or the tool's own "no log" or "no
   events" line. Never call log-derived time "your time": only the PI's own `pi_time` entries
   measure that.
9. **Next step.** The exact prompt to copy, from `START-HERE.md` if it is current, or as readiness
   implies: `/arpd-setup` to finish setup; `/arpd-plan` when planning is pending; the plan's start
   prompt when a plan is approved and not started; the current sprint's next step when one is open.
   Never suggest implementation of work no approved plan covers.

**Focus on material decisions and exceptions.** Gloss every internal ID in plain words. Do not
re-explain routine coordination.

**When you ask the PI anything,** follow `arpd/docs/INTERACTION.md` §2–§3: end the turn with exactly
one labelled block (`QUESTION FOR YOU`, `CHOICE FOR YOU (select one)`, or `APPROVAL REQUIRED` for a
decision the PI is asked to rule on), as plain text, not in a code fence, with nothing after its
closing divider. Print every option before any choice widget. The next-step prompt goes above the
block.

If the PI answers with a ruling, the lead agent records it **verbatim** in `DECISIONS.md` and logs
`python arpd/tools/log_event.py ruling --actor lead --ref R-NN`. A ruling that settles a decision left
pending in a closed sprint record names that record and the row's ID (the record is not edited). Any change to a governing document that
the ruling asks for goes through `/arpd-amend`; plan approvals and execution starts go through
`/arpd-plan`. Offer to log the PI's active minutes for this check-in:
`python arpd/tools/log_event.py pi_time --actor pi --minutes N`.
