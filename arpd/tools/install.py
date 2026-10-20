#!/usr/bin/env python3
"""Create, convert, import, install, update or repair an ARPD project from the kit.

    python arpd/tools/install.py convert <path> [--yes]          (run in a fresh kit clone)
    python arpd/tools/install.py new <path>                      (run from the kit clone)
    python arpd/tools/install.py import <source> <path> [--yes]  (run from the kit clone)
    python arpd/tools/install.py install <path> [--force] [--notes <path>]  (run from the kit clone)
    python arpd/tools/install.py update <path> [--kit <kit>] [--prune]
    python arpd/tools/install.py owed <path> [--kit <kit>] [--force]

A fresh kit clone becomes the project in place with convert (a fresh git history, no remote); new,
import and install create or prepare a project elsewhere, in its own git repository. Everything from
the kit goes into the project's arpd/ folder, except the skills (.claude/skills/arpd-*), which Claude
Code needs in .claude/.

convert  Turn a fresh kit clone (or a downloaded, unzipped kit) into the research project, in the same
         folder. The kit-development material named in the .arpd-kit manifest (the kit's README,
         CLAUDE.md, docs/, tests/, evaluation/, ...) is removed; arpd/ and .claude/skills/arpd-* are
         kept, and so is everything else, which is the PI's. In a git clone only files the kit's commit
         holds are removed: files the PI added under those folders, and kit files the PI changed, are
         kept and listed. The plan is printed first and nothing changes without --yes. Before anything
         is deleted, work that is on no remote (local commits, stashes) is saved to a verified git
         bundle beside the folder. Then the kit's history and remote are removed, a fresh repository
         (branch main) is started, environments and files of 50 MB or more are git-ignored, the stub
         CLAUDE.md and arpd/VERSION are written, and everything is committed once. Needs git with
         user.name and user.email set.

new      Create an empty project folder with its own git repository: the arpd/ payload, the skills, a
         .gitignore, a stub CLAUDE.md ("setup in progress") and arpd/VERSION, committed. Refuses a
         folder that exists and is not empty, or one inside the kit. Warns (does not refuse) when the
         folder is under OneDrive, below a folder holding CLAUDE.md or AGENTS.md, or inside another git
         repository. Needs git with user.name and user.email set.
import   Start a new project from existing code. A git source (a path or URL) is cloned with its
         history and submodules; its origin remote is renamed "upstream" and its push URL disabled,
         so the project can fetch from it but never pushes back. A plain folder is listed first
         (large files, environments, data-like files) and copied only with --yes; environments
         (.venv, node_modules, ...) are not copied, and files of 50 MB or more are git-ignored. The
         copied code is committed alone ("Import <source> (no changes)"). Then as for new (the stub
         CLAUDE.md only if the source has none), committed.
install  Add ARPD to an existing repository in place. An existing file that differs is never
         overwritten without --force (it is reported as a conflict). --notes names where the setup
         notes are kept (outside the repository) in the stub CLAUDE.md, or prints the line when a
         CLAUDE.md exists. Nothing is committed.
update   Refresh arpd/ (keeping arpd/logs/) and .claude/skills/arpd-* from the kit, and print what
         changed. Files no longer in the kit are listed, and removed only with --prune. Nothing is
         committed.
owed     Install what setup owes: arpd/settings/settings.json as .claude/settings.json (into an
         existing one, only its "hooks" key is merged, replacing earlier ARPD log-hook entries),
         arpd/agents/*.md into .claude/agents/, and any missing ARPD skill (needs the kit). The hook
         commands use "python" if it is on the PATH, else "python3", else this interpreter's path, and
         run the script through a launcher that exits 0 when it is missing (exit 2 would block prompts).

The kit is the folder that holds this script's arpd/ when that folder has the .arpd-kit marker
(running the kit clone's copy); a project's own copy needs --kit <path to the kit clone>.

Exit codes: 0 done; 1 refused or failed; 2 done, with conflicts or items left to the PI (listed).
Standard library only; Python 3.8+.
"""
import argparse
import datetime
import filecmp
import io
import json
import os
import re
import shutil
import stat
import subprocess
import sys

KIT_MARKER = ".arpd-kit"
PAYLOAD = "arpd"
FALLBACK_VERSION = "v0.7.0-rc.1"  # used when the kit's RELEASE-NOTES.md names no version
# Kit-development material that convert removes, when the .arpd-kit manifest lists none (older kits).
DEFAULT_MANIFEST = (".arpd-kit", "AGENTS.md", "CITATION.cff", "CLAUDE.md", "LICENSE", "README.md",
                    "RELEASE-NOTES.md", ".gitattributes", ".gitignore", "docs/", "evaluation/", "tests/")
CACHE_DIRS = {"__pycache__", ".pytest_cache", ".mypy_cache"}  # debris convert removes from kit folders
PAYLOAD_SKIP_DIRS = {"logs", "__pycache__", ".pytest_cache"}
PAYLOAD_SKIP_ROOT_FILES = {"VERSION"}
GITIGNORE_LINES = ["arpd/logs/", "output/", "__pycache__/", ".claude/settings.local.json"]
NOTES = "reports/setup/NOTES.md"


def stub_claude(notes=NOTES):
    return ("# Setup in progress\nThis project is being set up with ARPD. Run /arpd-setup to continue; the "
            "working notes are in %s. Do not build anything until setup is complete.\n" % notes)


STUB_CLAUDE = stub_claude()
DEFAULT_SKILLS = ("arpd-setup", "arpd-plan", "arpd-checkin", "arpd-amend")
ENV_DIRS = {".venv", "venv", "node_modules", "__pycache__", ".pytest_cache", ".mypy_cache", ".ipynb_checkpoints"}
DATA_EXT = {".csv", ".tsv", ".xlsx", ".xls", ".parquet", ".feather", ".h5", ".hdf5", ".sav", ".dta", ".rds",
            ".rdata", ".pkl", ".pickle", ".npy", ".npz", ".mat", ".db", ".sqlite", ".zip", ".gz", ".tar",
            ".7z", ".jsonl"}
