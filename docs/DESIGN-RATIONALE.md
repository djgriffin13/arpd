# Design rationale

Each mechanism in the kit is traced to:

- the coordination problem it addresses;
- its team-science anchor;
- the human–LLM agent-team guideline it implements (Yurrita et al., 2026: G1–G24);
- the adjacent empirical evidence;
- the practice that motivated it;
- **the type of evidence for it.**

**Evidence types**

- **Theory:** a team-science or organizational argument.
- **Adjacent:** empirical results from other agent settings, such as benchmarks or other domains.
- **Practice:** observed in the practitioner records the kit was distilled from. These are the
  governing records of three agent-built research instruments, referred to here as Projects A–C.
  This is descriptive, not causal.
- **Tested here:** evaluated in this project's own studies. **None yet.** See `evaluation/`.

Nothing below is claimed to be effective. Each row is a design rationale and a hypothesis.

## Mechanisms

| Mechanism (where) | Problem addressed | Team-science anchor | Guideline | Adjacent evidence | Practice origin | Evidence type |
|---|---|---|---|---|---|---|
| **Team charter**: a standing operating agreement, separate from sprint plans (`CLAUDE.md`) | No shared, durable agreement on how the team works | Team charters and performance strategies (Mathieu & Rapp, 2009) | G3, G8 | Constitutions measurably change agent coordination (Kumar et al., 2026). Codified context sustained a large codebase (Vasilopoulos, 2026). Generic context files add cost without benefit (Gloaguen et al., 2026). | Projects A–C: a charter read every session | Theory; adjacent; practice |
| **Lean core plus modules chosen to fit the task** | Governance overhead; mismatch between rules and task | Task–team fit; structural interdependence (Courtright et al., 2015) | G3 | Turning on all teamwork modules hurt performance (Mishra et al., 2025). Added contracts and verification lowered scores (Liu et al., 2026). | Practice: the charter shrank from one project to the next | Theory; adjacent |
| **Authority by subject; informative documents decide nothing** | Conflicting "sources of truth"; the newest document silently winning | Accountability and predictability as coordination conditions (Okhuysen & Bechky, 2009) | G15 | — | Project B, early period: about 20 overlapping documents, with status stated in four places | Theory; practice |
| **The PI's rulings recorded verbatim; relayed messages carry no authority** | Drift of goals through paraphrase; one agent's approval treated as the human's | Functional leadership: setting direction (Morgeson et al., 2010) | G16 | — | Project B: a relayed approval taken as the human's; goals kept only as a paraphrase widened the agents' authority | Theory; practice |
| **Paradigm specification** (constructs → operationalizations → invariants → claims and claims not to make → validation) | Software that is correct as code but wrong as science; drift away from the construct | Shared task understanding (Mathieu et al., 2000; DeChurch & Mesmer-Magnus, 2010) | G9, G10 | A non-engineer's agent-built system held up only when outcome, evidence, permissions and decisions traced to one objective (Ferris & Bonilla, 2026) | Project C: a statistical claim withdrawn as "wrong in this document before it was wrong in the code" | Theory; adjacent; practice |
| **Implemented ≠ Verified ≠ Validated** | Premature claims of done; software tests taken as scientific validity | Monitoring and verification within team processes (Marks et al., 2001) | G10, G11 | Experience-dependent ability to verify AI output (Fawzy et al., 2026) | Project B: an agent reported "verified" over 48 compilation errors (early, single-agent period) | Theory; adjacent; practice |
| **Decision routes by scientific consequence × delegated authority** (routine / delegated / consult). Delegation is recorded only as standing authorizations: an authority profile (consult first / bounded / exploratory) agreed at setup as SA-01, and narrower SAs the PI adds or changes in any message; all persist across sessions. Nothing consequential is adopted without the authority its route requires; defaults, not questions | The PI either flooded with routine questions or bypassed on consequential ones; autonomy left implicit, so the same permission questions recur | Levels of automation by function (Parasuraman et al., 2000); empowering vs directive leadership (Morgeson et al., 2010); attention as a scarce resource | G13, G14 | Human–AI combinations gain when the human adds what the AI lacks (Vaccaro et al., 2024) | Projects B and C: decision packs with defaults; autonomy granted and withdrawn by ruling. The March investigation needed exploratory authority | Theory; adjacent; practice |
| **Decisions explained by scientific consequence** | PhD researchers without engineering vocabulary | Expertise coordination (Faraj & Sproull, 2000) | G5, G6, G12 | — | Practice: plain-language summaries without internal IDs | Theory; practice |
| **Independent review: the reviewer did not write the change; evidence, not opinion** | Self-certification; correlated errors | Mutual performance monitoring and backup behaviour (Salas et al., 2005) | G11, G15 | LLM judges' errors are correlated: nine judges are worth about two votes (Kohli, 2026). Hierarchical send-backs on opinion lowered quality (Agachan et al., 2026). | Projects B and C: separate implementer and reviewer roles | Theory; adjacent; practice |
| **Known-answer tests never weakened; development checks vs studies** | Tests tuned to pass; toy runs cited as evidence | — | G11 | — | Project C: protected known-answer tests; the distinction between development simulations and validation studies | Practice |
| **Sprints with auditable close-outs and decision tracking** | Unrecoverable rationale; no basis for audit | Transition and action phases (Marks et al., 2001); debriefs (Tannenbaum & Cerasoli, 2013) | G15, G17, G18 | Persistent, milestone-driven development with verification phases (Lyu et al., 2026) | Projects A–C: plans, close-out records, gate records | Theory; adjacent; practice |
| **One status writer; STATUS.md as the handoff** | Context loss across session resets; conflicting status | Transactive memory (Wegner, 1987; Lewis, 2003) | G15 | Visibility of peers' state drove multi-agent gains (Özaytürk & Buzluca, 2026) | Project B: the coordinating agent unreachable for five hours left every agent idle | Theory; adjacent; practice |
| **Team × workspace arrangement chosen by task structure; separate runtime resources** | More agents than the task can use; interference | Task interdependence (Thompson, 1967; Courtright et al., 2015) | G2, G3 | Benefits depend on task and baseline capability (Kim et al., 2026). Interference rises beyond two agents (Özaytürk & Buzluca, 2026). | Project B: a shared port let one agent drive another's client; interleaved logs | Theory; adjacent; practice |
| **Acknowledgement ("10-4"); a wait needs a correctness reason** (peers) | Lost messages; idle agents | Closed-loop communication (Salas et al., 2005) | G12, G13 | — | Project B: two lost-message episodes; builders idle waiting on the integrator | Theory; practice |
| **Discovery is not scheduling** | Scope drift toward interesting side-work | Goal monitoring (Marks et al., 2001) | G16 | Specification and misalignment failures (Cemri et al., 2025) | Project B: six discovery categories, introduced by ruling | Theory; adjacent; practice |
| **Incidents → rules; rules retired; justified reopening** | A rule set that only grows; rationale lost when decisions change | Team reflexivity (Schippers et al., 2015); double-loop learning | G18, G20, G21 | Collective reflexivity improved agent teams; frozen configurations were evaluated on held-out cases (Hao et al., 2026) | Projects B and C: 13 charter amendments, each citing a ruling | Theory; adjacent; practice |
| **Event logging, with stated limits** | Unmeasured human effort; productivity claims based on perception | — | G15, G21 | Perceived productivity diverged from measured time (Becker et al., 2025) | — | Adjacent |

