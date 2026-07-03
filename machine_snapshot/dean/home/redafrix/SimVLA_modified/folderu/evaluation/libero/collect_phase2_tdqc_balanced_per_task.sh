#!/usr/bin/env bash
set -euo pipefail

# Collect balanced TDQC rollouts for LIBERO-PRO.
#
# For each (suite, task_id), this script keeps launching new seed batches until
# it has retained TARGET_PER_CLASS successes and TARGET_PER_CLASS failures, or
# until MAX_BATCHES_PER_TASK is reached. It keeps all raw batch JSONLs on disk,
# but only merges the balanced subset into the final combined JSONL.

REPO_ROOT="${REPO_ROOT:-/home/redafrix/SimVLA_modified}"
EVAL_DIR="${EVAL_DIR:-${REPO_ROOT}/evaluation/libero}"
LIBERO_PRO_ROOT="${LIBERO_PRO_ROOT:-/home/redafrix/LIBERO-PRO}"

PORTS="${PORTS:-8103 8104 8105}"
NO_VIDEO="${NO_VIDEO:-true}"
STATE_STATS_PATH="${STATE_STATS_PATH:-}"
REPLAN_STEPS="${REPLAN_STEPS:-5}"
FORCE_LIBERO_PRO_REGEN="${FORCE_LIBERO_PRO_REGEN:-false}"
EXTRA_PERTURBATIONS="${EXTRA_PERTURBATIONS:-}"
OBJECT_PERTURBATION_LEVEL="${OBJECT_PERTURBATION_LEVEL:-default}"

SUITES="${SUITES:-\
libero_spatial_object libero_spatial_swap libero_spatial_lan \
libero_object_object libero_object_swap libero_object_lan \
libero_goal_object libero_goal_swap libero_goal_lan \
libero_10_object libero_10_swap libero_10_lan\
}"
TASK_IDS="${TASK_IDS:-0 1 2 3 4 5 6 7 8 9}"

TARGET_PER_CLASS="${TARGET_PER_CLASS:-50}"
BATCH_TRIALS="${BATCH_TRIALS:-10}"
SEED_BASE="${SEED_BASE:-1000}"
MAX_BATCHES_PER_TASK="${MAX_BATCHES_PER_TASK:-100}"

read -r -a PORT_ARRAY <<< "${PORTS}"
if [ "${#PORT_ARRAY[@]}" -eq 0 ]; then
  echo "[ERROR] PORTS is empty. Example: PORTS=\"8103 8104 8105\"" >&2
  exit 1
fi
MAX_PARALLEL="${MAX_PARALLEL:-${#PORT_ARRAY[@]}}"
if [ "${MAX_PARALLEL}" -gt "${#PORT_ARRAY[@]}" ]; then
  MAX_PARALLEL="${#PORT_ARRAY[@]}"
fi

RUN_NAME="${RUN_NAME:-phase2_tdqc_balanced_$(date +%Y%m%d_%H%M%S)}"
OUT_DIR="${OUT_DIR:-${EVAL_DIR}/eval_libero_pro/${RUN_NAME}}"
RAW_DIR="${OUT_DIR}/raw_batches"
SELECTED_DIR="${OUT_DIR}/selected_balanced"
COMBINED_JSONL="${OUT_DIR}/combined_balanced.jsonl"
SUMMARY_JSON="${OUT_DIR}/balanced_summary.json"
MASTER_LOG="${OUT_DIR}/run_balanced_collection.log"

mkdir -p "${OUT_DIR}" "${RAW_DIR}" "${SELECTED_DIR}"
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

wait_for_servers() {
  local timeout_s="${SERVER_READY_TIMEOUT_S:-120}"
  local start_ts
  start_ts="$(date +%s)"
  while true; do
    local ready=0
    for port in "${PORT_ARRAY[@]}"; do
      if python - "${port}" <<'PY'
import socket
import sys

port = int(sys.argv[1])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1.0)
try:
    s.connect(("127.0.0.1", port))
