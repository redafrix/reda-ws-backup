# Stage 7 Flow-Trace Features

## Implemented

Added compact flow metadata to:

- `asynchvla_ws/src/simvla_trace/trace.py`

New trace output includes `flow_trace_summary` with:

- `initial_noise_norm`
- `final_action_norm`
- `velocity_norm_mean`
- `velocity_norm_max`
- `velocity_norm_final`
- `update_norm_mean`
- `update_norm_max`
- `update_norm_last`
- `total_path_length`
- `final_update_over_mean_update`
- `action_state_norm_mean`
- `action_state_norm_delta`

Created:

- `asynchvla_ws/src/data_building/build_flowtrace_multiseed_dataset.py`
- `asynchvla_ws/src/features_stage7/flow_trace_features.py`

## Validation

Both new files pass `python3 -m py_compile` on Bob.

## Not Yet Run

A flow-trace dataset build/training run was not launched yet because the Bob GPU is currently occupied by the Stage 7 extra-OOD completion job. Running flow-trace extraction concurrently would contend with the same 4070 Ti SUPER and make both jobs slower.

## Next Command

After the OOD completion job finishes:

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source asynchvla_ws/scripts/activate_simvla_bob.sh
python3 asynchvla_ws/src/data_building/build_flowtrace_multiseed_dataset.py \
  --split-manifest asynchvla_ws/data/splits/holdout_libero_object.json \
  --split-name holdout_libero_object \
  --max-contexts 200 --max-calib 80 --max-test-id 80 --max-test-ood 80 \
  --cap-per-file 10 --simvla-seeds 0 1 2 3 4
```

## Decision

Flow-trace features are implemented but not yet proven useful. Keep/drop decision is pending actual metrics versus Stage 6 `context_gated_action`.