LARGE_MB = 10       # listed in the inventory
IGNORE_MB = 50      # git-ignored on a folder import (git hosts warn at 50 MB and refuse at 100 MB)
LIST_MAX = 20


class Refused(Exception):
    pass


def say(msg=""):
    print(msg)


def warn(msg):
    print("WARNING: " + msg)


# --- the kit ------------------------------------------------------------------------------------

def is_kit(root):
    return bool(root) and os.path.isfile(os.path.join(root, KIT_MARKER)) and os.path.isdir(os.path.join(root, PAYLOAD))


def find_kit(arg):
    root = os.path.abspath(arg) if arg else os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    return root if is_kit(root) else None


def require_kit(arg):
    kit = find_kit(arg)
    if kit:
        return kit
    if arg:
        raise Refused("%s is not the ARPD kit (no %s marker and arpd/ folder there)" % (arg, KIT_MARKER))
    raise Refused("cannot find the ARPD kit from this copy of install.py; pass --kit <path to the kit clone>")


def kit_version(kit):
    try:
        with io.open(os.path.join(kit, "RELEASE-NOTES.md"), encoding="utf-8") as fh:
            first = fh.readline()
        m = re.search(r"\bv\d+\.\d+\.\d+(?:-[0-9A-Za-z.]+)?", first)
        if m:
            return m.group(0)
    except (IOError, OSError, UnicodeDecodeError):
        pass
    return FALLBACK_VERSION


def kit_commit(kit, untracked=True):
    """The kit's HEAD commit, noting uncommitted changes (to tracked files only, when not untracked)."""
    p = git(["rev-parse", "HEAD"], kit, check=False)
    if p.returncode != 0:
        return "unknown (the kit is not a git clone)"
    sha = p.stdout.strip()
    dirty = git(["status", "--porcelain"] + ([] if untracked else ["--untracked-files=no"]), kit, check=False)
    return sha + (" with uncommitted changes" if dirty.returncode == 0 and dirty.stdout.strip() else "")


def kit_manifest(root):
    """The top-level paths of kit-development material (without a trailing /) listed in the .arpd-kit
    marker: one per line; blank lines, # comments and prose lines (with spaces) are skipped. Entries
    that are not plain top-level kit paths (the payload, .claude, .git, absolute or ..) are dropped.
    Falls back to DEFAULT_MANIFEST when the marker lists none (an older kit)."""
    try:
        lines = io.open(os.path.join(root, KIT_MARKER), encoding="utf-8").read().splitlines()
    except (IOError, OSError, UnicodeDecodeError):
        lines = []
    out = []
    for line in lines:
        e = line.strip().replace("\\", "/").rstrip("/")
        if not e or e.startswith("#") or re.search(r"\s", e):
            continue
        top = e.split("/")[0]
        if os.path.isabs(e) or ".." in e.split("/") or top in (PAYLOAD, ".claude", ".git", ""):
            continue
        if e not in out:
            out.append(e)
    return out or [e.rstrip("/") for e in DEFAULT_MANIFEST]


# --- git ------------------------------------------------------------------------------------------

def git(args, cwd, check=True, env=None):
    try:
        p = subprocess.run(["git"] + list(args), cwd=cwd, capture_output=True, text=True, env=env)
    except OSError:
        raise Refused("git is not installed or not on PATH; install it from https://git-scm.com and rerun")
    if check and p.returncode != 0:
        raise Refused("git %s failed: %s" % (" ".join(args), (p.stderr or p.stdout).strip()))
    return p


def check_git(cwd):
    git(["--version"], cwd)
    name = git(["config", "--get", "user.name"], cwd, check=False).stdout.strip()
    email = git(["config", "--get", "user.email"], cwd, check=False).stdout.strip()
    if not (name and email):
        missing = [k for k, v in (("user.name", name), ("user.email", email)) if not v]
        raise Refused("git does not know who you are (%s not set). Run, with your own details:\n"
                      "    git config --global user.name \"Your Name\"\n"
                      "    git config --global user.email \"you@example.edu\"\n"
                      "then rerun this command." % " and ".join(missing))


def git_init(path):
    if git(["init", "-q", "-b", "main"], path, check=False).returncode != 0:
        git(["init", "-q"], path)
        git(["symbolic-ref", "HEAD", "refs/heads/main"], path)


def commit_all(path, message, exclude=(), force_add=False):
    """Stage everything (minus `exclude`) and commit. force_add also stages arpd/ and the ARPD skills
    even if a .gitignore excludes them."""
    git(["add", "-A", "--", "."] + [":(exclude,literal)" + x for x in exclude], path)
    if force_add:
        skills = [".claude/skills/" + x for x in kit_skills(path)]
        git(["add", "-f", "--", PAYLOAD] + skills + [":(exclude)arpd/logs", ":(exclude)**/__pycache__"], path)
    p = git(["commit", "-q", "--allow-empty", "-m", message], path, check=False)
    if p.returncode != 0:
        raise Refused("git commit failed in %s: %s\nThe files are in place but not committed. To recover, either "
                      "delete the folder %s and rerun, or fix the signing or identity problem git reports and "
                      "run  git commit -m \"%s\"  in %s." % (path, (p.stderr or p.stdout).strip(), path, message, path))
    return git(["rev-parse", "--short", "HEAD"], path).stdout.strip()


def is_url(src):
    return bool(re.match(r"^[A-Za-z][A-Za-z0-9+.-]*://", src) or re.match(r"^[^/\\\s]+@[^/\\\s]+:", src))


def is_git_source(src):
    if is_url(src):
        return True
    if not os.path.isdir(src):
        raise Refused("source %s not found" % src)
    if git(["rev-parse", "--is-bare-repository"], src, check=False).stdout.strip() == "true":
        return True
    top = git(["rev-parse", "--show-toplevel"], src, check=False)
    return top.returncode == 0 and same_path(top.stdout.strip(), src)


# --- paths ----------------------------------------------------------------------------------------

def same_path(a, b):
    return os.path.normcase(os.path.abspath(a)) == os.path.normcase(os.path.abspath(b))


def self_and_ancestors(path):
    path = os.path.abspath(path)
    while True:
        yield path
        parent = os.path.dirname(path)
        if parent == path:
            return
        path = parent


