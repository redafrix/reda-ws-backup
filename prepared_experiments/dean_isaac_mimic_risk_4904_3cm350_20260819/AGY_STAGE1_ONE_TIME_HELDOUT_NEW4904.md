# AGY Stage 1 — ONE-TIME Held-Out Test for NEW4904 Mimic V3

Agy is mechanical only. The scientific design, checkpoint selection and calibration are frozen.

Canonical workspace:
`/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813`

Experiment:
`isaac_mimic_h10_strict_3cm350_seen4904_v3`

Source dataset:
`isaac_seen4904_h10_3cm350_exact_v1`

Matched main model identity:
`isaac_seen4904_h10_topk8_temporal_3cm350_main_v2`

## 0. FINAL disposition from Stage0B

Stage0 training is ACCEPTED.

The strict-missing decision is frozen because the forensic audit recursively streamed all 96,813 source rows and found zero occurrences of all five required portable-Mimic cross-candidate trace names. Do not revisit or replace the missing 25 channels.

Primary result was frozen BEFORE held-out access:

- seed: 0
- checkpoint SHA256: `857e16b7d846051c29921d148d8545198e7057f2e1458040250de7b8cc965b82`
- operating point: `conformal_alpha_0.10`
- threshold: `0.8907762169837952`

Frozen experiment bindings:

- source dataset manifest SHA256: `61462ceead4a79d6d44a0ae80ee9ff25b958c4c1afbd67142c4df276801a0a3c`
- source split artifact SHA256: `34db754f88cc9f77ca72dc358a51235f7059278e561e662103451ec4ef8095b8`
- derived dataset manifest SHA256: `26e633c8815d92a46df841bd7976ec942740b83ec477cc20e7d9f6cf87bb3019`
- normalization SHA256: `5564083f1561b627c81305c9ebfcb34732c4f3529bc2421ab6d4124682e84b26`
- training freeze SHA256: `ec925b2dea8a66dd7b5317790d8f8c18bf59e67da0ddb0278ca678b5d8637e21`

Expected held-out split:

- 736 episodes
- 658 success episodes
- 78 failure episodes
- 14,526 query rows
- 2,730 positive rows
- 11,796 negative rows

## 1. PRETEST CRYPTOGRAPHIC / FIDELITY GATE

Before loading any held-out labels into a model-scoring path, verify all of the following:

1. exact source dataset manifest SHA
2. exact source TopK8 split-manifest SHA
3. exact derived Mimic dataset-manifest SHA
4. exact normalization SHA
5. exact training-freeze SHA
6. every selected checkpoint SHA matches TRAINING_FREEZE.json
7. every per-seed validation-freeze SHA matches TRAINING_FREEZE.json
8. seed0 checkpoint SHA and alpha0.10 threshold match the constants above
9. derived heavy-array SHA256s match dataset_manifest.json
10. held-out split contains exactly 14,526 rows / 736 episodes / 658 success / 78 failure / 2,730 positive rows / 11,796 negative rows
11. dims 9..33 are exactly zero on ALL held-out rows
12. normalization for dims 9..33 is mean0/std1 exactly
13. held-out episode ID set equals exactly the `test` episode ID set in the frozen TopK8 split manifest
14. train, validation and test sets are pairwise disjoint
15. no held-out result file exists from a prior V3 scoring run; if one exists, STOP and report rather than rescoring

If any gate fails: STOP BEFORE SCORING.

Do not change or repair anything in this stage.

## 2. ONE-TIME scoring

Only after all gates pass, score the already-frozen held-out test exactly ONCE for seeds 0,1,2,3,4.

For each seed:

- use its already-selected best checkpoint only
- use the frozen NEW4904 normalization only
- use its already-frozen validation thresholds only
- no threshold fitting from held-out scores
- no checkpoint/seed selection from held-out scores
- save raw held-out scores/targets/query keys for forensic reproducibility
- save a frozen test result package bound to checkpoint/normalization/dataset/validation-freeze SHA256s

Compute per seed:

### row metrics
- AUROC
- AUPRC

These are descriptive because rows within an episode are correlated.

### episode metrics for every already-frozen threshold
Report integer counts and rates:

- success false alarms / 658
- failure detected / 78
- Det@10 / 78
- Det@25 / 78
- Det@50 / 78
- never detected / 78
- mean first-alarm fraction among detected failures

Use the existing evaluator timing convention exactly:
`(first_alarm_query_index + 1) / episode_query_count`.

Primary report is irrevocably:
`seed0 + conformal_alpha_0.10`.

Do not promote seed2 even if it scores higher. Seed2 is robustness evidence only.

Report all-five mean/std for AUROC, AUPRC, alpha0.10 FA%, detection%, Det@25% and Det@50%, but preserve raw per-seed integer episode counts.

## 3. Existing TopK8 main-v2 matched comparison — NO RERUN