## Coverage of the human–LLM agent-team guidelines (Yurrita et al., 2026)

The guidelines were developed from an expert workshop and a review of 93 papers, and were evaluated
by experts on scenarios. **The kit offers a deployed implementation of most of them. Its evaluation
is planned.**

| Status | Guidelines |
|---|---|
| Implemented by kit mechanisms | G1 (setup: is a team warranted, and who owns what), G2, G3, G4, G5 (limits stated at setup), G6 (PI profile), G8, G9, G10, G11, G12, G13, G14, G15, G16, G18, G20, G21 |
| Partly implemented | G7 (QUICKSTART, START-HERE; no training materials yet); G17 (version control records agent involvement; a disclosure statement for papers is planned); G19 (model versions recorded; re-checking after model updates is planned) |
| Not applicable to builder agents | G22 (personality and embodiment), G23 (emotional needs). Agents *inside* instruments are covered by the simulated-agents module. |
| Stated limitation | G24 (interpersonal dynamics when several researchers share one agent team) |

## Prior tools and how the kit differs

| Prior tool or system | Overlap | Difference |
|---|---|---|
| Spec Kit (constitution, clarify, plan, analyze) | A governing document; clarifying questions; consistency checks | The science layer (paradigm spec; Validated as a separate state); team roles and decision rights; a non-developer principal |
| BMad Method; GSD discuss mode | A setup interview; durable decision artifacts | The same differences, plus verbatim rulings, and decision routes under which nothing consequential is adopted without the PI's authority |
| Superpowers (subagent-driven development) | Delegation to fresh subagents; review; a decision ledger | Explicit researcher authority over scientific decisions; auditable sprint records |
| Codified Context | An always-loaded constitution; specialist agents; on-demand specifications | A non-developer principal; the science layer; a planned controlled evaluation |
| Meta-Team | A team-reflexivity-based, evolving team constitution | A human principal who rules on changes; sustained instrument development; adoption by new users |
| Claude Code agent teams; subagents | The execution substrate | The kit is a governance layer over the substrate, not a substitute for it |

The claim is about the **integration** of these mechanisms for researcher-directed instrument
development, and its evaluation. It is not a claim that any single component is new.

References are listed in `docs/REFERENCES.md`.
