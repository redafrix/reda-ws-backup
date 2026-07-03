# Stage 9 / LIBERO-PRO / FIPER Current State Audit

Audit date: 2026-05-26  
Audit scope: read-only inspection of local workspace, Sam, Bob, current `fiper_sweep_eternal` collection, collector code, launch scripts, previous reports, and FIPER analysis scripts.  
Exception allowed by user: write this single report.  
User override during audit: ignore `libero_10_with_milk` task 3 and task 4 coverage gaps.

## 1. Executive Summary

The current final collection is still running on Sam and Bob. I did not stop it, start a new collector, or launch training.

The live dataset snapshot audited at roughly 2026-05-26 09:20 CEST is large enough for the next offline full FIPER train/eval campaign, provided the train/eval code uses a frozen snapshot of the JSONLs and excludes `libero_10_with_milk` task 3 and task 4 as intentionally ignored.

Current audited totals:

| Metric | Value |
|---|---:|
| Total rows | 631,159 |
| Total episodes | 4,182 |
| Success episodes | 3,613 |
| Failure/timeout episodes | 569 |
| Success rows | 460,459 |
| Failure/timeout rows | 170,700 |
| Episode length avg/min/max | 150.92 / 66 / 300 |
| Corrupt JSONL rows found | 0 |
| Missing required fields found | 0 |
| ACE candidates per row | 8 for all rows |
| `ace_replay_used` | `false` for all rows |
| Executed action check | `executed_action == main_candidate_action_chunk_env[0]` for all checked rows |
| Main chunk length | 10 for all rows |
| Executed action length | 7 for all rows |

The collector implementation matches the intended real-time monitor data semantics:

- receding horizon execution
- one random main chunk per timestep
- only the first action of that main chunk is executed
- ACE candidates are sampled from the same observation
- ACE candidates are saved only, not replayed
- all episode outcomes are saved
- success rows are marked train/calib/eval eligible
- failure/timeout rows are marked eval-only

The biggest remaining technical issue is not data volume. It is making the next train/eval run use the current v2 live data cleanly and reproducibly. The older bridge modules are partly scaffold/legacy and not sufficient alone for the current v2 schema. The strongest current analysis script is `run_full_analysis.py`, but it is hard-coded to the old archive path and should be parameterized or copied for the current frozen `fiper_sweep_eternal` snapshot before training.

Final decision:

`READY_FOR_FULL_FIPER_TRAIN_EVAL = YES`

Meaning: yes for the next offline full RND + ACE + FIPER train/eval campaign on a frozen snapshot, with `libero_10_with_milk` task 3 and task 4 ignored by instruction. This does not mean the online deployed monitor is finished.

## 2. Current Active Processes

### Local `/home/redafrix/tests/internship`

No local Stage 9/FIPER collection or training process was found. Local status during audit:

| Resource | Status |
|---|---|
| GPU | RTX 4060 Laptop, 15 MiB / 8188 MiB, about 20% util |
| RAM | 30 GiB total, 23 GiB available |
| Disk `/` | 302 GiB total, 51 GiB available, 83% used |
| Local `stage9_libero_pro_risk_data` | not present locally |

### Sam `PCROBOTUBUNTU05`

Active final collection processes:

| PID | Instance | Suites | Command summary | Status |
|---:|---|---|---|---|
| 3307980 | `instance_A` | `libero_spatial_with_mug`, `libero_object_with_mug`, `libero_goal_with_mug` | `collect_fiper_receding_all_outcomes_v2 --ace-candidates 8 --max-timesteps 300` | running |
| 3307901 | `instance_B` | `libero_spatial_with_milk`, `libero_10_with_milk`, `libero_goal_with_milk` | same collector, `--env-seed 42` | running |

Sam resource status during audit:

| Resource | Status |
|---|---|
| GPU | RTX 4070 Ti SUPER, 11,720 MiB / 16,376 MiB, 76% util, 79 C |
| RAM | 30 GiB total, 17 GiB available, 35 MiB swap used |
| Disk `/` | 468 GiB total, 152 GiB available, 66% used |
| Training processes | none found |
| Other notable process | old SmolVLM server still running, not part of this collection |

Sam active logs show the collection is still progressing. The main warning/error of interest is repeated, logged skipping of unavailable `libero_10_with_milk_t3` and `libero_10_with_milk_t4`:

```text
Skipping unavailable libero_10_with_milk_t3: Object 'milk_1' already has sampler associated with it!
Skipping unavailable libero_10_with_milk_t4: Object 'milk_1' already has sampler associated with it!
```

Per the user update during this audit, task 3 and task 4 for `libero_10_with_milk` are ignored.

### Bob `PCROBOTUBUNTU02`

Active final collection processes:

| PID | Instance | Suites | Command summary | Status |
|---:|---|---|---|---|
| 1841087 | `instance_A` | `libero_spatial_object`, `libero_object_object`, `libero_goal_object` | `collect_fiper_receding_all_outcomes_v2 --ace-candidates 8 --max-timesteps 300` | running |
| 1841632 | `instance_B` | `libero_spatial_env`, `libero_object_env`, `libero_goal_env` | same collector, `--env-seed 123` | running |

Bob resource status during audit:

| Resource | Status |
|---|---|
| GPU | RTX 4070 Ti SUPER, 11,233 MiB / 16,376 MiB, 100% util, 85 C |
| RAM | 30 GiB total, 19 GiB available, 1.3 GiB swap used |
| Disk `/media/rootalkhatib/My Passport` | 1.9 TiB total, 737 GiB available, 61% used |
| Training processes | none found |
| Other notable process | unrelated `marathon_c_50.py --idea 22` |

