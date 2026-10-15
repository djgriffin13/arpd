## B.S-MEAS: Measurement pipeline

*Module: measurement-pipeline v1.0. Select this when the instrument derives measures from existing
behavioural, trace, text, audio, video or telemetry data. One example is objective coordination
measures computed from game or sensor logs.*

1. **Every measure has a definition in the paradigm spec** (CON → OP). The code implements that
   definition and no other. A "better" variant is a proposal, not a change.
2. **Every measure has a reference calculation.**
   - A small, hand-checkable case, worked by hand or by an independent script, that the
     implementation must reproduce exactly.
   - The reference is never edited to match the code.
3. **Coverage is reported with every measure.** Report how many units, events or time windows it
   could be computed for, how many it could not, and why. A measure that could not be computed is
   reported as missing, never as zero.
4. **Raw → normalized → derived is one direction.**
   - Normalization is source-agnostic.
   - Derived measures read only normalized data.
   - Each layer is written by one component.
5. **Time is explicit.** Timestamps carry their unit and source clock. Intervals are half-open.
   Alignment between data sources is a documented, tested rule, never a guess.
6. **Repeatability.** Running the pipeline twice on the same input gives identical output. A test
   checks this.
7. **Validity evidence is separate from correctness.** Matching the reference calculation shows the
   code is right. Evidence that the measure captures the construct comes from the paradigm spec's
   VAL items, for example convergence with expert ratings, known-groups differences, or sensitivity
   to a manipulation. Only that evidence makes a measure *Validated*.
8. **More data is not more meaning.** Do not add measures because the data allow them. A new
   measure needs a construct it serves and a ruling.
