# V2 Implementation Contract

Create a NEW trainer from the exact promoted V1 trainer; do not edit or overwrite the V1 trainer or V1 outputs.

## Required dataset fields

Load the existing frozen train/validation/test arrays, including `episode_index.npy` and `label.npy`.

For each split, compute each episode's row count `T_i` from `episode_index.npy`. Verify all rows of a given episode carry one identical episode-level label. Abort on mixed labels within an episode.

## Training row weights

For the training split only:

- `N_success_episodes = 2736`
- `N_failure_episodes = 64`
- for a success row from episode i: `w = 0.5 / (2736 * T_i)`
- for a failure row from episode i: `w = 0.5 / (64 * T_i)`

Do not use `BCEWithLogitsLoss(pos_weight=...)` in V2.

Compute raw per-row BCE with logits using `reduction="none"`, then use:

`loss = sum(query_bce * batch_row_weight) / sum(batch_row_weight)`

for each shuffled minibatch.

The relative weights are the scientific contract; minibatch renormalization is allowed only by division by the sum of the sampled row weights in that minibatch.

## Weight audit before training

Before the first optimizer step, mechanically verify:

- sum of all success row weights across the train split = 0.5 within 1e-10
- sum of all failure row weights across the train split = 0.5 within 1e-10
- for every success episode, sum of its row weights = `0.5/2736` within tolerance
- for every failure episode, sum of its row weights = `0.5/64` within tolerance

Write `WEIGHTING_AUDIT.json` before training.

## Architecture and optimizer

Copy V1 exactly:

- SeqRiskModel
- static_dim 51
- history 16x21
- action 10x7
- width 128
- layers 3
- heads 4
- FFN 512
- dropout 0.1
- AdamW
- lr 2e-4
- weight_decay 1e-4
- batch_size 512
- epochs 10
- gradient_clip_norm 1.0
- training_seed 20260622

## Validation metrics

At every epoch calculate on the exact Seen validation rows:

1. `query_auprc`: ordinary unweighted row AUPRC
2. `query_auroc`: ordinary unweighted row AUROC
3. `episode_balanced_auprc`: row AUPRC with `sample_weight = 1/T_i`
4. `episode_balanced_auroc`: row AUROC with `sample_weight = 1/T_i`

Each episode must therefore contribute total metric weight 1 regardless of row count.

Select and save the best checkpoint using ONLY highest `episode_balanced_auprc`.

Do not use OOD150 or OOD400 for epoch/checkpoint selection.

## Thresholds

After selecting the V2 checkpoint, derive threshold candidates from Seen validation only. At minimum preserve the same V1 threshold families where applicable (`best_val_f1`, fixed 0.5, q90, q95, q99), but calculate them from V2 scores. Record both unweighted-query and episode-balanced variants if their definitions differ. Do not reuse V1 `0.7990124225616455` as V2's threshold.

## Seen comparison

Evaluate V1 and selected V2 on the identical frozen Seen validation and test splits. Record both ordinary query metrics and episode-balanced metrics for both models.

## OOD150 comparison

Only after the V2 checkpoint SHA and Seen-derived thresholds are frozen, evaluate V2 on the existing locked true-H10 OOD150 rows. This is comparison/development evidence only. Do not tune V2 architecture, weights, epoch, or thresholds on OOD150 in this task.

## OOD400

Forbidden. Do not launch, score, inspect outcomes, or tune against OOD400.
