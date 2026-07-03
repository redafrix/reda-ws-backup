# Official LIBERO Expert Action Normality Probe

## Setup

- Current score baseline: `v2_018_transformer_k16` mass-conformal alpha=0.15
- Official demos: `/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/data/libero_datasets/libero_object`
- Leakage rule: each fold excludes its held-out target objects from official expert fitting.
- Features used by expert score: only 10-step main action chunk, flattened to 70 dims.
- Forbidden deploy-time fields used: none.

## Aggregate Results

| Policy | Seen FA | OOD FA | OOD Failure Det | Det@25 | Det@50 | Mean Det Time | Never |
|---|---:|---:|---:|---:|---:|---:|---:|
| current_AND_official_meanstd | 1.4% | 8.0% | 13.6% | 2.0% | 10.9% | 0.441 | 86.4% |
| current_AND_official_robust | 2.3% | 10.6% | 32.0% | 15.0% | 27.9% | 0.302 | 68.0% |
| current_OR_official_meanstd | 25.6% | 41.7% | 98.6% | 63.3% | 93.9% | 0.248 | 1.4% |
| current_OR_official_robust | 27.0% | 43.1% | 98.6% | 63.9% | 95.2% | 0.228 | 1.4% |
| current_transformer_mass | 16.4% | 41.4% | 98.6% | 57.8% | 93.9% | 0.268 | 1.4% |
| official_meanstd | 10.5% | 8.3% | 13.6% | 7.5% | 8.8% | 0.417 | 86.4% |
| official_robust | 12.8% | 12.3% | 32.0% | 17.0% | 20.4% | 0.307 | 68.0% |

## Interpretation Guardrails

- This does not train on official held-out object demos for the corresponding fold.
- It is a quick action-space transfer probe, not a full visual/proprio encoder pretrain.
- If AND policies reduce false alarms but lose too much detection, official actions are not a useful deployment veto.
- If expert-only is weak, official expert actions are not enough by themselves for this OOD monitor.

## Output Files

- `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/experiments/official_expert_action_normality_probe_v1_smoke_20260528/official_expert_action_normality_results.csv`
- `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/experiments/official_expert_action_normality_probe_v1_smoke_20260528/official_expert_action_normality_results.json`
- `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/experiments/official_expert_action_normality_probe_v1_smoke_20260528/official_expert_action_normality_calibration.json`
