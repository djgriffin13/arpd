---
name: arpd-amend
description: Amend an ARPD project's governing documents under the PI's authority. Records a ruling verbatim; records or changes a standing authorization (SA-NN); amends the team charter or paradigm specification; adds, retires or changes a module; turns an incident into a rule; reopens a decision with its original rationale. Use when the PI types /arpd-amend or asks to change the rules, the science specification, the team arrangement, or what the agents may decide without asking.
argument-hint: "[ruling | authorization [SA-id] | charter | spec | module <name> | incident <id> | reopen <DEC-id>]"
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

## Recording or changing a standing authorization (SA-NN)

Delegation is recorded **only** as a standing authorization (`CLAUDE.md` §6). The PI can create or
change one in any message; no separate ruling is needed. If the PI delegates inside a ruling, record
the ruling as above **and** record the delegation as an SA that cites it.

1. **Get the PI's words.** If the scope is unclear, ask. Never widen a delegation beyond what the PI
   said, and never record as delegated anything §6 reserves to the PI.
2. **Record it verbatim** in `DECISIONS.md`, under *Standing authorizations*, as the next SA-NN:
   - the PI's exact words, quoted;
   - **Given:** the session, or the ruling R-NN that created it (an SA may cite the ruling that
     created it);
   - **Profile:** consult first / bounded autonomy / exploratory autonomy (SA-01, or when the
     profile changes);
   - **Purpose;**
   - **Scientific boundaries:** what agents may decide within;
   - **Permitted assumption changes;**
   - **Consult the PI when:** the triggers that still go to the PI;
   - **Reporting cadence;**
   - **Practical limits:** time, compute, cost;
   - **Supersedes:** the SA it replaces, or "none";
   - **In force until:** changed by the PI, or a stated end.
3. **A change is a new entry.** Never edit an SA in force. Write the new SA-NN, and mark the old one
   "Superseded by SA-NN"; the old one keeps its text. If the profile changed, update the charter's
   *Authority profile* line by the same route as any charter change.
4. **Read it back** to the PI in two or three plain sentences: what agents may now decide without
   asking, and what still comes to the PI.
5. **Check, log and commit:** run `python tools/check_governance.py`; log
   `python tools/log_event.py ruling --actor lead --ref SA-NN --note "<one line>"`; commit with the
   SA ID in the message.

**Pruning is welcome.** Ask the PI whether any rule no longer earns its cost. A charter should get
shorter as well as longer.
