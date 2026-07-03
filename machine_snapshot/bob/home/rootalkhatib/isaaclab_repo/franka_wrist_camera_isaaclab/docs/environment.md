# Runtime environment

The repository is configured for the local Isaac Sim / Isaac Lab environment selected by `run_collect.sh`.

Defaults:

```bash
CONDA_ENV_NAME=env_isaaclab_6_0
CONDA_ROOT=$HOME/miniconda3
ISAACLAB_ROOT=$HOME/IsaacLab-6.0
```

`run_collect.sh` activates the conda environment, sets the project and Isaac Lab `PYTHONPATH`, and adds the configured CUDA/NVRTC library directory when it exists. The local default is the conda env's `nvidia/cu13/lib` directory because this Isaac/Torch runtime needs `libnvrtc-builtins.so.13.0`.

Run collection with:

```bash
./run_collect.sh --collection_config configs/collection.yaml --headless
```

Headless RGB collection is expected to work in this configured environment. The repository does not block collection based on Isaac Sim or Isaac Lab version strings. Dataset integrity is enforced at recording time: if recorded RGB frames are all black or missing, saving and validation fail loudly.

Override local paths when needed:

```bash
CONDA_ENV_NAME=other_env ISAACLAB_ROOT=$HOME/OtherIsaacLab ./run_collect.sh --collection_config configs/collection.yaml --headless
```
