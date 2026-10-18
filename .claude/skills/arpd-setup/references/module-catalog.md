# Module catalogue

Install the fewest modules that fit. Context files that state generic practice add cost without
benefit, while project-specific, non-standard rules are what help (Gloaguen et al., 2026). Turning on
every teamwork module can hurt (Mishra et al., 2025).

Select a module only when this project needs it: for the instrument actually requested, and for the
scientific help the PI asked for (the theory-context choice). Never select one "just in case". For
product-only work, the team-arrangement module may be the only one, plus human-subjects data when
real data about people are collected. A science module's candidate invariants are proposed only
when the science is in scope (`interview-guide.md`, *Theory context*), or when correctness depends
on its semantics. Say in report §11 which modules were selected, and why, and summarize the rules
each one adds, so the PI sees what the charter will contain.

| Module | File (`arpd/constitution/modules/`) | Status | Recommend when | Candidate invariants to propose (in scientific language) |
|---|---|---|---|---|
| **Team arrangement** | `team/team-arrangement.md` | **Built** | Always | none |
| **Computational model** | `science/computational-model.md` | **Built** | Agent-based models, simulations, replications or extensions of formal models | "Each update rule is applied exactly as specified (order, timing, stopping rule)"; "Results are reported with Monte Carlo uncertainty"; "With extensions off, the original model's results are reproduced"; "A run is fully determined by its parameters and seed" |
| Statistical methods | `science/statistical-methods.md` | Draft | Estimators, statistical models, methods packages | "Unidentified models are refused, not estimated"; "Missing is not zero"; "Orientation and coding of the data are fixed at import"; "Known published estimates are reproduced within a stated tolerance" |
| Experiment platform | `science/experiment-platform.md` | Draft | Lab or online experiments, games, team tasks with participants | "Conditions differ only in the manipulated element"; "Every participant action is logged with timestamp and condition"; "Assignment is randomized and recorded" |
| Measurement pipeline | `science/measurement-pipeline.md` | Draft | Deriving measures from trace, telemetry, text, audio or video | "Each measure implements exactly its stated definition"; "Measures not computable are missing, never zero"; "Coverage is reported with every measure"; "Same input gives identical output" |
| Agents inside the instrument | `science/simulated-agents.md` | Draft | AI partners, confederate bots, simulated participants | "The agent's update rule and its timing are as specified"; "The agent's internal state is logged with every action"; "Simulated participants are never reported as people" |
| Human-subjects data | `science/human-subjects-data.md` | Draft | Any real data about people | "No participant data enter the repository"; "Collection changes follow the ethics approval" |

**Draft modules** may be installed, but tell the PI they are untested drafts. Record that in the
charter's Part B header line for the module.

## Not yet available

These are planned and documented from practice, but not packaged. Mention them only if asked:

- autonomous mode;
- cross-repository contracts;
- tiered test gates.
