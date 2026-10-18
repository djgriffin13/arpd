#!/usr/bin/env python3
"""Check a Project Definition Report (reports/setup/PROJECT-DEFINITION.md; in projects set up before
v0.6, reports/PROJECT-DEFINITION.md) against the v0.5 contract.

    python arpd/tools/check_report.py <report.md> [--stage draft|adopted]      (from the project root)

Each check is reported PASS, FAIL or WARN with what it rests on. HTML comments are ignored.

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
      not close it;
  (g) section 13 says that adoption does not authorize implementation (a sentence with not / no /
      never and "implement");
  (h) a "Completeness check" subsection is present (WARN if absent).

Exit code 0 if no check FAILs (WARN does not fail), 1 otherwise, 2 for a usage or read error.
It checks structure and authority only: not whether the requirements are right, the report is
complete, or the prose is good. It rewards no length and, beyond (g), no particular wording.
Standard library only; Python 3.8+.
"""
import argparse
import re
import sys

SECTIONS = range(1, 14)
DECISION_COLUMNS = ("Decision", "Alternatives considered", "Recommendation", "Rationale", "Status",
                    "Consequences")
FIELDS = (r"Description|Behaviou?r|Inputs?\s*(?:/|and)\s*outputs?|Constraints|Acceptance criteria|Priority"
          r"|Dependencies|Source|Status|Notes?|Target|Rationale")
FIELD = re.compile(r"^ ?(?:[-*]\s+)?\**\s*(" + FIELDS + r")\s*\**\s*:\s*\**\s*(.*)$", re.I)
BULLET = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+\S")
REQ_HEAD = re.compile(r"^(#{1,6})\s+\**(REQ-[A-Z0-9]+-\d+)\b\**\s*:?\s*(.*)$")
SECTION_HEAD = re.compile(r"^##\s+\**(\d+)\.")
# A gate is "before" plus at least one word naming a stage (before planning, before implementing X, before any
# release, before the roadmap beyond M1, ...). The report chooses the stage's wording; a determiner alone is not one.
DETERMINER = r"(?:the|a|an|any|each|every|all|some|its|this|that)\b"
GATE = re.compile(r"\bbefore\s+(?:%s\s*)*(?!%s)[A-Za-z0-9][\w-]*" % (DETERMINER, DETERMINER), re.I)
GATE_HINT = "before <stage>: before planning, before implementing <what>, before deployment, ..."
# The stages a gate is expected to name; any other wording is flagged (WARN), not failed.
STAGE = re.compile(r"\bbefore\s+(?:%s\s*)*(?:planning|plan\b|implement\w*|build\w*|cod\w+|develop\w*|deploy\w*|"
                   r"release\w*|launch\w*|go-live|data collection|collect\w*|pilot\w*|use\b|adoption|"
                   r"(?:the\s+)?(?:first\s+|next\s+)?(?:sprint|milestone|roadmap)|S\d+|M\d+|v\d)" % DETERMINER, re.I)
PRIORITIES = ("required", "desired", "future")
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


