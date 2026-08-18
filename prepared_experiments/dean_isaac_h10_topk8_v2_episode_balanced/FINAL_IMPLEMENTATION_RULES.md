# FINAL IMPLEMENTATION RULES — HIGHEST PRECEDENCE

If any earlier preparation file conflicts with this file, this file plus `WEIGHTING_NOTE.md` and `THRESHOLD_POLICY.md` take precedence.

1. Keep the exact V1 architecture, frozen Seen4000 dataset/splits/normalization/labels, optimizer recipe and seed.
2. Do not use V1 `pos_weight` in V2.
3. Desired full training objective is equal total loss mass per class and equal total contribution per episode within each class.
4. Raw scientific row weights:
   - success: `0.5 / (N_success_episodes * T_i)`
   - failure: `0.5 / (N_failure_episodes * T_i)`
5. For unbiased uniformly shuffled minibatches with loss scale comparable to ordinary BCE mean, define `row_multiplier = N_train_rows * raw_row_weight` and train with `mean(BCE_none * row_multiplier)`.
6. Do NOT divide by batch sum of weights.
7. Primary checkpoint selection = Seen-validation episode-balanced AUPRC with sample weight `1/T_i`.
8. Derive V2 primary thresholds from Seen validation only using episode-balanced definitions in `THRESHOLD_POLICY.md`. Preserve legacy unweighted threshold family only as a comparison output.
9. Freeze V2 checkpoint + thresholds before any OOD150 evaluation.
10. OOD150 is development comparison only; no tuning from it.
11. OOD400 is forbidden.
12. HARD1000 must remain alive; no second Isaac/Omniverse process.
