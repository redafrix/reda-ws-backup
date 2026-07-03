#!/usr/bin/env python3
"""Audit the balanced-600 protocol, campaign configuration, and rollout outputs."""

from __future__ import annotations

import argparse
import contextlib
import csv
import hashlib
import json
import math
import os
import pathlib
import sys
from collections import Counter, defaultdict
from typing import Any


ROOT = pathlib.Path(__file__).resolve().parents[1]
EXPECTED_SUITES = ("libero_goal_lan", "libero_goal_object")
EXPECTED_TASK_IDS = tuple(range(10))
EXPECTED_EPISODES_PER_TASK = 30
EXPECTED_EPISODES = 600
FIRST_QUERY_UNAVAILABLE_FIELDS = {
    "receding_overlap_mse_first",
    "receding_overlap_l2_mean_first",
    "receding_overlap_l2_max_first",
    "receding_overlap_cosine_first",
    "receding_overlap_mse_candidates_mean",
    "receding_overlap_mse_candidates_std",
    "receding_overlap_mse_candidates_min",
    "receding_overlap_mse_candidates_max",
}


def main() -> None:
    args = _parse_args()
    if args.command == "protocol":
        audit_protocol(args.csv, args.json)
    elif args.command == "campaign":
        audit_campaign(args.config)
    elif args.command == "result":
        audit_result(args.config, args.policy)
    else:
        raise RuntimeError(f"Unsupported command: {args.command}")


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    protocol = subparsers.add_parser("protocol")
    protocol.add_argument("--csv", type=pathlib.Path, required=True)
    protocol.add_argument("--json", type=pathlib.Path, required=True)
    campaign = subparsers.add_parser("campaign")
    campaign.add_argument("--config", type=pathlib.Path, required=True)
    result = subparsers.add_parser("result")
    result.add_argument("--config", type=pathlib.Path, required=True)
    result.add_argument("--policy", required=True)
    return parser.parse_args()


def audit_protocol(csv_path: pathlib.Path, json_path: pathlib.Path) -> None:
    rows = _read_csv(csv_path)
    metadata = _read_json(json_path)
    if _sha256(csv_path) != metadata["csv_sha256"]:
        raise RuntimeError("Protocol CSV hash does not match protocol JSON.")
    if len(rows) != EXPECTED_EPISODES or int(metadata["episode_count"]) != EXPECTED_EPISODES:
        raise RuntimeError(f"Protocol must contain exactly {EXPECTED_EPISODES} episodes.")
    orders = [int(row["selected_manifest_order"]) for row in rows]
    if orders != list(range(EXPECTED_EPISODES)):
        raise RuntimeError("Manifest order is not contiguous from 0 through 599.")
    identities = [_episode_identity(row) for row in rows]
    if len(set(identities)) != EXPECTED_EPISODES:
        raise RuntimeError("Protocol contains duplicate episode identities.")
    counts = Counter((row["task_suite_name"], int(row["task_id"])) for row in rows)
    expected_keys = {(suite, task_id) for suite in EXPECTED_SUITES for task_id in EXPECTED_TASK_IDS}
    if set(counts) != expected_keys or any(value != EXPECTED_EPISODES_PER_TASK for value in counts.values()):
        raise RuntimeError(f"Protocol is not 30 episodes per suite/task: {dict(counts)}")
    _validate_protocol_rows(rows)
    _validate_protocol_assets(metadata)
    _validate_selected_state_ranking(rows, int(metadata["selection_seed"]))
    _validate_registered_task_mapping(rows, metadata)
    print("PROTOCOL_AUDIT_PASS episodes=600 suites=2 tasks_per_suite=10 episodes_per_task=30")


