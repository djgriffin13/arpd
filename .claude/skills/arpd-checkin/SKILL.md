---
name: arpd-checkin
description: Give the PI a plain-language check-in on an ARPD project. Covers what works now, what needs the PI, what was decided without the PI, known problems, and resource use. Use when the PI types /arpd-checkin or asks "where are we?", "what do you need from me?" or "what happened while I was away?".
---

# ARPD check-in

Write a short, plain-language check-in for the PI. It should fit on one screen. Read these first:

- `STATUS.md`;
- the current or most recent sprint record in `reports/sprints/`;
- open decision packs in `reports/`;
- decisions recorded in `DECISIONS.md` since the last check-in, and the standing authorizations in force.

Then run `python tools/summarize_events.py --since <sprint start>`.

Cover:

1. **What now works**, as the PI would observe it, with the evidence in brackets (test name or check).
2. **What needs you**, ordered by what it unblocks. For each item, give:
   - the scientific consequence;
   - the options;
   - a recommendation;
   - the decision requested.

   Nothing consequential is adopted until the PI answers, or a standing authorization covers it.
3. **What was decided without you.** List delegated decisions individually, each with the standing
   authorization it used, and routine ones as a count. The PI may question or reverse any of them.
4. **Known problems and things not checked.** Also list any claims the PI should not make yet.
5. **Resource use.** Paste the summary table, keeping its labels. Never call log-derived time "your
   time": only the PI's own `pi_time` entries measure that.

**Focus on material decisions and exceptions.** Gloss every internal ID in plain words. Do not
re-explain routine coordination.

If the PI answers with a ruling, the lead agent records it **verbatim** in `DECISIONS.md` and logs
`python tools/log_event.py ruling --actor lead --ref R-NN`. Offer to log the PI's active minutes for
this check-in: `python tools/log_event.py pi_time --actor pi --minutes N`.
