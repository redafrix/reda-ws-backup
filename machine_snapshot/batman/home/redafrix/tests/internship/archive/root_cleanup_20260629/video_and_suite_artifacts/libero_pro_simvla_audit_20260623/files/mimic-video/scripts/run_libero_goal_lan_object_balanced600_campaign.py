#!/usr/bin/env python3
"""Validate or execute the frozen balanced-600 eight-policy campaign."""

from __future__ import annotations

import argparse
import json
import os
import pathlib
import subprocess
import time
from typing import Any


ROOT = pathlib.Path(__file__).resolve().parents[1]
WORLD_ROOT = ROOT.parent
DEFAULT_CONFIG = ROOT / "configs/uq_benchmarks/libero_goal_lan_object_balanced600_campaign_20260622.json"
WM_RUNNER = ROOT / "scripts/run_libero_goal_ood_full_uncertainty_collection.sh"
ARBITER_RUNNER = ROOT / "scripts/run_simvla_world_model_arbiter.py"
AUDITOR = ROOT / "scripts/audit_libero_goal_lan_object_balanced600.py"
PYTHON = ROOT / "model/.venv/bin/python"


def main() -> None:
    args = _parse_args()
    campaign_path = args.config.resolve()
    campaign = _read_json(campaign_path)
    _audit_campaign(campaign_path)
    commands = _build_commands(campaign)
    _preflight(campaign, commands)
    if args.validate_only:
        print("BALANCED600_VALIDATE_ONLY_PASS no rollouts started")
        return
    _require_cuda()
    _require_empty_outputs(campaign)
    _execute_campaign(campaign_path, campaign, commands)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=pathlib.Path, default=DEFAULT_CONFIG)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--validate-only", action="store_true")
    mode.add_argument("--run", action="store_true")
    return parser.parse_args()


def _build_commands(campaign: dict[str, Any]) -> dict[str, list[list[str]]]:
    commands: dict[str, list[list[str]]] = {}
    for policy_id in campaign["policy_order"]:
        policy = campaign["policies"][policy_id]
        if policy["runner"] == "world_model":
            commands[policy_id] = [
                [str(WM_RUNNER), suite, policy_id]
                for suite in campaign["expected_suites"]
            ]
        elif policy["runner"] == "arbiter":
            commands[policy_id] = [[str(PYTHON), str(ARBITER_RUNNER), "--config", str(_resolve(policy["config"]))]]
        else:
            raise RuntimeError(f"Unsupported runner for {policy_id}: {policy['runner']}")
    return commands


def _preflight(campaign: dict[str, Any], commands: dict[str, list[list[str]]]) -> None:
    for policy_id, policy_commands in commands.items():
        for command in policy_commands:
            if pathlib.Path(command[0]) == WM_RUNNER:
                suite = command[1]
                env = _world_model_environment(campaign, policy_id, suite, validate_only=True)
                subprocess.run([str(WM_RUNNER)], cwd=ROOT, env=env, check=True)
            else:
                subprocess.run([*command, "--validate-only"], cwd=ROOT, env=_arbiter_environment(), check=True)
        print(f"[preflight] policy={policy_id} passed", flush=True)


def _execute_campaign(
    campaign_path: pathlib.Path,
    campaign: dict[str, Any],
    commands: dict[str, list[list[str]]],
) -> None:
    campaign_root = _resolve(next(iter(campaign["policies"].values()))["output_root"]).parent
    campaign_root.mkdir(parents=True, exist_ok=True)
    started_at = time.perf_counter()
    completed: list[str] = []
    for policy_id in campaign["policy_order"]:
        policy_started_at = time.perf_counter()
        _write_status(campaign_root, campaign_path, completed, policy_id)
        for command in commands[policy_id]:
            if pathlib.Path(command[0]) == WM_RUNNER:
                suite = command[1]
                subprocess.run(
                    [str(WM_RUNNER)],
                    cwd=ROOT,
                    env=_world_model_environment(campaign, policy_id, suite, validate_only=False),
                    check=True,
                )
            else:
                subprocess.run(command, cwd=ROOT, env=_arbiter_environment(), check=True)
        _audit_result(campaign_path, policy_id)
        completed.append(policy_id)
        print(
            f"[campaign] policy={policy_id} completed wall_hours={(time.perf_counter() - policy_started_at) / 3600.0:.3f}",
            flush=True,
        )
    _write_status(campaign_root, campaign_path, completed, None)
    print(
        f"BALANCED600_CAMPAIGN_PASS policies={len(completed)} wall_hours={(time.perf_counter() - started_at) / 3600.0:.3f}",
        flush=True,
    )


