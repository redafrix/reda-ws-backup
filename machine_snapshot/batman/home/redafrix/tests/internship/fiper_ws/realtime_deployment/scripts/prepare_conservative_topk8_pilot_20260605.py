#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import secrets
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = ROOT / "configs"
RUN_ID = "conservative_topk8_midrange_pilot_20260605"
SEED_MANIFEST = CONFIG_DIR / f"{RUN_ID}_seed_manifest.json"
NUM_SEEDS = 50
PILOT_EPISODES = 12


HOSTS = {
    "bob": {
        "task_id": 7,
        "template": CONFIG_DIR / "canonical_dean_bob_task0_4policy_seq100_20260604_bob_risk_unc_topk8.json",
        "run_root": "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/runs",
        "python": "/usr/bin/python3",
        "runner": "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/scripts/run_dean_uncertainty_realtime_policy_v1.py",
        "activate": "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/activate_simvla_bob.sh",
    },
    "dean": {
        "task_id": 8,
        "template": CONFIG_DIR / "canonical_dean_bob_task0_4policy_seq100_20260604_dean_risk_unc_topk8.json",
        "run_root": "/home/dean/fiper_uncertainty_collection/realtime_deployment/runs",
        "python": "/home/redafrix/miniconda3/envs/simvla/bin/python",
        "runner": "/home/dean/fiper_uncertainty_collection/realtime_deployment/scripts/run_dean_uncertainty_realtime_policy_v1.py",
        "activate": "",
    },
}


VARIANTS = {
    "01_modified_simvla": {
        "policy": "simvla_only",
        "controls": {},
    },
    "02_topk8_protective": {
        "policy": "risk_unc_topk8",
        "controls": {
            "selection_min_margin": 0.15,
            "selection_strong_margin": 0.20,
            "selection_main_threshold": "q95",
            "selection_streak_threshold": "q95",
            "selection_min_high_risk_streak": 3,
            "selection_require_candidate_below_q95": True,
            "selection_max_first_action_l2": 0.35,
            "selection_max_modifications_per_episode": 1,
            "selection_cooldown_steps": 0,
            "selection_min_timestep": 0,
        },
    },
    "03_topk8_balanced": {
        "policy": "risk_unc_topk8",
        "controls": {
            "selection_min_margin": 0.20,
            "selection_strong_margin": 0.25,
            "selection_main_threshold": "q95",
            "selection_streak_threshold": "q95",
            "selection_min_high_risk_streak": 2,
            "selection_require_candidate_below_q95": True,
            "selection_max_first_action_l2": 0.50,
            "selection_max_modifications_per_episode": 2,
            "selection_cooldown_steps": 75,
            "selection_min_timestep": 0,
        },
    },
}


CONTROL_KEYS = {
    key
    for variant in VARIANTS.values()
    for key in variant["controls"]
}


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def load_or_create_seeds() -> dict:
    if SEED_MANIFEST.exists():
        return json.loads(SEED_MANIFEST.read_text())
    reset_seeds: list[int] = []
    seen: set[int] = set()
    while len(reset_seeds) < NUM_SEEDS:
        value = secrets.randbelow(2**31 - 1)
        if value not in seen:
            seen.add(value)
            reset_seeds.append(value)
    payload = {
        "run_id": RUN_ID,
        "num_seeds": NUM_SEEDS,
        "pilot_episodes": PILOT_EPISODES,
        "reset_seeds": reset_seeds,
        "reset_seeds_sha256": hashlib.sha256(json.dumps(reset_seeds).encode()).hexdigest(),
        "global_action_seed": secrets.randbelow(2**31 - 1),
        "model_load_seed": secrets.randbelow(2**31 - 1),
        "seed_generation": "Python secrets.randbelow on 2026-06-05",
    }
    write_json(SEED_MANIFEST, payload)
    return payload


