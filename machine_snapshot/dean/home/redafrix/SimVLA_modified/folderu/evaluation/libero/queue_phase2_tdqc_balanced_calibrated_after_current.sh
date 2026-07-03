#!/usr/bin/env bash
set -euo pipefail

# Queue balanced LIBERO-PRO TDQC collection after the currently running LIBERO
# collector finishes. This script assumes SimVLA servers are already running on
# PORTS. It runs multiple collector groups because perturbation difficulty is
# global per collect_phase2_tdqc_balanced_per_task.sh invocation.

REPO_ROOT="${REPO_ROOT:-/home/redafrix/SimVLA_modified}"
EVAL_DIR="${EVAL_DIR:-${REPO_ROOT}/evaluation/libero}"
LIBERO_PRO_ROOT="${LIBERO_PRO_ROOT:-/home/redafrix/LIBERO-PRO}"

PORTS="${PORTS:-8103 8104 8105}"
MAX_PARALLEL="${MAX_PARALLEL:-3}"
STATE_STATS_PATH="${STATE_STATS_PATH:-${REPO_ROOT}/norm_stats/libero_norm.json}"
NO_VIDEO="${NO_VIDEO:-true}"
TARGET_PER_CLASS="${TARGET_PER_CLASS:-50}"
BATCH_TRIALS="${BATCH_TRIALS:-10}"
MAX_BATCHES_PER_TASK="${MAX_BATCHES_PER_TASK:-120}"

RUN_ROOT_NAME="${RUN_ROOT_NAME:-phase2_tdqc_balanced_calibrated_$(date +%Y%m%d_%H%M%S)}"
RUN_ROOT="${EVAL_DIR}/eval_libero_pro/${RUN_ROOT_NAME}"
QUEUE_LOG="${RUN_ROOT}/queue_balanced_calibrated.log"
WAIT_POLL_SECONDS="${WAIT_POLL_SECONDS:-60}"
WAIT_TIMEOUT_SECONDS="${WAIT_TIMEOUT_SECONDS:-0}"  # 0 means wait forever.

mkdir -p "${RUN_ROOT}"

log() {
  printf '[%s] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$*" | tee -a "${QUEUE_LOG}"
}

active_libero_jobs() {
  pgrep -af "collect_phase2_tdqc_balanced_per_task.sh|run_libero_pro_eval.sh|libero_client.py" 2>/dev/null \
    | grep -v "queue_phase2_tdqc_balanced_calibrated_after_current.sh" \
    | grep -v "pgrep -af" \
    || true
}

generation_locks_busy() {
  shopt -s nullglob
  local lock
  for lock in "${LIBERO_PRO_ROOT}"/.*_pro_generation.lock; do
    if ! flock -n "${lock}" true 2>/dev/null; then
      echo "${lock}"
    fi
  done
}

wait_for_current_work() {
  local started now elapsed jobs locks
  started="$(date +%s)"

  while true; do
    jobs="$(active_libero_jobs)"
    locks="$(generation_locks_busy)"

    if [[ -z "${jobs}" && -z "${locks}" ]]; then
      log "No active LIBERO balanced/eval processes or generation locks remain."
      return 0
    fi

    now="$(date +%s)"
    elapsed=$((now - started))
    if [[ "${WAIT_TIMEOUT_SECONDS}" != "0" && "${elapsed}" -ge "${WAIT_TIMEOUT_SECONDS}" ]]; then
      log "[ERROR] Timed out waiting after ${elapsed}s."
      if [[ -n "${jobs}" ]]; then
        log "Still-active jobs:"
        printf '%s\n' "${jobs}" | tee -a "${QUEUE_LOG}"
      fi
      if [[ -n "${locks}" ]]; then
        log "Busy generation locks:"
        printf '%s\n' "${locks}" | tee -a "${QUEUE_LOG}"
      fi
      return 1
    fi

    log "Waiting for current LIBERO work to finish (${elapsed}s elapsed)."
    if [[ -n "${jobs}" ]]; then
      printf '%s\n' "${jobs}" | tee -a "${QUEUE_LOG}"
    fi
    if [[ -n "${locks}" ]]; then
      log "Busy generation locks:"
      printf '%s\n' "${locks}" | tee -a "${QUEUE_LOG}"
    fi
    sleep "${WAIT_POLL_SECONDS}"
  done
}

