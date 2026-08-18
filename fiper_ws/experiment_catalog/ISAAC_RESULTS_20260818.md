# Corrected True-H10 Isaac Sim Results — 2026-08-18

Canonical detailed record: [`../../isaac_experiment_map/FINAL_ISAAC_RESULTS_20260818.md`](../../isaac_experiment_map/FINAL_ISAAC_RESULTS_20260818.md).

Machine-readable record: [`../../isaac_experiment_map/final_isaac_results_20260818.json`](../../isaac_experiment_map/final_isaac_results_20260818.json).

## Offline detector

- Seen4000: **4000 episodes**, **3908 success / 92 failure**, **75,603 decision rows**.
- V1 validation: **AUROC 0.9344901338 / AUPRC 0.8494462696**.
- Locked historical true-H10 OOD150: **72 success / 78 failure**, 5,887 rows, **step AUROC 0.9165517742 / AUPRC 0.9800307262**.
- Selected main threshold: `best_val_f1 = 0.7990124225616455`, calibrated on Seen validation.

Interpretation: V1 is a current/main H10 proposal failure detector using multi-sample ACE/disagreement context. It was not trained on nine independently supervised counterfactual candidate outcomes.

## Definitive active controller

- Frozen controller: `A=0.7990124225616455`, `C=0.9`, `M=0.0`.
- Historical same-membership baseline: **72/150 (48.0%)**.
- Active: **75/150 (50.0%)**.
- Net: **+3 episodes / +2.0 percentage points**.
- Paired: **11 rescues / 8 regressions / 64 persisted successes / 67 persisted failures**.
- Controller: **57 accepted replacements** across **36/150 episodes**.
- Audit: **0 selection mismatches**, **0 execution mismatches**, max action discrepancy **0.0**.
- Membership: exact **150/150**, no missing/extra/duplicate IDs; historical membership exact.

`C=0.9` is an engineering operating point chosen from preserved live OOD-development nine-candidate decisions. Therefore the definitive OOD150 run is not a pristine untouched holdout for controller hyperparameter selection.

## Evidence

Primary evidence directory:

`prepared_experiments/dean_isaac_online_ood150_engineering_cap090_v1/`

Final evidence commits:

- `840d9b4ae44a9f83cd90d19ce663c7d5f3a7c442`
- `556aa351ba107d2f28d91582cc1b5f602f87fecf`
- `06d9d55c0c2a166719c4aaae0534cf973689f93e`

## HARD1000

HARD1000 resumed safely from the preserved 249-episode state and is ongoing. Intermediate counts are **not** a final result.

## Invalid historical evidence

Commit `70327b4b31bde35c01fda29a807f9100b5295a62` is invalid for historical candidate-wise alternative scores because candidates 1–8 diffusion traces were not archived. Correction commit: `86f5baf3281596df2305409499fc9e0c21d119ed`.
