# Franka wrist-camera tabletop collection

This repository collects Isaac Lab Franka tabletop manipulation episodes with synchronized robot state, actions, object metadata, and RGB camera observations from an agent camera and a wrist camera.

The maintained tasks are:

- **pick_place**: object-to-physical-receptacle placement with clutter and RGB-D;
- **reaching**: position-only TCP reaching toward named objects/receptacles in dense clutter.

Both tasks enforce:
- workspace constraints and minimum target/clutter/receptacle XY separation;
- reaching height derived from bbox geometry;
- reset logic that parks inactive asset-bank objects and zeros active object/receptacle velocities;
- RGB validation that fails loudly if recorded camera frames are black.

In addition, reaching uses position-only TCP control (orientation is not commanded), keeping the gripper closed at all times. Pick-place uses pose IK and executes a full pick, lift, move, and release sequence.

## Environment Bootstrap and Running Collection

Local environment bootstrap is managed through [run_collect.sh](run_collect.sh). It activates the configured conda environment and sets the Isaac Lab paths. The defaults are near the top of the script:

```bash
CONDA_ENV_NAME=env_isaaclab_6_0
CONDA_ROOT=$HOME/miniconda3
ISAACLAB_ROOT=$HOME/IsaacLab-6.0
CUDA_LIB_DIR=$CONDA_PREFIX/lib/python3.12/site-packages/nvidia/cu13/lib
```

You can override these defaults by setting environment variables before executing the script:

```bash
CONDA_ENV_NAME=env_isaaclab_6_0 ISAACLAB_ROOT=$HOME/IsaacLab-6.0 ./run_collect.sh --collection_config configs/collection.yaml --headless
```

### Running Pick-Place Collection
To run the default pick-place collection:

```bash
./run_collect.sh --collection_config configs/collection.yaml --headless
```

### Running Reaching Collection
To run the reaching smoke test collection:

```bash
./run_collect.sh --collection_config configs/collection_reaching_smoke.yaml --headless
```

To run full reaching collection:

```bash
./run_collect.sh --collection_config configs/collection_reaching.yaml --headless
```

## Collection Suites and Configuration Inspection

Reusable train, evaluation, and smoke suites live under [configs/suites/](configs/suites/) and the base configs under [configs/](configs/).

You can inspect candidate pools and deterministic object/receptacle compatibility samples for any collection suite or configuration without launching Isaac Sim:

```bash
PYTHONPATH=src python scripts/inspect_collection_suite.py configs/collection.yaml
PYTHONPATH=src python scripts/inspect_collection_suite.py configs/collection_reaching.yaml
PYTHONPATH=src python scripts/inspect_collection_suite.py configs/suites/pick_place_train_core.yaml
```

The maintained pick-place suites are:
- `pick_place_train_core`: diverse train target objects, physical receptacles (bowls and curated boxes), lighting variation, and clutter.
- `pick_place_train_dense_clutter`: train distribution with clutter concentrated around the workspace.
- `pick_place_eval_unseen_objects`: unseen target objects with train-split receptacles.
- `pick_place_eval_spatial_wide`: wider safe object and receptacle pose ranges.
- `pick_place_eval_lighting`: stronger dome-light intensity and color variation.
- `pick_place_eval_visual_shift`: stronger lighting plus table-color variation.
- `pick_place_headless_smoke`: one recorded pick-place episode through the full core path.

The generated train catalog currently provides bowls and hollow boxes as physical receptacles. Cups are visual containers only and are not physical placement receptacles.

Suite metadata, sampled assets, pose offsets, lighting/table-color values, camera dimensions/fps, and active clutter metadata are written to each `meta.json` and the collection `manifest.json`.

## RGB Validation

After a recorded collection, validate that recorded camera frames are correct and not black:

```bash
python scripts/check_headless_rgb.py data/raw/suites/pick_place_headless_smoke
python scripts/check_headless_rgb.py data/raw/debug_reaching_smoke
```

The script checks both `agent_rgb` and `wrist_rgb` in `trajectory.npz` and raises an exception if the data is missing or effectively black.

To create a side-by-side video from recorded episodes:

```bash
PYTHONPATH=src python scripts/stitch_episode_videos.py data/raw/debug_reaching_smoke
```

## Development and Testing

Run pure-Python static checks and unit tests with:

```bash
python -m compileall src scripts
PYTHONPATH=src python -m unittest discover -s tests
```

If `ruff` is installed in the active environment:

```bash
ruff check .
```

The scripts only load configs and dispatch package code. Scene construction lives in `scene/`, task specifications and preflight checks in `tasks/` and `collection/`, reset/recording in `episode/`, scripted policies in `policies/`, and dataset/export utilities in `export/`.
