# Interaction conventions

These conventions apply to `/arpd-setup`, `/arpd-plan`, and the turns of `/arpd-checkin` and
`/arpd-amend` that wait for the PI. They say how to talk to the PI. They are not a governing
document and grant no authority. Each skill keeps its own steps and its own progress line.

## 1. Five kinds of information and action

| Kind | Example | What it does | Where it is recorded |
|---|---|---|---|
| 1. Interview answer | "I want a chat window for two players." | Informs the lead. Decides nothing. | Discovery or planning notes |
| 2. Proposal or draft | A requirement the lead suggests; a plan draft | Nothing is adopted, scheduled or authorized | The draft, labelled as a proposal |
| 3. Ruling or standing authorization | "Make light-touch review the default." | Binds, in the PI's words, within its scope. A direct instruction to change a rule is enough; `/arpd-amend` records it without a second approval. | `DECISIONS.md`, R-NN or SA-NN |
| 4. Approved plan | "I approve PLAN-2026-10-20 v3." | Approves that version's scope. It does not start work. | R-NN citing file, version and commit |
| 5. Execution authorization | "Begin sprint 1 now." | Starts the work it names. For a series, it says whether it covers the first sprint or the whole series. | R-NN, or SA-NN for a series |

- Silence is never kind 3, 4 or 5. Neither is "sounds good" about a nearby draft, nor a choice
  that only moves the interview on.
- A brainstorming remark ("I might want check-ins") is kind 1 or 2 until the PI's intent is clear.
  Ask only when the intent is materially unclear.
- When the PI approves a plan without saying more, record planning approval only.

## 2. The labelled block

When you wait for the PI, end the turn with one labelled block. The block opens with a divider
line, then the label alone on a line, then the question or choice, then a closing divider.

- `QUESTION FOR YOU`: gathering information. It is not an approval.
- `CHOICE FOR YOU (select one)` or `CHOICE FOR YOU (select one or more)`: a bounded choice. It is
  not an approval unless it says so.
- `APPROVAL REQUIRED`: a consequential, version-specific decision or governing change. In one or two
  sentences, say what is approved, which records change, and what a yes authorizes. Never use it to
  move to the next phase or to ask a preference.

Rules:

- **The block is last.** Nothing follows the closing divider: no extra request ("when you answer,
  also tell me…"), no tip, no summary. Anything else you need goes inside the block or waits for the
  next turn. Explanation, progress and tool results all go above it. Write the block
  as plain text, not inside a code fence (the examples here are fenced only to show the layout).
- **A closing turn has no block.** When the skill ends and does not wait for the PI (for example,
  after "later"), end with the next step and the exact prompt instead.
- **One primary open question per pause.** A bounded choice may allow several answers.
- **Restate the active question.** If tools ran after you asked (you saved notes, ran a check),
  repeat the question at the end, in a new block.
- **The label does not change meaning.** A PI's direct instruction to change a rule is a ruling even
  if no approval block was shown.
- **A reply to an approval that also adds something.** If the PI assents and in the same reply
  raises a new consideration that could change what is being approved ("Yes. But the scale
  definitions aren't final"), do not record the approval yet. Say how the new point affects the
  draft, and ask once: approve as is, or revise first. A clear assent with nothing new is recorded
  at once, without a second confirmation.

```text
SETUP  ✓ Project → ● Requirements → ○ Architecture → ○ Team & Governance → ○ Definition Report
✓ Who uses it  ◉ Main workflow  ○ Data to keep (partial)  ○ Exports

────────────────────────────────
QUESTION FOR YOU
Walk me through one complete use, from the moment a student opens the app to the moment you see
their answers. Describe the full version you imagine; we will choose the first useful version later.
────────────────────────────────
```

## 3. Choices: print them before any widget

A native choice widget can vanish from the transcript. Before you open one:

1. print the full question;
2. print every option on its own line, starting `A.`, `B.` and so on, with enough words to tell them
   apart;
3. say whether to select one or more (the label says it);
4. mark any recommendation as "(recommended)". Never preselect an option silently.

Then you may open the widget with the same question and options. Record the answer: in the
discovery or planning notes for an ordinary answer, and verbatim in `DECISIONS.md` for a ruling or
an approval. If the widget fails, the printed block stands and the PI can answer by letter.

```text
────────────────────────────────
CHOICE FOR YOU (select one)
How should the team treat the theory behind this estimator?
A. Use it to guide implementation, without evaluating it.
B. Identify theoretical or methodological concerns as we go.
C. Help me develop it.
D. Leave theory aside.
────────────────────────────────
```

## 4. Progress lines

Show the skill's progress line above the block on every interview turn.

- **Setup:**
  `SETUP  ● Project → ○ Requirements → ○ Architecture → ○ Team & Governance → ○ Definition Report`
  (two spaces after `SETUP`; ✓ done, ● current, ○ to come). Under it, list the current phase's topics (◉ marks the current
  focus). With more than about six topics, show the counts line instead:
  `3 complete | 2 partial | 6 open; next: <topic>`, and add "Full phase plan on request."
- **Plan:** `PLAN  ✓ Review → ● Priorities → ○ Draft → ○ Approval → ○ Handoff`. Add topics
  (priorities, scope, dependencies, review level, exit evidence) when they help.

Progress is honest:

- Never show a percentage. The topic list changes as you learn.
- Set each topic's status from the whole answer, not only from the question you asked. One answer
  can close several topics.
- The topic list is a working aid, not a questionnaire.

## 5. Question fuse

After about 3–5 substantive questions in a phase or topic, stop and synthesize:

- what you now understand;
- the gaps that matter, and what they affect;
- a choice: add more, or move on.

The PI may ask to keep exploring. A phase ends when the understanding is enough to act on, not
when a list is full. Record deferred items with what they affect. Moving on is ordinary agreement,
not adoption of anything.

## 6. Explain when needed

- Use language suited to the PI. Gloss a technical term the first time it matters, and stop once
  the PI shows they know it. Never infer low research expertise from low coding experience.
- Explain an important engineering concept (where data live, what a dependency costs, what an
  approval changes) when a decision depends on it, in one or two sentences, above the block.
- For a consequential choice, give the options, their trade-offs and your recommendation, with the
  reason in one plain sentence.
- Say once what the process will do. After that the progress line carries it: do not narrate the
  process on every turn.
- Do not ask questions just to establish the PI's expertise. Infer it from how the PI writes, and
  adjust when they correct you.

## 7. Dependency screen

At each of these points, ask yourself one quick question:

- at setup synthesis;
- at sprint planning;
- at task planning;
- at a material change during implementation;
- at independent review;
- at sprint close-out;
- at check-in.

> Has this introduced, changed, resolved or exposed a dependency on a pending decision or on
> another requirement?

- **If no,** carry on. Do not audit the whole project.
- **If yes,** trace only the affected requirements and work, and update the entry.

**One canonical list.** It is `DECISIONS.md` *Waiting on the PI*, with the columns *Affects*,
*Needed by* and *Can continue meanwhile*. `STATUS.md` §5 summarizes it and points to it. Keep no
other tracker. Before adoption, open questions live in the discovery notes; they move to *Waiting on
the PI* at adoption.

**Block only what depends on it.** A pending decision blocks only the work that depends on it, from
the point where it is needed. Continue independent authorized work. Raise future blockers early, at
check-ins and planning, in batches, not every turn. Updating the dependency columns is routine.
Changing a requirement still needs a ruling.

## 8. ASCII fallback

Use this when output may not render Unicode (for example, redirected Windows output or plain log
files), or when the PI asks.

| Unicode | ASCII |
|---|---|
| `────────────────────────────────` | `--------------------------------` |
| ✓ | `[x]` |
| ● | `[>]` |
| ◉ | `[*]` |
| ○ | `[ ]` |
| → | `->` |

The labels and the option letters stay the same. The setup line in ASCII:
`SETUP  [>] Project -> [ ] Requirements -> [ ] Architecture -> [ ] Team & Governance -> [ ] Definition Report`
