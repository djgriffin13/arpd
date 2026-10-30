#!/bin/sh
# install.sh: the no-Python twin of arpd/tools/install.py.
#
#     sh arpd/tools/install.sh convert <path> [--dry-run | --yes [--include-local-work]] [--ignore <path> ...]
#     sh arpd/tools/install.sh new <path> [--kit <kit>]
#     sh arpd/tools/install.sh import <git path or URL> <path> [--force] [--kit <kit>]
#     sh arpd/tools/install.sh install <path> [--force] [--notes <path>] [--kit <kit>]
#     sh arpd/tools/install.sh update <path> [--kit <kit>] [--prune]
#     sh arpd/tools/install.sh owed <path> [--kit <kit>] [--force]
#
# Use it when Python 3.8+ is not available; with Python, use install.py. Each command does what the
# install.py command of the same name does (see install.py's docstring), with the same arguments,
# messages and exit codes: 0 done; 1 refused (a line starting "REFUSED:"); 2 done, with items left to
# the PI (listed). Warnings start "WARNING:".
#
# KEEP IN STEP: install.py and this script are two implementations of one behaviour. A change to one
# (a message, a gitignore line, the stub CLAUDE.md, the VERSION format, the convert plan) is made to
# both; tests/test_install_sh.py checks that convert leaves the same tree with either.
#
# What this script does not do (run install.py for these once Python is available):
#   - hooks: owed never installs .claude/settings.json (the event-logging hooks run Python); it says so
#     and exits 2 for that item. Agents and missing skills are installed as install.py does.
#   - folder import: import takes git sources only (a path to a repository, or a URL); for a plain
#     folder it refuses and says to copy the folder in by hand or use install.py.
#   - kit-files (kit development): writing .arpd-kit-files. convert reads that list as install.py does.
# Other differences: on Windows (Git Bash) paths are printed with forward slashes (C:/Users/...); file
# names holding a newline, a tab, a double quote or a backslash are not supported (git quotes them);
# owed reports nothing owed for the hooks when .claude/settings.json already runs arpd/tools/hooks/
# log_hook.py (install.py put them there; it is not re-checked); update's closing hint names both
# owed commands; --help prints a short usage and exits 1.
#
# Portability: POSIX sh (bash 3.2 on macOS, dash, Git Bash on Windows). No arrays, [[ ]], local,
# mapfile, sed -i, readlink -f, find -printf or stat. Tools: git, sh, ls, cp, mv, rm, mkdir, find,
# sed, awk (POSIX), grep, sort, cut, chmod, tail, tr, head, date, wc, cat, printf, uname, mktemp.

LC_ALL=C
export LC_ALL
IS_WIN=
case $(uname -s 2>/dev/null) in
    MINGW* | MSYS* | CYGWIN*) IS_WIN=1; PATH=/usr/bin:$PATH; export PATH ;;  # MSYS find/sort, not Windows'
esac
TAB=$(printf '\t')

KIT_MARKER=.arpd-kit
KIT_FILES=.arpd-kit-files
TOOL=arpd/tools/install.sh
FALLBACK_VERSION=v0.7.0-rc.4      # as install.py's FALLBACK_VERSION
DEFAULT_MANIFEST=".arpd-kit .arpd-kit-files AGENTS.md CITATION.cff CLAUDE.md LICENSE README.md RELEASE-NOTES.md .gitattributes .gitignore docs evaluation tests"
DEFAULT_SKILLS="arpd-setup arpd-plan arpd-checkin arpd-amend"
NOTES=reports/setup/NOTES.md
IGNORE_BYTES=52428800             # 50 MB: git-ignored
LARGE_BYTES=10485760              # 10 MB: listed
DATA_EXT=".csv .tsv .xlsx .xls .parquet .feather .h5 .hdf5 .sav .dta .rds .rdata .pkl .pickle .npy .npz .mat .db .sqlite .zip .gz .tar .7z .jsonl"

TMPD=$(mktemp -d 2>/dev/null) || TMPD=
if [ -z "$TMPD" ] || [ ! -d "$TMPD" ]; then
    TMPD=${TMPDIR:-/tmp}/arpd-install.$$
    mkdir "$TMPD" 2>/dev/null || { printf 'REFUSED: cannot create a temporary folder\n'; exit 1; }
fi
trap 'rm -rf "$TMPD"' EXIT
trap 'exit 1' HUP INT TERM

# --- output -------------------------------------------------------------------------------------

say() { printf '%s\n' "$1"; }
warn() { printf 'WARNING: %s\n' "$1"; }
refuse() { printf 'REFUSED: %s\n' "$1"; exit 1; }   # only from the main shell, never inside $( )

count() { awk 'END { print NR }' "$1"; }
join_lines() { awk '{ printf "%s%s", (NR > 1 ? ", " : ""), $0 } END { printf "\n" }' "$1"; }
indent() { sed 's/^/    /' "$1"; }

print_list() {  # title file [all]: the title and up to 20 items (every item with "all")
    [ -s "$2" ] || return 0
    say "$1:"
    if [ "$3" = all ]; then indent "$2"; return 0; fi
    awk 'NR <= 20 { print "    " $0 } END { if (NR > 20) printf "    ... and %d more\n", NR - 20 }' "$2"
}

mb() { awk -v n="$1" 'BEGIN { printf "%.1f MB", n / 1048576 }'; }

usage() {
    cat <<'EOF'
usage: sh arpd/tools/install.sh <command> ...

    convert <path> [--dry-run | --yes [--include-local-work]] [--ignore <path> ...]   (in a fresh kit clone)
    new <path> [--kit <kit>]                                               (run from the kit clone)
    import <git path or URL> <path> [--force] [--kit <kit>]                (run from the kit clone)
    install <path> [--force] [--notes <path>] [--kit <kit>]                (run from the kit clone)
    update <path> [--kit <kit>] [--prune]
    owed <path> [--kit <kit>] [--force]

The no-Python twin of arpd/tools/install.py (same commands, messages and exit codes); see that file
for what each command does. Not done here: the event-logging hooks (owed), importing a plain folder
(git sources only). Exit codes: 0 done; 1 refused or failed; 2 done, with items left to the PI.
EOF
}

usage_error() {
    usage >&2
    printf 'install.sh: error: %s\n' "$1" >&2
    exit 2
}

# --- paths --------------------------------------------------------------------------------------

abs_path() {  # an absolute path (C:/x/y form on Windows), for a path that need not exist
    _a=$1
    if [ -n "$IS_WIN" ]; then
        case $_a in *\\*) _a=$(printf '%s\n' "$_a" | sed 's#\\#/#g') ;; esac
    fi
    [ -n "$_a" ] || _a=.
    if [ -d "$_a" ]; then
        if [ -n "$IS_WIN" ]; then (cd "$_a" 2>/dev/null && { pwd -W 2>/dev/null || pwd; })
        else (cd "$_a" 2>/dev/null && pwd); fi
        return
    fi
    case $_a in
        */*) _ad=${_a%/*}; _ab=${_a##*/}; [ -n "$_ad" ] || _ad=/ ;;
        *) _ad=.; _ab=$_a ;;
    esac
    case $_ad in [A-Za-z]:) _ad=$_ad/ ;; esac
    _ad=$(abs_path "$_ad")
    case $_ab in
        '' | .) printf '%s\n' "$_ad" ;;
        ..) parent_var "$_ad"; printf '%s\n' "$PARENT" ;;
        *) join_path "$_ad" "$_ab" ;;
    esac
}

parent_var() {  # PARENT = the folder holding $1 ($1 itself at a root)
    case $1 in
        / | [A-Za-z]:/) PARENT=$1 ;;
        */*) PARENT=${1%/*}; case $PARENT in '') PARENT=/ ;; [A-Za-z]:) PARENT=$PARENT/ ;; esac ;;
        *) PARENT=$1 ;;
    esac
}

join_var() { case $1 in */) JOINED=$1$2 ;; *) JOINED=$1/$2 ;; esac; }   # JOINED = $1/$2
join_path() { join_var "$1" "$2"; printf '%s\n' "$JOINED"; }
base_of() { printf '%s\n' "${1##*/}"; }

ancestors() {  # $1 and every folder above it, nearest first
    _c=$1
    while :; do
        printf '%s\n' "$_c"
        parent_var "$_c"
        [ "$PARENT" = "$_c" ] && return 0
        _c=$PARENT
    done
}

lower() { printf '%s\n' "$1" | tr 'A-Z' 'a-z'; }

same_path() {
    if [ -n "$IS_WIN" ]; then [ "$(lower "$1")" = "$(lower "$2")" ]; else [ "$1" = "$2" ]; fi
}

existing_ancestor() {
    ancestors "$1" > "$TMPD/ea"
    while IFS= read -r _d <&3; do
        if [ -d "$_d" ]; then printf '%s\n' "$_d"; return 0; fi
    done 3< "$TMPD/ea"
}

walk_sort() {  # sort relative paths in the order Python's sorted os.walk visits them
    awk '{ n = split($0, c, "/"); k = ""; for (i = 1; i < n; i++) k = k "\001" "1" c[i]; print k "\001" "0" c[n] "\t" $0 }' |
        sort | cut -f2-
}

# --- the kit ------------------------------------------------------------------------------------

SCRIPT_DIR=$(abs_path "$(dirname -- "$0")")
parent_var "$SCRIPT_DIR"; parent_var "$PARENT"; SELF_KIT=$PARENT   # arpd/tools -> the kit root

