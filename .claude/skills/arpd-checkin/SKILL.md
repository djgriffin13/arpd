---
name: arpd-checkin
description: Give the PI a plain-language check-in on an ARPD project. Covers what works now, what needs the PI, what was decided without the PI, known problems, and resource use. Use when the PI types /arpd-checkin or asks "where are we?", "what do you need from me?" or "what happened while I was away?".
---

# ARPD check-in

Write a short, plain-language check-in for the PI. It should fit on one screen.

**A check-in changes no governing file.** It only reads, runs the two tools below, and records a
ruling verbatim if the PI gives one (last section).

Read these first:

- `STATUS.md`, including §5 *Waiting on the PI* and §6 *Owed*;
- the current or most recent sprint record in `reports/sprints/`;
- open decision packs in `reports/`;
- decisions recorded in `DECISIONS.md` since the last check-in, and the standing authorizations in force.

Then run both tools, every time:

- `python tools/check_governance.py`. Keep its actual OVERALL line and every step that is not PASS.
  Never state a checker result from memory or from an earlier run. If the checker cannot be run (it
  is missing, or it fails), say so plainly under "What needs you", with the error, and do not report
  the project as complete.
- **Reconcile the checker with `STATUS.md`.** If the checker reports a gap that STATUS does not list
  (for example, STATUS says "Nothing owed" while a file is MISSING), say that STATUS is out of date,
  and name each gap.
- `python tools/summarize_events.py --since <sprint start>`. If it reports no event log, or no events
  in the window, say so in plain words. Never invent figures.

Cover:

1. **What now works**, as the PI would observe it, with the evidence in brackets (test name or check).
2. **What needs you**, ordered by what it unblocks. It includes:
   - every open item in *Waiting on the PI*;
   - everything listed in `STATUS.md` §6 *Owed*;
   - every checker step that is not PASS, in plain words, with what the PI can do about it (for
     example, approve a file write, or run the commands listed under *Known gaps* in
     `START-HERE.md`).

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
3. **What was decided without you.** List delegated decisions individually, each with the standing
   authorization it used, and routine ones as a count. The PI may question or reverse any of them.
4. **Known problems and things not checked.** Also list any claims the PI should not make yet.
5. **Checks.** Quote the checker's OVERALL line exactly, and each step that is not PASS.
6. **Resource use.** Paste the summary table, keeping its labels, or the tool's own "no log" or "no
   events" line. Never call log-derived time "your time": only the PI's own `pi_time` entries
   measure that.

**Focus on material decisions and exceptions.** Gloss every internal ID in plain words. Do not
re-explain routine coordination.

If the PI answers with a ruling, the lead agent records it **verbatim** in `DECISIONS.md` and logs
`python tools/log_event.py ruling --actor lead --ref R-NN`. Any change to a governing document that
the ruling asks for goes through `/arpd-amend`. Offer to log the PI's active minutes for this
check-in: `python tools/log_event.py pi_time --actor pi --minutes N`.
