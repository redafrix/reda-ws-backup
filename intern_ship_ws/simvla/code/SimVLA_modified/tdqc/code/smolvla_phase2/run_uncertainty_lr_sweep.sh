#!/usr/bin/env bash
# Single-run uncertainty finetune launcher for LIBERO.
# Kept at the old path/name so existing habits still work.

set -euo pipefail

WS_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

# =============================================================================
# Paths
# =============================================================================
PRETRAINED_CKPT="${PRETRAINED_CKPT:-$WS_ROOT/assets/models/huggingface/SimVLA-LIBERO}"
TRAIN_METAS_PATH="${TRAIN_METAS_PATH:-$ROOT/datasets/metas/libero_train.json}"
NORM_STATS_PATH="${NORM_STATS_PATH:-$ROOT/norm_stats/libero_norm.json}"
OUTPUT_DIR="${OUTPUT_DIR:-$WS_ROOT/outputs/runs/simvla_libero_uncertainty}"

BATCH_SIZE="${BATCH_SIZE:-32}"
GRAD_ACCUM_STEPS="${GRAD_ACCUM_STEPS:-1}"
LEARNING_RATE="${LEARNING_RATE:-5e-5}"
LEARNING_COEF="${LEARNING_COEF:-1.0}"
WEIGHT_DECAY="${WEIGHT_DECAY:-1e-4}"
ITERS="${ITERS:-10000}"
WARMUP_STEPS="${WARMUP_STEPS:-100}"
FREEZE_STEPS="${FREEZE_STEPS:-0}"
FREEZE_MODE="${FREEZE_MODE:-none}"
NUM_PROCESSES="${NUM_PROCESSES:-1}"
MAIN_PROCESS_PORT="${MAIN_PROCESS_PORT:-29501}"
NUM_WORKERS="${NUM_WORKERS:-4}"
SAVE_INTERVAL="${SAVE_INTERVAL:-1000}"
LOG_INTERVAL="${LOG_INTERVAL:-10}"
MAX_GRAD_NORM="${MAX_GRAD_NORM:-1.0}"

# =============================================================================
# Model config: match the local SimVLA-LIBERO checkpoint
# =============================================================================
SMOLVLM_MODEL="${SMOLVLM_MODEL:-$WS_ROOT/assets/models/huggingface/SmolVLM-500M-Instruct}"
HIDDEN_SIZE="${HIDDEN_SIZE:-1024}"
DEPTH="${DEPTH:-24}"
NUM_HEADS="${NUM_HEADS:-16}"
USE_ADALN="${USE_ADALN:-false}"
NUM_ACTIONS="${NUM_ACTIONS:-10}"
ACTION_MODE="${ACTION_MODE:-libero_joint}"
IMAGE_SIZE="${IMAGE_SIZE:-384}"

# =============================================================================
# Uncertainty config
# =============================================================================
PREDICT_UNCERTAINTY="${PREDICT_UNCERTAINTY:-true}"
UNCERTAINTY_BETA="${UNCERTAINTY_BETA:-0.5}"
UNCERTAINTY_EPS="${UNCERTAINTY_EPS:-1e-6}"

if [[ ! -d "$PRETRAINED_CKPT" ]]; then
    echo "Missing pretrained checkpoint: $PRETRAINED_CKPT" >&2
    exit 1
fi

if [[ ! -f "$TRAIN_METAS_PATH" ]]; then
    echo "Missing training metadata: $TRAIN_METAS_PATH" >&2
    exit 1
fi

if [[ ! -f "$NORM_STATS_PATH" ]]; then
    echo "Missing norm stats: $NORM_STATS_PATH" >&2
    exit 1
fi

ARGS="--models ${PRETRAINED_CKPT} \
    --output_dir ${OUTPUT_DIR} \
    --train_metas_path ${TRAIN_METAS_PATH} \
    --smolvlm_model_path ${SMOLVLM_MODEL} \
    --action_mode ${ACTION_MODE} \
    --batch_size ${BATCH_SIZE} \
    --grad_accum_steps ${GRAD_ACCUM_STEPS} \
    --learning_rate ${LEARNING_RATE} \
    --learning_coef ${LEARNING_COEF} \
    --weight_decay ${WEIGHT_DECAY} \
    --num_actions ${NUM_ACTIONS} \
    --iters ${ITERS} \
    --warmup_steps ${WARMUP_STEPS} \
    --freeze_steps ${FREEZE_STEPS} \
    --freeze_mode ${FREEZE_MODE} \
    --hidden_size ${HIDDEN_SIZE} \
    --depth ${DEPTH} \
    --num_heads ${NUM_HEADS} \
    --num_workers ${NUM_WORKERS} \
    --save_interval ${SAVE_INTERVAL} \
    --log_interval ${LOG_INTERVAL} \
    --image_size ${IMAGE_SIZE} \
    --norm_stats_path ${NORM_STATS_PATH} \
    --max_grad_norm ${MAX_GRAD_NORM} \
    --uncertainty_beta ${UNCERTAINTY_BETA} \
    --uncertainty_eps ${UNCERTAINTY_EPS}"

if [[ "${USE_ADALN}" == "true" ]]; then
    ARGS="${ARGS} --use_adaln"
fi

if [[ "${PREDICT_UNCERTAINTY}" == "true" ]]; then
    ARGS="${ARGS} --predict_uncertainty"
fi

echo "============================================================"
echo "Starting SimVLA uncertainty finetuning on LIBERO"
echo "============================================================"
echo "WS root: ${WS_ROOT}"
echo "Pretrained checkpoint: ${PRETRAINED_CKPT}"
echo "Train metas: ${TRAIN_METAS_PATH}"
echo "Norm stats: ${NORM_STATS_PATH}"
echo "Output directory: ${OUTPUT_DIR}"
echo "Learning rate: ${LEARNING_RATE}"
echo "Freeze mode: ${FREEZE_MODE}"
echo "Freeze steps: ${FREEZE_STEPS}"
echo "Iterations: ${ITERS}"
echo "Batch size: ${BATCH_SIZE}"
echo "Gradient accumulation steps: ${GRAD_ACCUM_STEPS}"
echo "Effective batch size: $((BATCH_SIZE * NUM_PROCESSES * GRAD_ACCUM_STEPS))"
echo "Predict uncertainty: ${PREDICT_UNCERTAINTY}"
echo "Model config: hidden=${HIDDEN_SIZE} depth=${DEPTH} heads=${NUM_HEADS}"
echo "============================================================"

PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \
accelerate launch \
    --num_processes="${NUM_PROCESSES}" \
    --main_process_port "${MAIN_PROCESS_PORT}" \
    --mixed_precision bf16 \
    train_smolvlm.py ${ARGS}
