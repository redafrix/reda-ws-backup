#!/bin/bash

# ==============================================================================
# 🚀 ETERNAL FIPER SWEEP DEPLOYMENT (12 SUITES) - FIXED V2
# ==============================================================================
# This script launches high-diversity data collection on Sam and Bob.
# It uses symlinks on Bob to bypass space-in-path issues.
# ==============================================================================

CAMPAIGN_NAME="fiper_sweep_eternal"
NUM_SWEEPS=1000000
ACE=8
TIMEOUT=300

echo "Deploying Eternal Campaign: ${CAMPAIGN_NAME}"

# ------------------------------------------------------------------------------
# 🛰 NODE 1: SAM (PCROBOTUBUNTU05)
# ------------------------------------------------------------------------------
echo "[SAM] Launching Mug and Milk Categories..."

SAM_REDA_WS="/home/rootalkhatib/test/reda_ws"
SAM_BASE="${SAM_REDA_WS}/asynchvla_ws"
SAM_DATA="${SAM_BASE}/stage9_libero_pro_risk_data/campaigns/${CAMPAIGN_NAME}"
SAM_PYTHON="/home/rootalkhatib/envs/simvla/bin/python"
SAM_CMD="export REDA_WS='${SAM_REDA_WS}' && \
         export PYTHONPATH=\"\${REDA_WS}/intern_ship_ws/assets/repos/LIBERO-PRO:${SAM_BASE}/src:\${PYTHONPATH}\" && \
         export MUJOCO_GL='egl' && export PYOPENGL_PLATFORM='egl' && \
         mkdir -p \"${SAM_DATA}/instance_A\" \"${SAM_DATA}/instance_B\""

# Sam Instance A: Mug
ssh sam "${SAM_CMD} && nohup ${SAM_PYTHON} -m data_collection_stage9.collect_fiper_receding_all_outcomes_v2 \
    --suites libero_spatial_with_mug libero_object_with_mug libero_goal_with_mug \
    --num-sweeps ${NUM_SWEEPS} --ace-candidates ${ACE} --max-timesteps ${TIMEOUT} \
    --out-dir \"${SAM_DATA}/instance_A\" > \"${SAM_DATA}/sam_mug.log\" 2>&1 &"

sleep 1

# Sam Instance B: Milk
ssh sam "${SAM_CMD} && nohup ${SAM_PYTHON} -m data_collection_stage9.collect_fiper_receding_all_outcomes_v2 \
    --suites libero_spatial_with_milk libero_10_with_milk libero_goal_with_milk \
    --num-sweeps ${NUM_SWEEPS} --ace-candidates ${ACE} --max-timesteps ${TIMEOUT} --env-seed 42 \
    --out-dir \"${SAM_DATA}/instance_B\" > \"${SAM_DATA}/sam_milk.log\" 2>&1 &"

# ------------------------------------------------------------------------------
# 🛰 NODE 2: BOB (PCROBOTUBUNTU02)
# ------------------------------------------------------------------------------
echo "[BOB] Launching Object and Env Perturbation Categories..."

# Ensure the root symlink exists
ssh pcrobot "ln -sfn \"/media/rootalkhatib/My Passport/reda_ws\" /tmp/bob_reda_ws"

BOB_REDA_WS="/tmp/bob_reda_ws"
BOB_BASE="/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws"
BOB_DATA="${BOB_BASE}/stage9_libero_pro_risk_data/campaigns/${CAMPAIGN_NAME}"
BOB_PYTHON="/usr/bin/python3"
BOB_CMD="export REDA_WS='${BOB_REDA_WS}' && \
         export LIBERO_PRO_PATH='/tmp/bob_libero_pro' && \
         export SITE_PACKAGES='/tmp/bob_site_packages' && \
         export SRC_PATH='/tmp/bob_src' && \
         export SIMVLA_PATH='/tmp/bob_simvla' && \
         export PYTHONPATH=\"\${SIMVLA_PATH}:\${LIBERO_PRO_PATH}:\${SRC_PATH}:\${SITE_PACKAGES}:\${PYTHONPATH}\" && \
         export MUJOCO_GL='egl' && export PYOPENGL_PLATFORM='egl' && \
         mkdir -p \"${BOB_DATA}/instance_A\" \"${BOB_DATA}/instance_B\""

# Bob Instance A: Object Perturbations
ssh pcrobot "${BOB_CMD} && cd /tmp/bob_src && nohup ${BOB_PYTHON} -m data_collection_stage9.collect_fiper_receding_all_outcomes_v2 \
    --suites libero_spatial_object libero_object_object libero_goal_object \
    --num-sweeps ${NUM_SWEEPS} --ace-candidates ${ACE} --max-timesteps ${TIMEOUT} \
    --out-dir \"${BOB_DATA}/instance_A\" > \"${BOB_DATA}/bob_obj.log\" 2>&1 &"

sleep 1

# Bob Instance B: Env Perturbations
ssh pcrobot "${BOB_CMD} && cd /tmp/bob_src && nohup ${BOB_PYTHON} -m data_collection_stage9.collect_fiper_receding_all_outcomes_v2 \
    --suites libero_spatial_env libero_object_env libero_goal_env \
    --num-sweeps ${NUM_SWEEPS} --ace-candidates ${ACE} --max-timesteps ${TIMEOUT} --env-seed 123 \
    --out-dir \"${BOB_DATA}/instance_B\" > \"${BOB_DATA}/bob_env.log\" 2>&1 &"

echo "=============================================================================="
echo "✅ Eternal Deployment Triggered."
echo "Sam Mug Log: ${SAM_DATA}/sam_mug.log"
echo "Sam Milk Log: ${SAM_DATA}/sam_milk.log"
echo "Bob Obj Log: ${BOB_DATA}/bob_obj.log"
echo "Bob Env Log: ${BOB_DATA}/bob_env.log"
echo "=============================================================================="
