#!/usr/bin/env bash
# Bootstrap and train SimVLA uncertainty on all LIBERO suites from the SmolVLM base.
#
# Default behavior:
#   1. create/activate the SimVLA conda environment
#   2. install SimVLA training dependencies
#   3. download the SmolVLM backbone
#   4. download all LIBERO HDF5 suites
#   5. build LIBERO metadata and normalization stats
#   6. launch train_smolvlm.py with --predict_uncertainty
#
# Common overrides:
#   LIBERO_DATA_DIR=... OUTPUT_DIR=... bash train_simvla_base_all_libero_uncertainty.sh
#   RUN_TRAINING=false bash train_simvla_base_all_libero_uncertainty.sh

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

# =============================================================================
# Conda / installation
# =============================================================================
ENV_NAME="${ENV_NAME:-simvla}"
PYTHON_VERSION="${PYTHON_VERSION:-3.10}"
SETUP_ENV="${SETUP_ENV:-true}"
INSTALL_DEPS="${INSTALL_DEPS:-true}"
INSTALL_FLASH_ATTN="${INSTALL_FLASH_ATTN:-true}"
INSTALL_TENSORFLOW="${INSTALL_TENSORFLOW:-true}"
TORCH_INDEX_URL="${TORCH_INDEX_URL:-https://download.pytorch.org/whl/cu124}"

# =============================================================================
# Download locations
# =============================================================================
MODEL_ROOT="${MODEL_ROOT:-$ROOT/assets/models}"
START_CKPT="${START_CKPT:-}"
SMOLVLM_REPO="${SMOLVLM_REPO:-HuggingFaceTB/SmolVLM-500M-Instruct}"
SMOLVLM_LOCAL_DIR="${SMOLVLM_LOCAL_DIR:-$MODEL_ROOT/SmolVLM-500M-Instruct}"
SMOLVLM_MODEL_PATH="${SMOLVLM_MODEL_PATH:-$SMOLVLM_LOCAL_DIR}"

LIBERO_REPO="${LIBERO_REPO:-yifengzhu-hf/LIBERO-datasets}"
LIBERO_DATA_DIR="${LIBERO_DATA_DIR:-$ROOT/datasets/metas}"
SUBSETS=(${SUBSETS:-libero_10 libero_90 libero_goal libero_object libero_spatial})

TRAIN_METAS_PATH="${TRAIN_METAS_PATH:-$ROOT/datasets/metas/libero_train_all.json}"
NORM_STATS_PATH="${NORM_STATS_PATH:-$ROOT/norm_stats/libero_all_norm.json}"
FORCE_PREPARE="${FORCE_PREPARE:-false}"

# =============================================================================
# Training setup
# =============================================================================
RUN_TRAINING="${RUN_TRAINING:-true}"
OUTPUT_DIR="${OUTPUT_DIR:-$ROOT/runs/simvla_base_all_libero_uncertainty}"
ACTION_MODE="${ACTION_MODE:-libero_joint}"
NUM_ACTIONS="${NUM_ACTIONS:-10}"
IMAGE_SIZE="${IMAGE_SIZE:-384}"

LEARNING_RATE="${LEARNING_RATE:-1e-4}"
LEARNING_COEF="${LEARNING_COEF:-1.0}"
WEIGHT_DECAY="${WEIGHT_DECAY:-0.0}"
BATCH_SIZE="${BATCH_SIZE:-16}"
GRAD_ACCUM_STEPS="${GRAD_ACCUM_STEPS:-16}"
NUM_WORKERS="${NUM_WORKERS:-4}"
ITERS="${ITERS:-200000}"
WARMUP_STEPS="${WARMUP_STEPS:-1000}"
FREEZE_STEPS="${FREEZE_STEPS:-60000}"
FREEZE_MODE="${FREEZE_MODE:-freeze_vlm_entire_run}"
SAVE_INTERVAL="${SAVE_INTERVAL:-10000}"
LOG_INTERVAL="${LOG_INTERVAL:-10}"
MAX_GRAD_NORM="${MAX_GRAD_NORM:-1.0}"
NUM_PROCESSES="${NUM_PROCESSES:-1}"
MAIN_PROCESS_PORT="${MAIN_PROCESS_PORT:-29504}"
CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-0}"

PREDICT_UNCERTAINTY="${PREDICT_UNCERTAINTY:-true}"
UNCERTAINTY_BETA="${UNCERTAINTY_BETA:-0.5}"
UNCERTAINTY_EPS="${UNCERTAINTY_EPS:-1e-6}"
IGNORE_MISMATCHED_CHECKPOINT_SIZES="${IGNORE_MISMATCHED_CHECKPOINT_SIZES:-false}"

USE_LORA="${USE_LORA:-false}"
LORA_RANK="${LORA_RANK:-16}"
LORA_ALPHA="${LORA_ALPHA:-32}"
LORA_DROPOUT="${LORA_DROPOUT:-0.05}"

