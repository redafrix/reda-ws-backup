# Portable H10 Mimic risk-monitor contract — source transcription

This file records the exact H10 portability contract previously extracted from the user-provided `simvla_h10_risk_monitor_handoff (1).zip`. It is NOT the same artifact as the paper-level original W2A K1 description.

Use this file as the fallback implementation source if the original executable friend/W2A risk-head source cannot be recovered on Dean. If original executable source is recovered, compare it mechanically against this contract and let ChatGPT decide which source controls each component.

## Primary monitor

**Single-Head GRU — Combined without ACE**

Target semantics:

`P(eventual episode failure | query history)`

This single-head target is preferred for cross-policy H10 adaptation because its target meaning does not depend on proposal length.

## Fixed H10/K1 generation contract

- proposal horizon: 10
- commitment horizon used by local-label variants: 10
- monitor action representation in the handoff: 10D `[translation3, rotation6d6, gripper1]`
- stochastic action candidates: exactly 8
- ACE: excluded
- V2W features: excluded in K1
- successive-plan overlap features: excluded from the corrected portable H10 K1 contract

## Current-query scalar features — 37 total

### A. Nine candidate-disagreement scalars

1. `w2a_action_variance_mean`
2. `w2a_action_variance_max`
3. `w2a_pairwise_mse_mean`
4. `w2a_first_candidate_vs_mean_mse`
5. `w2a_endpoint_position_spread_mean_m`
6. `w2a_endpoint_position_spread_max_m`
7. `w2a_position_variance_mean`
8. `w2a_rotation_variance_mean`
9. `w2a_gripper_variance_mean`

### B. Five denoising-dynamics traces

At every denoising/generation iteration:

1. `sample_pairwise_mse_mean`
2. `sample_variance_max`
3. `sample_variance_mean`
4. `sample_velocity_mse_mean`
5. `vector_field_l2_mean`

For EACH trace reduce using, in this order:

- first
- last
- mean
- max
- last-minus-first

This yields 25 scalars.

### C. Three temporal-change scalars

1. `history_available`
2. absolute change from previous query in W2A/action variance
3. absolute change from previous query in endpoint spread

At the first query, `history_available=0` and both changes are zero.

Total scalar input per query: `9 + 25 + 3 = 37`.

## H10 horizon tensor — shape [10,6]

For each of the 10 proposal indices:

1. position variance mean
2. position variance max
3. rotation variance mean
4. gripper variance
5. cumulative position spread mean
6. cumulative position spread max

## Single-Head model architecture

- scalar encoder: Linear to hidden width 128, followed by LayerNorm, GELU and dropout 0.1
- horizon projection: each 6D H10 horizon token projected to width 128
- learned H10 positional embedding
- horizon Transformer: 2 layers, 4 attention heads, feed-forward width `4 * 128`, dropout 0.1
- horizon sequence summary: mean pool over the 10 horizon outputs
- concatenate scalar embedding and pooled horizon embedding: 256D
- query encoder: `256 -> 128 -> 64`
- temporal encoder over query records: GRU, 1 layer, input width 64, hidden width 128
- output: binary eventual-failure logit from GRU state

## Training constants from handoff

- batch size: 64
- epochs: 25
- optimizer: AdamW
- learning rate: 1e-3
- weight decay: 1e-4
- gradient clip: 1.0
- dropout: 0.1
- seeds: 0,1,2,3,4
- positive class weighting: from training data
- all feature normalization fitted on training only

## Handoff calibration

Native handoff operating levels include alpha 0.05, 0.10 and 0.15. Calibration is based on successful-episode maximum risk scores.

For the Isaac experiment, no test or OOD score may influence feature construction, model selection or threshold choice.

## Important distinction from the paper-level original K1 monitor

The retained U-VOWEL paper describes the original predictive W2A K1 monitor more abstractly as:

- 74 scalar W2A uncertainty features per query
- 16 temporal action-uncertainty tokens
- eight-query history
- two-layer GRU
- GRU/static width 128
- fused 64D latent

That paper-level description is NOT interchangeable with this explicit portable H10 handoff. Do not mix the 74/16 paper contract and the 37/[10,6] H10 handoff into one model unless an original executable source proves how they correspond.
