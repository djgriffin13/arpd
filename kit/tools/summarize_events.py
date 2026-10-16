#!/usr/bin/env python3
"""Summarize logs/events.jsonl for a sprint record (SPRINT-NN.md §2.7).

    python tools/summarize_events.py [--since 2026-10-20T09:00] [--until 2026-10-20T18:00]
    python tools/summarize_events.py --since ... --until ... --export reports/sprints/SPRINT-NN-events.jsonl

Prints a Markdown table. Every measure is labelled with what it is and is not. See docs/EVENTS.md.

- Elapsed time: from the first to the last event in the window. It includes idle time and the gaps
  between sessions.
- Agent-working time: in each main session, from each prompt submission to the end of that turn
  (Stop, StopFailure or SessionEnd), added up. Idle time and gaps between sessions are excluded. A
  turn with no end event in the window is counted up to the session's last event, and reported.
- Waiting after a turn: in each main session, from a Stop to the next prompt submission. This is an
  upper bound on time the team waited for the PI. It is NOT the PI's active time.
- Sessions with a turn that ended without a Stop: the turn ended in StopFailure or SessionEnd, or
  had no end event. These are failed or aborted turns.
- Prompt submissions: every UserPromptSubmit, from any source, including test or scripted prompts.
  They are not necessarily the PI's.
- Subagent time: subagent runs added together. They can overlap each other and the main session.
- Active PI time: only the PI's own `pi_time` entries. The hooks cannot measure it.

--export writes the raw log lines in the window to a file, so that a sprint's events can be
committed with its record (logs/ itself is not committed). It never overwrites an existing file.
"""
import argparse
import datetime
import io
import json
import os
import sys
from collections import defaultdict

TURN_END = ("Stop", "StopFailure", "SessionEnd")


def _ts(s):
    s = s.replace("Z", "+00:00")
    t = datetime.datetime.fromisoformat(s)
    return t if t.tzinfo else t.replace(tzinfo=datetime.timezone.utc)


def _fmt(sec):
    sec = int(round(sec))
    return "%dh %02dm %02ds" % (sec // 3600, (sec % 3600) // 60, sec % 60)


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
            r["_raw"] = line
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

    working = waiting = 0.0
    prompts = 0
    unended_turns = 0
    sessions_without_stop = 0
    for evs in by_session.values():
        turn_start = None   # time of the prompt that opened the current turn
        stopped_at = None   # time of the last Stop, while waiting for the next prompt
        bad = False
        for e in evs:
            ev = e["event"]
            if ev == "UserPromptSubmit":
                prompts += 1
                if stopped_at is not None:
                    waiting += (e["_t"] - stopped_at).total_seconds()
                    stopped_at = None
                if turn_start is None:
                    turn_start = e["_t"]
            elif ev in TURN_END:
                if turn_start is not None:
                    working += (e["_t"] - turn_start).total_seconds()
                    turn_start = None
                    if ev != "Stop":
                        bad = True
                stopped_at = e["_t"] if ev == "Stop" else None
        if turn_start is not None:  # the turn never ended within the window
            working += (evs[-1]["_t"] - turn_start).total_seconds()
            unended_turns += 1
            bad = True
        sessions_without_stop += bad

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
        "working": working,
        "waiting": waiting,
        "subagent_time": sub_time,
        "sessions": len(by_session),
        "sessions_without_stop": sessions_without_stop,
        "unended_turns": unended_turns,
        "subagents": sub_count,
        "prompts": prompts,
        "tools": tools,
        "tool_failures": failures,
        "compactions": compactions,
        "manual": dict(manual),
        "pi_minutes": pi_minutes,
    }


def export(events, path):
    if os.path.exists(path):
        sys.exit("refusing to overwrite %s; remove it or choose another name" % path)
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
        for e in events:
            fh.write(e["_raw"] + "\n")
    return len(events)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--log", default=os.path.join("logs", "events.jsonl"))
    ap.add_argument("--since")
    ap.add_argument("--until")
    ap.add_argument("--export", help="write the raw events in the window to this file (e.g. "
                                     "reports/sprints/SPRINT-NN-events.jsonl)")
    a = ap.parse_args()
    events = load(a.log, _ts(a.since) if a.since else None, _ts(a.until) if a.until else None)
    if a.export:
        n = export(events, a.export)
        print("Exported %d events to %s.\n" % (n, a.export))
    s = summarize(events)
    if s is None:
        print("No events in window (%s)." % a.log)
        return
    rows = [
        ("Elapsed time (first to last event; includes idle time and gaps between sessions)",
         _fmt(s["elapsed"]), "log"),
        ("Agent-working time, main sessions (prompt to end of turn: Stop, StopFailure or SessionEnd; "
         "idle time excluded)", _fmt(s["working"]) + (" (includes %d turn(s) with no end event)"
                                                     % s["unended_turns"] if s["unended_turns"] else ""), "log"),
        ("Waiting after a turn (Stop to next prompt; upper bound, not PI active time)", _fmt(s["waiting"]), "log"),
        ("Subagent time (summed; may overlap)", _fmt(s["subagent_time"]), "log"),
        ("Main sessions / with a turn that ended without Stop (failed or aborted) / subagent runs",
         "%d / %d / %d" % (s["sessions"], s["sessions_without_stop"], s["subagents"]), "log"),
        ("Prompt submissions (all sources, including test or scripted prompts)", str(s["prompts"]), "log"),
        ("Tool calls (failures) / compactions", "%d (%d) / %d" % (s["tools"], s["tool_failures"], s["compactions"]), "log"),
        ("Manual coordination events", ", ".join("%s=%d" % kv for kv in sorted(s["manual"].items())) or "none", "agents"),
        ("Active PI time (self-reported only)", ("%.0f min" % s["pi_minutes"]) if s["pi_minutes"] else "not recorded", "PI"),
    ]
    print("| Measure | Value | Source |\n|---|---|---|")
    for r in rows:
        print("| %s | %s | %s |" % r)


if __name__ == "__main__":
    main()
