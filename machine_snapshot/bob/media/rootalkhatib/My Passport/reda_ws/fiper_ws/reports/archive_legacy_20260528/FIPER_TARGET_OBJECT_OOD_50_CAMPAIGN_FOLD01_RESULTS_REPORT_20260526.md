# FIPER Target-Object OOD 50-Campaign Fold01 Results Report

Date: 2026-05-26

## 1. Executive Summary

The 50-experiment fold01 campaign completed on Sam with no failed jobs.

The result is important: success-only RND/AE variants still do not solve target-object OOD false alarms, but supervised temporal risk models trained only on seen-object failures produce a much better warning candidate.

Best balanced candidate:

- Job: `041_sup_seq_tcn_k8_no_proprio`
- Policy: model score-only `q95`, debounce `K=3`
- OOD success false alarm: `18.03%`
- Seen success false alarm: `25.86%`
- OOD failure detection: `94.29%`
- OOD failure Det@25: `71.43%`
- OOD failure mean first detection time: `0.2427`

This is a major improvement over the previous fold01 OR q95 K=3 baseline, which had `100%` OOD-success episode false alarms.

However, this is not a pure success-only FIPER monitor anymore. The winning family is supervised risk modeling using `success_train_seen` negatives and `failure_eval_seen` positives, with held-out target-object rows still evaluation-only.

## 2. What Ran

Workspace:

`/home/rootalkhatib/test/reda_ws/fiper_ws`

Fold:

`experiments/prepared_20260526/08_target_object_pick_basket_loto_v1/fold_01_holdout_butter_chocolate_pudding/datasets/refs`

Output:

`experiments/target_object_ood_50_campaign_v1_fold01_20260526`

Campaign files:

- `scripts/run_target_object_ood_campaign_v1.py`
- `configs/target_object_ood_50_campaign_v1.json`
- `reports/FIPER_TARGET_OBJECT_OOD_50_EXPERIMENT_IDEAS_20260526.txt`
- `a_prompt_.txt`

All 50 jobs completed. No `failed_jobs.jsonl` was present.

## 3. Data Rules

OOD held-out objects:

- `butter`
- `chocolate_pudding`

OOD target-object rows were not used for training, early stopping, or threshold calibration.

Thresholds were calibrated on `success_calib_seen` only.

Supervised jobs used:

- negative class: `success_train_seen`
- positive class: `failure_eval_seen`

This is valid as a seen-failure-to-unseen-object generalization test, but it must be reported separately from success-only RND.

## 4. Top OR-q95-K3 Jobs

These are from the automatic campaign objective using OR q95 K=3. This ranking is useful but not the final deployable policy ranking, because OR with ACE still carries high OOD-success false alarm burden.

| Rank | Job | Mode | Model | OOD Success FA | OOD Failure Det | OOD Failure Det@25 | Mean Time |
|---:|---|---|---|---:|---:|---:|---:|
| 1 | `050_sup_seq_tcn_k8_pos2` | supervised | TCN | 79.23% | 100.00% | 85.71% | 0.1584 |
| 2 | `044_sup_seq_lstm_k8` | supervised | LSTM | 76.50% | 100.00% | 82.86% | 0.1998 |
| 3 | `022_ae_no_objects_k8` | AE | MLP | 100.00% | 100.00% | 100.00% | 0.1721 |
| 4 | `009_rnd_full_k4` | RND | MLP | 100.00% | 100.00% | 100.00% | 0.0067 |
| 5 | `013_rnd_no_proprio_k8` | RND | MLP | 100.00% | 100.00% | 100.00% | 0.0086 |

Conclusion: OR q95 K=3 is still too noisy for target-object OOD.

## 5. Best Policy-Level Results

A policy-level sweep over job metrics found better rules than OR q95.

