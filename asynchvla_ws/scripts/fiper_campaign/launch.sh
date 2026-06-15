#!/bin/bash
CAMPAIGN_ID="fiper_receding_all_outcomes_$(date +%Y%m%d_%H%M%S)"
CAMPAIGN_ROOT="/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/$CAMPAIGN_ID"

mkdir -p "$CAMPAIGN_ROOT/scripts"
mkdir -p "$CAMPAIGN_ROOT/logs"
mkdir -p "$CAMPAIGN_ROOT/reports"
mkdir -p "$CAMPAIGN_ROOT/data/instance_A"
mkdir -p "$CAMPAIGN_ROOT/data/instance_B"

PYTHON_PATH="/home/rootalkhatib/envs/simvla/bin/python"
export REDA_WS="/home/rootalkhatib/test/reda_ws"

echo "Stopping old campaigns on Sam..."
pkill -f "collect_continuous_risk_dataset_v2.py"
pkill -f "collect_dense_failure_timestep_mining_v2.py"
pkill -f "collect_fiper_receding_all_outcomes_v1"

# CD to asynchvla_ws so that src is a package
cd /home/rootalkhatib/test/reda_ws/asynchvla_ws
export PYTHONPATH="$PWD:$PYTHONPATH"

echo "Launching Instance A (Spatial/Object)..."
nohup $PYTHON_PATH -m src.data_collection_stage9.collect_fiper_receding_all_outcomes_v1 \
    --suites libero_spatial_with_mug libero_object_with_mug \
    --task-ids 0 1 2 3 4 5 6 7 8 9 \
    --max-episodes-per-task 200 \
    --max-timesteps 400 \
    --ace-candidates 64 \
    --save-images \
    --out-dir "$CAMPAIGN_ROOT/data/instance_A" \
    > "$CAMPAIGN_ROOT/logs/instance_A.log" 2>&1 &
PID_A=$!

echo "Launching Instance B (Goal)..."
nohup $PYTHON_PATH -m src.data_collection_stage9.collect_fiper_receding_all_outcomes_v1 \
    --suites libero_goal_with_mug \
    --task-ids 0 1 2 3 4 5 6 7 8 9 \
    --max-episodes-per-task 200 \
    --max-timesteps 400 \
    --ace-candidates 64 \
    --save-images \
    --out-dir "$CAMPAIGN_ROOT/data/instance_B" \
    > "$CAMPAIGN_ROOT/logs/instance_B.log" 2>&1 &
PID_B=$!

echo "Campaign $CAMPAIGN_ID launched."
echo "Instance A PID: $PID_A"
echo "Instance B PID: $PID_B"

echo "instance_a_pid=$PID_A" > "$CAMPAIGN_ROOT/MANIFEST.env"
echo "instance_b_pid=$PID_B" >> "$CAMPAIGN_ROOT/MANIFEST.env"
echo "campaign_id=$CAMPAIGN_ID" >> "$CAMPAIGN_ROOT/MANIFEST.env"
echo "campaign_root=$CAMPAIGN_ROOT" >> "$CAMPAIGN_ROOT/MANIFEST.env"

cat << 'EOT' > "$CAMPAIGN_ROOT/scripts/status.sh"
#!/bin/bash
echo "--- Instance A Log (tail) ---"
tail -n 20 "$(dirname "$0")/../logs/instance_A.log"
echo "--- Instance B Log (tail) ---"
tail -n 20 "$(dirname "$0")/../logs/instance_B.log"
echo "--- GPU Status ---"
nvidia-smi
EOT
chmod +x "$CAMPAIGN_ROOT/scripts/status.sh"

cat << 'EOT' > "$CAMPAIGN_ROOT/scripts/stop.sh"
#!/bin/bash
source "$(dirname "$0")/../MANIFEST.env"
echo "Stopping PID $instance_a_pid and $instance_b_pid..."
kill $instance_a_pid $instance_b_pid
pkill -f "collect_fiper_receding_all_outcomes_v1"
EOT
chmod +x "$CAMPAIGN_ROOT/scripts/stop.sh"