Bob active logs show current object/env collection is still progressing. Old `instance_A.log` and `instance_B.log` contain earlier failed launch errors, but the active `bob_obj.log` and `bob_env.log` are running normally.

## 3. Current Campaign Roots

### Sam

Root:

```text
/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/fiper_sweep_eternal
```

Current files audited:

| File | Rows | Approx size |
|---|---:|---:|
| `instance_A/fiper_receding_samples.jsonl` | 158,601 | 5.298 GB |
| `instance_B/fiper_receding_samples.jsonl` | 158,720 | 5.273 GB |
| `sam_mug.log` | active log | 191 KB |
| `sam_milk.log` | active log | 184 KB |

Sam campaign disk usage was about 12 GB.

### Bob

Root:

```text
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/fiper_sweep_eternal
```

Current files audited:

| File | Rows | Approx size |
|---|---:|---:|
| `instance_A/fiper_receding_samples.jsonl` | 156,924 | 5.205 GB |
| `instance_B/fiper_receding_samples.jsonl` | 156,914 | 5.203 GB |
| `bob_obj.log` | active log | 201 KB |
| `bob_env.log` | active log | 198 KB |

Bob campaign disk usage was about 317 GB, mostly under `states/`. Disk space is still acceptable.

## 4. Dataset Inventory After Days Of Collection

This is a live snapshot. The files were still growing during audit.

### Machine Totals

| Machine | Rows | Episodes | Success episodes | Failure/timeout episodes | Success rows | Failure/timeout rows |
|---|---:|---:|---:|---:|---:|---:|
| Sam | 317,321 | 1,942 | 1,577 | 365 | 207,821 | 109,500 |
| Bob | 313,838 | 2,240 | 2,036 | 204 | 252,638 | 61,200 |
| Total | 631,159 | 4,182 | 3,613 | 569 | 460,459 | 170,700 |

### Perturbation Group Totals

| Group | Rows | Episodes | Success episodes | Failure/timeout episodes | Success rows | Failure/timeout rows |
|---|---:|---:|---:|---:|---:|---:|
| mug | 158,601 | 1,024 | 860 | 164 | 109,401 | 49,200 |
| milk | 158,720 | 918 | 717 | 201 | 98,504 | 60,300 |
| object | 156,924 | 1,109 | 1,001 | 108 | 124,675 | 32,400 |
| env | 156,914 | 1,131 | 1,035 | 96 | 128,194 | 28,800 |

### Suite Totals

| Suite | Rows | Success rows | Failure rows | Episodes | Success episodes | Failure episodes |
|---|---:|---:|---:|---:|---:|---:|
| `libero_10_with_milk` | 69,450 | 32,850 | 36,600 | 264 | 142 | 122 |
| `libero_goal_with_milk` | 41,882 | 33,266 | 8,700 | 324 | 295 | 29 |
| `libero_goal_with_mug` | 43,423 | 34,123 | 9,300 | 340 | 309 | 31 |
| `libero_object_with_mug` | 61,481 | 42,281 | 19,200 | 340 | 276 | 64 |
| `libero_spatial_with_milk` | 47,388 | 32,388 | 15,000 | 330 | 280 | 50 |
| `libero_spatial_with_mug` | 53,697 | 32,997 | 20,700 | 344 | 275 | 69 |
| `libero_goal_env` | 45,942 | 37,922 | 8,100 | 371 | 344 | 27 |
| `libero_goal_object` | 47,897 | 36,348 | 11,700 | 369 | 330 | 39 |
| `libero_object_env` | 63,063 | 53,763 | 9,300 | 380 | 349 | 31 |
| `libero_object_object` | 61,837 | 53,137 | 8,700 | 370 | 341 | 29 |
| `libero_spatial_env` | 47,909 | 36,509 | 11,400 | 380 | 342 | 38 |
| `libero_spatial_object` | 47,190 | 35,190 | 12,000 | 370 | 330 | 40 |

### Episode Length

| Machine | Avg | Min | Max |
|---|---:|---:|---:|
| Sam | 163.40 | 67 | 300 |
| Bob | 140.11 | 66 | 300 |
| Combined | 150.92 | 66 | 300 |

### Schema / Integrity Checks

| Check | Result |
|---|---|
| Corrupt JSONL rows | 0 |
| Missing required fields | 0 |
| Invalid suite rows outside final intended list | 0 |
| ACE candidate count distribution | `{8: 631159}` |
| ACE candidate seed count distribution | `{8: 631159}` |
| `ace_replay_used` distribution | `{False: 631159}` |
| Main chunk length distribution | `{10: 631159}` |
| Executed action length distribution | `{7: 631159}` |
| Executed action equals first main action | 631,159 / 631,159 checked |
| Unique main seeds | 631,104 |
| Unique ACE candidate seeds | 5,046,243 |

Deployability metadata in all checked rows:

| Field | Value |
|---|---|
| `proprio_deployable` | `true` |
| `history_deployable` | `true` |
| `candidate_action_deployable` | `true` |
| `object_positions_deployable` | `true` |
| `sim_state_deployable` | `false` |
| `before_image_deployable` | `true` |

Interpretation: the logged monitor inputs are deployable except simulator state. That is expected. Training/eval must not depend on simulator state if the target is real-time deployment.

## 5. Coverage Matrix

