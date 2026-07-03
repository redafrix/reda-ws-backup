# Official FIPER Seen Goal Object Materialization Report

Validation: PASS

- obs_embeddings.pt: `(194643, 960)`
- action_preds.pt: `(194643, 9, 10, 7)`
- num_rollouts: `900`
- num_steps: `194643`

| Split | Count |
|---|---:|
| train_success | 500 |
| calib_success | 150 |
| seen_test_success | 150 |
| seen_test_failure | 100 |

Flags:
- DATASET_MATERIALIZED = YES
- DATASET_VALIDATION_PASS = YES
- CALIBRATION_SEEN_SUCCESS_ONLY = YES
- OOD_USED = NO