def kit_containing(path):
    for d in self_and_ancestors(path):
        if os.path.isfile(os.path.join(d, KIT_MARKER)):
            return d
    return None


def refuse_target(path):
    if os.path.exists(path) and (not os.path.isdir(path) or os.listdir(path)):
        raise Refused("%s exists and is not empty; choose a new folder" % path)
    kit = kit_containing(path)
    if kit:
        raise Refused("%s is inside the ARPD kit (%s); the project must be its own repository outside the kit, "
                      "for example %s" % (path, kit, os.path.join(os.path.dirname(kit), os.path.basename(path))))


def location_warnings(path):
    parts = os.path.abspath(path).split(os.sep)
    roots = [os.environ.get(k) for k in ("OneDrive", "OneDriveCommercial", "OneDriveConsumer")]
    if any("onedrive" in p.lower() for p in parts) or any(r and os.path.abspath(path).lower().startswith(
            os.path.abspath(r).lower()) for r in roots):
        warn("%s is under OneDrive; syncing can lock or duplicate files while git and the agents work. "
             "A folder outside OneDrive is safer." % path)
    in_repo = False
    for d in list(self_and_ancestors(path))[1:]:
        for f in ("CLAUDE.md", "AGENTS.md"):
            if os.path.isfile(os.path.join(d, f)):
                warn("%s holds %s; Claude Code also reads instruction files from folders above the project, "
                     "so its instructions will mix with the project's." % (d, f))
        if not in_repo and os.path.exists(os.path.join(d, ".git")):
            in_repo = True
            warn("%s is inside another git repository (%s); the project will be a separate repository nested "
                 "in it." % (path, d))


# --- copying --------------------------------------------------------------------------------------

def payload_files(kit):
    """Relative paths (with /) of the kit's arpd/ files to copy."""
    root = os.path.join(kit, PAYLOAD)
    out = []
    for d, dirs, files in os.walk(root):
        dirs[:] = sorted(x for x in dirs if x not in PAYLOAD_SKIP_DIRS)
        for f in sorted(files):
            rel = os.path.relpath(os.path.join(d, f), root).replace(os.sep, "/")
            if f.endswith(".pyc") or rel in PAYLOAD_SKIP_ROOT_FILES:
                continue
            out.append(rel)
    return out


def kit_skills(kit):
    d = os.path.join(kit, ".claude", "skills")
    return sorted(x for x in os.listdir(d) if x.startswith("arpd-") and os.path.isdir(os.path.join(d, x))) \
        if os.path.isdir(d) else []


def tree_files(root):
    out = []
    for d, dirs, files in os.walk(root):
        dirs[:] = sorted(x for x in dirs if x != "__pycache__")
        out += [os.path.relpath(os.path.join(d, f), root).replace(os.sep, "/") for f in sorted(files)
                if not f.endswith(".pyc")]
    return out


def copy_files(pairs, force, result):
    """pairs: (source, destination, label). Fills result's added / same / changed / conflicts."""
    for src, dst, label in pairs:
        if not os.path.exists(dst):
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copyfile(src, dst)
            result["added"].append(label)
        elif filecmp.cmp(src, dst, shallow=False):
            result["same"].append(label)
        elif force:
            shutil.copyfile(src, dst)
            result["changed"].append(label)
        else:
            result["conflicts"].append(label)


def new_result():
    return {"added": [], "same": [], "changed": [], "conflicts": [], "stale": [], "removed": []}


def install_payload(kit, project, force):
    result = new_result()
    pairs = [(os.path.join(kit, PAYLOAD, *rel.split("/")), os.path.join(project, PAYLOAD, *rel.split("/")),
              PAYLOAD + "/" + rel) for rel in payload_files(kit)]
    for skill in kit_skills(kit):
        src = os.path.join(kit, ".claude", "skills", skill)
        pairs += [(os.path.join(src, *rel.split("/")), os.path.join(project, ".claude", "skills", skill, *rel.split("/")),
                   ".claude/skills/%s/%s" % (skill, rel)) for rel in tree_files(src)]
    copy_files(pairs, force, result)
    return result


def ensure_gitignore(project, extra=()):
    path = os.path.join(project, ".gitignore")
    existing = io.open(path, encoding="utf-8").read() if os.path.exists(path) else ""
    have = {l.strip() for l in existing.splitlines()}
    add = [l for l in list(GITIGNORE_LINES) + list(extra) if l not in have]
    if add:
        with io.open(path, "a", encoding="utf-8", newline="\n") as fh:
            if existing and not existing.endswith("\n"):
                fh.write("\n")
            fh.write("\n".join(add) + "\n")
    return add


def write_stub_claude(project, notes=None):
    path = os.path.join(project, "CLAUDE.md")
    if os.path.exists(path):
        return False
    with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(stub_claude(notes or NOTES))
    return True


def write_version(project, kit, how, imported=None, version=None, commit=None, extra_lines=()):
    """Write arpd/VERSION. version and commit default to the kit's (pass them when the kit's files or
    history are gone by then, as in convert); extra_lines are appended."""
    path = os.path.join(project, PAYLOAD, "VERSION")
    kept = []
    if imported is None and os.path.exists(path):  # keep the record of where the project came from
        for line in io.open(path, encoding="utf-8").read().splitlines():
            if line.startswith("Imported from:"):
                imported = line[len("Imported from:"):].strip()
            elif line.startswith("Converted from:"):
                kept.append(line)
    lines = ["ARPD %s (kit commit %s)" % (version or kit_version(kit), commit or kit_commit(kit)),
             "Installed by: arpd/tools/install.py %s, %s" % (how, datetime.date.today().isoformat())]
    if imported:
        lines.append("Imported from: " + imported)
    lines += [l for l in list(extra_lines) + kept if l not in lines]
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")


def report(result, verb="copied"):
    if result["added"]:
        say("%s %d file(s)" % (verb.capitalize(), len(result["added"])))
    if result["changed"]:
        say("Updated %d file(s):" % len(result["changed"]))
        for f in result["changed"]:
            say("    " + f)
    if result["same"]:
        say("Already up to date: %d file(s)" % len(result["same"]))
    if result["conflicts"]:
        say("CONFLICTS: %d existing file(s) differ from the kit and were NOT overwritten (rerun with --force "
            "to overwrite):" % len(result["conflicts"]))
        for f in result["conflicts"]:
            say("    " + f)


