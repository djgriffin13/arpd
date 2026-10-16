# Event log: what is captured, and what is not

`logs/events.jsonl` has one JSON object per line. It is append-only, and never edited by hand.

## Captured automatically (Claude Code hooks, `tools/hooks/log_hook.py`)

Every record has `ts` (UTC), `source: "hook"`, `event`, `session_id`, and, inside a subagent,
`agent_id` and `agent_type`.

| `event` | Extra fields | Meaning |
|---|---|---|
| `SessionStart` | `detail` (startup / resume / clear / compact / fork), `model` | A session began |
| `SessionEnd` | `detail` (reason) | A session ended |
| `UserPromptSubmit` | `prompt_chars` (and `prompt` only if `ARPD_LOG_PROMPT_TEXT=1`) | The PI sent a message: one **interaction event** |
| `PostToolUse` / `PostToolUseFailure` | `tool`, `duration_ms`, `outcome`, `subagent_type` (for Agent/Task) | A tool call finished |
| `SubagentStart` / `SubagentStop` | (`agent_id`, `agent_type`) | A subagent ran |
| `PreCompact` | `detail` (manual / auto) | Context was compacted (a continuity risk) |
| `Stop` | none | The main agent finished its turn, and is now waiting for the PI |
| `Notification` | `detail` (e.g. `idle_prompt`, `permission_prompt`) | Claude Code notified the PI |

**Not captured:** prompt text (by default), tool inputs and outputs, file contents, and model
reasoning.

## Recorded manually by agents and the PI (`tools/log_event.py`)

Hooks cannot see these events, so agents record them:

- `question`, `decision_pack`, `ruling`;
- `handoff`, `resume`, `interruption`;
- `review`, `sendback`, `incident`;
- `scope_change`, `sprint_start`, `sprint_close`.

The PI records `pi_time`: their own active minutes. **This is the only source of active human time.**

Manual events are as complete as the agents' compliance with the charter. A sprint audit compares
them with the sprint record and git.

## What the log can and cannot establish

| Measure | From the log? |
|---|---|
| Elapsed time; autonomous elapsed time (no PI prompt pending); summed agent time; number of PI interactions; subagent use; compactions | **Yes** (`tools/summarize_events.py`) |
| Time the team waited for the PI | **Upper bound only.** The PI may have been away or doing other work. |
| The PI's active time: thinking, reading, reviewing | **No.** Use the PI's `pi_time` entries and, in studies, coded screen recordings. |
| Whether an interaction was a scientific judgement or a coordination repair | **No.** That needs coding of the transcript or recording. |
| Token and credit cost | **No.** Take it from the tooling's usage reports. |

In studies with a simulated PI, interaction measures are **proxies** for human involvement, and are
labelled as such.
