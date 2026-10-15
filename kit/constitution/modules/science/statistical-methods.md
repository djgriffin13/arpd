## B.S-STAT: Statistical methods

*Module: statistical-methods v1.0. Select this when the instrument estimates models, computes
statistics, or implements a method from the methodological literature.*

1. **Only established methods ship under established names.**
   - A construction with no published warrant is labelled as this project's own.
   - A departure from a cited source is named where it occurs, in code comments and in the output.
2. **Every estimator states its assumptions and its known problems in the output.** An approximation
   is never hidden. A result names the estimator, the approximation used, and what it does not
   address.
3. **Identification is checked before estimation.**
   - Unidentified: refuse, and name the fix.
   - Weakly identified: warn.
   - Empirically unstable: warn after fitting.
   - The message says which of these it is.
4. **Orientation, coding and scale are fixed once, at import.** Examples are which way a tie points,
   which category is the reference, and whether a variable is centred. They are recorded as
   paradigm-spec invariants and never changed silently afterwards.
5. **Missing is not zero, and it is not structural absence.** Each data-consuming step has a test
   with missing cells.
6. **No pass/fail verdicts on fit unless the paradigm spec licenses them.** Report fit profiles with
   their known limits.
7. **Known-answer tests are the backbone.**
   - Every estimator has at least one test that recovers known generating parameters within a stated
     tolerance on simulated data.
   - Where possible, it also has a comparison with an established implementation on shared data
     (an *oracle*).
   - Oracle outputs are regenerated only by their scripts.
   - Tolerances are relative, stated, and justified.
8. **Development simulations vs validation studies.**
   - *Development simulation:* does the code do what the design says? It is small (seconds to a
     few minutes), targeted at one question, run without approval, recorded in one or two lines,
     and never cited as evidence about the method.
   - *Validation study:* how well does the method work (bias, coverage, power, robustness,
     comparisons)? It is a planned study in `validation/`, with a preregistered design (aims, data
     generation, estimands, methods, performance measures), Monte Carlo standard errors and a
     committed results file. Anything over about an hour of compute, or any cluster run, needs the
     PI's approval in words after a stated runtime estimate.
   - The boundary test: a number about *this code* is development; a number about *a method* is
     validation.
9. **Deterministic by construction.** Seeds are recorded. Results are reproducible bit for bit on the
   same platform, or the reason they are not is documented.
10. **Do not stop development to run ever-larger simulations.** Queue validation questions in
    `validation/QUEUE.md` and continue.