is_kit() { [ -n "$1" ] && [ -f "$1/$KIT_MARKER" ] && [ -d "$1/arpd" ]; }

find_kit() {  # prints the kit root or nothing
    if [ -n "$1" ]; then _r=$(abs_path "$1"); else _r=$SELF_KIT; fi
    if is_kit "$_r"; then printf '%s\n' "$_r"; fi
}

require_kit() {  # sets KIT
    KIT=$(find_kit "$1")
    [ -n "$KIT" ] && return 0
    [ -n "$1" ] && refuse "$1 is not the ARPD kit (no $KIT_MARKER marker and arpd/ folder there)"
    refuse "cannot find the ARPD kit from this copy of install.sh; pass --kit <path to the kit clone>"
}

kit_containing() {
    ancestors "$1" > "$TMPD/kc"
    while IFS= read -r _d <&3; do
        join_var "$_d" "$KIT_MARKER"
        if [ -f "$JOINED" ]; then printf '%s\n' "$_d"; return 0; fi
    done 3< "$TMPD/kc"
    return 1
}

kit_version() {
    _v=$(awk 'NR == 1 { l = " " $0; if (match(l, /[^A-Za-z0-9_]v[0-9]+\.[0-9]+\.[0-9]+(-[0-9A-Za-z.]+)?/)) print substr(l, RSTART + 1, RLENGTH - 1); exit }' \
        "$1/RELEASE-NOTES.md" 2>/dev/null)
    printf '%s\n' "${_v:-$FALLBACK_VERSION}"
}

kit_base() {  # kit: KB_SHA = the kit's own commit (the newest on HEAD that is on a remote: the parent of the
    # oldest local-only commit), else HEAD; empty when there is no HEAD. KB_LOCAL = the local-only commits on top.
    KB_SHA=; KB_LOCAL=0
    KB_SHA=$(git -C "$1" rev-parse HEAD 2>/dev/null) || { KB_SHA=; return 0; }
    [ -n "$(git -C "$1" remote 2>/dev/null)" ] || return 0
    git -C "$1" rev-list HEAD --not --remotes > "$TMPD/kb.local" 2>/dev/null || : > "$TMPD/kb.local"
    [ -s "$TMPD/kb.local" ] || return 0
    KB_LOCAL=$(count "$TMPD/kb.local")
    _kbb=$(git -C "$1" rev-parse -q --verify "$(tail -n 1 "$TMPD/kb.local")^" 2>/dev/null) || _kbb=
    [ -n "$_kbb" ] && KB_SHA=$_kbb
    return 0
}

kit_commit() {  # kit [no]: the kit's own commit, noting the PI's local commits and uncommitted changes (to tracked files only with "no")
    kit_base "$1"
    [ -n "$KB_SHA" ] || { say "unknown (the kit is not a git clone)"; return 0; }
    _sha=$KB_SHA
    [ "$KB_LOCAL" -gt 0 ] && _sha="$_sha with $KB_LOCAL local commit(s) of the PI's on top"
    if [ "$2" = no ]; then _st=$(git -C "$1" status --porcelain --untracked-files=no 2>/dev/null)
    else _st=$(git -C "$1" status --porcelain 2>/dev/null); fi
    if [ $? -eq 0 ] && [ -n "$_st" ]; then say "$_sha with uncommitted changes"; else say "$_sha"; fi
}

kit_skills() {  # the arpd-* skill folders under $1/.claude/skills, sorted
    [ -d "$1/.claude/skills" ] || return 0
    for _s in "$1"/.claude/skills/arpd-*; do
        [ -d "$_s" ] && printf '%s\n' "${_s##*/}"
    done | sort
}

read_manifest() {  # root -> $TMPD/manifest: the .arpd-kit entries, as install.py's kit_manifest
    if [ -f "$1/$KIT_MARKER" ]; then
        awk '{ e = $0; gsub(/^[ \t\r]+/, "", e); gsub(/[ \t\r]+$/, "", e); gsub(/\\/, "/", e); sub(/\/+$/, "", e)
               if (e == "" || substr(e, 1, 1) == "#" || e ~ /[ \t\r]/) next
               if (substr(e, 1, 1) == "/" || e ~ /^[A-Za-z]:\//) next
               n = split(e, c, "/"); bad = 0
               for (i = 1; i <= n; i++) if (c[i] == "..") bad = 1
               if (bad || c[1] == "arpd" || c[1] == ".claude" || c[1] == ".git" || c[1] == "") next
               if (!(e in seen)) { seen[e] = 1; print e } }' "$1/$KIT_MARKER" > "$TMPD/manifest"
    else
        : > "$TMPD/manifest"
    fi
    [ -s "$TMPD/manifest" ] || printf '%s\n' $DEFAULT_MANIFEST > "$TMPD/manifest"
}

# --- git ----------------------------------------------------------------------------------------

gitc() {  # dir args...: run git in dir (output in GOUT); refuse when it fails
    _gd=$1; shift
    GOUT=$(git -C "$_gd" "$@" 2>"$TMPD/git.err")
    if [ $? -ne 0 ]; then
        _ge=$(cat "$TMPD/git.err"); [ -n "$_ge" ] || _ge=$GOUT
        refuse "git $* failed: $_ge"
    fi
}

identity_problem() {  # dir: prints the refusal text and fails when user.name or user.email is unset
    _in=$(git -C "$1" config --get user.name 2>/dev/null)
    _ie=$(git -C "$1" config --get user.email 2>/dev/null)
    [ -n "$_in" ] && [ -n "$_ie" ] && return 0
    _im=
    [ -n "$_in" ] || _im=user.name
    [ -n "$_ie" ] || _im="${_im:+$_im and }user.email"
    printf '%s\n' "git does not know who you are ($_im not set). Run, with your own details:" \
        '    git config --global user.name "Your Name"' \
        '    git config --global user.email "you@example.edu"' \
        "then rerun this command."
    return 1
}

check_git() { _cm=$(identity_problem "$1") || refuse "$_cm"; }

git_init() {
    git -C "$1" init -q -b main >/dev/null 2>&1 && return 0
    gitc "$1" init -q
    gitc "$1" symbolic-ref HEAD refs/heads/main
}

commit_all() {  # path message [force] [recover]: stage everything (force: also arpd/ and the skills) and commit; sets SHA
    # recover replaces the advice printed if the commit fails.
    _cp=$1; _cmsg=$2; _cf=$3; _crec=$4
    gitc "$_cp" add -A -- .
    if [ -n "$_cf" ]; then
        kit_skills "$_cp" > "$TMPD/cskills"
        set -- arpd
        while IFS= read -r _s <&3; do set -- "$@" ".claude/skills/$_s"; done 3< "$TMPD/cskills"
        gitc "$_cp" add -f -- "$@" ':(exclude)arpd/logs' ':(exclude)**/__pycache__'
    fi
    if ! _co=$(git -C "$_cp" commit -q --allow-empty -m "$_cmsg" 2>&1); then
        [ -n "$_crec" ] || _crec="To recover, either delete the folder $_cp and rerun, or fix the signing or identity problem git reports and run  git commit -m \"$_cmsg\"  in $_cp."
        refuse "git commit failed in $_cp: $_co
The files are in place but not committed. $_crec"
    fi
    SHA=$(git -C "$_cp" rev-parse --short HEAD)
}

is_url() {
    printf '%s\n' "$1" | grep -Eq '^[A-Za-z][A-Za-z0-9+.-]*://' && return 0
    printf '%s\n' "$1" | grep -Eq '^[^/\[:space:]]+@[^/\[:space:]]+:'
}

is_git_source() {  # an existing folder: a bare repository or the top of a work tree
    [ "$(git -C "$1" rev-parse --is-bare-repository 2>/dev/null)" = true ] && return 0
    _top=$(git -C "$1" rev-parse --show-toplevel 2>/dev/null) || return 1
    same_path "$_top" "$1"
}

clean_url() { sed 's#^\([A-Za-z][A-Za-z0-9+.-]*://\)[^/@]*@#\1#'; }

# --- copying ------------------------------------------------------------------------------------

payload_list() {  # kit: the arpd/ files to copy (no logs, caches or VERSION), relative to arpd/
    (cd "$1/arpd" && find . \( -type d \( -name logs -o -name __pycache__ -o -name .pytest_cache \) \) -prune \
        -o ! -type d ! -name '*.pyc' -print) | sed 's#^\./##' | awk '$0 != "VERSION"' | walk_sort
}

tree_list() {  # folder: its files, relative, without __pycache__ or *.pyc
    [ -d "$1" ] || return 0
    (cd "$1" && find . \( -type d -name __pycache__ \) -prune -o ! -type d ! -name '*.pyc' -print) |
        sed 's#^\./##' | walk_sort
}

pairs_for() {  # src_root dst_root label_prefix < relative paths: "src dst label src_root dst_root rel" lines (tabs)
    AW_S=$1 AW_D=$2 AW_L=$3 awk '{ s = ENVIRON["AW_S"]; d = ENVIRON["AW_D"]
        print s "/" $0 "\t" d "/" $0 "\t" ENVIRON["AW_L"] $0 "\t" s "\t" d "\t" $0 }'
}

res_reset() { for _k in added same changed conflicts stale removed; do : > "$TMPD/$1.$_k"; done; }

GNU_CP=
cp --version >/dev/null 2>&1 && GNU_CP=1   # GNU cp (Git Bash, Linux) has --parents