def relaunch(path):
    say("\nProject: " + path)
    say("Next, in a new terminal:")
    say('    cd "%s"' % path)
    say("    claude")
    say("(or open the folder in the Claude Code desktop app; accept the folder-trust prompt),")
    say("then type /arpd-setup to continue setup there.")


# --- inventory of a plain folder ------------------------------------------------------------------

def is_env_dir(path, name):
    return name in ENV_DIRS or name == ".git" or os.path.isfile(os.path.join(path, "pyvenv.cfg"))


def new_inventory():
    return {"files": 0, "bytes": 0, "envs": [], "large": [], "ignore": [], "data": []}


def inventory_add(inv, rel, full):
    """Count one file in inv: its size, whether it is large or to be git-ignored, and data-like."""
    size = os.path.getsize(full)
    inv["files"] += 1
    inv["bytes"] += size
    if size >= IGNORE_MB * 1024 * 1024:
        inv["ignore"].append((rel, size))
    elif size >= LARGE_MB * 1024 * 1024:
        inv["large"].append((rel, size))
    if os.path.splitext(rel)[1].lower() in DATA_EXT:
        inv["data"].append(rel)


def inventory(src):
    """{files, bytes, envs, large, ignore, data}: what a folder import would copy and skip."""
    inv = new_inventory()
    for d, dirs, files in os.walk(src):
        keep = []
        for x in sorted(dirs):
            full = os.path.join(d, x)
            (inv["envs"].append(os.path.relpath(full, src).replace(os.sep, "/") + "/") if is_env_dir(full, x)
             else keep.append(x))
        dirs[:] = keep
        for f in sorted(files):
            full = os.path.join(d, f)
            inventory_add(inv, os.path.relpath(full, src).replace(os.sep, "/"), full)
    return inv


def mb(n):
    return "%.1f MB" % (n / 1048576.0)


def print_list(title, items):
    if items:
        say("%s:" % title)
        for i in items[:LIST_MAX]:
            say("    " + i)
        if len(items) > LIST_MAX:
            say("    ... and %d more" % (len(items) - LIST_MAX))


def print_inventory(src, inv, convert=False):
    """List what a folder import copies and skips (or, with convert, what conversion keeps)."""
    if convert:
        say("Your material (kept): %d file(s), %s." % (inv["files"], mb(inv["bytes"])))
        verbs = ("kept on disk but git-ignored (not committed)", "kept but git-ignored", "kept and committed")
    else:
        say("Inventory of %s: %d file(s), %s." % (src, inv["files"], mb(inv["bytes"])))
        verbs = ("NOT copied", "copied but git-ignored", "copied and committed")
    groups = [("Environments and repositories, " + verbs[0], inv["envs"]),
              ("Files of %d MB or more, %s" % (IGNORE_MB, verbs[1]), ["%s (%s)" % (r, mb(s)) for r, s in inv["ignore"]]),
              ("Large files (%d MB or more), %s" % (LARGE_MB, verbs[2]), ["%s (%s)" % (r, mb(s)) for r, s in inv["large"]]),
              ("Data-like files, %s (check that they may be kept in the repository)" % verbs[2], inv["data"])]
    for title, items in groups:
        print_list(title, items)


def copy_folder(src, dest):
    for d, dirs, files in os.walk(src):
        dirs[:] = [x for x in sorted(dirs) if not is_env_dir(os.path.join(d, x), x)]
        out = os.path.join(dest, os.path.relpath(d, src))
        os.makedirs(out, exist_ok=True)
        for f in files:
            shutil.copy2(os.path.join(d, f), os.path.join(out, f))


def warn_old_hooks(project):
    """Warn when the project's .claude/settings.json runs an older root tools/hooks/log_hook.py."""
    try:
        text = io.open(os.path.join(project, ".claude", "settings.json"), encoding="utf-8").read().replace("\\", "/")
    except (IOError, OSError, UnicodeDecodeError):
        return
    if re.search(r"(?<!arpd/)tools/hooks/log_hook\.py", text):
        warn(".claude/settings.json runs tools/hooks/log_hook.py; keep tools/hooks/ until setup re-points the hooks "
             "with  python arpd/tools/install.py owed .  (a hook whose script is missing blocks every prompt). "
             ".claude/ was not changed.")


# --- commands -------------------------------------------------------------------------------------

def existing_ancestor(path):
    return next(d for d in self_and_ancestors(path) if os.path.isdir(d))


def cmd_new(a):
    kit = require_kit(a.kit)
    path = os.path.abspath(a.path)
    refuse_target(path)
    location_warnings(path)
    check_git(existing_ancestor(path))
    os.makedirs(path, exist_ok=True)
    git_init(path)
    result = install_payload(kit, path, force=False)
    ensure_gitignore(path)
    write_stub_claude(path)
    write_version(path, kit, "new")
    sha = commit_all(path, "Bootstrap ARPD project (setup in progress)", force_add=True)
    report(result)
    say("Created a git repository (branch main) and committed %s: Bootstrap ARPD project (setup in progress)." % sha)
    relaunch(path)
    return 0


