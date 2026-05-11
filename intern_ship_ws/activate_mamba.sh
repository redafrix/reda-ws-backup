#!/usr/bin/env bash
set -euo pipefail

# Hybrid Mamba Setup: Use the internal SSD environment for stability, but workspace on external drive.
ENV_PATH="/home/redafrix/envs/simvla_mamba"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ ! -d "$ENV_PATH" ]; then
    echo "Error: Mamba Environment not found at $ENV_PATH"
    exit 1
fi

source "$ENV_PATH/bin/activate"

# Essential for CUDA/Mamba/CausalConv1d
export LD_LIBRARY_PATH="$ENV_PATH/lib/python3.10/site-packages/nvidia/cuda_runtime/lib:$ENV_PATH/lib/python3.10/site-packages/nvidia/cublas/lib:$ENV_PATH/lib/python3.10/site-packages/nvidia/cudnn/lib:$ENV_PATH/lib/python3.10/site-packages/nvidia/cusolver/lib:$ENV_PATH/lib/python3.10/site-packages/nvidia/cusparse/lib:$ENV_PATH/lib/python3.10/site-packages/nvidia/nccl/lib:$ENV_PATH/lib/python3.10/site-packages/nvidia/nvtx/lib:$ENV_PATH/lib/python3.10/site-packages/torch/lib:${LD_LIBRARY_PATH:-}"

export PYTHONNOUSERSITE=1
export PYTHONPATH="$SCRIPT_DIR:$SCRIPT_DIR/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/v8_exp12_mamba/phase2_tdqc:$PYTHONPATH"

echo "Activated Hybrid Mamba TDQC env:"
echo "  VIRTUAL_ENV=$VIRTUAL_ENV"
echo "  PYTHONPATH=$PYTHONPATH"
python -V
