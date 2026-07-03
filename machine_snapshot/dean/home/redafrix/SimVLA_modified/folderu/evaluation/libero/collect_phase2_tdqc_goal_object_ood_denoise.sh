#!/usr/bin/env bash
set -euo pipefail

# Collect a held-out LIBERO-PRO goal_object OOD set with the current denoise
# uncertainty logging. Jobs are split by task_id and seed so a single problematic
# task does not discard an entire suite/seed run.

REPO_ROOT="${REPO_ROOT:-/home/redafrix/SimVLA_modified}"
EVAL_DIR="${EVAL_DIR:-${REPO_ROOT}/evaluation/libero}"
LIBERO_PRO_ROOT="${LIBERO_PRO_ROOT:-/home/redafrix/LIBERO-PRO}"

PORTS="${PORTS:-8111 8112 8113 8114 8115}"
MAX_PARALLEL="${MAX_PARALLEL:-5}"
SEEDS="${SEEDS:-509 521 547 563 587}"
NUM_TRIALS="${NUM_TRIALS:-10}"
TASK_IDS="${TASK_IDS:-0 1 2 3 4 5 6 7 8 9}"
NO_VIDEO="${NO_VIDEO:-true}"
REPLAN_STEPS="${REPLAN_STEPS:-5}"
FORCE_LIBERO_PRO_REGEN="${FORCE_LIBERO_PRO_REGEN:-false}"

RUN_NAME="${RUN_NAME:-phase2_tdqc_goal_object_ood_denoise_$(date +%Y%m%d_%H%M%S)}"
OUT_DIR="${OUT_DIR:-${EVAL_DIR}/eval_libero_pro/${RUN_NAME}}"
COMBINED_JSONL="${OUT_DIR}/combined_goal_object_ood.jsonl"
MASTER_LOG="${OUT_DIR}/run_goal_object_ood_collection.log"

read -r -a PORT_ARRAY <<< "${PORTS}"
if [ "${#PORT_ARRAY[@]}" -eq 0 ]; then
  echo "[ERROR] PORTS is empty." >&2
  exit 1
fi

mkdir -p "${OUT_DIR}"
cd "${EVAL_DIR}"

if [ -f "${HOME}/miniconda3/etc/profile.d/conda.sh" ]; then
  source "${HOME}/miniconda3/etc/profile.d/conda.sh"
elif [ -f "${HOME}/anaconda3/etc/profile.d/conda.sh" ]; then
  source "${HOME}/anaconda3/etc/profile.d/conda.sh"
else
  echo "[ERROR] Could not find conda.sh." | tee -a "${MASTER_LOG}"
  exit 1
fi

conda activate libero

if [ ! -x "./run_libero_pro_eval.sh" ]; then
  echo "[ERROR] ./run_libero_pro_eval.sh not found or not executable." | tee -a "${MASTER_LOG}"
  exit 1
fi

: > "${COMBINED_JSONL}"

echo "============================================================" | tee -a "${MASTER_LOG}"
echo "Phase 2 TDQC goal_object OOD denoise collection" | tee -a "${MASTER_LOG}"
echo "RUN_NAME=${RUN_NAME}" | tee -a "${MASTER_LOG}"
echo "OUT_DIR=${OUT_DIR}" | tee -a "${MASTER_LOG}"
echo "PORTS=${PORTS}" | tee -a "${MASTER_LOG}"
echo "MAX_PARALLEL=${MAX_PARALLEL}" | tee -a "${MASTER_LOG}"
echo "SEEDS=${SEEDS}" | tee -a "${MASTER_LOG}"
echo "TASK_IDS=${TASK_IDS}" | tee -a "${MASTER_LOG}"
echo "NUM_TRIALS=${NUM_TRIALS}" | tee -a "${MASTER_LOG}"
echo "Expected if all runnable: 10 tasks * 5 seeds * ${NUM_TRIALS} trials" | tee -a "${MASTER_LOG}"
echo "============================================================" | tee -a "${MASTER_LOG}"

run_one_eval() {
  local task_id="$1"
  local seed="$2"
  local port="$3"
  local out_jsonl="${OUT_DIR}/libero_goal_object_task${task_id}_seed${seed}_${NUM_TRIALS}trials.jsonl"
  local run_log="${OUT_DIR}/libero_goal_object_task${task_id}_seed${seed}_${NUM_TRIALS}trials.log"
  local status_file="${OUT_DIR}/libero_goal_object_task${task_id}_seed${seed}_${NUM_TRIALS}trials.status"

  {
    echo "============================================================"
    echo "Running suite=libero_goal_object, task_id=${task_id}, seed=${seed}, trials=${NUM_TRIALS}, port=${port}"
    echo "Output JSONL: ${out_jsonl}"
    echo "Run log:      ${run_log}"
    echo "============================================================"
  } >> "${MASTER_LOG}"

  rm -f "${out_jsonl}" "${status_file}"
  (
    set +e
    LIBERO_PRO_ROOT="${LIBERO_PRO_ROOT}" \
    FORCE_LIBERO_PRO_REGEN="${FORCE_LIBERO_PRO_REGEN}" \
    TASK_SUITE="libero_goal_object" \
    TASK_ID="${task_id}" \
    NUM_TRIALS="${NUM_TRIALS}" \
    SEED="${seed}" \
    PORT="${port}" \
    REPLAN_STEPS="${REPLAN_STEPS}" \
    NO_VIDEO="${NO_VIDEO}" \
    UNCERTAINTY_LOG="${out_jsonl}" \
    ./run_libero_pro_eval.sh > "${run_log}" 2>&1
    rc=$?
    echo "${rc}" > "${status_file}"
    exit 0
  ) &
}

