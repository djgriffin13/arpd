---
name: arpd-amend
description: Amend an ARPD project's governing documents under the PI's authority. Records a ruling verbatim; amends the team charter or paradigm specification; adds, retires or changes a module; turns an incident into a rule; reopens a decision with its original rationale. Use when the PI types /arpd-amend or asks to change the rules, the science specification or the team arrangement.
argument-hint: "[ruling | charter | spec | module <name> | incident <id> | reopen <DEC-id>]"
---

# ARPD amendment

Governing documents change **only** by the PI's words (`CLAUDE.md` §3). This skill makes that easy
and auditable.

1. **Get the PI's words.** If the PI has not yet stated the change, draft it as a decision pack item:
   - the scientific consequence;
   - the options;
   - a recommendation.

   Wait for the PI's reply. Never write a ruling the PI did not give.
2. **Record the ruling verbatim** in `DECISIONS.md` as the next R-NN, typos included, with:
   - a *Reading* line;
   - a *Changes* line listing files and versions.
3. **Apply the change.**
   - **Charter:** edit `CLAUDE.md`, and add a version line naming R-NN.
   - **Paradigm spec:** never edit an accepted item. Add the new version, and mark the old one
     "Superseded by <ID> (R-NN)".
   - **Module:** add it from `kit/constitution/modules/`, retire it (move its text to
     `docs/retired-rules.md`, citing R-NN), or change its arrangement values.
   - **Incident → rule:** the rule cites its incident ID from `MASTER_PLAN.md` §7.
   - **Reopening a decision:** write a new DEC entry that quotes the original rationale, says what
     changed and why that rationale no longer holds, and names the affected work. Mark the old entry
     "Reopened by DEC-NN".
4. **Check:** run `python tools/check_governance.py` and report the result verbatim.
5. **Log:** `python tools/log_event.py ruling --actor lead --ref R-NN --note "<one line>"`.
6. **Commit** with the ruling ID in the message.

**Pruning is welcome.** Ask the PI whether any rule no longer earns its cost. A charter should get
shorter as well as longer.
