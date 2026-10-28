#!/usr/bin/env python3
"""Check a Project Blueprint (reports/setup/PROJECT-BLUEPRINT.md) against its contract, in either layout.

    python arpd/tools/check_report.py <blueprint.md> [--stage draft|adopted]      (from the project root)

Older projects. A project set up before the rename keeps its file as reports/setup/PROJECT-DEFINITION.md
(before v0.6, reports/PROJECT-DEFINITION.md). When the named reports/setup/PROJECT-BLUEPRINT.md does not
exist but reports/setup/PROJECT-DEFINITION.md beside it does, that older file is checked, and the
checker says so.

Each check is reported PASS, FAIL or WARN with what it rests on. HTML comments are ignored.

Layouts. A blueprint is the v0.7 layout (14 sections) if it has a "## 14." heading or its "## 3."
heading mentions constraints (v0.7 section 3 is "Constraints and model commitments"); otherwise it is
the v0.5 layout (13 sections). The layout is reported first and sets the section numbers below:

            sections  decision table  open items  what adoption authorizes
    v0.5    1-13      section 6       section 12  section 13
    v0.7    1-14      section 8       section 13  section 14

The checks, with the v0.5 section numbers (v0.7 messages use the v0.7 numbers):

  (a) header (the text before the first "## " heading): a "Version" line with vN and a "Status"
      line. --stage draft (the default): the Status says Draft, a DRAFT banner is present, and
      nothing in the header says "Adopted by R-NN" (elsewhere, "adopted by R-NN" cites an existing
      ledger entry, such as an import's inherited decisions). --stage adopted: the Status says
      "Adopted by R-NN (vN)", with the same vN as the Version line;
  (b) sections 1-13 present by number ("## 1." ... "## 13."), each with content or
      "Not applicable: <reason>"; no unfilled {{placeholder}};
  (c) every requirement ("#### REQ-<AREA>-NN: <name>") has "Acceptance criteria" with at least one
      bullet, a Priority (required / desired / future, or "open (O-NN)" when the PI left the scope
      open), a Source, and one Status from: Adopted,
      Adopted on adoption, Adopted (inherited, R-NN), Proposed, Provisional, Delegated (SA-NN ...),
      Open (<gate>), Excluded (a status written per part FAILs: split the requirement or use one
      status). Duplicate IDs FAIL, as does a requirement heading at another level;
  (d) a draft cannot adopt: a requirement with Status "Adopted" FAILs in a draft (except
      "Adopted (inherited, R-NN)", already adopted by that ruling), and "Adopted on adoption" FAILs
      when its Source is the lead's derivation: lead wording (lead, derived, recommendation) with
      no PI words in quotes (double, single or typographic), ruling or spec item, or with lead
      wording before them (the PI's words only cited), unless the Source says "PI accepted: '...'";
  (e) section 6 holds a decision table: Decision | Alternatives considered | Recommendation |
      Rationale | Status | Consequences. Each row's alternatives are non-empty, or say
      "none credible: <reason>"; a row whose Status is Open names a gate;
  (f) section 12: every open item names a gate: "before" plus a word naming a stage (before
      planning, before implementing <what>, before any release, before deployment, ...; the same
      rule as Open (<gate>) in (c) and (e)). An item is closed only by a leading "Resolved:",
      "Closed:" or "Excluded:", or, in a table, a Status cell of Adopted, Delegated, Resolved, Closed
      or Excluded, or a Gate cell of Resolved, Closed or Excluded; the words elsewhere in an item do
      not close it. An open item gated before planning WARNs unless it says "deferred by the PI"
      (setup asks such items before showing the blueprint);
  (g) section 13 says that adoption does not authorize implementation (a sentence with not / no /
      never and "implement");
  (h) a "Completeness check" subsection is present (WARN if absent).

v0.7 only (a v0.5 blueprint is checked exactly as above):
  (c) Priority is P1 Core (in the minimum usable version), P2 Next, P3 Planned, P4 Wanted or P5 Idea:
      "P1" to "P5", optionally followed by the level name in any form (P1 Core, P1 (Core), P2: Next;
      a name contradicting its number WARNs), or "open (O-NN)". The v0.5 values FAIL with the mapping
      (required -> P1 Core; desired -> P2 Next or P3 Planned; future -> P4 Wanted or P5 Idea).
      Feasibility, a status separate from priority, is optional: "established", or
      "to investigate: <what> (<gate>)" (no gate WARNs; anything else FAILs). Correctness-critical is
      optional: "yes: <why>" (yes without a reason WARNs) or "no" (anything else FAILs);
  (i) priorities respect dependencies: a requirement whose Dependencies name a requirement of this
      blueprint with a lower priority (a higher P number) FAILs, since it cannot be scheduled before what
      it depends on (open priorities are skipped); a dependency ID not in the blueprint WARNs;
  (j) a correctness-critical requirement at P4 or P5 WARNs: such requirements are rarely optional.
  (k) section 3 (v0.7): a row classed Must hold (an invariant) whose epistemic-status cell says it is a
      hypothesis FAILs (circularity), unless the row says it was "kept by the PI" after the review.
  An item gated "before planning" in (f) means before any plan of the work it affects; "before
  planning <a later milestone, sprint or release>" names that later stage and is not asked first.

Exit code 0 if no check FAILs (WARN does not fail), 1 otherwise, 2 for a usage or read error.
It checks structure and authority only: not whether the requirements are right, the blueprint is
complete, or the prose is good. It rewards no length and, beyond (g), no particular wording.
Standard library only; Python 3.8+.
"""
import argparse
import os
import re
import sys

