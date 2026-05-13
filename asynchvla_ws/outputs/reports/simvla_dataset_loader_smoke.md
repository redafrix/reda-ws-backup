# SimVLA Dataset Loader Smoke Test

- Workspace: `/media/rootalkhatib/My Passport/reda_ws`
- Loader: `/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/simvla/code/SimVLA_modified/datasets/dataset_smolvlm.py`
- Handler: `/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/simvla/code/SimVLA_modified/datasets/domain_handler/libero_hdf5.py`
- Debug meta: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/data/debug/one_libero_meta.json`
- HDF5: `/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/data/libero_datasets/libero_90/KITCHEN_SCENE5_close_the_top_drawer_of_the_cabinet_demo.hdf5`
- Task text: `close the top drawer of the cabinet`

## Sample Keys And Shapes

- `action`: `{'shape': [10, 7], 'dtype': 'torch.float32'}`
- `image_input`: `{'shape': [3, 3, 384, 384], 'dtype': 'torch.float32'}`
- `image_mask`: `{'shape': [3], 'dtype': 'torch.bool'}`
- `language_instruction`: `{'type': 'str', 'repr': "'close the top drawer of the cabinet'"}`
- `proprio`: `{'shape': [8], 'dtype': 'torch.float32'}`

## Alignment Decision

The official `LiberoHDF5Handler._get_action_chunk()` creates `[num_actions + 1, 7]` chunks internally: current action at index 0 plus 10 future actions. `datasets/utils.py::action_slice()` then sets `action = abs_traj[1:].clone()`, so the dataset sample exposes `action` as `[10, 7]`.

For SimVLA generated chunks with `num_actions=10`, compare generated normalized `[10,7]` against `sample['action']` normalized with the model action space. Do not include the current action at index 0 in the error target.

## Terminal Output

```text
dataset_loader_smoke: OK
hdf5 /media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/data/libero_datasets/libero_90/KITCHEN_SCENE5_close_the_top_drawer_of_the_cabinet_demo.hdf5
debug_meta /media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/data/debug/one_libero_meta.json
keys ['action', 'image_input', 'image_mask', 'language_instruction', 'proprio']
action {'shape': [10, 7], 'dtype': 'torch.float32'}
image_input {'shape': [3, 3, 384, 384], 'dtype': 'torch.float32'}
image_mask {'shape': [3], 'dtype': 'torch.bool'}
language_instruction {'type': 'str', 'repr': "'close the top drawer of the cabinet'"}
proprio {'shape': [8], 'dtype': 'torch.float32'}
expert_action_chunk_shape [10, 7]
expert_action_min_mean_max -1.0 -0.12530101835727692 0.6187499761581421
```
