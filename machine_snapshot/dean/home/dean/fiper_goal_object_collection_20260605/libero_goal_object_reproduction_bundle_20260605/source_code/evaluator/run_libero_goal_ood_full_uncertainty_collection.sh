#!/usr/bin/env bash
set -euo pipefail

# Full runtime uncertainty collection for goal-style OOD LIBERO rollouts.
# It combines learned V2W-head scoring, V2W multiseed context disagreement,
# W2A action-candidate disagreement, receding-plan overlap, raw action arrays,
# full V2W token variance arrays, and per-episode success/failure outcomes.

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MODEL_DIR="${ROOT_DIR}/model"
PYTHON="${PYTHON:-${MODEL_DIR}/.venv/bin/python}"
WORLD_ROOT="$(cd "${ROOT_DIR}/.." && pwd)"

OOD_IMPL="${OOD_IMPL:-plus}" # plus or pro
case "${OOD_IMPL}" in
  plus)
    LIBERO_ROOT="${LIBERO_PLUS_DIR:-${WORLD_ROOT}/LIBERO-plus}"
    LIBERO_CONFIG_PATH_DEFAULT="${LIBERO_CONFIG_PATH_DEFAULT:-${WORLD_ROOT}/.libero_plus}"
    TASK_SUITE_NAME="${TASK_SUITE_NAME:-libero_goal}"
    TASK_IDS="${TASK_IDS:-690,691,692,693,694,711,712,713,714,715,743,744,745,746,747,783,784,785,786,787,831,832,833,834,835,881,882,883,884,885,930,931,932,933,934,979,980,981,982,983,1025,1026,1027,1028,1029,1056,1057,1058,1059,1060}"
    ;;
  pro)
    LIBERO_ROOT="${LIBERO_PRO_ROOT:-${WORLD_ROOT}/LIBERO-PRO}"
    LIBERO_CONFIG_PATH_DEFAULT="${LIBERO_CONFIG_PATH_DEFAULT:-${LIBERO_ROOT}/local_config}"
    # This installed LIBERO-PRO checkout registers libero_goal_object_ood but
    # does not include matching BDDL/init files. libero_goal_object is the
    # present goal object-shift suite with runnable assets.
    TASK_SUITE_NAME="${TASK_SUITE_NAME:-libero_goal_object}"
    TASK_IDS="${TASK_IDS:-0-9}"
    ;;
  *)
    echo "OOD_IMPL must be 'plus' or 'pro', got '${OOD_IMPL}'." >&2
    exit 2
    ;;
esac

if [[ -z "${LIBERO_CONFIG_PATH:-}" ]]; then
  RUNTIME_LIBERO_CONFIG_DIR="${ROOT_DIR}/.runtime_libero_configs/${OOD_IMPL}"
  mkdir -p "${RUNTIME_LIBERO_CONFIG_DIR}"
  cat > "${RUNTIME_LIBERO_CONFIG_DIR}/config.yaml" <<EOF
benchmark_root: ${LIBERO_ROOT}/libero/libero
bddl_files: ${LIBERO_ROOT}/libero/libero/bddl_files
init_states: ${LIBERO_ROOT}/libero/libero/init_files
datasets: ${LIBERO_ROOT}/libero/datasets
assets: ${LIBERO_ROOT}/libero/libero/assets
EOF
  LIBERO_CONFIG_PATH="${RUNTIME_LIBERO_CONFIG_DIR}"
fi

export LIBERO_CONFIG_PATH
export PYTHONPATH="${ROOT_DIR}:${MODEL_DIR}:${LIBERO_ROOT}${PYTHONPATH:+:${PYTHONPATH}}"
export TOKENIZERS_PARALLELISM="${TOKENIZERS_PARALLELISM:-false}"
export TRANSFORMERS_NO_TF="${TRANSFORMERS_NO_TF:-1}"
export USE_TF="${USE_TF:-0}"
export TF_CPP_MIN_LOG_LEVEL="${TF_CPP_MIN_LOG_LEVEL:-3}"
export PYOPENGL_PLATFORM="${PYOPENGL_PLATFORM:-egl}"
export MUJOCO_GL="${MUJOCO_GL:-egl}"
export CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-0}"
export MPLCONFIGDIR="${MPLCONFIGDIR:-/tmp/matplotlib-${USER:-user}}"

