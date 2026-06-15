#!/bin/bash
# Bob FIPER Receding All-Outcomes Campaign Launcher
# Uses the validated environment from activate_simvla_bob.sh

REDA_WS="/media/rootalkhatib/My Passport/reda_ws"
ASYNCHVLA_WS="$REDA_WS/asynchvla_ws"
PYTHON_BIN="/usr/bin/python3"
SIMVLA_ENV_ROOT="/home/rootalkhatib/envs/simvla"
SIMVLA_SITE_PACKAGES="$SIMVLA_ENV_ROOT/lib/python3.10/site-packages"

LOG_DIR="$ASYNCHVLA_WS/logs"
CAMPAIGN_ID="fiper_receding_all_outcomes_bob_$(date +%Y%m%d_%H%M%S)"
DATA_ROOT="$ASYNCHVLA_WS/stage9_libero_pro_risk_data/campaigns/$CAMPAIGN_ID"

mkdir -p "$LOG_DIR"
mkdir -p "$DATA_ROOT/instance_A"
mkdir -p "$DATA_ROOT/instance_B"
mkdir -p "$DATA_ROOT/reports"

# Environment Setup
export REDA_WS="$REDA_WS"
export ASYNCVLA_WS="$ASYNCHVLA_WS"
export SIMVLA_ENV_ROOT="$SIMVLA_ENV_ROOT"
export SIMVLA_SITE_PACKAGES="$SIMVLA_SITE_PACKAGES"
export PYTHONNOUSERSITE=1
export PYTHONPATH="$ASYNCHVLA_WS/src:$SIMVLA_SITE_PACKAGES:$REDA_WS/intern_ship_ws/simvla/code/SimVLA_modified:$REDA_WS/intern_ship_ws/assets/data/LIBERO:$PYTHONPATH"
export LIBERO_CONFIG_PATH="$REDA_WS/intern_ship_ws/simvla/config/libero"
export HF_HOME="$REDA_WS/intern_ship_ws/assets/models/huggingface/.hf_home"

cd "$ASYNCHVLA_WS"

echo "Launching Bob Campaign: $CAMPAIGN_ID"

# Instance A: Spatial + Object (Tasks 0-9)
nohup $PYTHON_BIN -m src.data_collection_stage9.collect_fiper_receding_all_outcomes_v1 \
    --suites libero_spatial_with_mug libero_object_with_mug \
    --task-ids 0 1 2 3 4 5 6 7 8 9 \
    --max-episodes-per-task 200 \
    --max-timesteps 400 \
    --ace-candidates 64 \
    --env-seed 1337 \
    --out-dir "$DATA_ROOT/instance_A" > "$LOG_DIR/instance_A.log" 2>&1 &
PID_A=$!

# Instance B: Goal (Tasks 0-9)
nohup $PYTHON_BIN -m src.data_collection_stage9.collect_fiper_receding_all_outcomes_v1 \
    --suites libero_goal_with_mug \
    --task-ids 0 1 2 3 4 5 6 7 8 9 \
    --max-episodes-per-task 200 \
    --max-timesteps 400 \
    --ace-candidates 64 \
    --env-seed 4242 \
    --out-dir "$DATA_ROOT/instance_B" > "$LOG_DIR/instance_B.log" 2>&1 &
PID_B=$!

echo "Instance A PID: $PID_A"
echo "Instance B PID: $PID_B"
echo "Logs: $LOG_DIR"
echo "Data: $DATA_ROOT"

# Manifest
echo "{\"campaign_id\": \"$CAMPAIGN_ID\", \"instance_a_pid\": $PID_A, \"instance_b_pid\": $PID_B, \"data_root\": \"$DATA_ROOT\"}" > "$DATA_ROOT/MANIFEST.json"

# Status script
cat << EOS > "$ASYNCHVLA_WS/scripts/fiper_campaign_bob/status.sh"
#!/bin/bash
echo "Checking Bob PIDs..."
ps -p $PID_A $PID_B
echo "Checking logs tail..."
tail -n 20 "$LOG_DIR/instance_A.log" "$LOG_DIR/instance_B.log"
echo "Disk usage:"
df -h "$DATA_ROOT"
EOS
chmod +x "$ASYNCHVLA_WS/scripts/fiper_campaign_bob/status.sh"

# Stop script
cat << EOS > "$ASYNCHVLA_WS/scripts/fiper_campaign_bob/stop.sh"
#!/bin/bash
echo "Stopping Bob instances $PID_A $PID_B"
kill $PID_A $PID_B
EOS
chmod +x "$ASYNCHVLA_WS/scripts/fiper_campaign_bob/stop.sh"
