#!/usr/bin/env bash
set -euo pipefail

# Queue a raw-uncertainty LIBERO-PRO TDQC collection after the current
# asset-prep/eval work finishes. This script does not start servers; it assumes
# the five SimVLA servers are already listening on PORTS.

REPO_ROOT="${REPO_ROOT:-/home/redafrix/SimVLA_modified}"
EVAL_DIR="${EVAL_DIR:-${REPO_ROOT}/evaluation/libero}"
LIBERO_PRO_ROOT="${LIBERO_PRO_ROOT:-/home/redafrix/LIBERO-PRO}"

PORTS="${PORTS:-8103 8104 8105 8106 8107}"
MAX_PARALLEL="${MAX_PARALLEL:-5}"
NO_VIDEO="${NO_VIDEO:-true}"

# 12 LIBERO-PRO variant suites. With 10 tasks/suite, 3 seeds and 12 trials this
# produces about 4320 trajectories.
SUITES="${SUITES:-\
libero_spatial_object libero_spatial_swap libero_spatial_lan \
libero_object_object libero_object_swap libero_object_lan \
libero_goal_object libero_goal_swap libero_goal_lan \
libero_10_object libero_10_swap libero_10_lan\
}"
SEEDS="${SEEDS:-19 46 17}"
NUM_TRIALS="${NUM_TRIALS:-12}"

RUN_NAME="${RUN_NAME:-phase2_tdqc_raw_pro_4000_$(date +%Y%m%d_%H%M%S)}"
OUT_DIR="${OUT_DIR:-${EVAL_DIR}/eval_libero_pro/${RUN_NAME}}"
QUEUE_LOG="${OUT_DIR}/queued_collection.log"

WAIT_POLL_SECONDS="${WAIT_POLL_SECONDS:-60}"
WAIT_TIMEOUT_SECONDS="${WAIT_TIMEOUT_SECONDS:-0}"  # 0 means wait forever.

mkdir -p "${OUT_DIR}"

log() {
  printf '[%s] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$*" | tee -a "${QUEUE_LOG}"
}

active_libero_jobs() {
  pgrep -af "run_libero_pro_eval.sh|libero_client.py" \
    | grep -v "queue_phase2_tdqc_raw_pro_4000_collection.sh" \
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
      log "No active LIBERO eval/prep processes or generation locks remain."
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
        log "Still-held generation locks:"
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

validate_assets() {
  python - "$LIBERO_PRO_ROOT" ${SUITES} <<'PY'
import os
import sys
from pathlib import Path

root = Path(sys.argv[1])
suites = sys.argv[2:]
bddl_root = root / "libero" / "libero" / "bddl_files"
init_root = root / "libero" / "libero" / "init_files"

errors = []
for suite in suites:
    bddl = bddl_root / suite
    init = init_root / suite
    bddls = sorted(bddl.glob("*.bddl")) if bddl.is_dir() else []
    inits = sorted(init.glob("*.pruned_init")) if init.is_dir() else []
    if not bddls:
        errors.append(f"{suite}: missing .bddl files in {bddl}")
    if not inits:
        errors.append(f"{suite}: missing .pruned_init files in {init}")
    if bddl.is_symlink():
        errors.append(f"{suite}: bddl dir is still a symlink: {bddl}")
    if init.is_symlink():
        errors.append(f"{suite}: init dir is still a symlink: {init}")

if errors:
    print("LIBERO-PRO asset validation failed:", file=sys.stderr)
    for err in errors:
        print(f"  - {err}", file=sys.stderr)
    sys.exit(1)

for suite in suites:
    print(f"{suite}: assets OK")
PY
}

log "Queued raw LIBERO-PRO TDQC collection."
log "RUN_NAME=${RUN_NAME}"
log "OUT_DIR=${OUT_DIR}"
log "PORTS=${PORTS}"
log "MAX_PARALLEL=${MAX_PARALLEL}"
log "SUITES=${SUITES}"
log "SEEDS=${SEEDS}"
log "NUM_TRIALS=${NUM_TRIALS}"
log "Expected rollouts ~= 12 suites * 10 tasks * 3 seeds * 12 trials = 4320."

wait_for_current_work

log "Validating LIBERO-PRO variant assets before collection."
validate_assets 2>&1 | tee -a "${QUEUE_LOG}"

log "Starting collection. Raw uncertainties are stored in each JSONL uncertainty_trace as path_variance/last_step_variance."
cd "${EVAL_DIR}"

RUN_NAME="${RUN_NAME}" \
OUT_DIR="${OUT_DIR}" \
PORTS="${PORTS}" \
MAX_PARALLEL="${MAX_PARALLEL}" \
SUITES="${SUITES}" \
SEEDS="${SEEDS}" \
NUM_TRIALS="${NUM_TRIALS}" \
NO_VIDEO="${NO_VIDEO}" \
LIBERO_PRO_ROOT="${LIBERO_PRO_ROOT}" \
./run_phase2_libero_uncertainty_rollouts_12h.sh 2>&1 | tee -a "${QUEUE_LOG}"

log "Collection script finished."