VIDEO_MODEL="${VIDEO_MODEL:-${MODEL_DIR}/checkpoints/video_backbone/v2w_libero_goal_agentview_lora_rank256_lr1.778e-04_bsz32_iter_000007020_fused.pt}"
ACTION_MODEL="${ACTION_MODEL:-${MODEL_DIR}/checkpoints/action_decoder/w2a_libero_goal_half_v2w_libero_goal_agentview_lora_rank256_lr1.778e-04_bsz32_iter_000007020_fused_lr1.000e-04_layer20_bsz128_iter_000050022.pt}"
DATASET_STATS="${DATASET_STATS:-${MODEL_DIR}/checkpoints/dataset_statistics/libero_goal_half.json}"
EXPERIMENT="${EXPERIMENT:-w2a_libero_goal_half_v2w_libero_goal_agentview_lora_rank256_lr1.778e-04_bsz32_iter_000007020_fused_lr1.000e-04_layer20_bsz128}"

HEAD_KIND="${HEAD_KIND:-modeb10}" # modeb10 or flow
case "${HEAD_KIND}" in
  modeb10)
    V2W_UNCERTAINTY_HEAD="${V2W_UNCERTAINTY_HEAD:-${MODEL_DIR}/checkpoints/uncertainty/v2w_heads/libero_goal_variantA_nll_plus_energy_stride7_eps500_modeB10_from_flow_fixedmask_2ep_20260531_120356/v2w_uncertainty_head.pt}"
    ;;
  flow)
    V2W_UNCERTAINTY_HEAD="${V2W_UNCERTAINTY_HEAD:-${MODEL_DIR}/checkpoints/uncertainty/v2w_heads/libero_goal_variantA_nll_plus_energy_stride7_eps500_flowonly_safe_20260529_170855/v2w_uncertainty_head.pt}"
    ;;
  *)
    echo "HEAD_KIND must be 'modeb10' or 'flow', got '${HEAD_KIND}'." >&2
    exit 2
    ;;
esac

V2W_CALIBRATION="${V2W_CALIBRATION:-${MODEL_DIR}/checkpoints/uncertainty/v2w_heads/libero_goal_stride7_variantA_calibration.npz}"
V2W_UNCERTAINTY_VARIANT="${V2W_UNCERTAINTY_VARIANT:-a}"

IMG_HORIZON="${IMG_HORIZON:-5}"
LOWDIM_HORIZON="${LOWDIM_HORIZON:-1}"
STOP_VIDEO_DENOISING_STEP="${STOP_VIDEO_DENOISING_STEP:-0}"
VAM_NUM_SAMPLING_STEPS="${VAM_NUM_SAMPLING_STEPS:-2}"
NUM_EXECUTE_ACTIONS="${NUM_EXECUTE_ACTIONS:-14}"
NUM_TRIALS_PER_TASK="${NUM_TRIALS_PER_TASK:-1}"
TRIAL_START_INDEX="${TRIAL_START_INDEX:-0}"
NUM_STEPS_WAIT="${NUM_STEPS_WAIT:-10}"
MAX_EPISODE_STEPS="${MAX_EPISODE_STEPS:-}"
SEED="${SEED:-0}"
PROMPT_SOURCE="${PROMPT_SOURCE:-bddl_language}"
SAVE_VIDEOS="${SAVE_VIDEOS:-0}"
VALIDATE_ONLY="${VALIDATE_ONLY:-0}"
PRECOMPUTE_EMBEDDINGS="${PRECOMPUTE_EMBEDDINGS:-0}"
BALANCED_SUCCESS_TARGET="${BALANCED_SUCCESS_TARGET:-0}"
BALANCED_FAILURE_TARGET="${BALANCED_FAILURE_TARGET:-0}"

