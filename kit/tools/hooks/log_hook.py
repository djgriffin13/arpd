#!/usr/bin/env python3
"""ARPD event-logging hook for Claude Code.

Appends one JSON line per hook event to <project>/logs/events.jsonl. It is a pure logger:

- it never prints to stdout (stdout from some hooks is injected into the agent's context);
- it never blocks;
- it always exits 0, even on error.

It records metadata only: no prompt text, tool inputs, tool outputs or file contents. The exact
fields are documented in docs/EVENTS.md. Set ARPD_LOG_PROMPT_TEXT=1 to also record prompt text,
for the PI's own projects only.
"""
import datetime
import io
import json
import os
import sys


def _now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="milliseconds")


def _record(payload):
    event = payload.get("hook_event_name", "unknown")
    rec = {
        "ts": _now(),
        "source": "hook",
        "event": event,
        "session_id": payload.get("session_id"),
        "agent_id": payload.get("agent_id"),
        "agent_type": payload.get("agent_type") or None,
    }
    if event == "SessionStart":
        rec["detail"] = payload.get("source")
        rec["model"] = payload.get("model")
    elif event == "SessionEnd":
        rec["detail"] = payload.get("reason")
    elif event == "UserPromptSubmit":
        prompt = payload.get("prompt") or ""
        rec["prompt_chars"] = len(prompt)
        if os.environ.get("ARPD_LOG_PROMPT_TEXT") == "1":
            rec["prompt"] = prompt
    elif event in ("PostToolUse", "PostToolUseFailure"):
        rec["tool"] = payload.get("tool_name")
        rec["duration_ms"] = payload.get("duration_ms")
        rec["outcome"] = "failure" if event == "PostToolUseFailure" else "ok"
        tool_input = payload.get("tool_input") or {}
        if isinstance(tool_input, dict) and payload.get("tool_name") in ("Agent", "Task"):
            rec["subagent_type"] = tool_input.get("subagent_type")
    elif event in ("SubagentStart", "SubagentStop"):
        pass  # agent_id / agent_type already captured
    elif event in ("PreCompact", "PostCompact"):
        rec["detail"] = payload.get("trigger")
    elif event == "Notification":
        rec["detail"] = payload.get("notification_type")
    return rec


def main():
    try:
        raw = sys.stdin.buffer.read().decode("utf-8", errors="replace")
        payload = json.loads(raw) if raw.strip() else {}
        project = os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or os.getcwd()
        log_dir = os.path.join(project, "logs")
        os.makedirs(log_dir, exist_ok=True)
        with io.open(os.path.join(log_dir, "events.jsonl"), "a", encoding="utf-8") as fh:
            fh.write(json.dumps(_record(payload), ensure_ascii=False) + "\n")
    except Exception:  # a logger must never interfere with the session
        pass
    sys.exit(0)


if __name__ == "__main__":
    main()
