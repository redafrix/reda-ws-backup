# Stage 9 Full Training Report

Generated: `2026-05-19T10:25:00+02:00`

## Executive Summary

- Dataset validation status before training: `DATASET_READY_FOR_TRAINING = YES`.
- Frozen dataset: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/frozen/stage9_stop_validate_20260519_093940`
- Training split directory used for jobs: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/frozen/stage9_stop_validate_20260519_093940/splits_group_safe`
- Active campaign id: `stage9_full_training_20260519_1035`
- Active Bob campaign path: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/training/stage9_full_training_20260519_1035`
- Active Sam campaign path: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/training/stage9_full_training_20260519_1035`
- Training launched on both machines. Bob is running in tmux. Sam is running detached with nohup.
- Current best model/calibration sections are `PENDING`: queues are still running and will write metrics, calibration outputs, ensemble outputs, and long-top jobs automatically.

## Code Implemented

Created `asynchvla_ws/src/training_stage9/` on Bob and Sam:

- `stage9_dataset.py`: JSONL split loader, feature extraction, metadata-safe model inputs, group-safe split builder.
- `stage9_models.py`: MLP, residual/gated MLP, GRU/LSTM, small/medium/large Transformer, action chunk Transformer, cross-attention Transformer, TCN, Mamba.
- `stage9_losses.py`: binary, soft-label, ordinal, and subtype multitask losses.
- `stage9_eval.py`: AUROC, AUPRC, Brier, ECE, NLL, accepted-risk tables, subtype metrics, eval report writer.
- `stage9_calibration.py`: temperature scaling, Platt/logistic calibration, isotonic, beta calibration, conformal-style thresholds, ensemble_top3 creation.
- `train_stage9_risk_model.py`: trains one model/target job and writes `config.json`, `checkpoint.pt`, `metrics.json`, `predictions.jsonl`, `eval_report.md`.
- `launch_stage9_training_jobs.py`: creates group-safe splits, writes per-machine queue scripts, launches detached jobs, retries each job once, runs calibration and long-top follow-up.

Model inputs intentionally exclude `task_id`, `suite_id`, `task_name`, `suite`, `perturbation_type`, `seed`, `state_id`, and `sample_id`. Those fields are retained only in split metadata and prediction/eval reports.

## Bob/Sam Setup Status

| item | Bob | Sam |
|---|---|---|
| Workspace | `/media/rootalkhatib/My Passport/reda_ws` | `/home/rootalkhatib/test/reda_ws` |
| CUDA/Torch | `torch 2.5.1+cu121`, RTX 4070 Ti SUPER visible | `torch 2.5.1+cu121`, RTX 4070 Ti SUPER visible |
| Code synced | YES | YES |
| Dataset JSONL synced | native Bob dataset | 147 chunk JSONLs synced under `data/final_20h/synced_from_bob`, symlinked as `bob_20260518_193710` |
| Frozen splits synced | YES | YES |
| Python compile | PASS | PASS |
| 100-sample smoke | PASS: `bob_smoke_action_only` | PASS: `sam_smoke_context_action` |
| Mamba smoke | PASS: `bob_smoke_mamba` | PASS: `sam_smoke_mamba` |

## Dependency Status

- `sklearn` available on both machines.
- `mamba-ssm` and `causal-conv1d` were missing initially on both machines.
- First normal pip install failed:
  - Bob: build tried to compile `causal-conv1d` without `nvcc`.
  - Sam: isolated build could not see torch, then wheel fetch hit SSL verification.
- Clean resolution:
  - Installed exact prebuilt wheels directly with trusted GitHub hosts:
    - `causal_conv1d-1.5.0.post8+cu12torch2.5cxx11abiFALSE-cp310-cp310-linux_x86_64.whl`
    - `mamba_ssm-2.2.5+cu12torch2.5cxx11abiFALSE-cp310-cp310-linux_x86_64.whl`
  - The fused fast path expected `causal_conv1d.cpp_functions`, which is not exposed by this wheel. The Mamba model was therefore set to `use_fast_path=False`. This still uses `mamba_ssm` and passed real train smoke on both machines.