| Policy | Job | OOD Success FA | OOD Failure Det | OOD Det@25 | Mean Time | Seen Success FA |
|---|---|---:|---:|---:|---:|---:|
| score q95 K3 | `041_sup_seq_tcn_k8_no_proprio` | 18.03% | 94.29% | 71.43% | 0.2427 | 25.86% |
| score q95 K3 | `050_sup_seq_tcn_k8_pos2` | 26.23% | 100.00% | 71.43% | 0.2347 | 22.41% |
| score q95 K3 | `044_sup_seq_lstm_k8` | 16.94% | 94.29% | 65.71% | 0.2584 | 20.69% |
| score q95 K3 | `028_sup_full_nohist_mlp` | 18.03% | 97.14% | 62.86% | 0.2308 | 21.55% |
| score q95 K3 | `039_sup_seq_tcn_k16` | 20.22% | 97.14% | 62.86% | 0.2458 | 21.55% |

Best low-false-alarm candidate:

| Policy | Job | OOD Success FA | OOD Failure Det | OOD Det@25 | Mean Time | Seen Success FA |
|---|---|---:|---:|---:|---:|---:|
| AND q95 K3 | `047_sup_seq_transformer_medium_k8` | 4.37% | 85.71% | 8.57% | 0.5253 | 3.45% |

This low-FA transformer rule is too late for early warning, but it may be useful as a conservative late hard-stop signal.

## 6. Success-Only Results

The success-only anomaly family did not solve the OOD false alarm problem.

Best success-only anomaly variants either:

- kept OOD success false alarms near `100%`, or
- reduced false alarms only by becoming late and weak.

Example:

- `014_rnd_ace_only`, score q99 K3:
  - OOD success FA: `10.38%`
  - OOD failure det: `91.43%`
  - OOD Det@25: `11.43%`
  - Mean time: `0.4831`

That is not an early-warning solution.

Conclusion:

`SUCCESS_ONLY_RND_AE_SOLVES_TARGET_OBJECT_OOD = NO`

## 7. Temporal Model Lesson

The old archaeology result was useful. Temporal models were the first family to strongly reduce OOD-success false alarms while keeping useful failure detection.

Best temporal warning:

- `041_sup_seq_tcn_k8_no_proprio`, score q95 K3

Second-best temporal warning:

- `044_sup_seq_lstm_k8`, score q95 K3

The best TCN variant excluded current proprio from static context, but it still used history tokens containing previous proprio and actions. This suggests current proprio/context may add nuisance shift, while temporal action/proprio dynamics help detect real risk.

## 8. ACE Lesson

For target-object OOD, ACE should not be blindly OR-ed with model alarms.

The OR policy raises false alarms too much. The useful pattern is:

- use ACE as an input feature to the learned risk model,
- keep ACE as a secondary diagnostic score,
- avoid raw `model OR ACE` as the default deployment warning rule on target-object OOD.

## 9. Recommended Candidate Policies

Primary warning candidate:

`041_sup_seq_tcn_k8_no_proprio`, score q95 K3

Why:

- best balance of OOD-success false alarm and early failure detection,
- OOD success false alarm reduced from `100%` to `18.03%`,
- OOD failure detection remains `94.29%`,
- Det@25 remains `71.43%`.

Secondary warning candidate:

`044_sup_seq_lstm_k8`, score q95 K3

Why:

- slightly lower OOD success false alarm: `16.94%`,
- slightly weaker early detection: `65.71%`.

Conservative hard-stop candidate:

`047_sup_seq_transformer_medium_k8`, AND q95 K3

Why:

- very low OOD success false alarm: `4.37%`,
- but poor early detection: `8.57%` Det@25.

## 10. Remaining Caveats

1. Fold01 was used as the development fold. Do not claim final generalization yet.
2. Supervised models use seen-object failures, so this is no longer pure success-only FIPER.
3. Several top supervised models selected epoch 1 as best. This may be legitimate early-stopping behavior, but it should be repeated across seeds.
4. The auto-generated campaign objective overweights OR q95 and should not be used alone for deployment decisions.
5. Success-only RND/AE remains insufficient for target-object OOD.