Do NOT rerun or retrain TopK8.

Mechanically locate the already-frozen held-out result artifact belonging to:
`isaac_seen4904_h10_topk8_temporal_3cm350_main_v2`.

Before comparison prove:

- its source split artifact is the exact SHA `34db754f88cc9f77ca72dc358a51235f7059278e561e662103451ec4ef8095b8`, OR independently resolve its held-out episode IDs and prove exact 736/736 set equality with the Mimic test set;
- if query keys are stored, prove exact held-out `(episode_id, decision_index)` key equality;
- its held-out census is the same 736 eps / 658 success / 78 failure / 14,526 rows.

If exact membership cannot be proven, write `TOPK8_MATCHED_COMPARISON: NOT_PROVEN` and do not calculate deltas.

If proven, use EXISTING TopK8 numbers only and freeze:

### Threshold-independent matched comparison
- TopK8 row AUROC vs Mimic seed0 row AUROC
- delta = Mimic - TopK8
- TopK8 row AUPRC vs Mimic seed0 row AUPRC
- delta = Mimic - TopK8

### Matched validation-best-F1 comparison
Only if TopK8 has a threshold that was frozen from its validation set by the same row-best-F1 / best-val-F1 rule:

compare TopK8 best-val-F1 vs Mimic seed0 `row_best_f1`:

- FA counts /658
- failure detection /78
- Det@10 /78
- Det@25 /78
- Det@50 /78
- never /78

Do not compare different threshold-selection rules and call the delta matched.

### Mimic primary operating point
Separately report seed0 alpha0.10 results. This is the primary Mimic operating point but is not automatically a matched threshold comparison against TopK8 unless TopK8 used the same calibration rule.

## 4. Freeze

Write a single held-out freeze containing:

- all pretest hashes
- exact held-out membership set hash
- every seed checkpoint SHA
- every seed validation-freeze SHA
- every seed held-out result
- primary seed0/alpha0.10 result
- all-five robustness summary
- TopK8 provenance/comparison if proven
- `test_used_for_selection = false`
- `ood_scored = false`

Hash the final freeze.

## 5. ABSOLUTE PROHIBITIONS

Do NOT:

- retrain
- resume training
- modify zeroed dynamics channels
- use C0 dynamics
- change candidate subset
- change normalization
- change checkpoint
- change seed0 primary status
- recalibrate any threshold
- create a threshold from test
- select a model based on test
- rerun TopK8
- score OOD150
- score OOD400
- touch HARD1000
- launch Isaac Sim
- run SimVLA inference
- recollect

## Required return block

Return ONLY:

```text
PRETEST_GATE_NEW4904:
  status: PASSED|FAILED
  source_manifest_sha256: ...
  source_split_sha256: ...
  derived_manifest_sha256: ...
  normalization_sha256: ...
  training_freeze_sha256: ...
  all_checkpoint_validation_bindings_match: YES|NO
  strict_missing_zero_channels_test: YES|NO
  heldout_rows/episodes/success/failure: ...
  exact_topk8_test_membership: YES|NO

PRIMARY_SEED0_ALPHA010_NEW4904:
  threshold: ...
  row_auroc: ...
  row_auprc: ...
  success_false_alarms: <count>/658 | <percent>
  failure_detection: <count>/78 | <percent>
  det10: <count>/78 | <percent>
  det25: <count>/78 | <percent>
  det50: <count>/78 | <percent>
  never_detected: <count>/78
  mean_first_alarm_fraction: ...

ROBUSTNESS_ALPHA010_NEW4904:
  seed0: <AUROC> | <AUPRC> | <FA>/658 | <Det>/78 | <Det25>/78 | <Det50>/78
  seed1: ...
  seed2: ...
  seed3: ...
  seed4: ...
  mean_std_auroc: ...
  mean_std_auprc: ...
  mean_std_fa_percent: ...
  mean_std_failure_detection_percent: ...
  mean_std_det25_percent: ...
  mean_std_det50_percent: ...

SEED0_ALL_THRESHOLDS_NEW4904:
  <threshold_name>: <threshold> | <FA>/658 | <Det>/78 | <Det10>/78 | <Det25>/78 | <Det50>/78 | never <count>/78
  ...

MATCHED_TOPK8_MAIN_V2:
  status: VALID|NOT_PROVEN
  membership_exact_match: ...
  query_key_equality: ...
  topk8_result_path: ...
  topk8_result_sha256: ...
  threshold_independent: ...
  matched_row_best_f1: ...
  mimic_primary_alpha010_note: ...

HELDOUT_FREEZE_SHA256:
  ...

TEST_USED_FOR_SELECTION:
  NO
OOD_SCORED:
  NO
ISAAC_SIM_LAUNCHED:
  NO
HARD1000_TOUCHED:
  NO

COMMIT:
  <sha>
```
