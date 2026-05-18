# Stage 9 Object/Goal Distance Check

Exact goal pose: not exposed as a clean dedicated goal coordinate in the current wrapper.

Available fallback: observation keys include many `*_to_robot0_eef_pos` vectors, and the pipeline now computes relation-distance changes (`best_approach_delta`, `worst_relation_worsen_delta`). This is useful for approach progress but is not the same as object-to-goal progress.

Pilot result: later-state pilot labels mostly used weak approach evidence, not sparse reward or goal completion. This is why labels collapsed to GOOD.

Decision: before final collection, implement task-aware target object and receptacle/goal parsing from BDDL or LIBERO predicates. The current approach metric is insufficient for final GOOD/BAD labeling.