except OSError:
    sys.exit(1)
finally:
    s.close()
sys.exit(0)
PY
      then
        ready=$((ready + 1))
      fi
    done

    if [ "${ready}" -eq "${#PORT_ARRAY[@]}" ]; then
      echo "[OK] All ${ready}/${#PORT_ARRAY[@]} servers are reachable." | tee -a "${MASTER_LOG}"
      return 0
    fi

    local now_ts
    now_ts="$(date +%s)"
    if [ $((now_ts - start_ts)) -ge "${timeout_s}" ]; then
      echo "[ERROR] Only ${ready}/${#PORT_ARRAY[@]} servers are reachable after ${timeout_s}s." | tee -a "${MASTER_LOG}"
      echo "[ERROR] Start the SimVLA servers first, then rerun this collector." | tee -a "${MASTER_LOG}"
      return 1
    fi

    echo "[WAIT] Servers reachable: ${ready}/${#PORT_ARRAY[@]} ..." | tee -a "${MASTER_LOG}"
    sleep 5
  done
}

task_key() {
  local suite="$1"
  local task_id="$2"
  echo "${suite}__task${task_id}"
}

seed_for_attempt() {
  local key_idx="$1"
  local attempt_idx="$2"
  echo $((SEED_BASE + key_idx * 1000 + attempt_idx))
}

sanitize_key() {
  local key="$1"
  echo "${key//\//_}"
}

