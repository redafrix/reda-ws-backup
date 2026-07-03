#!/usr/bin/env bash
set -euo pipefail

# ============================================================
# Phase 2 TDQC rollout collection for SimVLA uncertainty traces
# ============================================================
#
# This script assumes:
# - One or more SimVLA servers are already running.
# - Each server listens on one port from PORTS.
# - You are using LIBERO-PRO at /home/redafrix/LIBERO-PRO.
# - run_libero_pro_eval.sh already works.
#
# It distributes suite/seed jobs across the available ports so
# you only need one client launcher even when evaluating in
# parallel.
#
# ============================================================

REPO_ROOT="${REPO_ROOT:-/home/redafrix/SimVLA_modified}"
EVAL_DIR="${EVAL_DIR:-${REPO_ROOT}/evaluation/libero}"
LIBERO_PRO_ROOT="${LIBERO_PRO_ROOT:-/home/redafrix/LIBERO-PRO}"

# Space-separated list of policy-server ports.
PORTS="${PORTS:-8103 8104}"
NO_VIDEO="${NO_VIDEO:-true}"
STATE_STATS_PATH="${STATE_STATS_PATH:-}"

# Default coverage matches the LIBERO-PRO table excluding Ori and Task:
# - Obj -> *_object
# - Pos -> *_swap
# - Sem -> *_lan
# Across:
# - Spatial -> libero_spatial_*
# - Object  -> libero_object_*
# - Goal    -> libero_goal_*
# - Long    -> libero_10_*
#
# With the defaults below:
# - Spatial: 25 tasks x 3 conds x 2 seeds x 2 trials = 300
# - Object:  25 tasks x 3 conds x 2 seeds x 2 trials = 300
# - Goal:    10 tasks x 3 conds x 2 seeds x 2 trials = 120
# - Long:    10 tasks x 3 conds x 2 seeds x 2 trials = 120
# - Total = 840 rollouts
SUITES="${SUITES:-\
libero_spatial_object libero_spatial_swap libero_spatial_lan \
libero_object_object libero_object_swap libero_object_lan \
libero_goal_object libero_goal_swap libero_goal_lan \
libero_10_object libero_10_swap libero_10_lan\
}"

# More seeds = more data = longer run.
SEEDS="${SEEDS:-19 46 17}"

# Trials per task per seed.
NUM_TRIALS="${NUM_TRIALS:-12}"

# Parallelism defaults to the number of ports unless overridden.
read -r -a PORT_ARRAY <<< "${PORTS}"
if [ "${#PORT_ARRAY[@]}" -eq 0 ]; then
  echo "[ERROR] PORTS is empty. Example: PORTS=\"8103 8104\"" >&2
  exit 1
fi
MAX_PARALLEL="${MAX_PARALLEL:-${#PORT_ARRAY[@]}}"

RUN_NAME="${RUN_NAME:-phase2_tdqc_$(date +%Y%m%d_%H%M%S)}"
OUT_DIR="${OUT_DIR:-${EVAL_DIR}/eval_libero_pro/${RUN_NAME}}"

COMBINED_JSONL="${OUT_DIR}/combined_all_suites_all_seeds.jsonl"
MASTER_LOG="${OUT_DIR}/run_collection.log"

mkdir -p "${OUT_DIR}"

cd "${EVAL_DIR}"

if [ -f "${HOME}/miniconda3/etc/profile.d/conda.sh" ]; then
  source "${HOME}/miniconda3/etc/profile.d/conda.sh"
elif [ -f "${HOME}/anaconda3/etc/profile.d/conda.sh" ]; then
  source "${HOME}/anaconda3/etc/profile.d/conda.sh"
else
  echo "[ERROR] Could not find conda.sh. Activate conda manually or fix the path." | tee -a "${MASTER_LOG}"
  exit 1
fi

conda activate libero

if [ ! -x "./run_libero_pro_eval.sh" ]; then
  echo "[ERROR] ./run_libero_pro_eval.sh not found or not executable." | tee -a "${MASTER_LOG}"
  echo "Try: chmod +x ./run_libero_pro_eval.sh" | tee -a "${MASTER_LOG}"
  exit 1
fi

: > "${COMBINED_JSONL}"

echo "============================================================" | tee -a "${MASTER_LOG}"
echo "Phase 2 TDQC LIBERO uncertainty rollout collection" | tee -a "${MASTER_LOG}"
echo "============================================================" | tee -a "${MASTER_LOG}"
echo "REPO_ROOT        = ${REPO_ROOT}" | tee -a "${MASTER_LOG}"
echo "EVAL_DIR         = ${EVAL_DIR}" | tee -a "${MASTER_LOG}"
echo "LIBERO_PRO_ROOT  = ${LIBERO_PRO_ROOT}" | tee -a "${MASTER_LOG}"
echo "PORTS            = ${PORTS}" | tee -a "${MASTER_LOG}"
echo "MAX_PARALLEL     = ${MAX_PARALLEL}" | tee -a "${MASTER_LOG}"
echo "NO_VIDEO         = ${NO_VIDEO}" | tee -a "${MASTER_LOG}"
echo "STATE_STATS_PATH = ${STATE_STATS_PATH:-<disabled>}" | tee -a "${MASTER_LOG}"
echo "SUITES           = ${SUITES}" | tee -a "${MASTER_LOG}"
echo "SEEDS            = ${SEEDS}" | tee -a "${MASTER_LOG}"
echo "NUM_TRIALS       = ${NUM_TRIALS}" | tee -a "${MASTER_LOG}"
echo "OUT_DIR          = ${OUT_DIR}" | tee -a "${MASTER_LOG}"
echo "COMBINED_JSONL   = ${COMBINED_JSONL}" | tee -a "${MASTER_LOG}"
echo "============================================================" | tee -a "${MASTER_LOG}"