copy_files() {  # pairs_file force result: copy each source to its destination, never over a differing file without force
    # Forks are slow in Git Bash, so existing files are compared by content with two git hash-object calls
    # (not one cmp each), and the copies go in one cp per source root (GNU cp --parents) or per folder.
    : > "$TMPD/cf.new"; : > "$TMPD/cf.old"; : > "$TMPD/cf.diff"
    while IFS= read -r _cline <&3; do
        _ct=${_cline#*"$TAB"}; _ct=${_ct%%"$TAB"*}
        if [ -e "$_ct" ]; then printf '%s\n' "$_cline" >> "$TMPD/cf.old"
        else printf '%s\n' "$_cline" >> "$TMPD/cf.new"; fi
    done 3< "$1"
    if [ -s "$TMPD/cf.old" ]; then
        cut -f1 "$TMPD/cf.old" | git hash-object --no-filters --stdin-paths > "$TMPD/cf.h1" 2>/dev/null
        cut -f2 "$TMPD/cf.old" | git hash-object --no-filters --stdin-paths > "$TMPD/cf.h2" 2>/dev/null
        AW_R="$TMPD/$3" awk -F "$TAB" -v force="$2" '
            part == 1 { h1[FNR] = $0; next }
            part == 2 { h2[FNR] = $0; next }
            { if (h1[FNR] != "" && h1[FNR] == h2[FNR]) print $3 >> (ENVIRON["AW_R"] ".same")
              else if (force != "") { print $3 >> (ENVIRON["AW_R"] ".changed"); print }
              else print $3 >> (ENVIRON["AW_R"] ".conflicts") }' \
            part=1 "$TMPD/cf.h1" part=2 "$TMPD/cf.h2" part=3 "$TMPD/cf.old" > "$TMPD/cf.diff"
    fi
    cut -f3 "$TMPD/cf.new" >> "$TMPD/$3.added"
    if [ -n "$GNU_CP" ]; then  # group: "src_root<TAB>dst_root<TAB>rel"
        cat "$TMPD/cf.new" "$TMPD/cf.diff" | cut -f4- | sort > "$TMPD/cf.copy"
    else                       # group: "dst_folder<TAB>dst_folder<TAB>src" (one cp per destination folder)
        cat "$TMPD/cf.new" "$TMPD/cf.diff" | awk -F "$TAB" '{ d = $2; sub(/\/[^\/]*$/, "", d); print d "\t" d "\t" $1 }' |
            sort > "$TMPD/cf.copy"
    fi
    _cg=; set --
    while IFS="$TAB" read -r _csr _cdr _crel <&3; do
        if [ "$_csr$TAB$_cdr" != "$_cg" ]; then
            [ $# -gt 0 ] && copy_group "$_cgs" "$_cgd" "$@"
            set --; _cg=$_csr$TAB$_cdr; _cgs=$_csr; _cgd=$_cdr
        fi
        set -- "$@" "$_crel"
    done 3< "$TMPD/cf.copy"
    [ $# -gt 0 ] && copy_group "$_cgs" "$_cgd" "$@"
    # A new file gets the default mode, as install.py's shutil.copyfile gives it (cp keeps an executable bit).
    if [ -z "$IS_WIN" ] && [ -s "$TMPD/cf.new" ]; then
        set --
        while IFS="$TAB" read -r _cs _ct _cl <&3; do set -- "$@" "$_ct"; done 3< "$TMPD/cf.new"
        chmod a-x -- "$@" 2>/dev/null
    fi
    return 0
}

copy_group() {  # src_root dst_root files...: copy (GNU: relative paths under src_root; else: sources into the folder)
    _gs=$1; _gd=$2; shift 2
    [ -d "$_gd" ] || mkdir -p "$_gd" || refuse "cannot create $_gd"
    if [ -n "$GNU_CP" ]; then
        (cd "$_gs" && cp --parents -- "$@" "$_gd/") || refuse "cannot copy files from $_gs to $_gd"
    else
        cp -- "$@" "$_gd/" || refuse "cannot copy files to $_gd"
    fi
}

install_payload() {  # kit project force: arpd/ and the skills, into result "res"
    res_reset res
    payload_list "$1" | pairs_for "$1/arpd" "$2/arpd" "arpd/" > "$TMPD/pairs"
    kit_skills "$1" > "$TMPD/kskills"
    while IFS= read -r _s <&3; do
        tree_list "$1/.claude/skills/$_s" |
            pairs_for "$1/.claude/skills/$_s" "$2/.claude/skills/$_s" ".claude/skills/$_s/" >> "$TMPD/pairs"
    done 3< "$TMPD/kskills"
    copy_files "$TMPD/pairs" "$3" res
}

ensure_gitignore() {  # project [extra_file]: append the lines it lacks; they are left in $TMPD/gi.added
    _gi=$1/.gitignore
    { printf '%s\n' 'arpd/logs/' 'output/' '__pycache__/' '.claude/settings.local.json' '.DS_Store'
      if [ -n "$2" ] && [ -f "$2" ]; then cat "$2"; fi; } > "$TMPD/gi.cand"
    if [ -f "$_gi" ]; then
        awk 'part == 1 { l = $0; gsub(/^[ \t\r]+/, "", l); gsub(/[ \t\r]+$/, "", l); have[l] = 1; next }
             !($0 in have)' part=1 "$_gi" part=2 "$TMPD/gi.cand" > "$TMPD/gi.added"
    else
        cat "$TMPD/gi.cand" > "$TMPD/gi.added"
    fi
    [ -s "$TMPD/gi.added" ] || return 0
    if [ -s "$_gi" ] && [ -n "$(tail -c 1 "$_gi")" ]; then printf '\n' >> "$_gi"; fi
    cat "$TMPD/gi.added" >> "$_gi"
}

write_stub_claude() {  # project notes: fails when a CLAUDE.md exists
    [ -e "$1/CLAUDE.md" ] && return 1
    printf '# Setup in progress\nThis project is being set up with ARPD. Run /arpd-setup to continue; the working notes are in %s. Do not build anything until setup is complete.\n' \
        "$2" > "$1/CLAUDE.md"
}

stub_line() {  # notes: the stub's second line
    printf 'This project is being set up with ARPD. Run /arpd-setup to continue; the working notes are in %s. Do not build anything until setup is complete.\n' "$1"
}

write_version() {  # project how version commit imported(- to keep the file's) extra_line
    _vf=$1/arpd/VERSION; _vi=$5
    : > "$TMPD/v.kept"
    if [ "$_vi" = - ]; then
        _vi=
        if [ -f "$_vf" ]; then
            _vi=$(awk '{ sub(/\r$/, "") } index($0, "Imported from:") == 1 { v = substr($0, 15); gsub(/^[ \t]+|[ \t]+$/, "", v); x = v } END { print x }' "$_vf")
            awk '{ sub(/\r$/, "") } index($0, "Converted from:") == 1' "$_vf" > "$TMPD/v.kept"
        fi
    fi
    { printf 'ARPD %s (kit commit %s)\n' "$3" "$4"
      printf 'Installed by: %s %s, %s\n' "$TOOL" "$2" "$(date +%Y-%m-%d)"
      if [ -n "$_vi" ]; then printf 'Imported from: %s\n' "$_vi"; fi; } > "$TMPD/v.base"
    { if [ -n "$6" ]; then printf '%s\n' "$6"; fi; cat "$TMPD/v.kept"; } > "$TMPD/v.more"
    mkdir -p "$1/arpd"
    { cat "$TMPD/v.base"; awk 'part == 1 { b[$0] = 1; next } !($0 in b)' part=1 "$TMPD/v.base" part=2 "$TMPD/v.more"; } > "$_vf"
}

report() {  # result
    _n=$(count "$TMPD/$1.added"); [ "$_n" -gt 0 ] && say "Copied $_n file(s)"
    _n=$(count "$TMPD/$1.changed")
    if [ "$_n" -gt 0 ]; then say "Updated $_n file(s):"; indent "$TMPD/$1.changed"; fi
    _n=$(count "$TMPD/$1.same"); [ "$_n" -gt 0 ] && say "Already up to date: $_n file(s)"
    _n=$(count "$TMPD/$1.conflicts")
    if [ "$_n" -gt 0 ]; then
        say "CONFLICTS: $_n existing file(s) differ from the kit and were NOT overwritten (rerun with --force to overwrite):"
        indent "$TMPD/$1.conflicts"
    fi
    return 0
}

relaunch() {
    say ""
    say "Project: $1"
    say "Next, in a new terminal:"
    say "    cd \"$1\""
    say "    claude"
    say "(or open the folder in the Claude Code desktop app; accept the folder-trust prompt),"
    say "then type /arpd-setup to continue setup there."
}

refuse_target() {
    if [ -e "$1" ]; then
        if [ ! -d "$1" ] || [ -n "$(ls -A "$1" 2>/dev/null)" ]; then refuse "$1 exists and is not empty; choose a new folder"; fi
    fi
    if _k=$(kit_containing "$1"); then
        parent_var "$_k"
        refuse "$1 is inside the ARPD kit ($_k); the project must be its own repository outside the kit, for example $(join_path "$PARENT" "$(base_of "$1")")"
    fi
}

location_warnings() {
    _lp=$(lower "$1"); _od=
    case $_lp in *onedrive*) _od=1 ;; esac
    for _r in "${OneDrive:-}" "${OneDriveCommercial:-}" "${OneDriveConsumer:-}"; do
        [ -n "$_r" ] || continue
        _r=$(lower "$(printf '%s\n' "$_r" | sed 's#\\#/#g')")
        case $_lp in "$_r"*) _od=1 ;; esac
    done
    [ -n "$_od" ] && warn "$1 is under OneDrive; syncing can lock or duplicate files while git and the agents work. A folder outside OneDrive is safer."
    ancestors "$1" | sed 1d > "$TMPD/lw"
    _inrepo=
    while IFS= read -r _d <&3; do
        for _f in CLAUDE.md AGENTS.md; do
            join_var "$_d" "$_f"
            [ -f "$JOINED" ] && warn "$_d holds $_f; Claude Code also reads instruction files from folders above the project, so its instructions will mix with the project's."
        done
        join_var "$_d" .git
        if [ -z "$_inrepo" ] && { [ -e "$JOINED" ] || [ -L "$JOINED" ]; }; then
            _inrepo=1
            warn "$1 is inside another git repository ($_d); the project will be a separate repository nested in it."
        fi
    done 3< "$TMPD/lw"
    return 0
}

warn_old_hooks() {
    _sf=$1/.claude/settings.json
    [ -f "$_sf" ] || return 0
    if awk '{ gsub(/\\/, "/"); s = s $0 "\n" }
            END { t = s; while ((i = index(t, "tools/hooks/log_hook.py")) > 0) {
                      if (i < 6 || substr(t, i - 5, 5) != "arpd/") exit 0
                      t = substr(t, i + 1) }
                  exit 1 }' "$_sf"; then
        warn ".claude/settings.json runs tools/hooks/log_hook.py; keep tools/hooks/ until setup re-points the hooks with  python arpd/tools/install.py owed .  (a hook whose script is missing blocks every prompt). .claude/ was not changed."
    fi
}

# --- commands -----------------------------------------------------------------------------------

cmd_new() {
    require_kit "$KITARG"
    P=$(abs_path "$POS1")
    refuse_target "$P"
    location_warnings "$P"
    check_git "$(existing_ancestor "$P")"
    mkdir -p "$P" || refuse "cannot create $P"
    git_init "$P"
    install_payload "$KIT" "$P" ""
    ensure_gitignore "$P" ""
    write_stub_claude "$P" "$NOTES"
    write_version "$P" new "$(kit_version "$KIT")" "$(kit_commit "$KIT")" - ""
    commit_all "$P" "Bootstrap ARPD project (setup in progress)" force
    report res
    say "Created a git repository (branch main) and committed $SHA: Bootstrap ARPD project (setup in progress)."
    relaunch "$P"
    exit 0
}

cmd_import() {
    require_kit "$KITARG"
    DEST=$(abs_path "$POS2")
    refuse_target "$DEST"
    SRC=$POS1
    if ! is_url "$SRC"; then
        SRC=$(abs_path "$SRC")
        if _k=$(kit_containing "$SRC") && same_path "$_k" "$KIT"; then
            refuse "the source is the ARPD kit itself; use new to start an empty project"
        fi
        ancestors "$DEST" > "$TMPD/danc"
        while IFS= read -r _d <&3; do
            same_path "$_d" "$SRC" && refuse "$DEST is inside the source $SRC; choose a folder outside it"
        done 3< "$TMPD/danc"
        [ -d "$SRC" ] || refuse "source $SRC not found"
        is_git_source "$SRC" || refuse "$SRC is a plain folder, not a git repository; install.sh imports git sources only. Copy the folder in by hand (create the project with  sh arpd/tools/install.sh new <path>, then copy the files in and commit them), or use  python arpd/tools/install.py import  once Python 3.8+ is available (it lists large files and environments first and copies the rest)."
    fi
    location_warnings "$DEST"
    check_git "$(existing_ancestor "$DEST")"
    parent_var "$DEST"; mkdir -p "$PARENT"
    if ! _o=$(cd "$PARENT" && GIT_TERMINAL_PROMPT=0 git clone -q --recurse-submodules "$SRC" "$DEST" 2>&1); then
        refuse "git clone of $SRC failed: $_o"
    fi
    gitc "$DEST" remote rename origin upstream
    gitc "$DEST" remote set-url --push upstream DISABLED
    _at=$(git -C "$DEST" rev-parse HEAD 2>/dev/null) || _at="no commits"
    say "Cloned $SRC ($_at) into $DEST. Its remote is now 'upstream' (fetch only; push disabled)."
    install_payload "$KIT" "$DEST" "$FORCE"
    ensure_gitignore "$DEST" ""
    _stub=1; write_stub_claude "$DEST" "$NOTES" || _stub=
    write_version "$DEST" import "$(kit_version "$KIT")" "$(kit_commit "$KIT")" "$SRC at $_at" ""
    commit_all "$DEST" "Bootstrap ARPD (setup in progress)" force
    report res
    warn_old_hooks "$DEST"
    [ -n "$_stub" ] || say "The source's own CLAUDE.md was kept; setup will fold it into the charter."
    say "Committed $SHA: Bootstrap ARPD (setup in progress)."
    relaunch "$DEST"
    [ -s "$TMPD/res.conflicts" ] && exit 2
    exit 0
}

cmd_install() {
    require_kit "$KITARG"
    P=$(abs_path "$POS1")
    [ -d "$P" ] || refuse "$P is not a folder"
    kit_containing "$P" >/dev/null && refuse "$P is the ARPD kit or inside it; install into the project's own repository"
    [ -e "$P/.git" ] || warn "$P is not the top of a git repository; the ARPD records are meant to be committed."
    location_warnings "$P"
    install_payload "$KIT" "$P" "$FORCE"
    ensure_gitignore "$P" ""
    _notes=${NOTES_ARG:-$NOTES}
    _stub=1; write_stub_claude "$P" "$_notes" || _stub=
    write_version "$P" install "$(kit_version "$KIT")" "$(kit_commit "$KIT")" - ""
    report res
    warn_old_hooks "$P"
    [ -s "$TMPD/gi.added" ] && say "Added to .gitignore: $(join_lines "$TMPD/gi.added")"
    if [ -n "$_stub" ]; then
        say "Wrote a stub CLAUDE.md (setup in progress)."
    else
        say "Kept the existing CLAUDE.md. For the PI to add to it while setup runs:"
        say "    $(stub_line "$_notes")"
    fi
    say "Nothing was committed."
    [ -s "$TMPD/res.conflicts" ] && exit 2
    exit 0
}

stale_or_prune() {  # dst_root label_prefix list_file: files no longer in the kit
    while IFS= read -r _r <&3; do
        if [ -n "$PRUNE" ]; then
            rm -f "$1/$_r"
            printf '%s%s\n' "$2" "$_r" >> "$TMPD/res.removed"
        else
            printf '%s%s\n' "$2" "$_r" >> "$TMPD/res.stale"
        fi
    done 3< "$3"
}

cmd_update() {
    require_kit "$KITARG"
    P=$(abs_path "$POS1")
    [ -d "$P/arpd" ] || refuse "$P has no arpd/ folder (a project set up before v0.6, or not an ARPD project); use install to add arpd/"
    kit_containing "$P" >/dev/null && refuse "$P is the ARPD kit or inside it"
    res_reset res
    payload_list "$KIT" > "$TMPD/kitpay"
    pairs_for "$KIT/arpd" "$P/arpd" "arpd/" < "$TMPD/kitpay" > "$TMPD/pairs"
    copy_files "$TMPD/pairs" 1 res
    tree_list "$P/arpd" > "$TMPD/projpay"
    awk 'part == 1 { k[$0] = 1; next }
         { split($0, c, "/"); if (!($0 in k) && $0 != "VERSION" && c[1] != "logs" && c[1] != "__pycache__" && c[1] != ".pytest_cache") print }' \
        part=1 "$TMPD/kitpay" part=2 "$TMPD/projpay" > "$TMPD/gone"
    stale_or_prune "$P/arpd" "arpd/" "$TMPD/gone"
    kit_skills "$KIT" > "$TMPD/kskills"
    while IFS= read -r _s <&3; do
        tree_list "$KIT/.claude/skills/$_s" > "$TMPD/ssrc"
        pairs_for "$KIT/.claude/skills/$_s" "$P/.claude/skills/$_s" ".claude/skills/$_s/" < "$TMPD/ssrc" > "$TMPD/pairs"
        copy_files "$TMPD/pairs" 1 res
        tree_list "$P/.claude/skills/$_s" > "$TMPD/sdst"
        awk 'part == 1 { k[$0] = 1; next } !($0 in k)' part=1 "$TMPD/ssrc" part=2 "$TMPD/sdst" > "$TMPD/gone"
        stale_or_prune "$P/.claude/skills/$_s" ".claude/skills/$_s/" "$TMPD/gone"
    done 3< "$TMPD/kskills"
    if [ -d "$P/.claude/skills" ]; then
        for _e in "$P"/.claude/skills/arpd-*; do
            { [ -e "$_e" ] || [ -L "$_e" ]; } || continue
            printf '%s\n' "${_e##*/}"
        done | sort > "$TMPD/pskills"
        while IFS= read -r _s <&3; do
            grep -qxF "$_s" "$TMPD/kskills" ||
                printf '%s\n' ".claude/skills/$_s/ (no longer in the kit; not removed)" >> "$TMPD/res.stale"
        done 3< "$TMPD/pskills"
    fi
    write_version "$P" update "$(kit_version "$KIT")" "$(kit_commit "$KIT")" - ""
    say "Updated from the kit at $KIT ($(kit_version "$KIT"))."
    for _k in added:Added changed:Changed "removed:Removed (--prune)" "stale:No longer in the kit (kept; rerun with --prune to remove)"; do
        _f=$TMPD/res.${_k%%:*}
        if [ -s "$_f" ]; then say "${_k#*:}: $(count "$_f")"; indent "$_f"; fi
    done
    if [ ! -s "$TMPD/res.added" ] && [ ! -s "$TMPD/res.changed" ] && [ ! -s "$TMPD/res.removed" ]; then
        say "arpd/ and the skills already matched the kit."
    fi
    if cat "$TMPD/res.added" "$TMPD/res.changed" | grep -Eq '^arpd/(settings|agents)/'; then
        say "arpd/settings or arpd/agents changed: run  sh arpd/tools/install.sh owed .  to reinstall them (with Python,  python arpd/tools/install.py owed .  also reinstalls the hooks)."
    fi
    say "arpd/logs/ was kept. Nothing was committed."
    exit 0
}

cmd_owed() {
    P=$(abs_path "$POS1")
    [ -d "$P/arpd" ] || refuse "$P has no arpd/ folder; run new, import or install first"
    : > "$TMPD/problems"
    # Settings: the hooks run Python, so they are left to install.py.
    _sf=$P/.claude/settings.json
    if [ -f "$_sf" ] && awk '{ gsub(/\\/, "/") } index($0, "arpd/tools/hooks/log_hook.py") { f = 1 } END { exit !f }' "$_sf"; then
        say ".claude/settings.json already names the ARPD hooks (not checked or changed here: that needs Python)."
    else
        say "Event-logging hooks not installed: they need Python 3.8+ (run install.py owed later, once Python is available)." >> "$TMPD/problems"
    fi
    # Agents.
    res_reset ag
    : > "$TMPD/pairs"
    if [ -d "$P/arpd/agents" ]; then
        for _f in "$P"/arpd/agents/*.md; do
            [ -e "$_f" ] && printf '%s\n' "${_f##*/}"
        done | pairs_for "$P/arpd/agents" "$P/.claude/agents" ".claude/agents/" > "$TMPD/pairs"
    fi
    copy_files "$TMPD/pairs" "$FORCE" ag
    cat "$TMPD/ag.added" "$TMPD/ag.changed" | sed 's/^/Installed /'
    sed 's/^/Already installed: /' "$TMPD/ag.same"
    sed 's#$# differs from arpd/agents/; not overwritten (rerun with --force)#' "$TMPD/ag.conflicts" >> "$TMPD/problems"
    # Skills.
    _kit=$(find_kit "$KITARG")
    [ -n "$KITARG" ] && [ -z "$_kit" ] && refuse "$KITARG is not the ARPD kit"
    if [ -n "$_kit" ]; then kit_skills "$_kit" > "$TMPD/oskills"; else printf '%s\n' $DEFAULT_SKILLS > "$TMPD/oskills"; fi
    while IFS= read -r _s <&3; do
        [ -f "$P/.claude/skills/$_s/SKILL.md" ] && continue
        if [ -z "$_kit" ]; then
            say ".claude/skills/$_s is missing; rerun with --kit <path to the kit clone> to install it" >> "$TMPD/problems"
            continue
        fi
        res_reset sk
        tree_list "$_kit/.claude/skills/$_s" | pairs_for "$_kit/.claude/skills/$_s" "$P/.claude/skills/$_s" "" > "$TMPD/spairs"
        copy_files "$TMPD/spairs" 1 sk
        say "Installed skill .claude/skills/$_s"
    done 3< "$TMPD/oskills"
    if [ -s "$TMPD/problems" ]; then
        say "Not done:"
        indent "$TMPD/problems"
        exit 2
    fi
    say "Nothing owed remains for settings, agents or skills. Nothing was committed."
    exit 0
}

