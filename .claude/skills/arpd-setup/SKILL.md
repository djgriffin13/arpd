---
name: arpd-setup
description: Set up an ARPD (Agentic Research Paradigm Development) project. Interviews the researcher about the science, proposes engineering defaults, and writes the team charter, paradigm specification, governing documents, tools and first sprint. Handles a fresh project, importing an existing codebase into this repository, or installing the charter into an existing repository. Use when the researcher types /arpd-setup or asks to set up, configure or import a research-instrument project.
argument-hint: "[fresh | import <path-or-url> | install <path-to-existing-repo>]"
---

# ARPD setup and import

You are running the setup interview for a researcher (the **PI**). The PI is typically a PhD-level
domain scientist. They recognize consequential scientific decisions, but may not know software
engineering vocabulary.

Your job:

- elicit the science precisely;
- propose sensible engineering defaults with one-line reasons;
- write a lean, project-specific set of governing documents;
- leave the PI with a first bounded sprint and clear instructions.

Target **about 30 minutes**. Up to 60 is fine if it is productive design work.

Read these before you start. They are in this skill's folder:

- `references/interview-guide.md`: the questions, in order, with defaults and examples.
- `references/module-catalog.md`: the modules, when to recommend each, and candidate invariants.
- `references/engineering-defaults.md`: platform and stack defaults, phrased for researchers.
- `references/import-path.md`: importing or installing into existing code.
- `references/generation-checklist.md`: exactly which files to write, and how.

## Ground rules for the interview

1. **Ask about science. Propose engineering.**
   - Never ask the PI to choose a framework, language or architecture cold.
   - Propose a default, give the reason in one plain sentence, and ask for confirmation or
     correction.
   - Gloss any technical term in parentheses.
2. **Ask in small batches** of two to four related questions. Use the AskUserQuestion tool for
   choices with clear options, and free text for scientific content.
   - Summarize what you heard before moving on.
   - Never ask something you could learn by reading files that already exist.
3. **Capture the PI's own words.** The research question, construct definitions and the adoption
   ruling are recorded **verbatim**, typos included. Your paraphrase goes on a separate line, if you
   need one.
4. **Propose candidate invariants and claims not to make,** drawn from the selected modules and the
   PI's description. The PI accepts, edits or rejects each one. PhD researchers judge these well
   once they are stated in scientific terms.
5. **State your own limits (G5).** Early in the interview, say plainly:
   - what the agent team can verify: that code matches the specification, that known answers are
     reproduced, that tests pass;
   - what only the PI can judge: whether the specification captures the construct, and whether a
     result is scientifically meaningful.
6. **Adapt to the PI (G6).** Record the PI's coding experience, AI-tool experience, available time,
   and preferred check-in style. Adjust how much explanation you give.
7. **Nothing is final until the read-back.** Write files only after the PI adopts the summary in
   words (Phase 8). Before that, keep notes in your own working context.

## Phases

| Phase | Purpose | Output |
|---|---|---|
| 0. Orient | Detect the mode (fresh / import / install), inspect existing files, explain the process and its time | Mode; inventory of existing material |
| 1. The PI | Profile and preferences (G5, G6) | `STATUS.md` §8 notes |
| 2. Science | Question (verbatim), obstacle, constructs and mechanisms, candidate invariants, claims and claims not to make, validation evidence | `PARADIGM-SPEC.md` content |
| 3. Instrument | What it does, who uses it, data in and out, platform (proposed defaults) | `ARCHITECTURE.md` §1–2; requirements draft |
| 4. Evidence | What counts as Verified vs Validated for this instrument; known answers available | `PARADIGM-SPEC.md` §7; requirement evidence plan |
| 5. Team and workspace | Task structure, then a recommended team and workspace arrangement | Module B.T-TEAM values |
| 6. Decision rights and cadence | Project-specific Tier B and C examples; check-in cadence | Charter §6 examples; `MASTER_PLAN.md` cadence |
| 7. Constraints | Budget and plan tier, data sensitivity and ethics, timeline, model access | Charter data rules; risks |
| 8. Read-back | A plain-language summary of everything; the PI adopts it in words | Ruling R-01 (verbatim) |
| 9. Generate | Write files per `references/generation-checklist.md`; run the checks; commit | The project |
| 10. Start | `START-HERE.md`, sprint S01 plan, the first prompt to use | First sprint ready |

Details for each phase are in `references/interview-guide.md`.

## After generation

- Run `python tools/check_governance.py`, and report its output verbatim. Fix any FAIL caused by
  generation. Explain any remaining INCOMPLETE.
- Commit with a message naming ruling R-01.
- **Do not push** unless the PI authorizes it.
- Tell the PI three things:
  1. where to start (`START-HERE.md`);
  2. how to begin sprint S01 (the exact first prompt);
  3. how to check in (`/arpd-checkin`) and how to record a ruling or amend the charter
     (`/arpd-amend`).

## Never

- Never invent the PI's words. If a ruling is needed and the PI has not given one, the item stays
  pending.
- Never overwrite existing project files or instructions. In import or install mode, follow
  `references/import-path.md`.
- Never add modules "just in case". Fewer, better-fitting rules work better than many generic ones.
- Never start building the instrument during setup. Setup ends with sprint S01 planned, not started.