run_group() {
  local tag="$1"
  local suites="$2"
  local task_ids="$3"
  local seed_base="$4"
  local object_level="$5"
  local extra_perturbations="$6"

  local run_name="${RUN_ROOT_NAME}__${tag}"
  local out_dir="${RUN_ROOT}/${tag}"

  log "Starting group=${tag}"
  log "  suites=${suites}"
  log "  task_ids=${task_ids}"
  log "  seed_base=${seed_base}"
  log "  object_level=${object_level}"
  log "  extra_perturbations=${extra_perturbations:-<none>}"
  log "  out_dir=${out_dir}"

  RUN_NAME="${run_name}" \
  OUT_DIR="${out_dir}" \
  LIBERO_PRO_ROOT="${LIBERO_PRO_ROOT}" \
  PORTS="${PORTS}" \
  MAX_PARALLEL="${MAX_PARALLEL}" \
  STATE_STATS_PATH="${STATE_STATS_PATH}" \
  TARGET_PER_CLASS="${TARGET_PER_CLASS}" \
  BATCH_TRIALS="${BATCH_TRIALS}" \
  SEED_BASE="${seed_base}" \
  MAX_BATCHES_PER_TASK="${MAX_BATCHES_PER_TASK}" \
  SUITES="${suites}" \
  TASK_IDS="${task_ids}" \
  OBJECT_PERTURBATION_LEVEL="${object_level}" \
  EXTRA_PERTURBATIONS="${extra_perturbations}" \
  FORCE_LIBERO_PRO_REGEN=true \
  NO_VIDEO="${NO_VIDEO}" \
  "${EVAL_DIR}/collect_phase2_tdqc_balanced_per_task.sh" 2>&1 | tee -a "${QUEUE_LOG}"

  log "Finished group=${tag}"
}

main() {
  cd "${EVAL_DIR}"

  log "Queued calibrated balanced TDQC collection."
  log "RUN_ROOT=${RUN_ROOT}"
  log "PORTS=${PORTS}"
  log "MAX_PARALLEL=${MAX_PARALLEL}"
  log "TARGET_PER_CLASS=${TARGET_PER_CLASS}"
  log "BATCH_TRIALS=${BATCH_TRIALS}"
  log "MAX_BATCHES_PER_TASK=${MAX_BATCHES_PER_TASK}"
  log "STATE_STATS_PATH=${STATE_STATS_PATH}"

  wait_for_current_work

  # Current manual smoke covers libero_spatial_object task ids 0,1,2.
  # Continue the same calibrated difficulty for the remaining spatial-object tasks.
  run_group \
    "spatial_object_tasks3_9_hard_swap" \
    "libero_spatial_object" \
    "3 4 5 6 7 8 9" \
    "73000" \
    "hard" \
    "swap"

  # Object perturbation suites were too easy with object-only perturbations.
  # Add swap to create failures while preserving the object-holdout nature.
  run_group \
    "object_suites_hard_swap" \
    "libero_object_object libero_goal_object" \
    "0 1 2 3 4 5 6 7 8 9" \
    "90000" \
    "hard" \
    "swap"

  # LIBERO-10 object was already closer to mixed success/failure in prior data,
  # so use hard object replacement but do not add swap unless a later audit shows
  # it is still too easy.
  run_group \
    "libero10_object_hard" \
    "libero_10_object" \
    "0 1 2 3 4 5 6 7 8 9" \
    "120000" \
    "hard" \
    ""

  # Language perturbation suites were extremely easy; combine with swap to avoid
  # collecting almost only successes.
  run_group \
    "language_suites_swap_object" \
    "libero_spatial_lan libero_object_lan libero_goal_lan libero_10_lan" \
    "0 1 2 3 4 5 6 7 8 9" \
    "140000" \
    "hard" \
    "swap object"

  # Swap suites were already failure-heavy, so keep them pure swap to preserve
  # enough successes for 50/50 balancing.
  run_group \
    "swap_suites_default" \
    "libero_spatial_swap libero_object_swap libero_goal_swap libero_10_swap" \
    "0 1 2 3 4 5 6 7 8 9" \
    "190000" \
    "default" \
    ""

  log "All calibrated balanced groups finished."
}

main "$@"