HIDDEN_SIZE="${HIDDEN_SIZE:-1024}"
DEPTH="${DEPTH:-24}"
NUM_HEADS="${NUM_HEADS:-16}"
USE_ADALN="${USE_ADALN:-false}"

export TF_CPP_MIN_LOG_LEVEL="${TF_CPP_MIN_LOG_LEVEL:-2}"
export HF_HUB_ENABLE_HF_TRANSFER=0
export CUDA_VISIBLE_DEVICES

find_conda_sh() {
    local candidates=(
        "$HOME/miniconda3/etc/profile.d/conda.sh"
        "$HOME/anaconda3/etc/profile.d/conda.sh"
        "/opt/conda/etc/profile.d/conda.sh"
    )
    for candidate in "${candidates[@]}"; do
        if [[ -f "$candidate" ]]; then
            echo "$candidate"
            return 0
        fi
    done
    return 1
}

activate_env() {
    local conda_sh
    conda_sh="$(find_conda_sh)" || {
        echo "Could not find conda.sh. Set up conda first or run with SETUP_ENV=false inside an active env." >&2
        exit 1
    }
    # shellcheck disable=SC1090
    source "$conda_sh"
    if ! conda env list | awk '{print $1}' | grep -qx "$ENV_NAME"; then
        echo "Creating conda env: $ENV_NAME (python=$PYTHON_VERSION)"
        conda create -n "$ENV_NAME" "python=$PYTHON_VERSION" -y
    fi
    # Temporarily disable -u because some conda activation scripts (like cuda-nvcc)
    # reference unset variables.
    set +u
    conda activate "$ENV_NAME"
    set -u
}

install_deps() {
    python -m pip install --upgrade pip
    python -m pip install torch torchvision --index-url "$TORCH_INDEX_URL"
    python -m pip install "transformers>=4.57.0"
    python -m pip install \
        peft accelerate fastapi tensorboard uvicorn json_numpy safetensors scipy \
        einops timm mmengine pyarrow h5py mediapy num2words av wandb websockets \
        msgpack_numpy huggingface_hub tqdm ninja typeguard
    if [[ "$INSTALL_TENSORFLOW" == "true" ]]; then
        python -m pip install tensorflow tensorflow-datasets
    fi
    if [[ "$INSTALL_FLASH_ATTN" == "true" ]]; then
        echo "Installing flash-attn (this may take a while)..."
        if command -v nvcc >/dev/null; then
            python -m pip install flash-attn==2.5.6 --no-build-isolation
        else
            echo "Warning: nvcc not found, attempting to install flash-attn without --no-build-isolation"
            python -m pip install flash-attn==2.5.6
        fi
    fi
}

download_model() {
    local repo_id="$1"
    local out_dir="$2"
    mkdir -p "$out_dir"
    python - "$repo_id" "$out_dir" <<'PY'
import os
import sys
import time
from huggingface_hub import snapshot_download

repo_id, out_dir = sys.argv[1], os.path.abspath(sys.argv[2])
print(f"Downloading {repo_id} -> {out_dir}")

max_retries = 10
for i in range(max_retries):
    try:
        snapshot_download(
            repo_id=repo_id,
            repo_type="model",
            local_dir=out_dir,
            local_dir_use_symlinks=False,
            resume_download=True,
        )
        break
    except Exception as e:
        if i < max_retries - 1:
            print(f"Download attempt {i+1} failed: {e}. Retrying in 10s...")
            time.sleep(10)
        else:
            raise e
PY
}

download_libero() {
    mkdir -p "$LIBERO_DATA_DIR"
    python - "$LIBERO_REPO" "$LIBERO_DATA_DIR" "${SUBSETS[@]}" <<'PY'
import os
import sys
import time
from pathlib import Path
from huggingface_hub import snapshot_download

repo_id = sys.argv[1]
download_dir = Path(sys.argv[2]).expanduser().resolve()
subsets = sys.argv[3:]
expected_counts = {
    "libero_object": 10,
    "libero_goal": 10,
    "libero_spatial": 10,
    "libero_10": 10,
    "libero_90": 90,
}

download_dir.mkdir(parents=True, exist_ok=True)

def count_hdf5(subset: str) -> int:
    subset_dir = download_dir / subset
    if not subset_dir.is_dir():
        return 0
    return sum(1 for _ in subset_dir.glob("*.hdf5"))

for subset in subsets:
    existing = count_hdf5(subset)
    expected = expected_counts.get(subset)
    if expected is not None and existing >= expected:
        print(f"Skipping {subset}: already complete ({existing}/{expected})")
        continue
    suffix = f" ({existing}/{expected})" if expected is not None else f" ({existing} present)"
    print(f"Downloading {subset}{suffix}")
    
    max_retries = 10
    for i in range(max_retries):
        try:
            snapshot_download(
                repo_id=repo_id,
                repo_type="dataset",
                local_dir=str(download_dir),
                allow_patterns=f"{subset}/*",
                local_dir_use_symlinks=False,
                resume_download=True,
            )
            break
        except Exception as e:
            if i < max_retries - 1:
                print(f"Download attempt {i+1} failed: {e}. Retrying in 10s...")
                time.sleep(10)
            else:
                raise e

missing = []
for subset in subsets:
    existing = count_hdf5(subset)
    expected = expected_counts.get(subset)
    print(f"{subset}: {existing} HDF5 files")
    if expected is not None and existing < expected:
        missing.append(f"{subset}: expected {expected}, found {existing}")

if missing:
    raise SystemExit("Incomplete LIBERO download:\n" + "\n".join(missing))
PY
}

