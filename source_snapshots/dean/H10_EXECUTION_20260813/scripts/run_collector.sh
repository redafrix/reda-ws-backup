#!/usr/bin/env bash
set -euo pipefail

WORKSPACE=/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813
PY=/mnt/ai/isaac/envs/env_isaaclab_6_0/bin/python
ISAAC_REPO=/mnt/ai/projects/simvla_reproduction_workspace/franka_wrist_camera_isaaclab
EXP_PATH=/mnt/ai/isaac/envs/env_isaaclab_6_0/lib/python3.12/site-packages/isaacsim/apps

if pgrep -af '/mnt/ai/pi05/openpi/.venv/bin/python.*train_grad_accum.py' >/dev/null; then
    printf 'Refusing launch: pi0.5 train_grad_accum.py is active.\n' >&2
    exit 30
fi
if pgrep -af '[s]imvla_reaching_rollout.py|[c]ollect_isaac_risk.py' >/dev/null; then
    printf 'Refusing launch: another SimVLA/Isaac collector is active.\n' >&2
    exit 31
fi

[[ -x "$PY" ]] || {
    printf 'Missing Isaac Python: %s\n' "$PY" >&2
    exit 32
}
[[ -f "$EXP_PATH/isaacsim.exp.base.kit" ]] || {
    printf 'Missing Isaac Sim experience files: %s\n' "$EXP_PATH" >&2
    exit 33
}

export OMNI_KIT_ACCEPT_EULA=YES
export EXP_PATH
export XDG_CACHE_HOME=/mnt/ai/isaac/cache/xdg
export UV_CACHE_DIR=/mnt/ai/isaac/cache/uv
export PYTHONUNBUFFERED=1
export PYTHONNOUSERSITE=1
export TRANSFORMERS_OFFLINE=1
export HF_HUB_OFFLINE=1
export TOKENIZERS_PARALLELISM=false
export PYTHONPATH="$WORKSPACE/src:$ISAAC_REPO/src${PYTHONPATH:+:$PYTHONPATH}"

cd "$WORKSPACE"
exec "$PY" -u scripts/collect_isaac_risk.py "$@"
