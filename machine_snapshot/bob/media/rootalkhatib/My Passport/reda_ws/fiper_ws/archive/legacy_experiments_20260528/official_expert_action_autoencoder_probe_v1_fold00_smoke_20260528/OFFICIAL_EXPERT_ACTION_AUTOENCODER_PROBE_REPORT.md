# Official LIBERO Expert Action Autoencoder Probe

## Setup

- Current score baseline: `v2_018_transformer_k16` mass-conformal alpha=0.15
- Official demos: `/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/data/libero_datasets/libero_object`
- Leakage rule: each fold excludes its held-out target objects from official expert fitting.
- Features used by expert score: only 10-step main action chunk, flattened to 70 dims.
- Forbidden deploy-time fields used: none.
- Network architecture: MLP Autoencoder (70 -> 128 -> 64 -> 32 -> 64 -> 128 -> 70)
- Epochs: 3, Batch Size: 256, Learning Rate: 0.001

## Results Table

| Policy | Seen FA | OOD FA | OOD Failure Det | Det@10 | Det@25 | Det@50 | Mean Det Time | Never |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| fold_00_holdout_alphabet_soup_bbq_sauce - current_transformer_mass | 15.4% | 25.6% | 95.2% | 0.0% | 26.2% | 85.7% | 0.332 | 4.8% |
| fold_00_holdout_alphabet_soup_bbq_sauce - official_autoencoder_mass | 15.4% | 3.8% | 26.2% | 0.0% | 0.0% | 11.9% | 0.605 | 73.8% |
| fold_00_holdout_alphabet_soup_bbq_sauce - current_AND_official_autoencoder | 3.7% | 2.8% | 26.2% | 0.0% | 9.5% | 26.2% | 0.314 | 73.8% |
| fold_00_holdout_alphabet_soup_bbq_sauce - current_OR_official_autoencoder | 27.2% | 26.5% | 95.2% | 0.0% | 33.3% | 85.7% | 0.312 | 4.8% |

## Output Files

- `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/experiments/official_expert_action_autoencoder_probe_v1_fold00_smoke_20260528/official_expert_action_autoencoder_results.csv`
- `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/experiments/official_expert_action_autoencoder_probe_v1_fold00_smoke_20260528/official_expert_action_autoencoder_results.json`
- `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/experiments/official_expert_action_autoencoder_probe_v1_fold00_smoke_20260528/official_expert_action_autoencoder_calibration.json`
