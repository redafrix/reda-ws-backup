# FIPER Codex Independent Verification Report

Date: 2026-05-26  
Node used for full reruns: Sam (`/home/rootalkhatib/test/reda_ws/fiper_ws`)  
Local synced script: `/home/redafrix/tests/internship/fiper_ws/scripts/run_receding_only_fiper_train_eval.py`

## 1. Executive Summary

Codex independently audited the post-Gemini FIPER workspace, split refs, runner script, saved artifacts, and reported metrics. The original idea still looks strong, but the previous `global_v1` and OOD-task results were not clean enough to treat as final evidence because the runner had a serious row-loader bug.

Main finding:

- The generated refs use 1-based `line_no`.
- The runner used `enumerate(f)` starting at 0.
- Therefore the runner loaded the next raw JSONL row for each ref, then overwrote metadata with the ref metadata.
- This dropped the last referenced line per affected source/split and could mismatch action/ACE chunks to metadata.

Codex patched the runner, synced it to local/Sam/Bob, verified the loader by smoke test, and reran full corrected training/evaluation on Sam for:

- `experiments/fiper_receding_only_global_v2_loaderfix_20260526`
- `experiments/fiper_ood_task_8_9_v2_loaderfix_20260526`

Corrected verdict:

- `RND + ACE OR q95` still works on global receding-only data.
- Strict unseen task IDs 8/9 still show excellent failure detection.
- Success-episode false alarms remain high, especially on unseen task successes, so this is not ready as a hard-stop monitor. It is currently best interpreted as a warning/risk monitor with debounce.

## 2. Process And Sync State

Collectors and training were not running after the verification runs. Sam and Bob both compile the patched runner and have matching script hash:

```text
0e32f4d265186fff98e32cd9740f3ecc647064230df01dec90c7e28dcd0774fb  scripts/run_receding_only_fiper_train_eval.py
```

Bob was not used for full reruns. It was only checked for script sync and compilation.

## 3. Dataset And Split Verification

Combined dataset inventory still matches the prepared manifest:

```text
total rows: 635,921
success rows: 464,321
failure_or_timeout rows: 171,600
ACE candidate count: 8 for every row
ace_replay_used=false: all rows
first-action execution mismatches: 0
```

Global split refs verified independently:

| Split | Rows | Episodes | Outcome |
|---|---:|---:|---|
| success_train | 324,825 | 2,555 | success only |
| success_calib | 70,352 | 549 | success only |
| success_test_id | 69,144 | 545 | success only |
| failure_eval_all | 171,600 | 572 | failure_or_timeout only |
| failure_eval_early | 42,900 | 572 | failure_or_timeout only |
| failure_eval_mid | 85,800 | 572 | failure_or_timeout only |
| failure_eval_late | 42,900 | 572 | failure_or_timeout only |
| failure_eval_near_end | 28,600 | 572 | failure_or_timeout only |

Strict OOD task split refs verified independently:

| Split | Rows | Episodes | Tasks |
|---|---:|---:|---|
| success_train_seen | 255,705 | 2,003 | 0-7 |
| success_calib_seen | 55,698 | 431 | 0-7 |
| success_test_seen | 54,288 | 425 | 0-7 |
| success_test_ood | 98,630 | 790 | 8-9 |
| failure_eval_seen | 152,400 | 508 | 0-7 |
| failure_eval_ood | 19,200 | 64 | 8-9 |
| failure_eval_ood_late | 4,800 | 64 | 8-9 |
| failure_eval_ood_near_end | 3,200 | 64 | 8-9 |

The earlier Gemini OOD report gave wrong success episode counts. The row counts were correct; the episode counts in that report were not.

## 4. Code Fixes Applied

Patched `scripts/run_receding_only_fiper_train_eval.py`:

- Fixed row loading to use `enumerate(f, start=1)`.
- Added zero-row guard in `process_data`.
- Added `--episode-summary-splits`.
- Default episode summaries now exclude derived temporal subsets ending `_early`, `_mid`, `_late`, `_near_end`.
- Score files are cleared at the start of every run, not only eval-only.
- `fiper_scores_by_split.jsonl` now stores `episode_key` and `timestep`.
- OOD success reporting no longer assumes the split is named `success_test_id`.
- Runner snapshots itself into `experiment_dir/code/`.
- Future generated verdict text no longer hardcodes broad `READY` claims.

