# Import baseline, {{YYYY-MM-DD}}

**Informative evidence.** This report records the imported project's state before ARPD changed
anything. It decides nothing (`CLAUDE.md` §2). The import decision (DEC-NN in `DECISIONS.md`) cites
it. When the first sprint starts, its Part 1 cites it too. Neither copies it.

**Written once, then frozen.** Record outputs verbatim, including failures. Never report the
baseline as better than it is. A later run goes in a sprint record, not here.

---

## 1. Source and provenance

| Field | Value |
|---|---|
| Origin | {{local path, or git URL}} |
| Commit | {{SHA of the source commit inspected, or "not a git repository"}} |
| Date inspected | {{date and time in UTC}} |
| Where it was inspected | {{in place / a temporary clone outside this repository}} |
| Brought in as | {{history as a subdirectory / history at the root / a plain copy, committed as <SHA>}} |
| Cited by | DEC-NN; the first sprint's Part 1 (when it starts) |

## 2. Commands run

Each command exactly as run, with its working directory and its output verbatim.

### {{command}}

- **Working directory:** {{path}}
- **Exit code:** {{n}}

```text
{{output, verbatim}}
```

## 3. Test counts

| Suite or command | Passed | Failed | Skipped | Errors | Notes |
|---|---|---|---|---|---|

## 4. Governance checker output

Only if the source has an ARPD checker (`tools/check_governance.py` in an older starter,
`arpd/tools/check_governance.py` from v0.6). Otherwise write "No checker in
the source".

```text
{{output, verbatim}}
```

## 5. What was not run

List each check that was not run, and why (for example: needs data that is not in the repository,
needs a service, would run longer than allowed). Write "Nothing" only when nothing was skipped.
