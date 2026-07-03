#!/usr/bin/env bash
set -e

# Load Bob SimVLA environment
REDA_WS="/media/rootalkhatib/My Passport/reda_ws"
source "${REDA_WS}/asynchvla_ws/scripts/activate_simvla_bob.sh"
export LIBERO_CONFIG_PATH="${REDA_WS}/asynchvla_ws/configs/libero_pro_bob"

# Add local src and LIBERO-PRO to PYTHONPATH
VIDEO_WS="${REDA_WS}/video_labeling_ws"
export PYTHONPATH="${VIDEO_WS}/src:${REDA_WS}/asynchvla_ws/src:${REDA_WS}/intern_ship_ws/assets/repos/LIBERO-PRO:${PYTHONPATH}"

# Rendering setup
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl

# Run generation
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
OUT_DIR="${VIDEO_WS}/failure_video_runs_${TIMESTAMP}"

LOG_FILE="${VIDEO_WS}/generation.log"
echo "Logging to ${LOG_FILE}"

python3 "${VIDEO_WS}/generate_failure_review_videos.py" \
    --suites libero_spatial_with_mug libero_object_with_mug libero_goal_with_mug libero_10_with_mug \
    --task-ids 0 1 2 3 4 5 6 7 8 9 \
    --target-failure-videos 30 \
    --max-attempts 500 \
    --max-steps 400 \
    --fps 10 \
    --out-dir "$OUT_DIR" >> "$LOG_FILE" 2>&1
