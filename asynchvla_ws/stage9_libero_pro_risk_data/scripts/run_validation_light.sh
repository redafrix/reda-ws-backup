#!/usr/bin/env bash
set -euo pipefail
ROOT="/media/rootalkhatib/My Passport/reda_ws"
cd "$ROOT"
source asynchvla_ws/scripts/activate_simvla_bob.sh
export LIBERO_CONFIG_PATH="$ROOT/asynchvla_ws/configs/libero_pro_bob"
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl
export PYTHONPATH="$ROOT/asynchvla_ws/src:$PYTHONPATH"
python3 -m data_collection_stage9.validate_observation_signals --suites libero_object_with_mug libero_spatial_with_mug libero_goal_with_mug --tasks 0
python3 -m data_collection_stage9.validate_reset_determinism --suite libero_object_with_mug --task-id 0 --horizon 5
python3 -m data_collection_stage9.validate_controlled_actions --suite libero_object_with_mug --task-id 0 --horizon 10
