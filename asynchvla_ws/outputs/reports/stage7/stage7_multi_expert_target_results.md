# Stage 7 — Multi-Expert Min-Distance Target Results

- Timestamp: `2026-05-15 11:30` (Bob)
- Splits tested: `holdout_libero_object`, `holdout_object_bowl`
- Pool mode: `same_split_same_task` (analysis-friendly; pool drawn from candidates of the same task within each split, excluding self context). K_mean ≈ 20 actual experts per candidate.
- Variants: `action_only_baseline` (proxy for "without strong context features"), `context_gated_action` (best Stage 6 model).
- Targets compared:
  - `target_chunk_l2_single_expert` (baseline, copy of `true_chunk_l2_error`).
  - `target_chunk_min_l2_K10` (min L2 to nearest 10 same-task experts).
  - `target_chunk_softmin_l2_K10` (β=4 soft-min over 10 same-task experts).

## Test_OOD — SimVLA-only metrics

### holdout_libero_object

| target | variant | pairwise | improvement_over_seed0 | AUROC top30 worst | switch proxy gap @reject0.25 |
|---|---|---|---|---|---|
| l2_single_expert | action_only | 0.7244 | 0.0460 | 0.6750 | 0.3155 |
| min_l2_K10      | action_only | 0.7036 | 0.0400 | 0.6663 | 0.3328 |
| softmin_l2_K10  | action_only | **0.7624** | 0.0498 | 0.6824 | 0.3022 |
| l2_single_expert | context_gated_action | **0.9204** | 0.0643 | **0.9512** | 0.5514 |
| min_l2_K10      | context_gated_action | 0.9052 | 0.0589 | 0.9391 | 0.5618 |
| softmin_l2_K10  | context_gated_action | 0.9132 | 0.0604 | 0.9240 | 0.5567 |

### holdout_object_bowl

| target | variant | pairwise | improvement_over_seed0 | AUROC top30 worst | switch proxy gap @reject0.25 |
|---|---|---|---|---|---|
| l2_single_expert | action_only | 0.7444 | 0.0493 | 0.8686 | 0.8810 |
| min_l2_K10      | action_only | 0.7388 | **0.0546** | 0.8610 | 0.8512 |
| softmin_l2_K10  | action_only | 0.7436 | 0.0507 | 0.8254 | 0.7879 |
| l2_single_expert | context_gated_action | **0.9220** | 0.0648 | **0.9953** | **1.2482** |
| min_l2_K10      | context_gated_action | 0.9128 | **0.0654** | 0.9939 | 1.2480 |
| softmin_l2_K10  | context_gated_action | 0.9192 | 0.0643 | 0.9895 | 1.2173 |

## Decision: **DROP** multi-expert target

Per the Stage 7 keep/drop rule, a new feature must improve at least one deployment metric by:

- SimVLA-only OOD pairwise +0.02 → **fails** (multi-expert is slightly worse on the best model).
- switch proxy accepted/rejected gap +0.05 → **fails** (within noise).
- AUROC top-30 bad +0.02 → **fails** (within noise; slight regression).
- Calibration coverage/width improved → not tested explicitly, but if pairwise and AUROC are flat or worse, residual conformal width will not improve.

The strongest model (`context_gated_action`) already harvests the multi-expert prior implicitly through the gated context conditioning. Switching the *target* to multi-expert loses some discriminative signal between the canonical demonstration and obvious failures, slightly underfitting the long tail. For `action_only_baseline`, `softmin_l2_K10` does give a marginal pairwise lift on holdout_libero_object (+0.038), but action-only is not the deployment model anyway.

## What this rules out

- The "single L2 is brittle" hypothesis as the **main** weakness of the Stage 6 rater on test_ood is not supported by this experiment. With K=20 same-task experts (essentially the full pool the OOD test set has access to), the target relaxation does not unlock additional uncertainty signal.

## What it does not rule out

- Multi-expert pool **at training time only**, where train candidates also see a relaxed target (already what we did via same_split mode), is what we tested. We have **not** tested:
  - A wider expert pool that includes other *similar* tasks (cross-task nearest).
  - A learned expert weighting (e.g., the rater predicts pool weights end-to-end).
  - A different per-step reduction (we used mean per-step L2 across the 10-step chunk).
- For deployment, a `train_only_same_task` pool was not productively testable because the OOD task by construction does not appear in train, so the pool size collapses to 0. A more flexible cross-task nearest-K pool could be examined later but is out of scope here.

## Artifacts

- `asynchvla_ws/data/processed_stage5/holdout_libero_object/multiseed_candidate_*_multiexp.pt`
- `asynchvla_ws/data/processed_stage5/holdout_libero_object/multiseed_multi_expert_summary.json`
- `asynchvla_ws/data/processed_stage5/holdout_object_bowl/multiseed_candidate_*_multiexp.pt`
- `asynchvla_ws/data/processed_stage5/holdout_object_bowl/multiseed_multi_expert_summary.json`
- `asynchvla_ws/outputs/reports/stage6/stage7_multi_expert_target_holdout_libero_object.{json,md}`
- `asynchvla_ws/outputs/reports/stage6/stage7_multi_expert_target_holdout_object_bowl.{json,md}`

Builder: `asynchvla_ws/src/data_building/build_multi_expert_min_distance_targets.py`.
Runner: `asynchvla_ws/src/rater_stage7/run_stage7_multi_expert_target_experiments.py`.

## Recommendation

- **Keep**: original `true_chunk_l2_error` single-expert target for the deployable `context_gated_action` model.
- **Drop**: multi-expert target families. Do not push to Stage 6 production code path.
- **Future work** (only if execution validation in Phase 4 shows a clear "false-high-uncertainty" tail): try cross-task K-NN expert pool restricted to *successful* SimVLA seeds, not all candidate demonstrations.
