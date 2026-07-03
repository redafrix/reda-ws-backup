# Experiment README Schema

Every catalog entry must answer these questions before its result is trusted:

1. Which host and original path contain the raw artifacts?
2. Was the experiment offline training, data collection, smoke testing, or online rollout?
3. Which exact SimVLA checkpoint generated the actions?
4. Which risk detector and action-selection policy were active?
5. Which suite, task, perturbation, reset seeds, and action seeds were used?
6. Was execution first-action receding horizon, five-action chunks, or ten-action chunks?
7. How was success defined, and were exceptions excluded from success counts?
8. Are raw per-episode files present, or is only an aggregate report available?
9. Is the result complete, partial, active, archived, or semantically unverified?
10. What conclusion is supported, and what stronger conclusion is not supported?

Directory names and old prose labels are not sufficient evidence. The catalog records semantic corrections separately from original artifacts so historical files remain unchanged.
