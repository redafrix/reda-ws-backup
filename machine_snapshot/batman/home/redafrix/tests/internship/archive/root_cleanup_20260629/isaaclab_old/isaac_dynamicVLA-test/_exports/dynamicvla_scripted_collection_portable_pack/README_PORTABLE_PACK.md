# DynamicVLA Scripted Data-Collection Portable Pack

This is a code-only portable pack for recreating the DynamicVLA scripted synthetic data-collection pipeline on another PC.

It does NOT include:
- Isaac Sim
- Isaac Lab
- DOM objects
- DOM scenes
- DOM tests
- datasets
- translated datasets
- videos
- model checkpoints
- training data

It DOES include:
- DynamicVLA code needed for scripted data collection
- baseline patched code
- static-object modified code
- helper scripts
- patch files
- checkpoint/reference documentation

---

## 1. Official sources

DynamicVLA GitHub:
https://github.com/hzxie/DynamicVLA

DOM Training Set, large training dataset:
https://huggingface.co/datasets/hzxie/DOM

DOM Testing Set:
https://gateway.infinitescript.com/?f=DOM-Test

DOM 3D Objects:
https://gateway.infinitescript.com/?f=DOM-3D-Objects

DOM 3D Scenes:
https://gateway.infinitescript.com/?f=DOM-3D-Scenes

DynamicVLA pretrained model:
https://huggingface.co/hzxie/dynamic-vla-DOM

---

## 2. Expected target PC layout

On the other PC, create a project root like:

```text
PROJECT_ROOT/
├── objects/           # Download/extract DOM 3D Objects here
├── scenes/            # Download/extract DOM 3D Scenes here
│   ├── textures/
│   └── *.usd
├── tests/             # Download/extract DOM Testing Set JSON files here
│   └── *.json
├── test-envs.txt      # Included in DOM Testing Set
├── datasets/          # Raw generated datasets will be saved here
├── datasets-tr/       # Translated generated datasets will be saved here
├── videos/            # Optional local inspection videos
└── dynamic-vla/       # Copy from this pack or clone official GitHub
```

---

## 3. Isaac requirements

Install on the target PC:

* Isaac Sim 4.5.0
* Isaac Lab 2.2.1
* Python 3.10
* Additional Isaac environment dependencies:

  * shapely
  * pyzmq
  * h5py
  * numpy
  * opencv-python or imageio for video tools

The original README recommends separate environments:

* one for model training/inference
* one for Isaac Lab simulation/evaluation

For data collection only, the Isaac Lab environment is the important one.

---

## 4. Included code versions

### `code/dynamic-vla/`

Baseline DynamicVLA code copied from the working workspace.

This includes the minimal compatibility patch:

* removed extra `args.timeout` passed into `get_test_env()` in:

  * `scripts/translate_dataset_seq.py`
  * `scripts/replay_dataset_seq.py`

### `code/dynamic-vla-static-v1/`

Development version for static-object scripted collection.

Known features:

* `--static_objects`
* keeps physics/gravity/collisions
* disables intentional initial object velocity
* output remains compatible with translation

Possible newer feature if present:

* `--static_stable_spawn`
* intended to reduce rolling by forcing more stable/yaw-only object spawn behavior

---

## 5. Basic official scripted collection command

Run from Isaac Lab environment:

```bash
cd PROJECT_ROOT/IsaacLab

./isaaclab.sh -p PROJECT_ROOT/dynamic-vla/simulations/simulate.py \
  --headless \
  --scene_dir PROJECT_ROOT/scenes \
  --object_dir PROJECT_ROOT/objects \
  --enable_cameras \
  --seed 42 \
  --save \
  --task place \
  --robot franka \
  --debug \
  -n 3
```

Expected outputs:

```text
PROJECT_ROOT/datasets/*.h5
PROJECT_ROOT/datasets/*.json
PROJECT_ROOT/datasets/*.mp4
```

---

## 6. Translate generated trajectories

```bash
mkdir -p PROJECT_ROOT/datasets-tr

cd PROJECT_ROOT/IsaacLab

./isaaclab.sh -p PROJECT_ROOT/dynamic-vla/scripts/translate_dataset_seq.py \
  --headless \
  --dataset_dir PROJECT_ROOT/datasets \
  --output_dir PROJECT_ROOT/datasets-tr \
  --scene_dir PROJECT_ROOT/scenes \
  --object_dir PROJECT_ROOT/objects \
  --enable_cameras \
  --save \
  --debug
```

Expected outputs:

```text
PROJECT_ROOT/datasets-tr/*-tr.h5
PROJECT_ROOT/datasets-tr/*-tr.json
PROJECT_ROOT/datasets-tr/*SUCCESS.mp4 or *FAIL.mp4
```

---

## 7. Static-object scripted collection command

Use this if copying `code/dynamic-vla-static-v1/` as the target repo:

```bash
cd PROJECT_ROOT/IsaacLab

./isaaclab.sh -p PROJECT_ROOT/dynamic-vla-static-v1/simulations/simulate.py \
  --headless \
  --scene_dir PROJECT_ROOT/scenes \
  --object_dir PROJECT_ROOT/objects \
  --enable_cameras \
  --seed 700 \
  --save \
  --task place \
  --robot franka \
  --debug \
  --static_objects \
  -n 3
```

If `--static_stable_spawn` exists in the copied script, test it like this:

```bash
./isaaclab.sh -p PROJECT_ROOT/dynamic-vla-static-v1/simulations/simulate.py \
  --headless \
  --scene_dir PROJECT_ROOT/scenes \
  --object_dir PROJECT_ROOT/objects \
  --enable_cameras \
  --seed 800 \
  --save \
  --task place \
  --robot franka \
  --debug \
  --static_stable_spawn \
  -n 3
```

---

## 8. Multi-camera visual inspection

Use:

```bash
python tools/make_multicam_video.py \
  --input PROJECT_ROOT/datasets-tr/example-tr.h5 \
  --output PROJECT_ROOT/videos/example_multicam.mp4 \
  --fps 20
```

This creates a single video grid from:

* wrist camera RGB
* side camera RGB
* opposite/front camera RGB
* wrist segmentation
* side segmentation
* opposite/front segmentation

---

## 9. Important rules

Always:

* run Isaac in `--headless` mode unless doing manual GUI inspection
* enable cameras when generating visual data: `--enable_cameras`
* explicitly set `-n`; do not use default 10000 accidentally
* clean stale Isaac/Kit processes before launching
* keep raw and translated datasets separate
* start with small tests before scaling

Never:

* launch two Isaac instances at the same time
* include assets/datasets/checkpoints in this code pack
* train before validating generated data visually
