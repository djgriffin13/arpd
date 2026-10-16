# Event log: what is captured, and what is not

`logs/events.jsonl` has one JSON object per line. It is append-only, and never edited by hand.
`logs/` is not committed. At each sprint close, the lead exports that sprint's events to a committed
file (see *Keeping a sprint's events* below).

## Captured automatically (Claude Code hooks, `tools/hooks/log_hook.py`)

Every record has `ts` (UTC), `source: "hook"`, `event`, `session_id`, and, inside a subagent,
`agent_id` and `agent_type`.

| `event` | Extra fields | Meaning |
|---|---|---|
| `SessionStart` | `detail` (startup / resume / clear / compact / fork), `model` (may be null: Claude Code does not always supply it) | A session began |
| `SessionEnd` | `detail` (reason) | A session ended |
| `UserPromptSubmit` | `prompt_chars` (and `prompt` only if `ARPD_LOG_PROMPT_TEXT=1`) | A prompt was submitted: one **interaction event**. The source is not recorded: it may be the PI, a tester or a script |
| `PostToolUse` / `PostToolUseFailure` | `tool`, `duration_ms`, `outcome`, `subagent_type` (for Agent/Task) | A tool call finished |
| `SubagentStart` / `SubagentStop` | (`agent_id`, `agent_type`) | A subagent ran |
| `PreCompact` | `detail` (manual / auto) | Context was compacted (a continuity risk) |
| `Stop` | none | The main agent finished its turn, and is now waiting for the PI |
| `StopFailure` | `detail` (the error type, if the payload names one) | The turn ended in an error (for example, an API or authentication error). No `Stop` follows |
| `Notification` | `detail` (e.g. `idle_prompt`, `permission_prompt`) | Claude Code notified the PI |

**Not captured:** prompt text (by default), tool inputs and outputs, file contents, and model
reasoning.

## Recorded manually by agents and the PI (`tools/log_event.py`)

Hooks cannot see these events, so agents record them:

- `question`, `decision_pack`, `ruling` (a ruling, or a standing authorization SA-NN);
- `proposed`, `authorized`, `adopted`: when a consequential decision (`--ref DEC-NN`) was proposed,
  authorized (the note names the SA-NN or R-NN) and adopted (the note names the version). They are
  the timing evidence that the decision record cites (`CLAUDE.md` §6). A commit time alone is not;
- `handoff`, `resume`, `interruption`;
- `review`, `sendback`, `incident`;
- `scope_change`, `sprint_start`, `sprint_close`.

The PI records `pi_time`: their own active minutes. **This is the only source of active human time.**

Manual events are as complete as the agents' compliance with the charter. A sprint audit compares
them with the sprint record and git.

## What the log can and cannot establish

| Measure | From the log? |
|---|---|
| Elapsed time (includes idle time and gaps between sessions); agent-working time (each prompt to the end of its turn: `Stop`, `StopFailure` or `SessionEnd`, summed over sessions, so it can exceed elapsed time when sessions overlap; idle time excluded; a turn interrupted by a new prompt is closed at its last event); summed subagent time; turns interrupted or ended without a `Stop`; prompt submissions (any source); compactions; per-session activity (`--sessions`) | **Yes** (`tools/summarize_events.py`) |
| Time the team waited for the PI (`Stop` to the next prompt in the same session) | **Upper bound only.** The PI may have been away or doing other work. |
| Whether a prompt came from the PI | **No.** Prompt submissions count every source, including test or scripted prompts. |
| The PI's active time: thinking, reading, reviewing | **No.** Use the PI's `pi_time` entries and, in studies, coded screen recordings. |
| Whether an interaction was a scientific judgement or a coordination repair | **No.** That needs coding of the transcript or recording. |
| Token and credit cost | **No.** Take it from the tooling's usage reports. |

In studies with a simulated PI, interaction measures are **proxies** for human involvement, and are
labelled as such.

## Keeping a sprint's events

At sprint close, the lead exports the sprint's window and commits it with the sprint record:

    python tools/summarize_events.py --since <sprint start> --until <close> --export reports/sprints/SPRINT-NN-events.jsonl

The export holds the raw log lines in the window, unchanged. It never overwrites an existing file,
and an empty window writes nothing.
The same command prints the measures for the sprint record's resource-use table (§2.7). Events
outside any exported window stay only in the local, uncommitted log.

## Recovery after a lost session

The recovering lead runs `python tools/summarize_events.py --since <the time STATUS.md was last
rewritten> --sessions` and quotes its output in the `Recovered:` line of `STATUS.md` (`CLAUDE.md`
§9). It never describes the log from memory. The `--sessions` table has one line per main session:
start, end, prompts, tool calls, subagents, turns interrupted or ended without a `Stop`, and whether
the session did work (at least one tool call). Sessions that failed at once show "no".

If `logs/` is absent (a fresh clone, or another machine), the lead says so and runs the same command
with `--log` pointing at the last exported `reports/sprints/SPRINT-NN-events.jsonl`, together with
`git log`. Events after that export cannot be recovered.
