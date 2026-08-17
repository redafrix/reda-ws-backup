# Dean Isaac OOD150 Online Risk Intervention Protocol — 2026-08-17

## Goal
Measure whether the **current V1 true-H10 Isaac risk head** can improve SimVLA task success in closed loop on the exact locked OOD150 scenes.

## Controller being ported
This is the final LIBERO TopK8 online logic used in the publication campaign, ported to Isaac without changing the VLA:

1. At every H10 replan, sample the normal SimVLA main chunk plus 8 seeded alternatives (9 total).
2. Compute one `new_training` ACE vector from alternatives 1..8, exactly as in the trained feature contract.
3. Build candidate-specific 49D uncertainty descriptors for all 9 candidate chunks.
4. Score all 9 H10 chunks with the single trained 51D-static SeqRiskModel.
5. If the main score is below the main alarm threshold, execute main H10.
6. Otherwise find the lowest-risk alternative. Select it only if its score is <= the selected-score cap.
7. Margin is exactly zero. Execution remains H10; no H1/horizon-shortening is used.

This corresponds to the final LIBERO `argmin_on_alarm` + `selection_max_selected_score` logic. The historically successful Goal-Object-OOD configuration used `best_val_f1` as the main threshold and `q90_success` as selected-score cap with zero margin.

## Current Dean model fixed before online testing
- model: `models/isaac_h10_topk8_temporal_v1/model.pt`
- expected SHA256: `ad049519746913c4c2ce1a0b57fb32ad5c3395f5bce6841648c68cc94f862b38`
- normalization SHA256: `78c934b33e0536bd7cb6b7e5b1962da32305729f602d8269d3a38422841ce050`
- all threshold values come from the already frozen seen-validation `thresholds.json`
- strict success definition remains 2 cm with 0.2 s settle time
- baseline OOD150 remains the already-audited 72/150 SimVLA H10 run.

## Anti-leak controller selection
The risk model, normalization and numeric thresholds remain seen-only. We do permit **controller-pair selection** on OOD, but we do not select and report on the same episodes:

- `dev40`: fixed deterministic 20 baseline-success + 20 baseline-failure OOD scenes. All six predeclared threshold/cap pairs run here.
- `holdout110`: untouched remaining OOD scenes. Exactly one selected controller runs here after dev selection.
- primary final success claim = held-out 110 episodes.
- secondary descriptive result = selected controller across all 150 (its dev40 + its holdout110); this is not called an unbiased locked-test estimate because dev40 influenced controller selection.

Selection on dev40 is deterministic: maximize online successes, then minimize regressions, then minimize changed episodes, then lexical variant id.

## Predeclared grid
See `configs/threshold_grid.json`. No values may be added after observing dev outcomes.

## Mandatory parity gate
Before any active intervention, run source episodes 0,1,2 in `shadow` mode. The controller computes scores/selections but executes the main candidate. Baseline and shadow must match in outcome, step counts, all main/ACE chunks, ACE, uncertainty49, history and executed action sequences at tolerance 1e-6. Failure aborts the protocol.

## HARD1000 handling
HARD1000 is paused only via stop markers after the current episode. No process is killed. Its stop markers remain in place until the online protocol completes. A separate resume script is provided but is **not** run automatically.
