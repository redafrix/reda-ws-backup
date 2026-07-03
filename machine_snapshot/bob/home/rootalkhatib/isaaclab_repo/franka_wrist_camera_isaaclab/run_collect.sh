#!/usr/bin/env bash
set -euo pipefail

# Explicit defaults near the top, override-friendly
CONDA_ENV_NAME="${CONDA_ENV_NAME:-env_isaaclab_6_0}"
CONDA_ROOT="${CONDA_ROOT:-$HOME/miniconda3}"
ISAACLAB_ROOT="${ISAACLAB_ROOT:-$HOME/IsaacLab-6.0}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ISAACLAB_PYTHON_SCRIPT="${ISAACLAB_PYTHON_SCRIPT:-${SCRIPT_DIR}/scripts/collect.py}"

if [[ ! -f "$CONDA_ROOT/etc/profile.d/conda.sh" ]]; then
    echo "Missing conda.sh at: $CONDA_ROOT/etc/profile.d/conda.sh" >&2
    exit 1
fi

source "$CONDA_ROOT/etc/profile.d/conda.sh"
conda activate "$CONDA_ENV_NAME"

CUDA_LIB_DIR="${CUDA_LIB_DIR:-$CONDA_PREFIX/lib/python3.12/site-packages/nvidia/cu13/lib}"

if [[ ! -x "$ISAACLAB_ROOT/isaaclab.sh" ]]; then
    echo "Missing Isaac Lab launcher at: $ISAACLAB_ROOT/isaaclab.sh" >&2
    exit 1
fi

export PYTHONPATH="$SCRIPT_DIR/src:$ISAACLAB_ROOT/source/isaaclab:$ISAACLAB_ROOT/source/isaaclab_assets:$ISAACLAB_ROOT/source/isaaclab_tasks:$ISAACLAB_ROOT/source/isaaclab_mimic:$ISAACLAB_ROOT/source/isaaclab_rl:$ISAACLAB_ROOT/source/isaaclab_contrib:${PYTHONPATH:-}"

export VK_ICD_FILENAMES="${VK_ICD_FILENAMES:-/usr/share/vulkan/icd.d/nvidia_icd.json}"
export TERM=xterm

if [[ -d "$CUDA_LIB_DIR" ]]; then
    export LD_LIBRARY_PATH="$CUDA_LIB_DIR:${LD_LIBRARY_PATH:-}"
fi

exec "$ISAACLAB_ROOT/isaaclab.sh" -p "$ISAACLAB_PYTHON_SCRIPT" "$@"
