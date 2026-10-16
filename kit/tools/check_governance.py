#!/usr/bin/env python3
"""Governance checks for an ARPD project.

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
2. Intra-repository Markdown links resolve.
3. Requirements:
   - states are valid;
   - Verified and Validated rows carry evidence;
   - Validated rows cite a ruling (R-NN);
   - sources point to items that exist in PARADIGM-SPEC.md or DECISIONS.md.
4. Plans: unique numbers, valid status.
5. Closed sprint records:
   - have a decision-tracking table;
   - every consequential decision cites its authority: a standing authorization (SA-NN) for the
     delegated route, a ruling (R-NN) for the consult route. One still awaiting a decision makes
     the result INCOMPLETE (PENDING);
   - none was authorized after adoption, unless it was ratified and recorded as an incident
     (I-NN), which is ADVISORY. Legacy records using "Tier C" columns are read as the consult
     route.
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


def table_rows(text, header_startswith):
    """Yield dict rows of the first Markdown table whose header starts with header_startswith."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip().startswith("|") and line.strip("| ").lower().startswith(header_startswith.lower()):
            headers = [h.strip() for h in line.strip().strip("|").split("|")]
            for row in lines[i + 2:]:
                if not row.strip().startswith("|"):
                    return
                cells = [c.strip() for c in row.strip().strip("|").split("|")]
                if len(cells) == len(headers):
                    yield dict(zip(headers, cells))
            return


def check_exists():
    missing = [f for f in GOVERNING if not os.path.exists(os.path.join(ROOT, f))]
    step("Governing documents exist", "FAIL" if missing else "PASS", ["missing: " + m for m in missing])


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


def check_sprints():
    d = os.path.join(ROOT, "reports", "sprints")
    if not os.path.isdir(d):
        step("Closed sprints: decision tracking and authorization", "PASS", ["no sprint records yet"])
        return
    problems, pending, advisories = [], [], []
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
            rid = r.get("ID", "?")
            route = _col(r, "Route").strip().lower()
            tier = _col(r, "Tier").strip().upper()
            authority = _col(r, "Authority", "Decided by")
            timing_raw = _col(r, "Authorized before adoption", "Before or after commit")
            timing = timing_raw.lower()
            if route:
                consequential = route.startswith("delegated") or route.startswith("consult")
                needed = r"\bSA-\d+\b" if route.startswith("delegated") else r"\bR-\d+\b"
            else:  # legacy format (Tier A/B/C)
                consequential = tier.startswith("C")
                needed = r"\bR-\d+\b"
            if not consequential:
                continue
            is_pending = "pending" in authority.lower() or "pending" in timing
            has_authority = bool(re.search(needed, authority)) and "pending" not in authority.lower()
            if is_pending and not has_authority:
                pending.append("%s: %s awaiting the PI's decision" % (name, rid))
                continue
            if not has_authority:
                problems.append("%s: consequential decision %s adopted without the required authority (%s)"
                                % (name, rid, "standing authorization" if "SA" in needed else "ruling"))
                continue
            late = timing.startswith("no") or "after" in timing
            if late:
                if re.search(r"\bI-\d+\b", timing_raw + " " + authority):
                    advisories.append("%s: %s ratified after adoption (recorded incident)" % (name, rid))
                else:
                    problems.append("%s: %s authorized after adoption, with no incident recorded" % (name, rid))
    status = "FAIL" if problems else ("PENDING" if pending else ("ADVISORY" if advisories else "PASS"))
    step("Closed sprints: decision tracking and authorization", status, problems + pending + advisories)


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
    for fn in (check_exists, check_links, check_requirements, check_plans, check_sprints, check_index):
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
