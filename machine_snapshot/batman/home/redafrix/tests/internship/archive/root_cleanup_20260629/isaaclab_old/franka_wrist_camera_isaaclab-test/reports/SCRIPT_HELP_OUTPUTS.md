usage: generate_object_catalog.py [-h] [--asset-root ASSET_ROOT]
                                  [--output OUTPUT]

Generate a USD object catalog.

options:
  -h, --help            show this help message and exit
  --asset-root ASSET_ROOT
                        Root directory containing object USD asset folders.
  --output OUTPUT       Generated catalog YAML path.
usage: inspect_object_catalog.py [-h] [--config CONFIG]

Inspect a USD object catalog.

options:
  -h, --help       show this help message and exit
  --config CONFIG  Catalog config name under configs/.
objects: 1
id                     label          category       kind       size
cube_primitive_006     cube           primitive      cuboid     (0.06, 0.06, 0.06)
usage: inspect_collection.py [-h] collection_dir

Inspect a raw tabletop collection.

positional arguments:
  collection_dir

options:
  -h, --help      show this help message and exit
usage: export_ila.py [-h] raw_collection_dir export_dir

Export raw tabletop collection to ILA format.

positional arguments:
  raw_collection_dir
  export_dir

options:
  -h, --help          show this help message and exit
usage: write_ila_splits.py [-h] [--val_fraction VAL_FRACTION] dataset_dir

Write deterministic ILA train/val splits.

positional arguments:
  dataset_dir

options:
  -h, --help            show this help message and exit
  --val_fraction VAL_FRACTION
usage: write_ila_stats.py [-h] dataset_dir

Write ILA dataset statistics.

positional arguments:
  dataset_dir

options:
  -h, --help   show this help message and exit
Traceback (most recent call last):
  File "/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/franka_wrist_camera_isaaclab/scripts/inspect_ila_dataset.py", line 13, in <module>
    from franka_wrist_camera_scene.datasets.ila import ILADataset
  File "/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/franka_wrist_camera_isaaclab/src/franka_wrist_camera_scene/datasets/ila.py", line 9, in <module>
    import torch
ModuleNotFoundError: No module named 'torch'
usage: visualize_ila_episode.py [-h] [--output OUTPUT]
                                [--num_frames NUM_FRAMES]
                                dataset_dir episode_id

Visualize one exported ILA episode.

positional arguments:
  dataset_dir
  episode_id

options:
  -h, --help            show this help message and exit
  --output OUTPUT
  --num_frames NUM_FRAMES
