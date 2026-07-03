#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"

LIBERO_PRO_ROOT="${LIBERO_PRO_ROOT:-/home/redafrix/LIBERO-PRO}"
LIBERO_CONFIG_PATH="${LIBERO_CONFIG_PATH:-${SCRIPT_DIR}/.libero_pro_config}"
PORT="${PORT:-8102}"
TASK_SUITE="${TASK_SUITE:-libero_10_temp}"
NUM_TRIALS="${NUM_TRIALS:-10}"
TASK_ID="${TASK_ID:-}"
VIDEO_OUT="${VIDEO_OUT:-${SCRIPT_DIR}/eval_libero_pro}"
UNCERTAINTY_LOG="${UNCERTAINTY_LOG:-${VIDEO_OUT}/${TASK_SUITE}_uncertainty.jsonl}"
CLIENT_TYPE="${CLIENT_TYPE:-websocket}"
SEED="${SEED:-7}"
REPLAN_STEPS="${REPLAN_STEPS:-5}"
NO_VIDEO="${NO_VIDEO:-false}"
FORCE_LIBERO_PRO_REGEN="${FORCE_LIBERO_PRO_REGEN:-false}"

if [[ ! -d "${LIBERO_PRO_ROOT}" ]]; then
    echo "Missing LIBERO-PRO root: ${LIBERO_PRO_ROOT}" >&2
    echo "Clone the official repo first: https://github.com/Zxy-MLlab/LIBERO-PRO" >&2
    exit 1
fi

export PYTHONPATH="${LIBERO_PRO_ROOT}:${PYTHONPATH:-}"
export LIBERO_CONFIG_PATH

mkdir -p "${LIBERO_CONFIG_PATH}"
cat > "${LIBERO_CONFIG_PATH}/config.yaml" <<EOF
benchmark_root: ${LIBERO_PRO_ROOT}/libero/libero
bddl_files: ${LIBERO_PRO_ROOT}/libero/libero/bddl_files
init_states: ${LIBERO_PRO_ROOT}/libero/libero/init_files
datasets: ${LIBERO_PRO_ROOT}/libero/datasets
assets: ${LIBERO_PRO_ROOT}/libero/libero/assets
EOF

mkdir -p "${SCRIPT_DIR}/libero_pro_overrides"

python - <<PY
import os
import sys
import yaml
import shutil
import fcntl

task_suite = "${TASK_SUITE}"
root = "${LIBERO_PRO_ROOT}"

suffix_to_flag = {
    "_env": "use_environment",
    "_swap": "use_swap",
    "_object": "use_object",
    "_lan": "use_language",
    "_task": "use_task",
}

base_suite = task_suite
selected_flag = None
for suffix, flag in suffix_to_flag.items():
    if task_suite.endswith(suffix):
        base_suite = task_suite[: -len(suffix)]
        selected_flag = flag
        break