# --- convert: a fresh kit clone becomes the project in place ------------------------------------

file_sizes() {  # list (relative to the current folder) -> "<size> ./<path>" lines from wc -c, in batches
    _fl=$1
    set --
    while IFS= read -r _f <&3; do
        set -- "$@" "./$_f"
        if [ $# -ge 200 ]; then wc -c "$@" 2>/dev/null; set --; fi
    done 3< "$_fl"
    if [ $# -gt 0 ]; then wc -c "$@" 2>/dev/null; fi
    return 0
}

convert_plan() {  # in $CPATH (the current folder): $TMPD/p.* lists and PLAN_* settings
    read_manifest "$CPATH"
    _cd=$(git -C "$CPATH" rev-parse --show-cdup 2>"$TMPD/err"); _rc=$?
    PLAN_GIT=; PLAN_LISTED=
    [ $_rc -eq 0 ] && [ -z "$_cd" ] && PLAN_GIT=1
    if [ -z "$PLAN_GIT" ] && { [ -e "$CPATH/.git" ] || [ -L "$CPATH/.git" ]; }; then
        _m=$(cat "$TMPD/err"); [ -n "$_m" ] || _m=$_cd
        refuse "$CPATH has a .git that git cannot read ($_m); repair or remove it and rerun. Nothing was changed."
    fi
    # The walk skips .git, arpd/ and the ARPD skills, as install.py's convert_plan does.
    find . \( -type d \( -path ./.git -o -path ./arpd -o -path './.claude/skills/arpd-*' \) \) -prune \
        -o -type d -print | sed -e 's#^\./##' -e '/^\.$/d' | sort > "$TMPD/dirs"
    find . \( -type d \( -path ./.git -o -path ./arpd -o -path './.claude/skills/arpd-*' \) \) -prune \
        -o ! -type d -print | sed 's#^\./##' | walk_sort > "$TMPD/files"
    : > "$TMPD/kitfiles"; : > "$TMPD/changed"; _nohead=1
    if [ -n "$PLAN_GIT" ]; then
        if git -C "$CPATH" rev-parse -q --verify HEAD >/dev/null 2>&1; then
            _nohead=
            # The kit's files are those of the kit's own commit, never of the PI's local commits on top of it: a
            # file the PI committed under a kit folder, or a kit file the PI changed in a commit, is the PI's (kept).
            kit_base "$CPATH"
            git -C "$CPATH" -c core.quotepath=off ls-tree -r --name-only "$KB_SHA" > "$TMPD/kitfiles" 2>/dev/null || : > "$TMPD/kitfiles"
            git -C "$CPATH" -c core.quotepath=off diff --name-only "$KB_SHA" > "$TMPD/changed" 2>/dev/null || : > "$TMPD/changed"
            # The kit's own file list, as the base commit holds it, has the last word: a file is the kit's only if
            # the list names it with the content the base commit holds. So a file the PI committed under a kit
            # folder stays the PI's even when the base cannot be told apart from the PI's commits (no remote, or
            # the PI's commits pushed to a remote of their own).
            if git -C "$CPATH" show "$KB_SHA:$KIT_FILES" > "$TMPD/blist.raw" 2>/dev/null; then
                awk '{ l = $0; gsub(/^[ \t\r]+/, "", l); gsub(/[ \t\r]+$/, "", l); i = index(l, " ")
                       if (i == 41) { s = substr(l, 1, 40); if (s !~ /[^0-9a-f]/) print s "\t" substr(l, 42) } }' \
                    "$TMPD/blist.raw" > "$TMPD/blist"
                git -C "$CPATH" -c core.quotepath=off ls-tree -r "$KB_SHA" > "$TMPD/btree" 2>/dev/null || : > "$TMPD/btree"
                AW_K="$TMPD/kitfiles.listed" AW_C="$TMPD/changed.listed" awk -F "$TAB" -v marker="$KIT_MARKER" -v list="$KIT_FILES" '
                    function under(r,  i) { for (i = 1; i <= nm; i++) if (r == m[i] || index(r, m[i] "/") == 1) return 1; return 0 }
                    function iscache(r,  n, c, i) {
                        if (r ~ /\.pyc$/) return 1
                        n = split(r, c, "/")
                        for (i = 1; i < n; i++) if (c[i] == "__pycache__" || c[i] == ".pytest_cache" || c[i] == ".mypy_cache") return 1
                        return 0 }
                    BEGIN { ko = ENVIRON["AW_K"]; co = ENVIRON["AW_C"]; printf "" > ko; printf "" > co }
                    part == "m" { m[++nm] = $0; next }
                    part == "b" { bl[$2] = $1; next }
                    part == "t" { n = split($1, meta, " "); if (n == 3) blob[$2] = meta[3]; next }
                    part == "k" { r = $0
                                  if (under(r) && r != marker && r != list && !iscache(r) && !(r in bl)) next  # committed by the PI: theirs
                                  print r > ko
                                  if ((r in bl) && blob[r] != bl[r]) print r > co }' \
                    part=m "$TMPD/manifest" part=b "$TMPD/blist" part=t "$TMPD/btree" part=k "$TMPD/kitfiles"
                cat "$TMPD/kitfiles.listed" > "$TMPD/kitfiles"
                cat "$TMPD/changed" "$TMPD/changed.listed" | sort -u > "$TMPD/changed.all"
                cat "$TMPD/changed.all" > "$TMPD/changed"
            fi
        fi
    elif [ -f "$CPATH/$KIT_FILES" ]; then
        # A download with the kit file list: a file is the kit's only if listed with the same content.
        PLAN_LISTED=1; _nohead=
        awk '{ l = $0; gsub(/^[ \t\r]+/, "", l); gsub(/[ \t\r]+$/, "", l); i = index(l, " ")
               if (i == 41) { s = substr(l, 1, 40); if (s !~ /[^0-9a-f]/) print s "\t" substr(l, 42) } }' \
            "$CPATH/$KIT_FILES" > "$TMPD/listed"
        cut -f2- "$TMPD/listed" > "$TMPD/kitfiles"
        awk 'function under(r,  i) { for (i = 1; i <= nm; i++) if (r == m[i] || index(r, m[i] "/") == 1) return 1; return 0 }
             part == "m" { m[++nm] = $0; next }
             part == "l" { t = index($0, "\t"); listed[substr($0, t + 1)] = 1; next }
             under($0) && ($0 in listed)' part=m "$TMPD/manifest" part=l "$TMPD/listed" part=f "$TMPD/files" > "$TMPD/cand"
        : > "$TMPD/shas"
        if [ -s "$TMPD/cand" ]; then
            git -c core.autocrlf=true hash-object --stdin-paths < "$TMPD/cand" > "$TMPD/shas" 2>"$TMPD/err" ||
                refuse "git hash-object failed: $(cat "$TMPD/err")"
        fi
        awk -v same="$(count "$TMPD/cand")" 'part == "l" { t = index($0, "\t"); want[substr($0, t + 1)] = substr($0, 1, t - 1); next }
             part == "s" { got[FNR] = $1; ns = FNR; next }
             part == "c" { if (ns != same || got[FNR] != want[$0]) print }' \
            part=l "$TMPD/listed" part=s "$TMPD/shas" part=c "$TMPD/cand" > "$TMPD/changed"
    fi
    awk -v nohead="$_nohead" -v marker="$KIT_MARKER" -v list="$KIT_FILES" '
        function under(r,  i) { for (i = 1; i <= nm; i++) if (r == m[i] || index(r, m[i] "/") == 1) return 1; return 0 }
        function kitarea(r,  i) { if (under(r)) return 1; for (i = 1; i <= nm; i++) if (index(m[i], r "/") == 1) return 1; return 0 }
        function parent(r) { if (match(r, /\/[^\/]*$/)) return substr(r, 1, RSTART - 1); return "" }
        function base(r) { if (match(r, /\/[^\/]*$/)) return substr(r, RSTART + 1); return r }
        function iscache(r,  n, c, i) {
            if (r ~ /\.pyc$/) return 1
            n = split(r, c, "/")
            for (i = 1; i < n; i++) if (c[i] == "__pycache__" || c[i] == ".pytest_cache" || c[i] == ".mypy_cache") return 1
            return 0 }
        BEGIN { split(".venv venv node_modules __pycache__ .pytest_cache .mypy_cache .ipynb_checkpoints .git", t, " ")
                for (i in t) envname[t[i]] = 1 }
        part == "m" { m[++nm] = $0; next }
        part == "k" { kit[$0] = 1; next }
        part == "c" { chg[$0] = 1; next }
        part == "v" { if (base($0) == "pyvenv.cfg") venv[parent($0)] = 1; next }
        part == "d" { d = $0; p = parent(d)
                      if (p != "" && (p in pruned)) { pruned[d] = 1; next }
                      if (!kitarea(d) && ((base(d) in envname) || (d in venv))) { pruned[d] = 1; print "E\t" d }
                      next }
        part == "f" { f = $0; p = parent(f)
                      if (p != "" && (p in pruned)) next
                      if (!under(f)) print "P\t" f
                      else if (f == marker || f == list || nohead || ((f in kit) && !(f in chg)) || (!(f in kit) && iscache(f))) print "R\t" f
                      else if (f in kit) print "C\t" f
                      else print "K\t" f }' \
        part=m "$TMPD/manifest" part=k "$TMPD/kitfiles" part=c "$TMPD/changed" part=v "$TMPD/files" \
        part=d "$TMPD/dirs" part=f "$TMPD/files" > "$TMPD/plan"
    for _k in R C K P; do grep "^$_k$TAB" "$TMPD/plan" | cut -f2- > "$TMPD/p.$_k"; done
    grep "^E$TAB" "$TMPD/plan" | cut -f2- | walk_sort | sed 's#$#/#' > "$TMPD/p.E"
    grep -E "^(P|K)$TAB" "$TMPD/plan" | cut -f2- > "$TMPD/p.inv"
    awk '$0 == "arpd" || index($0, "arpd/") == 1 || $0 ~ /^\.claude\/skills\/arpd-[^\/]+$/ || $0 ~ /^\.claude\/skills\/arpd-[^\/]+\//' \
        "$TMPD/changed" | sort > "$TMPD/pc"
    : > "$TMPD/p.payload"
    while IFS= read -r _r <&3; do
        [ -e "$_r" ] && printf '%s\n' "$_r" >> "$TMPD/p.payload"
    done 3< "$TMPD/pc"
    # Inventory of the PI's files: sizes, files to git-ignore, large and data-like files.
    file_sizes "$TMPD/p.inv" > "$TMPD/sizes"
    AW_DATA=$DATA_EXT awk -v ig="$IGNORE_BYTES" -v lg="$LARGE_BYTES" '
        function ext(r,  b) {
            b = r; if (match(b, /\/[^\/]*$/)) b = substr(b, RSTART + 1)
            sub(/^\.+/, "", b)
            if (match(b, /\.[^.]*$/)) return tolower(substr(b, RSTART))
            return "" }
        BEGIN { n = split(ENVIRON["AW_DATA"], t, " "); for (i = 1; i <= n; i++) data[t[i]] = 1 }
        part == "s" { if (match($0, /^ *[0-9]+ /)) { s = substr($0, 1, RLENGTH) + 0; nm = substr($0, RLENGTH + 1)
                          if (substr(nm, 1, 2) == "./") size[substr(nm, 3)] = s }
                      next }
        part == "l" { r = $0; s = (r in size) ? size[r] : 0; nf++; nb += s
                      if (s >= ig) printf "I\t%s\t%.0f\n", r, s
                      else if (s >= lg) printf "L\t%s\t%.0f\n", r, s
                      if (ext(r) in data) print "D\t" r }
        END { printf "N\t%d\nB\t%.0f\n", nf, nb }' part=s "$TMPD/sizes" part=l "$TMPD/p.inv" > "$TMPD/inv"
    INV_FILES=$(awk -F "$TAB" '$1 == "N" { print $2 }' "$TMPD/inv")
    INV_BYTES=$(awk -F "$TAB" '$1 == "B" { print $2 }' "$TMPD/inv")
    awk -F "$TAB" '$1 == "I" { print $2 }' "$TMPD/inv" > "$TMPD/i.ignore"
    awk -F "$TAB" '$1 == "I" { printf "%s (%.1f MB)\n", $2, $3 / 1048576 }' "$TMPD/inv" > "$TMPD/i.ignore.fmt"
    awk -F "$TAB" '$1 == "L" { printf "%s (%.1f MB)\n", $2, $3 / 1048576 }' "$TMPD/inv" > "$TMPD/i.large.fmt"
    awk -F "$TAB" '$1 == "D" { print $2 }' "$TMPD/inv" > "$TMPD/i.data"
}

