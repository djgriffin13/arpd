#!/usr/bin/env python3
r"""Governance checks for an ARPD project.

    python tools/check_governance.py

Each step reports PASS, FAIL, MISSING (could not run), PENDING (awaiting
the PI's ruling) or ADVISORY. The overall result is:

- PASS only if every step passed;
- INCOMPLETE if any step could not run;
- FAIL otherwise.

It never reports PASS for something it did not check.

Exit codes: 0 PASS, 1 FAIL, 2 INCOMPLETE.

The checks:

1. The governing documents exist.
   Charter adopted; templates filled: an unfilled {{...}} placeholder outside HTML comments in a
   governing document is a FAIL; a charter still marked "Pending adoption" is PENDING.
2. Intra-repository Markdown links resolve.
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
     a ruling (R-NN) for the consult route. Every SA-NN and R-NN cited must exist in DECISIONS.md.
     One still awaiting a decision makes the result INCOMPLETE (PENDING);
   - each consequential decision records whether it was authorized before adoption (first word
     yes / before, no / after, or pending). Not recorded makes the result INCOMPLETE (MISSING).
     Authorized after adoption is ADVISORY if ratified and recorded as an incident (I-NN), and a
     FAIL otherwise.
6. INDEX.md mentions every top-level entry (advisory).
"""
import io
import os
import re
import sys

ROOT = "."
GOVERNING = ["CLAUDE.md", "PARADIGM-SPEC.md", "REQUIREMENTS.md", "MASTER_PLAN.md", "DECISIONS.md",
             "ARCHITECTURE.md", "STATUS.md", "INDEX.md"]
REQ_STATES = {"Planned", "Implemented", "Verified", "Validated", "Retired"}
PLAN_STATES = {"Proposed", "Approved", "Active", "Complete"}
SKIP_DIRS = {".git", "node_modules", "__pycache__", "logs", "output", ".venv", "venv", "kit"}

results = []


def step(name, status, details=()):
    results.append((name, status, list(details)))


def read(path):
    with io.open(os.path.join(ROOT, path), encoding="utf-8") as fh:
        return fh.read()


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
    missing = [f for f in GOVERNING if not os.path.exists(os.path.join(ROOT, f))]
    step("Governing documents exist", "FAIL" if missing else "PASS", ["missing: " + m for m in missing])


def check_adoption():
    unfilled = []
    for f in GOVERNING:
        if not os.path.exists(os.path.join(ROOT, f)):
            continue  # reported by check_exists
        text = re.sub(r"<!--.*?-->", "", read(f), flags=re.S)
        for ph in sorted(set(re.findall(r"\{\{[^{}]*\}\}", text))):
            unfilled.append("%s: unfilled placeholder %s" % (f, ph[:60]))
    pending = (os.path.exists(os.path.join(ROOT, "CLAUDE.md"))
               and "pending adoption" in read("CLAUDE.md").lower())
    notes = unfilled + (["CLAUDE.md: the charter is pending adoption (no adoption ruling recorded yet)"]
                        if pending else [])
    step("Charter adopted; templates filled", "FAIL" if unfilled else ("PENDING" if pending else "PASS"), notes)


def check_links():
    bad = []
    for f in md_files():
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


def check_plans():
    d = os.path.join(ROOT, "plans")
    if not os.path.isdir(d):
        step("Plans", "MISSING", ["plans/ absent"])
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


def decision_ids():
    """SA-NN and R-NN entries that exist in DECISIONS.md: as a heading, or as a table row's first cell."""
    if not os.path.exists(os.path.join(ROOT, "DECISIONS.md")):
        return set()
    found = set()
    for line in read("DECISIONS.md").splitlines():
        s = line.strip()
        m = None
        if s.startswith("#"):
            m = re.match(r"^#+\s*[*`]*((?:SA|R)-\d+)\b", s)
        elif s.startswith("|"):
            m = re.match(r"^[*`\s]*((?:SA|R)-\d+)\b", split_row(s)[0])
        if m:
            found.add(m.group(1))
    return found


def check_sprints():
    d = os.path.join(ROOT, "reports", "sprints")
    if not os.path.isdir(d):
        step("Closed sprints: decision tracking and authorization", "PASS", ["no sprint records yet"])
        return
    problems, missing, pending, advisories = [], [], [], []
    known = decision_ids()
    for name in sorted(os.listdir(d)):
        if not name.endswith(".md"):
            continue
        text = read(os.path.join("reports", "sprints", name))
        if "**Closed:**" not in text or "{{date" in text.split("**Closed:**", 1)[1][:80]:
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
            if not authority_pending:
                for ref in re.findall(r"\b(?:SA|R)-\d+\b", authority):
                    if ref not in known:
                        problems.append("%s: %s cites %s, which does not exist in DECISIONS.md"
                                        % (name, rid, ref))
            if not consequential:
                continue
            when = _timing(timing_raw)
            has_authority = bool(re.search(needed, authority)) and not authority_pending
            if (authority_pending or when == "pending") and not has_authority:
                pending.append("%s: %s awaiting the PI's decision" % (name, rid))
                continue
            if not has_authority:
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
            if when == "pending":
                pending.append("%s: %s authorization timing pending" % (name, rid))
            elif when is None:
                missing.append("%s: %s authorization timing not recorded ('%s')" % (name, rid, timing_raw))
            elif when == "late":
                if re.search(r"\bI-\d+\b", timing_raw + " " + authority):
                    advisories.append("%s: %s ratified after adoption (recorded incident)" % (name, rid))
                else:
                    problems.append("%s: %s authorized after adoption, with no incident recorded" % (name, rid))
    status = ("FAIL" if problems else "MISSING" if missing else "PENDING" if pending
              else "ADVISORY" if advisories else "PASS")
    step("Closed sprints: decision tracking and authorization", status,
         problems + missing + pending + advisories)


def check_index():
    if not os.path.exists(os.path.join(ROOT, "INDEX.md")):
        step("INDEX covers top level (advisory)", "MISSING", ["INDEX.md absent"])
        return
    idx = read("INDEX.md")
    missing = [e for e in sorted(os.listdir(ROOT))
               if not e.startswith(".") and e not in SKIP_DIRS and e not in idx]
    step("INDEX covers top level (advisory)", "PASS" if not missing else "ADVISORY",
         ["not mentioned: " + m for m in missing])


def main():
    for fn in (check_exists, check_adoption, check_links, check_requirements, check_plans, check_sprints, check_index):
        try:
            fn()
        except Exception as exc:  # report, never hide
            step(fn.__name__, "MISSING", ["check could not run: %r" % exc])
    width = max(len(n) for n, _, _ in results)
    for name, status, details in results:
        print("%-*s  %s" % (width, name, status))
        for d in details:
            print("    - " + d)
    statuses = {s for _, s, _ in results}
    overall = "FAIL" if "FAIL" in statuses else ("INCOMPLETE" if statuses & {"MISSING", "PENDING"} else "PASS")
    print("\nOVERALL: " + overall)
    sys.exit({"PASS": 0, "FAIL": 1, "INCOMPLETE": 2}[overall])


if __name__ == "__main__":
    main()
