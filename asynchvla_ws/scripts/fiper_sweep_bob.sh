#!/bin/bash

# Configuration
CAMPAIGN_NAME="fiper_sweep_20260522"
BASE_DIR="/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws"
DATA_DIR="${BASE_DIR}/stage9_libero_pro_risk_data/campaigns/${CAMPAIGN_NAME}"
PYTHON="/usr/bin/python3"
export REDA_WS="/media/rootalkhatib/My Passport/reda_ws"

# Environment - Using Symlinks to avoid space issues
export LIBERO_PRO_PATH="/tmp/bob_libero_pro"
export SITE_PACKAGES="/tmp/bob_site_packages"
export SRC_PATH="/tmp/bob_src"

export SIMVLA_PATH="/tmp/bob_simvla"
export PYTHONPATH="${SIMVLA_PATH}:${LIBERO_PRO_PATH}:${SRC_PATH}:${SITE_PACKAGES}:${PYTHONPATH}"
export MUJOCO_GL="egl"
export PYOPENGL_PLATFORM="egl"

mkdir -p "${DATA_DIR}/instance_A"
mkdir -p "${DATA_DIR}/instance_B"

cd "${SRC_PATH}"

# Instance A: Object Perturbations
nohup "${PYTHON}" -m data_collection_stage9.collect_fiper_receding_all_outcomes_v2 \
    --suites libero_spatial_object libero_object_object libero_goal_object \
    --task-ids 0 1 2 3 4 5 6 7 8 9 \
    --num-sweeps 100 \
    --ace-candidates 8 \
    --max-timesteps 300 \
    --out-dir "${DATA_DIR}/instance_A" \
    > "${DATA_DIR}/instance_A.log" 2>&1 &
echo "Launched Bob Instance A (Object) with PID $!"

# Instance B: Env Perturbations
nohup "${PYTHON}" -m data_collection_stage9.collect_fiper_receding_all_outcomes_v2 \
    --suites libero_spatial_env libero_object_env libero_goal_env \
    --task-ids 0 1 2 3 4 5 6 7 8 9 \
    --num-sweeps 100 \
    --ace-candidates 8 \
    --max-timesteps 300 \
    --env-seed 123 \
    --out-dir "${DATA_DIR}/instance_B" \
    > "${DATA_DIR}/instance_B.log" 2>&1 &
echo "Launched Bob Instance B (Env) with PID $!"
