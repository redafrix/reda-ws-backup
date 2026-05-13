# Trace One Sample Smoke Test

Status: `OK`

## Results

```json
{
  "checkpoint": "/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000",
  "local_backbone": "/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/models/huggingface/SmolVLM-500M-Instruct",
  "hdf5": "/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/data/libero_datasets/libero_90/KITCHEN_SCENE5_close_the_top_drawer_of_the_cabinet_demo.hdf5",
  "language_instruction": "close the top drawer of the cabinet",
  "input_ids": {
    "shape": [
      1,
      50
    ],
    "dtype": "torch.int64",
    "device": "cuda:0"
  },
  "image_input": {
    "shape": [
      1,
      3,
      3,
      384,
      384
    ],
    "dtype": "torch.float32",
    "device": "cuda:0"
  },
  "image_mask": {
    "shape": [
      1,
      3
    ],
    "dtype": "torch.bool",
    "device": "cuda:0"
  },
  "proprio": {
    "shape": [
      1,
      8
    ],
    "dtype": "torch.float32",
    "device": "cuda:0"
  },
  "expert_postprocessed_action": {
    "shape": [
      1,
      10,
      7
    ],
    "dtype": "torch.float32",
    "device": "cuda:0"
  },
  "expert_normalized_action": {
    "shape": [
      1,
      10,
      7
    ],
    "dtype": "torch.float32",
    "device": "cuda:0"
  },
  "generated_normalized_action_seed0": {
    "shape": [
      1,
      10,
      7
    ],
    "dtype": "torch.float32",
    "device": "cuda:0"
  },
  "generated_postprocessed_action_seed0": {
    "shape": [
      1,
      10,
      7
    ],
    "dtype": "torch.float32",
    "device": "cuda:0"
  },
  "pooled_vlm_features_seed0": {
    "shape": [
      1,
      960
    ],
    "dtype": "torch.float32",
    "device": "cuda:0"
  },
  "vlm_feature_shape_seed0": [
    1,
    122,
    960
  ],
  "proprio_norm_seed0": {
    "shape": [
      1,
      8
    ],
    "dtype": "torch.float32",
    "device": "cuda:0"
  },
  "seed0": 0,
  "seed1": 1,
  "num_flow_steps": 10,
  "actions_differ_between_seed0_seed1": true,
  "normalized_action_error_per_step_l2": [
    0.9314292073249817,
    1.0640287399291992,
    1.1854674816131592,
    1.3185051679611206,
    1.4286484718322754,
    1.4919395446777344,
    1.604980230331421,
    1.6370543241500854,
    1.672574520111084,
    1.7161381244659424
  ],
  "normalized_action_error_chunk_l2_mean": 1.4050766229629517,
  "postprocessed_action_error_per_step_l2": [
    0.9314292073249817,
    1.0640287399291992,
    1.1854674816131592,
    1.3185051679611206,
    1.4286484718322754,
    1.4919395446777344,
    1.604980230331421,
    1.6370543241500854,
    1.672574520111084,
    1.7161381244659424
  ],
  "postprocessed_action_error_chunk_l2_mean": 1.4050766229629517,
  "first_flow_step": {
    "t": 1.0,
    "dt": -0.1,
    "velocity_mean": 0.11160401999950409,
    "logvar_mean": -5.36920690536499
  },
  "last_flow_step": {
    "t": 0.10000000000000014,
    "dt": -0.1,
    "velocity_mean": 0.16131801903247833,
    "logvar_mean": -2.2472708225250244
  }
}
```

## Alignment

The expert target is `sample['action']`, already `[10,7]` after the official loader slices `abs_trajectory[1:]`. The trace generated normalized action is `[1,10,7]`; normalized error is computed after `model.action_space.normalize_action(sample['action'])`.
