# Tutorial: build a Spades game with ARPD

In this tutorial you use ARPD to have AI agents build a small Spades card game with a window: you
plus three computer players, one of them your partner. You act as the researcher in charge (ARPD
calls you the **PI**). You describe what you want, settle the decisions that are yours, approve a
plan, and the agents build and test the game. The game also records every bid and card played and
saves them as a CSV file you can open in a spreadsheet.

**This is a deliberately simple example.** It walks through one small project from start to finish
so you can see how ARPD works. As you go, think about a question of your own and the tool it would
need; the last section, [Your own project](#your-own-project), gives the same steps at a high level
so you can try one.

## Why a card game?

The game is a toy, but it has the shape of a real research instrument:

- **Exact rules** that the software must implement correctly, and that only you can settle when
  they are unclear.
- **Artificial agents** (the computer players) whose behaviour you specify, so it can be checked.
- **A team task.** Spades is a partnership game: partners commit to a joint goal (the team's bid)
  and must coordinate without talking, under incomplete information. That is a small version of the
  coordination problems studied in organizational research.
- **Behavioural data:** every decision is recorded, with how long you took to make it.

From here the extension to interaction between several people is short: networked play so that
four people play as two teams; human–AI teams in which the computer partner's strategy is the
experimental condition; a chat channel between partners; or new measures in the play log. Each is
another round of the same steps with ARPD: describe it, settle the decisions that are yours,
approve a plan, and have the agents build and test it.

**Before you start:** finish **Start here** in the [README](README.md). You should be in your
`spades-demo` folder with Claude Code running.

**Time:** about 1 hour. **Agent use:** about $7.50 in credits.

## How to use this tutorial

Each step shows:

- **▶ Type:** text to type or paste at Claude Code's prompt.
- **ARPD will ask something like:** what to expect.
- **Reply:** text you can copy and paste.

**ARPD is not scripted.** Its wording, and sometimes its order, differ from run to run. Read what
it actually asks and answer that. The replies here cover the questions that usually come up.

**Lettered choices.** Many questions come as a lettered list, with ARPD's recommendation marked
*(recommended)*. You can reply with just the letter. The steps below say which letter fits this
tutorial.

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
saving or resuming games, no clever AI. A later version could be networked; not now.

Rules: standard four-player partnership Spades.
- 52 cards, 13 each, aces high. The first dealer is random; then the deal passes clockwise.
- Bidding starts left of the dealer and goes clockwise, one round, no passing. Each player bids
  0-13; a bid of 0 is nil. No blind nil. A team's bid is the sum of the partners' bids.
- The player left of the dealer leads first. Players must follow suit if they can; otherwise they
  may play any card. The highest spade wins the trick, or else the highest card of the suit led.
  The winner leads next.
- Spades may not be led until a spade has been played on another suit, unless the leader holds only
  spades.
- A team that makes its bid scores 10 x bid, plus 1 per extra trick (a "bag"); a team that falls
  short scores -10 x bid. Nil scores +100 if that player takes no tricks, -100 if they take any; the
  partner's bid is scored on its own, and a nil bidder's tricks don't count toward it but always count
  as bags, whether or not the team makes its bid. Every 10 bags costs 100 points; extra bags carry
  over.
- The first team to 500 wins. If both reach 500 on the same hand, the higher score wins. If the
  scores are tied, play another hand.

Computer players use exactly these rules, nothing more. They choose only from the cards they may
legally play. Card order for "lowest" and "highest": non-spades by rank (on equal rank, clubs <
diamonds < hearts), then spades by rank. A card "would win" if it beats every card played to the
trick so far. "Above 10" means J, Q, K or A. The bid count adds up its three parts.
- Bid: count 1 per ace, 1 per king with at least one other card of its suit, and 1 per spade beyond
  the third. If the count is 0 and the hand has no spade above 10, bid nil; otherwise bid the count,
  at least 1.
- Lead: the highest card of its longest non-spade suit (on equal length: clubs, then diamonds, then
  hearts); if it may lead only spades, its lowest spade.
- Not leading: if its partner is winning the trick, play its lowest card; otherwise its lowest card
  that would win; if none would win, its lowest card.
- If it bid nil: lead its lowest card; otherwise play its highest card that would not win, or, if
  every card would win, its highest card. Its partner plays normally.

Aim for a first demonstration: as soon as there is a window I can click through, stop and ask me
to try it, before refining or polishing anything.

In the window: my hand as clickable cards, with only legal cards active; the four cards on the
table; each player's bid and tricks; both teams' scores and bags; computer plays shown with a short
pause; buttons to bid 0-13; a summary after each hand; a new-game button at the end.

Play log: record every bid and every card played, and save it as a CSV file in a "data" folder,
one file per game, named by the date and time the game started. Write the finished hands at the
end of each hand, so a game stopped part-way keeps them. One row per bid or card, with these columns:
- game_id: the same for every row of one game
- hand: 1, 2, 3, ...
- trick: 1-13 for cards; blank for bids
- seat: S, W, N or E (I am S, my partner N)
- player: human or computer
- team: NS or EW
- action: bid or play
- value: the bid (0-13), or the card as rank and suit letters, such as QH or 10S
- legal_options: how many legal choices that player had
- think_seconds: for my actions, seconds from when I could act to my click; blank for computers
- trick_winner: on the last card of each trick, the seat that won it; otherwise blank
- timestamp: date and time of the action
The log holds only my own play on this computer, with no names.

Tests: the rules, the scoring, each computer rule, the play log (a hand gives 4 bid rows and 52
card rows, with the columns above), and a game played by four computer players to the end, which
fails if no team has won within 200 hands. No test may open the window or wait for a click:
test the game logic without the window.
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

- It first shows a preview of what moves and asks how to proceed. If the preview only moves ARPD's
  own files, reply `Yes, go ahead.` (or the letter for converting as shown).
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

**Reply, only if the summary matches the brief** (or the letter for *Yes, continue*):

```text
Yes, that's right. Continue.
```

The same applies when it asks whether you are ready to move on to the next phase.

Otherwise, say what is wrong, in plain words.

### 6. Objectives

**If it asks what would convince you that it works:**

```text
I can play a hand in the window, the computer players follow the stated rules, and the play log
opens in a spreadsheet with one row per bid and card. Tests check the rules, the scoring, each
computer rule, the play log, and a full all-computer game to 500.
```

**If it asks what the tool will not do:**

```text
No networking, no saving or resuming games, no smarter computer players, no sound or card images.
```

**If it asks about research questions or theory:**

```text
None for now. This is a demonstration. The play log shows how play-level data could be collected
for later questions about team coordination.
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
rules are your decision, not the agents'. It explains the case with an example and offers options.
Pick the one that matches how you play; if unsure, the letter of the option it recommends. Either
way, it is recorded as your ruling.

> **Look here:** ARPD records your rulings word for word. Later they appear in `DECISIONS.md`.

**If it asks about the play log** (what a column means, where the files go, or privacy):

```text
The columns in my first message define it. The log holds only my own play on this computer, with no
names.
```

If it asks about a detail of a column that the brief does not settle (for example, exactly when the
think time starts), pick the option that matches what you mean. If unsure, use the letter of the
option it recommends.

> **Look here:** ARPD treats what recorded data *means* as your decision, never the agents'. In a
> real study this is where measurement validity is decided. It records each answer as your ruling.

### 8. Design

**If it lists design proposals (screen layout, button labels, a short pause between computer
plays) and asks whether you accept them:** read them; if they fit, reply with the letter for
*accept all*.

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

**If it asks where the later networked version goes** (P1 to P5): the letter for **P5 Idea**.

**If it asks about priorities or a minimum version:**

```text
The whole game is the first priority. Nothing else.
```

**If it proposes a package for how the work runs** (one sprint at a time, review depth, how far the
agents may go on their own) **and asks you to accept it:** read it; if it keeps the game rules as
your decisions, reply with the letter for *accept as proposed*.

**If it asks whether to include ARPD's logging and agent-role files:**

```text
Yes, include them.
```

### 10. ✋ Adopt the Project Definition Report

ARPD drafts `reports/setup/PROJECT-DEFINITION.md`, checks it, summarizes it, and asks how you want
to handle it (accept its proposals and go to adoption, change something, go through them one by
one, or reject).

> **Look here:** open `reports/setup/PROJECT-DEFINITION.md` in any text editor. Check that the game
> rules and the computer players' rules are recorded as yours, and that nothing you did not ask
> for has crept in.

**If it matches what you asked for,** reply with the letter for *accept and go to adoption*.

ARPD then shows an **APPROVAL REQUIRED** block. Read it. It may list a few proposals that are
**accepted only if you name them**, usually readings of what a game term means (for example, which
card "wins"). Those are data decisions, so ARPD will not assume them; unnamed, they stay open and
block the build.

**Reply, only if the report and those proposals match what you asked for.** Use the version number
and the proposal IDs ARPD shows, for example:

```text
I adopt version 1 of the Project Definition Report, with REQ-SCORE-03 and REQ-RULE-01 accepted.
```

If it lists no such proposals, leave out the "with … accepted" part. If something is wrong, say
what; ARPD revises the report and asks again.

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

**Look at the data.** Open the newest CSV file in the `data` folder with a spreadsheet program. Each
row is one bid or card, with your think time on your own rows. Ask yourself what you could study
with it, and what you would add for a real study.

---

## If something goes wrong

| Problem | What to do |
|---|---|
| `claude` is not found | Open a new terminal window. See the README, step 3 |
| The game window does not open | Run the Tkinter check from the README, step 4 |
| A command is blocked by Claude Code's safety check | Paste the one-line `!` command ARPD gives you |
| The session closed or crashed | `claude` in the same folder, then `/arpd-checkin` |
| You hit a usage limit | Wait for it to reset, then `claude` and `/arpd-checkin` |
| Nothing happens for 10 minutes or more during the build | Close any game window that has opened. If still stuck, press Esc and type: `A command seems to be hanging, possibly a test that opened the game window. Stop it and continue.` |
| ARPD asks something you don't understand | Ask it: `What does that mean, and what do you recommend?` |

## What to look at afterwards

- `CLAUDE.md`: the team charter the agents work under.
- `DECISIONS.md`: your rulings, word for word.
- `REQUIREMENTS.md`: each requirement and its evidence.
- `reports/`: the setup record, the approved plan, and the sprint close-out.
- `arpd/docs/GUIDE.md`: the full guide to using ARPD for your own projects.

---

## Your own project

The same steps work for a tool of your own: an experiment platform, a simulation, a survey or
measurement tool, a data pipeline, or an extension of this game. At a high level:

1. **Start from a fresh copy.** Clone ARPD into a new folder named for your project (README,
   Start here, step 5), open Claude Code there, and type `/arpd-setup`.
2. **Describe what you want in your own words:** the question, the tool you think you need, who
   will use it, and what data it handles. A rough idea is fine; setup draws out the rest. Mention
   any existing notes, code or data, and say early if the tool will collect data from people.
3. **Choose ARPD's role.** *A* builds what you specify. *C* also reviews how well the design fits
   your theory or research question. *D* helps you work out what to build and develop the science
   behind it with you.
4. **Work through the phases.** Settle what is yours: the rules of the task, what each recorded
   value means, and what would convince you the tool works. Accept or change ARPD's proposals.
5. **Read and adopt the Project Definition Report.** Nothing is built before this.
6. **Plan a small first piece** with `/arpd-plan`. Approve the exact version, then begin.
7. **Check in and review.** Use `/arpd-checkin` to see where things stand. Read each close-out and
   try the tool yourself. Use `/arpd-amend` to change a ruling or the charter. Plan the next piece
   with `/arpd-plan`.

**Start small.** A first piece you can try within a session teaches you more than a long
specification. For example, turn this game into a small experiment: give the computer partner two
strategies, assign one per game as the condition, and compare the play logs.