def make_launcher(host: str, paths: dict, config_paths: list[tuple[str, str, Path]]) -> Path:
    launcher = ROOT / "scripts" / f"launch_{RUN_ID}_{host}.sh"
    run_dir = f"{paths['run_root']}/{RUN_ID}_{host}_task{paths['task_id']}"
    lines = [
        "#!/usr/bin/env bash",
        "set -euo pipefail",
        f"source {json.dumps(paths['activate'])}" if paths["activate"] else ":",
        "export TOKENIZERS_PARALLELISM=false",
        "export USE_TF=0 TRANSFORMERS_NO_TF=1 USE_FLAX=0",
        "export MUJOCO_GL=egl PYOPENGL_PLATFORM=egl PYTHONUNBUFFERED=1",
        "export NVIDIA_TF32_OVERRIDE=0 CUBLAS_WORKSPACE_CONFIG=:4096:8",
        f"RUN_DIR={json.dumps(run_dir)}",
        'mkdir -p "$RUN_DIR/logs"',
        'STATUS="$RUN_DIR/sequential_status.jsonl"',
        ': > "$STATUS"',
        "if pgrep -af 'run_dean_uncertainty_realtime_policy_v1.py' | grep -v grep | grep -v \"$$\" >/dev/null; then",
        "  echo 'conflicting realtime runner already active' >&2",
        "  pgrep -af 'run_dean_uncertainty_realtime_policy_v1.py' >&2",
        "  exit 2",
        "fi",
    ]
    for stage, policy, config_path in config_paths:
        remote_config = f"{paths['run_root'].rsplit('/runs', 1)[0]}/configs/{config_path.name}"
        lines.extend(
            [
                f'printf \'{{"time":"%s","stage":"{stage}","event":"start"}}\\n\' "$(date -Is)" >> "$STATUS"',
                "set +e",
                f"{json.dumps(paths['python'])} {json.dumps(paths['runner'])} --config {json.dumps(remote_config)} --policy {policy} --num-episodes {PILOT_EPISODES} > \"$RUN_DIR/logs/{stage}.log\" 2>&1",
                "code=$?",
                "set -e",
                f'printf \'{{"time":"%s","stage":"{stage}","event":"end","code":%s}}\\n\' "$(date -Is)" "$code" >> "$STATUS"',
                'if [[ "$code" -ne 0 ]]; then exit "$code"; fi',
            ]
        )
    lines.append('printf \'{"time":"%s","event":"all_done"}\\n\' "$(date -Is)" >> "$STATUS"')
    launcher.write_text("\n".join(lines) + "\n")
    launcher.chmod(0o755)
    return launcher


def main() -> None:
    seeds = load_or_create_seeds()
    generated: list[Path] = [SEED_MANIFEST]
    for host, paths in HOSTS.items():
        template = json.loads(paths["template"].read_text())
        config_paths: list[tuple[str, str, Path]] = []
        for stage, variant in VARIANTS.items():
            cfg = dict(template)
            for key in CONTROL_KEYS:
                cfg.pop(key, None)
            cfg.update(variant["controls"])
            cfg.update(
                {
                    "experiment_id": RUN_ID,
                    "stage_name": stage,
                    "variant_name": stage,
                    "suite": "libero_object_object",
                    "task_id": int(paths["task_id"]),
                    "host_role": host,
                    "reset_seeds": seeds["reset_seeds"],
                    "reset_seeds_sha256": seeds["reset_seeds_sha256"],
                    "global_action_seed": seeds["global_action_seed"],
                    "model_load_seed": seeds["model_load_seed"],
                    "seed_generation": seeds["seed_generation"],
                    "output_dir": f"{paths['run_root']}/{RUN_ID}_{host}_task{paths['task_id']}/{stage}",
                }
            )
            path = CONFIG_DIR / f"{RUN_ID}_{host}_task{paths['task_id']}_{stage}.json"
            write_json(path, cfg)
            generated.append(path)
            config_paths.append((stage, variant["policy"], path))
        generated.append(make_launcher(host, paths, config_paths))
    for path in generated:
        print(path)


if __name__ == "__main__":
    main()