def audit_campaign(config_path: pathlib.Path) -> None:
    campaign = _read_json(config_path)
    protocol_path = _resolve(campaign["protocol_csv"])
    audit_protocol(protocol_path, _resolve(campaign["protocol_json"]))
    if _sha256(protocol_path) != campaign["protocol_sha256"]:
        raise RuntimeError("Campaign protocol hash mismatch.")
    if int(campaign["expected_episode_count"]) != EXPECTED_EPISODES:
        raise RuntimeError("Campaign expected_episode_count must be 600.")
    order = list(campaign["policy_order"])
    policies = campaign["policies"]
    if len(order) != 8 or len(set(order)) != 8 or set(order) != set(policies):
        raise RuntimeError("Campaign must define eight unique policies in one explicit order.")
    _validate_policy_contracts(policies)
    _validate_artifacts(campaign["artifacts"])
    _validate_calibrated_thresholds(campaign)
    for policy_id in order:
        policy = policies[policy_id]
        if policy["runner"] == "arbiter":
            arbiter_path = _resolve(policy["config"])
            if _sha256(arbiter_path) != policy["config_sha256"]:
                raise RuntimeError(f"Arbiter config hash mismatch for {policy_id}.")
            _validate_arbiter_config(policy_id, _read_json(arbiter_path), protocol_path)
    print("CAMPAIGN_AUDIT_PASS policies=8 protocol_sha256=" + campaign["protocol_sha256"])


def audit_result(config_path: pathlib.Path, policy_id: str) -> None:
    campaign = _read_json(config_path)
    if policy_id not in campaign["policies"]:
        raise RuntimeError(f"Unknown campaign policy: {policy_id}")
    policy = campaign["policies"][policy_id]
    expected_rows = _read_csv(_resolve(campaign["protocol_csv"]))
    output_root = _resolve(policy["output_root"])
    if policy["runner"] == "world_model":
        _audit_world_model_result(policy_id, policy, output_root, expected_rows)
    elif policy["runner"] == "arbiter":
        _audit_arbiter_result(policy_id, output_root, expected_rows)
    else:
        raise RuntimeError(f"Unsupported runner for {policy_id}: {policy['runner']}")
    print(f"RESULT_AUDIT_PASS policy={policy_id} episodes={EXPECTED_EPISODES}")


def _validate_protocol_rows(rows: list[dict[str, str]]) -> None:
    states_by_task: dict[tuple[str, int], set[int]] = defaultdict(set)
    for row in rows:
        suite, task_id, state_index, eval_seed = _episode_identity(row)
        if suite not in EXPECTED_SUITES or task_id not in EXPECTED_TASK_IDS:
            raise RuntimeError(f"Unexpected suite/task identity: {(suite, task_id)}")
        if state_index < 0 or state_index >= 50:
            raise RuntimeError(f"Initial-state index outside 0..49: {state_index}")
        if int(row["trial_index"]) != state_index or eval_seed != 0 or int(row["episode_seed"]) != 0:
            raise RuntimeError(f"Seed/trial contract mismatch for {row['episode_uid']}")
        states_by_task[(suite, task_id)].add(state_index)
        bddl_path = pathlib.Path(row["bddl_path"])
        init_path = pathlib.Path(row["init_state_path"])
        if not bddl_path.is_file() or not init_path.is_file():
            raise FileNotFoundError(f"Missing protocol asset for {row['episode_uid']}")
        if _bddl_language(bddl_path) != row["task_description"]:
            raise RuntimeError(f"BDDL language mismatch for {row['episode_uid']}")
    if any(len(states) != EXPECTED_EPISODES_PER_TASK for states in states_by_task.values()):
        raise RuntimeError("At least one suite/task does not have 30 unique initial states.")


def _validate_protocol_assets(metadata: dict[str, Any]) -> None:
    assets = metadata["assets"]
    if len(assets) != len(EXPECTED_SUITES) * len(EXPECTED_TASK_IDS):
        raise RuntimeError("Protocol JSON must inventory exactly 20 task assets.")
    for asset in assets:
        bddl_path = pathlib.Path(asset["bddl_path"])
        init_path = pathlib.Path(asset["init_state_path"])
        if _sha256(bddl_path) != asset["bddl_sha256"]:
            raise RuntimeError(f"BDDL hash mismatch: {bddl_path}")
        if _sha256(init_path) != asset["init_state_sha256"]:
            raise RuntimeError(f"Init-state hash mismatch: {init_path}")
        if int(asset["num_initial_states"]) < 50:
            raise RuntimeError(f"Init-state file has fewer than 50 states: {init_path}")


