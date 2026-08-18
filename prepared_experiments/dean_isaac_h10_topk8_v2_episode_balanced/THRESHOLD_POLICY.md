# V2 Threshold Policy

Thresholds must be derived from the selected V2 checkpoint using Seen validation only.

Preserve two families for transparent comparison:

1. `query_weighted_*`: exact legacy V1 definitions on validation rows, including unweighted best-F1 and ordinary success-row q90/q95/q99. These exist only to compare V2 scores with V1 under the old convention.
2. `episode_balanced_*`: definitions using validation row sample weight `1/T_i`, so each episode has equal total influence.

For episode-balanced best-F1, use `precision_recall_curve(..., sample_weight=1/T_i)` and choose the threshold maximizing weighted F1.

For episode-balanced success q90/q95/q99, compute weighted quantiles over success rows with row weight `1/T_i`; do not use ordinary `np.quantile` for these fields.

Always include fixed 0.5 as a reference.

The primary V2 threshold family for the corrected objective is `episode_balanced_*`.

Do not reuse V1 threshold 0.7990124225616455 as a V2 threshold. Do not use OOD150 or OOD400 to choose any V2 threshold.