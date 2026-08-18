# Required V2 Outputs

The V2 run must produce machine-readable artifacts without overwriting V1.

Required output directory on Dean:

`/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/models/isaac_h10_topk8_temporal_v2_episode_balanced/`

Required files:

- `TRAINING_CONFIG.json`
- `WEIGHTING_AUDIT.json`
- `TRAINING_HISTORY.json`
- `results.json`
- `thresholds.json`
- `model_manifest.json`
- `V1_V2_SEEN_COMPARISON.json`
- `V1_V2_OOD150_COMPARISON.json` only after Seen selection/thresholds are frozen
- model checkpoint may exist locally on Dean but must not overwrite V1

`WEIGHTING_AUDIT.json` must include at minimum:

- train episode count / failure episode count / success episode count
- train row count / failure row count / success row count
- min/mean/max query rows per success episode
- min/mean/max query rows per failure episode
- sum of row weights over success rows
- sum of row weights over failure rows
- per-episode total weight min/mean/max separately for each class
- assertion that all success episodes have equal total weight within numerical tolerance
- assertion that all failure episodes have equal total weight within numerical tolerance
- assertion that total success loss mass equals total failure loss mass within numerical tolerance

`V1_V2_SEEN_COMPARISON.json` must contain side-by-side V1 and V2 on identical Seen validation/test rows:

- unweighted query AUPRC
- unweighted query AUROC
- episode-balanced AUPRC (`sample_weight=1/T_i`)
- episode-balanced AUROC (`sample_weight=1/T_i`)
- threshold(s) derived from Seen validation for each model
- query-level confusion metrics at the selected threshold
- episode-level detector metrics already used by the existing evaluator when applicable

V2 checkpoint selection must use Seen-validation episode-balanced AUPRC only.

OOD150 may be evaluated only after the selected V2 checkpoint and Seen-derived threshold file are frozen. OOD400 is forbidden in this experiment.
