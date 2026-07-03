# FIPER Current Baseline

Date: 2026-05-28

The current baseline for Stage 9 / LIBERO-PRO / FIPER is:

```text
MODEL_ID = v2_018_transformer_k16
MODEL_CLASS = supervised temporal risk scorer
POLICY = score q95 + success-only conformal risk mass, alpha=0.15
```

This is the baseline because the later official-LIBERO, dynamic-threshold, and
capacity/history sweeps did not beat it under the agreed decision rules.

## Inputs

Deployable inputs only:

- current SimVLA main action chunk, 10 x 7
- action statistics from the main action chunk
- ACE metrics from sampled candidate chunks
- current proprio
- history window `k=16`
  - previous proprio
  - previous executed actions
  - previous ACE metrics

Forbidden inputs are not used:

- reward
- success flag
- object poses / `object_positions_before`
- task/language metadata as input
- future timesteps
- OOD rows in train/calibration

## Architecture

```text
model = seq_transformer
history_steps = 16
width = 128
layers = 3
heads = 4
action_repr = stats
include_ace = true
include_ace_history = true
include_proprio = true
include_objects = false
```

The model outputs one scalar supervised risk score per timestep:

```text
risk_score = sigmoid(logit)
```

## Online Policy

The current deployment policy is:

```text
row_threshold = q95(risk_score on success_calib_seen)
excess_t = max(0, risk_score_t - row_threshold)
risk_mass_t = sum(excess_i for i <= t)
alarm when risk_mass_t >= conformal_threshold
```

The conformal threshold is calibrated from success validation episodes only:

```text
conformal_threshold = split_conformal_upper(
  episode_total_risk_mass on success_val_seen,
  alpha = 0.15
)
```

## Main Evidence

Target-object OOD, all 5 folds:

```text
OOD success false alarm: 43.1%
OOD failure detection: 98.0%
Det@25: 56.5%
Det@50: 92.5%
Mean detection time: 0.275
Never detected: 2.0%
```

Fold00 existing real baseline:

```text
Seen FA: 15.4%
OOD FA: 25.6%
Failure Det: 95.2%
Det@25: 26.2%
Det@50: 85.7%
Mean time: 0.332
```

## Current Artifact Paths

Paths are relative to `fiper_ws` so they work on both Sam and Bob.

```text
data/frozen/fiper_sweep_eternal_20260527_combined/
data/manifests/fiper_sweep_eternal_20260527_combined/
experiments/prepared_20260527/
experiments/clean_temporal_nextgen_v2_full_all_20260527/*/jobs/v2_018_transformer_k16/
experiments/transformer_k16_online_policy_sweep_20260528/
experiments/transformer_k16_dynamic_threshold_policy_sweep_20260528/
experiments/transformer_capacity_history_sweep_fold00_v1_20260528/
experiments/transformer_capacity_history_small_sweep_fold00_v1_20260528/
reports/TRANSFORMER_CAPACITY_HISTORY_BIG_SMALL_SWEEP_FOLD00_V1_REPORT.md
```

## Rejected Directions

- Official LIBERO action normality / autoencoder score: reduced false alarms but killed failure recall.
- Official LIBERO pretraining: did not beat existing real `v2_018`.
- Simple dynamic thresholds / timestep-binned thresholds: only tiny or negative improvement.
- Bigger/smaller Transformer capacity sweep on fold00: no model beat existing real `v2_018` under the decision rule.

