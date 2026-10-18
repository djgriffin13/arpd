#!/usr/bin/env python3
"""Print the next free plan number (NNN).

It scans plans/ in the working tree and on every local and remote branch, so that agents working in
parallel worktrees never claim the same number.

    python arpd/tools/next_plan_number.py      (from the project root)
"""
import os
import re
import subprocess

PAT = re.compile(r"(?:^|/)plans/(\d{3})-[^/]+\.md$")


def numbers_in_tree(root="."):
    found = set()
    d = os.path.join(root, "plans")
    if os.path.isdir(d):
        for name in os.listdir(d):
            m = PAT.search("plans/" + name)
            if m:
                found.add(int(m.group(1)))
    return found


def numbers_on_branches():
    found = set()
    try:
        refs = subprocess.run(["git", "for-each-ref", "--format=%(refname)", "refs/heads", "refs/remotes"],
                              capture_output=True, text=True, check=True).stdout.split()
    except Exception:
        return found
    for ref in refs:
        try:
            out = subprocess.run(["git", "ls-tree", "-r", "--name-only", ref, "--", "plans/"],
                                 capture_output=True, text=True, check=True).stdout
        except Exception:
            continue
        for line in out.splitlines():
            m = PAT.search(line)
            if m:
                found.add(int(m.group(1)))
    return found


if __name__ == "__main__":
    used = numbers_in_tree() | numbers_on_branches()
    print("%03d" % (max(used) + 1 if used else 1))
