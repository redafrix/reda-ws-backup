# Safe Script Test Plan

Rules:
- No long data collection.
- No modifications.
- Headless only.
- Use max_steps / num_episodes / small output dirs when available.
- Inspect-only scripts can run normally.
- Scripts that require generated data should be tested after one tiny collection if possible.

## Script names
collect.py
debug_scene.py
export_ila.py
generate_object_catalog.py
inspect_collection.py
inspect_episode.py
inspect_ila_dataset.py
inspect_object_catalog.py
inspect_objects.py
run.sh
visualize_ila_episode.py
write_ila_splits.py
write_ila_stats.py

## run.sh content
#!/usr/bin/env bash
# Main entry point bash script to run simulation, collection, or evaluation commands.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ISAACLAB_ROOT="${ISAACLAB_ROOT:-$HOME/IsaacLab}"

export PYTHONPATH="$REPO_ROOT/src:${PYTHONPATH:-}"
exec "$ISAACLAB_ROOT/isaaclab.sh" -p "$REPO_ROOT/scripts/debug_scene.py" "$@"

## Root run scripts
### run_collect
#!/usr/bin/env bash
# Helper script to run the Franka wrist camera data collection with pre-configured env variables.

# Exit immediately if a command exits with a non-zero status
set -euo pipefail

# Get directory of this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Clean up conda env variables to prevent conflicting python environment paths
unset CONDA_PREFIX
unset CONDA_DEFAULT_ENV

# Set PYTHONPATH to include all relevant Isaac Lab modules and the project src folder
export PYTHONPATH="/home/utilisateur/IsaacLab/source/isaaclab:/home/utilisateur/IsaacLab/source/isaaclab_assets:/home/utilisateur/IsaacLab/source/isaaclab_contrib:/home/utilisateur/IsaacLab/source/isaaclab_mimic:/home/utilisateur/IsaacLab/source/isaaclab_rl:/home/utilisateur/IsaacLab/source/isaaclab_tasks:${SCRIPT_DIR}/src:${PYTHONPATH:-}"

# Force Vulkan to use the NVIDIA ICD (prevents interference from integrated graphics GPUs)
export VK_ICD_FILENAMES=/usr/share/vulkan/icd.d/nvidia_icd.json
export TERM=xterm

ISAACLAB_ROOT="${ISAACLAB_ROOT:-$HOME/IsaacLab}"

exec "$ISAACLAB_ROOT/isaaclab.sh" -p "${SCRIPT_DIR}/scripts/collect.py" "$@"
### run_collect.sh
#!/usr/bin/env bash
# Helper script to run the Franka wrist camera data collection with pre-configured env variables.

# Exit immediately if a command exits with a non-zero status
set -euo pipefail

# Get directory of this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Clean up conda env variables to prevent conflicting python environment paths
unset CONDA_PREFIX
unset CONDA_DEFAULT_ENV

# Set PYTHONPATH to include all relevant Isaac Lab modules and the project src folder
export PYTHONPATH="/home/utilisateur/IsaacLab/source/isaaclab:/home/utilisateur/IsaacLab/source/isaaclab_assets:/home/utilisateur/IsaacLab/source/isaaclab_contrib:/home/utilisateur/IsaacLab/source/isaaclab_mimic:/home/utilisateur/IsaacLab/source/isaaclab_rl:/home/utilisateur/IsaacLab/source/isaaclab_tasks:${SCRIPT_DIR}/src:${PYTHONPATH:-}"

# Force Vulkan to use the NVIDIA ICD (prevents interference from integrated graphics GPUs)
export VK_ICD_FILENAMES=/usr/share/vulkan/icd.d/nvidia_icd.json
export TERM=xterm

ISAACLAB_ROOT="${ISAACLAB_ROOT:-$HOME/IsaacLab}"

exec "$ISAACLAB_ROOT/isaaclab.sh" -p "${SCRIPT_DIR}/scripts/collect.py" "$@"
### run_sim.sh
#!/usr/bin/env bash
# Helper script to run the Franka wrist camera simulation with pre-configured env variables.

# Exit immediately if a command exits with a non-zero status
set -euo pipefail

# Get directory of this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Clean up conda env variables to prevent conflicting python environment paths
unset CONDA_PREFIX
unset CONDA_DEFAULT_ENV

# Set PYTHONPATH to include all relevant Isaac Lab modules and the project src folder
export PYTHONPATH="/home/utilisateur/IsaacLab/source/isaaclab:/home/utilisateur/IsaacLab/source/isaaclab_assets:/home/utilisateur/IsaacLab/source/isaaclab_contrib:/home/utilisateur/IsaacLab/source/isaaclab_mimic:/home/utilisateur/IsaacLab/source/isaaclab_rl:/home/utilisateur/IsaacLab/source/isaaclab_tasks:${SCRIPT_DIR}/src:${PYTHONPATH:-}"

# Force Vulkan to use the NVIDIA ICD (prevents interference from integrated graphics GPUs)
export VK_ICD_FILENAMES=/usr/share/vulkan/icd.d/nvidia_icd.json
export TERM=xterm

# Execute the simulation run script passing along all arguments
exec "${SCRIPT_DIR}/scripts/run.sh" "$@"