def requirements(lines):
    """[(id, heading level, line number, {field: value}, acceptance bullets)] for each REQ heading."""
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
        fields, bullets, current = {}, 0, None
        for b in body:
            f = FIELD.match(b)
            if f:
                current = re.sub(r"\s+", " ", f.group(1).lower())
                fields.setdefault(current, f.group(2).strip())
                if current == "acceptance criteria" and BULLET.match(f.group(2) or ""):
                    bullets += 1
            elif current == "acceptance criteria" and BULLET.match(b):
                bullets += 1
        reqs.append((m.group(2), len(m.group(1)), i, fields, bullets))
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
    """[(status, check, evidence)] for one report's text."""
    text = re.sub(r"<!--.*?-->", "", text.replace("﻿", ""), flags=re.S)
    lines = [l.rstrip("\r") for l in text.split("\n")]
    out = []

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
    # Only the header can claim the report's own adoption; elsewhere "adopted by R-NN" cites an existing
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
            problems.append("an adopted report's Status must say 'Adopted by R-NN (vN)': " + short(sline))
        elif am and vm and am.group(2) != vm.group(1):
            problems.append("Status adopts v%s but the Version line is v%s" % (am.group(2), vm.group(1)))
        if banner:
            out.append(("WARN", name, "an adopted report still carries a DRAFT banner: " + short(banner[0])))
    out += [("FAIL", name, p) for p in problems] or [("PASS", name, short(sline or ""))]

    # (b) sections
    found, dupes = sections(lines)
    name = "(b) sections 1-13 present, each with content or 'Not applicable: <reason>'"
    problems = ["section %d missing (expected a heading '## %d. ...')" % (n, n) for n in SECTIONS if n not in found]
    problems += ["section %d appears more than once" % n for n in dupes]
    for n in SECTIONS:
        if n not in found:
            continue
        heading, body = found[n]
        na, reason = not_applicable(body)
        if na and not reason:
            problems.append("section %d says 'Not applicable' without a reason" % n)
        elif not na and not any(l.strip() for l in body):
            problems.append("section %d is empty: write it, or 'Not applicable: <reason>'" % n)
    order = [n for n in found if n in SECTIONS]
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
    problems, adopt_problems, seen = [], [], {}
    if not reqs:
        problems.append("no requirement headings '#### REQ-<AREA>-NN: <name>'")
    for rid, level, at, fields, bullets in reqs:
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
        elif not re.match(r"(%s)\b" % "|".join(PRIORITIES), prio) and not OPEN_PRIORITY.match(prio):
            problems.append("%s: Priority '%s' is not required / desired / future, or open (O-NN) when the PI "
                            "left the scope open" % (rid, short(prio, 30)))
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
    out += [("FAIL", name_d, p) for p in adopt_problems] or [("PASS", name_d, "no requirement adopted by a draft"
                                                               if stage == "draft" else "stage adopted")]

    # (e) section 6 decision table
    name = "(e) section 6: decision table with alternatives"
    problems = []
    if 6 in found and is_na(6):
        out.append(("WARN", name, "section 6 says Not applicable: no architecture decisions recorded"))
    elif 6 in found:
        want = [c.lower() for c in DECISION_COLUMNS]
        candidates = tables(body_of(6))
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
        problems.append("section 6 missing")
    out += [("FAIL", name, p) for p in problems]

    # (f) section 12 open items name a gate
    name = "(f) section 12: every open item names a gate"
    problems, items = [], 0
    if 12 in found and not is_na(12):
        body = body_of(12)
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
    out += [("FAIL", name, p) for p in problems] or [("PASS", name, "%d open item(s)" % items)]
    odd = sorted({m.group(0) for line in lines for m in GATE.finditer(line) if not STAGE.match(line[m.start():])})
    if odd:
        out.append(("WARN", "(f) gates name a project stage",
                    "gate wording does not name a project stage (planning, implementing <what>, deployment, a "
                    "sprint, milestone or release): " + ", ".join(short(g, 40) for g in odd)))

    # (g) section 13: adoption does not authorize implementation
    name = "(g) section 13: adoption does not authorize implementation"
    s13 = " ".join(body_of(13))
    sentences = re.split(r"(?<=[.;:!?])\s+", s13)
    hit = next((x for x in sentences if re.search(r"\b(?:not|no|never)\b", x, re.I) and re.search(r"implement", x, re.I)), None)
    out.append(("PASS", name, short(hit)) if hit else
               ("FAIL", name, "section 13 does not say that adoption does not authorize implementation"))

    # (h) completeness check
    name = "(h) completeness check subsection"
    cc = next((l for l in lines if re.match(r"^#{2,4}\s+.*completeness check", l, re.I)), None)
    out.append(("PASS", name, short(cc)) if cc else ("WARN", name, "no 'Completeness check' subsection"))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("file")
    ap.add_argument("--stage", choices=("draft", "adopted"), default="draft")
    args = ap.parse_args(argv)
    try:
        sys.stdout.reconfigure(errors="replace")
    except AttributeError:
        pass
    try:
        text = read_text(args.file)
    except OSError as exc:
        print("cannot read %s: %s" % (args.file, exc))
        return 2
    results = check(text, args.stage)
    for status, name, evidence in results:
        print("%-4s  %s\n      %s" % (status, name, evidence))
    failed = any(s == "FAIL" for s, _, _ in results)
    print("\nRESULT: " + ("FAIL" if failed else "PASS"))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
