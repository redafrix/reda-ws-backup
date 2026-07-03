import json
from pathlib import Path

# Files on Dean (we will read it and write the new ones)
balanced_config_path = "/home/dean/fiper_uncertainty_collection/realtime_deployment/configs/conservative_topk8_midrange_pilot_20260605_dean_task8_03_topk8_balanced.json"

# We will write the python script to run on Dean to generate these configs
setup_remote_script = """import json
from pathlib import Path

balanced_path = "/home/dean/fiper_uncertainty_collection/realtime_deployment/configs/conservative_topk8_midrange_pilot_20260605_dean_task8_03_topk8_balanced.json"
with open(balanced_path) as f:
    cfg = json.load(f)

# Modify basic fields
cfg["experiment_id"] = "tuned_topk8_pilot_20260605"

# 04_topk8_moderate
cfg_mod = cfg.copy()
cfg_mod["stage_name"] = "04_topk8_moderate"
cfg_mod["variant_name"] = "04_topk8_moderate"
cfg_mod["selection_min_high_risk_streak"] = 2
cfg_mod["selection_min_margin"] = 0.08
cfg_mod["selection_strong_margin"] = 0.12
cfg_mod["selection_require_candidate_below_q95"] = False
cfg_mod["selection_max_modifications_per_episode"] = 2
cfg_mod["output_dir"] = "/home/dean/fiper_uncertainty_collection/realtime_deployment/runs/tuned_topk8_pilot_20260605_dean_task8/04_topk8_moderate"

with open("/home/dean/fiper_uncertainty_collection/realtime_deployment/configs/tuned_topk8_pilot_20260605_dean_task8_04_topk8_moderate.json", "w") as f:
    json.dump(cfg_mod, f, indent=2)

# 05_topk8_active
cfg_act = cfg.copy()
cfg_act["stage_name"] = "05_topk8_active"
cfg_act["variant_name"] = "05_topk8_active"
cfg_act["selection_min_high_risk_streak"] = 1
cfg_act["selection_min_margin"] = 0.08
cfg_act["selection_strong_margin"] = 0.12
cfg_act["selection_require_candidate_below_q95"] = False
cfg_act["selection_max_modifications_per_episode"] = 2
cfg_act["output_dir"] = "/home/dean/fiper_uncertainty_collection/realtime_deployment/runs/tuned_topk8_pilot_20260605_dean_task8/05_topk8_active"

with open("/home/dean/fiper_uncertainty_collection/realtime_deployment/configs/tuned_topk8_pilot_20260605_dean_task8_05_topk8_active.json", "w") as f:
    json.dump(cfg_act, f, indent=2)

print("Created tuned config files on Dean.")
"""

# Let's write the launch script content that will run on Dean
launch_script_content = """#!/usr/bin/env bash
set -euo pipefail

export TOKENIZERS_PARALLELISM=false
export USE_TF=0 TRANSFORMERS_NO_TF=1 USE_FLAX=0
export MUJOCO_GL=egl PYOPENGL_PLATFORM=egl PYTHONUNBUFFERED=1
export NVIDIA_TF32_OVERRIDE=0 CUBLAS_WORKSPACE_CONFIG=:4096:8

RUN_DIR="/home/dean/fiper_uncertainty_collection/realtime_deployment/runs/tuned_topk8_pilot_20260605_dean_task8"
mkdir -p "$RUN_DIR/logs"
STATUS="$RUN_DIR/sequential_status.jsonl"
: > "$STATUS"

if pgrep -af 'run_dean_uncertainty_realtime_policy_v1.py' | grep -v grep | grep -v "$$" >/dev/null; then
  echo 'conflicting realtime runner already active' >&2
  pgrep -af 'run_dean_uncertainty_realtime_policy_v1.py' >&2
  exit 2
fi

# Stage 04_topk8_moderate
printf '{"time":"%s","stage":"04_topk8_moderate","event":"start"}\\n' "$(date -Is)" >> "$STATUS"
set +e
"/home/redafrix/miniconda3/envs/simvla/bin/python" "/home/dean/fiper_uncertainty_collection/realtime_deployment/scripts/run_dean_uncertainty_realtime_policy_v1.py" \\
  --config "/home/dean/fiper_uncertainty_collection/realtime_deployment/configs/tuned_topk8_pilot_20260605_dean_task8_04_topk8_moderate.json" \\
  --policy risk_unc_topk8 --num-episodes 12 > "$RUN_DIR/logs/04_topk8_moderate.log" 2>&1
code=$?
set -e
printf '{"time":"%s","stage":"04_topk8_moderate","event":"end","code":%s}\\n' "$(date -Is)" "$code" >> "$STATUS"
if [[ "$code" -ne 0 ]]; then exit "$code"; fi

# Stage 05_topk8_active
printf '{"time":"%s","stage":"05_topk8_active","event":"start"}\\n' "$(date -Is)" >> "$STATUS"
set +e
"/home/redafrix/miniconda3/envs/simvla/bin/python" "/home/dean/fiper_uncertainty_collection/realtime_deployment/scripts/run_dean_uncertainty_realtime_policy_v1.py" \\
  --config "/home/dean/fiper_uncertainty_collection/realtime_deployment/configs/tuned_topk8_pilot_20260605_dean_task8_05_topk8_active.json" \\
  --policy risk_unc_topk8 --num-episodes 12 > "$RUN_DIR/logs/05_topk8_active.log" 2>&1
code=$?
set -e
printf '{"time":"%s","stage":"05_topk8_active","event":"end","code":%s}\\n' "$(date -Is)" "$code" >> "$STATUS"
if [[ "$code" -ne 0 ]]; then exit "$code"; fi

printf '{"time":"%s","event":"all_done"}\\n' "$(date -Is)" >> "$STATUS"
print "Tuned pilot sweep finished successfully!"
"""