if selected_flag is not None:
    target_init_dir = os.path.join(root, "libero", "libero", "init_files", task_suite)
    target_bddl_dir = os.path.join(root, "libero", "libero", "bddl_files", task_suite)
    generated_suite = f"{base_suite}_temp"
    generated_init_dir = os.path.join(root, "libero", "libero", "init_files", generated_suite)
    generated_bddl_dir = os.path.join(root, "libero", "libero", "bddl_files", generated_suite)
    force_regen = "${FORCE_LIBERO_PRO_REGEN}" == "true"
    lock_path = os.path.join(root, f".{base_suite}_pro_generation.lock")

    def remove_path(path):
        if os.path.islink(path) or os.path.isfile(path):
            os.unlink(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)

    def remove_stale_shared_temp_alias(path):
        # Older versions aliased every PRO variant for a base suite to the same
        # base_temp directory, so e.g. object/swap/language silently reused
        # whichever perturbation was generated last. Treat that as missing and
        # materialize a variant-specific copy below.
        try:
            if os.path.islink(path) and os.path.realpath(path) in {
                os.path.realpath(generated_init_dir),
                os.path.realpath(generated_bddl_dir),
            }:
                os.unlink(path)
        except FileNotFoundError:
            pass

    if force_regen:
        for path in [target_init_dir, target_bddl_dir, generated_init_dir, generated_bddl_dir]:
            if os.path.lexists(path):
                remove_path(path)
    else:
        remove_stale_shared_temp_alias(target_init_dir)
        remove_stale_shared_temp_alias(target_bddl_dir)

    def sanitize_bddl_dir(path):
        if not os.path.exists(path):
            return
        for name in os.listdir(path):
            if not name.endswith(".bddl"):
                continue
            fpath = os.path.join(path, name)
            with open(fpath, "r", encoding="utf-8") as f:
                text = f.read()
            fixed = text.replace(" - white_white_porcelain_mug", " - white_porcelain_mug")
            # LIBERO-PRO sometimes creates a second mug instance with an invalid doubled token
            # in the instance / region names. Rename that second mug consistently.
            fixed = fixed.replace("white_white_porcelain_mug_1", "white_porcelain_mug_2")
            fixed = fixed.replace("white_white_porcelain_mug_init_region", "white_porcelain_mug_2_init_region")
            fixed = fixed.replace("living_room_table_white_porcelain_mug_2_init_region", "living_room_table_white_porcelain_mug_2_init_region")

            # Merge duplicate category declarations inside (:objects ...).
            start = fixed.find("(:objects")
            if start != -1:
                end = fixed.find("(:obj_of_interest", start)
                if end != -1:
                    block = fixed[start:end]
                    lines = block.splitlines()
                    merged = []
                    category_to_instances = {}
                    category_order = []
                    for line in lines[1:]:
                        stripped = line.strip()
                        if not stripped:
                            continue
                        if "-" not in stripped:
                            continue
                        left, right = stripped.split("-", 1)
                        instances = left.strip().split()
                        category = right.strip()
                        if category not in category_to_instances:
                            category_to_instances[category] = []
                            category_order.append(category)
                        for inst in instances:
                            if inst not in category_to_instances[category]:
                                category_to_instances[category].append(inst)
                    merged.append(lines[0])
                    for category in category_order:
                        insts = " ".join(category_to_instances[category])
                        merged.append(f"    {insts} - {category}")
                    merged.append("  )")
                    merged.append("")
                    new_block = "\n".join(merged)
                    fixed = fixed[:start] + new_block + fixed[end:]

            if fixed != text:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(fixed)

    if not os.path.exists(target_init_dir) or not os.path.exists(target_bddl_dir):
        print(f"Generating missing LIBERO-PRO suite assets for {task_suite} ...")
        os.makedirs(os.path.dirname(lock_path), exist_ok=True)
        with open(lock_path, "w", encoding="utf-8") as lock_file:
            print(f"Waiting for LIBERO-PRO generation lock: {lock_path}")
            fcntl.flock(lock_file, fcntl.LOCK_EX)
            try:
                if force_regen:
                    for path in [target_init_dir, target_bddl_dir, generated_init_dir, generated_bddl_dir]:
                        if os.path.lexists(path):
                            remove_path(path)

                if os.path.exists(target_init_dir) and os.path.exists(target_bddl_dir):
                    print(f"Assets appeared while waiting for lock: {task_suite}")
                else:
                    sys.path.insert(0, root)
                    import perturbation

                    cfg_path = os.path.join(root, "evaluation_config.yaml")
                    with open(cfg_path, "r", encoding="utf-8") as f:
                        cfg = yaml.safe_load(f)

                    cfg["bddl_files_path"] = os.path.join(root, "libero", "libero", "bddl_files", base_suite)
                    cfg["script_path"] = os.path.join(root, "notebooks", "generate_init_states.py")
                    cfg["init_file_dir"] = os.path.join(root, "libero", "libero", "init_files")
                    cfg["task_suite_name"] = base_suite

                    for flag in ["use_environment", "use_swap", "use_object", "use_language", "use_task"]:
                        cfg[flag] = (flag == selected_flag)

                    ood = cfg.get("ood_task_configs", {})
                    fixed_ood = {}
                    for k, v in ood.items():
                        resolved = v if os.path.isabs(v) else os.path.join(root, v.lstrip("./"))
                        if k == "object":
                            override_dir = os.path.join("${SCRIPT_DIR}", "libero_pro_overrides")
                            fixed_path = os.path.join(override_dir, "ood_object.fixed.yaml")
                            with open(resolved, "r", encoding="utf-8") as f:
                                text = f.read()
                            text = text.replace("\\n    :\\n      - yellow_cabinet\\n      - white_cabinet\\n", "\\n    wooden_cabinet:\\n      - yellow_cabinet\\n      - white_cabinet\\n")
                            with open(fixed_path, "w", encoding="utf-8") as f:
                                f.write(text)
                            resolved = fixed_path
                        fixed_ood[k] = resolved
                    cfg["ood_task_configs"] = fixed_ood

                    perturbation.create_env(configs=cfg)

                    sanitize_bddl_dir(generated_bddl_dir)

                    if os.path.exists(generated_init_dir):
                        print(f"Copying {generated_init_dir} -> {target_init_dir}")
                        shutil.copytree(generated_init_dir, target_init_dir, dirs_exist_ok=True)
                    if os.path.exists(generated_bddl_dir):
                        print(f"Copying {generated_bddl_dir} -> {target_bddl_dir}")
                        shutil.copytree(generated_bddl_dir, target_bddl_dir, dirs_exist_ok=True)
            finally:
                fcntl.flock(lock_file, fcntl.LOCK_UN)

    sanitize_bddl_dir(target_bddl_dir)

    missing_assets = []
    if not os.path.isdir(target_bddl_dir) or not any(name.endswith(".bddl") for name in os.listdir(target_bddl_dir)):
        missing_assets.append(target_bddl_dir)
    if not os.path.isdir(target_init_dir) or not any(name.endswith(".pruned_init") for name in os.listdir(target_init_dir)):
        missing_assets.append(target_init_dir)
    if missing_assets:
        raise RuntimeError(f"LIBERO-PRO asset generation failed for {task_suite}; missing usable assets: {missing_assets}")
