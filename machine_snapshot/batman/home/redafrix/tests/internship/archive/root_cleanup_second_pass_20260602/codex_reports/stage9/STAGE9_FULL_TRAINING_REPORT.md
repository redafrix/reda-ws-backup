# Stage 9 Full Training Report

Generated: `2026-05-19T12:24:00+02:00`

## Executive Summary

- Training campaign status: `FINISHED`.
- Last live check: `2026-05-19 12:21 CEST`.
- Bob: no active Stage 9 training process; GPU idle at `0%`; campaign summaries written.
- Sam: no active Stage 9 training process; GPU idle at `0%`; campaign summaries written.
- Dataset status before training: `DATASET_READY_FOR_TRAINING = YES`.
- Frozen dataset: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/frozen/stage9_stop_validate_20260519_093940`
- Group-safe splits used: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/frozen/stage9_stop_validate_20260519_093940/splits_group_safe`
- Campaign id: `stage9_full_training_20260519_1035`
- Bob campaign path: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/training/stage9_full_training_20260519_1035/bob`
- Sam campaign path: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/training/stage9_full_training_20260519_1035/sam`

## What Ran

- Bob trained the heavy queue: small/medium/large history Transformers, action-chunk Transformer, cross-attention Transformer, Mamba history, and Mamba medium history.
- Sam trained the lightweight queue: action-only MLP, context-action MLP, GRU, LSTM, TCN, residual MLP, and gated context-action MLP.
- Each machine completed `35` quick jobs, calibration summaries, and `3` long-top jobs.
- Outputs include `metrics.json`, `predictions.jsonl`, `eval_report.md`, `checkpoint.pt` for real models, plus calibration outputs.
- `ensemble_top3` is a prediction ensemble and does not have a single model checkpoint.

## Dataset And Split Audit

- Samples: `37,632`
- Same-state groups: `1,426`
- Same-state group leakage: `0`
- Training split directory: `splits_group_safe`
- Metadata fields such as task id, suite id, perturbation type, seed, state id, and sample id are not used as model inputs.

Split label counts:

| split | samples | groups | GOOD_STRONG | VALIDATED_BAD | GOOD_WEAK | AMBIGUOUS |
|---|---:|---:|---:|---:|---:|---:|
| train | 12,832 | 454 | 5,127 | 2,535 | 1,626 | 3,544 |
| calib | 2,280 | 82 | 1,115 | 460 | 123 | 582 |
| test_seen_task | 1,592 | 54 | 686 | 338 | 138 | 430 |
| test_unseen_task | 5,120 | 193 | 1,707 | 1,070 | 1,034 | 1,309 |
| test_unseen_seed | 5,568 | 196 | 2,649 | 990 | 631 | 1,298 |
| test_unseen_perturbation | 10,240 | 447 | 6,646 | 1,521 | 211 | 1,862 |

## Dependency Status

- Torch/CUDA was available on Bob and Sam.
- Mamba was installed and smoke-tested on both machines.
- The available `causal-conv1d` wheel did not expose the fused `cpp_functions` API, so Mamba ran with `use_fast_path=False`.
- This is slower than the fused path but valid; both Mamba training smoke tests passed.

## Best Raw Test-Seen Results

Bob top raw/test-seen result:

- `small_history_transformer_k8`, target `clean_binary`
- AUROC BAD: `0.8675`
- AUPRC BAD: `0.8389`
- Brier: `0.1487`
- Checkpoint: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/training/stage9_full_training_20260519_1035/bob/quick/clean_binary/small_history_transformer_k8/checkpoint.pt`

Sam top raw/test-seen result:

- `residual_mlp_large`, target `soft_no_ambiguous`, long-top rank 1
- AUROC BAD: `0.8629`
- AUPRC BAD: `0.8361`
- Brier: `0.1236`
- Checkpoint: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/training/stage9_full_training_20260519_1035/sam/long_top/rank1_soft_no_ambiguous_residual_mlp_large/checkpoint.pt`

