#!/usr/bin/env bash
set -euo pipefail

# Collect only rollout cells missing from
# phase2_tdqc_raw_pro_4000_20260428_171248.
#
# Missing cells found from the original manifest:
# - libero_goal_object: tasks 0..9, seeds 17/19/46
# - libero_10_object: task 4, seeds 17/19/46
#
# Outputs are intentionally written to a fresh run directory so this remains an
# uncontaminated zero-shot evaluation set.

REPO_ROOT="${REPO_ROOT:-/home/redafrix/SimVLA_modified}"
EVAL_DIR="${EVAL_DIR:-${REPO_ROOT}/evaluation/libero}"
LIBERO_PRO_ROOT="${LIBERO_PRO_ROOT:-/home/redafrix/LIBERO-PRO}"

PORTS="${PORTS:-8103 8104 8105 8106 8107}"
NO_VIDEO="${NO_VIDEO:-true}"
SEEDS="${SEEDS:-17 19 46}"
NUM_TRIALS="${NUM_TRIALS:-12}"

read -r -a PORT_ARRAY <<< "${PORTS}"
if [ "${#PORT_ARRAY[@]}" -eq 0 ]; then
  echo "[ERROR] PORTS is empty." >&2
  exit 1
fi
MAX_PARALLEL="${MAX_PARALLEL:-${#PORT_ARRAY[@]}}"

RUN_NAME="${RUN_NAME:-phase2_tdqc_raw_pro_missing_$(date +%Y%m%d_%H%M%S)}"
OUT_DIR="${OUT_DIR:-${EVAL_DIR}/eval_libero_pro/${RUN_NAME}}"
COMBINED_JSONL="${OUT_DIR}/combined_missing_cells.jsonl"
MASTER_LOG="${OUT_DIR}/run_missing_collection.log"

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
echo "Phase 2 TDQC missing-cell LIBERO-PRO collection" | tee -a "${MASTER_LOG}"
echo "RUN_NAME=${RUN_NAME}" | tee -a "${MASTER_LOG}"
echo "OUT_DIR=${OUT_DIR}" | tee -a "${MASTER_LOG}"
echo "PORTS=${PORTS}" | tee -a "${MASTER_LOG}"
echo "MAX_PARALLEL=${MAX_PARALLEL}" | tee -a "${MASTER_LOG}"
echo "SEEDS=${SEEDS}" | tee -a "${MASTER_LOG}"
echo "NUM_TRIALS=${NUM_TRIALS}" | tee -a "${MASTER_LOG}"
echo "Expected if all runnable: 33 task/seed jobs * ${NUM_TRIALS} = 396 trajectories" | tee -a "${MASTER_LOG}"
echo "============================================================" | tee -a "${MASTER_LOG}"

run_one_eval() {
  local suite="$1"
  local task_id="$2"
  local seed="$3"
  local port="$4"
  local out_jsonl="${OUT_DIR}/${suite}_task${task_id}_seed${seed}_${NUM_TRIALS}trials.jsonl"
  local run_log="${OUT_DIR}/${suite}_task${task_id}_seed${seed}_${NUM_TRIALS}trials.log"
  local status_file="${OUT_DIR}/${suite}_task${task_id}_seed${seed}_${NUM_TRIALS}trials.status"

  {
    echo "============================================================"
    echo "Running suite=${suite}, task_id=${task_id}, seed=${seed}, trials=${NUM_TRIALS}, port=${port}"
    echo "Output JSONL: ${out_jsonl}"
    echo "Run log:      ${run_log}"
    echo "============================================================"
  } >> "${MASTER_LOG}"

  rm -f "${out_jsonl}" "${status_file}"
  (
    set +e
    LIBERO_PRO_ROOT="${LIBERO_PRO_ROOT}" \
    TASK_SUITE="${suite}" \
    TASK_ID="${task_id}" \
    NUM_TRIALS="${NUM_TRIALS}" \
    SEED="${seed}" \
    PORT="${port}" \
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
  for task_id in 0 1 2 3 4 5 6 7 8 9; do
    port="${PORT_ARRAY[$((job_idx % ${#PORT_ARRAY[@]}))]}"
    run_one_eval "libero_goal_object" "${task_id}" "${seed}" "${port}"
    active_jobs=$((active_jobs + 1))
    job_idx=$((job_idx + 1))
    if [ "${active_jobs}" -ge "${MAX_PARALLEL}" ]; then
      wait -n
      active_jobs=$((active_jobs - 1))
    fi
  done
done

for seed in ${SEEDS}; do
  port="${PORT_ARRAY[$((job_idx % ${#PORT_ARRAY[@]}))]}"
  run_one_eval "libero_10_object" "4" "${seed}" "${port}"
  active_jobs=$((active_jobs + 1))
  job_idx=$((job_idx + 1))
  if [ "${active_jobs}" -ge "${MAX_PARALLEL}" ]; then
    wait -n
    active_jobs=$((active_jobs - 1))
  fi
done

wait

failed_jobs=0
total_written=0
shopt -s nullglob
for status_file in "${OUT_DIR}"/*.status; do
  stem="${status_file%.status}"
  out_jsonl="${stem}.jsonl"
  run_log="${stem}.log"
  rc="$(cat "${status_file}")"
  if [ "${rc}" != "0" ]; then
    echo "[WARNING] Job failed: ${stem}, rc=${rc}. See ${run_log}" | tee -a "${MASTER_LOG}"
    failed_jobs=$((failed_jobs + 1))
    continue
  fi
  if [ ! -s "${out_jsonl}" ]; then
    echo "[WARNING] No JSONL data was written: ${out_jsonl}. See ${run_log}" | tee -a "${MASTER_LOG}"
    failed_jobs=$((failed_jobs + 1))
    continue
  fi
  n_lines=$(wc -l < "${out_jsonl}")
  total_written=$((total_written + n_lines))
  echo "[OK] Wrote ${n_lines} rollout lines to ${out_jsonl}" | tee -a "${MASTER_LOG}"
  cat "${out_jsonl}" >> "${COMBINED_JSONL}"
done

total_lines=$(wc -l < "${COMBINED_JSONL}" || echo "0")
echo "============================================================" | tee -a "${MASTER_LOG}"
echo "Missing-cell collection finished." | tee -a "${MASTER_LOG}"
echo "Successful rollout lines merged: ${total_written}" | tee -a "${MASTER_LOG}"
echo "Total combined rollout lines: ${total_lines}" | tee -a "${MASTER_LOG}"
echo "Failed jobs: ${failed_jobs}" | tee -a "${MASTER_LOG}"
echo "Combined JSONL: ${COMBINED_JSONL}" | tee -a "${MASTER_LOG}"
echo "============================================================" | tee -a "${MASTER_LOG}"