UQ_NUM_ACTION_CANDIDATES="${UQ_NUM_ACTION_CANDIDATES:-8}"
UQ_ACTION_CANDIDATE_BATCH_SIZE="${UQ_ACTION_CANDIDATE_BATCH_SIZE:-4}"
UQ_NUM_WORLD_CANDIDATES="${UQ_NUM_WORLD_CANDIDATES:-3}"
SAVE_V2W_VARIANCE_ARRAYS="${SAVE_V2W_VARIANCE_ARRAYS:-1}"
UQ_SAVE_CANDIDATE_ARRAYS="${UQ_SAVE_CANDIDATE_ARRAYS:-1}"
UQ_CONTROL_POLICY="${UQ_CONTROL_POLICY:-first_candidate}"
UQ_MIN_EXECUTE_ACTIONS="${UQ_MIN_EXECUTE_ACTIONS:-1}"
UQ_ADAPTIVE_SPIKE_Z="${UQ_ADAPTIVE_SPIKE_Z:-3.0}"
UQ_ADAPTIVE_SPIKE_WARMUP="${UQ_ADAPTIVE_SPIKE_WARMUP:-4}"
UQ_ADAPTIVE_VARIANCE_FLOOR="${UQ_ADAPTIVE_VARIANCE_FLOOR:-0.0}"