def _world_model_environment(
    campaign: dict[str, Any],
    policy_id: str,
    suite: str,
    validate_only: bool,
) -> dict[str, str]:
    policy = campaign["policies"][policy_id]
    output_dir = _resolve(policy["output_root"]) / suite
    env = os.environ.copy()
    env.update(
        {
            "PYTHON": str(PYTHON),
            "OOD_IMPL": "pro",
            "LIBERO_PRO_ROOT": str(WORLD_ROOT / "LIBERO-PRO"),
            "EPISODE_MANIFEST_PATH": str(_resolve(campaign["protocol_csv"])),
            "TASK_SUITE_NAME": suite,
            "TASK_IDS": "0-9",
            "NUM_TRIALS_PER_TASK": "50",
            "TRIAL_START_INDEX": "0",
            "NUM_STEPS_WAIT": "10",
            "MAX_EPISODE_STEPS": str(campaign["max_episode_steps"]),
            "SEED": "0",
            "PROMPT_SOURCE": str(campaign["prompt_source"]),
            "PRECOMPUTE_EMBEDDINGS": "0",
            "SAVE_VIDEOS": "0",
            "VALIDATE_ONLY": "1" if validate_only else "0",
            "RESULT_DIR_OVERRIDE": str(output_dir),
            "RUN_SUFFIX": f"b600_{policy_id}",
            "VAM_NUM_SAMPLING_STEPS": "2",
            "STOP_VIDEO_DENOISING_STEP": "0",
            "NUM_EXECUTE_ACTIONS": str(policy["execute_horizon"]),
            "ENABLE_V2W_UNCERTAINTY": "1" if policy["enable_v2w_uncertainty"] else "0",
            "UQ_NUM_ACTION_CANDIDATES": str(policy["uq_num_action_candidates"]),
            "UQ_ACTION_CANDIDATE_BATCH_SIZE": str(policy.get("uq_action_candidate_batch_size", 1)),
            "UQ_NUM_WORLD_CANDIDATES": str(policy["uq_num_world_candidates"]),
            "UQ_CONTROL_POLICY": str(policy["uq_control_policy"]),
            "UQ_SAVE_CANDIDATE_ARRAYS": "1" if policy["save_candidate_arrays"] else "0",
            "SAVE_V2W_VARIANCE_ARRAYS": "1" if policy["save_v2w_variance_arrays"] else "0",
        }
    )
    if policy["enable_v2w_uncertainty"]:
        env.update(
            {
                "UQ_RISK_MODEL_DIR": str(_resolve(policy["uq_risk_model_dir"])),
                "UQ_RISK_THRESHOLD": str(policy["uq_risk_threshold"]),
                "UQ_RISK_MEDIUM_THRESHOLD": str(policy["uq_risk_medium_threshold"]),
                "UQ_RISK_PERSISTENCE": str(policy["uq_risk_persistence"]),
                "UQ_RISK_MEDIUM_EXECUTE_ACTIONS": str(policy["uq_risk_medium_execute_actions"]),
                "UQ_RISK_HIGH_EXECUTE_ACTIONS": str(policy["uq_risk_high_execute_actions"]),
            }
        )
    return env


def _arbiter_environment() -> dict[str, str]:
    env = os.environ.copy()
    env.update(
        {
            "WORLD_ROOT": str(WORLD_ROOT),
            "SIMVLA_ROOT": str(WORLD_ROOT / "SimVLA_modified"),
            "LIBERO_PRO_ROOT": str(WORLD_ROOT / "LIBERO-PRO"),
            "SIMVLA_NORM_STATS": str(WORLD_ROOT / "SimVLA_modified/norm_stats/libero_norm.json"),
            "SMOLVLM_PATH": str(
                pathlib.Path.home()
                / ".cache/huggingface/hub/models--HuggingFaceTB--SmolVLM-500M-Instruct/"
                "snapshots/a7da5b986cb59b408707209984f360a5f4ad7e47"
            ),
            "HF_HUB_OFFLINE": "1",
            "TRANSFORMERS_OFFLINE": "1",
            "MPLCONFIGDIR": f"/tmp/matplotlib-{os.environ.get('USER', 'user')}",
        }
    )
    return env


def _require_empty_outputs(campaign: dict[str, Any]) -> None:
    for policy_id in campaign["policy_order"]:
        output = _resolve(campaign["policies"][policy_id]["output_root"])
        if output.exists() and any(output.iterdir()):
            raise RuntimeError(f"Refusing to reuse non-empty output for {policy_id}: {output}")


def _require_cuda() -> None:
    result = subprocess.run(
        ["nvidia-smi", "--query-gpu=index,name,memory.used,memory.total", "--format=csv,noheader"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"CUDA preflight failed: {result.stderr.strip()}")
    print("[gpu] " + result.stdout.strip(), flush=True)


def _audit_campaign(config_path: pathlib.Path) -> None:
    subprocess.run(
        [str(PYTHON), str(AUDITOR), "campaign", "--config", str(config_path)],
        cwd=ROOT,
        check=True,
    )


def _audit_result(config_path: pathlib.Path, policy_id: str) -> None:
    subprocess.run(
        [str(PYTHON), str(AUDITOR), "result", "--config", str(config_path), "--policy", policy_id],
        cwd=ROOT,
        check=True,
    )


def _write_status(
    campaign_root: pathlib.Path,
    campaign_path: pathlib.Path,
    completed: list[str],
    active_policy: str | None,
) -> None:
    status_path = campaign_root / "campaign_status.json"
    temporary_path = status_path.with_suffix(".json.tmp")
    payload = {
        "campaign_config": str(campaign_path),
        "updated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "completed_policies": completed,
        "active_policy": active_policy,
    }
    temporary_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    temporary_path.replace(status_path)


def _resolve(path: str | pathlib.Path) -> pathlib.Path:
    candidate = pathlib.Path(path)
    return candidate.resolve() if candidate.is_absolute() else (ROOT / candidate).resolve()


def _read_json(path: pathlib.Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