# The section numbers each layout uses (see the module docstring).
LAYOUTS = {"v0.5": {"sections": 13, "decisions": 6, "open": 12, "authorizes": 13},
           "v0.7": {"sections": 14, "decisions": 8, "open": 13, "authorizes": 14}}
DECISION_COLUMNS = ("Decision", "Alternatives considered", "Recommendation", "Rationale", "Status",
                    "Consequences")
FIELDS = (r"Description|Behaviou?r|Inputs?\s*(?:/|and)\s*outputs?|Constraints|Acceptance criteria|Priority"
          r"|Dependencies|Source|Status|Notes?|Target|Rationale|Feasibility|Correctness[\s-]*critical")
FIELD = re.compile(r"^ ?(?:[-*]\s+)?\**\s*(" + FIELDS + r")\s*\**\s*:\s*\**\s*(.*)$", re.I)
BULLET = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+\S")
REQ_HEAD = re.compile(r"^(#{1,6})\s+\**(REQ-[A-Z0-9]+-\d+)\b\**\s*:?\s*(.*)$")
SECTION_HEAD = re.compile(r"^##\s+\**(\d+)\.")
# A gate is "before" plus at least one word naming a stage (before planning, before implementing X, before any
# release, before the roadmap beyond M1, ...). The blueprint chooses the stage's wording; a determiner alone is not one.
DETERMINER = r"(?:the|a|an|any|each|every|all|some|its|this|that)\b"
GATE = re.compile(r"\bbefore\s+(?:%s\s*)*(?!%s)[A-Za-z0-9][\w-]*" % (DETERMINER, DETERMINER), re.I)
GATE_HINT = "before <stage>: before planning, before implementing <what>, before deployment, ..."
# The stages a gate is expected to name; any other wording is flagged (WARN), not failed.
STAGE = re.compile(r"\bbefore\s+(?:%s\s*)*(?:planning|plan\b|implement\w*|build\w*|cod\w+|develop\w*|deploy\w*|"
                   r"release\w*|launch\w*|go-live|data collection|collect\w*|pilot\w*|use\b|adoption|"
                   r"(?:the\s+)?(?:first\s+|next\s+)?(?:sprint|milestone|roadmap)|S\d+|M\d+|v\d)" % DETERMINER, re.I)
PRIORITIES = ("required", "desired", "future")
# v0.7: P1 Core ... P5 Idea; the level name is optional and may be written in any form.
P_LEVELS = {1: "Core", 2: "Next", 3: "Planned", 4: "Wanted", 5: "Idea"}
P_PRIORITY = re.compile(r"p([1-5])(?!\d)\W*([a-z]*)", re.I)
OLD_PRIORITY_HINT = "required -> P1 Core; desired -> P2 Next or P3 Planned; future -> P4 Wanted or P5 Idea"
REQ_ID = re.compile(r"\bREQ-[A-Z0-9]+-\d+\b")
# A priority the PI left open names the open decision that will set it: "open (O-NN)".
OPEN_PRIORITY = re.compile(r"open\s*\(\s*O-\d+\b", re.I)
# A quotation: double, single or typographic quotes. A single quote opens only where no letter precedes it
# and closes only where none follows, so the apostrophes in "lead's ... PI's" are not a quotation.
QUOTE = (r"(?:\"[^\"\n]+\"|“[^”\n]+”|(?<![A-Za-z])'[^'\n]+'(?![A-Za-z])"
         r"|(?<![A-Za-z])‘[^’\n]+’(?![A-Za-z]))")