Cell format: `success episodes / failure-or-timeout episodes`.

`libero_10_with_milk` task 3 and task 4 are ignored by user instruction.

| Suite | t0 | t1 | t2 | t3 | t4 | t5 | t6 | t7 | t8 | t9 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `libero_10_with_milk` | 29/4 | 0/33 | 9/24 | ignored | ignored | 28/5 | 11/22 | 18/15 | 23/10 | 24/9 |
| `libero_goal_with_milk` | 20/13 | 31/2 | 31/2 | 32/1 | 31/1 | 31/1 | 25/7 | 32/0 | 30/2 | 32/0 |
| `libero_goal_with_mug` | 23/11 | 30/4 | 29/5 | 29/5 | 34/0 | 34/0 | 28/6 | 34/0 | 34/0 | 34/0 |
| `libero_object_with_mug` | 26/8 | 33/1 | 13/21 | 25/9 | 31/3 | 34/0 | 19/15 | 30/4 | 32/2 | 33/1 |
| `libero_spatial_with_milk` | 33/0 | 32/1 | 26/7 | 33/0 | 31/2 | 32/1 | 32/1 | 2/31 | 29/4 | 30/3 |
| `libero_spatial_with_mug` | 23/12 | 32/3 | 35/0 | 35/0 | 33/1 | 7/27 | 34/0 | 24/10 | 21/13 | 31/3 |
| `libero_goal_env` | 28/10 | 34/3 | 32/5 | 33/4 | 37/0 | 36/1 | 37/0 | 37/0 | 35/2 | 35/2 |
| `libero_goal_object` | 24/13 | 33/4 | 30/7 | 31/6 | 37/0 | 37/0 | 36/1 | 37/0 | 34/3 | 31/5 |
| `libero_object_env` | 27/11 | 26/12 | 36/2 | 36/2 | 37/1 | 38/0 | 35/3 | 38/0 | 38/0 | 38/0 |
| `libero_object_object` | 30/7 | 28/9 | 33/4 | 34/3 | 36/1 | 37/0 | 36/1 | 34/3 | 36/1 | 37/0 |
| `libero_spatial_env` | 38/0 | 37/1 | 38/0 | 38/0 | 36/2 | 7/31 | 38/0 | 36/2 | 37/1 | 37/1 |
| `libero_spatial_object` | 37/0 | 37/0 | 37/0 | 37/0 | 34/3 | 3/34 | 37/0 | 36/1 | 36/1 | 36/1 |

Rows per suite/task:

| Suite | t0 | t1 | t2 | t3 | t4 | t5 | t6 | t7 | t8 | t9 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `libero_10_with_milk` | 6,523 | 9,900 | 9,487 | ignored | ignored | 7,672 | 9,386 | 8,921 | 8,922 | 8,639 |
| `libero_goal_with_milk` | 6,947 | 6,351 | 4,144 | 3,233 | 2,909 | 3,150 | 4,658 | 4,539 | 3,651 | 2,300 |
| `libero_goal_with_mug` | 6,417 | 3,854 | 4,110 | 6,947 | 2,895 | 4,326 | 4,623 | 2,491 | 3,049 | 4,711 |
| `libero_object_with_mug` | 6,840 | 5,277 | 8,702 | 7,463 | 6,368 | 5,153 | 7,391 | 4,975 | 4,464 | 4,848 |
| `libero_spatial_with_milk` | 2,941 | 3,419 | 5,794 | 3,678 | 4,138 | 3,953 | 3,488 | 9,515 | 5,987 | 4,475 |
| `libero_spatial_with_mug` | 6,383 | 4,750 | 4,011 | 3,095 | 4,771 | 9,166 | 3,799 | 7,104 | 6,154 | 4,464 |
| `libero_goal_env` | 7,438 | 3,729 | 4,610 | 7,231 | 3,126 | 5,148 | 3,341 | 2,626 | 3,470 | 5,223 |
| `libero_goal_object` | 7,338 | 3,992 | 5,012 | 7,538 | 3,192 | 5,006 | 3,629 | 2,695 | 3,621 | 5,874 |
| `libero_object_env` | 8,139 | 8,638 | 5,999 | 6,334 | 5,856 | 5,080 | 7,236 | 5,061 | 6,156 | 4,564 |
| `libero_object_object` | 7,636 | 8,042 | 6,338 | 6,212 | 5,687 | 4,933 | 7,021 | 5,471 | 6,048 | 4,449 |
| `libero_spatial_env` | 2,865 | 4,598 | 3,537 | 3,191 | 5,083 | 10,594 | 3,915 | 5,995 | 3,596 | 4,535 |
| `libero_spatial_object` | 2,791 | 4,215 | 3,643 | 3,065 | 5,362 | 10,672 | 3,816 | 5,743 | 3,502 | 4,381 |

Coverage interpretation:

- The dataset is broad enough for the next global train/calib/test/eval campaign.
- It is not perfectly balanced.
- Some cells are failure-heavy and success-light, especially `libero_10_with_milk_t1`, `libero_spatial_with_milk_t7`, `libero_spatial_with_mug_t5`, `libero_spatial_env_t5`, and `libero_spatial_object_t5`.
- Those imbalance cells are useful for failure evaluation, but they are weak for per-task success-only calibration.
- For global or suite/group-level RND train/calib/test, the success volume is enough.
- For strict per-task RND calibration, more success rows would be needed in low-success cells.

## 6. Collector Implementation Audit

Main collector audited:

```text
stage9_v2_tools/data_collection_stage9/collect_fiper_receding_all_outcomes_v2.py
```

Findings:

| Requirement | Audit result |
|---|---|
| Receding horizon | implemented |
| Random main seed per timestep | implemented |
| Save full main chunk | implemented |
| Execute only first action | implemented |
| Sample ACE candidates from same observation | implemented |
| Save ACE chunks only | implemented |
| Do not replay ACE chunks | implemented |
| Continue receding horizon | implemented |
| Save all outcomes | implemented |
| Success rows train/calib/eval eligible | implemented |
| Failure/timeout rows eval-only | implemented |
| Round-robin suite/task scheduling | implemented |
| Broken suite/task logging | implemented, not silent |

Code-level evidence:

- `generate_chunk(...)` samples a candidate chunk from SimVLA without stepping the env.
- The sweep loop iterates suite and task IDs round-robin.
- Env construction is wrapped in try/except and logs `Skipping unavailable ...` before continuing.
- The observation is captured before action.
- `main_seed = random.randint(...)` is generated per timestep.
- The main chunk is generated once from the current observation.
- ACE seeds and ACE chunks are generated from the same `obs` before the environment step.
- Rows store `main_candidate_action_chunk_env`, `main_candidate_action_chunk_normalized`, `executed_action`, `ace_candidate_chunks_env`, `ace_candidate_chunks_normalized`, `ace_candidate_seeds`, and `ace_replay_used=False`.
- The executed action is `main_chunk[0]`.
- The only env step at the timestep is `env.step(act)` where `act` is the first action of the main chunk.
- Episode rows are backfilled after the episode with:
  - `episode_outcome = "success"` and `allowed_use = "train_calib_eval_success"` for successes
  - `episode_outcome = "failure_or_timeout"` and `allowed_use = "eval_only_failure"` for failures/timeouts

Important behavior:

- Rows are appended after the full episode, not per step. That makes each written episode internally coherent.
- The current collector is `collect_fiper_receding_all_outcomes_v2.py`. The v1 name in older notes should be treated as historical.

Launch script audited:

```text
launch_eternal_fiper_sweep.sh
```

It matches the intended final suite list:

- Sam mug: `libero_spatial_with_mug`, `libero_object_with_mug`, `libero_goal_with_mug`
- Sam milk: `libero_spatial_with_milk`, `libero_10_with_milk`, `libero_goal_with_milk`
- Bob object: `libero_spatial_object`, `libero_object_object`, `libero_goal_object`
- Bob env: `libero_spatial_env`, `libero_object_env`, `libero_goal_env`

Legacy caution:

```text
stage9_v2_tools/scripts/fiper_sweep_sam.sh
```

still contains the invalid old `libero_object_with_milk` path and should not be used for the final current collection.

## 7. RND / ACE / FIPER Pipeline Audit

### What Exists

Working previous analysis path:

```text
run_full_analysis.py
```

This is the strongest existing end-to-end offline analysis script. It handles the current v2 row schema concepts:

- reads v2 JSONL rows
- checks required fields
- checks `ace_replay_used`
- checks executed action equals first main action
- builds episode-safe splits
- computes ACE from `ace_candidate_chunks_normalized`
- trains action-heavy RND on successful main chunks
- calibrates thresholds on success calibration data
- evaluates failure rows
- runs corrupted-action sanity tests
- computes RND + ACE FIPER quadrants
- writes reports and model checkpoints

But it is hard-coded to:

```text
/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/archive_20260522
```

For the current final data, it should be parameterized or copied into a current-campaign analyzer before running.

Other useful scripts:

| File | Status |
|---|---|
| `run_expert_transfer_analysis.py` | useful prior experiment; not the final method |
| `stage9_v2_tools/train_rnd_oe_fixed.py` | fixed old constant-feature RND issue, but targets older schema |
| `stage9_v2_tools/evaluate_success_only_fiper.py` | older success-only FIPER path, not current v2 final dataset path |
| `fiper_ws/stage9_fiper_bridge/conformal.py` | useful threshold utilities |
| `fiper_ws/stage9_fiper_bridge/rnd_oe.py` | scaffold RND/OE module; not production-ready for final v2 deployment |
| `fiper_ws/stage9_fiper_bridge/ace.py` | older same-state/grouped ACE helper; not directly current v2 row-ready |
| `fiper_ws/stage9_fiper_bridge/stage9_io.py` | old grouping helpers; current v2 rows do not use its expected `state_id` fields |

### What Is Missing Before Training/Eval

Missing for the next campaign:

1. A frozen snapshot or explicit stop point. Do not train directly on growing JSONLs.
2. A current-campaign version of `run_full_analysis.py` that takes the Sam/Bob `fiper_sweep_eternal` JSONL paths as arguments.
3. Explicit exclusion config for ignored `libero_10_with_milk` task 3 and task 4.
4. A split manifest saved before training, with episode IDs, suite, task, perturbation group, and outcome.
5. Per-task and per-group evaluation tables, because the current dataset is not perfectly balanced.

Missing for real deployment:

1. Online latency measurement for SimVLA main chunk plus 8 ACE candidate chunks.
2. Runtime threshold service or monitor wrapper.
3. Online logging format for RND, ACE, thresholds, quadrant, and intervention decision.
4. A recovery or action policy after alarm.
5. Real closed-loop deployment validation with alarm-only mode before intervention.

## 8. Previous Report Synthesis

### Old Terminal Labels / VLM Audit

