#!/usr/bin/env bash
set -u

ROOT="/media/rootalkhatib/My Passport/reda_ws"
SRC="${ROOT}/asynchvla_ws/src"
LIBERO_PRO="${ROOT}/intern_ship_ws/assets/repos/LIBERO-PRO"
DATA_ROOT="${ROOT}/asynchvla_ws/stage9_libero_pro_risk_data/data/probe/dense_15h_bob_v6_parserfix_scorerfix_20seed_evalhorizon_20260521"
LOG_DIR="${ROOT}/asynchvla_ws/stage9_libero_pro_risk_data/logs"
REPORT_DIR="${ROOT}/asynchvla_ws/stage9_libero_pro_risk_data/reports"
LIVE_REPORT="${REPORT_DIR}/STAGE9_DENSE_15H_BOB_V6_LIVE_REPORT.md"
START_TS="$(date +%s)"
DEADLINE_TS="$((START_TS + 15 * 3600))"

mkdir -p "${DATA_ROOT}" "${LOG_DIR}" "${REPORT_DIR}"

cd "${ROOT}" || exit 2
source "asynchvla_ws/scripts/activate_simvla_bob.sh"
export PYTHONPATH="${SRC}:${LIBERO_PRO}:${PYTHONPATH:-}"
export LIBERO_CONFIG_PATH="${ROOT}/asynchvla_ws/temp_config"
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl

write_live_header() {
  {
    echo "# Stage 9 Dense 15h Bob V6 Live Report"
    echo
    echo "- Started: $(date '+%F %T')"
    echo "- Deadline epoch: ${DEADLINE_TS}"
    echo "- Data root: \`${DATA_ROOT}\`"
    echo "- Policy: Bob only, real SimVLA seeds only, dense failed-episode timestep scan."
    echo "- Parent max steps: 400."
    echo "- Replay starts at env step 10."
    echo "- Replay seeds per state: 20."
    echo "- Target action chunk: first 10 SimVLA actions."
    echo "- Scoring/evidence horizons: 10, 20, and 40 steps. H20/H40 continue with SimVLA policy after the initial 10-action target chunk."
    echo "- Fixes active: env runtime counters restored on same-state replay; pick/place task parser v2 preserves target/goal roles; same-state strong-progress alternatives raise action-specific no-progress risk; phase does not use absolute table-object z as transport; weak approach progress becomes GOOD_WEAK/low risk."
    echo
  } > "${LIVE_REPORT}"
}

append_live() {
  {
    echo
    echo "## $(date '+%F %T')"
    echo
    printf '%s\n' "$*"
  } >> "${LIVE_REPORT}"
}

remaining_seconds() {
  local now
  now="$(date +%s)"
  echo "$((DEADLINE_TS - now))"
}

run_diag() {
  local out_dir="$1"
  local name="$2"
  if [[ -s "${out_dir}/dense_replay_counterfactual_samples.jsonl" ]]; then
    python3 -m data_collection_stage9.diagnose_v2_collection \
      "${out_dir}" \
      --out-json "${REPORT_DIR}/${name}_diagnosis.json" \
      --out-md "${REPORT_DIR}/${name}_diagnosis.md" \
      >> "${LOG_DIR}/${name}_diagnosis.log" 2>&1 || true
  fi
}

run_job() {
  local name="$1"
  local suite="$2"
  local task_id="$3"
  local eval_horizon="$4"
  local max_states="$5"
  local replay_seed_base="$6"
  local env_seed="$7"
  local policy_seed_base="$8"
  local stop_step=$((400 - eval_horizon))

  local remain
  remain="$(remaining_seconds)"
  if (( remain < 900 )); then
    append_live "Skipping \`${name}\`: less than 15 minutes remain."
    return 0
  fi

  local out_dir="${DATA_ROOT}/${name}"
  local log="${LOG_DIR}/v6_${name}.log"
  mkdir -p "${out_dir}"

  append_live "Starting \`${name}\`: suite=${suite}, task_id=${task_id}, target_chunk=10, eval_horizon=${eval_horizon}, max_states=${max_states}, 20 seeds/state, timeout=${remain}s."
  echo "[$(date '+%F %T')] START ${name}" | tee -a "${log}"

  timeout --signal=INT --kill-after=120s "${remain}s" \
    python3 -m data_collection_stage9.collect_dense_failure_timestep_mining_v2 \
      --suites "${suite}" \
      --task-ids "${task_id}" \
      --rollouts-per-task 10 \
      --max-parent-episodes 24 \
      --max-failure-episodes 1 \
      --parent-max-steps 400 \
      --start-step 10 \
      --stop-step "${stop_step}" \
      --state-stride 1 \
      --max-replay-states "${max_states}" \
      --parent-policy-chunk-steps 10 \
      --candidate-chunk-steps 10 \
      --eval-horizon "${eval_horizon}" \
      --num-replay-seeds 20 \
      --replay-seed-base "${replay_seed_base}" \
      --env-seed "${env_seed}" \
      --policy-seed-base "${policy_seed_base}" \
      --progress-every-states 25 \
      --out-dir "${out_dir}" \
      >> "${log}" 2>&1
  local status=$?
  echo "[$(date '+%F %T')] END ${name} status=${status}" | tee -a "${log}"

  run_diag "${out_dir}" "${name}"
  local replay_count=0
  local group_count=0
  [[ -f "${out_dir}/dense_replay_counterfactual_samples.jsonl" ]] && replay_count="$(wc -l < "${out_dir}/dense_replay_counterfactual_samples.jsonl")"
  [[ -f "${out_dir}/dense_same_state_group_summaries.jsonl" ]] && group_count="$(wc -l < "${out_dir}/dense_same_state_group_summaries.jsonl")"
  append_live "Finished \`${name}\` with status ${status}. Replay samples=${replay_count}; same-state groups=${group_count}; output=\`${out_dir}\`."

  if (( status == 124 || status == 130 || status == 137 )); then
    append_live "Deadline or interrupt reached during \`${name}\`; stopping queue."
    exit 0
  fi
}

write_live_header
append_live "Bob-only V6 parser/scorer-fix eval-horizon queue launched. Sam is intentionally unused."

job_index=0
for round in 0 1 2 3 4 5 6 7 8 9; do
  for suite in libero_spatial_with_mug libero_object_with_mug; do
    for task_id in 0 1 2 3 4 5; do
      for eval_horizon in 10 20 40; do
        job_index=$((job_index + 1))
        seed_base=$((2026052100 + round * 1000 + job_index * 17))
        max_states=0
        if (( eval_horizon == 20 )); then
          max_states=220
        elif (( eval_horizon == 40 )); then
          max_states=120
        fi
        run_job "h${eval_horizon}_${suite}_task${task_id}_round${round}" "${suite}" "${task_id}" "${eval_horizon}" "${max_states}" "${seed_base}" "${seed_base}" "$((round * 1000 + task_id * 100 + eval_horizon))"
      done
    done
  done
done

append_live "Queue completed before the 15h deadline."