EVAL_RANK="${EVAL_RANK:-0}"
EVAL_WORLD_SIZE="${EVAL_WORLD_SIZE:-1}"
TRIAL_END_INDEX=$((TRIAL_START_INDEX + NUM_TRIALS_PER_TASK - 1))
RUN_SUFFIX="${RUN_SUFFIX:-${OOD_IMPL}_${HEAD_KIND}_t${TRIAL_START_INDEX}to${TRIAL_END_INDEX}_r${EVAL_RANK}of${EVAL_WORLD_SIZE}}"
ACTION_STEM="$(basename "${ACTION_MODEL}" .pt)"
UQ_ADAPTIVE_SPIKE_Z_TAG="$("${PYTHON}" -c 'import sys; print(f"{float(sys.argv[1]):g}")' "${UQ_ADAPTIVE_SPIKE_Z}")"
UQ_ADAPTIVE_VARIANCE_FLOOR_TAG="$("${PYTHON}" -c 'import sys; print(f"{float(sys.argv[1]):g}")' "${UQ_ADAPTIVE_VARIANCE_FLOOR}")"
RUN_LABEL="${ACTION_STEM}_step${VAM_NUM_SAMPLING_STEPS}_stopafter${STOP_VIDEO_DENOISING_STEP}_execute${NUM_EXECUTE_ACTIONS}_uqK${UQ_NUM_ACTION_CANDIDATES}_w2ab${UQ_ACTION_CANDIDATE_BATCH_SIZE}_wuqK${UQ_NUM_WORLD_CANDIDATES}_v2wuq_${RUN_SUFFIX}"
case "${UQ_CONTROL_POLICY}" in
  first_candidate)
    ;;
  action_cycle)
    RUN_LABEL="${ACTION_STEM}_step${VAM_NUM_SAMPLING_STEPS}_stopafter${STOP_VIDEO_DENOISING_STEP}_execute${NUM_EXECUTE_ACTIONS}_uqK${UQ_NUM_ACTION_CANDIDATES}_w2ab${UQ_ACTION_CANDIDATE_BATCH_SIZE}_wuqK${UQ_NUM_WORLD_CANDIDATES}_v2wuq_ctrlcycle_min${UQ_MIN_EXECUTE_ACTIONS}_z${UQ_ADAPTIVE_SPIKE_Z_TAG}_vf${UQ_ADAPTIVE_VARIANCE_FLOOR_TAG}_${RUN_SUFFIX}"
    ;;
  action_medoid)
    RUN_LABEL="${ACTION_STEM}_step${VAM_NUM_SAMPLING_STEPS}_stopafter${STOP_VIDEO_DENOISING_STEP}_execute${NUM_EXECUTE_ACTIONS}_uqK${UQ_NUM_ACTION_CANDIDATES}_w2ab${UQ_ACTION_CANDIDATE_BATCH_SIZE}_wuqK${UQ_NUM_WORLD_CANDIDATES}_v2wuq_ctrlmedoid_min${UQ_MIN_EXECUTE_ACTIONS}_z${UQ_ADAPTIVE_SPIKE_Z_TAG}_vf${UQ_ADAPTIVE_VARIANCE_FLOOR_TAG}_${RUN_SUFFIX}"
    ;;
  action_antimedoid)
    RUN_LABEL="${ACTION_STEM}_step${VAM_NUM_SAMPLING_STEPS}_stopafter${STOP_VIDEO_DENOISING_STEP}_execute${NUM_EXECUTE_ACTIONS}_uqK${UQ_NUM_ACTION_CANDIDATES}_w2ab${UQ_ACTION_CANDIDATE_BATCH_SIZE}_wuqK${UQ_NUM_WORLD_CANDIDATES}_v2wuq_ctrlantimed_min${UQ_MIN_EXECUTE_ACTIONS}_z${UQ_ADAPTIVE_SPIKE_Z_TAG}_vf${UQ_ADAPTIVE_VARIANCE_FLOOR_TAG}_${RUN_SUFFIX}"
    ;;
  adaptive_horizon)
    RUN_LABEL="${ACTION_STEM}_step${VAM_NUM_SAMPLING_STEPS}_stopafter${STOP_VIDEO_DENOISING_STEP}_execute${NUM_EXECUTE_ACTIONS}_uqK${UQ_NUM_ACTION_CANDIDATES}_w2ab${UQ_ACTION_CANDIDATE_BATCH_SIZE}_wuqK${UQ_NUM_WORLD_CANDIDATES}_v2wuq_ctrladap_min${UQ_MIN_EXECUTE_ACTIONS}_z${UQ_ADAPTIVE_SPIKE_Z_TAG}_vf${UQ_ADAPTIVE_VARIANCE_FLOOR_TAG}_${RUN_SUFFIX}"
    ;;
  medoid_adaptive_horizon)
    RUN_LABEL="${ACTION_STEM}_step${VAM_NUM_SAMPLING_STEPS}_stopafter${STOP_VIDEO_DENOISING_STEP}_execute${NUM_EXECUTE_ACTIONS}_uqK${UQ_NUM_ACTION_CANDIDATES}_w2ab${UQ_ACTION_CANDIDATE_BATCH_SIZE}_wuqK${UQ_NUM_WORLD_CANDIDATES}_v2wuq_ctrlmedadap_min${UQ_MIN_EXECUTE_ACTIONS}_z${UQ_ADAPTIVE_SPIKE_Z_TAG}_vf${UQ_ADAPTIVE_VARIANCE_FLOOR_TAG}_${RUN_SUFFIX}"
    ;;
  world_action_medoid)
    RUN_LABEL="${ACTION_STEM}_step${VAM_NUM_SAMPLING_STEPS}_stopafter${STOP_VIDEO_DENOISING_STEP}_execute${NUM_EXECUTE_ACTIONS}_uqK${UQ_NUM_ACTION_CANDIDATES}_w2ab${UQ_ACTION_CANDIDATE_BATCH_SIZE}_wuqK${UQ_NUM_WORLD_CANDIDATES}_v2wuq_ctrlwmedoid_min${UQ_MIN_EXECUTE_ACTIONS}_z${UQ_ADAPTIVE_SPIKE_Z_TAG}_vf${UQ_ADAPTIVE_VARIANCE_FLOOR_TAG}_${RUN_SUFFIX}"
    ;;
  world_lowest_v2w_variance)
    RUN_LABEL="${ACTION_STEM}_step${VAM_NUM_SAMPLING_STEPS}_stopafter${STOP_VIDEO_DENOISING_STEP}_execute${NUM_EXECUTE_ACTIONS}_uqK${UQ_NUM_ACTION_CANDIDATES}_w2ab${UQ_ACTION_CANDIDATE_BATCH_SIZE}_wuqK${UQ_NUM_WORLD_CANDIDATES}_v2wuq_ctrlwlowvar_min${UQ_MIN_EXECUTE_ACTIONS}_z${UQ_ADAPTIVE_SPIKE_Z_TAG}_vf${UQ_ADAPTIVE_VARIANCE_FLOOR_TAG}_${RUN_SUFFIX}"
    ;;
  *)
    echo "UQ_CONTROL_POLICY must be first_candidate, action_cycle, action_medoid, action_antimedoid, adaptive_horizon, medoid_adaptive_horizon, world_action_medoid, or world_lowest_v2w_variance; got ${UQ_CONTROL_POLICY}." >&2
    exit 2
    ;;
