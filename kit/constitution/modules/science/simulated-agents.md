## B.S-SIM: Agents inside the instrument

*Module: simulated-agents v1.0. Select this when the instrument contains artificial actors, such as
an AI partner, a confederate bot, or simulated team members or populations.*

There are two kinds of agent in this project. Never confuse them:

- **builder agents** develop the instrument;
- **instrument agents** act inside it.

Evidence that the build process works says nothing about whether an instrument agent behaves as
the science requires.

1. **The instrument agent's behavioural model is specified in the paradigm spec.** That means:
   - what it observes;
   - what it believes or learns;
   - how and *when* it updates;
   - how it chooses actions;
   - what is held fixed across conditions.
2. **Its policy is deterministic given its seed and inputs,** or its randomness is explicit and
   recorded.
3. **The update rule is tested against hand-computed cases.** A passing unit test for an update
   function shows the code implements the rule. It does not show that the rule represents the
   human or organizational process it stands for. Only VAL items do that.
4. **The agent's internal state is logged alongside participant actions,** so that analyses can link
   what the agent "believed" to what it did and to how people responded.
5. **No language model inside the instrument unless the paradigm spec calls for it.** If one is used:
   - pin the model version;
   - log every prompt and response;
   - treat its variability as part of the manipulation, to be measured.
6. **Synthetic participants are not participants.** Results from simulated people may test the
   instrument. They are never reported as evidence about people.
