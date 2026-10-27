# Tutorial: build a Spades game with ARPD

In this tutorial you use ARPD to have AI agents build a small Spades card game with a window: you
plus three computer players, one of them your partner. You act as the researcher in charge (ARPD
calls you the **PI**). You describe what you want, settle the decisions that are yours, approve a
plan, and the agents build and test the game.

**Before you start:** finish **Start here** in the [README](README.md). You should be in your
`spades-demo` folder with Claude Code running.

**Time:** *[to be measured]*. **Agent use:** *[to be measured]*.

## How to use this tutorial

Each step shows:

- **▶ Type:** text to type or paste at Claude Code's prompt.
- **ARPD will ask something like:** what to expect.
- **Reply:** text you can copy and paste.

**ARPD is not scripted.** Its wording, and sometimes its order, differ from run to run. Read what
it actually asks and answer that. The replies here cover the questions that usually come up.

**The standing reply.** For a routine question this tutorial does not cover, paste:

```text
Use your recommendation. Keep it as simple as possible — this is a demo.
```

**Approvals are different.** The standing reply never counts as **adopting** the project
definition, **approving** a plan, or saying **begin**. At those three points, marked ✋ below, read
what ARPD shows you. Use the given reply only if it matches what you asked for; otherwise say what
is wrong. Those approvals are what keep you in charge.

**Permission prompts.** Claude Code asks before it edits files or runs commands. For edits and
commands inside your `spades-demo` folder, choose **Yes** (or the option that allows them for this
session). Say **No** to anything outside the folder you did not expect, and ask ARPD why.

---

## Part 1: Setup

Setup interviews you in phases (Intake, Objectives, Constraints, Design, Development), confirms a
summary at the end of each, and then writes a **Project Definition Report** for you to adopt.

### 1. Start setup

**▶ Type:**

```text
/arpd-setup
```

**ARPD will ask something like:** what you would like to accomplish.

**Reply:** paste this whole brief.

```text
I want a simple Spades card game with a window (GUI) that I can play on this computer: me plus
three computer players. The player opposite me is my partner. Use Python with its built-in Tkinter
and no other packages. Keep it simple: no networking, no card images (text like "Q♥" is fine), no
saving, no clever AI. A later version could be networked; not now.

Rules: standard four-player partnership Spades.
- 52 cards, 13 each. The first dealer is random; then the deal passes clockwise.
- Bidding starts left of the dealer and goes clockwise, one round, no passing. Each player bids
  0-13; a bid of 0 is nil. No blind nil. A team's bid is the sum of the partners' bids.
- The player left of the dealer leads first. Players must follow suit if they can; otherwise they
  may play any card. The highest spade wins the trick, or else the highest card of the suit led.
  The winner leads next.
- Spades may not be led until a spade has been played on another suit, unless the leader holds only
  spades.
- A team that makes its bid scores 10 x bid, plus 1 per extra trick (a "bag"); a team that falls
  short scores -10 x bid. Nil scores +100 if that player takes no tricks, -100 if they take any; the
  partner's bid is scored on its own, and a nil bidder's tricks don't count toward it but do count
  as bags. Every 10 bags costs 100 points; extra bags carry over.
- The first team to 500 wins. If both reach 500 on the same hand, the higher score wins. If the
  scores are tied, play another hand.

Computer players use exactly these rules, nothing more. They choose only from the cards they may
legally play. Card order for "lowest" and "highest": non-spades by rank (on equal rank, clubs <
diamonds < hearts), then spades by rank.
- Bid: count 1 per ace, 1 per king with at least one other card of its suit, and 1 per spade beyond
  the third. If the count is 0 and the hand has no spade above 10, bid nil; otherwise bid the count,
  at least 1.
- Lead: the highest card of its longest non-spade suit (on equal length: clubs, then diamonds, then
  hearts); if it may lead only spades, its lowest spade.
- Not leading: if its partner is winning the trick, play its lowest card; otherwise its lowest card
  that would win; if none would win, its lowest card.
- If it bid nil: lead its lowest card; otherwise play its highest card that would not win, or, if
  every card would win, its highest card. Its partner plays normally.

In the window: my hand as clickable cards, with only legal cards active; the four cards on the
table; each player's bid and tricks; both teams' scores and bags; computer plays shown with a short
pause; buttons to bid 0-13; a summary after each hand; a new-game button at the end.

Tests: the rules, the scoring, each computer rule, and a game played by four computer players to
the end, which fails if no team has won within 200 hands.
```

### 2. Where the project lives

**ARPD will ask something like:** where the project should live, with options such as *here, in
this folder (recommended)*, a new folder, or an existing repository.

**Reply:**

```text
Here, in this folder.
```

ARPD then turns this folder into your project: a fresh git history, and ARPD's own files (this
tutorial included) moved to a backup folder beside it. Nothing is deleted.

- If it shows a preview first and asks to go ahead, reply `Yes, go ahead.`
- If Claude Code's safety check blocks the command, ARPD gives you **one line starting with `!`**.
  Copy that line exactly, paste it at the prompt and press Enter.

### 3. About you and the users

**ARPD will ask something like:** how comfortable you are with code, and how involved you want to
be in technical decisions.

**Reply:**

```text
I can run scripts but prefer not to write code. Ask me about the game rules, not technical details.
```

**If it asks who will use the tool:**

```text
Only me, on this computer.
```

### 4. ARPD's role

**ARPD will ask something like:** *What role would you like me to play?* with options A to F.

**Reply:**

```text
A
```

*(A = build what you specify, raising only problems that would stop it working.)*

> **Look here:** the role you pick is recorded, and it sets how far ARPD questions your design.

### 5. Phase summaries

