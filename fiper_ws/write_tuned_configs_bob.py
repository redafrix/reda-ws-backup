import json
from pathlib import Path

# Paths on Bob
balanced_path = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/configs/conservative_topk8_midrange_pilot_20260605_bob_task7_03_topk8_balanced.json"

with open(balanced_path) as f:
    cfg = json.load(f)

# Modify basic fields
cfg["experiment_id"] = "tuned_topk8_pilot_20260605"

# 04_topk8_moderate_active
cfg_mod = cfg.copy()
cfg_mod["stage_name"] = "04_topk8_moderate_active"
cfg_mod["variant_name"] = "04_topk8_moderate_active"
cfg_mod["selection_min_high_risk_streak"] = 2
cfg_mod["selection_min_margin"] = 0.05
cfg_mod["selection_strong_margin"] = 0.08
cfg_mod["selection_require_candidate_below_q95"] = False
cfg_mod["selection_max_modifications_per_episode"] = 2
cfg_mod["output_dir"] = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/runs/tuned_topk8_pilot_20260605_bob_task7/04_topk8_moderate_active"

with open("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/configs/tuned_topk8_pilot_20260605_bob_task7_04_topk8_moderate_active.json", "w") as f:
    json.dump(cfg_mod, f, indent=2)

# 05_topk8_highly_active
cfg_act = cfg.copy()
cfg_act["stage_name"] = "05_topk8_highly_active"
cfg_act["variant_name"] = "05_topk8_highly_active"
cfg_act["selection_min_high_risk_streak"] = 1
cfg_act["selection_min_margin"] = 0.05
cfg_act["selection_strong_margin"] = 0.08
cfg_act["selection_require_candidate_below_q95"] = False
cfg_act["selection_max_modifications_per_episode"] = 5
cfg_act["output_dir"] = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/runs/tuned_topk8_pilot_20260605_bob_task7/05_topk8_highly_active"

with open("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/configs/tuned_topk8_pilot_20260605_bob_task7_05_topk8_highly_active.json", "w") as f:
    json.dump(cfg_act, f, indent=2)

print("Created tuned config files on Bob.")

# Write launch script for Bob
launch_script_content = """#!/usr/bin/env bash
set -euo pipefail
source "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/activate_simvla_bob.sh"
export TOKENIZERS_PARALLELISM=false
export USE_TF=0 TRANSFORMERS_NO_TF=1 USE_FLAX=0
export MUJOCO_GL=egl PYOPENGL_PLATFORM=egl PYTHONUNBUFFERED=1
export NVIDIA_TF32_OVERRIDE=0 CUBLAS_WORKSPACE_CONFIG=:4096:8

RUN_DIR="/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/runs/tuned_topk8_pilot_20260605_bob_task7"
mkdir -p "$RUN_DIR/logs"
STATUS="$RUN_DIR/sequential_status.jsonl"
: > "$STATUS"

# Stage 04_topk8_moderate_active
printf '{"time":"%s","stage":"04_topk8_moderate_active","event":"start"}\\n' "$(date -Is)" >> "$STATUS"
set +e
"/usr/bin/python3" "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/scripts/run_dean_uncertainty_realtime_policy_v1.py" \\
  --config "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/configs/tuned_topk8_pilot_20260605_bob_task7_04_topk8_moderate_active.json" \\
  --policy risk_unc_topk8 --num-episodes 12 > "$RUN_DIR/logs/04_topk8_moderate_active.log" 2>&1
code=$?
set -e
printf '{"time":"%s","stage":"04_topk8_moderate_active","event":"end","code":%s}\\n' "$(date -Is)" "$code" >> "$STATUS"
if [[ "$code" -ne 0 ]]; then exit "$code"; fi

# Stage 05_topk8_highly_active
printf '{"time":"%s","stage":"05_topk8_highly_active","event":"start"}\\n' "$(date -Is)" >> "$STATUS"
set +e
"/usr/bin/python3" "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/scripts/run_dean_uncertainty_realtime_policy_v1.py" \\
  --config "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/configs/tuned_topk8_pilot_20260605_bob_task7_05_topk8_highly_active.json" \\
  --policy risk_unc_topk8 --num-episodes 12 > "$RUN_DIR/logs/05_topk8_highly_active.log" 2>&1
code=$?
set -e
printf '{"time":"%s","stage":"05_topk8_highly_active","event":"end","code":%s}\\n' "$(date -Is)" "$code" >> "$STATUS"
if [[ "$code" -ne 0 ]]; then exit "$code"; fi

printf '{"time":"%s","event":"all_done"}\\n' "$(date -Is)" >> "$STATUS"
"""

launch_path = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/scripts/launch_tuned_topk8_pilot_20260605_bob.sh")
launch_path.write_text(launch_script_content)
launch_path.chmod(0o755)
print("Created launch script on Bob and made it executable.")