process_batch_into_selected() {
  local batch_jsonl="$1"
  local selected_jsonl="$2"
  local target="$3"
  local metrics_file="$4"

  python - "${batch_jsonl}" "${selected_jsonl}" "${target}" "${metrics_file}" <<'PY'
import json
import sys
from pathlib import Path

batch_path = Path(sys.argv[1])
selected_path = Path(sys.argv[2])
target = int(sys.argv[3])
metrics_path = Path(sys.argv[4])

selected_success = 0
selected_failure = 0
if selected_path.exists():
    with selected_path.open("r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            rec = json.loads(line)
            if rec.get("success"):
                selected_success += 1
            else:
                selected_failure += 1

raw_success = 0
raw_failure = 0
added_success = 0
added_failure = 0
selected_lines = []

if batch_path.exists():
    with batch_path.open("r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            try:
                rec = json.loads(line)
            except Exception:
                continue
            is_success = bool(rec.get("success"))
            if is_success:
                raw_success += 1
                if selected_success < target:
                    selected_lines.append(line)
                    selected_success += 1
                    added_success += 1
            else:
                raw_failure += 1
                if selected_failure < target:
                    selected_lines.append(line)
                    selected_failure += 1
                    added_failure += 1

if selected_lines:
    with selected_path.open("a", encoding="utf-8") as f:
        for line in selected_lines:
            f.write(line if line.endswith("\n") else line + "\n")

metrics = {
    "raw_success": raw_success,
    "raw_failure": raw_failure,
    "added_success": added_success,
    "added_failure": added_failure,
    "selected_success": selected_success,
    "selected_failure": selected_failure,
    "complete": selected_success >= target and selected_failure >= target,
}
metrics_path.write_text(json.dumps(metrics), encoding="utf-8")
print(json.dumps(metrics))
PY
}

echo "============================================================" | tee -a "${MASTER_LOG}"
echo "Balanced Phase 2 TDQC LIBERO uncertainty rollout collection" | tee -a "${MASTER_LOG}"
echo "============================================================" | tee -a "${MASTER_LOG}"
echo "REPO_ROOT            = ${REPO_ROOT}" | tee -a "${MASTER_LOG}"
echo "EVAL_DIR             = ${EVAL_DIR}" | tee -a "${MASTER_LOG}"
echo "LIBERO_PRO_ROOT      = ${LIBERO_PRO_ROOT}" | tee -a "${MASTER_LOG}"
echo "PORTS                = ${PORTS}" | tee -a "${MASTER_LOG}"
echo "MAX_PARALLEL         = ${MAX_PARALLEL}" | tee -a "${MASTER_LOG}"
echo "NO_VIDEO             = ${NO_VIDEO}" | tee -a "${MASTER_LOG}"
echo "STATE_STATS_PATH     = ${STATE_STATS_PATH:-<disabled>}" | tee -a "${MASTER_LOG}"
echo "EXTRA_PERTURBATIONS  = ${EXTRA_PERTURBATIONS:-<none>}" | tee -a "${MASTER_LOG}"
echo "OBJECT_PERTURB_LEVEL = ${OBJECT_PERTURBATION_LEVEL}" | tee -a "${MASTER_LOG}"
echo "SUITES               = ${SUITES}" | tee -a "${MASTER_LOG}"
echo "TASK_IDS             = ${TASK_IDS}" | tee -a "${MASTER_LOG}"
echo "TARGET_PER_CLASS     = ${TARGET_PER_CLASS}" | tee -a "${MASTER_LOG}"
echo "BATCH_TRIALS         = ${BATCH_TRIALS}" | tee -a "${MASTER_LOG}"
echo "SEED_BASE            = ${SEED_BASE}" | tee -a "${MASTER_LOG}"
echo "MAX_BATCHES_PER_TASK = ${MAX_BATCHES_PER_TASK}" | tee -a "${MASTER_LOG}"
echo "OUT_DIR              = ${OUT_DIR}" | tee -a "${MASTER_LOG}"
echo "============================================================" | tee -a "${MASTER_LOG}"

wait_for_servers

COLLECTION_FORCE_LIBERO_PRO_REGEN="${FORCE_LIBERO_PRO_REGEN}"
if [[ "${FORCE_LIBERO_PRO_REGEN}" == "true" ]]; then
  echo "[PREP] FORCE_LIBERO_PRO_REGEN=true: regenerating each suite once before collection." | tee -a "${MASTER_LOG}"
  for suite in ${SUITES}; do
    prep_log="${RAW_DIR}/$(sanitize_key "${suite}")__asset_prep.log"
    prep_status="${RAW_DIR}/$(sanitize_key "${suite}")__asset_prep.status"
    echo "[PREP] suite=${suite} log=${prep_log}" | tee -a "${MASTER_LOG}"
    set +e
    LIBERO_PRO_ROOT="${LIBERO_PRO_ROOT}" \
    FORCE_LIBERO_PRO_REGEN=true \
    EXTRA_PERTURBATIONS="${EXTRA_PERTURBATIONS}" \
    OBJECT_PERTURBATION_LEVEL="${OBJECT_PERTURBATION_LEVEL}" \
    TASK_SUITE="${suite}" \
    TASK_ID="" \
    NUM_TRIALS=0 \
    SEED="${SEED_BASE}" \
    PORT="${PORT_ARRAY[0]}" \
    REPLAN_STEPS="${REPLAN_STEPS}" \
    NO_VIDEO="${NO_VIDEO}" \
    STATE_STATS_PATH="${STATE_STATS_PATH}" \
    UNCERTAINTY_LOG="${RAW_DIR}/$(sanitize_key "${suite}")__asset_prep.jsonl" \
    ./run_libero_pro_eval.sh > "${prep_log}" 2>&1
    prep_rc=$?
    set -e
    echo "${prep_rc}" > "${prep_status}"
    if [ "${prep_rc}" -ne 0 ]; then
      echo "[PREP WARNING] suite=${suite} rc=${prep_rc}. Continuing; batch jobs may reuse existing assets or fail individually. See ${prep_log}" | tee -a "${MASTER_LOG}"
    fi
  done
  COLLECTION_FORCE_LIBERO_PRO_REGEN=false
  echo "[PREP] Suite asset regeneration complete; batch jobs will reuse generated assets." | tee -a "${MASTER_LOG}"
fi

declare -a TASK_KEYS=()
declare -A TASK_SUITE_OF=()
declare -A TASK_ID_OF=()
declare -A KEY_INDEX=()
declare -A BATCHES_LAUNCHED=()
declare -A RAW_SUCCESS_TOTAL=()
declare -A RAW_FAILURE_TOTAL=()
declare -A SELECTED_SUCCESS=()
declare -A SELECTED_FAILURE=()
declare -A TASK_COMPLETE=()
declare -A TASK_RUNNING=()
declare -A SELECTED_FILE_OF=()

key_idx=0
for suite in ${SUITES}; do
  for task_id in ${TASK_IDS}; do
    key="$(task_key "${suite}" "${task_id}")"
    TASK_KEYS+=("${key}")
    TASK_SUITE_OF["${key}"]="${suite}"
    TASK_ID_OF["${key}"]="${task_id}"
    KEY_INDEX["${key}"]="${key_idx}"
    BATCHES_LAUNCHED["${key}"]=0
    RAW_SUCCESS_TOTAL["${key}"]=0
    RAW_FAILURE_TOTAL["${key}"]=0
    SELECTED_SUCCESS["${key}"]=0
    SELECTED_FAILURE["${key}"]=0
    TASK_COMPLETE["${key}"]=0
    TASK_RUNNING["${key}"]=0
    SELECTED_FILE_OF["${key}"]="${SELECTED_DIR}/$(sanitize_key "${key}")_balanced.jsonl"
    : > "${SELECTED_FILE_OF[${key}]}"
    key_idx=$((key_idx + 1))
  done
done

declare -A PORT_BUSY=()
declare -A PID_TO_KEY=()
declare -A PID_TO_PORT=()
declare -A PID_TO_BATCH_JSONL=()
declare -A PID_TO_STATUS_FILE=()
declare -A PID_TO_LOG_FILE=()
declare -A PID_TO_METRICS_FILE=()
declare -a ACTIVE_PIDS=()

for port in "${PORT_ARRAY[@]}"; do
  PORT_BUSY["${port}"]=0
done

get_free_port() {
  for port in "${PORT_ARRAY[@]}"; do
    if [ "${PORT_BUSY[${port}]}" -eq 0 ]; then
      echo "${port}"
      return 0
    fi
  done
  return 1
}

launch_batch() {
  local key="$1"
  local port="$2"
  local suite="${TASK_SUITE_OF[${key}]}"
  local task_id="${TASK_ID_OF[${key}]}"
  local batch_idx="${BATCHES_LAUNCHED[${key}]}"
  local seed
  seed="$(seed_for_attempt "${KEY_INDEX[${key}]}" "${batch_idx}")"

  local stem="${RAW_DIR}/$(sanitize_key "${key}")_batch${batch_idx}_seed${seed}"
  local out_jsonl="${stem}.jsonl"
  local run_log="${stem}.log"
  local status_file="${stem}.status"
  local metrics_file="${stem}.metrics.json"

  rm -f "${out_jsonl}" "${run_log}" "${status_file}" "${metrics_file}"

  {
    echo "[LAUNCH] suite=${suite} task=${task_id} batch=${batch_idx} seed=${seed} port=${port}"
  } | tee -a "${MASTER_LOG}"

  (
    set +e
    LIBERO_PRO_ROOT="${LIBERO_PRO_ROOT}" \
    FORCE_LIBERO_PRO_REGEN="${COLLECTION_FORCE_LIBERO_PRO_REGEN}" \
    EXTRA_PERTURBATIONS="${EXTRA_PERTURBATIONS}" \
    OBJECT_PERTURBATION_LEVEL="${OBJECT_PERTURBATION_LEVEL}" \
    TASK_SUITE="${suite}" \
    TASK_ID="${task_id}" \
    NUM_TRIALS="${BATCH_TRIALS}" \
    SEED="${seed}" \
    PORT="${port}" \
    REPLAN_STEPS="${REPLAN_STEPS}" \
    NO_VIDEO="${NO_VIDEO}" \
    STATE_STATS_PATH="${STATE_STATS_PATH}" \
    UNCERTAINTY_LOG="${out_jsonl}" \
    ./run_libero_pro_eval.sh > "${run_log}" 2>&1
    rc=$?
    echo "${rc}" > "${status_file}"
    exit 0
  ) &

  local pid=$!
  ACTIVE_PIDS+=("${pid}")
  PID_TO_KEY["${pid}"]="${key}"
  PID_TO_PORT["${pid}"]="${port}"
  PID_TO_BATCH_JSONL["${pid}"]="${out_jsonl}"
  PID_TO_STATUS_FILE["${pid}"]="${status_file}"
  PID_TO_LOG_FILE["${pid}"]="${run_log}"
  PID_TO_METRICS_FILE["${pid}"]="${metrics_file}"
  PORT_BUSY["${port}"]=1
  TASK_RUNNING["${key}"]=1
  BATCHES_LAUNCHED["${key}"]=$((BATCHES_LAUNCHED[${key}] + 1))
}

pick_next_task() {
  for key in "${TASK_KEYS[@]}"; do
    if [ "${TASK_COMPLETE[${key}]}" -eq 1 ]; then
      continue
    fi
    if [ "${TASK_RUNNING[${key}]}" -eq 1 ]; then
      continue
    fi
    if [ "${BATCHES_LAUNCHED[${key}]}" -ge "${MAX_BATCHES_PER_TASK}" ]; then
      continue
    fi
    echo "${key}"
    return 0
  done
  return 1
}

all_tasks_done() {
  for key in "${TASK_KEYS[@]}"; do
    if [ "${TASK_COMPLETE[${key}]}" -eq 0 ] && [ "${BATCHES_LAUNCHED[${key}]}" -lt "${MAX_BATCHES_PER_TASK}" ]; then
      return 1
    fi
  done
  return 0
}

process_finished_pid() {
  local pid="$1"
  local key="${PID_TO_KEY[${pid}]}"
  local port="${PID_TO_PORT[${pid}]}"
  local batch_jsonl="${PID_TO_BATCH_JSONL[${pid}]}"
  local status_file="${PID_TO_STATUS_FILE[${pid}]}"
  local run_log="${PID_TO_LOG_FILE[${pid}]}"
  local metrics_file="${PID_TO_METRICS_FILE[${pid}]}"

  local rc="missing"
  if [ -f "${status_file}" ]; then
    rc="$(cat "${status_file}")"
  fi
  if [ "${rc}" != "0" ]; then
    echo "[WARNING] Nonzero rc=${rc} for ${key}. Keeping any partial JSONL. See ${run_log}" | tee -a "${MASTER_LOG}"
  fi

  local metrics_json
  metrics_json="$(process_batch_into_selected \
    "${batch_jsonl}" \
    "${SELECTED_FILE_OF[${key}]}" \
    "${TARGET_PER_CLASS}" \
    "${metrics_file}")"

  local parsed
  parsed="$(python - "${metrics_file}" <<'PY'
import json, sys
from pathlib import Path
m = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
print(m["raw_success"], m["raw_failure"], m["selected_success"], m["selected_failure"], int(m["complete"]))
PY
)"
  read -r batch_raw_success batch_raw_failure new_selected_success new_selected_failure is_complete <<< "${parsed}"

  RAW_SUCCESS_TOTAL["${key}"]=$((RAW_SUCCESS_TOTAL[${key}] + batch_raw_success))
  RAW_FAILURE_TOTAL["${key}"]=$((RAW_FAILURE_TOTAL[${key}] + batch_raw_failure))
  SELECTED_SUCCESS["${key}"]="${new_selected_success}"
  SELECTED_FAILURE["${key}"]="${new_selected_failure}"
  TASK_COMPLETE["${key}"]="${is_complete}"
  TASK_RUNNING["${key}"]=0
  PORT_BUSY["${port}"]=0

  {
    echo "[DONE] ${key} rc=${rc} raw(+${batch_raw_success}/+${batch_raw_failure}) selected=${new_selected_success}/${new_selected_failure} batches=${BATCHES_LAUNCHED[${key}]}"
  } | tee -a "${MASTER_LOG}"

  unset PID_TO_KEY["${pid}"]
  unset PID_TO_PORT["${pid}"]
  unset PID_TO_BATCH_JSONL["${pid}"]
  unset PID_TO_STATUS_FILE["${pid}"]
  unset PID_TO_LOG_FILE["${pid}"]
  unset PID_TO_METRICS_FILE["${pid}"]
}

while true; do
  while [ "${#ACTIVE_PIDS[@]}" -lt "${MAX_PARALLEL}" ]; do
    if ! port="$(get_free_port)"; then
      break
    fi
    if ! next_key="$(pick_next_task)"; then
      break
    fi
    launch_batch "${next_key}" "${port}"
  done

  if [ "${#ACTIVE_PIDS[@]}" -eq 0 ]; then
    if all_tasks_done; then
      break
    fi
    echo "[ERROR] No active jobs and unfinished tasks remain. Check MAX_BATCHES_PER_TASK or failing tasks." | tee -a "${MASTER_LOG}"
    break
  fi

  sleep 2
  remaining_pids=()
  for pid in "${ACTIVE_PIDS[@]}"; do
    if kill -0 "${pid}" 2>/dev/null; then
      remaining_pids+=("${pid}")
      continue
    fi
    wait "${pid}" || true
    process_finished_pid "${pid}"
  done
  ACTIVE_PIDS=("${remaining_pids[@]}")
done

: > "${COMBINED_JSONL}"
for key in "${TASK_KEYS[@]}"; do
  selected_file="${SELECTED_FILE_OF[${key}]}"
  if [ -s "${selected_file}" ]; then
    cat "${selected_file}" >> "${COMBINED_JSONL}"
  fi
done

{
python - "${SUMMARY_JSON}" "${COMBINED_JSONL}" "${TARGET_PER_CLASS}" "${#TASK_KEYS[@]}" <<'PY'
import json
import os
import sys
from pathlib import Path

summary_path = Path(sys.argv[1])
combined_path = Path(sys.argv[2])
target = int(sys.argv[3])
expected_tasks = int(sys.argv[4])

selected_dir = summary_path.parent / "selected_balanced"
rows = []
total_success = 0
total_failure = 0
completed = 0

for path in sorted(selected_dir.glob("*_balanced.jsonl")):
    success = failure = 0
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            rec = json.loads(line)
            if rec.get("success"):
                success += 1
            else:
                failure += 1
    total_success += success
    total_failure += failure
    done = success >= target and failure >= target
    completed += int(done)
    rows.append({
        "file": path.name,
        "selected_success": success,
        "selected_failure": failure,
        "complete": done,
    })

summary = {
    "target_per_class": target,
    "expected_task_count": expected_tasks,
    "completed_task_count": completed,
    "selected_success_total": total_success,
    "selected_failure_total": total_failure,
    "combined_lines": sum(1 for _ in combined_path.open("r", encoding="utf-8")) if combined_path.exists() else 0,
    "tasks": rows,
}
summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
print(json.dumps(summary, indent=2))
PY
} | tee -a "${MASTER_LOG}"

echo "============================================================" | tee -a "${MASTER_LOG}"
echo "Balanced collection finished." | tee -a "${MASTER_LOG}"
echo "Selected combined JSONL: ${COMBINED_JSONL}" | tee -a "${MASTER_LOG}"
echo "Summary JSON: ${SUMMARY_JSON}" | tee -a "${MASTER_LOG}"
echo "============================================================" | tee -a "${MASTER_LOG}"