PI_SOURCE = re.compile(QUOTE + r"|\b(?:R|CON|OP|INV|CLM|VAL|ASM)-\d+\b")
PI_ACCEPTED = re.compile(r"\bPI\s+accepted\b\W{0,3}" + QUOTE, re.I)
LEAD_ONLY = re.compile(r"\b(?:lead|derived|derivation|recommend\w*|inferred)\b", re.I)
INHERITED = re.compile(r"adopted\s*\(\s*inherited\b", re.I)
INHERITED_OK = re.compile(r"adopted\s*\(\s*inherited\s*[,;:]?\s*R-\d+\s*\)", re.I)
# Section 12: an open item gated "before planning" is asked before the blueprint is shown, unless the PI deferred it.
BEFORE_PLANNING = re.compile(r"\bbefore\s+(?:%s\s*)*(?:planning|plan)\b(?!\s+(?:(?:of|for)\s+)?(?:%s\s*)*"
                             r"(?:(?:next|later|following|second|third)\s+)?(?:milestone|M\d|S\d|sprint|release|v\d|phase))"
                             % (DETERMINER, DETERMINER), re.I)
PI_DEFERRED = re.compile(r"\bdeferred\s+by\s+the\s+PI\b", re.I)
# Section 12: an item is closed only by a leading marker, or (in a table) by a Status or Gate cell saying so.
CLOSED_MARK = re.compile(r"^\W*(?:resolved|closed|excluded)\W*:", re.I)
CLOSED_STATUS = re.compile(r"^(?:adopted|delegated|resolved|closed|excluded)\b", re.I)
CLOSED_GATE = re.compile(r"^(?:resolved|closed|excluded)\b", re.I)


def read_text(path):
    data = open(path, "rb").read()
    if data.startswith(b"\xef\xbb\xbf"):
        data = data[3:]
    if data[:2] in (b"\xff\xfe", b"\xfe\xff"):
        return data.decode("utf-16", "replace")
    return data.decode("utf-8", "replace")


def short(text, n=100):
    text = " ".join(text.split())
    return text if len(text) <= n else text[:n - 3] + "..."


def plain(value):
    """A field value without Markdown emphasis or backticks."""
    return re.sub(r"[*`_]", "", value).strip()