- Bob requires `$HOME/.local/lib/python3.10/site-packages` in `PYTHONPATH`; launcher exports it automatically.

## Split Audit

The original validated split directory was not used directly for training because `test_unseen_seed` held out candidate-generation seed values, which would leak same-state groups across train/test. A new group-safe split directory was created:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/frozen/stage9_stop_validate_20260519_093940/splits_group_safe`

Audit result:

- Samples: `37,632`
- Same-state groups: `1,426`
- Same-state group leakage: `0`
- Note: `test_unseen_seed` is group-safe and uses the parent rollout index parsed from `state_id`, because candidate-generation seeds coexist inside each same-state group.

| split | samples | groups | GOOD_STRONG | VALIDATED_BAD | GOOD_WEAK | AMBIGUOUS |
|---|---:|---:|---:|---:|---:|---:|
| train | 12,832 | 454 | 5,127 | 2,535 | 1,626 | 3,544 |
| calib | 2,280 | 82 | 1,115 | 460 | 123 | 582 |
| test_seen_task | 1,592 | 54 | 686 | 338 | 138 | 430 |
| test_unseen_task | 5,120 | 193 | 1,707 | 1,070 | 1,034 | 1,309 |
| test_unseen_seed | 5,568 | 196 | 2,649 | 990 | 631 | 1,298 |
| test_unseen_perturbation | 10,240 | 447 | 6,646 | 1,521 | 211 | 1,862 |

Training uses balanced binary sampling where applicable, but evaluation keeps the original group-safe split distributions.

## Target Modes

All launched jobs cover:

1. `clean_binary`: `GOOD_STRONG=0`, `VALIDATED_BAD=1`, ignore `GOOD_WEAK/AMBIGUOUS`.
2. `soft_labels`: `GOOD_STRONG=0.0 w=1.0`, `GOOD_WEAK=0.25 w=0.3`, `AMBIGUOUS=0.5 w=0.1`, `VALIDATED_BAD=1.0 w=1.0`.
3. `soft_no_ambiguous`: same as soft labels but ignore `AMBIGUOUS`.
4. `ordinal`: `GOOD_STRONG=0`, `GOOD_WEAK=1`, `AMBIGUOUS=2`, `VALIDATED_BAD=3`.
5. `subtype_multitask`: main safe/risky head plus auxiliary `action_specific/state_context` subtype head for bad samples.

## Model Families Launched

Bob heavy queue models:

- `small_history_transformer_k8`
- `medium_history_transformer_k8`
- `large_history_transformer_k8`
- `action_chunk_transformer`
- `history_action_cross_attention_transformer`
- `Mamba_history_k8`
- `Mamba_medium_history_k8`

Sam lightweight queue models:

- `action_only_mlp`
- `context_action_mlp`
- `history_gru_k8`
- `history_lstm_k8`
- `TCN_history_k8`
- `residual_mlp_large`
- `gated_context_action_mlp`

Each machine launches 35 quick jobs: 7 model families x 5 target modes. Each quick job uses 8 epochs and up to 16k training rows. After quick jobs, each queue runs calibration and `run_long_top`, which trains the top local models for longer and enables MC dropout on the rank-1 long job. `ensemble_top3` is built during calibration from the top completed prediction files.

## Launch Status

Bob:

- Launch method: `tmux`
- Session: `stage9_train_bob_9_1035`
- Job manifest: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/training/stage9_full_training_20260519_1035/bob/job_manifest.json`
- Queue script: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/scripts/training/stage9_train_queue_bob_stage9_full_training_20260519_1035.sh`
- Jobs launched: `35`
- Last checked status: active, running `clean_binary / medium_history_transformer_k8`.
- Completed quick metrics at last check: `1`.

Sam:

- Launch method: `nohup`
- PID: `1009683`
- Nohup log: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/scripts/training/stage9_train_queue_sam_stage9_full_training_20260519_1035.nohup.log`
- Job manifest: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/training/stage9_full_training_20260519_1035/sam/job_manifest.json`
- Queue script: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/scripts/training/stage9_train_queue_sam_stage9_full_training_20260519_1035.sh`
- Jobs launched: `35`
- Last checked status: active, running `clean_binary / action_only_mlp`.
- Completed quick metrics at last check: `0` for the clean relaunched queue.