Loader smoke after patch:

```text
case 0 ref_line_no 273 ref_t 0 correct_t 0 next_t 1
 matches_correct True matches_next_line False
case 1 ref_line_no 274 ref_t 1 correct_t 1 next_t 2
 matches_correct True matches_next_line False
case 2 ref_line_no 275 ref_t 2 correct_t 2 next_t 3
 matches_correct True matches_next_line False
```

## 5. Corrected Full Global Result

Experiment:

```text
experiments/fiper_receding_only_global_v2_loaderfix_20260526
```

Training:

```text
epochs: 20
batch size: 256
device: cuda
loss: 0.000439927 -> 0.000111464
score rows written: 440,944 / 440,944 expected
episode summary rows: 545 success + 572 failure = 1,117
```

Thresholds:

| Signal | q90 | q95 | q99 |
|---|---:|---:|---:|
| RND | 0.027435 | 0.035757 | 0.061451 |
| ACE entropy | -342.266321 | -341.129443 | -338.542054 |

Row-level q95 rates:

| Split | RND | ACE | OR | AND |
|---|---:|---:|---:|---:|
| success_test_id | 4.00% | 3.85% | 6.35% | 1.50% |
| failure_eval_all | 23.19% | 30.97% | 35.51% | 18.65% |
| failure_eval_early | 10.05% | 5.69% | 12.14% | 3.59% |
| failure_eval_mid | 25.09% | 35.06% | 39.12% | 21.03% |
| failure_eval_late | 32.53% | 48.05% | 51.64% | 28.94% |
| failure_eval_near_end | 33.01% | 48.39% | 52.12% | 29.28% |

Failure episode-level q95:

| Signal | Detection | Det @10% | Det @25% | Det @50% | Never | Mean Norm Time |
|---|---:|---:|---:|---:|---:|---:|
| RND | 85.84% | 38.11% | 65.03% | 79.37% | 14.16% | 0.1783 |
| ACE | 86.54% | 4.02% | 41.96% | 76.92% | 13.46% | 0.3038 |
| OR | 93.53% | 38.81% | 71.33% | 89.16% | 6.47% | 0.1708 |
| AND | 69.93% | 2.10% | 28.50% | 59.27% | 30.07% | 0.3388 |

OR q95 debounce:

| K | Success Ep FA | Failure Detection | Det @25% | Mean Detection Time |
|---:|---:|---:|---:|---:|
| 1 | 72.29% | 93.53% | 71.33% | 0.1708 |
| 2 | 52.84% | 88.11% | 57.52% | 0.2135 |
| 3 | 38.35% | 84.79% | 47.38% | 0.2533 |
| 5 | 22.02% | 79.02% | 39.34% | 0.2876 |

Corruption sanity remains useful:

```text
random_uniform: 100.00%
gaussian_noise_high: 100.00%
gripper_flipped: 83.53%
shuffled_timestep_order: 63.66%
zero: 0.00%
```

Interpretation:

- The corrected global result validates the main RND+ACE idea.
- OR is better than either signal alone for total failure coverage.
- RND is the faster early signal; ACE contributes extra coverage and late uncertainty.
- Raw episode false alarms are high; K=3 debounce is a better deployment candidate than raw K=1.

## 6. Corrected Strict OOD Task Result

Experiment:

```text
experiments/fiper_ood_task_8_9_v2_loaderfix_20260526
```

Training:

```text
train/calib tasks: 0-7 only
OOD eval tasks: 8-9 only
epochs: 20
batch size: 256
device: cuda
loss: 0.000504615 -> 0.000117393
score rows written: 332,518 / 332,518 expected
```

Thresholds:

| Signal | q90 | q95 | q99 |
|---|---:|---:|---:|
| RND | 0.028686 | 0.036919 | 0.058993 |
| ACE entropy | -342.286048 | -341.281387 | -338.711003 |

Row-level q95 rates:

| Split | RND | ACE | OR | AND |
|---|---:|---:|---:|---:|
| success_test_seen | 5.26% | 5.17% | 8.22% | 2.21% |
| success_test_ood | 24.76% | 3.97% | 26.46% | 2.26% |
| failure_eval_seen | 25.36% | 31.25% | 37.18% | 19.42% |
| failure_eval_ood | 44.14% | 39.32% | 54.97% | 28.48% |
| failure_eval_ood_late | 50.29% | 57.29% | 67.83% | 39.75% |
| failure_eval_ood_near_end | 51.53% | 57.69% | 69.13% | 40.09% |