def split_row(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    return [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", s)]


def tables(lines):
    """[(header cells, [row cells or None for a malformed row], [raw rows])] for each table."""
    out, i = [], 0
    while i < len(lines):
        if lines[i].strip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|?[\s:|-]+\|[\s:|-]*$", lines[i + 1]) \
                and "-" in lines[i + 1]:
            header = split_row(lines[i])
            rows, raw = [], []
            j = i + 2
            while j < len(lines) and lines[j].strip().startswith("|"):
                cells = split_row(lines[j])
                rows.append(cells if len(cells) == len(header) else None)
                raw.append(lines[j].strip())
                j += 1
            out.append((header, rows, raw))
            i = j
        else:
            i += 1
    return out


def sections(lines):
    """{number: (heading line, [body lines])} for "## N." headings; also the duplicate numbers."""
    found, dupes, current = {}, [], None
    for line in lines:
        if line.startswith("## ") or line.startswith("##\t"):
            m = SECTION_HEAD.match(line)
            current = None
            if m:
                n = int(m.group(1))
                if n in found:
                    dupes.append(n)
                else:
                    found[n] = (line, [])
                    current = n
            continue
        if line.startswith("# ") and current is not None:
            current = None
            continue
        if current is not None:
            found[current][1].append(line)
    return found, dupes


def not_applicable(body):
    text = "\n".join(body).strip()
    m = re.match(r"^\**\s*Not applicable\s*\**\s*:\s*\**\s*(.*)", text, re.I | re.S)
    return (True, bool(m.group(1).strip())) if m else (False, False)


def layout_of(text):
    """'v0.7' if the blueprint has a "## 14." heading or its "## 3." heading mentions constraints, else 'v0.5'."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    for line in text.split("\n"):
        line = line.rstrip("\r")
        m = SECTION_HEAD.match(line)
        if m and (m.group(1) == "14" or (m.group(1) == "3" and re.search(r"constraint", line, re.I))):
            return "v0.7"
    return "v0.5"


def priority_level(value):
    """The P number (1-5) of a v0.7 Priority value, or None (open, missing or not a P value)."""
    m = P_PRIORITY.match(plain(value))
    return int(m.group(1)) if m else None


def requirements(lines):
    """[(id, heading level, line number, {field: value}, acceptance bullets, {field: full text})] for each
    REQ heading; the full text adds a field's continuation lines (a Dependencies list, for example)."""
    reqs = []
    for i, line in enumerate(lines):
        m = REQ_HEAD.match(line)
        if not m:
            continue
        body = []
        for nxt in lines[i + 1:]:
            if re.match(r"^#{1,6}\s", nxt):
                break
            body.append(nxt)
        fields, texts, bullets, current = {}, {}, 0, None
        for b in body:
            f = FIELD.match(b)
            if f:
                current = re.sub(r"\s+", " ", f.group(1).lower())
                current = re.sub(r"^correctness[\s-]*critical$", "correctness-critical", current)
                fields.setdefault(current, f.group(2).strip())
                texts.setdefault(current, []).append(f.group(2))
                if current == "acceptance criteria" and BULLET.match(f.group(2) or ""):
                    bullets += 1
            else:
                if current is not None:
                    texts[current].append(b)
                if current == "acceptance criteria" and BULLET.match(b):
                    bullets += 1
        reqs.append((m.group(2), len(m.group(1)), i, fields, bullets,
                     {k: "\n".join(v) for k, v in texts.items()}))
    return reqs


def lead_derived(source):
    """True if a Source is the lead's derivation rather than the PI's words.

    It is the lead's when lead wording (lead, derived, recommendation, ...) comes before any PI quotation
    or cited item, or there is none, unless the Source records the PI accepting it ("PI accepted: '...'").
    """
    s = plain(source)
    if PI_ACCEPTED.search(s):
        return False
    lead, pi = LEAD_ONLY.search(s), PI_SOURCE.search(s)
    return bool(lead) and (not pi or lead.start() < pi.start())


def status_problem(status, stage, source):
    """None if a requirement Status is acceptable, else the reason."""
    s = plain(status)
    low = s.lower()
    if not s:
        return "no Status"
    if re.match(r"adopted[\s-]+on[\s-]+adoption\b", low):
        if stage == "draft" and lead_derived(source):
            return ("Status '%s' but the Source is the lead's derivation (no PI words, or they are only cited): "
                    "a draft cannot adopt it; mark it Proposed or Provisional, or record the PI's acceptance "
                    "(PI accepted: '...')" % short(s, 40))
        return None
    if INHERITED.match(s):
        if not INHERITED_OK.match(s):
            return ("Status '%s': %san inherited requirement names the ruling that adopted it: "
                    "Adopted (inherited, R-NN)" % (short(s, 40), "a draft cannot adopt; " if stage == "draft" else ""))
        return None
    if re.match(r"adopted\b", low):
        if stage == "draft":
            return ("Status '%s': a draft cannot adopt (use Proposed; Adopted on adoption for PI words; or "
                    "Adopted (inherited, R-NN) for a requirement already adopted)" % short(s, 40))
        return None
    if re.match(r"(proposed|provisional|excluded)\b", low):
        return None
    if re.match(r"delegated\b", low):
        return None if re.match(r"delegated\s*\(\s*SA-\d+", s, re.I) else "Delegated must name its SA: Delegated (SA-NN ...)"
    if re.match(r"open\b", low):
        return None if GATE.search(s) else "Open must name its gate: Open (%s)" % GATE_HINT
    return ("Status '%s' is not one of Adopted, Proposed, Provisional, Delegated (SA-NN), Open (gate), Excluded; "
            "a requirement has one status: if its parts differ, split the requirement or use one status"
            % short(s, 40))


def check(text, stage="draft"):
    """[(status, check, evidence)] for one blueprint's text."""
    text = re.sub(r"<!--.*?-->", "", text.replace("﻿", ""), flags=re.S)
    lines = [l.rstrip("\r") for l in text.split("\n")]
    layout = layout_of(text)
    lay = LAYOUTS[layout]
    v07 = layout == "v0.7"
    numbers = range(1, lay["sections"] + 1)
    out = [("PASS", "layout", "%s (%d sections)" % (layout, lay["sections"]))]

    # (a) header
    first = next((i for i, l in enumerate(lines) if l.startswith("## ")), len(lines))
    header = lines[:first]
    vline = next((l for l in header if re.match(r"^\s*(?:[-*]\s+)?\**\s*Version\s*\**\s*:?", l)), None)
    vm = re.search(r"\bv(\d+)\b", vline or "")
    sline = next((l for l in header if re.match(r"^\s*(?:[-*]\s+)?\**\s*Status\s*\**\s*:", l)), None)
    name = "(a) header: version, status, banner"
    problems = []
    if not vm:
        problems.append("no 'Version' line with vN in the header" if not vline else "Version line has no vN: " + short(vline))
    if not sline:
        problems.append("no 'Status' line in the header")
    banner = [l for l in header if re.search(r"\bDRAFT\b", l) and l is not sline]
    # Only the header can claim the blueprint's own adoption; elsewhere "adopted by R-NN" cites an existing
    # ledger entry (an import listing the starter's decisions, for example).
    adopted_claims = [l for l in header if re.search(r"adopted\s+by\s+R-\d+", l, re.I)]
    if stage == "draft":
        if sline and not re.search(r"\bdraft\b", sline, re.I):
            problems.append("a draft's Status must say Draft vN: " + short(sline))
        if not banner:
            problems.append("no DRAFT banner in the header")
        for l in adopted_claims:
            problems.append("a draft says 'Adopted by R-': " + short(l))
        if sline and vm:
            sv = re.search(r"\bv(\d+)\b", sline)
            if sv and sv.group(1) != vm.group(1):
                problems.append("Status version v%s differs from Version v%s" % (sv.group(1), vm.group(1)))
    else:
        am = re.search(r"adopted\s+by\s+(R-\d+)\s*\(\s*v(\d+)\s*\)", sline or "", re.I)
        if sline and not am:
            problems.append("an adopted blueprint's Status must say 'Adopted by R-NN (vN)': " + short(sline))
        elif am and vm and am.group(2) != vm.group(1):
            problems.append("Status adopts v%s but the Version line is v%s" % (am.group(2), vm.group(1)))
        if banner:
            out.append(("WARN", name, "an adopted blueprint still carries a DRAFT banner: " + short(banner[0])))
    out += [("FAIL", name, p) for p in problems] or [("PASS", name, short(sline or ""))]

    # (b) sections
    found, dupes = sections(lines)
    name = "(b) sections 1-%d present, each with content or 'Not applicable: <reason>'" % lay["sections"]
    problems = ["section %d missing (expected a heading '## %d. ...')" % (n, n) for n in numbers if n not in found]
    problems += ["section %d appears more than once" % n for n in dupes]
    for n in numbers:
        if n not in found:
            continue
        heading, body = found[n]
        na, reason = not_applicable(body)
        if na and not reason:
            problems.append("section %d says 'Not applicable' without a reason" % n)
        elif not na and not any(l.strip() for l in body):
            problems.append("section %d is empty: write it, or 'Not applicable: <reason>'" % n)
    order = [n for n in found if n in numbers]
    if order != sorted(order):
        out.append(("WARN", name, "sections out of order: " + ", ".join(map(str, order))))
    placeholders = sorted(set(re.findall(r"\{\{[^{}]*\}\}", text)))
    problems += ["unfilled placeholder " + short(p, 60) for p in placeholders]
    out += [("FAIL", name, p) for p in problems] or [("PASS", name, "%d sections" % len(found))]

    def body_of(n):
        return found[n][1] if n in found else []

    def is_na(n):
        return not_applicable(body_of(n))[0]

    # (c) and (d) requirements
    reqs = requirements(lines)
    name_c = "(c) requirements: acceptance criteria, priority, source, status"
    name_d = "(d) a draft cannot adopt"
    problems, adopt_problems, seen, warns = [], [], {}, []
    if not reqs:
        problems.append("no requirement headings '#### REQ-<AREA>-NN: <name>'")
    for rid, level, at, fields, bullets, _texts in reqs:
        if level != 4:
            problems.append("%s: heading level %d; requirements are '#### REQ-<AREA>-NN: <name>'" % (rid, level))
        if rid in seen:
            problems.append("%s: duplicate requirement ID (also at line %d)" % (rid, seen[rid] + 1))
        seen.setdefault(rid, at)
        if "acceptance criteria" not in fields:
            problems.append("%s: no 'Acceptance criteria' field" % rid)
        elif bullets < 1:
            problems.append("%s: 'Acceptance criteria' has no bullet" % rid)
        prio = plain(fields.get("priority", "")).lower()
        if not prio:
            problems.append("%s: no Priority" % rid)
        elif v07:
            problems += v07_priority_problems(rid, prio, warns)
        elif not re.match(r"(%s)\b" % "|".join(PRIORITIES), prio) and not OPEN_PRIORITY.match(prio):
            problems.append("%s: Priority '%s' is not required / desired / future, or open (O-NN) when the PI "
                            "left the scope open" % (rid, short(prio, 30)))
        if v07:
            problems += v07_field_problems(rid, fields, warns)
        source = fields.get("source", "")
        if not plain(source):
            problems.append("%s: no Source" % rid)
        if "status" not in fields:
            problems.append("%s: no Status" % rid)
        else:
            why = status_problem(fields["status"], stage, source)
            if why and "draft cannot adopt" in why:
                adopt_problems.append("%s: %s" % (rid, why))
            elif why:
                problems.append("%s: %s" % (rid, why))
    out += [("FAIL", name_c, p) for p in problems] or [("PASS", name_c, "%d requirement(s)" % len(reqs))]
    out += [("WARN", name_c, w) for w in warns]
    out += [("FAIL", name_d, p) for p in adopt_problems] or [("PASS", name_d, "no requirement adopted by a draft"
                                                               if stage == "draft" else "stage adopted")]

    # (e) the decision table (v0.5 section 6, v0.7 section 8)
    sd = lay["decisions"]
    name = "(e) section %d: decision table with alternatives" % sd
    problems = []
    if sd in found and is_na(sd):
        out.append(("WARN", name, "section %d says Not applicable: no architecture decisions recorded" % sd))
    elif sd in found:
        want = [c.lower() for c in DECISION_COLUMNS]
        candidates = tables(body_of(sd))
        table = next((t for t in candidates if all(any(h.lower().startswith(w) for h in t[0]) for w in want)), None)
        if not table:
            problems.append("no table with the columns " + " | ".join(DECISION_COLUMNS))
        else:
            header, rows, raw = table
            col = {w: next(i for i, h in enumerate(header) if h.lower().startswith(w)) for w in want}
            if not rows:
                problems.append("the decision table has no rows")
            for cells, line in zip(rows, raw):
                if cells is None:
                    problems.append("malformed row (cell count does not match the header): " + short(line, 80))
                    continue
                dec = short(plain(cells[col["decision"]]), 40) or "(unnamed decision)"
                alt = plain(cells[col["alternatives considered"]])
                if re.match(r"none\b", alt, re.I):
                    if not re.match(r"none credible\s*:\s*\S", alt, re.I):
                        problems.append("%s: alternatives 'none' without 'none credible: <reason>'" % dec)
                elif not re.sub(r"[-—–\s]|n/?a", "", alt, flags=re.I):
                    problems.append("%s: no alternatives considered (or 'none credible: <reason>')" % dec)
                st = plain(cells[col["status"]])
                if re.match(r"open\b", st, re.I) and not GATE.search(st):
                    problems.append("%s: Status Open without a gate" % dec)
            if not problems:
                out.append(("PASS", name, "%d decision row(s)" % len(rows)))
    else:
        problems.append("section %d missing" % sd)
    out += [("FAIL", name, p) for p in problems]

    # (f) open items name a gate (v0.5 section 12, v0.7 section 13)
    so = lay["open"]
    name = "(f) section %d: every open item names a gate" % so
    problems, items, planning = [], 0, 0
    if so in found and not is_na(so):
        body = body_of(so)
        table_lines = set()
        for header, rows, raw in tables(body):
            gate_col = next((i for i, h in enumerate(header) if re.search(r"gate|needed by", h, re.I)), None)
            status_col = next((i for i, h in enumerate(header) if re.match(r"status\b", plain(h), re.I)), None)
            for cells, line in zip(rows, raw):
                table_lines.add(line)
                if cells is None:
                    problems.append("malformed row: " + short(line, 80))
                    continue
                if CLOSED_MARK.match(plain(cells[0])) or (
                        status_col is not None and CLOSED_STATUS.match(plain(cells[status_col]))) or (
                        gate_col is not None and CLOSED_GATE.match(plain(cells[gate_col]))):
                    continue
                items += 1
                where = cells[gate_col] if gate_col is not None else line
                if not GATE.search(where):
                    problems.append("open item without a gate: " + short(line, 80))
                planning += bool(BEFORE_PLANNING.search(where) and not PI_DEFERRED.search(line))
        for line in body:
            if line.strip() in table_lines or not re.match(r"^(?:[-*+]|\d+[.)])\s+\S", line):
                continue  # only top-level bullets are items
            if CLOSED_MARK.match(plain(re.sub(r"^(?:[-*+]|\d+[.)])\s+", "", line))):
                continue
            if re.match(r"^[-*+]\s+none\b", line, re.I):
                continue
            items += 1
            if not GATE.search(line):
                problems.append("open item without a gate (%s): %s" % (GATE_HINT, short(line, 80)))
            planning += bool(BEFORE_PLANNING.search(line) and not PI_DEFERRED.search(line))
    out += [("FAIL", name, p) for p in problems] or [("PASS", name, "%d open item(s)" % items)]
    if planning:
        out.append(("WARN", "(f) items gated before planning were asked",
                    "%d open item(s) gated before planning: ask them before presenting, or record the PI's "
                    "deferral (\"deferred by the PI\")" % planning))
    odd = sorted({m.group(0) for line in lines for m in GATE.finditer(line) if not STAGE.match(line[m.start():])})
    if odd:
        out.append(("WARN", "(f) gates name a project stage",
                    "gate wording does not name a project stage (planning, implementing <what>, deployment, a "
                    "sprint, milestone or release): " + ", ".join(short(g, 40) for g in odd)))

    # (g) what adoption authorizes (v0.5 section 13, v0.7 section 14): not implementation
    sa = lay["authorizes"]
    name = "(g) section %d: adoption does not authorize implementation" % sa
    sentences = re.split(r"(?<=[.;:!?])\s+", " ".join(body_of(sa)))
    hit = next((x for x in sentences if re.search(r"\b(?:not|no|never)\b", x, re.I) and re.search(r"implement", x, re.I)), None)
    out.append(("PASS", name, short(hit)) if hit else
               ("FAIL", name, "section %d does not say that adoption does not authorize implementation" % sa))

    # (k) v0.7 section 3: a hypothesis is never a Must hold (circularity)
    if lay["sections"] == 14 and 3 in found and not is_na(3):
        name = "(k) section 3: no hypothesis held as an invariant"
        problems = []
        for header, rows, raw in tables(body_of(3)):
            ccol = next((i for i, h in enumerate(header) if re.match(r"class\b", plain(h), re.I)), None)
            if ccol is None:
                continue
            for cells, line in zip(rows, raw):
                if cells is None:
                    continue
                cls = plain(cells[ccol])
                scol = next((i for i, h in enumerate(header) if re.search(r"epistemic", plain(h), re.I)), None)
                status = plain(cells[scol]) if scol is not None else \
                    " ".join(plain(c) for i, c in enumerate(cells) if i != ccol)  # no epistemic column: the row
                status = re.sub(r"\b(?:not|no|never)\s+(?:an?\s+)?hypothes\w*", "", status, flags=re.I)  # "a rule, not a hypothesis"
                kept = re.search(r"kept\s+by\s+the\s+PI", " ".join(plain(c) for c in cells), re.I)
                if re.search(r"must\s+hold|invariant", cls, re.I) and re.search(r"\bhypothes[ie]s", status, re.I) \
                        and not kept:
                    problems.append("a row classed %s is a hypothesis: a hypothesis the project studies is an "
                                    "open question or an outcome, never an invariant (circularity): %s"
                                    % (short(cls, 20), short(line, 80)))
        out += [("FAIL", name, p) for p in problems] or [("PASS", name, "no Must hold row is a hypothesis")]

    # (h) completeness check
    name = "(h) completeness check subsection"
    cc = next((l for l in lines if re.match(r"^#{2,4}\s+.*completeness check", l, re.I)), None)
    out.append(("PASS", name, short(cc)) if cc else ("WARN", name, "no 'Completeness check' subsection"))
    if v07:
        out += dependency_checks(reqs)
    return out


def v07_priority_problems(rid, prio, warns):
    """(c) v0.7: P1-P5 with an optional level name, or open (O-NN). Problems returned; warnings appended."""
    m = P_PRIORITY.match(prio)
    if m:
        n, word = int(m.group(1)), m.group(2).lower()
        names = {v.lower(): k for k, v in P_LEVELS.items()}
        if word in names and names[word] != n:
            warns.append("%s: Priority '%s': P%d is %s and %s is P%d; say which the PI chose"
                         % (rid, short(prio, 30), n, P_LEVELS[n], P_LEVELS[names[word]], names[word]))
        return []
    if OPEN_PRIORITY.match(prio):
        return []
    if re.match(r"(%s)\b" % "|".join(PRIORITIES), prio):
        return ["%s: Priority '%s' is the v0.5 scale; a v0.7 blueprint uses P1 Core, P2 Next, P3 Planned, P4 Wanted, "
                "P5 Idea (%s)" % (rid, short(prio, 30), OLD_PRIORITY_HINT)]
    return ["%s: Priority '%s' is not P1 Core / P2 Next / P3 Planned / P4 Wanted / P5 Idea, or open (O-NN) when the "
            "PI left it open" % (rid, short(prio, 30))]


def v07_field_problems(rid, fields, warns):
    """(c) v0.7: the optional Feasibility and Correctness-critical fields. Problems returned; warnings appended."""
    problems = []
    if "feasibility" in fields:
        feas = plain(fields["feasibility"])
        inv = re.match(r"to\s+investigate\b\W*(.*)", feas, re.I)
        if re.match(r"established\b", feas, re.I):
            pass
        elif inv and re.search(r"[A-Za-z0-9]", inv.group(1)):
            if not GATE.search(inv.group(1)):
                warns.append("%s: Feasibility 'to investigate' names no gate: to investigate: <what> (%s)"
                             % (rid, GATE_HINT))
        else:
            problems.append("%s: Feasibility '%s' is not 'established' or 'to investigate: <what> (<gate>)'"
                            % (rid, short(feas, 40)))
    if "correctness-critical" in fields:
        cc = plain(fields["correctness-critical"])
        m = re.match(r"(yes|no)\b(.*)", cc, re.I)
        if not m:
            problems.append("%s: Correctness-critical '%s' is not 'yes: <why>' or 'no'" % (rid, short(cc, 40)))
        elif m.group(1).lower() == "yes" and not re.search(r"[A-Za-z0-9]", m.group(2)):
            warns.append("%s: Correctness-critical 'yes' without a reason: yes: <why it is critical>" % rid)
    return problems


def dependency_checks(reqs):
    """v0.7 (i) priorities respect dependencies; (j) correctness-critical requirements are not left optional."""
    out, levels = [], {}
    for rid, _level, _at, fields, _bullets, _texts in reqs:
        levels.setdefault(rid, priority_level(fields.get("priority", "")))
    name = "(i) priorities respect dependencies"
    problems, warns, links = [], [], 0
    for rid, _level, _at, _fields, _bullets, texts in reqs:
        deps = []
        for d in REQ_ID.findall(texts.get("dependencies", "")):
            if d != rid and d not in deps:
                deps.append(d)
        for dep in deps:
            if dep not in levels:
                warns.append("%s depends on %s, which is not in this blueprint (a requirement defined elsewhere? "
                             "check the ID)" % (rid, dep))
                continue
            links += 1
            a, b = levels[rid], levels[dep]
            if a is not None and b is not None and b > a:
                problems.append("%s (P%d) depends on %s (P%d): a requirement cannot be scheduled before what it "
                                "depends on; raise %s or lower %s" % (rid, a, dep, b, dep, rid))
    out += [("FAIL", name, p) for p in problems] or [("PASS", name, "%d dependency link(s) within the blueprint" % links)]
    out += [("WARN", name, w) for w in warns]
    name = "(j) correctness-critical requirements"
    critical, warns = 0, []
    for rid, _level, _at, fields, _bullets, _texts in reqs:
        if not re.match(r"yes\b", plain(fields.get("correctness-critical", "")), re.I):
            continue
        critical += 1
        n = levels.get(rid)
        if n is not None and n >= 4:
            warns.append("%s is correctness-critical at P%d %s: correctness-critical requirements are rarely "
                         "optional; confirm the PI chose this" % (rid, n, P_LEVELS[n]))
    out += [("WARN", name, w) for w in warns] or [
        ("PASS", name, "%d correctness-critical requirement(s), none at P4 or P5" % critical)]
    return out


# The blueprint's file name, and the name it had in projects set up before the rename.
BLUEPRINT_NAME, OLDER_NAME = "PROJECT-BLUEPRINT.md", "PROJECT-DEFINITION.md"


def older_name(path):
    """path, or, when it names a PROJECT-BLUEPRINT.md that does not exist, the older PROJECT-DEFINITION.md
    beside it if that exists (a project set up before the rename)."""
    if os.path.basename(path) != BLUEPRINT_NAME or os.path.exists(path):
        return path
    older = os.path.join(os.path.dirname(path), OLDER_NAME)
    return older if os.path.isfile(older) else path


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("file")
    ap.add_argument("--stage", choices=("draft", "adopted"), default="draft")
    args = ap.parse_args(argv)
    try:
        sys.stdout.reconfigure(errors="replace")
    except AttributeError:
        pass
    path = older_name(args.file)
    if path != args.file:
        print("%s does not exist; checking the older blueprint file %s (a project set up before the "
              "rename)\n" % (args.file, path))
    try:
        text = read_text(path)
    except OSError as exc:
        print("cannot read %s: %s" % (path, exc))
        return 2
    results = check(text, args.stage)
    for status, name, evidence in results:
        print("%-4s  %s\n      %s" % (status, name, evidence))
    failed = any(s == "FAIL" for s, _, _ in results)
    print("\nRESULT: " + ("FAIL" if failed else "PASS"))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