def cmd_import(a):
    kit = require_kit(a.kit)
    dest = os.path.abspath(a.path)
    refuse_target(dest)
    src = a.source if is_url(a.source) else os.path.abspath(a.source)
    if not is_url(src) and kit_containing(src) and same_path(kit_containing(src), kit):
        raise Refused("the source is the ARPD kit itself; use new to start an empty project")
    if not is_url(src) and any(same_path(d, src) for d in self_and_ancestors(dest)):
        raise Refused("%s is inside the source %s; choose a folder outside it" % (dest, src))
    git_src = is_git_source(src)
    location_warnings(dest)
    check_git(existing_ancestor(dest))
    if git_src:
        env = dict(os.environ, GIT_TERMINAL_PROMPT="0")
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        p = git(["clone", "-q", "--recurse-submodules", src, dest], os.path.dirname(dest), check=False, env=env)
        if p.returncode != 0:
            raise Refused("git clone of %s failed: %s" % (src, (p.stderr or p.stdout).strip()))
        git(["remote", "rename", "origin", "upstream"], dest)
        git(["remote", "set-url", "--push", "upstream", "DISABLED"], dest)
        head = git(["rev-parse", "HEAD"], dest, check=False)
        at = head.stdout.strip() if head.returncode == 0 else "no commits"
        imported = "%s at %s" % (src, at)
        say("Cloned %s (%s) into %s. Its remote is now 'upstream' (fetch only; push disabled)." % (src, at, dest))
        extra = []
    else:
        inv = inventory(src)
        print_inventory(src, inv)
        if not a.yes:
            say("\nReview the list above: nothing copied yet; rerun with --yes to copy the folder.")
            return 0
        copy_folder(src, dest)
        git_init(dest)
        extra = [r for r, _ in inv["ignore"]]
        commit_all(dest, "Import %s (no changes)" % src, exclude=extra)
        imported = "%s (a folder, copied %s)" % (src, datetime.date.today().isoformat())
    result = install_payload(kit, dest, force=a.force)
    ensure_gitignore(dest, extra)
    stub = write_stub_claude(dest)
    write_version(dest, kit, "import", imported=imported)
    sha = commit_all(dest, "Bootstrap ARPD (setup in progress)", force_add=True)
    report(result)
    warn_old_hooks(dest)
    if not stub:
        say("The source's own CLAUDE.md was kept; setup will fold it into the charter.")
    say("Committed %s: Bootstrap ARPD (setup in progress)." % sha)
    relaunch(dest)
    return 2 if result["conflicts"] else 0


def cmd_install(a):
    kit = require_kit(a.kit)
    path = os.path.abspath(a.path)
    if not os.path.isdir(path):
        raise Refused("%s is not a folder" % path)
    if kit_containing(path):
        raise Refused("%s is the ARPD kit or inside it; install into the project's own repository" % path)
    if not os.path.exists(os.path.join(path, ".git")):
        warn("%s is not the top of a git repository; the ARPD records are meant to be committed." % path)
    location_warnings(path)
    result = install_payload(kit, path, force=a.force)
    added = ensure_gitignore(path)
    stub = write_stub_claude(path, a.notes)
    write_version(path, kit, "install")
    report(result)
    warn_old_hooks(path)
    if added:
        say("Added to .gitignore: " + ", ".join(added))
    if stub:
        say("Wrote a stub CLAUDE.md (setup in progress).")
    else:
        say("Kept the existing CLAUDE.md. For the PI to add to it while setup runs:")
        say("    " + stub_claude(a.notes or NOTES).splitlines()[1])
    say("Nothing was committed.")
    return 2 if result["conflicts"] else 0


def _mirror(src_root, dst_root, label, keep, prune, result):
    """Make dst_root's files match src_root's (files under `keep` are left alone)."""
    src_files = set(tree_files(src_root)) if os.path.isdir(src_root) else set()
    pairs = [(os.path.join(src_root, *r.split("/")), os.path.join(dst_root, *r.split("/")), label + r)
             for r in sorted(src_files)]
    copy_files(pairs, True, result)
    if os.path.isdir(dst_root):
        for r in tree_files(dst_root):
            if r in src_files or any(r == k or r.startswith(k + "/") for k in keep):
                continue
            if prune:
                os.remove(os.path.join(dst_root, *r.split("/")))
                result["removed"].append(label + r)
            else:
                result["stale"].append(label + r)


def cmd_update(a):
    kit = require_kit(a.kit)
    path = os.path.abspath(a.path)
    if not os.path.isdir(os.path.join(path, PAYLOAD)):
        raise Refused("%s has no arpd/ folder (a project set up before v0.6, or not an ARPD project); "
                      "use install to add arpd/" % path)
    if kit_containing(path):
        raise Refused("%s is the ARPD kit or inside it" % path)
    result = new_result()
    src_payload = os.path.join(kit, PAYLOAD)
    # Payload: the kit's files (without logs, caches or VERSION), keeping the project's logs and VERSION.
    pairs = [(os.path.join(src_payload, *r.split("/")), os.path.join(path, PAYLOAD, *r.split("/")), "arpd/" + r)
             for r in payload_files(kit)]
    copy_files(pairs, True, result)
    kit_set = set(payload_files(kit))
    for r in tree_files(os.path.join(path, PAYLOAD)):
        if r in kit_set or r in PAYLOAD_SKIP_ROOT_FILES or r.split("/")[0] in PAYLOAD_SKIP_DIRS:
            continue
        if a.prune:
            os.remove(os.path.join(path, PAYLOAD, *r.split("/")))
            result["removed"].append("arpd/" + r)
        else:
            result["stale"].append("arpd/" + r)
    skills = kit_skills(kit)
    for skill in skills:
        _mirror(os.path.join(kit, ".claude", "skills", skill), os.path.join(path, ".claude", "skills", skill),
                ".claude/skills/%s/" % skill, (), a.prune, result)
    d = os.path.join(path, ".claude", "skills")
    for extra in (sorted(x for x in os.listdir(d) if x.startswith("arpd-") and x not in skills) if os.path.isdir(d) else []):
        result["stale"].append(".claude/skills/%s/ (no longer in the kit; not removed)" % extra)
    write_version(path, kit, "update")
    say("Updated from the kit at %s (%s)." % (kit, kit_version(kit)))
    for key, title in (("added", "Added"), ("changed", "Changed"), ("removed", "Removed (--prune)"),
                       ("stale", "No longer in the kit (kept; rerun with --prune to remove)")):
        if result[key]:
            say("%s: %d" % (title, len(result[key])))
            for f in result[key]:
                say("    " + f)
    if not (result["added"] or result["changed"] or result["removed"]):
        say("arpd/ and the skills already matched the kit.")
    if any(f.startswith(("arpd/settings/", "arpd/agents/")) for f in result["added"] + result["changed"]):
        say("arpd/settings or arpd/agents changed: run  python arpd/tools/install.py owed .  to reinstall them.")
    say("arpd/logs/ was kept. Nothing was committed.")
    return 0