def _validate_selected_state_ranking(rows: list[dict[str, str]], selection_seed: int) -> None:
    for suite in EXPECTED_SUITES:
        for task_id in EXPECTED_TASK_IDS:
            ranked = sorted(
                range(50),
                key=lambda state: hashlib.sha256(
                    f"{selection_seed}:{suite}:{task_id}:{state}".encode("ascii")
                ).digest(),
            )
            expected = sorted(ranked[:EXPECTED_EPISODES_PER_TASK])
            observed = sorted(
                int(row["initial_state_index"])
                for row in rows
                if row["task_suite_name"] == suite and int(row["task_id"]) == task_id
            )
            if observed != expected:
                raise RuntimeError(f"State-selection ranking mismatch for {suite} task {task_id}.")


def _validate_registered_task_mapping(
    rows: list[dict[str, str]], metadata: dict[str, Any]
) -> None:
    libero_root = pathlib.Path(metadata["libero_pro_root"]).resolve()
    package_root = libero_root / "libero" / "libero"
    if not (package_root / "__init__.py").is_file():
        raise FileNotFoundError(f"Invalid LIBERO-PRO package layout: {package_root}")
    os.environ["LIBERO_CONFIG_PATH"] = str(libero_root / "local_config")
    sys.path.insert(0, str(libero_root))
    with open(os.devnull, "w", encoding="utf-8") as sink, contextlib.redirect_stdout(sink):
        from libero.libero import benchmark  # pylint: disable=import-outside-toplevel

        benchmark_dict = benchmark.get_benchmark_dict()
        for suite in EXPECTED_SUITES:
            registered = benchmark_dict[suite]()
            if registered.n_tasks != len(EXPECTED_TASK_IDS):
                raise RuntimeError(f"Registered suite {suite} has {registered.n_tasks} tasks, expected 10.")
            for task_id in EXPECTED_TASK_IDS:
                task = registered.get_task(task_id)
                manifest_files = {
                    row["bddl_file"]
                    for row in rows
                    if row["task_suite_name"] == suite and int(row["task_id"]) == task_id
                }
                if manifest_files != {task.bddl_file}:
                    raise RuntimeError(
                        f"Registered BDDL mapping mismatch for {suite} task {task_id}: "
                        f"registered={task.bddl_file}, manifest={sorted(manifest_files)}"
                    )


def _validate_policy_contracts(policies: dict[str, dict[str, Any]]) -> None:
    expected_horizons = {"wm_h56": 56, "wm_h28": 28, "wm_h14": 14}
    for policy_id, horizon in expected_horizons.items():
        policy = policies[policy_id]
        expected = (True, 8, 3, "first_candidate", horizon)
        actual = (
            bool(policy["enable_v2w_uncertainty"]),
            int(policy["uq_num_action_candidates"]),
            int(policy["uq_num_world_candidates"]),
            policy["uq_control_policy"],
            int(policy["execute_horizon"]),
        )
        if actual != expected:
            raise RuntimeError(f"Invalid comparable WM baseline contract for {policy_id}: {actual}")
    for policy_id, expected_control in {
        "wm_risk_h56_h21": "calibrator_adaptive_horizon",
        "wm_risk_medoid_h56_h21": "risk_gated_action_medoid_horizon",
    }.items():
        policy = policies[policy_id]
        actual = (
            policy["uq_control_policy"],
            int(policy["execute_horizon"]),
            int(policy["uq_risk_high_execute_actions"]),
            int(policy["uq_num_action_candidates"]),
            int(policy["uq_num_world_candidates"]),
        )
        if actual != (expected_control, 56, 21, 8, 3):
            raise RuntimeError(f"Invalid risk-aware WM contract for {policy_id}: {actual}")


def _validate_artifacts(artifacts: dict[str, dict[str, str]]) -> None:
    for name, artifact in artifacts.items():
        path = _resolve(artifact["path"])
        if not path.is_file():
            raise FileNotFoundError(path)
        if _sha256(path) != artifact["sha256"]:
            raise RuntimeError(f"Artifact hash mismatch for {name}: {path}")