The old `VALIDATED_BAD` labels are not trustworthy for RND training or calibration. They were heavily contaminated by terminal outcome artifacts and weak local evidence. The VLM audit was useful as a disagreement detector, not as a final labeler. The old BAD set should not be treated as verified local action-bad labels.

Relevant conclusions from prior reports:

- `VLM_AUDIT_PIPELINE_WORKS = YES`
- `VLM_CAN_CERTIFY_LABELS_ALONE = NO`
- `CURRENT_DATASET_NEEDS_RELABEL_V2_BEFORE_FINAL_TRAINING = YES`
- old terminal failure labels must not be used for RND train/calib

For the current FIPER direction, this means:

- success rows can train/calibrate RND
- failure/timeout rows are eval/challenge only
- ACE/RND monitor quality must be judged against held-out outcomes and perturbation shifts, not old local BAD labels

### First Receding FIPER Full Test

Report:

```text
gemini_handoff_current/STAGE9_FIPER_RECEDING_FULL_TEST_REPORT.md
```

Key result:

- RND + ACE looked promising.
- ACE and RND were complementary.
- Combined monitor flagged 72.06% of failure steps in that prior 64-candidate dataset under q95-style thresholds.
- ACE caught failures RND missed.
- RND caught some failures ACE missed.
- RND was sensitive to action corruptions.
- RND was very task-specific and false-alarmed under cross-suite shifts.

### Archive 20260522 Analysis

Report:

```text
gemini_handoff_current/STAGE9_ARCHIVE_20260522_FULL_ANALYSIS_REPORT.md
```

Key result:

- The archive 8-candidate receding data had clean schema, no corrupt rows, correct no-replay ACE, and correct first-action execution.
- ACE was the stronger failure signal.
- Archive-trained RND alone was weaker but useful as a secondary action-normality signal.
- Combined RND + ACE was still the target.
- RND remained sensitive to task/suite shifts, so task/group-aware reporting is mandatory.

### Expert LIBERO RND Transfer Test

Report:

```text
gemini_handoff_current/STAGE9_LIBERO_EXPERT_TO_RECEDING_ARCHIVE_EVAL_REPORT.md
```

Key result:

- `LIBERO_EXPERT_FIPER_DOES_NOT_TRANSFER`
- Official LIBERO expert-only RND did not transfer well to receding LIBERO-PRO rollouts.
- Expert RND failure detection was low compared with ACE-only.
- `libero_90` training was not helpful and was considered harmful for this transfer setting.
- The reason is distribution shift: static expert demonstrations do not match closed-loop receding SimVLA feedback dynamics.

Current implication:

- train/calibrate RND mainly on successful closed-loop receding SimVLA rows
- do not use `libero_90` in the final current collection
- keep ACE as the primary policy uncertainty signal

### Sam Data Audit / Launch Reports

Reports:

```text
SAM_DATA_AUDIT.md
FINAL_DEPLOYMENT_SUCCESS_REPORT.md
```

Key result:

- The final `fiper_sweep_eternal` launch was intended to run continuously across Sam and Bob.
- The invalid `libero_object_with_milk` suite was replaced by `libero_10_with_milk`.
- Current live process PIDs still match the deployed final sweep family.

## 9. What Is Trustworthy

Trustworthy:

- Current v2 JSONL row schema for monitor inputs.
- Current collector's no-replay ACE semantics.
- Current collector's first-action-only receding execution.
- Current episode outcome marking at row level.
- Current success/failure episode counts from the audited snapshot.
- Current suite list in `launch_eternal_fiper_sweep.sh`.
- Current evidence that final collection is still running.
- ACE as the strongest current failure-proximity signal from previous analyses.
- Success-only closed-loop receding rollouts as the correct RND train/calib source.

## 10. What Is Not Trustworthy

Not trustworthy:

- Old `VALIDATED_BAD` labels as local action-bad ground truth.
- Failure/timeout rows for RND training or calibration.
- Official LIBERO expert-only RND as the final transfer monitor.
- `libero_90` for current final collection/training.
- Legacy `libero_object_with_milk`.
- Legacy `fiper_sweep_sam.sh` final-suite configuration.
- The old `stage9_fiper_bridge` modules as a complete current v2 training/deployment pipeline without adaptation.
- Direct training on live growing JSONLs.

## 11. Remaining Blockers

For next offline train/eval:

1. Freeze or snapshot the current JSONLs before training.
2. Parameterize/copy `run_full_analysis.py` for the current Sam/Bob `fiper_sweep_eternal` paths.
3. Add an exclusion list for `libero_10_with_milk` task 3 and task 4.
4. Save a split manifest and all thresholds/checkpoints.
5. Report low-success cells separately, especially:
   - `libero_10_with_milk_t1`
   - `libero_spatial_with_milk_t7`
   - `libero_spatial_with_mug_t5`
   - `libero_spatial_env_t5`
   - `libero_spatial_object_t5`

For deployment:

1. Make a real-time monitor wrapper.
2. Benchmark latency for 1 main chunk + 8 ACE candidates per timestep.
3. Store online RND/ACE/quadrant logs.
4. Decide alarm behavior.
5. Run alarm-only online validation before any intervention.

## 12. Whether Data Is Ready For Training/Eval

Question-by-question:

