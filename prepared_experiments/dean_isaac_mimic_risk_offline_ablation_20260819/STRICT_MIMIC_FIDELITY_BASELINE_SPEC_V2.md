# STRICT MIMIC FIDELITY BASELINE SPEC V2

## Purpose

This is a fidelity correction, not a performance-tuning variant.

The previous `isaac_mimic_h10_c0dyn_v1` experiment remains frozen as a proxy-enhanced Isaac adaptation. It MUST NOT be deleted or retroactively changed.

For the strict ablation baseline, the goal is to reproduce the portable H10 Mimic handoff as closely as the retained Round0 evidence permits, while refusing to invent information for source features that cannot be reconstructed.

No choice in this specification may depend on seen-test or OOD150 performance.

## Source contract

Authoritative explicit implementation contract:
`MIMIC_H10_HANDOFF_CONTRACT.md`

The handoff requires:
- 8 stochastic candidates;
- 9 final-candidate disagreement scalars;
- 5 cross-candidate denoising-dynamics traces x 5 summaries = 25 scalars;
- 3 query-to-query temporal-change scalars;
- H10 tensor [10,6];
- 37D scalar encoder, 128D static branch;
- H10 Transformer 2 layers / 4 heads / width 128;
- query encoder 256->128->64;
- 1-layer GRU 64->128;
- eventual episode-failure target;
- handoff training hyperparameters;
- successful-episode-max calibration.

## Critical retained-evidence fact

Round0 retains genuine final chunks for 9 candidates, but internal denoising trajectories only for candidate0.

Therefore the exact handoff quantities:
- `sample_pairwise_mse_mean`
- `sample_variance_max`
- `sample_variance_mean`
- `sample_velocity_mse_mean`
- `vector_field_l2_mean`

cannot be reproduced as 8-candidate denoising traces.

Alternative candidate X_d/V_d SHALL NOT be fabricated, inferred from final chunks, linearly interpolated, or replaced by candidate0 values.

## Strict missing-feature decision

For the strict baseline, the unavailable 25 cross-candidate denoising summary channels are DISABLED, not replaced by bespoke proxy features.

The scalar input remains 37D to preserve the handoff architecture exactly:
- dims 0..8: exact 9 candidate-disagreement scalars;
- dims 9..33: constant zero, representing unavailable handoff denoising channels;
- dims 34..36: exact 3 temporal-change scalars.

The zero channels are structural missing-input channels, not estimated values and not claimed as Mimic dynamics.

Normalization:
- exact available scalar channels are normalized from TRAIN only;
- disabled channels use mean=0, std=1 and remain exactly zero after normalization;
- horizon [10,6] uses the same TRAIN-only per-channel normalization as V1.

This is closer to the source contract than substituting new candidate0 proxy semantics, because it preserves the source architecture while adding no non-source information.

## Everything else stays frozen

Dataset source: same Round0 4000 episodes only.
Split: exact same 2800/600/600 episode split.
Candidate subset: main + alternatives 1..7, exactly 8 candidates, fixed stored order.
Final-candidate feature space: ENV 7D -> source-backed Mimic 10D conversion.
Nine disagreement formulas: unchanged from `FINAL_ADAPTATION_SPEC_V1.md`.
Horizon [10,6] formulas: unchanged.
Temporal 3 formulas: unchanged.

Temporal query window: 8 query records ending at current query; left-zero-padded after standardization. This is retained from the paper-level K1 temporal depth because the portable handoff transcription does not specify a fixed window length.

Architecture: exactly the portable handoff architecture already implemented:
- scalar Linear(37,128), LayerNorm, GELU, dropout .1;
- H10 Linear(6,128) + learned positions + 2-layer 4-head Transformer FFN512 dropout .1 + mean pool;
- concat 256 -> 128 -> 64;
- 1-layer GRU input64 hidden128;
- Linear128->1.

Training:
- batch 64;
- 25 epochs;
- AdamW lr 1e-3;
- weight decay 1e-4;
- grad clip 1.0;
- dropout .1;
- seeds 0..4;
- weighted BCE with pos_weight from TRAIN rows only;
- every train query once/epoch;
- per-seed checkpoint selection = highest validation row AUPRC, earliest tie;
- seed0 permanently primary.

Calibration:
- validation only;
- alpha .05/.10/.15 successful-episode-max corrected order statistic;
- alpha .10 primary;
- supplementary fixed .5, row best-F1, q90/q95/q99.

## Evaluation order

1. Build strict V2 dataset without touching V1.
2. Prove exact available-channel parity against V1:
   - dims 0..8 identical;
   - dims 34..36 identical;
   - horizon identical;
   - dims 9..33 exactly zero.
3. Train seeds 0..4.
4. Freeze validation selections and thresholds.
5. Score the same seen held-out 600 once.
6. Only after seen freeze, optionally score historical OOD150 unchanged.

No model/threshold/seed may be selected based on seen-test or OOD performance.

## Naming

Strict baseline experiment:
`isaac_mimic_h10_strict_missingdyn_v2`

V1 name remains:
`isaac_mimic_h10_c0dyn_v1`

Interpretation:
- V2 = primary strict source-fidelity Mimic ablation under retained-data limitations.
- V1 = secondary proxy-enhanced adaptation showing what happens when exact candidate0 dynamics are engineered into the unavailable handoff channels.

Never call V2 an exact reproduction of the original friend monitor because the 25 cross-candidate denoising channels are unavailable.
