# Stage 7 History Models

## Status

History/window models were not trained in this pass.

## Reason

The current Stage 5/6 candidate datasets contain independent decision contexts and `source_local_index` metadata, but no validated rollout sequence log with previous selected actions, previous uncertainties, and future-free temporal windows. Building a history model directly from absolute dataset indices risks accidentally encoding demonstration order or timestep-like leakage.

## Safe Plan

Create history datasets only from validated rollout logs or from HDF5 demos where windows are built from previous observations/actions while excluding absolute timestep, episode progress, episode length, trajectory length, and success/failure from inputs.

Candidate models:

- GRU/LSTM over previous pooled VLM/proprio/action/uncertainty features.
- Small Transformer encoder over fixed windows 2/4/8.
- Temporal convolution baseline.

## Decision

History is pending execution/sequence data. Do not claim history helps yet.
