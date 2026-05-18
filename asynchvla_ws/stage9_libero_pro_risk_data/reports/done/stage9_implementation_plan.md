# Stage 9 Implementation Plan

Goal: collect real LIBERO-PRO counterfactual short-horizon action-risk labels from real SimVLA-generated candidate action chunks.

Implemented as a separate pipeline under `stage9_libero_pro_risk_data` and `src/data_collection_stage9`.

Validation order:
1. Observation/signal audit.
2. Same-state reset determinism.
3. SimVLA seed repeatability.
4. Controlled action label sanity.
5. Object/drop/goal/contact availability.
6. Label distribution pilot.
7. Visual label debug.
8. Label consistency audit.
9. Label learnability smoke.

Final collection is not launched unless reset determinism, signals, SimVLA seed repeatability, label sanity, and pilot quality pass.