def _validate_calibrated_thresholds(campaign: dict[str, Any]) -> None:
    model_metadata = _read_json(_resolve(campaign["artifacts"]["wm_risk_metadata"]["path"]))
    model_contract = (
        model_metadata["feature_profile"],
        model_metadata["label_column"],
        int(model_metadata["history"]),
        model_metadata["action_candidate_policy"],
    )
    if model_contract != ("action_plus_v2w_ace", "failure_label", 8, "ignore"):
        raise RuntimeError(f"Unexpected WM risk-model contract: {model_contract}")
    threshold_path = _resolve(campaign["artifacts"]["wm_conformal_thresholds"]["path"])
    rows = _read_csv(threshold_path)
    matches = [
        row
        for row in rows
        if row["model"] == "ng_gru_h8_action_v2wace_s1"
        and float(row["alpha"]) == 0.2
        and row["horizon"] == "first5"
    ]
    if len(matches) != 1:
        raise RuntimeError("Could not uniquely resolve the WM alpha=0.2 first5 conformal threshold.")
    expected = float(matches[0]["threshold"])
    for policy_id in ("wm_risk_h56_h21", "wm_risk_medoid_h56_h21"):
        actual = float(campaign["policies"][policy_id]["uq_risk_threshold"])
        if actual != expected:
            raise RuntimeError(f"WM threshold provenance mismatch for {policy_id}: {actual} != {expected}")
    simvla_thresholds = _read_json(_resolve(campaign["artifacts"]["simvla_risk_thresholds"]["path"]))
    if not math.isclose(float(simvla_thresholds["q95"]), 0.6155413389205933, rel_tol=0.0, abs_tol=1e-12):
        raise RuntimeError("Unexpected SimVLA q95 threshold artifact.")


def _validate_arbiter_config(policy_id: str, config: dict[str, Any], protocol_path: pathlib.Path) -> None:
    if int(config["expected_episode_count"]) != EXPECTED_EPISODES or not config["require_empty_output_dir"]:
        raise RuntimeError(f"Invalid output/cardinality contract for {policy_id}.")
    if _resolve(config["simvla"]["episode_manifest_csv"]) != protocol_path.resolve():
        raise RuntimeError(f"Arbiter {policy_id} does not use the frozen campaign manifest.")
    if int(config["simvla"]["max_steps"]) != 250 or int(config["simvla"]["execution_horizon"]) != 10:
        raise RuntimeError(f"Invalid SimVLA horizon/timeout for {policy_id}.")
    if policy_id == "dual_simvla_wm_risk_h56_h21":
        arbiter = config["arbiter"]
        world_model = config["world_model"]
        expected = (
            arbiter["policy"],
            arbiter["simvla_trigger_threshold"],
            int(arbiter["simvla_high_risk_streak"]),
            int(arbiter["world_model_low_risk_execute_actions"]),
            int(arbiter["both_high_execute_actions"]),
            world_model["uq_control_policy"],
            int(world_model["num_execute_actions"]),
            int(world_model["uq_risk_high_execute_actions"]),
        )
        if expected != (
            "dual_main_risk_simvla_medoid",
            "q95",
            3,
            56,
            21,
            "calibrator_adaptive_horizon",
            56,
            21,
        ):
            raise RuntimeError(f"Invalid dual-arbiter contract: {expected}")


def _audit_world_model_result(
    policy_id: str,
    policy: dict[str, Any],
    output_root: pathlib.Path,
    expected_rows: list[dict[str, str]],
) -> None:
    observed_uids: list[str] = []
    episode_rows: list[dict[str, Any]] = []
    for suite in EXPECTED_SUITES:
        suite_dir = output_root / suite
        outcomes = _read_jsonl(suite_dir / "episode_outcomes.jsonl")
        expected_suite = [row for row in expected_rows if row["task_suite_name"] == suite]
        if len(outcomes) != len(expected_suite):
            raise RuntimeError(f"{policy_id}/{suite} expected 300 outcomes, got {len(outcomes)}.")
        for outcome in outcomes:
            observed_uids.append(
                f"{suite}_task{int(outcome['task_id']):02d}_init{int(outcome['episode_index']):03d}_seed0"
            )
            _require_positive(outcome, "wall_time_seconds")
            if int(outcome["policy_queries"]) < 1:
                raise RuntimeError(f"Invalid policy query count in {policy_id}/{suite}.")
        runtimes = _read_jsonl(suite_dir / "policy_query_runtime.jsonl")
        if len(runtimes) != sum(int(row["policy_queries"]) for row in outcomes):
            raise RuntimeError(f"Policy-query timing count mismatch in {policy_id}/{suite}.")
        for runtime in runtimes:
            _require_positive(runtime, "query_wall_seconds")
        summary = _read_json(suite_dir / "runtime_summary.json")
        if int(summary["completed_episodes"]) != 300:
            raise RuntimeError(f"Runtime summary episode count mismatch in {policy_id}/{suite}.")
        _require_positive(summary, "rollout_wall_seconds")
        episode_rows.extend(outcomes)
        if bool(policy["enable_v2w_uncertainty"]):
            _audit_world_model_uq_rows(policy_id, suite_dir, policy, runtimes)
    expected_uids = [row["episode_uid"] for row in expected_rows]
    if observed_uids != expected_uids:
        raise RuntimeError(f"Episode identity/order mismatch for {policy_id}.")
    if len(episode_rows) != EXPECTED_EPISODES:
        raise RuntimeError(f"Expected 600 aggregate outcomes for {policy_id}.")


