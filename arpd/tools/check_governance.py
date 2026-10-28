#!/usr/bin/env python3
r"""Governance checks for an ARPD project.

    python arpd/tools/check_governance.py      (from the project root)

Each step reports PASS, FAIL, MISSING (could not run), PENDING (awaiting
the PI's ruling) or ADVISORY (a note that does not change the result). The overall result is:

- FAIL if any step failed;
- otherwise INCOMPLETE if any step could not run (MISSING) or awaits the PI (PENDING);
- otherwise PASS.

Within the steps listed below, it does not report PASS for an item it could not check. What it does
not check is printed in a "Not checked" block after the steps. It relies on what is recorded in
DECISIONS.md, the sprint records, REQUIREMENTS.md and START-HERE.md's map; it cannot show that those
records are true.

Run in the kit itself (a folder holding the .arpd-kit marker), it stops: the kit is not a project.
When arpd/VERSION exists, its first line is printed first.

Exit codes: 0 PASS, 1 FAIL, 2 INCOMPLETE.

The checks:

1. The governing documents exist.
   Charter adopted; templates filled:
   - an unfilled {{...}} placeholder in a governing document is a FAIL (placeholders inside HTML
     comments, fenced code blocks and inline code are ignored);
   - CLAUDE.md's Version line decides adoption: it must name an adoption ruling (R-NN) that exists
     in DECISIONS.md and is not pending. Pending or awaiting adoption, or a pending or unrecorded
     ruling, is PENDING; no Version line is MISSING;
   - once adopted, no standing authorization (authority profile) in DECISIONS.md is ADVISORY.
2. Intra-repository Markdown links resolve (older kit copies a v0.5 project may still hold,
   docs/arpd-kit/ and, with arpd/VERSION or kit/, examples/ and evaluation/, are listed under
   "Not checked").
3. Requirements:
   - states are valid;
   - Verified and Validated rows carry evidence;
   - Validated rows cite a ruling (R-NN);
   - sources point to items that exist in PARADIGM-SPEC.md or DECISIONS.md.
4. Plans: unique numbers, valid status.
5. Closed sprint records:
   - have a decision-tracking table, every row of which can be read (a row whose cell count does
     not match the header is a FAIL, never silently skipped; "\|" is a literal pipe inside a cell);
   - every row has a recognized route (routine / delegated / consult). A missing or unrecognized
     route is a FAIL, unless the record is a legacy one with a "Tier" column (Tier C is read as the
     consult route). A routine row that states a scientific consequence is a FAIL;
   - every consequential decision cites its authority: a standing authorization (SA-NN) for the
     delegated route (a delegation the PI gave in a ruling is recorded as an SA citing that ruling),
     a ruling (R-NN) for the consult route. Every SA-NN and R-NN cited must exist in DECISIONS.md,
     outside HTML comments; one whose entry is still pending counts as pending, not as authority.
     One still awaiting a decision makes the result INCOMPLETE (PENDING);
   - each consequential decision records whether it was authorized before adoption (first word
     yes / before, no / after, or pending). Not recorded makes the result INCOMPLETE (MISSING).
     Authorized after adoption is ADVISORY if ratified and recorded as an incident (I-NN), and a
     FAIL otherwise;
   - a sprint row is a snapshot; the decision's own entry in DECISIONS.md (DEC-NN: its Authorized
     and Adopted lines) is authoritative, but it can never excuse a late authorization:
     - an entry whose Authorized line records ratification after adoption is late, even if the
       row says "yes": ADVISORY with an incident (I-NN, in the row or the entry), FAIL otherwise;
     - dates must be ISO 8601 (YYYY-MM-DD, or YYYY-MM-DDTHH:MMZ). If both lines carry dates and
       either is in another format, the order cannot be checked: MISSING. If authorization is the
       later one (full timestamps when both have times; the same day without times is in order),
       it is late: ADVISORY with an I-NN, FAIL otherwise;
     - a row that cites its own authority and is marked late (timing no / after) never becomes
       PASS;
     - the entry decides whether the decision was adopted: an Adopted line of "not yet", pending or
       none means not adopted, whatever the row says;
     - a PENDING row becomes PASS when the entry cites given authority with ISO dates in order
       (authorized no later than adopted), and MISSING when those dates are not recorded. This
       includes a frozen row marked "after" whose own authority cell was pending, such as a
       pre-charter default the PI later ratified: the incident is already in the record;
     - "Deferred by R-NN" is a deferral, never authorization. A PENDING decision not adopted and
       deferred by a given ruling is ADVISORY: still to decide, and dependent work stays blocked.
       A deferral cannot cover a decision that was adopted: FAIL unless ratified with an incident.
       Once the entry cites given authority, earlier deferral history is ignored and the decision
       is checked as authorized;
     - a row marked authorized before adoption still fails if its entry records adoption (a date
       or version, not "not yet") without given authority; if the entry records neither authority
       nor adoption, it is PENDING;
     - the authorization date is the ISO date next to the cited R-NN / SA-NN, or right after
       "authorized"; several dates with none tied to the authority is MISSING (ambiguous);
     - a consequential row with no entry in DECISIONS.md is ADVISORY: checked on the row alone.
   A ruling or SA counts as given only if its section has a Given line that is not pending-like
   (pending, awaiting, to be given, not yet, placeholder, TBD), or, with no Given line, a dated
   heading (YYYY-MM-DD) with no pending-like word.
   No sprint records (no reports/sprints/, or an empty one) passes: setup can be complete with
   planning still to do.
5b. Open sprint records (no completed **Closed:** field): their decision tracking is not checked
   until close. Only Part 1's approval references are: in a record with the rows "Approved plan",
   "Execution authorized by" or "Transition policy", every R-NN / SA-NN those rows cite must exist
   in DECISIONS.md (FAIL otherwise) and must not be pending (PENDING); an "Approved plan" or
   "Execution authorized by" row that cites none is MISSING. A cited SA that has been superseded is
   ADVISORY (Part 1 is frozen at sprint start). A ruling cited in "Execution authorized by" whose
   own "Execution authorized:" line says no is a FAIL: a planning-only approval is not a start. An
   "Approved plan" row that cites no ruling (only an SA) is ADVISORY: plan approval is a ruling. The "Approved plan" row must name a plan and
   version (PLAN-YYYY-MM-DD[-n] vN; MISSING otherwise) whose file is in reports/planning/ (FAIL
   otherwise); a cited ruling's Approves line must name that file and version (FAIL otherwise; no
   Approves line is ADVISORY). A record without these rows (the older format, including the old
   "Authorized to continue..." row) is ADVISORY, never a FAIL. A plan in reports/planning/ marked
   "approved by R-NN" where R-NN is not a given ruling is ADVISORY; a draft plan needs no ruling.
6. START-HERE.md's "## Map" section mentions every top-level entry (except START-HERE.md itself and
   the skipped folders, arpd/ among them), and every path it lists (in backticks, in a table row's first
   column or first on a bullet line) exists, unless its line says "pending:" or "git-ignored"
   (advisory). A project set up before v0.6 whose START-HERE.md has no Map section uses its INDEX.md
   (the whole file) instead.
7. Event logging and agent roles installed: .claude/settings.json runs arpd/tools/hooks/log_hook.py
   (or, in a project set up before v0.6, tools/hooks/log_hook.py; directly or through the fail-safe
   launcher), that script exists (FAIL otherwise: a missing script can block every prompt), and
   does not set "disableAllHooks": true; and, when the Team arrangement line mentions subagents or
   peers (and is not solo), .claude/agents/implementer.md and reviewer.md exist. Anything missing is
   MISSING, unless a decision in DECISIONS.md records it as not installed ("event logging not
   installed" / "agent files not installed", citing R-NN or with a "Route: routine" line), which is
   ADVISORY. An agent file that differs from arpd/agents/ is ADVISORY.
8. ARPD skills installed: .claude/skills/arpd-checkin/SKILL.md, .claude/skills/arpd-amend/SKILL.md
   and .claude/skills/arpd-plan/SKILL.md exist in the project (only there). Anything missing is MISSING, unless a decision records "skills not installed" as in step 7
   (ADVISORY).
9. Live items cite no superseded spec item (advisory): a requirement's source, an A-rule in
   ARCHITECTURE.md, a claim (CLM-NN) in PARADIGM-SPEC.md, or a standing authorization in force
   (one not "superseded by SA-NN") that cites a PARADIGM-SPEC.md item whose row says "Superseded
   by" is ADVISORY. Retired requirements and A-rules are ignored.
10. Requirement details (advisory): when REQUIREMENTS.md has a "## Requirement details" section,
   a requirement in the table (not Retired) with no details entry ("### REQ-...:") holding
   "Acceptance criteria" with at least one bullet is ADVISORY. Without that section (the older
   format) the step passes and says it was not compared.
11. Adopted blueprint traced (advisory): for each given ruling whose Adopts line names a file and version
   (e.g. "`reports/setup/PROJECT-BLUEPRINT.md` v2", or, in a project set up before the rename,
   "`reports/setup/PROJECT-DEFINITION.md` v2" or the legacy "`reports/PROJECT-DEFINITION.md` v2"),
   that file exists (a named reports/setup/PROJECT-BLUEPRINT.md that does not exist is read from the
   older reports/setup/PROJECT-DEFINITION.md beside it, if that exists) and its Status line reads
   "Adopted by R-NN (vN)" with the same ruling and version; otherwise ADVISORY. With no Adopts line
   (the older format) the step passes and says it was not compared. The blueprint's content is not
   compared with the governing documents.

A file the checks read that is not UTF-8 (for example saved as UTF-16) is a FAIL in the step that read
it: "<file>: not UTF-8 (save as UTF-8)".
"""
import datetime
import io
import os
import re
import sys