| Question | Answer |
|---|---|
| Enough success rows for RND train/calib/test? | Yes. 460,459 success rows, 3,613 success episodes. |
| Enough failure rows for evaluation? | Yes. 170,700 failure/timeout rows, 569 failure/timeout episodes. |
| Enough per-perturbation coverage? | Yes for mug, milk, object, env, with ignored milk task 3/4 caveat. |
| Enough task coverage? | Yes for global/suite/group train/eval; weak for strict per-task calibration in low-success cells. |
| Are OOD task/object/env tests now possible? | Yes. The data has enough task, suite, object, and env perturbation coverage for meaningful OOD analysis. |
| Is current data balanced enough? | Good enough for next full offline campaign; not perfectly balanced. |
| Should collection continue, stop, or adjust? | Do not stop from this audit. For training, freeze/snapshot now or explicitly stop later. Continue only if more balance is desired. |

Final decision:

`READY_FOR_FULL_FIPER_TRAIN_EVAL = YES`

Exact meaning:

- YES for a frozen-snapshot offline RND + ACE + FIPER train/eval campaign.
- YES only with `libero_10_with_milk` task 3 and task 4 excluded/ignored.
- NO claim of final online deployment readiness yet.

## 13. Recommended Next Command / Work Plan

Do not start this automatically. This is the recommended next phase when explicitly requested.

1. Freeze the live dataset into a read-only snapshot or explicitly stop the collectors if the user decides the live campaign is complete.
2. Create a current-campaign analysis script from `run_full_analysis.py` with CLI arguments:
   - `--sam-root /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/fiper_sweep_eternal`
   - `--bob-root "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/fiper_sweep_eternal"`
   - `--exclude-suite-task libero_10_with_milk:3`
   - `--exclude-suite-task libero_10_with_milk:4`
   - `--out-dir /home/rootalkhatib/test/reda_ws/fiper_ws/experiments/current_fiper_sweep_eternal_full_analysis_YYYYMMDD_HHMMSS`
3. Build episode-safe splits:
   - success train
   - success calibration
   - success ID test
   - failure eval all
   - failure early/late/near-end eval
   - OOD task success
   - OOD suite success
   - OOD perturbation success
   - OOD object success
   - OOD env success
4. Train success-only action-heavy RND on successful closed-loop receding main chunks only.
5. Compute ACE from `ace_candidate_chunks_normalized`.
6. Calibrate RND and ACE thresholds on success calibration rows.
7. Evaluate:
   - ID false alarm
   - failure detection
   - early/late failure detection
   - suite/task/group OOD false alarms
   - corrupted-action sanity
   - RND-only, ACE-only, RND OR ACE, RND AND ACE, and quadrant results
8. Save:
   - split manifest
   - RND predictor/target checkpoints
   - normalization stats
   - thresholds
   - eval JSON/CSV tables
   - final report

## 14. Exact Files Read

Local memory/context:

```text
/home/redafrix/.codex/memories/MEMORY.md
```

Current collector and launch code:

```text
/home/redafrix/tests/internship/stage9_v2_tools/data_collection_stage9/collect_fiper_receding_all_outcomes_v2.py
/home/redafrix/tests/internship/launch_eternal_fiper_sweep.sh
/home/redafrix/tests/internship/stage9_v2_tools/scripts/fiper_sweep_sam.sh
/home/redafrix/tests/internship/stage9_v2_tools/scripts/fiper_sweep_bob.sh
```

FIPER/RND/ACE code:

```text
/home/redafrix/tests/internship/run_full_analysis.py
/home/redafrix/tests/internship/run_expert_transfer_analysis.py
/home/redafrix/tests/internship/stage9_v2_tools/train_rnd_oe_fixed.py
/home/redafrix/tests/internship/stage9_v2_tools/evaluate_success_only_fiper.py
/home/redafrix/tests/internship/fiper_ws/stage9_fiper_bridge/ace.py
/home/redafrix/tests/internship/fiper_ws/stage9_fiper_bridge/rnd_oe.py
/home/redafrix/tests/internship/fiper_ws/stage9_fiper_bridge/conformal.py
/home/redafrix/tests/internship/fiper_ws/stage9_fiper_bridge/stage9_io.py
```

Primary reports read or searched directly:

```text
/home/redafrix/tests/internship/gemini_handoff_current/STAGE9_FIPER_RECEDING_FULL_TEST_REPORT.md
/home/redafrix/tests/internship/gemini_handoff_current/STAGE9_ARCHIVE_20260522_FULL_ANALYSIS_REPORT.md
/home/redafrix/tests/internship/gemini_handoff_current/STAGE9_LIBERO_EXPERT_TO_RECEDING_ARCHIVE_EVAL_REPORT.md
/home/redafrix/tests/internship/gemini_handoff_current/ace_success_vs_failure_report.md
/home/redafrix/tests/internship/gemini_handoff_current/corrupted_action_sanity_report.md
/home/redafrix/tests/internship/gemini_handoff_current/fiper_combined_analysis_report.md
/home/redafrix/tests/internship/gemini_handoff_current/ood_suite_smoke_report.md
/home/redafrix/tests/internship/gemini_handoff_current/receding_dataset_inventory.md
/home/redafrix/tests/internship/gemini_handoff_current/rnd_success_only_vs_failure_report.md
/home/redafrix/tests/internship/gemini_handoff_current/split_summary.md
/home/redafrix/tests/internship/gemini_handoff_current/supervised_episode_outcome_diagnostic_report.md
/home/redafrix/tests/internship/gemini_handoff_current/STAGE9_OBJECT_ENV_PERTURBATION_SETUP_REPORT.md
/home/redafrix/tests/internship/FINAL_DEPLOYMENT_SUCCESS_REPORT.md
/home/redafrix/tests/internship/SAM_DATA_AUDIT.md
/home/redafrix/tests/internship/codex_reports/stage9/STAGE9_VLM_LABEL_AUDIT_EXPERIMENT_REPORT.md
/home/redafrix/tests/internship/codex_reports/stage9/done/STAGE9_CORRECTED_LABEL_PIPELINE_REPORT.md
/home/redafrix/tests/internship/codex_reports/stage9/done/STAGE9_SINGLE_README_REPORT.md
/home/redafrix/tests/internship/codex_reports/stage9/STAGE9_CONTINUOUS_RISK_LABELING_METHOD_COMPARISON_REPORT.md
```

