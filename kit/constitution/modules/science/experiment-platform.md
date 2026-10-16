## B.S-EXP: Experiment platform

*Module: experiment-platform v0.1 (**draft, untested**). Select this when the instrument presents tasks, stimuli or
partners to human participants, for example a lab game, a team task or a survey experiment.*

1. **The manipulation is an invariant.**
   - Conditions differ only in what the paradigm spec says they differ in.
   - Instructions, timing, layout and feedback are otherwise identical, and a test checks this.
   - Any change to what a participant sees or experiences is consequential (charter §6).
2. **Every participant action is logged at the finest grain the paradigm spec names.** That means
   the event, the actor, the condition and a timestamp. Nothing is logged only in aggregate.
   Researchers can always aggregate later; they cannot disaggregate.
3. **Logs are append-only and versioned.** Each log records the instrument version (the commit),
   the condition assignment, and the configuration that produced it. A log that cannot be traced to
   a version is not data.
4. **Randomization and assignment** are implemented once. They are seeded and recorded, and tested
   for balance on simulated sessions.
5. **Pilot with simulated participants before people.** Scripted or simulated sessions exercise
   every condition and path. A full simulated session's log is checked against the paradigm spec's
   operationalizations.
6. **The PI's walkthrough is run as a participant would experience it,** in every condition, before
   any real data are collected.
7. **No deception, consent or debriefing content changes without the PI,** and nothing changes
   without ethics approval where the paradigm spec says one applies.
8. **Data export** matches a documented codebook (`docs/CODEBOOK.md`). It has one row per unit at
   the level named in the paradigm spec, and every variable is defined.
