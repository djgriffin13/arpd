## B.S-MODEL: Computational and simulation models

*Module: computational-model v1.0. Select this when the instrument is a computational model whose
behaviour is the object of study. Examples: agent-based models, simulations of organizational
learning, search on fitness landscapes, system-dynamics models. It applies whether the model is
replicated from the literature, extended, or built new.*

### Three kinds of evidence, kept apart

Every report keeps these three separate. Never let one stand in for another.

| Evidence | Question it answers | Typical checks | Where it lives |
|---|---|---|---|
| **Software verification** | Does the code implement the rules as specified? | Deterministic unit tests of each rule on hand-built cases, including edge cases where a rule must or must not fire. Seed reproducibility. | `tests/test_verification*` |
| **Replication fidelity** | Does the model reproduce the published or reference results it claims to reproduce? | Direction and size of published effects, under the published parameters, with Monte Carlo uncertainty | `tests/test_replication*`, `RESULTS.md` |
| **Extension evidence** | Does a new mechanism behave as its specification says? And what does it show? | Checks specific to the extension: limiting cases, a known-answer case, sensitivity. Results reported with uncertainty and with the stated assumptions. | `tests/test_extension*`, `RESULTS.md` |

Passing verification does not establish fidelity. Fidelity does not establish that an extension is
right. Only the PI's ruling, on the paradigm spec's VAL items, makes a requirement *Validated*.

### Rules

1. **Every rule is specified before it is coded.** Each model rule is written in the paradigm spec
   as an invariant or operationalization:
   - its update rule;
   - its order within a period (simultaneous or sequential);
   - its stopping rule;
   - its initial conditions.

   Where the source is ambiguous, record the interpretation chosen as an **assumption** (ASM-NN in
   the spec), with the alternative and why it was not chosen. Tag the code that implements it with
   the same ID.
2. **Determinism.** A run is fully determined by its parameters and seed. Every result file records
   both, along with the code commit.
3. **Stochastic uncertainty is always reported.** Report means with Monte Carlo standard errors (or
   intervals) and the number of replications. A difference is described as a difference only if it
   is large relative to its uncertainty. The criterion is stated in advance.
4. **Replication checks are never weakened.** If a replication check fails:
   - first look for a rule ambiguity, and record it;
   - never tune parameters or tolerances to make it pass without a ruling.

   A failed replication is a reportable result.
5. **Extensions are switchable and default to off.** An extension is added through a documented
   extension point, not by editing core rules.
   - **With every extension disabled, the original model's verification and replication checks
     must still pass,** and core output must be identical for the same seed.
   - This "extension-off identity" is checked by a test.
6. **Development runs vs studies.** Small runs that check the code are development checks (charter
   §7). Parameter sweeps that say something about the *model's behaviour* are studies:
   - planned in a plan;
   - with the design stated before running (parameters, replications, outcomes);
   - results committed with the seed and commit.
7. **Outputs** go to a git-ignored output directory, unless a ruling makes a result part of the
   record, in which case it is committed alongside `RESULTS.md`.
8. **Claims not to make.** Every model's paradigm spec lists what its results do not license. For
   example: a model result is not evidence about real organizations without external validation, and
   a parameter's effect holds only within the explored range.