## 11. Next Work Plan

Freeze 2-3 policies and test them without retuning on folds 00, 02, and 03:

1. `041_sup_seq_tcn_k8_no_proprio`, score q95 K3
2. `044_sup_seq_lstm_k8`, score q95 K3
3. `047_sup_seq_transformer_medium_k8`, AND q95 K3

Run multiple seeds for the first two candidates before finalizing:

- seeds: `42`, `43`, `44`
- same fold01 split first
- then fixed model/policy family on folds 00/02/03

## 12. Exact Commands Run

Compile/check:

```bash
python3 -m py_compile scripts/run_target_object_ood_campaign_v1.py
python3 -m json.tool configs/target_object_ood_50_campaign_v1.json >/tmp/target_object_ood_50_campaign_v1.checked.json
```

Smoke:

```bash
python3 scripts/run_target_object_ood_campaign_v1.py \
  --campaign-config configs/target_object_ood_50_campaign_v1.json \
  --refs-dir experiments/prepared_20260526/08_target_object_pick_basket_loto_v1/fold_01_holdout_butter_chocolate_pudding/datasets/refs \
  --output-dir experiments/target_object_ood_50_campaign_v1_fold01_smoke_20260526 \
  --device cpu \
  --max-jobs 2 \
  --max-train-rows 2000 \
  --max-calib-rows 1000 \
  --max-eval-rows 1000 \
  --max-epochs 3 \
  --patience 2 \
  --batch-size 128 \
  --force
```

Full campaign:

```bash
nohup python3 scripts/run_target_object_ood_campaign_v1.py \
  --campaign-config configs/target_object_ood_50_campaign_v1.json \
  --refs-dir experiments/prepared_20260526/08_target_object_pick_basket_loto_v1/fold_01_holdout_butter_chocolate_pudding/datasets/refs \
  --output-dir experiments/target_object_ood_50_campaign_v1_fold01_20260526 \
  --device cuda \
  --seed 42 \
  > experiments/target_object_ood_50_campaign_v1_fold01_20260526.launch.log 2>&1 &
```

## 13. Exact Files Written

Local:

- `scripts/run_target_object_ood_campaign_v1.py`
- `configs/target_object_ood_50_campaign_v1.json`
- `reports/FIPER_TARGET_OBJECT_OOD_50_EXPERIMENT_IDEAS_20260526.txt`
- `reports/FIPER_TARGET_OBJECT_OOD_50_CAMPAIGN_FOLD01_RESULTS_REPORT_20260526.md`
- `a_prompt_.txt`
- `experiments/target_object_ood_50_campaign_v1_fold01_20260526/campaign_summary.csv`
- `experiments/target_object_ood_50_campaign_v1_fold01_20260526/campaign_summary.json`
- `experiments/target_object_ood_50_campaign_v1_fold01_20260526/CAMPAIGN_TOPLINE_REPORT.md`

Sam:

- same script/config/ideas report
- full job directories under `experiments/target_object_ood_50_campaign_v1_fold01_20260526/jobs/`
- top-level campaign summary files

## 14. Final Decision Fields

```text
FULL_50_CAMPAIGN_COMPLETE = YES
BEST_JOB = 041_sup_seq_tcn_k8_no_proprio with score_q95_K3
BEST_SUCCESS_ONLY_JOB = NONE_FOR_EARLY_WARNING
BEST_TEMPORAL_JOB = 041_sup_seq_tcn_k8_no_proprio
OOD_SUCCESS_FALSE_ALARM_IMPROVED = YES
OOD_FAILURE_EARLY_DETECTION_STILL_USEFUL = YES
READY_TO_FREEZE_POLICY_AND_TEST_FOLDS_00_02_03 = YES
CURRENT_BEST_POLICY_DEPLOYABILITY = WARNING_ONLY_NOT_HARD_STOP
```