esac
RESULT_DIR="${ROOT_DIR}/results/${RUN_LABEL}/${TASK_SUITE_NAME}"

if (( ${#RUN_LABEL} > 255 )); then
  echo "Result directory component is too long (${#RUN_LABEL} > 255): ${RUN_LABEL}" >&2
  echo "Use a shorter RUN_SUFFIX; the action-model stem is already included automatically." >&2
  exit 1
fi

MANIFEST_DIR="${MODEL_DIR}/checkpoints/precomputed_embeddings/${OOD_IMPL}_goal_manifests"
PROMPTS_FILE="${MANIFEST_DIR}/${OOD_IMPL}_goal_${PROMPT_SOURCE}_prompts.txt"
T5_GPU_MEMORY="${T5_GPU_MEMORY:-24GiB}"
T5_CPU_MEMORY="${T5_CPU_MEMORY:-20GiB}"
T5_DTYPE="${T5_DTYPE:-float16}"
T5_OFFLOAD_DIR="${T5_OFFLOAD_DIR:-/tmp/t5_11b_offload_${OOD_IMPL}_goal_full_uq}"

export TASK_IDS PROMPT_SOURCE TASK_SUITE_NAME PROMPTS_FILE
export V2W_UNCERTAINTY_HEAD V2W_CALIBRATION V2W_UNCERTAINTY_VARIANT
export NUM_TRIALS_PER_TASK TRIAL_START_INDEX RESULT_DIR

cd "${ROOT_DIR}"
mkdir -p "${MANIFEST_DIR}"

for required_path in "${VIDEO_MODEL}" "${ACTION_MODEL}" "${DATASET_STATS}" "${V2W_UNCERTAINTY_HEAD}" "${V2W_CALIBRATION}"; do
  if [[ ! -f "${required_path}" ]]; then
    echo "Missing required file: ${required_path}" >&2
    exit 1
  fi
done

"${PYTHON}" - <<'PY'
import json
import os

import torch

from model.uncertainty import V2WCalibration, V2WUncertaintyModel

variant = os.environ["V2W_UNCERTAINTY_VARIANT"].lower()
use_variant_b = variant == "b"
model = V2WUncertaintyModel(use_variant_b=use_variant_b)
model.load_state_dict(torch.load(os.environ["V2W_UNCERTAINTY_HEAD"], map_location="cpu"))
calibration = V2WCalibration(num_bins=10, use_variant_b=use_variant_b)
calibration.load(os.environ["V2W_CALIBRATION"])
summary = calibration.summary()
if not summary["finite"] or not summary["positive"]:
    raise SystemExit(f"Invalid V2W calibration baseline: {json.dumps(summary, sort_keys=True)}")
print(f"verified V2W uncertainty checkpoint and calibration: {json.dumps(summary, sort_keys=True)}")
PY

"${PYTHON}" - <<'PY'
import os
import sys
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

from libero.libero import benchmark

from eval.libero.run import get_task_init_states_compatible, parse_task_ids, task_description_for_policy

task_ids = parse_task_ids(os.environ["TASK_IDS"])
prompt_source = os.environ["PROMPT_SOURCE"]
task_suite_name = os.environ["TASK_SUITE_NAME"]
prompts_file = Path(os.environ["PROMPTS_FILE"])
num_trials_per_task = int(os.environ["NUM_TRIALS_PER_TASK"])
trial_start_index = int(os.environ["TRIAL_START_INDEX"])
required_initial_states = trial_start_index + num_trials_per_task

with redirect_stdout(StringIO()):
    suite = benchmark.get_benchmark_dict()[task_suite_name]()

prompts = []
for task_id in task_ids:
    if task_id < 0 or task_id >= suite.n_tasks:
        raise SystemExit(f"task_id={task_id} out of range for {task_suite_name} with {suite.n_tasks} tasks")
    initial_states = get_task_init_states_compatible(suite, task_id)
    if required_initial_states > len(initial_states):
        raise SystemExit(
            f"task_id={task_id} has {len(initial_states)} initial states, "
            f"but trials {trial_start_index}-{required_initial_states - 1} were requested"
        )
    prompts.append(task_description_for_policy(suite.get_task(task_id), prompt_source))

unique_prompts = list(dict.fromkeys(prompts))
prompts_file.write_text("\n".join(unique_prompts) + "\n", encoding="utf-8")
print(
    f"wrote {len(unique_prompts)} unique prompts to {prompts_file}; "
    f"validated trial range {trial_start_index}-{required_initial_states - 1}"
)
sys.stdout.flush()
sys.stderr.flush()
os._exit(0)
PY

if [[ "${PRECOMPUTE_EMBEDDINGS}" == "1" ]]; then
  "${PYTHON}" model/scripts/precompute_libero_embeddings_standalone.py \
    --checkpoint-dir "${MODEL_DIR}/checkpoints" \
    --prompts-file "${PROMPTS_FILE}" \
    --gpu-memory "${T5_GPU_MEMORY}" \
    --cpu-memory "${T5_CPU_MEMORY}" \
    --dtype "${T5_DTYPE}" \
    --offload-dir "${T5_OFFLOAD_DIR}"
fi

"${PYTHON}" - <<'PY'
import os
import sys
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

from libero.libero import benchmark
from imaginaire.constants import CHECKPOINTS_DIR

from eval.libero.prompt_embeddings import prompt_embedding_filename
from eval.libero.run import parse_task_ids, task_description_for_policy

task_ids = parse_task_ids(os.environ["TASK_IDS"])
prompt_source = os.environ["PROMPT_SOURCE"]
task_suite_name = os.environ["TASK_SUITE_NAME"]
embedding_dir = Path(CHECKPOINTS_DIR) / "precomputed_embeddings"

with redirect_stdout(StringIO()):
    suite = benchmark.get_benchmark_dict()[task_suite_name]()

missing = []
for task_id in task_ids:
    prompt = task_description_for_policy(suite.get_task(task_id), prompt_source)
    path = embedding_dir / prompt_embedding_filename(prompt)
    if not path.exists():
        missing.append((task_id, prompt, path))

if missing:
    for task_id, prompt, path in missing:
        print(f"missing embedding task_id={task_id} prompt={prompt!r} path={path}")
    raise SystemExit(f"{len(missing)} required prompt embeddings are missing; rerun with PRECOMPUTE_EMBEDDINGS=1")

print(f"verified embeddings for {len(task_ids)} task instances")
sys.stdout.flush()
sys.stderr.flush()
os._exit(0)
PY

if [[ "${VALIDATE_ONLY}" == "1" ]]; then
  echo "VALIDATE_ONLY=1: preflight passed; not starting rollout."
  echo "Expected result directory: ${RESULT_DIR}"
  exit 0
fi

save_video_flag=(--no-save-videos)
if [[ "${SAVE_VIDEOS}" == "1" ]]; then
  save_video_flag=(--save-videos)
fi

variance_array_flag=(--no-v2w-uncertainty-save-variance-arrays)
if [[ "${SAVE_V2W_VARIANCE_ARRAYS}" == "1" ]]; then
  variance_array_flag=(--v2w-uncertainty-save-variance-arrays)
fi

candidate_array_flag=(--no-uq-save-candidate-arrays)
if [[ "${UQ_SAVE_CANDIDATE_ARRAYS}" == "1" ]]; then
  candidate_array_flag=(--uq-save-candidate-arrays)
fi

balanced_target_args=()
if (( BALANCED_SUCCESS_TARGET > 0 || BALANCED_FAILURE_TARGET > 0 )); then
  balanced_target_args=(
    --balanced-success-target "${BALANCED_SUCCESS_TARGET}"
    --balanced-failure-target "${BALANCED_FAILURE_TARGET}"
  )
fi

max_episode_step_args=()
if [[ -n "${MAX_EPISODE_STEPS}" ]]; then
  max_episode_step_args=(--max-episode-steps "${MAX_EPISODE_STEPS}")
fi

"${PYTHON}" eval/libero/run.py \
  --vam-experiment-name "${EXPERIMENT}" \
  --vam-video-model-path "${VIDEO_MODEL}" \
  --vam-action-model-path "${ACTION_MODEL}" \
  --vam-dataset-statistics-path "${DATASET_STATS}" \
  --vam-img-horizon "${IMG_HORIZON}" \
  --vam-lowdim-horizon "${LOWDIM_HORIZON}" \
  --vam-stop-video-denoising-step "${STOP_VIDEO_DENOISING_STEP}" \
  --vam-num-execute-actions "${NUM_EXECUTE_ACTIONS}" \
  --vam-num-sampling-steps "${VAM_NUM_SAMPLING_STEPS}" \
  --task-suite-name "${TASK_SUITE_NAME}" \
  --num-trials-per-task "${NUM_TRIALS_PER_TASK}" \
  --trial-start-index "${TRIAL_START_INDEX}" \
  --num-steps-wait "${NUM_STEPS_WAIT}" \
  "${max_episode_step_args[@]}" \
  --seed "${SEED}" \
  --eval-rank "${EVAL_RANK}" \
  --eval-world-size "${EVAL_WORLD_SIZE}" \
  --no-use-text-encoder \
  --prompt-source "${PROMPT_SOURCE}" \
  --task-ids "${TASK_IDS}" \
  --run-suffix "${RUN_SUFFIX}" \
  --uq-num-action-candidates "${UQ_NUM_ACTION_CANDIDATES}" \
  --uq-action-candidate-batch-size "${UQ_ACTION_CANDIDATE_BATCH_SIZE}" \
  --uq-num-world-candidates "${UQ_NUM_WORLD_CANDIDATES}" \
  --uq-log-action-candidates \
  "${candidate_array_flag[@]}" \
  --v2w-uncertainty-head-path "${V2W_UNCERTAINTY_HEAD}" \
  --v2w-uncertainty-calibration-path "${V2W_CALIBRATION}" \
  --v2w-uncertainty-variant "${V2W_UNCERTAINTY_VARIANT}" \
  --uq-control-policy "${UQ_CONTROL_POLICY}" \
  --uq-min-execute-actions "${UQ_MIN_EXECUTE_ACTIONS}" \
  --uq-adaptive-spike-z "${UQ_ADAPTIVE_SPIKE_Z}" \
  --uq-adaptive-spike-warmup "${UQ_ADAPTIVE_SPIKE_WARMUP}" \
  --uq-adaptive-variance-floor "${UQ_ADAPTIVE_VARIANCE_FLOOR}" \
  "${balanced_target_args[@]}" \
  "${variance_array_flag[@]}" \
  "${save_video_flag[@]}"

"${PYTHON}" scripts/analyze_v2w_uncertainty_rollouts.py "${RESULT_DIR}"
