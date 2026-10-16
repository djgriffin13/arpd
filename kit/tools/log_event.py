#!/usr/bin/env python3
"""Record a coordination event that the hooks cannot see.

Agents (and the PI) append manual events to logs/events.jsonl, for example:

    python tools/log_event.py question --actor lead --ref DP-2026-10-20 --note "asked PI about turnover rule"
    python tools/log_event.py handoff  --actor lead --note "STATUS.md rewritten before context reset"
    python tools/log_event.py review   --actor reviewer --ref plan-004 --result PASS
    python tools/log_event.py pi_time  --actor pi --minutes 25 --note "reviewed decision pack, 2 rulings"
    python tools/log_event.py adopted  --actor lead --ref DEC-04 --note "authorized by R-03; commit abc1234"

Event types and their meanings are listed in docs/EVENTS.md.
"""
import argparse
import datetime
import io
import json
import os

TYPES = [
    "question",      # agent asks the PI something
    "decision_pack", # consult-route decision sent to the PI
    "ruling",        # PI ruling, or a standing authorization (SA-NN), recorded
    "proposed",      # a consequential decision was proposed (--ref DEC-NN)
    "authorized",    # it was authorized (--ref DEC-NN; --note names the SA-NN or R-NN)
    "adopted",       # it was adopted (--ref DEC-NN; --note names the version or commit)
    "handoff",       # STATUS.md rewritten for a successor
    "resume",        # a session resumed from STATUS.md after a reset
    "interruption",  # work interrupted (by PI, error, limit, outage)
    "review",        # independent review completed
    "sendback",      # work returned on a failed check
    "incident",      # coordination/governance failure
    "scope_change",  # sprint scope changed after the plan
    "sprint_start",
    "sprint_close",
    "pi_time",       # PI's self-reported active minutes (the only source of active human time)
]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("type", choices=TYPES)
    ap.add_argument("--actor", required=True, help="role or session, e.g. lead, implementer-2, pi")
    ap.add_argument("--ref", default=None, help="IDs involved: plan, decision, ruling, sprint")
    ap.add_argument("--result", default=None, help="PASS / FAIL / INCOMPLETE where relevant")
    ap.add_argument("--minutes", type=float, default=None, help="for pi_time only")
    ap.add_argument("--note", default=None, help="one line")
    ap.add_argument("--log", default=os.path.join("logs", "events.jsonl"))
    a = ap.parse_args()
    rec = {
        "ts": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="milliseconds"),
        "source": "manual",
        "event": a.type,
        "actor": a.actor,
        "ref": a.ref,
        "result": a.result,
        "minutes": a.minutes,
        "note": a.note,
    }
    os.makedirs(os.path.dirname(a.log) or ".", exist_ok=True)
    with io.open(a.log, "a", encoding="utf-8") as fh:
        fh.write(json.dumps({k: v for k, v in rec.items() if v is not None}, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
