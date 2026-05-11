#!/usr/bin/env bash
set -euo pipefail

# Hybrid Setup: Use the internal SSD environment for stability, but workspace on external drive.
ENV_PATH="/home/redafrix/envs/simvla"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Initialize conda
source "$(conda info --base)/etc/profile.d/conda.sh" 2>/dev/null || source "$HOME/miniconda3/etc/profile.d/conda.sh" 2>/dev/null || true

if [ ! -d "$ENV_PATH" ]; then
    echo "Error: Environment not found at $ENV_PATH"
    exit 1
fi

conda activate "$ENV_PATH"
export PYTHONNOUSERSITE=1
export LIBERO_CONFIG_PATH="$SCRIPT_DIR/simvla/config/libero"

echo "Activated Hybrid SimVLA env:"
echo "  CONDA_PREFIX=$CONDA_PREFIX"
echo "  WORKSPACE_DIR=$SCRIPT_DIR"
echo "  PYTHONNOUSERSITE=$PYTHONNOUSERSITE"
python -V