Strict OOD failure episodes only (`failure_eval_ood`, 64 episodes):

| Rule | Detection | Det @10% | Det @25% | Det @50% | Mean Norm Time |
|---|---:|---:|---:|---:|---:|
| OR q95 K=1 | 100.00% | 64.06% | 96.88% | 100.00% | 0.0774 |
| OR q95 K=2 | 100.00% | 48.44% | 95.31% | 100.00% | 0.1090 |
| OR q95 K=3 | 98.44% | 42.19% | 92.19% | 98.44% | 0.1202 |

OOD success false alarms are high:

| Split | K=1 Ep FA | K=2 Ep FA | K=3 Ep FA |
|---|---:|---:|---:|
| success_test_seen | 80.24% | 61.65% | 50.59% |
| success_test_ood | 85.82% | 74.43% | 68.23% |

Interpretation:

- Strict OOD task failure detection is real and strong.
- The OOD success false alarm burden is too high for hard-stop deployment.
- This result supports a warning monitor or risk score, not an autonomous stop policy.

## 7. Trustworthy Now

- Combined dataset row counts and split purity.
- Success-only RND train/calib split construction.
- Failure rows excluded from train/calib.
- ACE chunks are saved/evaluated only; manifest says `ace_replay_used=false`.
- Corrected `global_v2_loaderfix` full results.
- Corrected `ood_task_8_9_v2_loaderfix` strict OOD failure metrics.
- Local/Sam/Bob patched runner script hash match and compile.

## 8. Not Trustworthy / Superseded

- `experiments/fiper_receding_only_global_v1` as final evidence: superseded by loader-fixed v2.
- `FIPER_RECEDING_ONLY_GLOBAL_V1_DETAILED_AUDIT.md`: contains the old `3405` episode-counting bug.
- Original OOD task report episode counts: wrong for success split episodes.
- Auto-generated broad verdict fields from earlier runner versions: too optimistic and partly hardcoded.
- Any future result produced by an old copy of `run_receding_only_fiper_train_eval.py` with hash different from `0e32f4d...`.

## 9. Remaining Limitations

- ACE uses a regularized Gaussian logdet proxy with only 8 samples in a 70-dimensional action-chunk space. Treat it as a stable uncertainty score, not a rigorous full-rank entropy estimate.
- Global split is ID/random over all tasks and suites; it is not an OOD test.
- Only strict OOD task IDs 8/9 have been corrected and rerun fully.
- OOD perturbation holdouts and suite-family holdouts still need corrected full reruns.
- Bob has the patched script but has not replicated the full corrected experiments.
- Official LIBERO data is still not part of these corrected experiments.

## 10. Recommended Next Work

Do not use the old `global_v1` or OOD `v1` as final evidence. Use the loader-fixed v2 experiments as the current baseline.

Next recommended corrected experiments on Sam:

```bash
cd /home/rootalkhatib/test/reda_ws/fiper_ws
source ../asynchvla_ws/scripts/activate_simvla_sam.sh

# Example: perturbation holdout env
python3 scripts/run_receding_only_fiper_train_eval.py \
  --experiment-dir experiments/fiper_ood_perturbation_env_v1_loaderfix_20260526 \
  --refs-dir experiments/prepared_20260526/02_ood_perturbation_holdout_env/datasets/refs \
  --train-split success_train_seen \
  --calib-split success_calib_seen \
  --success-eval-splits success_test_seen success_test_ood \
  --failure-eval-splits failure_eval_seen failure_eval_ood failure_eval_ood_late failure_eval_ood_near_end \
  --device cuda \
  --epochs 20 \
  --batch-size 256 \
  --seed 42 \
  --report-name FIPER_OOD_PERTURBATION_ENV_V1_LOADERFIX_REPORT.md
```

Run the same pattern for holdout `mug`, `milk`, and `object`, then suite-family holdouts. After that, decide whether Bob replication or official LIBERO mixed training is justified.

## 11. Exact Commands Run

Representative commands executed during this verification:

```bash
ssh -o BatchMode=yes sam 'hostname; date; pgrep -af "run_receding_only_fiper_train_eval|collect_fiper|python.*fiper" || true; uptime; free -h; nvidia-smi ...'
ssh -o BatchMode=yes pcrobot 'hostname; date; pgrep -af "run_receding_only_fiper_train_eval|collect_fiper|python.*fiper" || true; uptime; free -h; nvidia-smi ...'
ssh -o BatchMode=yes sam 'cd /home/rootalkhatib/test/reda_ws/fiper_ws && python3 -m py_compile scripts/run_receding_only_fiper_train_eval.py scripts/prepare_fiper_experiment_splits.py scripts/materialize_fiper_split.py'
ssh -o BatchMode=yes sam 'cd /home/rootalkhatib/test/reda_ws/fiper_ws && wc -l experiments/fiper_receding_only_global_v1/scores/*.jsonl experiments/fiper_ood_task_8_9_v1_20260526/scores/*.jsonl'
scp -o BatchMode=yes sam:/home/rootalkhatib/test/reda_ws/fiper_ws/scripts/run_receding_only_fiper_train_eval.py /home/redafrix/tests/internship/fiper_ws/scripts/run_receding_only_fiper_train_eval.py
scp -o BatchMode=yes /home/redafrix/tests/internship/fiper_ws/scripts/run_receding_only_fiper_train_eval.py sam:/home/rootalkhatib/test/reda_ws/fiper_ws/scripts/run_receding_only_fiper_train_eval.py
scp -o BatchMode=yes /home/redafrix/tests/internship/fiper_ws/scripts/run_receding_only_fiper_train_eval.py 'pcrobot:/media/rootalkhatib/My\ Passport/reda_ws/fiper_ws/scripts/run_receding_only_fiper_train_eval.py'
python3 -m py_compile fiper_ws/scripts/run_receding_only_fiper_train_eval.py
```

Smoke and full run commands:

```bash
python3 scripts/run_receding_only_fiper_train_eval.py \
  --experiment-dir experiments/codex_verify_global_loaderfix_smoke_20260526 \
  --device cpu --epochs 1 --batch-size 64 --seed 7 \
  --max-train-rows 512 --max-calib-rows 256 --max-eval-rows 256

python3 scripts/run_receding_only_fiper_train_eval.py \
  --experiment-dir experiments/codex_verify_ood_task_loaderfix_smoke_20260526 \
  --refs-dir experiments/prepared_20260526/01_ood_task_8_9/datasets/refs \
  --train-split success_train_seen --calib-split success_calib_seen \
  --success-eval-splits success_test_seen success_test_ood \
  --failure-eval-splits failure_eval_seen failure_eval_ood failure_eval_ood_late failure_eval_ood_near_end \
  --device cpu --epochs 1 --batch-size 64 --seed 7 \
  --max-train-rows 512 --max-calib-rows 256 --max-eval-rows 256

python3 scripts/run_receding_only_fiper_train_eval.py \
  --experiment-dir experiments/fiper_receding_only_global_v2_loaderfix_20260526 \
  --device cuda --epochs 20 --batch-size 256 --seed 42

python3 scripts/run_receding_only_fiper_train_eval.py \
  --experiment-dir experiments/fiper_ood_task_8_9_v2_loaderfix_20260526 \
  --refs-dir experiments/prepared_20260526/01_ood_task_8_9/datasets/refs \
  --train-split success_train_seen --calib-split success_calib_seen \
  --success-eval-splits success_test_seen success_test_ood \
  --failure-eval-splits failure_eval_seen failure_eval_ood failure_eval_ood_late failure_eval_ood_near_end \
  --device cuda --epochs 20 --batch-size 256 --seed 42
```

## 12. Final Decision

```text
PIPELINE_BUG_FOUND = YES
PIPELINE_BUG_FIXED = YES
OLD_V1_RESULTS_FINAL_TRUSTWORTHY = NO
CORRECTED_GLOBAL_V2_SUPPORTS_FIPER_IDEA = YES
CORRECTED_OOD_TASK_V2_SUPPORTS_FAILURE_DETECTION = YES
READY_FOR_HARD_STOP_DEPLOYMENT = NO
READY_FOR_NEXT_OOD_PERTURBATION_TESTS = YES
```