## Best Calibrated Accuracy Candidate

Best seen-task calibrated AUROC found:

- Machine: Bob
- Model: `Mamba_history_k8`
- Target mode: `clean_binary`
- Calibration: `beta`
- Test-seen AUROC BAD: `0.8868`
- Test-seen AUPRC BAD: `0.8387`
- Test-seen Brier: `0.1252`
- Average AUROC across seen/unseen task/seed/perturbation: `0.7606`
- Accept-90 BAD leakage:
  - test_seen_task: `0.2581`
  - test_unseen_task: `0.3397`
  - test_unseen_seed: `0.2067`
  - test_unseen_perturbation: `0.1754`
- Checkpoint: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/training/stage9_full_training_20260519_1035/bob/quick/clean_binary/Mamba_history_k8/checkpoint.pt`

This is the best accuracy candidate, but it is not the safest acceptance policy because leakage at 90% accept is high, especially on unseen task.

## Best First Safe-Policy Candidate

Best low-leakage first candidate found:

- Machine: Sam
- Model: `residual_mlp_large`
- Target mode: `soft_labels`
- Calibration: `beta`
- Test-seen AUROC BAD: `0.7854`
- Test-seen AUPRC BAD: `0.6400`
- Test-seen Brier: `0.1570`
- Average accept-90 BAD leakage across seen/unseen task/seed/perturbation: `0.1477`
- Accept-90 threshold: `0.9242723988069587`
- Accept-90 BAD leakage:
  - test_seen_task: `0.1361`
  - test_unseen_task: `0.1788`
  - test_unseen_seed: `0.1403`
  - test_unseen_perturbation: `0.1354`
- Checkpoint: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/training/stage9_full_training_20260519_1035/sam/quick/soft_labels/residual_mlp_large/checkpoint.pt`

For strict safety, use more conservative acceptance thresholds from this same calibration file:

- Accept-50 threshold: about `0.0708` on calibration; observed leakage is lower than accept-90 but accepts fewer actions.
- Accept-25 threshold: about `0.0468` on calibration; calibration leakage is `0.0`, but this is very selective.

## Important Limitation

The first models are useful and the training pipeline is working, but the safe-action leakage at 90% acceptance is still too high for deployment as a hard safety filter. This is especially visible on unseen-task and unseen-perturbation transfer. The next serious step should not be blind deployment; it should be more data, better perturbation balance, and threshold selection against the exact acceptable-risk target.

## Recommendation

- Best accurate model: Bob `Mamba_history_k8 / clean_binary / beta`.
- Best fast/runtime model: Sam `residual_mlp_large / soft_no_ambiguous` or `soft_labels`.
- Best first safe-policy model: Sam `residual_mlp_large / soft_labels / beta`, using a conservative threshold.
- Recommended default safe threshold for broad acceptance experiment: beta risk threshold `0.9242723988069587`.
- Recommended strict threshold for actual safe-action filtering: use the accept-50 or accept-25 calibrated threshold from the same calibration file, then verify on a fresh held-out LIBERO-PRO rollout set.

## Inference Starting Point

Fast/safe first checkpoint:

```bash
/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/training/stage9_full_training_20260519_1035/sam/quick/soft_labels/residual_mlp_large/checkpoint.pt
```

Accuracy-first checkpoint:

```bash
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/training/stage9_full_training_20260519_1035/bob/quick/clean_binary/Mamba_history_k8/checkpoint.pt
```

## Final State

- Full campaign finished: `YES`
- Both PCs used: `YES`
- Mamba included: `YES`
- Group-safe splits used: `YES`
- Metadata leakage prevented in model inputs: `YES`
- Best checkpoints available: `YES`
- First training results available: `YES`
- Dataset ready for serious model training: `YES`
- Model ready for conservative offline evaluation: `YES`
- Model ready as an unsupervised production safety gate: `NO`

`TRAINING_CAMPAIGN_COMPLETE = YES`