Remote paths inspected or searched:

```text
/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/fiper_sweep_eternal
/home/rootalkhatib/test/reda_ws/fiper_ws
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/fiper_sweep_eternal
```

Note: the specifically named local files `STAGE9_PIPELINE_CLARIFICATION_AND_STATUS_REPORT.md`, `STAGE9_FIPER_RECEDING_ACE_NO_REPLAY_FIX.md`, `STAGE9_FIPER_RECEDING_ALL_OUTCOMES_LAUNCH_REPORT.md`, and `STAGE9_FIPER_RECEDING_COLLECTION_12H_STATUS_REPORT.md` were searched for by filename in the local workspace and were not found under `/home/redafrix/tests/internship`. Equivalent launch/status conclusions were recovered from `FINAL_DEPLOYMENT_SUCCESS_REPORT.md`, `SAM_DATA_AUDIT.md`, live processes, logs, and the collector code.

## 15. Exact Commands Run

Memory/context:

```bash
rg -n "Stage 9|LIBERO-PRO|FIPER|RND|ACE|stage9_libero_pro_risk_data|STAGE9_FIPER|GOOD_STRONG|VLM audit" /home/redafrix/.codex/memories/MEMORY.md
nl -ba /home/redafrix/.codex/memories/MEMORY.md | sed -n '1,110p'
```

Local file discovery/status:

```bash
pwd && rg --files | sed -n '1,160p'
ps -eo pid,ppid,stat,etime,%cpu,%mem,cmd | rg -i "collect_fiper|fiper_sweep|launch_eternal|train_rnd|rnd_oe|libero|simvla|stage9|fiper_ws"
nvidia-smi
free -h
df -h /
ls -ld /home/rootalkhatib /home/rootalkhatib/test/reda_ws /media/rootalkhatib "/media/rootalkhatib/My Passport/reda_ws"
find /home/redafrix/tests/internship -name 'STAGE9_PIPELINE_CLARIFICATION_AND_STATUS_REPORT.md' -o -name 'STAGE9_FIPER_RECEDING_ACE_NO_REPLAY_FIX.md' -o -name 'STAGE9_FIPER_RECEDING_ALL_OUTCOMES_LAUNCH_REPORT.md' -o -name 'STAGE9_FIPER_RECEDING_COLLECTION_12H_STATUS_REPORT.md' -o -name 'FINAL_DEPLOYMENT_SUCCESS_REPORT.md' -o -name 'SAM_DATA_AUDIT.md' | sort
find /home/redafrix/tests/internship -name run_full_analysis.py -o -name run_expert_transfer_analysis.py -o -name train_rnd_oe_fixed.py -o -name evaluate_success_only_fiper.py 2>/dev/null | sort
rg --files | rg '(^|/)launch_eternal_fiper_sweep\.sh$|collect_fiper_receding_all_outcomes_v[12]\.py$|stage9_fiper_bridge/(ace|rnd_oe|conformal|stage9_io)\.py$|run_full_analysis\.py$|run_expert_transfer_analysis\.py$|train_rnd_oe_fixed\.py$|evaluate_success_only_fiper\.py$'
```

Local code/report reads:

```bash
nl -ba stage9_v2_tools/data_collection_stage9/collect_fiper_receding_all_outcomes_v2.py | sed -n '1,260p'
nl -ba launch_eternal_fiper_sweep.sh | sed -n '1,220p'
nl -ba stage9_v2_tools/scripts/fiper_sweep_sam.sh | sed -n '1,180p'
nl -ba stage9_v2_tools/scripts/fiper_sweep_bob.sh | sed -n '1,180p'
nl -ba fiper_ws/stage9_fiper_bridge/ace.py | sed -n '1,240p'
nl -ba fiper_ws/stage9_fiper_bridge/rnd_oe.py | sed -n '1,260p'
nl -ba fiper_ws/stage9_fiper_bridge/conformal.py | sed -n '1,220p'
nl -ba fiper_ws/stage9_fiper_bridge/stage9_io.py | sed -n '1,220p'
nl -ba run_full_analysis.py | sed -n '1,90p;115,210p;225,360p;372,696p;700,790p;798,1015p'
nl -ba run_expert_transfer_analysis.py | sed -n '1,260p'
nl -ba stage9_v2_tools/train_rnd_oe_fixed.py | sed -n '1,260p'
nl -ba stage9_v2_tools/evaluate_success_only_fiper.py | sed -n '1,260p'
sed -n '1,220p' FINAL_DEPLOYMENT_SUCCESS_REPORT.md
sed -n '1,220p' SAM_DATA_AUDIT.md
find /home/redafrix/tests/internship/codex_reports/stage9 -maxdepth 3 -type f \( -name '*.md' -o -name '*.txt' \) | sort
find /home/redafrix/tests/internship/gemini_handoff_current -maxdepth 2 -type f \( -name '*.md' -o -name '*.txt' \) | sort
rg -n "FINAL_DECISION|Final Decision|READY|VALIDATED_BAD|LABELER_READY|CURRENT_DATASET|VLM_AUDIT|GOOD_STRONG|GOOD_WEAK|AMBIGUOUS|EEF closer|RND|ACE|FIPER|libero_90|expert-only|archive|receding" codex_reports/stage9 gemini_handoff_current FINAL_DEPLOYMENT_SUCCESS_REPORT.md SAM_DATA_AUDIT.md | sed -n '1,260p'
```

