# Result Interpretation Rules

This experiment is a one-variable methodological ablation.

Primary question: does episode-balanced/class-balanced training improve the same H10 TopK8 temporal risk architecture relative to V1?

Do not call V2 better merely because its training loss is smaller or because its score calibration differs.

Compare V1 and V2 primarily on:

- Seen validation episode-balanced AUPRC/AUROC
- Seen test episode-balanced AUPRC/AUROC
- ordinary query-level AUPRC/AUROC (to ensure no hidden regression)
- existing episode detector metrics on Seen/OOD150 where the evaluator supports them

Report absolute differences V2 minus V1.

A favorable result requires improvement or useful tradeoff on Seen-held-out metrics without relying on OOD150 tuning. OOD150 is secondary development evidence.

Do not change architecture/hyperparameters in response to OOD150 during this experiment. If another training variant is desired, create V3 rather than mutating V2.

OOD400 stays sealed for later confirmation.
