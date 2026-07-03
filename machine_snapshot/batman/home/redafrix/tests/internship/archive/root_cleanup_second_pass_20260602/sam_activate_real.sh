#!/usr/bin/env bash
export REDA_WS="/home/rootalkhatib/test/reda_ws"
export PATH="/home/rootalkhatib/envs/simvla/bin:$PATH"
export PYTHONPATH="$REDA_WS/intern_ship_ws/simvla/code/SimVLA_modified:$REDA_WS/asynchvla_ws/src:${PYTHONPATH:-}"
export HF_HOME="$REDA_WS/intern_ship_ws/assets/models/huggingface/.hf_cache"
export TRANSFORMERS_CACHE="$HF_HOME/transformers"
export HF_HUB_CACHE="$HF_HOME/hub"
echo "Activated AsyncVLA Sam SimVLA env"
echo "  PYTHON_BIN=$(command -v python3)"
echo "  REDA_WS=$REDA_WS"
python3 --version