Sam live status:

```bash
ssh sam 'hostname; date; ps -eo pid,ppid,stat,lstart,etime,%cpu,%mem,cmd | egrep "collect_fiper|fiper_sweep|launch_eternal|train_rnd|rnd_oe|libero|simvla|stage9|fiper_ws" | grep -v egrep'
ssh sam 'nvidia-smi; free -h; df -h / /home/rootalkhatib/test/reda_ws 2>/dev/null'
ssh sam 'du -sh /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/fiper_sweep_eternal/*'
ssh sam 'find /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/fiper_sweep_eternal -maxdepth 3 -type f -printf "%p %s\n" | sort'
ssh sam 'tail -n 120 /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/fiper_sweep_eternal/sam_mug.log'
ssh sam 'tail -n 120 /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/fiper_sweep_eternal/sam_milk.log'
ssh sam 'grep -RniE "error|exception|traceback|warning|skipping|failed|nan|oom|cuda" /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/fiper_sweep_eternal/*.log | tail -n 200'
ssh sam 'find /home/rootalkhatib/test/reda_ws -name run_full_analysis.py -o -name run_expert_transfer_analysis.py -o -name train_rnd_oe_fixed.py -o -name evaluate_success_only_fiper.py 2>/dev/null | sort'
ssh sam 'find /home/rootalkhatib/test/reda_ws -name "STAGE9_PIPELINE_CLARIFICATION_AND_STATUS_REPORT.md" -o -name "STAGE9_FIPER_RECEDING_ACE_NO_REPLAY_FIX.md" -o -name "STAGE9_FIPER_RECEDING_ALL_OUTCOMES_LAUNCH_REPORT.md" -o -name "STAGE9_FIPER_RECEDING_COLLECTION_12H_STATUS_REPORT.md" -o -name "FINAL_DEPLOYMENT_SUCCESS_REPORT.md" -o -name "SAM_DATA_AUDIT.md" 2>/dev/null | sort'
```

Bob live status:

```bash
ssh pcrobot 'hostname; date; ps -eo pid,ppid,stat,lstart,etime,%cpu,%mem,cmd | egrep "collect_fiper|fiper_sweep|launch_eternal|train_rnd|rnd_oe|libero|simvla|stage9|fiper_ws" | grep -v egrep'
ssh pcrobot 'nvidia-smi; free -h; df -h "/media/rootalkhatib/My Passport" / 2>/dev/null'
ssh pcrobot 'du -sh "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/fiper_sweep_eternal"/*'
ssh pcrobot 'find "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/fiper_sweep_eternal" -maxdepth 3 -type f -printf "%p %s\n" | sort'
ssh pcrobot 'tail -n 120 "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/fiper_sweep_eternal/bob_obj.log"'
ssh pcrobot 'tail -n 120 "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/fiper_sweep_eternal/bob_env.log"'
ssh pcrobot 'grep -RniE "error|exception|traceback|warning|skipping|failed|nan|oom|cuda" "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/fiper_sweep_eternal"/*.log | tail -n 200'
```

Dataset audit:

```bash
ssh sam 'python3 - <<PY
# streamed both Sam fiper_sweep_eternal JSONLs and counted rows, episodes,
# outcomes, suites, task IDs, perturbation groups, corrupt rows, missing fields,
# ACE candidate counts, ace_replay_used, main chunk length, executed action length,
# executed_action == first main action, unique main seeds, unique ACE seeds,
# deployability flags, and last collection time.
PY'
ssh pcrobot 'python3 - <<PY
# same streaming JSONL audit for Bob fiper_sweep_eternal instance_A and instance_B.
PY'
ssh sam 'python3 - <<PY
# streamed Sam JSONLs again for row-level suite/group/task outcome counts.
PY'
ssh pcrobot 'python3 - <<PY
# streamed Bob JSONLs again for row-level suite/group/task outcome counts.
PY'
```

Continuation/check commands after interruption:

```bash
test -e codex_reports/stage9/STAGE9_CODEX_ONBOARDING_CURRENT_STATE_AUDIT.md; echo $?
ps -eo pid,ppid,stat,cmd | rg 'ssh pcrobot.*STAGE9_PIPELINE|find .*/media/rootalkhatib/My Passport/reda_ws'
kill 14925 || true; ps -p 14925 -o pid,stat,cmd
ps -eo pid,ppid,stat,cmd | rg 'ssh pcrobot.*stage9_libero_pro_risk_data/campaigns.*STAGE9_PIPELINE|ssh pcrobot.*find'
kill 15221 || true; ps -p 15221 -o pid,stat,cmd
ps -eo pid,ppid,stat,cmd | rg 'ssh pcrobot find|ssh sam find|run_full_analysis|collect_fiper'
```

The `kill` commands above only terminated my own hung remote `find` inspection processes. No collection or training process was stopped.

