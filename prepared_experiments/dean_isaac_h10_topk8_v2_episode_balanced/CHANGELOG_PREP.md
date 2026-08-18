# Preparation changelog

- Initial V2 concept: inverse episode-duration weighting plus episode-level class balancing.
- Final minibatch implementation pinned in `WEIGHTING_NOTE.md`: use mean-one row multipliers `N_train_rows * w_raw` and ordinary batch mean. This supersedes any earlier wording that suggested normalizing by the sum of sampled weights inside each batch.
- Threshold policy pinned in `THRESHOLD_POLICY.md`: preserve legacy query-weighted thresholds for comparison and add episode-balanced primary thresholds derived from Seen validation only.
