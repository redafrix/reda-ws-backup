#!/usr/bin/env bash
set -euo pipefail

# Experiment-specific Activation Script (v8_exp11_transformer)
ENV_PATH="/home/redafrix/envs/simvla_transformer"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Initialize conda
source "$(conda info --base)/etc/profile.d/conda.sh" 2>/dev/null || source "$HOME/miniconda3/etc/profile.d/conda.sh" 2>/dev/null || true

if [ ! -d "$ENV_PATH" ]; then
    echo "Error: Environment not found at $ENV_PATH"
    exit 1
fi

conda activate "$ENV_PATH"

# Set PYTHONPATH to include the capsule's code directory
export PYTHONPATH="$SCRIPT_DIR:$PYTHONPATH"

export PYTHONNOUSERSITE=1

echo "Activated Transformer Experiment env:"
echo "  CONDA_PREFIX=$CONDA_PREFIX"
echo "  PYTHONPATH=$PYTHONPATH"
python -V