local_work() {  # REASONS ("; "-joined), $TMPD/remotes, $TMPD/details
    REASONS=; ORIGIN=
    : > "$TMPD/remotes"; : > "$TMPD/details"; : > "$TMPD/other.remotes"
    [ -n "$PLAN_GIT" ] || return 0
    git -C "$CPATH" remote > "$TMPD/remotes" 2>/dev/null
    if [ -s "$TMPD/remotes" ]; then set -- --exclude=refs/stash --all --not --remotes
    else set -- --exclude=refs/stash --all; fi
    _n=$(git -C "$CPATH" rev-list --count "$@" 2>/dev/null)
    case $_n in '' | *[!0-9]*) _n=0 ;; esac
    if [ "$_n" -gt 0 ]; then
        REASONS="$_n commit(s) not on any remote"
        [ -s "$TMPD/remotes" ] || REASONS="$REASONS (the clone has no remote)"
        git -C "$CPATH" log --oneline -n 10 "$@" 2>/dev/null | sed 's/^/commit /' >> "$TMPD/details"
        [ "$_n" -gt 10 ] && say "... and $((_n - 10)) more commit(s)" >> "$TMPD/details"
    fi
    _cur=$(git -C "$CPATH" symbolic-ref -q --short HEAD 2>/dev/null)
    git -C "$CPATH" for-each-ref --format='%(refname:short)' refs/heads 2>/dev/null |
        AW_CUR=$_cur awk '$0 != "" && $0 != ENVIRON["AW_CUR"]' > "$TMPD/branches"
    if [ -s "$TMPD/branches" ]; then
        REASONS="${REASONS:+$REASONS; }$(count "$TMPD/branches") other local branch(es)"
        sed 's/^/branch /' "$TMPD/branches" >> "$TMPD/details"
    fi
    if git -C "$CPATH" rev-parse -q --verify refs/stash >/dev/null 2>&1; then
        REASONS="${REASONS:+$REASONS; }a stash"
        say "stash $(git -C "$CPATH" stash list -n 1 2>/dev/null)" >> "$TMPD/details"
    fi
    if grep -qx origin "$TMPD/remotes"; then
        ORIGIN=$(git -C "$CPATH" remote get-url origin 2>/dev/null | clean_url)
    fi
    : > "$TMPD/other.remotes"   # "<name> <url>" for every remote but origin, credentials stripped
    while IFS= read -r _rn <&3; do
        [ "$_rn" = origin ] && continue
        printf '%s %s\n' "$_rn" "$(git -C "$CPATH" remote get-url "$_rn" 2>/dev/null | clean_url)" >> "$TMPD/other.remotes"
    done 3< "$TMPD/remotes"
}