ROOT = "."
GOVERNING = ["CLAUDE.md", "PARADIGM-SPEC.md", "REQUIREMENTS.md", "MASTER_PLAN.md", "DECISIONS.md",
             "ARCHITECTURE.md", "STATUS.md", "START-HERE.md"]
KIT_MARKER = ".arpd-kit"  # present at the root of the ARPD kit itself, never in a project
REQ_STATES = {"Planned", "Implemented", "Verified", "Validated", "Retired"}
PLAN_STATES = {"Proposed", "Approved", "Active", "Complete"}
# "arpd" is the kit payload copied into the project (not the project's own records); "kit" is its name
# in projects set up before v0.6.
SKIP_DIRS = {".git", "node_modules", "__pycache__", "logs", "output", ".venv", "venv", "arpd", "kit"}

results = []
not_checked = []   # exclusions found while checking, printed after the steps


def step(name, status, details=()):
    results.append((name, status, list(details)))


class NotUTF8(Exception):
    """A file the checks read is not UTF-8; the step that read it FAILs."""

    def __init__(self, path):
        Exception.__init__(self, path)
        self.path = path.replace(os.sep, "/")


def read(path):
    try:
        with io.open(os.path.join(ROOT, path), encoding="utf-8") as fh:
            return fh.read()
    except UnicodeDecodeError:
        raise NotUTF8(path)


def governing():
    """The governing documents. A project set up before v0.6 may have INDEX.md and no START-HERE.md."""
    if not os.path.exists(os.path.join(ROOT, "START-HERE.md")) and os.path.exists(os.path.join(ROOT, "INDEX.md")):
        return [f if f != "START-HERE.md" else "INDEX.md" for f in GOVERNING]
    return list(GOVERNING)


def md_files():
    for d, dirs, files in os.walk(ROOT):
        dirs[:] = [x for x in dirs if x not in SKIP_DIRS and not x.startswith(".")]
        for f in files:
            if f.endswith(".md"):
                yield os.path.relpath(os.path.join(d, f), ROOT)


MALFORMED = "__malformed__"