def _merge_hooks(existing, ours):
    hooks = dict(existing.get("hooks") or {})
    for event, entries in (ours.get("hooks") or {}).items():
        kept = [e for e in hooks.get(event, []) if "log_hook.py" not in json.dumps(e)]
        hooks[event] = kept + entries
    merged = dict(existing)
    merged["hooks"] = hooks
    return merged


def interpreter():
    """The command the hooks run: "python" if on the PATH, else "python3", else this interpreter."""
    return "python" if shutil.which("python") else ("python3" if shutil.which("python3") else sys.executable)


def with_interpreter(settings, command):
    """settings with every log-hook entry's command set to `command`."""
    out = json.loads(json.dumps(settings))
    for entries in (out.get("hooks") or {}).values():
        for entry in entries:
            for h in entry.get("hooks", []):
                if "log_hook.py" in json.dumps(h.get("args", [])):
                    h["command"] = command
    return out


def cmd_owed(a):
    path = os.path.abspath(a.path)
    payload = os.path.join(path, PAYLOAD)
    if not os.path.isdir(payload):
        raise Refused("%s has no arpd/ folder; run new, import or install first" % path)
    problems = []
    # Settings.
    src = os.path.join(payload, "settings", "settings.json")
    dst = os.path.join(path, ".claude", "settings.json")
    if not os.path.isfile(src):
        problems.append("arpd/settings/settings.json is missing; event logging not installed")
    elif not os.path.exists(dst):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        ours = with_interpreter(json.loads(io.open(src, encoding="utf-8").read()), interpreter())
        with io.open(dst, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(json.dumps(ours, indent=2) + "\n")
        say("Installed .claude/settings.json (event-logging hooks, run with %s)." % interpreter())
    else:
        try:
            existing = json.loads(io.open(dst, encoding="utf-8").read())
            if not isinstance(existing, dict):
                raise ValueError("not a JSON object")
        except ValueError as exc:
            existing = None
            problems.append(".claude/settings.json is not valid JSON (%s); not changed" % exc)
        if existing is not None:
            merged = _merge_hooks(existing, with_interpreter(json.loads(io.open(src, encoding="utf-8").read()),
                                                             interpreter()))
            if merged == existing:
                say(".claude/settings.json already runs the ARPD hooks.")
            else:
                with io.open(dst, "w", encoding="utf-8", newline="\n") as fh:
                    fh.write(json.dumps(merged, indent=2) + "\n")
                say("Merged the ARPD hooks into .claude/settings.json (its other settings kept).")
    # Agents.
    agents = os.path.join(payload, "agents")
    result = new_result()
    if os.path.isdir(agents):
        copy_files([(os.path.join(agents, f), os.path.join(path, ".claude", "agents", f), ".claude/agents/" + f)
                    for f in sorted(os.listdir(agents)) if f.endswith(".md")], a.force, result)
    for f in result["added"] + result["changed"]:
        say("Installed " + f)
    for f in result["same"]:
        say("Already installed: " + f)
    for f in result["conflicts"]:
        problems.append("%s differs from arpd/agents/; not overwritten (rerun with --force)" % f)
    # Skills.
    kit = find_kit(a.kit)
    if a.kit and not kit:
        raise Refused("%s is not the ARPD kit" % a.kit)
    for skill in (kit_skills(kit) if kit else DEFAULT_SKILLS):
        if os.path.isfile(os.path.join(path, ".claude", "skills", skill, "SKILL.md")):
            continue
        if not kit:
            problems.append(".claude/skills/%s is missing; rerun with --kit <path to the kit clone> to install it" % skill)
            continue
        r = new_result()
        s = os.path.join(kit, ".claude", "skills", skill)
        copy_files([(os.path.join(s, *x.split("/")), os.path.join(path, ".claude", "skills", skill, *x.split("/")),
                     x) for x in tree_files(s)], True, r)
        say("Installed skill .claude/skills/%s" % skill)
    if problems:
        say("Not done:")
        for p in problems:
            say("    " + p)
        return 2
    say("Nothing owed remains for settings, agents or skills. Nothing was committed.")
    return 0


# --- convert: a fresh kit clone becomes the project in place --------------------------------------

OLD_GIT = ".git-arpd-old"  # the kit's .git is moved here first (so a locked file stops before any deletion)


def under(rel, entries):
    return any(rel == e or rel.startswith(e + "/") for e in entries)


def is_payload_path(rel):
    return under(rel, [PAYLOAD]) or bool(re.match(r"^\.claude/skills/arpd-[^/]+(/|$)", rel))


def is_cache(rel):
    return rel.endswith(".pyc") or any(x in CACHE_DIRS for x in rel.split("/")[:-1])


def git_paths(args, cwd):
    p = git(args, cwd, check=False)
    return {x for x in p.stdout.split("\0") if x} if p.returncode == 0 else set()


def clean_url(url):
    """url without a user:password@ part, so a token in a remote URL is never printed or committed."""
    return re.sub(r"^([A-Za-z][A-Za-z0-9+.-]*://)[^/@]*@", r"\1", url)


def convert_plan(root):
    """What convert removes and keeps. In a git clone the kit's files are those in its HEAD commit; files
    under the manifest entries that the PI changed or added are kept (caches there are removed)."""
    manifest = kit_manifest(root)
    cdup = git(["rev-parse", "--show-cdup"], root, check=False)
    is_git = cdup.returncode == 0 and cdup.stdout.strip() == ""
    if not is_git and os.path.lexists(os.path.join(root, ".git")):
        raise Refused("%s has a .git that git cannot read (%s); repair or remove it and rerun. Nothing was "
                      "changed." % (root, (cdup.stderr or cdup.stdout).strip()))
    has_head = is_git and git(["rev-parse", "-q", "--verify", "HEAD"], root, check=False).returncode == 0
    kit_files = git_paths(["ls-tree", "-r", "-z", "--name-only", "HEAD"], root) if has_head else None
    changed = git_paths(["diff", "--name-only", "-z", "HEAD"], root) if has_head else set()
    plan = {"manifest": manifest, "git": is_git, "remove": [], "changed_kit": [], "pi_in_kit": [], "pi": [],
            "payload_changed": sorted(r for r in changed if is_payload_path(r) and
                                      os.path.exists(os.path.join(root, *r.split("/")))),
            "inv": new_inventory()}
    for d, dirs, files in os.walk(root):
        rd = os.path.relpath(d, root).replace(os.sep, "/")
        rd = "" if rd == "." else rd + "/"
        keep = []
        for x in sorted(dirs):
            rel = rd + x
            if (not rd and x == ".git") or is_payload_path(rel):
                continue
            kit_area = under(rel, manifest) or any(e.startswith(rel + "/") for e in manifest)
            if not kit_area and is_env_dir(os.path.join(d, x), x):
                plan["inv"]["envs"].append(rel + "/")
                continue
            keep.append(x)
        dirs[:] = keep
        for f in sorted(files):
            rel, full = rd + f, os.path.join(d, f)
            if not under(rel, manifest):
                plan["pi"].append(rel)
                inventory_add(plan["inv"], rel, full)
            elif rel == KIT_MARKER or kit_files is None or (rel in kit_files and rel not in changed) or \
                    (rel not in kit_files and is_cache(rel)):
                plan["remove"].append(rel)
            elif rel in kit_files:
                plan["changed_kit"].append(rel)
            else:
                plan["pi_in_kit"].append(rel)
                inventory_add(plan["inv"], rel, full)
    return plan


def local_work(root):
    """(reasons, remotes): why the clone holds work that is on no remote (local-only commits, a stash)."""
    remotes = git(["remote"], root, check=False).stdout.split()
    p = git(["rev-list", "--count", "--exclude=refs/stash", "--all"] + (["--not", "--remotes"] if remotes else []),
            root, check=False)
    n = int(p.stdout.strip() or 0) if p.returncode == 0 else 0
    reasons = ["%d commit(s) not on any remote%s" % (n, "" if remotes else " (the clone has no remote)")] if n else []
    if git(["rev-parse", "-q", "--verify", "refs/stash"], root, check=False).returncode == 0:
        reasons.append("a stash")
    return reasons, remotes


def write_bundle(root):
    """Back up every ref (branches, tags, remote-tracking refs, the stash) to a verified bundle beside root."""
    parent, name = os.path.split(root)
    stem = os.path.join(parent, "%s-pre-arpd-history-%s" % (
        name, datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%MZ")))
    path, n = stem + ".bundle", 2
    while os.path.exists(path):
        path, n = "%s-%d.bundle" % (stem, n), n + 1
    p = git(["bundle", "create", path, "--all"], root, check=False)
    v = git(["bundle", "verify", path], root, check=False) if p.returncode == 0 else p
    if v.returncode != 0:
        if os.path.exists(path):
            os.remove(path)
        raise Refused("could not write a verified backup of this clone's history to %s: %s\nNothing was deleted."
                      % (path, (v.stderr or v.stdout).strip()))
    return path


def _force_remove(func, path, _exc):
    os.chmod(path, stat.S_IWRITE)  # git's pack files are read-only on Windows
    func(path)


def remove_path(path):
    if os.path.isdir(path) and not os.path.islink(path):
        if sys.version_info >= (3, 12):
            shutil.rmtree(path, onexc=_force_remove)
        else:
            shutil.rmtree(path, onerror=_force_remove)
    else:
        try:
            os.remove(path)
        except OSError:
            _force_remove(os.remove, path, None)


def print_convert_plan(path, plan, version, commit, reasons, remotes, origin):
    say("Convert %s (ARPD %s) into the research project, in place." % (path, version))
    if plan["git"]:
        say("It is a git clone at %s, %s." % (commit, "remote origin " + origin if origin else
                                               "remotes " + ", ".join(remotes) if remotes else "with no remote"))
    else:
        say("It is a download, not a git clone: every file under the kit entries of %s is removed, including "
            "any you added there (move those out first)." % KIT_MARKER)
    say()
    print_list("Kit files to remove (%d)" % len(plan["remove"]), plan["remove"])
    say("Kept as they are (the ARPD infrastructure): arpd/ and %s." % (
        ", ".join(".claude/skills/%s/" % s for s in kit_skills(path)) or "no skills"))
    print_list("Kit files you changed: kept, not removed (%d; review them)" % len(plan["changed_kit"]),
               plan["changed_kit"])
    print_list("Your files inside kit folders: kept (%d)" % len(plan["pi_in_kit"]), plan["pi_in_kit"])
    print_list("Your other files: kept (%d)" % len(plan["pi"]), plan["pi"])
    if plan["payload_changed"]:
        warn("you changed %d ARPD file(s) in arpd/ or .claude/skills/arpd-*; they are kept as they are, but a "
             "later update from a kit will overwrite them:" % len(plan["payload_changed"]))
        print_list("Changed ARPD files", plan["payload_changed"])
    if plan["inv"]["files"] or plan["inv"]["envs"]:
        print_inventory(path, plan["inv"], convert=True)
    else:
        say("Your material: none besides the kit.")
    say()
    say("Git history: the kit's history is removed; the project starts a fresh history (branch main) with no remote.")
    if not plan["git"]:
        say("There is no git history to keep (not a git clone).")
    elif reasons:
        say("Safeguard: this clone holds work that is on no remote (%s), so a backup bundle will be written "
            "outside the folder, in %s, and verified before anything is deleted." % ("; ".join(reasons),
                                                                                  os.path.dirname(path)))
    else:
        say("Safeguard: every commit is on the remote, so the kit's history remains available from %s. "
            "No backup is needed." % (origin or "its remote"))


def cmd_convert(a):
    path = os.path.abspath(a.path)
    if not is_kit(path):
        raise Refused("%s is not an ARPD kit (no %s marker and arpd/ folder there). convert works only on a fresh "
                      "ARPD kit clone or download; for an existing repository use install, for a new folder use "
                      "new." % (path, KIT_MARKER))
    plan = convert_plan(path)
    version, commit = kit_version(path), kit_commit(path, untracked=False)  # the PI's new files are expected
    reasons, remotes = local_work(path) if plan["git"] else ([], [])
    origin = clean_url(git(["remote", "get-url", "origin"], path, check=False).stdout.strip()) \
        if "origin" in remotes else ""
    print_convert_plan(path, plan, version, commit, reasons, remotes, origin)
    location_warnings(path)
    if not a.yes:
        try:
            check_git(path)
        except Refused as exc:
            warn("%s" % exc)
        say("\nReview the plan above: nothing changed yet; rerun with --yes to convert this folder.")
        return 0
    check_git(path)
    identity = [(k, git(["config", "--get", k], path, check=False).stdout.strip()) for k in ("user.name", "user.email")]
    say()
    bundle = write_bundle(path) if plan["git"] and reasons else None
    if bundle:
        say("Backed up this clone's history (every branch, tag and stash) to %s (verified)." % bundle)
        say('    To restore it:  git clone "%s" <folder>' % bundle)
    elif plan["git"]:
        say("No local-only work; the kit's history remains available from %s." % (origin or "its remote"))
    left, old = [], None
    if os.path.lexists(os.path.join(path, ".git")):
        old = os.path.join(path, OLD_GIT)
        try:
            if os.path.lexists(old):
                remove_path(old)
            os.rename(os.path.join(path, ".git"), old)
        except OSError as exc:
            raise Refused("cannot move the kit's .git aside (%s); close any program using this folder (an editor, "
                          "a terminal running git) and rerun. Nothing was deleted%s." % (
                              exc, "; the backup bundle is kept" if bundle else ""))
    removed = []
    for rel in plan["remove"]:
        try:
            remove_path(os.path.join(path, *rel.split("/")))
            removed.append(rel)
        except OSError as exc:
            left.append("could not remove the kit file %s (%s); delete it yourself" % (rel, exc))
    for entry in plan["manifest"]:
        top = os.path.join(path, *entry.split("/"))
        for d, _, _ in (os.walk(top, topdown=False) if os.path.isdir(top) else ()):
            try:
                os.rmdir(d)  # only empty folders
            except OSError:
                pass
    extra = [r for r, _ in plan["inv"]["ignore"]] + plan["inv"]["envs"]
    if old:
        try:
            remove_path(old)
        except OSError as exc:
            extra.append(OLD_GIT + "/")
            left.append("could not delete %s, the kit's old git history (%s); close any program using it and "
                        "delete the folder yourself" % (OLD_GIT, exc))
    git_init(path)
    for key, value in identity:  # an identity set only in the kit clone's own config went with its .git
        if value and not git(["config", "--get", key], path, check=False).stdout.strip():
            git(["config", key, value], path)
    ensure_gitignore(path, extra)
    stub = write_stub_claude(path)
    source = ("Converted from: the ARPD kit clone (%s) at %s" % (origin or "no remote", commit) if plan["git"]
              else "Converted from: an ARPD kit download (not a git clone)")
    write_version(path, path, "convert", version=version, commit=commit, extra_lines=[source])
    sha = commit_all(path, "Start ARPD project in place (setup in progress)", force_add=True)  # extra: in .gitignore
    if plan["changed_kit"]:
        left.append("review the kit files you changed, kept and committed: " + ", ".join(plan["changed_kit"]))
    if plan["payload_changed"]:
        left.append("your changes to ARPD files are kept, but a later update from a kit will overwrite them: " +
                    ", ".join(plan["payload_changed"]))
    say("Removed %d kit file(s) and the kit's git history and remote." % len(removed))
    say("Kept: arpd/, the ARPD skills and your material (%d file(s))%s." % (
        plan["inv"]["files"], ", and %d kit file(s) you changed" % len(plan["changed_kit"])
        if plan["changed_kit"] else ""))
    if extra:
        say("Git-ignored (kept on disk, not committed): " + ", ".join(extra))
    if stub:
        say("Wrote the stub CLAUDE.md (setup in progress).")
    else:
        say("The existing CLAUDE.md was kept (you changed it) and not replaced by the setup stub; review it.")
    say("Started a fresh git repository (branch main) and committed %s: Start ARPD project in place "
        "(setup in progress)." % sha)
    say("No remote is configured; nothing was pushed.")
    if left:
        say("Left to you:")
        for item in left:
            say("    " + item)
    say("Setup continues in this session.")
    return 2 if left else 0


def main(argv=None):
    try:
        sys.stdout.reconfigure(errors="replace")
    except (AttributeError, ValueError):
        pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="command")
    p = sub.add_parser("convert", help="turn a fresh kit clone into the project in place (fresh history)")
    p.add_argument("path")
    p.add_argument("--yes", action="store_true", help="convert after reviewing the plan")
    p = sub.add_parser("new", help="create a new project folder and repository")
    p.add_argument("path")
    p = sub.add_parser("import", help="start a new project from existing code (git path or URL, or a folder)")
    p.add_argument("source")
    p.add_argument("path")
    p.add_argument("--yes", action="store_true", help="copy a plain folder after reviewing its inventory")
    p.add_argument("--force", action="store_true", help="overwrite the source's differing arpd/ or skill files")
    p = sub.add_parser("install", help="add ARPD to an existing repository in place (no commit)")
    p.add_argument("path")
    p.add_argument("--force", action="store_true", help="overwrite existing files that differ")
    p.add_argument("--notes", help="where the setup notes are kept, named in the stub CLAUDE.md")
    p = sub.add_parser("update", help="refresh arpd/ and the skills from the kit (no commit)")
    p.add_argument("path")
    p.add_argument("--prune", action="store_true", help="remove files no longer in the kit")
    p = sub.add_parser("owed", help="install the hook settings, agent files and missing skills")
    p.add_argument("path")
    p.add_argument("--force", action="store_true", help="overwrite agent files that differ")
    for name, p in sub.choices.items():
        if name != "convert":  # convert's kit is the folder itself
            p.add_argument("--kit", help="path to the kit clone (needed when running a project's copy)")
    a = ap.parse_args(argv)
    if not a.command:
        ap.print_help()
        return 1
    try:
        return {"convert": cmd_convert, "new": cmd_new, "import": cmd_import, "install": cmd_install, "update": cmd_update,
                "owed": cmd_owed}[a.command](a)
    except Refused as exc:
        say("REFUSED: %s" % exc)
        return 1


if __name__ == "__main__":
    sys.exit(main())
