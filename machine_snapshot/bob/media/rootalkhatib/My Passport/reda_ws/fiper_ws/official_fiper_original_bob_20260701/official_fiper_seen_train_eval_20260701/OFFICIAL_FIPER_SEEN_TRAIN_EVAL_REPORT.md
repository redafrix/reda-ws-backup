# Official FIPER Seen Train/Eval Report

## Protocol

- Repo: official FIPER clone, method classes unchanged.
- Repo path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701/repos/fiper`
- Dataset: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701/official_fiper_data/libero_goal_object_official/processed_rollouts`
- Dataset adapter only: explicit tensor load to avoid the repo loader key-suffix bug.
- Training/calibration semantics: official code trains RND on `calibration` rollouts and computes thresholds on successful calibration rollouts.
- Test set: seen held-out `libero_goal_object_official` only.
- Seeds: 0, 1, 2, 42, 43.

## Dataset Validation

- `task_config`: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701/repos/fiper/configs/task/libero_goal_object_official.yaml`
- `obs_embeddings_shape`: `(194643, 960)`
- `action_preds_shape`: `(194643, 9, 10, 7)`
- `num_rollouts`: `900`
- `num_steps`: `194643`
- `calibration_rollout_labels`: `150`
- `test_rollout_labels`: `250`
- `successful_rollout_labels`: `800`
- `failed_rollout_labels`: `100`
- `id_rollout_labels`: `900`
- `ood_rollout_labels`: `0`

## Best q95 tvt_quantile Operating Points

| Method | Window | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| entropy | 50 | 40.0% | 100.0% | 39.0% | 67.0% | 84.0% | 0.260 | 0.0% |
| rnd_oe | 1 | 15.7% | 71.0% | 0.0% | 24.4% | 31.2% | 0.427 | 29.0% |
| rnd_oe_and_entropy | 1/40 | 1.7% | 69.8% | 0.0% | 16.0% | 21.2% | 0.568 | 30.2% |

## Output Files

- Raw per-seed q95 sweep: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701/official_fiper_seen_train_eval_20260701/official_fiper_q95_per_seed.csv`
- Averaged q95 sweep: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701/official_fiper_seen_train_eval_20260701/official_fiper_q95_aggregate.csv`
- Per-seed minimal q95 rows: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701/official_fiper_seen_train_eval_20260701/official_fiper_q95_per_seed.csv`

## Flags

- `OFFICIAL_METHOD_CLASSES_UNCHANGED = YES`
- `DATASET_ADAPTER_USED = YES`
- `NO_OOD_USED = YES`
- `RND_TRAINED_ON_OFFICIAL_CALIBRATION_SUBSET = YES`
- `THRESHOLDS_CALIBRATED_ON_SUCCESSFUL_CALIBRATION_ROLLOUTS = YES`
- `SEEN_TEST_ONLY = YES`
- `RUN_COMPLETE = YES`