def split_row(line):
    """Cells of one Markdown table line. A backslash-escaped pipe is a literal pipe in a cell."""
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    return [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", s)]


def table_rows(text, header_startswith):
    """Yield dict rows of the first Markdown table whose header starts with header_startswith.

    A row whose cell count does not match the header is yielded as {MALFORMED: line}, so that the
    caller reports it rather than silently dropping it.
    """
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip().startswith("|") and line.strip("| ").lower().startswith(header_startswith.lower()):
            headers = split_row(line)
            for row in lines[i + 2:]:
                if not row.strip().startswith("|"):
                    return
                cells = split_row(row)
                if len(cells) == len(headers):
                    yield dict(zip(headers, cells))
                else:
                    yield {MALFORMED: row.strip()}
            return


def check_exists():
    missing = [f for f in governing() if not os.path.exists(os.path.join(ROOT, f))]
    step("Governing documents exist", "FAIL" if missing else "PASS", ["missing: " + m for m in missing])


def _strip_non_text(text):
    """Text without HTML comments, fenced code blocks or inline code."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"^(```|~~~).*?^\1[^\n]*$", "", text, flags=re.S | re.M)
    return re.sub(r"`[^`\n]*`", "", text)


def _version_status(known, pending_ids):
    """(status, note) for CLAUDE.md's Version line: PASS, PENDING or MISSING."""
    text = re.sub(r"<!--.*?-->", "", read("CLAUDE.md"), flags=re.S)
    text = re.sub(r"^(```|~~~).*?^\1[^\n]*$", "", text, flags=re.S | re.M)
    m = re.search(r"^[ \t]*(?:[-*][ \t]+)?\**Version\b:?\**:?(.*)$", text, flags=re.M | re.I)
    if not m:
        return "MISSING", "CLAUDE.md: no Version line, so adoption cannot be checked"
    line = m.group(1)
    adopted_by = re.search(r"adopted by\b[^.;]*?\b(R-\d+)\b", line, re.I)
    if adopted_by and adopted_by.group(1) in known:
        return "PASS", None
    sentences = re.split(r"(?<=[.;])\s+", line)
    chosen = next((x for x in sentences if re.search(r"adopt|\bR-\d+\b", x, re.I)), line)
    if re.search(r"\b(pending|awaiting|not yet adopted|proposal)\b", chosen, re.I):
        return "PENDING", "CLAUDE.md: the charter is not yet adopted (%s)" % _clean(chosen)[:80]
    refs = re.findall(r"\bR-\d+\b", chosen)
    if any(r in known for r in refs):
        return "PASS", None
    if refs:
        return "PENDING", ("CLAUDE.md: adoption ruling %s is %s in DECISIONS.md"
                           % (refs[0], "still pending" if refs[0] in pending_ids else "not recorded"))
    return "PENDING", "CLAUDE.md: the Version line names no adoption ruling (R-NN)"


def check_adoption():
    unfilled = []
    for f in governing():
        if not os.path.exists(os.path.join(ROOT, f)):
            continue  # reported by check_exists
        for ph in sorted(set(re.findall(r"\{\{[^{}]*\}\}", _strip_non_text(read(f))))):
            unfilled.append("%s: unfilled placeholder %s" % (f, ph[:60]))
    notes = list(unfilled)
    status = "FAIL" if unfilled else "PASS"
    if os.path.exists(os.path.join(ROOT, "CLAUDE.md")):
        known, pending_ids, _ = decision_index()
        vstatus, note = _version_status(known, pending_ids)
        if note:
            notes.append(note)
        if status == "PASS":
            status = vstatus
        if vstatus == "PASS" and not any(k.startswith("SA-") for k in known):
            notes.append("DECISIONS.md: no standing authorization (authority profile) recorded")
            if status == "PASS":
                status = "ADVISORY"
    step("Charter adopted; templates filled", status, notes)


def _older_blueprint(path):
    """path, or, when it names a PROJECT-BLUEPRINT.md that does not exist, the older PROJECT-DEFINITION.md
    beside it if that exists (a project set up before the rename)."""
    if os.path.basename(path) != "PROJECT-BLUEPRINT.md" or os.path.isfile(os.path.join(ROOT, path)):
        return path
    older = path[:-len("PROJECT-BLUEPRINT.md")] + "PROJECT-DEFINITION.md"
    return older if os.path.isfile(os.path.join(ROOT, older)) else path


def check_adopted_report():
    """Advisory: the blueprint a ruling's Adopts line names exists and its Status names that ruling and version."""
    name = "Adopted blueprint traced (advisory)"
    known, _, sections = decision_index()
    traced = [(r, _entry_line(body, "Adopts")) for r, body in sorted(sections.items()) if r.startswith("R-")]
    traced = [(r, line) for r, line in traced if line]
    if not traced:
        step(name, "PASS", ["no ruling in DECISIONS.md has an Adopts line: older format; not compared"])
        return
    notes, ok = [], []
    for rid, adopts in traced:
        if rid not in known:
            ok.append("%s is still pending; its Adopts line is not compared" % rid)
            continue
        m = re.search(r"`([^`]+)`", adopts) or re.search(r"(\S+\.md)\b", adopts)
        if not m:
            notes.append("%s: its Adopts line names no file" % rid)
            continue
        path = m.group(1).strip()
        v = re.search(r"\bv(\d+)\b", adopts[m.end():])
        if not v:
            notes.append("%s: its Adopts line names %s but no version (vN)" % (rid, path))
            continue
        want = "Adopted by %s (v%s)" % (rid, v.group(1))
        path = _older_blueprint(path)
        if not os.path.isfile(os.path.join(ROOT, path)):
            notes.append("%s, named by %s's Adopts line, does not exist" % (path, rid))
            continue
        text = re.sub(r"<!--.*?-->", "", read(path), flags=re.S)
        header = re.split(r"^## ", text, maxsplit=1, flags=re.M)[0]
        st = re.search(r"^\s*(?:[-*]\s+)?\**\s*Status\s*\**\s*:(.*)$", header, re.M | re.I)
        if not st:
            notes.append("%s: no Status line in its header; cannot check that it reads '%s'" % (path, want))
            continue
        status = _clean(st.group(1))
        am = re.search(r"adopted\s+by\s+(R-\d+)\s*\(\s*v(\d+)\s*\)", status, re.I)
        if not am or (am.group(1), am.group(2)) != (rid, v.group(1)):
            notes.append("%s: Status line does not read '%s' (it reads: %s)" % (path, want, status[:80]))
        else:
            ok.append("%s: %s" % (path, want))
    step(name, "ADVISORY" if notes else "PASS", notes or ok)


# Folders that only the old kit's copies of examples/ and evaluation/ held: a project's own examples/ or
# evaluation/ (a converted clone keeps the PI's files there) is never called a kit leftover.
LEGACY_KIT_MARKS = {"examples": ("march-1991",),
                    "evaluation": ("developer-tests", "study1-comparative", "study2-usability", "feasibility-demo")}


def _legacy_kit_folders():
    """Old kit copies a v0.5 project may still hold after moving to arpd/ (removed by a remove-only
    commit): docs/arpd-kit/ always; examples/ and evaluation/ only when arpd/VERSION or kit/ marks
    the project as set up from the kit and the folder holds what the old kit's copy held."""
    found = ["docs/arpd-kit/"] if os.path.isdir(os.path.join(ROOT, "docs", "arpd-kit")) else []
    if os.path.isfile(os.path.join(ROOT, "arpd", "VERSION")) or os.path.isdir(os.path.join(ROOT, "kit")):
        found += [d + "/" for d, marks in sorted(LEGACY_KIT_MARKS.items())
                  if any(os.path.isdir(os.path.join(ROOT, d, m)) for m in marks)]
    return found


def check_links():
    bad = []
    legacy = _legacy_kit_folders()
    if legacy:
        not_checked.append("links in older kit copies (%s); remove them in one remove-only commit"
                           % ", ".join(legacy))
    for f in md_files():
        if any(f.replace(os.sep, "/").startswith(d) for d in legacy):
            continue
        text = read(f)
        text = re.sub(r"```.*?```", "", text, flags=re.S)  # ignore code blocks
        for target in re.findall(r"\]\(([^)\s]+)\)", text):
            if re.match(r"^(https?:|mailto:|#)", target) or "{{" in target:
                continue
            path = target.split("#")[0].split(":")[0] if not re.match(r"^[A-Za-z]:", target) else target
            full = os.path.normpath(os.path.join(os.path.dirname(f), path))
            if path and not os.path.exists(full):
                bad.append("%s -> %s" % (f, target))
    step("Intra-repo links resolve", "FAIL" if bad else "PASS", bad)


def spec_ids():
    ids = set()
    for f in ("PARADIGM-SPEC.md", "DECISIONS.md"):
        if os.path.exists(os.path.join(ROOT, f)):
            ids |= set(re.findall(r"\b((?:CON|OP|INV|CLM|NCL|VAL|ASM|Q|R|DEC)-\d+)\b", read(f)))
    return ids


def check_requirements():
    if not os.path.exists(os.path.join(ROOT, "REQUIREMENTS.md")):
        step("Requirements", "MISSING", ["REQUIREMENTS.md absent"])
        return
    rows = list(table_rows(read("REQUIREMENTS.md"), "ID"))
    if not rows:
        step("Requirements", "MISSING", ["no requirements table found"])
        return
    ids = spec_ids()
    problems = []
    for r in rows:
        if MALFORMED in r:
            problems.append("malformed row (cell count does not match the header): %s" % r[MALFORMED][:80])
            continue
        rid, state = r.get("ID", ""), r.get("State", "")
        ev, src = r.get("Evidence", ""), r.get("Source", "")
        if not rid or "{{" in rid:
            not_checked.append("REQUIREMENTS.md: a row with %s was skipped (template or blank row)"
                               % ("a placeholder ID" if rid else "no ID"))
            continue
        if state not in REQ_STATES:
            problems.append("%s: invalid state '%s'" % (rid, state))
        if state in ("Verified", "Validated") and not ev:
            problems.append("%s: %s without evidence" % (rid, state))
        if state == "Validated" and not re.search(r"\bR-\d+\b", ev):
            problems.append("%s: Validated without a ruling (R-NN) in evidence" % rid)
        for ref in re.findall(r"\b(?:CON|OP|INV|CLM|VAL|R)-\d+\b", src):
            if ref not in ids:
                problems.append("%s: source %s not found in PARADIGM-SPEC/DECISIONS" % (rid, ref))
        if not re.search(r"\b(?:CON|OP|INV|CLM|VAL|R)-\d+\b", src):
            problems.append("%s: no traceable source" % rid)
    step("Requirements: states, evidence, traceability", "FAIL" if problems else "PASS", problems)


def check_requirement_details():
    """Advisory: each adopted requirement has acceptance criteria in its Requirement details entry."""
    name = "Requirement details: acceptance criteria (advisory)"
    if not os.path.exists(os.path.join(ROOT, "REQUIREMENTS.md")):
        return  # reported by check_requirements
    text = re.sub(r"<!--.*?-->", "", read("REQUIREMENTS.md"), flags=re.S)
    m = re.search(r"^## Requirement details\b(.*?)(?=^## |\Z)", text, re.S | re.M)
    if not m:
        step(name, "PASS", ["no Requirement details section in REQUIREMENTS.md (older format); not compared"])
        return
    entries = {}
    for e in re.finditer(r"^#{3,4}\s+\**(REQ-[A-Za-z0-9]+-\d+)\b(.*?)(?=^#{1,4}\s|\Z)", m.group(1), re.S | re.M):
        body = e.group(2)
        ac = re.search(r"^[-*]?\s*\**Acceptance criteria\**\s*:?\**(.*?)(?=^[-*]\s+\**[A-Z][\w /]*:|\Z)", body, re.S | re.M)
        entries[e.group(1)] = bool(ac and re.search(r"^\s+(?:[-*+]|\d+[.)])\s+\S", ac.group(1), re.M))
    notes = []
    for r in table_rows(text, "ID"):
        rid = r.get("ID", "")
        if MALFORMED in r or not rid or "{{" in rid or r.get("State") == "Retired":
            continue
        if not entries.get(rid):
            notes.append("%s: adopted requirement without acceptance criteria in Requirement details" % rid)
    step(name, "ADVISORY" if notes else "PASS", notes)


def check_plans():
    d = os.path.join(ROOT, "plans")
    if not os.path.isdir(d):
        step("Plans: unique numbers, valid status", "PASS",
             ["no plans/ folder yet (it is created with the first task plan)"])
        return
    nums, problems = {}, []
    for name in sorted(os.listdir(d)):
        m = re.match(r"(\d{3})-.+\.md$", name)
        if not m:
            continue
        nums.setdefault(m.group(1), []).append(name)
        st = re.search(r"\|\s*Status\s*\|\s*([A-Za-z]+)", read(os.path.join("plans", name)))
        if not st or st.group(1) not in PLAN_STATES:
            problems.append("%s: status missing or invalid" % name)
    problems += ["duplicate plan number %s: %s" % (n, ", ".join(v)) for n, v in nums.items() if len(v) > 1]
    step("Plans: unique numbers, valid status", "FAIL" if problems else "PASS", problems)


def _col(row, *prefixes):
    """Value of the first column whose header starts with any of the given prefixes."""
    for key, val in row.items():
        for p in prefixes:
            if key.lower().startswith(p.lower()):
                return val
    return ""


def _has_col(row, prefix):
    return any(key.lower().startswith(prefix.lower()) for key in row)


def _clean(value):
    """A cell value without Markdown emphasis (*, **, backticks) or surrounding whitespace."""
    return re.sub(r"[*`]", "", value or "").strip()


def _states_none(consequence):
    """True if a 'scientific consequence' cell says there is none (none / a dash / empty)."""
    c = _clean(consequence).lower()
    return c in ("", "\u2014", "\u2013", "-", "n/a") or bool(re.match(r"^none\b", c))


def _timing(value):
    """Classify the 'authorized before adoption?' cell by its first word.

    Returns 'timely' (yes / before), 'late' (no / after), 'pending', or None (not recorded, or not
    readable). "none" and "not applicable" are not read as "no".
    """
    m = re.match(r"^\W*(yes|no|pending|before|after)\b", _clean(value), re.I)
    if not m:
        return None
    return {"yes": "timely", "before": "timely", "no": "late", "after": "late"}.get(m.group(1).lower(), "pending")


PENDING_LIKE = r"(pending|awaiting|to be given|not yet|placeholder|tbd)\b"


def decision_index():
    """What DECISIONS.md records, outside HTML comments.

    Returns (known, pending_ids, sections):
    - known: SA-NN and R-NN entries that exist and are not pending (a heading, or a table row's first
      cell). A heading containing "(pending", a section whose Given line says pending, or a table row
      mentioning "pending" is pending;
    - pending_ids: SA-NN and R-NN entries that exist but are still pending;
    - sections: the text of every SA-NN, R-NN and DEC-NN section, by ID.
    """
    if not os.path.exists(os.path.join(ROOT, "DECISIONS.md")):
        return set(), set(), {}
    text = re.sub(r"<!--.*?-->", "", read("DECISIONS.md"), flags=re.S)
    sections, headings, current = {}, {}, None
    table_pending = {}
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("#"):
            m = re.match(r"^#+\s*[*`]*((?:SA|R|DEC)-\d+)\b", s)
            current = m.group(1) if m else None
            if current:
                headings[current] = s
                sections[current] = s + "\n"
            continue
        if current:
            sections[current] += line + "\n"
        if s.startswith("|"):
            m = re.match(r"^[*`\s]*((?:SA|R)-\d+)\b", split_row(s)[0])
            if m:
                table_pending[m.group(1)] = table_pending.get(m.group(1), False) or "pending" in s.lower()
    known, pending_ids = set(), set()
    for ident, head in headings.items():
        if ident.startswith("DEC-"):
            continue
        given = re.search(r"\*\*Given:\*\*\s*(.*)", sections[ident])
        if given:
            is_given = not re.match(r"^\W*" + PENDING_LIKE, _clean(given.group(1)), re.I)
        else:
            is_given = (bool(re.search(r"\b\d{4}-\d{2}-\d{2}\b", head))
                        and not re.search(r"\(?" + PENDING_LIKE, head, re.I))
        if "(pending" in head.lower():
            is_given = False
        (known if is_given else pending_ids).add(ident)
    for ident, is_pending in table_pending.items():
        if ident in headings:
            continue
        (pending_ids if is_pending else known).add(ident)
    return known, pending_ids, sections


def _entry_line(body, label):
    m = re.search(r"^\s*-\s*\*\*%s:\*\*(.*?)(?=^\s*-\s*\*\*|^#|\Z)" % label, body, flags=re.S | re.M)
    return " ".join(m.group(1).split()) if m else ""


_MONTH = r"(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?"
_NON_ISO = (r"\b\d{1,2}/\d{1,2}/\d{2,4}\b|\b\d{1,2}\.\d{1,2}\.\d{4}\b|\b\d{1,2}\s+" + _MONTH + r"\s+\d{4}\b|\b"
            + _MONTH + r"\s+\d{1,2},?\s+\d{4}\b")
_ISO = r"\b(\d{4}-\d{2}-\d{2})(?:[T ](\d{2}:\d{2})(?::\d{2})?\s*(Z|[+-]\d{2}:?\d{2})?)?"


def _moment(m):
    """The aware datetime of an ISO match that has a time, or None."""
    if not m.group(2):
        return None
    tz = (m.group(3) or "Z").replace("Z", "+00:00")
    if re.match(r"^[+-]\d{4}$", tz):
        tz = tz[:3] + ":" + tz[3:]
    try:
        return datetime.datetime.fromisoformat("%sT%s%s" % (m.group(1), m.group(2), tz))
    except ValueError:
        return None


def _when(text):
    """(kind, date, moment, shown) for the first date in a line: kind is "iso", "other" or None."""
    m = re.search(_ISO, text)
    if m:
        return "iso", m.group(1), _moment(m), m.group(0).strip()
    if re.search(_NON_ISO, text, re.I):
        return "other", None, None, None
    return None, None, None, None


_TIE = r"^[\s,;:()\-\u2013\u2014]*(?:by|on|in|via|under)?[\s,;:()\-\u2013\u2014]*$"


def _auth_when(auth):
    """Like _when, for the Authorized line: the date tied to the authority.

    With one ISO date, that date. With several, the one immediately before or after a cited R-NN /
    SA-NN, or right after "authorized"; kind "ambiguous" if none (or more than one) is tied.
    """
    dates = list(re.finditer(_ISO, auth))
    if len(dates) <= 1:
        return _when(auth)
    refs = list(re.finditer(r"\b(?:SA|R)-\d+\b", auth))
    tied = []
    for m in dates:
        before, after = auth[:m.start()], auth[m.end():]
        if re.search(r"authori[sz]ed\s*(?:on\s*)?$", before, re.I):
            tied.append(m)
            continue
        for r in refs:
            between = auth[m.end():r.start()] if r.start() >= m.end() else auth[r.end():m.start()]
            if re.match(_TIE, between, re.I):
                tied.append(m)
                break
    if len({t.group(0) for t in tied}) != 1:
        return "ambiguous", None, None, None
    t = tied[0]
    return "iso", t.group(1), _moment(t), t.group(0).strip()


def _entry(rid, needed, known, sections):
    """What the decision's own entry in DECISIONS.md records."""
    body = sections.get(rid, "")
    auth, adopted = _entry_line(body, "Authorized"), _entry_line(body, "Adopted")
    deferred = re.search(r"\bdeferred by (R-\d+)\b", _clean(body), re.I)
    auth_wo_deferral = re.sub(r"\bdeferred by R-\d+\b", "", auth, flags=re.I)  # a deferral is not authorization
    a_kind, a_date, a_moment, a_show = _auth_when(auth)
    d_kind, d_date, d_moment, d_show = _when(adopted)
    both = bool(a_kind and d_kind)
    iso_both = both and a_kind == d_kind == "iso"
    late = False
    if iso_both:
        late = (a_moment > d_moment) if (a_moment and d_moment) else (a_date > d_date)
    not_adopted = bool(adopted) and re.match(r"^\W*(not yet|no\b|pending|none|n/a|—|-|$)", _clean(adopted), re.I)
    given = [x for x in re.findall(needed, auth_wo_deferral) if x in known]
    return {
        "exists": bool(body),
        "has_auth_line": bool(auth),
        "given": given,
        "incident": bool(re.search(r"\bI-\d+\b", auth)),
        "after_wording": bool(re.search(r"ratifi\w*\s+after\b|after\s+(?:the\s+)?adoption", auth, re.I)),
        "auth_pending": bool(re.match(r"^\W*" + PENDING_LIKE, _clean(auth_wo_deferral), re.I)),
        "has_adopted_line": bool(adopted),
        "adopted": bool(adopted) and not not_adopted,
        "date_ambiguous": a_kind == "ambiguous",
        "dates_bad": both and a_kind != "ambiguous" and not iso_both,
        "dates_late": late,
        "dates_in_order": iso_both and not late,
        "dates": (a_show, d_show),
        # a deferral counts only while the entry cites no given authority
        "deferred_by": deferred.group(1) if deferred and deferred.group(1) in known and not given else None,
    }


def _verdict(kind, msg, row_late, row_incident, row_auth_pending, e, name, rid):
    """Combine the sprint row's verdict with the decision's own entry. Returns (kind, msg) or None for PASS.

    kind is the row's own verdict: PENDING, ADVISORY (late, incident recorded), FAIL (late, no
    incident) or TIMELY.
    """
    if not e["exists"]:
        if kind == "TIMELY":
            return "ADVISORY", "%s: %s has no decision entry in DECISIONS.md; checked on the sprint row alone" % (
                name, rid)
        return kind, msg
    incident = row_incident or e["incident"]
    ratified = "%s: %s ratified after adoption (recorded incident; per its entry in DECISIONS.md)" % (name, rid)
    # 1. The entry records ratification after adoption: late, whatever the row says.
    if e["after_wording"] and (e["given"] or kind != "PENDING"):
        if incident:
            return "ADVISORY", ratified
        return "FAIL", ("%s: %s: its entry in DECISIONS.md records ratification after adoption, with no incident "
                        "recorded" % (name, rid))
    # 2. Dates: ISO 8601 only; the authorization date must be identifiable; authorization after adoption is late.
    if e["dates_late"]:
        auth_d, adopt_d = e["dates"]
        if incident:
            return "ADVISORY", "%s: %s ratified after adoption (authorized %s, adopted %s; recorded incident)" % (
                name, rid, auth_d, adopt_d)
        return "FAIL", ("%s: %s authorized after adoption per DECISIONS.md (authorized %s, adopted %s), with no "
                        "incident recorded" % (name, rid, auth_d, adopt_d))
    if kind == "FAIL":
        return kind, msg
    if e["date_ambiguous"]:
        return "MISSING", ("%s: %s authorization date ambiguous: several dates on the Authorized line, none tied to "
                           "the authority; cannot check order" % (name, rid))
    if e["dates_bad"]:
        return "MISSING", "%s: %s authorization/adoption dates not in ISO 8601; cannot check order" % (name, rid)
    # 3. The row says authorized before adoption: the entry must agree.
    if kind == "TIMELY":
        if e["given"] and not e["auth_pending"]:
            return None
        if e["adopted"]:
            return "FAIL", ("%s: consequential decision %s: its entry in DECISIONS.md records adoption without "
                            "authority" % (name, rid))
        if e["has_auth_line"] or e["has_adopted_line"]:
            return "PENDING", "%s: %s: its entry in DECISIONS.md records no authority yet" % (name, rid)
        return None
    if kind == "ADVISORY":
        return kind, msg
    # 4. PENDING: the entry decides adoption, deferral and authority.
    adopted = e["adopted"] if e["has_adopted_line"] else row_late
    if e["deferred_by"] and not adopted:
        return "ADVISORY", "%s: %s deferred by %s (still to decide; dependent work stays blocked)" % (
            name, rid, e["deferred_by"])
    if e["deferred_by"] and adopted:
        return "FAIL", ("%s: consequential decision %s was adopted, so the deferral by %s cannot cover it: "
                        "adopted without authority" % (name, rid, e["deferred_by"]))
    if not e["given"] or e["auth_pending"]:
        return kind, msg
    if row_late and not row_auth_pending:
        # the row itself cites authority and is marked late
        return ("ADVISORY", ratified) if incident else (
            "FAIL", "%s: %s authorized after adoption, with no incident recorded" % (name, rid))
    if e["dates_in_order"]:
        return None
    return "MISSING", ("%s: %s: its entry cites %s, but the Authorized and Adopted dates (ISO 8601) are not both "
                       "recorded; cannot check order" % (name, rid, e["given"][0]))


def _is_open(text):
    """True if a sprint record has no completed **Closed:** field."""
    if "**Closed:**" not in text:
        return True
    rest = text.split("**Closed:**", 1)[1]
    value = rest.split("\n", 1)[0].strip() or rest.strip()[:80]  # the date may sit on the next line
    value = value.strip("*_ ").lower()
    # Open: the template placeholder, or nothing / a not-yet word. Any other value closes the record.
    return "{{date" in value or not value or value.startswith(("not yet", "open", "—", "-", "n/a", "pending"))


def check_sprints():
    d = os.path.join(ROOT, "reports", "sprints")
    if not os.path.isdir(d):
        step("Closed sprints: decision tracking and authorization", "PASS", ["no sprint records yet"])
        return
    problems, missing, pending, advisories = [], [], [], []
    known, pending_ids, sections = decision_index()
    for name in sorted(os.listdir(d)):
        if not name.endswith(".md"):
            continue
        text = read(os.path.join("reports", "sprints", name))
        if _is_open(text):
            not_checked.append("reports/sprints/%s is open (not closed): decision tracking is checked only at "
                               "close; only its Part 1 approval references are checked now" % name)
            continue  # open sprint
        rows = list(table_rows(text, "ID | Decision"))
        if not rows:
            problems.append("%s: closed without a decision-tracking table" % name)
            continue
        for r in rows:
            if MALFORMED in r:
                problems.append("%s: malformed row (cell count does not match the header): %s"
                                % (name, r[MALFORMED][:80]))
                continue
            rid = _clean(r.get("ID", "")) or "?"
            route = _clean(_col(r, "Route")).lower()
            tier = _clean(_col(r, "Tier")).upper()
            authority = _clean(_col(r, "Authority", "Decided by"))
            timing_raw = _clean(_col(r, "Authorized before adoption", "Before or after commit"))
            consequence = _col(r, "Scientific consequence")
            route_word = re.match(r"^(routine|delegated|consult)\b", route)
            if route_word:
                route = route_word.group(1)
                consequential = route in ("delegated", "consult")
                needed = r"\bSA-\d+\b" if route == "delegated" else r"\bR-\d+\b"
                if route == "routine" and not _states_none(consequence):
                    problems.append("%s: %s: routine route but a scientific consequence is stated (%s)"
                                    % (name, rid, _clean(consequence)[:60]))
                    continue
            elif _has_col(r, "Tier") and not _has_col(r, "Route"):  # legacy format (Tier A/B/C)
                if not re.match(r"^[ABC]\b", tier):
                    problems.append("%s: %s: tier missing or unrecognized ('%s')" % (name, rid, tier))
                    continue
                consequential = tier.startswith("C")
                needed = r"\bR-\d+\b"
            else:
                problems.append("%s: %s: route missing or unrecognized ('%s')" % (name, rid, route))
                continue
            authority_pending = "pending" in authority.lower()
            refs = re.findall(r"\b(?:SA|R)-\d+\b", authority)
            if not authority_pending:
                for ref in refs:
                    if ref not in known and ref not in pending_ids:
                        problems.append("%s: %s cites %s, which does not exist in DECISIONS.md"
                                        % (name, rid, ref))
            if not consequential:
                continue
            when = _timing(timing_raw)
            usable = [x for x in refs if re.match(needed, x) and x in known]
            waiting = [x for x in refs if re.match(needed, x) and x in pending_ids]
            has_authority = bool(usable) and not authority_pending
            if (authority_pending or when == "pending" or waiting) and not has_authority:
                kind, msg = "PENDING", "%s: %s awaiting the PI's decision" % (name, rid)
                if waiting and not authority_pending:
                    msg += " (cites %s, which is still pending in DECISIONS.md)" % waiting[0]
            elif not has_authority:
                if route == "delegated" and re.search(r"\bR-\d+\b", authority):
                    why = ("the delegated route requires a standing authorization (SA-NN); a delegation "
                           "given in a ruling is recorded as an SA that cites the ruling (charter section 6)")
                elif route == "consult" and re.search(r"\bSA-\d+\b", authority):
                    why = "the consult route requires a ruling (R-NN), not a standing authorization"
                else:
                    why = "standing authorization (SA-NN)" if "SA" in needed else "ruling (R-NN)"
                problems.append("%s: consequential decision %s adopted without the required authority (%s)"
                                % (name, rid, why))
                continue
            elif when == "pending":
                kind, msg = "PENDING", "%s: %s authorization timing pending" % (name, rid)
            elif when is None:
                missing.append("%s: %s authorization timing not recorded ('%s')" % (name, rid, timing_raw))
                continue
            elif when == "late":
                if re.search(r"\bI-\d+\b", timing_raw + " " + authority):
                    kind, msg = "ADVISORY", "%s: %s ratified after adoption (recorded incident)" % (name, rid)
                else:
                    kind, msg = "FAIL", "%s: %s authorized after adoption, with no incident recorded" % (name, rid)
            else:
                kind, msg = "TIMELY", None
            outcome = _verdict(kind, msg, when == "late", bool(re.search(r"\bI-\d+\b", timing_raw + " " + authority)),
                               authority_pending, _entry(rid, needed, known, sections), name, rid)
            if outcome:
                {"PENDING": pending, "ADVISORY": advisories, "FAIL": problems,
                 "MISSING": missing}[outcome[0]].append(outcome[1])
    status = ("FAIL" if problems else "MISSING" if missing else "PENDING" if pending
              else "ADVISORY" if advisories else "PASS")
    step("Closed sprints: decision tracking and authorization", status,
         problems + missing + pending + advisories)


APPROVAL_ROWS = ("Approved plan", "Execution authorized by", "Transition policy")


def _part1_rows(text):
    """{row name: value} for Part 1's approval rows in a sprint record, outside HTML comments."""
    found = {}
    for line in re.sub(r"<!--.*?-->", "", text, flags=re.S).splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = split_row(line)
        for label in APPROVAL_ROWS:
            if len(cells) > 1 and _clean(cells[0]).lower() == label.lower() and label not in found:
                found[label] = cells[1]
    return found


PLAN_NAME = r"\bPLAN-\d{4}-\d{2}-\d{2}(?:-\d+)?\b"


def _plan_version(text):
    """(plan name, version number) named in text, e.g. ("PLAN-2026-10-18", "2"); None where absent."""
    m = re.search(PLAN_NAME, text)
    if not m:
        return None, None
    v = re.search(r"\bv(\d+)\b|\bversion\s+(\d+)\b", text[m.end():], re.I)
    return m.group(0), (v.group(1) or v.group(2)) if v else None


def _superseded_sas(sections):
    """{SA-NN: what supersedes it}, from its own "superseded by SA-NN" or another SA's Supersedes line."""
    found = {}
    for ident, body in sections.items():
        if not ident.startswith("SA-"):
            continue
        by = re.search(r"superseded by\s+[*`]*(SA-\d+)", body, re.I)
        if by:
            found[ident] = by.group(1)
        for old in re.findall(r"\bSA-\d+\b", _entry_line(body, "Supersedes")):
            if old != ident:
                found.setdefault(old, ident)
    return found


def _check_approved_plan(f, cell, known, sections, problems, missing, advisories):
    """The plan named in Part 1's Approved plan row exists, and a cited ruling approves that version."""
    plan, version = _plan_version(cell)
    if not plan or not version:
        missing.append("%s: Approved plan names no plan and version (PLAN-YYYY-MM-DD vN)" % f)
        return
    if not os.path.exists(os.path.join(ROOT, "reports", "planning", plan + ".md")):
        problems.append("%s: Approved plan names %s, which is not in reports/planning/" % (f, plan))
    if not re.search(r"\bR-\d+\b", cell):
        advisories.append("%s: Approved plan cites no ruling (R-NN); plan approval is a ruling (CORE section 5)" % f)
    rulings = [r for r in re.findall(r"\bR-\d+\b", cell) if r in known]
    named = {}
    for r in rulings:
        approves = _entry_line(sections.get(r, ""), "Approves")
        if approves:
            named[r] = _plan_version(approves)
        else:
            advisories.append("%s: %s has no Approves line; the plan version it approves is not checked" % (f, r))
    if named and (plan, version) not in named.values():
        r, (p, v) = sorted(named.items())[0]
        problems.append("%s: Approved plan is %s v%s, but %s approves %s v%s" % (f, plan, version, r, p, v))


def check_open_sprints():
    name = "Open sprints: plan approval and execution authority cited"
    d = os.path.join(ROOT, "reports", "sprints")
    names = sorted(os.listdir(d)) if os.path.isdir(d) else []
    planning = os.path.join(ROOT, "reports", "planning")
    problems, missing, pending, advisories, checked = [], [], [], [], 0
    known, pending_ids, sections = decision_index()
    superseded = _superseded_sas(sections)
    for f in names:
        if not f.endswith(".md"):
            continue
        text = read(os.path.join("reports", "sprints", f))
        if not _is_open(text):
            continue  # closed: checked by check_sprints
        rows = _part1_rows(text)
        if not rows:
            advisories.append("%s: older format; plan approval not recorded in Part 1" % f)
            continue
        checked += 1
        for label in APPROVAL_ROWS:
            if label not in rows:
                if label != "Transition policy":
                    advisories.append("%s: no \"%s\" row in Part 1" % (f, label))
                continue
            refs = re.findall(r"\b(?:SA|R)-\d+\b", rows[label])
            if not refs and label != "Transition policy":
                missing.append("%s: %s cites no ruling or standing authorization (R-NN / SA-NN)" % (f, label))
            for ref in refs:
                if ref in pending_ids:
                    pending.append("%s: %s cites %s, which is still pending in DECISIONS.md" % (f, label, ref))
                elif ref not in known:
                    problems.append("%s: %s cites %s, which does not exist in DECISIONS.md" % (f, label, ref))
                elif ref in superseded:
                    # Part 1 is frozen once the sprint starts, so this cannot be a FAIL
                    advisories.append("%s: %s cites %s, which is superseded by %s; check whether continuation is "
                                      "still authorized (the SA was changed or withdrawn)"
                                      % (f, label, ref, superseded[ref]))
                elif label == "Execution authorized by" and ref.startswith("R-") and re.match(
                        r"^\W*no\b", _clean(_entry_line(sections.get(ref, ""), "Execution authorized")), re.I):
                    problems.append("%s: %s cites %s, whose Execution authorized line says no: a planning-only "
                                    "approval does not start work" % (f, label, ref))
        if "Approved plan" in rows:
            _check_approved_plan(f, rows["Approved plan"], known, sections, problems, missing, advisories)
    for f in sorted(os.listdir(planning)) if os.path.isdir(planning) else []:
        if f.endswith(".md"):
            text = re.sub(r"<!--.*?-->", "", read(os.path.join("reports", "planning", f)), flags=re.S)
            for ref in sorted(set(re.findall(r"approved by\s+[*`]*(R-\d+)\b", text, re.I))):
                if ref not in known:
                    advisories.append("reports/planning/%s: marked approved by %s, which %s in DECISIONS.md" % (
                        f, ref, "is still pending" if ref in pending_ids else "does not exist"))
    if checked:
        not_checked.append("open sprints: whether the cited ruling or SA covers that sprint's scope, and "
                           "whether the approved plan file still matches the commit its ruling names")
    status = ("FAIL" if problems else "MISSING" if missing else "PENDING" if pending
              else "ADVISORY" if advisories else "PASS")
    details = problems + missing + pending + advisories
    step(name, status, details or ["no open sprint records" if not checked else "cited authority exists"])


MAP_STEP = "START-HERE map covers top level; listed paths exist (advisory)"


def _project_map():
    """(file, text) of the project's map: START-HERE.md's "## Map" section, else a legacy INDEX.md
    (the whole file); (None, reason) when there is none."""
    if os.path.exists(os.path.join(ROOT, "START-HERE.md")):
        m = re.search(r"^##\s+Map\b[^\n]*\n(.*?)(?=^##\s|\Z)", read("START-HERE.md"), re.S | re.M)
        if m:
            return "START-HERE.md", m.group(1)
    if os.path.exists(os.path.join(ROOT, "INDEX.md")):
        return "INDEX.md", read("INDEX.md")
    if os.path.exists(os.path.join(ROOT, "START-HERE.md")):
        return None, "START-HERE.md has no '## Map' section"
    return None, "START-HERE.md absent"


def _listed_paths(line):
    """Paths a map line lists: backticked paths in a table row's first column, or the first backticked
    path on a bullet line."""
    s = line.strip()
    if s.startswith("|"):
        return re.findall(r"`([^`]+)`", split_row(line)[0])
    if re.match(r"^[-*+]\s", s):
        m = re.search(r"`([^`]+)`", s)
        return [m.group(1)] if m else []
    return []


def check_map():
    where, text = _project_map()
    if where is None:
        step(MAP_STEP, "MISSING", [text])
        return
    notes = ["not mentioned: " + e for e in sorted(os.listdir(ROOT))
             if not e.startswith(".") and e not in SKIP_DIRS and e != where and e not in text]
    for line in text.splitlines():
        if re.search(r"pending:|git-ignored", line, re.I):
            continue
        for path in _listed_paths(line):
            path = path.strip()
            if "{{" in path or "*" in path or "<" in path or re.match(r"^[a-z]+:", path):
                continue
            if not os.path.exists(os.path.join(ROOT, path.rstrip("/"))):
                notes.append("listed but does not exist: " + path)
    if where == "INDEX.md":
        notes_ok = ["map read from INDEX.md (a project set up before v0.6)"]
    else:
        notes_ok = []
    step(MAP_STEP, "ADVISORY" if notes else "PASS", notes + notes_ok if notes else notes_ok)


def _not_installed_decision(phrase):
    """A decision in DECISIONS.md recording `phrase` (e.g. "event logging not installed"), citing a
    ruling (R-NN) or the routine route; or None."""
    _, _, sections = decision_index()
    for ident, body in sections.items():
        text = " ".join(_clean(body).split()).lower()
        if ident.startswith("DEC-") and phrase in text and re.search(r"\br-\d+\b|\broute:\s*routine\b", text):
            return ident
    return None


HOOK_REF = re.compile(r"(arpd\W{1,4})?tools\W{1,4}hooks\W{1,4}log_hook\.py")


def check_logging():
    name = "Event logging and agent roles installed"
    gaps, fails, advisories = [], [], []
    settings = os.path.join(".claude", "settings.json")
    if not os.path.exists(os.path.join(ROOT, settings)):
        gaps.append(("event logging not installed", ".claude/settings.json is missing"))
    elif not HOOK_REF.search(read(settings).replace("\\", "/")):
        gaps.append(("event logging not installed", ".claude/settings.json does not run arpd/tools/hooks/log_hook.py"))
    else:
        # The script each hook runs (a plain path or the fail-safe launcher's), relative to the project root.
        scripts = {"arpd/tools/hooks/log_hook.py" if m.group(1) else "tools/hooks/log_hook.py"
                   for m in HOOK_REF.finditer(read(settings).replace("\\", "/"))}
        for rel in sorted(scripts):
            if not os.path.isfile(os.path.join(ROOT, *rel.split("/"))):
                fails.append(".claude/settings.json runs %s, which does not exist: every prompt may be blocked; run "
                             "python arpd/tools/install.py owed . --kit <kit>" % rel)
        if re.search(r'"disableAllHooks"\s*:\s*true', read(settings)):
            gaps.append(("event logging not installed", ".claude/settings.json sets disableAllHooks: true"))
    team = ""
    if os.path.exists(os.path.join(ROOT, "CLAUDE.md")):
        m = re.search(r"\*\*Team arrangement:\*\*([^\n]*)", read("CLAUDE.md"))
        team = m.group(1).lower() if m else ""
    if ("subagent" in team or "peer" in team) and "solo" not in team:
        for role in ("implementer", "reviewer"):
            here, kit = (os.path.join(ROOT, d, "agents", role + ".md") for d in (".claude", "arpd"))
            if not os.path.exists(here):
                gaps.append(("agent files not installed", ".claude/agents/%s.md is missing (team arrangement "
                             "needs it)" % role))
            elif os.path.isfile(kit) and read(here) != read(kit):
                advisories.append(".claude/agents/%s.md differs from arpd/agents/%s.md (an older or edited copy; "
                                  "python arpd/tools/install.py owed . --force replaces it)" % (role, role))
    if not gaps:
        step(name, "FAIL" if fails else ("ADVISORY" if advisories else "PASS"), fails + advisories)
        return
    notes, unexplained = [], False
    for phrase, what in gaps:
        dec = _not_installed_decision(phrase)
        if dec:
            notes.append("%s; recorded as not installed in %s" % (what, dec))
        else:
            notes.append("%s; no decision records it as not installed" % what)
            unexplained = True
    step(name, "FAIL" if fails else ("MISSING" if unexplained else "ADVISORY"), fails + notes + advisories)


SKILLS = ("arpd-checkin", "arpd-amend", "arpd-plan")


def check_skills():
    name = "ARPD skills installed"
    missing = []
    for skill in SKILLS:
        if not os.path.exists(os.path.join(ROOT, ".claude", "skills", skill, "SKILL.md")):
            missing.append(".claude/skills/%s/SKILL.md is missing" % skill)
    if not missing:
        step(name, "PASS")
        return
    dec = _not_installed_decision("skills not installed")
    if dec:
        step(name, "ADVISORY", ["%s; recorded as not installed in %s" % (m, dec) for m in missing])
    else:
        step(name, "MISSING", ["%s; no decision records it as not installed" % m for m in missing])


SPEC_ID = r"\b(?:CON|OP|INV|CLM|NCL|VAL|ASM|Q)-\d+\b"


def _superseded_items():
    """{spec ID: what supersedes it} for PARADIGM-SPEC.md table rows that say "Superseded by"."""
    if not os.path.exists(os.path.join(ROOT, "PARADIGM-SPEC.md")):
        return {}
    text = re.sub(r"<!--.*?-->", "", read("PARADIGM-SPEC.md"), flags=re.S)
    found = {}
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        m = re.match(r"^[*`\s]*(" + SPEC_ID + ")", split_row(line)[0])
        by = re.search(r"superseded by\s+[*`]*([A-Z]+-\d+)", line, re.I)
        if m and by:
            found[m.group(1)] = by.group(1)
    return found


def _table_items(path, id_pattern):
    """(ID, cells) for each table row in `path` whose first cell is an ID; retired rows are left out."""
    if not os.path.exists(os.path.join(ROOT, path)):
        return
    text = re.sub(r"<!--.*?-->", "", read(path), flags=re.S)
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = split_row(line)
        m = re.match(r"^[*`\s]*(" + id_pattern + r")\b", cells[0])
        if m and not any(_clean(c).lower() == "retired" for c in cells):
            yield m.group(1), cells


def check_superseded():
    name = "Live items cite no superseded spec item (advisory)"
    old = _superseded_items()
    if not old:
        step(name, "PASS")
        return
    cites = []   # (file, item ID, the text that may cite a superseded item)
    if os.path.exists(os.path.join(ROOT, "REQUIREMENTS.md")):
        for r in table_rows(read("REQUIREMENTS.md"), "ID"):
            if MALFORMED not in r and r.get("ID") and r.get("State") != "Retired":
                cites.append(("REQUIREMENTS.md", r["ID"], r.get("Source", "")))
    for aid, cells in _table_items("ARCHITECTURE.md", r"A-\d+"):
        cites.append(("ARCHITECTURE.md", aid, " ".join(cells[1:])))
    for cid, cells in _table_items("PARADIGM-SPEC.md", r"CLM-\d+"):
        cites.append(("PARADIGM-SPEC.md", cid, " ".join(cells[1:])))
    _, _, sections = decision_index()
    for ident, body in sections.items():
        if ident.startswith("SA-") and not re.search(r"superseded by\s+[*`]*SA-\d+", body, re.I):
            cites.append(("DECISIONS.md", ident, body))
    notes = []
    for where, item, text in cites:
        for ref in sorted(set(re.findall(SPEC_ID, text))):
            if ref in old and item not in old:
                notes.append("%s %s cites %s, which is superseded by %s" % (where, item, ref, old[ref]))
    step(name, "ADVISORY" if notes else "PASS", notes)



def check_readiness():
    """Advisory: STATUS Readiness's Execution line against the sprint records. Nothing more."""
    name = "Readiness agrees with the sprint records (advisory)"
    if not os.path.exists(os.path.join(ROOT, "STATUS.md")):
        return
    status = read("STATUS.md")
    m = re.search(r"^## Readiness\b(.*?)(?=^## )", status, re.S | re.M)
    if not m:
        step(name, "PASS", ["no Readiness block in STATUS.md (older format); not compared"])
        return
    ex = re.search(r"Execution:\**\s*(.+)", m.group(1))
    execution = ex.group(1).strip().lower() if ex else ""
    d = os.path.join(ROOT, "reports", "sprints")
    open_records = [f for f in (sorted(os.listdir(d)) if os.path.isdir(d) else [])
                    if f.endswith(".md") and _is_open(read(os.path.join("reports", "sprints", f)))]
    notes = []
    if open_records and "not started" in execution:
        notes += ["%s is open, but STATUS Readiness says execution: not started" % f for f in open_records]
    if not open_records and "in progress" in execution:
        notes.append("STATUS Readiness says execution: in progress, but no sprint record is open")
    step(name, "ADVISORY" if notes else "PASS", notes or ["Execution line consistent with the sprint records"])

STEPS = (
    (check_exists, "Governing documents exist"),
    (check_adoption, "Charter adopted; templates filled"),
    (check_adopted_report, "Adopted blueprint traced (advisory)"),
    (check_links, "Intra-repo links resolve"),
    (check_requirements, "Requirements: states, evidence, traceability"),
    (check_requirement_details, "Requirement details: acceptance criteria (advisory)"),
    (check_plans, "Plans: unique numbers, valid status"),
    (check_sprints, "Closed sprints: decision tracking and authorization"),
    (check_open_sprints, "Open sprints: plan approval and execution authority cited"),
    (check_readiness, "Readiness agrees with the sprint records (advisory)"),
    (check_map, MAP_STEP),
    (check_logging, "Event logging and agent roles installed"),
    (check_skills, "ARPD skills installed"),
    (check_superseded, "Live items cite no superseded spec item (advisory)"),
)


def main():
    if os.path.exists(os.path.join(ROOT, KIT_MARKER)):
        print("This is the ARPD kit, not a project; run setup to create a project.")
        sys.exit(2)
    version = os.path.join(ROOT, "arpd", "VERSION")
    if os.path.isfile(version):
        try:
            first = (read(os.path.join("arpd", "VERSION")).splitlines() or [""])[0].strip()
        except NotUTF8:
            first = ""
        if first:
            print(first + "\n")
    for fn, title in STEPS:
        try:
            fn()
        except NotUTF8 as exc:  # a file the step read is not UTF-8: say which, never crash
            step(title, "FAIL", ["%s: not UTF-8 (save as UTF-8)" % exc.path])
        except Exception as exc:  # report, never hide
            step(title, "MISSING", ["check could not run: %r" % exc])
    width = max(len(n) for n, _, _ in results)
    for name, status, details in results:
        print("%-*s  %s" % (width, name, status))
        for d in details:
            print("    - " + d)
    print("\nNot checked:")
    for d in not_checked + [
            "dates, rulings and authorizations are checked as recorded, not verified as true or as the PI's "
            "own words",
            "whether a plan approval or start direction was the PI's own words",
            "STATUS readiness flags beyond the Execution line (setup, planning, next step) and START-HERE.md are not checked against the records",
            "installation checks look at files, not at whether the hooks actually fired",
            "that the adopted blueprint's content matches the governing documents (only its ruling and version are "
            "traced)",
            "the code itself: run the project's tests separately"]:
        print("    - " + d)
    print("Relies on recorded information in DECISIONS.md, sprint records, REQUIREMENTS.md and START-HERE.md's "
          "map (INDEX.md in older projects).")
    statuses = {s for _, s, _ in results}
    overall = "FAIL" if "FAIL" in statuses else ("INCOMPLETE" if statuses & {"MISSING", "PENDING"} else "PASS")
    print("\nOVERALL: " + overall)
    sys.exit({"PASS": 0, "FAIL": 1, "INCOMPLETE": 2}[overall])


if __name__ == "__main__":
    main()
