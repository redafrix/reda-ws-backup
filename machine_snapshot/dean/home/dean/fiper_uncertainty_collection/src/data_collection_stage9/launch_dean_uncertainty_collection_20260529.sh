#!/usr/bin/env bash
set -euo pipefail

SESSION="dean_fiper_uncertainty_20260529"
BASE="/home/dean/fiper_uncertainty_collection"
SRC="${BASE}/src/data_collection_stage9"
RUN_ROOT="${BASE}/runs/dean_object_uncertainty_20260529"
PY="/home/redafrix/miniconda3/envs/simvla/bin/python"
SCRIPT="${SRC}/collect_fiper_uncertainty_receding_dean_v1.py"
SHA="3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71"
WORKERS=4

if tmux has-session -t "${SESSION}" 2>/dev/null; then
  echo "ERROR: tmux session already exists: ${SESSION}" >&2
  exit 2
fi

if pgrep -af "collect_fiper_uncertainty_receding_dean_v1.py" >/dev/null; then
  echo "ERROR: existing Dean uncertainty collector process is already running" >&2
  pgrep -af "collect_fiper_uncertainty_receding_dean_v1.py" >&2
  exit 3
fi

mkdir -p "${RUN_ROOT}/logs"

make_cmd() {
  local worker_index="$1"
  local worker_id="dean_w${worker_index}"
  local out_dir="${RUN_ROOT}/worker_${worker_index}"
  local log_path="${RUN_ROOT}/logs/worker_${worker_index}.log"
  cat <<CMD
cd "${SRC}" && \
export PYTHONPATH="${SRC}:/home/redafrix/LIBERO-PRO:/home/redafrix/SimVLA_modified" && \
export MUJOCO_GL=egl && \
export PYOPENGL_PLATFORM=egl && \
export USE_TF=0 && \
export TRANSFORMERS_NO_TF=1 && \
export USE_FLAX=0 && \
export TOKENIZERS_PARALLELISM=false && \
"${PY}" "${SCRIPT}" \
  --out-dir "${out_dir}" \
  --suites libero_spatial_object libero_object_object libero_goal_object libero_10_object libero_90 \
  --num-sweeps 1000000 \
  --max-timesteps 300 \
  --ace-candidates 8 \
  --worker-id "${worker_id}" \
  --worker-shard-index "${worker_index}" \
  --worker-shard-count "${WORKERS}" \
  --global-action-seed 2026052900 \
  --expected-checkpoint-sha256 "${SHA}" \
  --resume \
  > "${log_path}" 2>&1
CMD
}

tmux new-session -d -s "${SESSION}" -n worker_0 "$(make_cmd 0)"
for i in 1 2 3; do
  tmux new-window -t "${SESSION}" -n "worker_${i}" "$(make_cmd "${i}")"
done

cat > "${RUN_ROOT}/launch_manifest.json" <<JSON
{
  "schema_version": "dean_uncertainty_collection_launch_v1",
  "session": "${SESSION}",
  "run_root": "${RUN_ROOT}",
  "workers": ${WORKERS},
  "suites": ["libero_spatial_object", "libero_object_object", "libero_goal_object", "libero_10_object", "libero_90"],
  "excluded_suites": ["libero_100"],
  "ace_candidates": 8,
  "max_timesteps": 300,
  "checkpoint_sha256": "${SHA}",
  "launch_time": "$(date --iso-8601=seconds)"
}
JSON

tmux ls
echo "LAUNCHED ${SESSION}"
