# Stage 8 History Models

Status: pending rollout sequence data.

History/window models require rollout traces with previous selected actions, previous uncertainty, proprio, and optionally VLM/flowtrace features. This job intentionally does not train a history model until rollout logs are available.

Planned windows:

- 2
- 4
- 8
- 16 as backup if enough data exists

Planned models:

- GRU/LSTM
- small Transformer
- TCN
- Mamba only if already installed

No future information, timestep, episode progress, or trajectory length will be used as inputs.
