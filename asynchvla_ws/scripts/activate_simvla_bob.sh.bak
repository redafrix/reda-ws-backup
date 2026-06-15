#!/usr/bin/env bash
set -euo pipefail

# Bob-specific lightweight SimVLA environment.
# Uses system Python/CUDA PyTorch plus project-local target site-packages.
export ASYNCVLA_WS="/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws"
export REDA_WS="/media/rootalkhatib/My Passport/reda_ws"
export SIMVLA_ENV_ROOT="/home/rootalkhatib/envs/simvla"
export SIMVLA_SITE_PACKAGES="$SIMVLA_ENV_ROOT/lib/python3.10/site-packages"
export PYTHONNOUSERSITE=1
export PYTHONPATH="$SIMVLA_SITE_PACKAGES:$REDA_WS/intern_ship_ws/simvla/code/SimVLA_modified:$REDA_WS/intern_ship_ws/assets/data/LIBERO:${PYTHONPATH:-}"
export LIBERO_CONFIG_PATH="$REDA_WS/intern_ship_ws/simvla/config/libero"
export HF_HOME="$REDA_WS/intern_ship_ws/assets/models/huggingface/.hf_home"
export TRANSFORMERS_CACHE="$HF_HOME/transformers"
export HF_HUB_CACHE="$HF_HOME/hub"

python_bin="/usr/bin/python3"
export PYTHON_BIN="$python_bin"

echo "Activated AsyncVLA Bob SimVLA env"
echo "  PYTHON_BIN=$PYTHON_BIN"
echo "  SIMVLA_SITE_PACKAGES=$SIMVLA_SITE_PACKAGES"
echo "  REDA_WS=$REDA_WS"
echo "  LIBERO_CONFIG_PATH=$LIBERO_CONFIG_PATH"
$PYTHON_BIN --version