prepare_libero() {
    if [[ "$FORCE_PREPARE" == "true" || ! -f "$TRAIN_METAS_PATH" ]]; then
        python create_libero_meta.py \
            --data_dir "$LIBERO_DATA_DIR" \
            --subsets "${SUBSETS[@]}" \
            --output "$TRAIN_METAS_PATH"
    else
        echo "Using existing metadata: $TRAIN_METAS_PATH"
    fi

    if [[ "$FORCE_PREPARE" == "true" || ! -f "$NORM_STATS_PATH" ]]; then
        python compute_libero_norm_stats.py \
            --data_dir "$LIBERO_DATA_DIR" \
            --subsets "${SUBSETS[@]}" \
            --output "$NORM_STATS_PATH"
    else
        echo "Using existing norm stats: $NORM_STATS_PATH"
    fi
}

launch_training() {
    local args
    args="--output_dir ${OUTPUT_DIR} \
        --train_metas_path ${TRAIN_METAS_PATH} \
        --smolvlm_model_path ${SMOLVLM_MODEL_PATH} \
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

    if [[ "$USE_LORA" == "true" ]]; then
        args="${args} --use_lora --lora_rank ${LORA_RANK} --lora_alpha ${LORA_ALPHA} --lora_dropout ${LORA_DROPOUT}"
    fi

    if [[ -n "$START_CKPT" ]]; then
        args="--models ${START_CKPT} ${args}"
    fi

    # Auto-resume logic
    LATEST_CKPT=$(find "${OUTPUT_DIR}" -maxdepth 1 -type d -name "ckpt-*" | sort -V | tail -n 1 || true)
    if [[ -n "$LATEST_CKPT" ]]; then
        echo "Found existing checkpoint directory: $LATEST_CKPT. Resuming..."
        args="--models ${LATEST_CKPT} --resume ${args}"
    fi

    if [[ "$USE_ADALN" == "true" ]]; then
        args="${args} --use_adaln"
    fi
    if [[ "$PREDICT_UNCERTAINTY" == "true" ]]; then
        args="${args} --predict_uncertainty"
    fi
    if [[ "$IGNORE_MISMATCHED_CHECKPOINT_SIZES" == "true" ]]; then
        args="${args} --ignore_mismatched_checkpoint_sizes"
    fi

    echo "============================================================"
    echo "Starting SimVLA base -> all LIBERO uncertainty training"
    echo "============================================================"
    echo "Repo root: $ROOT"
    echo "SmolVLM backbone: $SMOLVLM_MODEL_PATH"
    echo "Start checkpoint: ${START_CKPT:-None, initialize SimVLA action transformer from config}"
    echo "LIBERO data: $LIBERO_DATA_DIR"
    echo "Subsets: ${SUBSETS[*]}"
    echo "Train metadata: $TRAIN_METAS_PATH"
    echo "Norm stats: $NORM_STATS_PATH"
    echo "Output directory: $OUTPUT_DIR"
    echo "Freeze mode: $FREEZE_MODE"
    echo "Use LoRA: $USE_LORA (r=$LORA_RANK, alpha=$LORA_ALPHA)"
    echo "Predict uncertainty: $PREDICT_UNCERTAINTY"
    echo "Ignore mismatched checkpoint sizes: $IGNORE_MISMATCHED_CHECKPOINT_SIZES"
    echo "Effective batch size: $((BATCH_SIZE * NUM_PROCESSES * GRAD_ACCUM_STEPS))"
    echo "============================================================"

    PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \
    accelerate launch \
        --num_processes="$NUM_PROCESSES" \
        --main_process_port "$MAIN_PROCESS_PORT" \
        --mixed_precision bf16 \
        train_smolvlm.py ${args}
}

if [[ "$SETUP_ENV" == "true" ]]; then
    activate_env
fi

if [[ "$INSTALL_DEPS" == "true" ]]; then
    install_deps
fi

if [[ -n "$SMOLVLM_LOCAL_DIR" ]]; then
    download_model "$SMOLVLM_REPO" "$SMOLVLM_LOCAL_DIR"
fi

download_libero
prepare_libero

if [[ "$RUN_TRAINING" == "true" ]]; then
    launch_training
else
    echo "RUN_TRAINING=false, stopping after setup."
fi