PY

if [[ "${NUM_TRIALS}" == "0" ]]; then
    echo "Asset prep completed for ${TASK_SUITE}; NUM_TRIALS=0 so skipping evaluation."
    exit 0
fi

echo "============================================================"
echo "Running LIBERO-PRO evaluation via SimVLA server"
echo "============================================================"
echo "LIBERO_PRO_ROOT: ${LIBERO_PRO_ROOT}"
echo "LIBERO_CONFIG_PATH: ${LIBERO_CONFIG_PATH}"
echo "Task suite: ${TASK_SUITE}"
echo "Trials: ${NUM_TRIALS}"
echo "Task id filter: ${TASK_ID:-<all>}"
echo "Port: ${PORT}"
echo "Uncertainty log: ${UNCERTAINTY_LOG}"
echo "============================================================"

ARGS=(
    --host 127.0.0.1
    --port "${PORT}"
    --client_type "${CLIENT_TYPE}"
    --task_suite "${TASK_SUITE}"
    --num_trials "${NUM_TRIALS}"
    --seed "${SEED}"
    --replan_steps "${REPLAN_STEPS}"
    --video_out "${VIDEO_OUT}"
    --uncertainty_log "${UNCERTAINTY_LOG}"
)

if [[ -n "${TASK_ID}" ]]; then
    ARGS+=(--task_id "${TASK_ID}")
fi

if [[ "${NO_VIDEO}" == "true" ]]; then
    ARGS+=(--no_video)
fi

python "${SCRIPT_DIR}/libero_client.py" "${ARGS[@]}"