active_jobs=0
job_idx=0
for seed in ${SEEDS}; do
  for task_id in ${TASK_IDS}; do
    port="${PORT_ARRAY[$((job_idx % ${#PORT_ARRAY[@]}))]}"
    run_one_eval "${task_id}" "${seed}" "${port}"
    active_jobs=$((active_jobs + 1))
    job_idx=$((job_idx + 1))
    if [ "${active_jobs}" -ge "${MAX_PARALLEL}" ]; then
      wait -n
      active_jobs=$((active_jobs - 1))
    fi
  done
done

wait

failed_jobs=0
empty_jobs=0
total_written=0
shopt -s nullglob
for status_file in "${OUT_DIR}"/*.status; do
  stem="${status_file%.status}"
  out_jsonl="${stem}.jsonl"
  run_log="${stem}.log"
  rc="$(cat "${status_file}")"
  if [ "${rc}" != "0" ]; then
    echo "[WARNING] Job returned rc=${rc}: ${stem}. Keeping any valid partial JSONL. See ${run_log}" | tee -a "${MASTER_LOG}"
    failed_jobs=$((failed_jobs + 1))
  fi
  if [ ! -s "${out_jsonl}" ]; then
    echo "[WARNING] No JSONL data was written: ${out_jsonl}. See ${run_log}" | tee -a "${MASTER_LOG}"
    empty_jobs=$((empty_jobs + 1))
    continue
  fi
  n_lines=$(wc -l < "${out_jsonl}")
  total_written=$((total_written + n_lines))
  echo "[MERGE] ${n_lines} rollout lines from ${out_jsonl}" | tee -a "${MASTER_LOG}"
  cat "${out_jsonl}" >> "${COMBINED_JSONL}"
done

python - "${COMBINED_JSONL}" "${MASTER_LOG}" <<'PY'
import json
import sys
from collections import Counter
from pathlib import Path

path = Path(sys.argv[1])
log_path = Path(sys.argv[2])
denoise_keys = [
    "denoise_initial_mean",
    "denoise_final_mean",
    "denoise_delta",
    "denoise_slope",
    "denoise_final_max",
    "denoise_spike",
    "denoise_final_gripper",
    "denoise_final_rotation_mean",
]
valid = bad = missing_denoise = 0
success = 0
by_task = Counter()
by_task_success = Counter()
with path.open("r", encoding="utf-8") as f:
    for line in f:
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
        except Exception:
            bad += 1
            continue
        trace = rec.get("uncertainty_trace") or []
        if not trace:
            bad += 1
            continue
        if any(k not in trace[0] or trace[0][k] is None for k in denoise_keys):
            missing_denoise += 1
            continue
        valid += 1
        s = bool(rec.get("success"))
        success += int(s)
        task_id = rec.get("task_id")
        by_task[task_id] += 1
        by_task_success[task_id] += int(s)

lines = [
    "",
    "Validation summary:",
    f"  valid episodes: {valid}",
    f"  success/failure: {success}/{valid - success}",
    f"  bad_or_empty_trace: {bad}",
    f"  missing_denoise: {missing_denoise}",
    "  by_task:",
]
for task_id in sorted(by_task, key=lambda x: int(x) if str(x).isdigit() else str(x)):
    n = by_task[task_id]
    s = by_task_success[task_id]
    lines.append(f"    task {task_id}: {n} episodes, {s}/{n} successes")
text = "\n".join(lines)
print(text)
with log_path.open("a", encoding="utf-8") as f:
    f.write(text + "\n")
PY

total_lines=$(wc -l < "${COMBINED_JSONL}" || echo "0")
echo "============================================================" | tee -a "${MASTER_LOG}"
echo "Goal-object OOD collection finished." | tee -a "${MASTER_LOG}"
echo "Raw merged rollout lines: ${total_written}" | tee -a "${MASTER_LOG}"
echo "Total combined lines: ${total_lines}" | tee -a "${MASTER_LOG}"
echo "Jobs with nonzero rc: ${failed_jobs}" | tee -a "${MASTER_LOG}"
echo "Empty jobs: ${empty_jobs}" | tee -a "${MASTER_LOG}"
echo "Combined JSONL: ${COMBINED_JSONL}" | tee -a "${MASTER_LOG}"
echo "============================================================" | tee -a "${MASTER_LOG}"
