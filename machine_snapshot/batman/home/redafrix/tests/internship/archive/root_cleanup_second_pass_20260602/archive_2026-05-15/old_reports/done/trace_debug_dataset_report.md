# Trace Debug Dataset Report

- Dataset: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/data/debug/trace_debug.pt`
- File size bytes: `1393986`
- Number of samples: `200`
- Schema: `trace_debug_v1`
- Checkpoint: `/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000`

## Keys And First-Sample Shapes

- `sample_id`: `str`
- `context_id`: `str`
- `task_name`: `str`
- `task_id`: `str`
- `demo_id`: `NoneType`
- `source_hdf5`: `str`
- `source_local_index`: `int`
- `language_instruction`: `str`
- `proprio`: `{'shape': [8], 'dtype': 'torch.float32'}`
- `pooled_vlm_features`: `{'shape': [960], 'dtype': 'torch.float32'}`
- `generated_normalized_action`: `{'shape': [10, 7], 'dtype': 'torch.float32'}`
- `generated_postprocessed_action`: `{'shape': [10, 7], 'dtype': 'torch.float32'}`
- `expert_normalized_action`: `{'shape': [10, 7], 'dtype': 'torch.float32'}`
- `expert_postprocessed_action`: `{'shape': [10, 7], 'dtype': 'torch.float32'}`
- `per_step_l2_error_normalized`: `{'shape': [10], 'dtype': 'torch.float32'}`
- `chunk_l2_error_normalized`: `float`
- `seed`: `int`
- `split`: `str`

## NaN/Inf Checks

- `proprio` finite: `True`
- `pooled_vlm_features` finite: `True`
- `generated_normalized_action` finite: `True`
- `generated_postprocessed_action` finite: `True`
- `expert_normalized_action` finite: `True`
- `expert_postprocessed_action` finite: `True`
- `per_step_l2_error_normalized` finite: `True`

## Error Stats

- chunk L2 min: `0.4533155560493469`
- chunk L2 mean: `1.652939796447754`
- chunk L2 max: `3.2215378284454346`

## Task Counts

- `close the top drawer of the cabinet`: `50`
- `open the top drawer of the cabinet`: `50`
- `put the bowl on the plate`: `25`
- `put the chocolate pudding to the right of the plate`: `25`
- `turn on the stove`: `50`

## Examples

- `debug_000000` task=`close the top drawer of the cabinet` instruction=`close the top drawer of the cabinet` source_index=`0`
- `debug_000001` task=`close the top drawer of the cabinet` instruction=`close the top drawer of the cabinet` source_index=`1`
- `debug_000002` task=`close the top drawer of the cabinet` instruction=`close the top drawer of the cabinet` source_index=`2`
- `debug_000003` task=`close the top drawer of the cabinet` instruction=`close the top drawer of the cabinet` source_index=`3`
- `debug_000004` task=`close the top drawer of the cabinet` instruction=`close the top drawer of the cabinet` source_index=`4`
- `debug_000005` task=`close the top drawer of the cabinet` instruction=`close the top drawer of the cabinet` source_index=`5`
- `debug_000006` task=`close the top drawer of the cabinet` instruction=`close the top drawer of the cabinet` source_index=`6`
- `debug_000007` task=`close the top drawer of the cabinet` instruction=`close the top drawer of the cabinet` source_index=`7`
