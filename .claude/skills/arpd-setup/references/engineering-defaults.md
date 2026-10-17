# Engineering defaults (propose these, with the reason, in plain language)

Choose by **who will use the instrument**, and **what it must plug into**. Always give the one-line
reason, and accept the PI's correction.

| Instrument | Default proposal | Plain-language reason |
|---|---|---|
| Computational model or simulation | **Python package** with numpy; tests with pytest; results to CSV | "Widely used for simulation, easy to read, and results open in R, Stata or Excel." |
| Statistical method for R users | **R package** (testthat tests, roxygen docs) | "Your colleagues can install and use it the way they use other R tools." |
| Statistical method, general | Python package, plus an R wrapper later if needed | "Fast to build and test; the R wrapper can come once the method is validated." |
| Online experiment or game | **Web app**: a Python (FastAPI or Flask) server with a simple browser front end; SQLite during development; CSV export | "Participants only need a browser link; the data export is one row per action." |
| Measurement from existing data files | **Python command-line pipeline** that reads raw files and writes tidy CSV, with a coverage report | "Re-runnable on new data with one command; every measure traceable to its definition." |
| Desktop tool for the PI | Python with a simple local web interface | "Avoids installation problems; runs on your machine." |

**Always, regardless of platform:**

- Git from day one, with small commits that explain *why*.
- One command runs the test suite. Name it in `START-HERE.md`, e.g.
  `python -m pytest --ignore=kit --ignore=examples`: the kit's own tests are not project tests
  (`generation-checklist.md`, *The project's test command*).
- Seeds recorded for anything random.
- Outputs go to a git-ignored `output/` folder unless a ruling makes them part of the record.
- No real participant data in the repository.
- Dependencies: few, well-known, and permissively licensed. A new dependency with licence or cost
  implications is consequential (charter §6).

Avoid proposing anything the PI would need a developer to maintain unless they asked for it:
microservices, containers, GPU, cloud deployment.