refuse_other_worktrees() {
    git -C "$CPATH" worktree list --porcelain 2>/dev/null | sed -n 's/^worktree //p' > "$TMPD/wt" || return 0
    : > "$TMPD/wt.other"
    while IFS= read -r _w <&3; do
        same_path "$_w" "$CPATH" || printf '%s\n' "$_w" >> "$TMPD/wt.other"
    done 3< "$TMPD/wt"
    [ -s "$TMPD/wt.other" ] || return 0
    refuse "this clone has other git worktrees ($(join_lines "$TMPD/wt.other")); converting would delete the history they depend on. Remove them (git worktree remove <path>; git worktree prune for one whose folder is gone) or convert a fresh clone. Nothing was changed."
}

backup_var() {  # BACKUP = a new folder beside the project: <name>-pre-arpd-backup-<UTC time>[-n]
    parent_var "$CPATH"
    join_var "$PARENT" "$(base_of "$CPATH")-pre-arpd-backup-$(date -u +%Y%m%dT%H%MZ)"
    BACKUP=$JOINED; _i=2
    while [ -e "$BACKUP" ]; do BACKUP=$JOINED-$_i; _i=$((_i + 1)); done
}

write_restore() {  # has_git: $BACKUP/RESTORE.md, as install.py's RESTORE_TEXT
    _note=
    [ -n "$1" ] && _note=' and its git history (`.git`: every branch, tag and stash, including any local commits)'
    _p=$(printf '%s\n' "$CPATH" | sed 's#\\#/#g'); _b=$(printf '%s\n' "$BACKUP" | sed 's#\\#/#g')
    cat > "$BACKUP/RESTORE.md" <<EOF
# Restoring the ARPD kit clone

This folder holds what \`convert\` moved out of

    $_p

on $(date -u +%Y-%m-%dT%H:%MZ): the kit's own files$_note. Nothing was deleted.

## To undo the conversion

Do this soon after converting, before you have committed work you want to keep: it replaces the
project's new history. In the project folder, in Git Bash or another shell:

    cd "$_p"
    rm -rf .git
    cp -a "$_b/." .
    rm -f RESTORE.md
    git status

\`git status\` then shows what you added since the conversion (and \`arpd/VERSION\`). If you have
committed work since, copy it out first.

## To recover something from the kit's history later

    git -C "$_b" log --all --oneline
    git -C "$_b" show <commit>:<path>

The project does not need this folder. Delete it whenever you no longer want the backup.
EOF
}

print_convert_plan() {
    say "Convert $CPATH (ARPD $VERSION_) into the research project, in place."
    if [ -n "$PLAN_GIT" ]; then
        if [ -n "$ORIGIN" ]; then _w="remote origin $ORIGIN"
        elif [ -s "$TMPD/remotes" ]; then _w="remotes $(join_lines "$TMPD/remotes")"
        else _w="with no remote"; fi
        say "It is a git clone at $COMMIT_, $_w."
        print_list "Other remotes, which go with the kit's history to the backup (note them to add back with git remote add)" "$TMPD/other.remotes" all
    elif [ -n "$PLAN_LISTED" ]; then
        say "It is a download, not a git clone: the kit's files are recognized from $KIT_FILES; any other file, or a kit file whose content you changed, is kept."
    else
        say "It is a download, not a git clone, and has no $KIT_FILES list: every file under the kit entries of $KIT_MARKER is moved to the backup folder."
        warn "files you added inside the kit's folders cannot be told apart from the kit's own and would be moved to the backup folder with them; move them out of those folders first."
    fi
    say ""
    print_list "Kit files to move to the backup folder ($(count "$TMPD/p.R"))" "$TMPD/p.R" all
    _sk=$(kit_skills "$CPATH" | awk '{ printf "%s.claude/skills/%s/", (NR > 1 ? ", " : ""), $0 } END { if (NR == 0) printf "no skills" }')
    say "Kept as they are (the ARPD infrastructure): arpd/ and $_sk."
    print_list "Kit files you changed: kept, not moved ($(count "$TMPD/p.C"); review them)" "$TMPD/p.C" all
    print_list "Your files inside kit folders: kept ($(count "$TMPD/p.K"))" "$TMPD/p.K" all
    print_list "Your other files: kept ($(count "$TMPD/p.P"))" "$TMPD/p.P" all
    print_list "Will be git-ignored (your choice; kept on disk, not committed)" "$TMPD/ignores"
    if [ -s "$TMPD/p.payload" ]; then
        warn "you changed $(count "$TMPD/p.payload") ARPD file(s) in arpd/ or .claude/skills/arpd-*; they are kept as they are, but a later update from a kit will overwrite them:"
        print_list "Changed ARPD files" "$TMPD/p.payload"
    fi
    if [ "$INV_FILES" -gt 0 ] || [ -s "$TMPD/p.E" ]; then
        say "Your material (kept): $INV_FILES file(s), $(mb "$INV_BYTES")."
        print_list "Environments and repositories, kept on disk but git-ignored (not committed)" "$TMPD/p.E" all
        print_list "Files of 50 MB or more, kept but git-ignored" "$TMPD/i.ignore.fmt" all
        print_list "Large files (10 MB or more), kept and committed" "$TMPD/i.large.fmt" all
        print_list "Data-like files, kept and committed (check that they may be kept in the repository)" "$TMPD/i.data" all
    else
        say "Your material: none besides the kit."
    fi
    say ""
    parent_var "$CPATH"
    _h=; [ -n "$PLAN_GIT" ] && _h=" and the kit's git history (.git, with every branch, tag and stash)"
    say "Backup: nothing is deleted. The kit files above$_h are moved to a new folder beside this one, <name>-pre-arpd-backup-<time> in $PARENT, with a RESTORE.md that says how to undo the conversion; delete that folder whenever you no longer need it."
    if [ -n "$PLAN_GIT" ]; then
        say "Git history: the project starts a fresh history (branch main) with no remote."
    else
        say "Git history: there is none yet (not a git clone); the project starts one (branch main) with no remote."
    fi
    if [ -n "$REASONS" ]; then
        print_list "Local work in this clone (on no remote)" "$TMPD/details"
        say "This clone holds work that is on no remote ($REASONS). It is kept in the backup folder's history, but converting needs --include-local-work as well as --yes. If this is a checkout where ARPD itself is developed, do not convert it: use a fresh clone."
    fi
}

move_group() {  # dst_folder relative paths...: move them into the folder, counting MOVED and listing failures in left
    _md=$1; shift
    if [ -d "$_md" ] || mkdir -p "$_md" 2>/dev/null; then
        if mv -- "$@" "$_md/" 2>/dev/null; then MOVED=$((MOVED + $#)); return 0; fi
    fi
    for _f in "$@"; do   # find the files that would not move
        [ -e "$_f" ] || [ -L "$_f" ] || { MOVED=$((MOVED + 1)); continue; }   # moved by the batch above
        if _e=$({ mkdir -p "$_md" && mv -- "$_f" "$_md/"; } 2>&1) && [ ! -e "$_f" ]; then
            MOVED=$((MOVED + 1))
        else
            say "could not move the kit file $_f to the backup folder ($(printf '%s\n' "$_e" | head -n 1)); it is still here: move or delete it yourself" >> "$TMPD/left"
        fi
    done
}

cmd_convert() {
    CPATH=$(abs_path "$POS1")
    is_kit "$CPATH" || refuse "$CPATH is not an ARPD kit (no $KIT_MARKER marker and arpd/ folder there). convert works only on a fresh ARPD kit clone or download; for an existing repository use install, for a new folder use new."
    cd "$CPATH" || refuse "cannot enter $CPATH"
    convert_plan
    [ -n "$PLAN_GIT" ] && refuse_other_worktrees
    VERSION_=$(kit_version "$CPATH"); COMMIT_=$(kit_commit "$CPATH" no)   # the PI's new files are expected
    local_work
    # --ignore: "/" + the path (glob characters escaped), + "/" for a folder; such paths leave the inventory lists.
    : > "$TMPD/ignores"; : > "$TMPD/chosen"
    while IFS= read -r _x <&3; do
        _n=$(printf '%s\n' "$_x" | sed -e 's#\\#/#g' -e 's#^/*##' -e 's#/*$##')
        printf '%s\n' "$_n" >> "$TMPD/chosen"
        _g=/$(printf '%s\n' "$_n" | sed 's/[][*?!#]/\\&/g')
        if [ -d "./$_n" ]; then _g=$_g/; fi
        printf '%s\n' "$_g" >> "$TMPD/ignores"
    done 3< "$TMPD/args.ignore"
    if [ -s "$TMPD/chosen" ]; then
        awk -F "$TAB" 'part == 1 { c[++n] = $0; next }
             { if ($1 == "L" || $1 == "D") for (i = 1; i <= n; i++) if ($2 == c[i] || index($2, c[i] "/") == 1) next
               print }' part=1 "$TMPD/chosen" part=2 "$TMPD/inv" > "$TMPD/inv.kept"
        awk -F "$TAB" '$1 == "L" { printf "%s (%.1f MB)\n", $2, $3 / 1048576 }' "$TMPD/inv.kept" > "$TMPD/i.large.fmt"
        awk -F "$TAB" '$1 == "D" { print $2 }' "$TMPD/inv.kept" > "$TMPD/i.data"
    fi
    print_convert_plan
    exec 4< "$TMPD/ignores"
    while IFS= read -r _n <&3; do
        IFS= read -r _g <&4
        { [ -e "./$_n" ] || [ -L "./$_n" ]; } || warn "--ignore $_g: no such file or folder here; it is added to .gitignore anyway."
    done 3< "$TMPD/chosen"
    exec 4<&-
    location_warnings "$CPATH"
    if [ -n "$YES" ] && [ -n "$DRY_RUN" ]; then
        refuse "--yes and --dry-run cannot be used together. Nothing was changed."
    fi
    if [ -z "$YES" ]; then
        _m=$(identity_problem "$CPATH") || warn "$_m"
        say ""
        say "Review the plan above: nothing changed yet; rerun with --yes to convert this folder."
        exit 0
    fi
    if [ -n "$REASONS" ] && [ -z "$INCLUDE_LOCAL" ]; then
        refuse "this clone holds local work ($REASONS); review it above and rerun with --yes --include-local-work to keep it in the backup folder and convert. Nothing was changed."
    fi
    check_git "$CPATH"
    ID_NAME=$(git -C "$CPATH" config --get user.name 2>/dev/null)
    ID_EMAIL=$(git -C "$CPATH" config --get user.email 2>/dev/null)
    say ""
    : > "$TMPD/left"
    backup_var
    _e=$(mkdir "$BACKUP" 2>&1) || refuse "cannot create the backup folder $BACKUP ($(printf '%s\n' "$_e" | head -n 1)). Nothing was changed."
    HAS_GIT=
    if [ -e .git ] || [ -L .git ]; then   # first, so that a locked file stops everything before any kit file moves
        HAS_GIT=1
        if ! _e=$(mv .git "$BACKUP/.git" 2>&1); then
            rmdir "$BACKUP" 2>/dev/null
            refuse "cannot move the kit's .git to the backup folder ($(printf '%s\n' "$_e" | head -n 1)); close any program using this folder (an editor, a terminal running git) and rerun. Nothing was changed."
        fi
    fi
    # Move the kit files to <backup>/<rel>, one mv per destination folder.
    MOVED=0
    AW_B=$BACKUP awk '{ d = ""; if (match($0, /\/[^\/]*$/)) d = "/" substr($0, 1, RSTART - 1); print ENVIRON["AW_B"] d "\t" $0 }' \
        "$TMPD/p.R" | sort -t "$TAB" -k1,1 > "$TMPD/moves"
    _mg=; set --
    while IFS="$TAB" read -r _mdir _mrel <&3; do
        if [ "$_mdir" != "$_mg" ]; then
            [ $# -gt 0 ] && move_group "$_mg" "$@"
            set --; _mg=$_mdir
        fi
        set -- "$@" "$_mrel"
    done 3< "$TMPD/moves"
    [ $# -gt 0 ] && move_group "$_mg" "$@"
    while IFS= read -r _e <&3; do   # only empty folders
        if [ -d "./$_e" ]; then find "./$_e" -depth -type d -exec rmdir {} \; 2>/dev/null; fi
    done 3< "$TMPD/manifest"
    write_restore "$HAS_GIT"
    cat "$TMPD/i.ignore" "$TMPD/p.E" "$TMPD/ignores" > "$TMPD/extra"
    git_init "$CPATH"
    # An identity set only in the kit clone's own config went with its .git.
    if [ -n "$ID_NAME" ] && [ -z "$(git -C "$CPATH" config --get user.name 2>/dev/null)" ]; then gitc "$CPATH" config user.name "$ID_NAME"; fi
    if [ -n "$ID_EMAIL" ] && [ -z "$(git -C "$CPATH" config --get user.email 2>/dev/null)" ]; then gitc "$CPATH" config user.email "$ID_EMAIL"; fi
    ensure_gitignore "$CPATH" "$TMPD/extra"
    _stub=1; write_stub_claude "$CPATH" "$NOTES" || _stub=
    if [ -n "$PLAN_GIT" ]; then _src="Converted from: the ARPD kit clone (${ORIGIN:-no remote}) at $COMMIT_"
    else _src="Converted from: an ARPD kit download (not a git clone)"; fi
    if [ -s "$TMPD/other.remotes" ]; then _src="$_src
$(sed 's/^/Remote removed at conversion: /' "$TMPD/other.remotes")"; fi
    write_version "$CPATH" convert "$VERSION_" "$COMMIT_" - "$_src"
    _msg="Start ARPD project in place (setup in progress)"
    commit_all "$CPATH" "$_msg" force "Do NOT delete this folder: it holds your files, and the conversion is otherwise done (do not rerun convert). Fix the signing or identity problem git reports, then run  git add -A  and  git commit -m \"$_msg\"  in $CPATH."   # extra: already in .gitignore
    [ -s "$TMPD/p.C" ] && say "review the kit files you changed, kept and committed: $(join_lines "$TMPD/p.C")" >> "$TMPD/left"
    [ -s "$TMPD/p.payload" ] && say "your changes to ARPD files are kept, but a later update from a kit will overwrite them: $(join_lines "$TMPD/p.payload")" >> "$TMPD/left"
    _h=; [ -n "$HAS_GIT" ] && _h=" and the kit's git history (every branch, tag and stash)"
    say "Moved $MOVED kit file(s)$_h to the backup folder $BACKUP. Nothing was deleted."
    say "    To undo the conversion, follow $BACKUP/RESTORE.md; delete that folder when you no longer need it."
    _nc=$(count "$TMPD/p.C"); _x=
    [ "$_nc" -gt 0 ] && _x=", and $_nc kit file(s) you changed"
    say "Kept: arpd/, the ARPD skills and your material ($INV_FILES file(s))$_x."
    [ -s "$TMPD/extra" ] && say "Git-ignored (kept on disk, not committed): $(join_lines "$TMPD/extra")"
    if [ -n "$_stub" ]; then say "Wrote the stub CLAUDE.md (setup in progress)."
    else say "The existing CLAUDE.md was kept (you changed it) and not replaced by the setup stub; review it."; fi
    say "Started a fresh git repository (branch main) and committed $SHA: Start ARPD project in place (setup in progress)."
    say "No remote is configured; nothing was pushed."
    if [ -s "$TMPD/left" ]; then
        say "Left to you:"
        indent "$TMPD/left"
    fi
    say "Setup continues in this session."
    [ -s "$TMPD/left" ] && exit 2
    exit 0
}

# --- arguments ----------------------------------------------------------------------------------

[ $# -gt 0 ] || { usage; exit 1; }
CMD=$1; shift
case $CMD in
    -h | --help) usage; exit 1 ;;
    convert | new | import | install | update | owed) ;;
    *) usage_error "argument command: invalid choice: '$CMD'" ;;
esac
POS1= POS2= NPOS=0 YES= FORCE= PRUNE= KITARG= NOTES_ARG= INCLUDE_LOCAL= DRY_RUN= OPTS=
: > "$TMPD/args.ignore"
need() { [ "$1" -ge 2 ] || usage_error "argument $2: expected one argument"; }
while [ $# -gt 0 ]; do
    case $1 in
        --yes) YES=1; OPTS="$OPTS yes" ;;
        --force) FORCE=1; OPTS="$OPTS force" ;;
        --prune) PRUNE=1; OPTS="$OPTS prune" ;;
        --include-local-work) INCLUDE_LOCAL=1; OPTS="$OPTS include" ;;
        --dry-run) DRY_RUN=1; OPTS="$OPTS dryrun" ;;
        --kit) need $# --kit; KITARG=$2; OPTS="$OPTS kit"; shift ;;
        --kit=*) KITARG=${1#--kit=}; OPTS="$OPTS kit" ;;
        --notes) need $# --notes; NOTES_ARG=$2; OPTS="$OPTS notes"; shift ;;
        --notes=*) NOTES_ARG=${1#--notes=}; OPTS="$OPTS notes" ;;
        --ignore) need $# --ignore; printf '%s\n' "$2" >> "$TMPD/args.ignore"; OPTS="$OPTS ignore"; shift ;;
        --ignore=*) printf '%s\n' "${1#--ignore=}" >> "$TMPD/args.ignore"; OPTS="$OPTS ignore" ;;
        -h | --help) usage; exit 1 ;;
        -?*) usage_error "unrecognized arguments: $1" ;;
        *) NPOS=$((NPOS + 1))
           case $NPOS in 1) POS1=$1 ;; 2) POS2=$1 ;; *) usage_error "unrecognized arguments: $1" ;; esac ;;
    esac
    shift
done
case $CMD in
    convert) ALLOWED="yes include ignore dryrun"; WANT=1 ;;
    new) ALLOWED="kit"; WANT=1 ;;
    import) ALLOWED="yes force kit"; WANT=2 ;;
    install) ALLOWED="force notes kit"; WANT=1 ;;
    update) ALLOWED="prune kit"; WANT=1 ;;
    owed) ALLOWED="force kit"; WANT=1 ;;
esac
for _o in $OPTS; do
    case " $ALLOWED " in *" $_o "*) ;; *) usage_error "unrecognized arguments for $CMD: --$_o" ;; esac
done
[ "$NPOS" -ge "$WANT" ] || usage_error "the following arguments are required for $CMD: $(if [ "$WANT" = 2 ] && [ "$NPOS" = 1 ]; then echo path; elif [ "$WANT" = 2 ]; then echo source, path; else echo path; fi)"
[ "$NPOS" -le "$WANT" ] || usage_error "unrecognized arguments: $POS2"
command -v git >/dev/null 2>&1 || refuse "git is not installed or not on PATH; install it from https://git-scm.com and rerun"

case $CMD in
    convert) cmd_convert ;;
    new) cmd_new ;;
    import) cmd_import ;;
    install) cmd_install ;;
    update) cmd_update ;;
    owed) cmd_owed ;;
esac
