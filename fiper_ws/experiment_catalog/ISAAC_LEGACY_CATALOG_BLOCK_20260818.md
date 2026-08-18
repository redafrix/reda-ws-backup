## Corrected True-H10 Isaac Sim Result (2026-08-18)

Canonical record: [`ISAAC_RESULTS_20260818.md`](ISAAC_RESULTS_20260818.md) and [`../../isaac_experiment_map/FINAL_ISAAC_RESULTS_20260818.md`](../../isaac_experiment_map/FINAL_ISAAC_RESULTS_20260818.md).

- Seen4000: **4000 episodes**, **3908 success / 92 failure**, **75,603 decision rows**.
- V1 validation AUROC/AUPRC: **0.9344901338 / 0.8494462696**.
- Locked historical true-H10 OOD150 detector: **72 success / 78 failure**, **5,887 rows**, step **AUROC 0.9165517742 / AUPRC 0.9800307262**.
- Main detector threshold: `best_val_f1 = 0.7990124225616455`, calibrated on Seen validation.
- Definitive active controller: `A=0.7990124225616455`, `C=0.9`, `M=0.0`.
- Active result: **75/150 (50.0%)** versus historical same-membership **72/150 (48.0%)**, net **+3 episodes / +2.0 percentage points**.
- Paired: **11 rescues / 8 regressions / 64 persisted successes / 67 persisted failures**.
- Controller audit: **57 accepted replacements** across **36/150 episodes**, **0 selection mismatches**, **0 execution mismatches**, max selected-vs-executed action difference **0.0**.
- Exact membership: 150 expected / 150 actual / 150 unique, no missing, extra, or duplicate IDs; historical membership exact.
- `A` is Seen-calibrated. `C=0.9` is engineering-development-informed from preserved live nine-candidate OOD-development decisions, so the final 150 is **not** a pristine untouched holdout for controller hyperparameter selection.
- V1 is a current/main H10 proposal failure detector with multi-sample ACE/disagreement context; it was **not** trained on nine independently supervised counterfactual candidate outcomes.
- HARD1000 resumed safely from the preserved 249-episode state and is ongoing; intermediate HARD1000 counts are **not** final results.
- Commit `70327b4b31bde35c01fda29a807f9100b5295a62` is **invalid for historical candidate-wise alternative scores** because candidates 1–8 diffusion traces were not archived. Correction commit: `86f5baf3281596df2305409499fc9e0c21d119ed`.