A deprecated first campaign attempt `stage9_full_training_20260519_1028` was discarded because the launcher did not create per-campaign log directories before starting queue jobs. That launcher bug was fixed before launching the active `stage9_full_training_20260519_1035` campaign.

## Calibration Plan

For every completed model prediction set, `stage9_calibration.py` runs:

- raw probabilities
- temperature scaling
- Platt/logistic calibration
- isotonic regression
- beta calibration
- conformal-style thresholds at accept 90/75/50/25%
- accepted/rejected risk tables
- `ensemble_top3` mean/std predictions and calibration

Metrics written include AUROC BAD, AUPRC BAD, Brier, ECE, NLL, precision/recall BAD, accepted BAD leakage, rejected BAD enrichment, GOOD_STRONG kept rate, and transfer across seen/unseen task, seed, and perturbation splits.

## Current Early Metrics

These are not final. They only prove the pipeline is training and producing metrics.

- Bob first completed quick job: `clean_binary / small_history_transformer_k8`
  - calib AUROC reached about `0.86` during quick training.
- Sam first active quick job: `clean_binary / action_only_mlp`
  - calib AUROC reached about `0.78` during quick training before final evaluation writing.

Final best model per split, best calibrated model, accepted/rejected risk tables, subtype performance, checkpoint recommendation, and threshold recommendation are pending until queues finish.

## Pending Final Outputs

Each job output directory will contain:

- `config.json`
- `checkpoint.pt`
- `metrics.json`
- `predictions.jsonl`
- `eval_report.md`
- `calibration/` after calibration runs

Campaign-level summaries expected after queues finish:

- Bob: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/training/stage9_full_training_20260519_1035/bob/calibration_campaign_summary.json`
- Sam: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/training/stage9_full_training_20260519_1035/sam/calibration_campaign_summary.json`
- Long-top summaries under each machine campaign directory.

## Best Model And Recommendation

Status: `PENDING_RUNNING_JOBS`.

Do not select a final checkpoint or safe threshold until both queues finish calibration. The report should be updated from the completed `metrics.json` and `calibration_metrics.json` files.

Recommended selection rule after completion:

1. Prefer low accepted BAD leakage at accept 90% on `calib` and `test_seen_task`.
2. Require threshold transfer to `test_unseen_task`, `test_unseen_seed`, and `test_unseen_perturbation` without large leakage increase.
3. Tie-break by AUPRC BAD, then Brier/ECE.
4. Report separately for `action_specific` and `state_context` subtypes.

## Inference Command Template

Replace `<BEST_JOB_DIR>` after calibration finishes:

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
export PYTHONPATH="$HOME/.local/lib/python3.10/site-packages:$PWD/asynchvla_ws/src:$PYTHONPATH"
python3 -m training_stage9.train_stage9_risk_model \
  --split-dir "asynchvla_ws/stage9_libero_pro_risk_data/data/frozen/stage9_stop_validate_20260519_093940/splits_group_safe" \
  --output-dir "<NEW_EVAL_OUTPUT_DIR>" \
  --model "<BEST_MODEL_NAME>" \
  --target-mode "<BEST_TARGET_MODE>" \
  --epochs 0
```

A dedicated single-sample inference wrapper is still needed after the best checkpoint is selected; current scripts are train/eval campaign scripts.

## Exact Monitoring Commands

Bob:

```bash
ssh pcrobot 'tmux ls; tail -f "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/training/stage9_full_training_20260519_1035/bob/logs/bob_quick_clean_binary_medium_history_transformer_k8.log"'
```

Sam:

```bash
ssh sam 'ps -p 1009683 -o pid,etime,cmd; tail -f "/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/scripts/training/stage9_train_queue_sam_stage9_full_training_20260519_1035.nohup.log"'
```

## Final State

- Full training campaign launched: `YES`
- Both PCs used: `YES`
- Mamba dependency installed and smoke-tested: `YES`, using Mamba non-fused path due available wheel API.
- Metadata-safe model inputs enforced: `YES`
- Group-safe splits used: `YES`
- Best final model selected: `NO, pending campaign completion`
- Serious training currently running: `YES`
