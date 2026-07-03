# Phase 2 TDQC for SimVLA

This folder trains a separate TDQC calibrator on top of the already-trained Phase-1 SimVLA uncertainty head.

The Phase-1 VLA stays frozen. Phase 2 only trains a small RNN that maps uncertainty traces to final failure probability.

## 1. Collect uncertainty rollouts

Your current LIBERO client already supports:

```bash
--uncertainty_log path/to/rollouts.jsonl
```

Each JSONL row must contain:

```json
{
  "success": true,
  "uncertainty_trace": [
    {
      "path_step_mean": 0.01,
      "last_step_mean": 0.2,
      "path_variance": [0.01, 0.02, 0.01, 0.0, 0.01, 0.02, 0.01],
      "last_step_variance": [0.2, 0.3, 0.1, 0.2, 0.2, 0.1, 0.3],
      "mean_path_var": 0.01,
      "mean_last_var": 0.2,
      "max_path_var": 0.03,
      "max_last_var": 0.7
    }
  ]
}
```

## 2. Convert JSONL to TDQC dataset

```bash
python -m phase2_tdqc.convert_uncertainty_jsonl_to_tdqc \
  --input_jsonl evaluation/libero/eval_libero_pro/libero_10_object_alltasks.jsonl \
  --output_path runs/tdqc_datasets/libero_10_object_alltasks_tdqc.pt
```

To train from raw per-action uncertainty vectors instead of only scalar
summaries, collect new rollouts with the updated client and convert with:

```bash
python -m phase2_tdqc.convert_uncertainty_jsonl_to_tdqc \
  --input_jsonl evaluation/libero/eval_libero_pro/your_raw_rollouts.jsonl \
  --output_path runs/tdqc_datasets/your_raw_tdqc.pt \
  --feature_mode raw_plus_summary \
  --raw_action_dim 7
```

`raw_plus_summary` uses the six original scalar summaries plus the raw
`path_variance[7]` and `last_step_variance[7]` vectors for the executed action.
Use `--feature_mode raw` if you want only the 14 raw variance dimensions.

## 3. Train calibrator

```bash
python -m phase2_tdqc.train_tdqc_calibrator \
  --dataset_path runs/tdqc_datasets/libero_10_object_alltasks_tdqc.pt \
  --output_dir runs/tdqc_calibrator/libero_10_object_alltasks \
  --epochs 100 \
  --batch_size 32 \
  --lr 1e-4 \
  --hidden_dim 64 \
  --target_update_freq 25
```

The checkpoint is saved as:

```text
runs/tdqc_calibrator/libero_10_object_alltasks/tdqc_calibrator_best.pt
```

## 4. What is being optimized

For non-terminal steps:

```text
q_t -> stopgrad(q_target_{t+1})
```

For the final valid step:

```text
q_T -> Y_fail
```

where `Y_fail = 1` for failed rollouts and `0` for successful rollouts.

So the trained output is directly interpretable as:

```text
P(final rollout failure | uncertainty history up to this step)
```