run_one_eval() {
  local suite="$1"
  local seed="$2"
  local port="$3"
  local out_jsonl="$4"
  local run_log="$5"
  local status_file="$6"

  {
    echo "============================================================"
    echo "Running suite=${suite}, seed=${seed}, trials=${NUM_TRIALS}, port=${port}"
    echo "Output JSONL: ${out_jsonl}"
    echo "Run log:      ${run_log}"
    echo "============================================================"
  } >> "${MASTER_LOG}"

  rm -f "${out_jsonl}" "${status_file}"

  (
    set +e
    LIBERO_PRO_ROOT="${LIBERO_PRO_ROOT}" \
    TASK_SUITE="${suite}" \
    NUM_TRIALS="${NUM_TRIALS}" \
    SEED="${seed}" \
    PORT="${port}" \
    NO_VIDEO="${NO_VIDEO}" \
    STATE_STATS_PATH="${STATE_STATS_PATH}" \
    UNCERTAINTY_LOG="${out_jsonl}" \
    ./run_libero_pro_eval.sh > "${run_log}" 2>&1
    rc=$?
    echo "${rc}" > "${status_file}"
    exit 0
  ) &
}

active_jobs=0
job_idx=0
for suite in ${SUITES}; do
  for seed in ${SEEDS}; do
    port="${PORT_ARRAY[$((job_idx % ${#PORT_ARRAY[@]}))]}"
    out_jsonl="${OUT_DIR}/${suite}_seed${seed}_${NUM_TRIALS}trials.jsonl"
    run_log="${OUT_DIR}/${suite}_seed${seed}_${NUM_TRIALS}trials.log"
    status_file="${OUT_DIR}/${suite}_seed${seed}_${NUM_TRIALS}trials.status"

    run_one_eval "${suite}" "${seed}" "${port}" "${out_jsonl}" "${run_log}" "${status_file}"

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
total_written=0
for suite in ${SUITES}; do
  for seed in ${SEEDS}; do
    out_jsonl="${OUT_DIR}/${suite}_seed${seed}_${NUM_TRIALS}trials.jsonl"
    run_log="${OUT_DIR}/${suite}_seed${seed}_${NUM_TRIALS}trials.log"
    status_file="${OUT_DIR}/${suite}_seed${seed}_${NUM_TRIALS}trials.status"

    rc="missing"
    if [ -f "${status_file}" ]; then
      rc="$(cat "${status_file}")"
    fi

    if [ "${rc}" != "0" ]; then
      echo "[WARNING] Job failed: suite=${suite}, seed=${seed}, rc=${rc}. See ${run_log}" | tee -a "${MASTER_LOG}"
      failed_jobs=$((failed_jobs + 1))
      continue
    fi

    if [ ! -s "${out_jsonl}" ]; then
      echo "[WARNING] No JSONL data was written for suite=${suite}, seed=${seed}. See ${run_log}" | tee -a "${MASTER_LOG}"
      failed_jobs=$((failed_jobs + 1))
      continue
    fi

    n_lines=$(wc -l < "${out_jsonl}")
    total_written=$((total_written + n_lines))
    echo "[OK] Wrote ${n_lines} rollout lines to ${out_jsonl}" | tee -a "${MASTER_LOG}"
    cat "${out_jsonl}" >> "${COMBINED_JSONL}"
  done
done

total_lines=$(wc -l < "${COMBINED_JSONL}" || echo "0")

echo "" | tee -a "${MASTER_LOG}"
echo "============================================================" | tee -a "${MASTER_LOG}"
echo "Collection finished." | tee -a "${MASTER_LOG}"
echo "Successful rollout lines merged: ${total_written}" | tee -a "${MASTER_LOG}"
echo "Total combined rollout lines: ${total_lines}" | tee -a "${MASTER_LOG}"
echo "Failed jobs: ${failed_jobs}" | tee -a "${MASTER_LOG}"
echo "Combined JSONL:" | tee -a "${MASTER_LOG}"
echo "${COMBINED_JSONL}" | tee -a "${MASTER_LOG}"
echo "============================================================" | tee -a "${MASTER_LOG}"

echo ""
echo "Next step: convert + train TDQC:"
echo ""
echo "python -m phase2_tdqc.convert_uncertainty_jsonl_to_tdqc \\"
echo "  --input_jsonl ${COMBINED_JSONL} \\"
echo "  --output_path ${REPO_ROOT}/runs/tdqc_datasets/${RUN_NAME}_tdqc.pt"
echo ""
echo "python -m phase2_tdqc.train_tdqc_calibrator \\"
echo "  --dataset_path ${REPO_ROOT}/runs/tdqc_datasets/${RUN_NAME}_tdqc.pt \\"
echo "  --output_dir ${REPO_ROOT}/runs/tdqc_calibrator/${RUN_NAME} \\"
echo "  --epochs 100 \\"
echo "  --batch_size 32 \\"
echo "  --lr 1e-4 \\"
echo "  --hidden_dim 64 \\"
echo "  --target_update_freq 25"
