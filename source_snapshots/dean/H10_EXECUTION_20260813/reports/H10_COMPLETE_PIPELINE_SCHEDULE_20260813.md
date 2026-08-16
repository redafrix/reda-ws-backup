# Complete H10 Pipeline Schedule

This schedule replaces every H1-derived dataset, risk-head model, calibration,
evaluation and hard-enrichment result. No historical H1 row is an input.

## Serialized Stages

1. Collect the original 4,000 official seen scenes with true `chunk_h10`
   execution into `outputs/final_seen_h10_round_000_seed20260730`.
2. Exhaustively audit every committed H10 row and losslessly compress the
   authoritative row streams.
3. Freeze the H10 Round-0 scientific dataset using scene-family-disjoint
   70/15/15 train/calibration/test splits and training-only normalization.
4. Train a new Isaac H10 TopK8 temporal risk-head checkpoint at
   `models/isaac_h10_topk8_temporal_v1`.
   It uses the promoted LIBERO architecture and optimization recipe but starts
   with new Isaac-trained weights; LIBERO risk-head weights are not reused.
5. Prepare and collect a fresh locked OOD-150 evaluation using H10 execution,
   exhaustively audit it, and evaluate the first H10 risk model.
6. Generate 4,000 new official seen candidate scenes without collecting them.
   Exclude Round-0 and locked OOD-150 fingerprints and OOD asset variants.
7. Select and collect exactly 1,000 H10 hard-enrichment scenes into
   `outputs/final_seen_h10_round_002_seed20260804`.
8. Exhaustively audit and losslessly compress the H10 hard-1000.
9. Freeze the combined 5,000-episode H10 dataset at
   `frozen_datasets/isaac_seen_h10_topk8_v2_round0_hard1000`.
10. Train a new combined H10 model at
    `models/isaac_h10_topk8_temporal_v2_round0_hard1000`.
11. Evaluate that combined model against the same locked H10 OOD-150 set and
    generate the final dataset, training and evaluation reports.

Every GPU stage is serial. A collector, risk trainer and pi0.5 trainer cannot
run concurrently through these launchers.

## Persistence

- Primary service: `simvla-isaac-risk-h10-pipeline.service`
- First-cycle handoff path: `simvla-h10-hard1000-handoff.path`
- Hard-1000 watchdog timer: `simvla-h10-hard1000-watchdog.timer`
- Round-0 tmux: `simvla-risk-h10-final-seen-r000`
- Later hard-1000 tmux: `simvla-h10-hard1000-pipeline`

The path unit activates when
`automation/FIRST_RISK_TRAIN_AND_LOCKED_EVAL_COMPLETE` is atomically created.
It prevents the initial supervisor from entering open-ended broad collection
and hands the GPU to the hard-1000 pipeline. The watchdog checks every five
minutes and resumes only incomplete atomic stages.

## Current Status at Installation

```text
ROUND0_H10_COLLECTION=RUNNING
ROUND0_COMMITTED_EPISODES=27
FIRST_H10_MODEL_TRAINING=WAITING_FOR_ROUND0_AUDIT
FIRST_H10_OOD150_EVALUATION=WAITING
H10_HARD1000_COLLECTION=WAITING
COMBINED_H10_5000_TRAINING=WAITING
COMBINED_H10_OOD150_EVALUATION=WAITING
```

Regression tests after installing the complete chain: `37 passed, 2 skipped`.
The skipped tests require the future generated hard-round manifest and become
applicable only after H10 Round 0 completes.

## Required Contracts

```text
ROUND0_EXECUTION_MODE=chunk_h10
HARD1000_EXECUTION_MODE=chunk_h10
OOD150_EXECUTION_MODE=chunk_h10
MAIN_CHUNK_SHAPE=[10,7]
ALTERNATIVE_CHUNKS_SHAPE=[8,10,7]
NORMAL_ACTIONS_PER_REPLAN=10
MAX_SIM_STEPS=2400
MAX_CONTROL_TICKS=600
MAX_DECISION_ROWS=60
H1_DATA_REUSED=NO
GPU_STAGES_SERIAL=YES
AUTOMATIC_4000_TRAIN_EVAL_1000_COMBINED_TRAIN_EVAL=YES
```
