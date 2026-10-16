#!/usr/bin/env python3
"""Summarize logs/events.jsonl for a sprint record (SPRINT-NN.md §2.7).

    python tools/summarize_events.py [--since 2026-10-20T09:00] [--until 2026-10-20T18:00]

Prints a Markdown table. Every measure is labelled with what it is and is not. See docs/EVENTS.md.

- Elapsed time: from the first to the last event in the window.
- Waiting on the PI: in each main session, from a Stop (the agent finished its turn) to the next
  prompt submission. This is an upper bound on time the team waited. It is NOT the PI's active
  time.
- Autonomous elapsed time: elapsed time minus waiting on the PI.
- Summed agent session time: main sessions plus subagents, added together. This can exceed
  elapsed time, because agents can work in parallel.
- Active PI time: only the PI's own `pi_time` entries. The hooks cannot measure it.
"""
import argparse
import datetime
import io
import json
import os
from collections import defaultdict


def _ts(s):
    s = s.replace("Z", "+00:00")
    t = datetime.datetime.fromisoformat(s)
    return t if t.tzinfo else t.replace(tzinfo=datetime.timezone.utc)


def _fmt(sec):
    sec = int(round(sec))
    return "%dh %02dm" % (sec // 3600, (sec % 3600) // 60)


def load(path, since=None, until=None):
    out = []
    if not os.path.exists(path):
        return out
    with io.open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
                r["_t"] = _ts(r["ts"])
            except Exception:
                continue
            if since and r["_t"] < since:
                continue
            if until and r["_t"] > until:
                continue
            out.append(r)
    out.sort(key=lambda r: r["_t"])
    return out


def summarize(events):
    if not events:
        return None
    elapsed = (events[-1]["_t"] - events[0]["_t"]).total_seconds()
    hook = [e for e in events if e.get("source") == "hook"]
    main = [e for e in hook if not e.get("agent_id")]

    by_session = defaultdict(list)
    for e in main:
        by_session[e.get("session_id")].append(e)

    waiting = 0.0
    session_time = 0.0
    prompts = 0
    for evs in by_session.values():
        session_time += (evs[-1]["_t"] - evs[0]["_t"]).total_seconds()
        stopped_at = None
        for e in evs:
            if e["event"] == "Stop":
                stopped_at = e["_t"]
            elif e["event"] == "UserPromptSubmit":
                prompts += 1
                if stopped_at is not None:
                    waiting += (e["_t"] - stopped_at).total_seconds()
                stopped_at = None

    sub_open, sub_time, sub_count = {}, 0.0, 0
    for e in hook:
        if e["event"] == "SubagentStart" and e.get("agent_id"):
            sub_open[e["agent_id"]] = e["_t"]
        elif e["event"] == "SubagentStop" and e.get("agent_id") in sub_open:
            sub_time += (e["_t"] - sub_open.pop(e["agent_id"])).total_seconds()
            sub_count += 1

    manual = defaultdict(int)
    pi_minutes = 0.0
    for e in events:
        if e.get("source") == "manual":
            manual[e["event"]] += 1
            if e["event"] == "pi_time" and e.get("minutes"):
                pi_minutes += float(e["minutes"])

    tools = sum(1 for e in hook if e["event"] in ("PostToolUse", "PostToolUseFailure"))
    failures = sum(1 for e in hook if e["event"] == "PostToolUseFailure")
    compactions = sum(1 for e in hook if e["event"] == "PreCompact")
    return {
        "elapsed": elapsed,
        "waiting": waiting,
        "autonomous": max(0.0, elapsed - waiting),
        "summed_agent": session_time + sub_time,
        "sessions": len(by_session),
        "subagents": sub_count,
        "prompts": prompts,
        "tools": tools,
        "tool_failures": failures,
        "compactions": compactions,
        "manual": dict(manual),
        "pi_minutes": pi_minutes,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--log", default=os.path.join("logs", "events.jsonl"))
    ap.add_argument("--since")
    ap.add_argument("--until")
    a = ap.parse_args()
    s = summarize(load(a.log, _ts(a.since) if a.since else None, _ts(a.until) if a.until else None))
    if s is None:
        print("No events in window (%s)." % a.log)
        return
    rows = [
        ("Elapsed time (first to last event)", _fmt(s["elapsed"]), "log"),
        ("Waiting on the PI (Stop to next prompt; upper bound, not PI active time)", _fmt(s["waiting"]), "log"),
        ("Autonomous elapsed time (elapsed minus waiting)", _fmt(s["autonomous"]), "log"),
        ("Summed agent time (sessions plus subagents; may exceed elapsed)", _fmt(s["summed_agent"]), "log"),
        ("Main sessions / subagent runs", "%d / %d" % (s["sessions"], s["subagents"]), "log"),
        ("PI prompt submissions (interaction events)", str(s["prompts"]), "log"),
        ("Tool calls (failures) / compactions", "%d (%d) / %d" % (s["tools"], s["tool_failures"], s["compactions"]), "log"),
        ("Manual coordination events", ", ".join("%s=%d" % kv for kv in sorted(s["manual"].items())) or "none", "agents"),
        ("Active PI time (self-reported only)", ("%.0f min" % s["pi_minutes"]) if s["pi_minutes"] else "not recorded", "PI"),
    ]
    print("| Measure | Value | Source |\n|---|---|---|")
    for r in rows:
        print("| %s | %s | %s |" % r)


if __name__ == "__main__":
    main()
