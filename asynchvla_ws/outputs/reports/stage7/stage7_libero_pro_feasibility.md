# Stage 7 LIBERO-PRO Feasibility

## Local Search

Searched local workspace for LIBERO-PRO / perturbation data. Found only TDQC evaluation logs:

- `intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/v9_eval_libero_pro/phase2_tdqc_pro_state_mahal_k8_6000_20260507_145523/*.log`

No raw LIBERO-PRO HDF5 demonstrations with images, proprio, instructions, and expert actions were found in the current workspace scan.

## Usability For This Method

The found LIBERO-PRO material is not usable as rater training/evaluation data for SimVLA action-error uncertainty because it is TDQC rollout logging, not raw demonstrations with expert action chunks.

Hard rule respected: TDQC `.pt`/logs were not used as rater data and no external OOD claim is made from them.

## Decision

- LIBERO-PRO is not locally ready for Stage 7 action-error experiments.
- A proper LIBERO-PRO pilot requires locating/cloning the actual perturbation benchmark and verifying whether it provides expert actions or simulator reset states.
- Do not start a large download until size and dataset format are confirmed.