At the end of each phase ARPD shows a summary and asks whether it is right.

**Reply, only if the summary matches the brief:**

```text
Yes, that's right. Continue.
```

Otherwise, say what is wrong, in plain words.

### 6. Objectives

**If it asks what would convince you that it works:**

```text
I can play a hand in the window and the computer players follow the stated rules. Tests check the
rules, the scoring, each computer rule, and a full all-computer game to 500.
```

**If it asks what the tool will not do:**

```text
No networking, no saving games, no smarter computer players, no sound or card images.
```

**If it asks about research questions or theory:**

```text
None. This is a demonstration game, not a research instrument.
```

### 7. Constraints

**If it asks about platform, cost or technology:**

```text
My own computer, offline. Python with Tkinter only, no extra packages. Keep agent use low.
```

**If it asks about a rule detail the brief already answers,** point to it:

```text
The rules in my first message settle that.
```

**If it asks about a rule detail the brief does not settle,** that is ARPD doing its job: game
rules are your decision, not the agents'. Answer it, or reply:

```text
Use the standard Spades rule. Record it as my ruling.
```

> **Look here:** ARPD records your rulings word for word. Later they appear in `DECISIONS.md`.

### 8. Design

**If it asks for your own design ideas, or offers design alternatives:**

```text
Use your recommendation: the simplest design that keeps the game rules testable without the window.
```

### 9. Development: how the agents work

**ARPD will ask something like:** *How should the agents work on this project?* with options A to D.

**Reply:**

```text
A
```

*(A = one agent builds; a fresh reviewer agent that did not write the code checks each change.)*

**If it then asks for anything more about how the agents run:**

```text
No, nothing more.
```

**If it asks about priorities or a minimum version:**

```text
The whole game is the first priority. Nothing else.
```

**If it asks whether to include ARPD's logging and agent-role files:**

```text
Yes, include them.
```

### 10. ✋ Adopt the Project Definition Report

ARPD writes `reports/setup/PROJECT-DEFINITION.md`, shows you a summary, and asks you to adopt it.

> **Look here:** open `reports/setup/PROJECT-DEFINITION.md` in any text editor. Check that the game
> rules and the computer players' rules are recorded as yours, and that nothing you did not ask
> for has crept in.

**Reply, only if it matches what you asked for** (use the version number ARPD shows):

```text
I adopt version 1 of the Project Definition Report.
```

Otherwise, say what to change. ARPD revises the report and asks again.

After adoption, ARPD writes the project's governing documents: the team charter (`CLAUDE.md`),
`REQUIREMENTS.md`, `DECISIONS.md` and others. It may ask permission to write files in `.claude/`;
answer **Yes**. When it says setup is complete, go on to Part 2. If it suggests starting a new
Claude Code session, type `/exit`, then `claude`, in the same folder.

---

## Part 2: Planning

### 11. Start planning

**▶ Type:**

```text
/arpd-plan
```

**ARPD will ask something like:** what you want this piece of work to achieve.

**Reply:**

```text
The first playable version: the whole game as defined, with its tests.
```

### 12. ✋ Approve the plan

ARPD drafts a plan and asks you to approve that exact version.

> **Look here:** the plan is saved, with its version, under `reports/planning/`. Approval applies
> to that version only. If it changes, ARPD asks again.

**Reply, only if the plan matches what you asked for** (use the version ARPD shows):

```text
I approve version 1 of this plan.
```

### 13. ✋ Begin

**ARPD will ask something like:** whether to begin now or later.

**Reply:**

```text
Begin now.
```

---

## Part 3: The build

The agents now write the game and its tests, and a separate reviewer agent checks each change.
This takes a while. Claude Code shows what they are doing.

- **Permission prompts:** allow running Python and the tests inside your folder.
- **If ARPD stops with a question:** answer it. For routine choices, use the standing reply.
- **If the session ends** (you close the terminal, or hit a usage limit): run `claude` in the same
  folder, then type `/arpd-checkin`. ARPD reports where things stand and what to do next.

When ARPD reports the work finished:

> **Look here:** the close-out report under `reports/sprints/`, and `REQUIREMENTS.md`, where each
> requirement shows whether it is *Implemented* or *Verified* (tested).

**▶ Type:**

```text
/arpd-checkin
```

### 14. Play

The command to start the game is in `START-HERE.md` in your folder (or ask ARPD:
`How do I start the game?`). It is usually:

- **Windows:** `py spades.py`
- **macOS / Linux:** `python3 spades.py`

Run it in a second terminal window, in the same folder. **Play one hand.** A full game to 500 is
optional; the tests already play whole games.

If something looks wrong, tell ARPD in plain words, for example:

```text
My partner played a spade when it could have followed suit.
```

That is the normal loop: you report, the agents fix and test, and you check.

---

## If something goes wrong

| Problem | What to do |
|---|---|
| `claude` is not found | Open a new terminal window. See the README, step 3 |
| The game window does not open | Run the Tkinter check from the README, step 4 |
| A command is blocked by Claude Code's safety check | Paste the one-line `!` command ARPD gives you |
| The session closed or crashed | `claude` in the same folder, then `/arpd-checkin` |
| You hit a usage limit | Wait for it to reset, then `claude` and `/arpd-checkin` |
| ARPD asks something you don't understand | Ask it: `What does that mean, and what do you recommend?` |

## What to look at afterwards

- `CLAUDE.md`: the team charter the agents work under.
- `DECISIONS.md`: your rulings, word for word.
- `REQUIREMENTS.md`: each requirement and its evidence.
- `reports/`: the setup record, the approved plan, and the sprint close-out.
- `arpd/docs/GUIDE.md`: the full guide to using ARPD for your own projects.