def _audit_world_model_uq_rows(
    policy_id: str,
    suite_dir: pathlib.Path,
    policy: dict[str, Any],
    runtime_rows: list[dict[str, Any]],
) -> None:
    rows = _read_jsonl(suite_dir / "action_candidate_uncertainty.jsonl")
    if len(rows) != len(runtime_rows):
        raise RuntimeError(f"UQ/query row count mismatch for {policy_id}/{suite_dir.name}.")
    v2w_rows = _read_jsonl(suite_dir / "v2w_uncertainty_scores.jsonl")
    expected_v2w_rows = len(runtime_rows) * int(policy["uq_num_world_candidates"])
    if len(v2w_rows) != expected_v2w_rows:
        raise RuntimeError(
            f"V2W/query row count mismatch for {policy_id}/{suite_dir.name}: "
            f"expected {expected_v2w_rows}, got {len(v2w_rows)}."
        )
    allowed_horizons = _allowed_world_model_horizons(policy)
    expected_action_candidates = int(policy["uq_num_action_candidates"])
    expected_world_candidates = int(policy["uq_num_world_candidates"])
    for row, runtime in zip(rows, runtime_rows, strict=True):
        if (
            int(row["num_candidates"]) != expected_action_candidates
            or int(row["world_context_num_candidates"]) != expected_world_candidates
        ):
            raise RuntimeError(f"Candidate cardinality mismatch for {policy_id}.")
        if bool(row["oom_fallback"]):
            raise RuntimeError(f"OOM fallback occurred in {policy_id}.")
        if int(row["selected_execute_horizon"]) not in allowed_horizons:
            raise RuntimeError(f"Unexpected execution horizon in {policy_id}: {row['selected_execute_horizon']}")
        if int(runtime["selected_execute_horizon"]) != int(row["selected_execute_horizon"]):
            raise RuntimeError(f"Timing/UQ horizon mismatch in {policy_id}.")
        _require_saved_array(row, "action_candidate_array_path")
        _require_probability(row, "risk_probability")
        unavailable = set(row["risk_unavailable_scalar_fields"])
        expected_unavailable = (
            FIRST_QUERY_UNAVAILABLE_FIELDS if int(row["episode_query_index"]) == 1 else set()
        )
        if unavailable != expected_unavailable:
            raise RuntimeError(
                f"Unexpected unavailable risk features in {policy_id}: "
                f"query={row['episode_query_index']} unavailable={sorted(unavailable)}"
            )
        if policy["uq_control_policy"] == "risk_gated_action_medoid_horizon":
            reason = row["risk_horizon_reason"]
            selection = row["candidate_selection_reason"]
            expected_selection = "high_risk_action_medoid" if reason == "persistent_high_risk" else "low_risk_first_candidate"
            if selection != expected_selection:
                raise RuntimeError(f"Risk/medoid decision mismatch in {policy_id}.")
    for row in v2w_rows:
        _require_saved_array(row, "v2w_variance_array_path")


def _allowed_world_model_horizons(policy: dict[str, Any]) -> set[int]:
    if policy["uq_control_policy"] == "first_candidate":
        return {int(policy["execute_horizon"])}
    return {
        int(policy["execute_horizon"]),
        int(policy["uq_risk_medium_execute_actions"]),
        int(policy["uq_risk_high_execute_actions"]),
    }


