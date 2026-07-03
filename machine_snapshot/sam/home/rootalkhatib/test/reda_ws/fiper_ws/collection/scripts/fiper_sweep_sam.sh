#!/bin/bash

# Configuration
CAMPAIGN_NAME="fiper_sweep_20260522"
BASE_DIR="/home/rootalkhatib/test/reda_ws/asynchvla_ws"
DATA_DIR="${BASE_DIR}/stage9_libero_pro_risk_data/campaigns/${CAMPAIGN_NAME}"
PYTHON="/home/rootalkhatib/envs/simvla/bin/python"

# Environment
export REDA_WS="/home/rootalkhatib/test/reda_ws"
export PYTHONPATH="${REDA_WS}/intern_ship_ws/assets/repos/LIBERO-PRO:${BASE_DIR}/src:${PYTHONPATH}"
export MUJOCO_GL="egl"
export PYOPENGL_PLATFORM="egl"

mkdir -p "${DATA_DIR}/instance_A"
mkdir -p "${DATA_DIR}/instance_B"

# Instance A: Mug Suites
nohup ${PYTHON} -m data_collection_stage9.collect_fiper_receding_all_outcomes_v2 \
    --suites libero_spatial_with_mug libero_object_with_mug libero_goal_with_mug \
    --task-ids 0 1 2 3 4 5 6 7 8 9 \
    --num-sweeps 100 \
    --ace-candidates 8 \
    --max-timesteps 300 \
    --out-dir "${DATA_DIR}/instance_A" \
    > "${DATA_DIR}/instance_A.log" 2>&1 &
echo "Launched Sam Instance A (Mug) with PID $!"

# Instance B: Milk Suites
nohup ${PYTHON} -m data_collection_stage9.collect_fiper_receding_all_outcomes_v2 \
    --suites libero_spatial_with_milk libero_object_with_milk libero_goal_with_milk \
    --task-ids 0 1 2 3 4 5 6 7 8 9 \
    --num-sweeps 100 \
    --ace-candidates 8 \
    --max-timesteps 300 \
    --env-seed 42 \
    --out-dir "${DATA_DIR}/instance_B" \
    > "${DATA_DIR}/instance_B.log" 2>&1 &
echo "Launched Sam Instance B (Milk) with PID $!"
