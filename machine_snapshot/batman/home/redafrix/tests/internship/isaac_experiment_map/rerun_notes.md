# Isaac Rerun Notes

These notes preserve the working structure. They are not meant to be run blindly without checking Bob state, available GPU memory, and whether a server is already running.

## General Rules

- Use Isaac rollout with `--device cpu --rendering_mode performance` when the OpenPI server is using the GPU.
- Use no image flip for Isaac camera observations.
- Keep LIBERO and DROID outputs separate.
- Use collection-length failure limits:
  - reaching: `3600`.
  - pick-place: `3800`.
- If a final episode video/rgb is corrupt after shutdown, rerun episode 4 plus disposable episode 5 using the `*_ep4_plus_dummy_rerun.yaml` configs, delete episode 5, then rebuild the combined video.

## Pi0.5 LIBERO Server

From Bob repo root:

```bash
XLA_PYTHON_CLIENT_PREALLOCATE=false XLA_PYTHON_CLIENT_MEM_FRACTION=0.65 ./run_pi05_libero_server_bob.sh
```

Expected port:

```text
8005
```

## Pi0.5 LIBERO Rollouts

```bash
./run_pi05_reaching_rollout.sh \
  --rollout_config configs/eval_pi05_reaching_bob_5ep.yaml \
  --headless --device cpu --rendering_mode performance

./run_pi05_pick_place_rollout.sh \
  --rollout_config configs/eval_pi05_pick_place_bob_5ep.yaml \
  --headless --device cpu --rendering_mode performance
```

## Pi0.5 DROID Server

From Bob repo root:

```bash
XLA_PYTHON_CLIENT_PREALLOCATE=false XLA_PYTHON_CLIENT_MEM_FRACTION=0.65 ./run_pi05_droid_server_bob.sh
```

Expected port:

```text
8006
```

## Pi0.5 DROID Rollouts

```bash
./run_pi05_droid_reaching_rollout.sh \
  --rollout_config configs/eval_pi05_droid_reaching_bob_5ep.yaml \
  --headless --device cpu --rendering_mode performance

./run_pi05_droid_pick_place_rollout.sh \
  --rollout_config configs/eval_pi05_droid_pick_place_bob_5ep.yaml \
  --headless --device cpu --rendering_mode performance
```

## Build Combined Pi0.5 Video

Example for DROID:

```bash
/home/rootalkhatib/miniconda3/envs/env_isaaclab_6_0/bin/python3 scripts/create_pi05_combined_agent_video.py \
  --reaching-dir data/raw/pi05_droid_reaching_5ep_collection_limit \
  --pick-place-dir data/raw/pi05_droid_pick_place_5ep_collection_limit \
  --output data/processed/pi05_droid_10_tests_agent_view_2x.mp4 \
  --speed 2 \
  --force
```

Example for LIBERO:

```bash
/home/rootalkhatib/miniconda3/envs/env_isaaclab_6_0/bin/python3 scripts/create_pi05_combined_agent_video.py \
  --reaching-dir data/raw/pi05_libero_reaching_5ep_collection_limit \
  --pick-place-dir data/raw/pi05_libero_pick_place_5ep_collection_limit \
  --output data/processed/pi05_libero_10_tests_agent_view_2x.mp4 \
  --speed 2 \
  --force
```

## Local Fast Labeled Videos

The current final local videos were postprocessed from the combined videos:

- `vids/pi05_droid_10_tests_agent_view_4x_labeled.mp4`
- `vids/pi05_libero_10_tests_agent_view_4x_labeled.mp4`

The label style that worked cleanly at `300x300` was a two-line full-width top banner.