def _audit_arbiter_result(
    policy_id: str,
    output_root: pathlib.Path,
    expected_rows: list[dict[str, str]],
) -> None:
    outcomes = _read_jsonl(output_root / "episode_summaries.jsonl")
    if len(outcomes) != EXPECTED_EPISODES:
        raise RuntimeError(f"{policy_id} expected 600 outcomes, got {len(outcomes)}.")
    if [row["episode_uid"] for row in outcomes] != [row["episode_uid"] for row in expected_rows]:
        raise RuntimeError(f"Episode identity/order mismatch for {policy_id}.")
    for outcome in outcomes:
        if outcome["task_suite_name"] not in EXPECTED_SUITES:
            raise RuntimeError(f"Unexpected suite in {policy_id}: {outcome['task_suite_name']}")
        _require_positive(outcome, "wall_time_seconds")
        if int(outcome["num_queries"]) < 1:
            raise RuntimeError(f"Invalid query count in {policy_id}.")
    steps = _read_jsonl(output_root / "arbiter_step_scores.jsonl")
    if len(steps) != sum(int(row["num_queries"]) for row in outcomes):
        raise RuntimeError(f"Step/query count mismatch for {policy_id}.")
    for row in steps:
        _require_positive(row, "query_wall_time_seconds")
        if policy_id in {"hf_simvla", "modified_simvla_60k"}:
            if row["branch"] != "simvla" or int(row["selected_execute_horizon"]) != 10:
                raise RuntimeError(f"Baseline SimVLA branch changed in {policy_id}.")
        else:
            if int(row["selected_execute_horizon"]) not in {10, 21, 56}:
                raise RuntimeError(f"Unexpected dual horizon in {policy_id}.")
            if row["simvla_trigger_threshold_name"] != "q95":
                raise RuntimeError("Dual arbiter did not use the calibrated q95 SimVLA threshold.")
    runtime = _read_json(output_root / "runtime_summary.json")
    if int(runtime["completed_episodes"]) != EXPECTED_EPISODES:
        raise RuntimeError(f"Runtime summary count mismatch for {policy_id}.")
    _require_positive(runtime, "rollout_wall_seconds")
    if policy_id == "dual_simvla_wm_risk_h56_h21":
        fallback_count = sum(int(row["fallback_calls"]) for row in outcomes)
        fallback_dir = output_root / "world_model_fallback"
        fallback_runtimes = _read_jsonl(fallback_dir / "policy_query_runtime.jsonl")
        if len(fallback_runtimes) != fallback_count:
            raise RuntimeError(
                f"Dual WM fallback/query count mismatch: {len(fallback_runtimes)} != {fallback_count}."
            )
        _audit_world_model_uq_rows(
            policy_id,
            fallback_dir,
            {"uq_control_policy": "calibrator_adaptive_horizon"},
            fallback_runtimes,
        )


def _episode_identity(row: dict[str, str]) -> tuple[str, int, int, int]:
    return (
        row["task_suite_name"],
        int(row["task_id"]),
        int(row["initial_state_index"]),
        int(row["eval_seed"]),
    )


def _require_positive(row: dict[str, Any], key: str) -> None:
    value = float(row[key])
    if not math.isfinite(value) or value <= 0.0:
        raise RuntimeError(f"{key} must be finite and positive, got {value}.")


def _require_probability(row: dict[str, Any], key: str) -> None:
    value = float(row[key])
    if not math.isfinite(value) or value < 0.0 or value > 1.0:
        raise RuntimeError(f"{key} must be a finite probability, got {value}.")


def _require_saved_array(row: dict[str, Any], key: str) -> None:
    path = pathlib.Path(str(row[key]))
    if not path.is_file():
        raise FileNotFoundError(f"Missing saved query array referenced by {key}: {path}")


def _read_csv(path: pathlib.Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _read_json(path: pathlib.Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _read_jsonl(path: pathlib.Path) -> list[dict[str, Any]]:
    if not path.is_file():
        raise FileNotFoundError(path)
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def _resolve(path: str | pathlib.Path) -> pathlib.Path:
    candidate = pathlib.Path(path)
    return candidate.resolve() if candidate.is_absolute() else (ROOT / candidate).resolve()


def _sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _bddl_language(path: pathlib.Path) -> str:
    text = path.read_text(encoding="utf-8")
    marker = "(:language"
    start = text.find(marker)
    end = text.find(")", start)
    if start < 0 or end < 0:
        raise RuntimeError(f"Missing BDDL language: {path}")
    return " ".join(text[start + len(marker) : end].strip().lower().split())


if __name__ == "__main__":
    main()
