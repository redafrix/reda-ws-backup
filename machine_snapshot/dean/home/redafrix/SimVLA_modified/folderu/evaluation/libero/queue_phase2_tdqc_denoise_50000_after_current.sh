#!/usr/bin/env bash
set -euo pipefail

# Queue a second large TDQC denoise-uncertainty collection after the current
# collection finishes. This script assumes the five SimVLA servers are already
# running on ports 8111-8115.

REPO_ROOT="${REPO_ROOT:-/home/redafrix/SimVLA_modified}"
EVAL_DIR="${EVAL_DIR:-${REPO_ROOT}/evaluation/libero}"

CURRENT_RUN_NAME="${CURRENT_RUN_NAME:-phase2_tdqc_denoise_15000_20260430_093849}"
CURRENT_RUN_DIR="${CURRENT_RUN_DIR:-${EVAL_DIR}/eval_libero_pro/${CURRENT_RUN_NAME}}"
CURRENT_LOG="${CURRENT_LOG:-${CURRENT_RUN_DIR}/run_collection.log}"

NEXT_RUN_NAME="${NEXT_RUN_NAME:-phase2_tdqc_denoise_50000_after_${CURRENT_RUN_NAME}_$(date +%Y%m%d_%H%M%S)}"
NEXT_OUT_DIR="${NEXT_OUT_DIR:-${EVAL_DIR}/eval_libero_pro/${NEXT_RUN_NAME}}"

PORTS="${PORTS:-8111 8112 8113 8114 8115}"
MAX_PARALLEL="${MAX_PARALLEL:-5}"

# 12 suites * 10 tasks * 5 seeds * 84 trials = 50,400 rollouts.
SEEDS="${SEEDS:-211 223 257 281 307}"
NUM_TRIALS="${NUM_TRIALS:-84}"
NO_VIDEO="${NO_VIDEO:-true}"

POLL_SECONDS="${POLL_SECONDS:-300}"
QUEUE_LOG="${QUEUE_LOG:-/tmp/phase2_tdqc_denoise_50000_queue.log}"

log() {
  printf '[%(%F %T)T] %s\n' -1 "$*" | tee -a "${QUEUE_LOG}"
}

current_finished() {
  [ -f "${CURRENT_LOG}" ] && grep -q "Collection finished." "${CURRENT_LOG}"
}

current_has_live_clients() {
  pgrep -af "libero_client.py.*${CURRENT_RUN_DIR}" >/dev/null 2>&1
}

wait_for_current_run() {
  log "Waiting for current run to finish."
  log "CURRENT_RUN_DIR=${CURRENT_RUN_DIR}"
  log "CURRENT_LOG=${CURRENT_LOG}"

  while true; do
    if current_finished && ! current_has_live_clients; then
      log "Current run is finished and no matching clients are live."
      return 0
    fi

    if [ -d "${CURRENT_RUN_DIR}" ]; then
      local lines
      lines="$(find "${CURRENT_RUN_DIR}" -maxdepth 1 -name '*.jsonl' ! -name 'combined*' -type f -exec wc -l {} + 2>/dev/null | awk '/total$/ {print $1}' | tail -1)"
      lines="${lines:-0}"
      log "Still waiting. Current partial rollout lines: ${lines}"
    else
      log "Still waiting. Current run dir does not exist yet."
    fi

    sleep "${POLL_SECONDS}"
  done
}

main() {
  cd "${EVAL_DIR}"
  wait_for_current_run

  log "Starting next collection."
  log "NEXT_RUN_NAME=${NEXT_RUN_NAME}"
  log "NEXT_OUT_DIR=${NEXT_OUT_DIR}"
  log "PORTS=${PORTS}"
  log "SEEDS=${SEEDS}"
  log "NUM_TRIALS=${NUM_TRIALS}"
  log "Expected rollouts: 12 suites * 10 tasks * 5 seeds * 84 trials = 50400"

  RUN_NAME="${NEXT_RUN_NAME}" \
  OUT_DIR="${NEXT_OUT_DIR}" \
  PORTS="${PORTS}" \
  MAX_PARALLEL="${MAX_PARALLEL}" \
  SEEDS="${SEEDS}" \
  NUM_TRIALS="${NUM_TRIALS}" \
  NO_VIDEO="${NO_VIDEO}" \
  ./run_phase2_libero_uncertainty_rollouts_12h.sh
}

main "$@"
