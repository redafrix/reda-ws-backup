#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import random
import shlex
from pathlib import Path
from typing import Any


CAMPAIGN_ID = "bob_risk_matrix_campaign_20260605"
BOB_FIPER = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws")
BOB_REDA = Path("/media/rootalkhatib/My Passport/reda_ws")
BOB_CAMPAIGN = BOB_FIPER / "trash" / CAMPAIGN_ID
MODIFIED_HASH = "3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71"
ORIGINAL_HASH = "9d3b1767773da86906d771b1eca2c2911087371bf8b3890a7336b6773270f6be"
TOPK8_DIMS = [6, 21, 25, 27, 23, 2, 26, 24]


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def q(value: str | Path) -> str:
    return shlex.quote(str(value))


def activated(command: str) -> list[str]:
    activate = BOB_REDA / "asynchvla_ws/scripts/activate_simvla_bob.sh"
    exports = (
        "export MUJOCO_GL=egl PYOPENGL_PLATFORM=egl USE_TF=0 TRANSFORMERS_NO_TF=1 "
        "USE_FLAX=0 TOKENIZERS_PARALLELISM=false HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 "
        "CUBLAS_WORKSPACE_CONFIG=:4096:8; "
    )
    return ["bash", "-lc", f"source {q(activate)} >/dev/null; {exports}{command}"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--local-root", required=True)
    args = parser.parse_args()
    local_root = Path(args.local_root).resolve()
    configs_dir = local_root / "configs" / "generated"
    jobs: list[dict[str, Any]] = []

    def add_job(
        job_id: str,
        command: list[str],
        depends: list[str] | None = None,
        checks: list[dict[str, Any]] | None = None,
        timeout: int = 172800,
        attempts: int = 2,
        allow_failed_dependencies: bool = False,
    ) -> None:
        jobs.append(
            {
                "id": job_id,
                "command": command,
                "depends_on": depends or [],
                "checks": checks or [],
                "timeout_seconds": timeout,
                "max_attempts": attempts,
                "allow_failed_dependencies": allow_failed_dependencies,
                "cwd": str(BOB_CAMPAIGN),
                "log": str(BOB_CAMPAIGN / "logs" / f"{job_id}.log"),
            }
        )

    prepare_cmd = (
        f"mkdir -p {q(BOB_CAMPAIGN / 'inputs')} {q(BOB_CAMPAIGN / 'runs')} {q(BOB_CAMPAIGN / 'models')} "
        f"{q(BOB_CAMPAIGN / 'smokes')} {q(BOB_CAMPAIGN / 'state')} {q(BOB_CAMPAIGN / 'logs')}; "
        f"rm -rf {q(BOB_CAMPAIGN / 'inputs' / 'episode_bundle')} {q(BOB_CAMPAIGN / 'inputs' / 'canonical_detectors')}; "
        f"cp -a {q(BOB_FIPER / 'trash/goal_object_modified_simvla_chunk10_100_20260605/bundle')} "
        f"{q(BOB_CAMPAIGN / 'inputs' / 'episode_bundle')}; "
        f"cp -a {q(BOB_FIPER / 'realtime_deployment/dean_artifacts/current_dean_risk_models_20260602/all_tasks_full')} "
        f"{q(BOB_CAMPAIGN / 'inputs' / 'canonical_detectors')}"
    )
    add_job(
        "000_prepare_inputs",
        ["bash", "-lc", prepare_cmd],
        checks=[{"type": "file", "path": str(BOB_CAMPAIGN / "inputs/episode_bundle/verification/episode_identity_table.csv")}],
    )

    sync_script = BOB_CAMPAIGN / "src/sync_dean_dataset.py"
    chunk10_dest = BOB_CAMPAIGN / "inputs/datasets/goal_object_exact200_chunk10"
    add_job(
        "001_sync_exact200_chunk10",
        [
            "/usr/bin/python3",
            str(sync_script),
            "--remote-host",
            "dean@100.124.50.124",
            "--remote-root",
            "/home/dean/fiper_goal_object_collection_20260605/runs/production_20260605/exact_200/chunk10",
            "--dest",
            str(chunk10_dest),
            "--min-episodes",
            "200",
        ],
        depends=["000_prepare_inputs"],
        checks=[{"type": "file", "path": str(chunk10_dest / "SYNC_MANIFEST.json")}],
        timeout=21600,
    )

    canonical_base = BOB_CAMPAIGN / "inputs/canonical_detectors/base"
    canonical_top8 = BOB_CAMPAIGN / "inputs/canonical_detectors/unc_topk8"
    exact_manifest = BOB_CAMPAIGN / "inputs/episode_bundle/verification/episode_identity_table.csv"
    checkpoint_paths = {
        "original": BOB_FIPER / "checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO",
        "modified": BOB_FIPER / "checkpoints/simvla_libero_uncertainty/ckpt-60000",
    }
    checkpoint_hashes = {"original": ORIGINAL_HASH, "modified": MODIFIED_HASH}
    policy_detector = {
        "simvla_only": None,
        "shadow_base": "base",
        "risk_base": "base",
        "shadow_topk8": "top8",
        "risk_topk8": "top8",
    }

    def make_runtime_config(
        job_id: str,
        checkpoint_kind: str,
        policy: str,
        horizon: int,
        output_root: Path,
        detector_base: Path = canonical_base,
        detector_top8: Path = canonical_top8,
        exact: bool = True,
        suite: str = "libero_goal_object",
        task_id: int = 0,
        reset_seeds: list[int] | None = None,
        smoke: bool = False,
    ) -> Path:
        cfg = {
            "experiment_id": job_id,
            "suite": suite,
            "task_id": task_id,
            "checkpoint": str(checkpoint_paths[checkpoint_kind]),
            "expected_checkpoint_sha256": checkpoint_hashes[checkpoint_kind],
            "simvla_root": str(BOB_REDA / "intern_ship_ws/simvla/code/SimVLA_modified"),
            "libero_pro_root": str(BOB_REDA / "intern_ship_ws/assets/repos/LIBERO-PRO"),
            "norm_stats": str(BOB_REDA / "intern_ship_ws/simvla/code/SimVLA_modified/norm_stats/libero_norm.json"),
            "smolvlm_path": str(BOB_FIPER / "realtime_deployment/smolvlm_cache"),
            "risk_model_base_dir": str(detector_base),
            "risk_model_unc_topk8_dir": str(detector_top8),
            "expected_topk8_dims": TOPK8_DIMS,
            "output_dir": str(output_root),
            "execution_horizon": horizon,
            "global_action_seed": 206050917,
            "model_load_seed": 206050911,
            "ace_candidate_count": 8,
            "history_steps": 16,
            "max_steps": 12 if smoke else (250 if exact else 300),
            "warmup": 10,
            "resolution": 128,
            "image_size": 384,
            "model_denoise_steps": 10,
            "selection_min_margin": 0.10,
            "selection_strong_margin": 0.15,
            "selection_main_threshold": "q95",
            "selection_streak_threshold": "q95",
            "selection_min_high_risk_streak": 1,
            "selection_require_candidate_below_q95": False,
            "selection_max_modifications_per_episode": 0,
            "selection_cooldown_steps": 0,
            "selection_min_timestep": 0,
            "reset_seeds": reset_seeds or [],
        }
        if exact:
            cfg["episode_manifest_csv"] = str(exact_manifest)
            cfg["episode_bundle_root"] = str(BOB_CAMPAIGN / "inputs/episode_bundle")
            cfg["exact_episodes_per_task"] = 10
        path = configs_dir / f"{job_id}.json"
        write_json(path, cfg)
        return path

    runner = BOB_CAMPAIGN / "src/run_policy_matrix.py"

    def add_runtime_pair(
        prefix: str,
        checkpoint_kind: str,
        policy: str,
        horizon: int,
        depends: list[str],
        detector_base: Path = canonical_base,
        detector_top8: Path = canonical_top8,
        exact: bool = True,
        suite: str = "libero_goal_object",
        task_id: int = 0,
        reset_seeds: list[int] | None = None,
        production_episodes: int = 100,
    ) -> str:
        smoke_id = f"{prefix}_smoke"
        prod_id = f"{prefix}_prod100"
        smoke_out = BOB_CAMPAIGN / "smokes" / prefix
        prod_out = BOB_CAMPAIGN / "runs" / prefix
        smoke_cfg = make_runtime_config(
            smoke_id, checkpoint_kind, policy, horizon, smoke_out, detector_base, detector_top8, exact, suite, task_id, reset_seeds, True
        )
        prod_cfg = make_runtime_config(
            prod_id, checkpoint_kind, policy, horizon, prod_out, detector_base, detector_top8, exact, suite, task_id, reset_seeds, False
        )
        smoke_cmd = activated(f"/usr/bin/python3 {q(runner)} --config {q(BOB_CAMPAIGN / 'configs/generated' / smoke_cfg.name)} --policy {q(policy)} --smoke")
        prod_cmd = activated(
            f"/usr/bin/python3 {q(runner)} --config {q(BOB_CAMPAIGN / 'configs/generated' / prod_cfg.name)} "
            f"--policy {q(policy)} --num-episodes {production_episodes}"
        )
        add_job(
            smoke_id,
            smoke_cmd,
            depends=depends,
            checks=[{"type": "jsonl", "path": str(smoke_out / policy / "episode_summaries.jsonl"), "min_rows": 1}],
            timeout=1800,
            allow_failed_dependencies=True,
        )
        add_job(
            prod_id,
            prod_cmd,
            depends=[smoke_id],
            checks=[{"type": "jsonl", "path": str(prod_out / policy / "episode_summaries.jsonl"), "min_rows": production_episodes}],
            timeout=172800,
        )
        return prod_id

    core_specs = []
    for horizon in [10]:
        for checkpoint_kind, policies in [
            ("original", ["simvla_only", "shadow_base", "risk_base"]),
            ("modified", ["simvla_only", "shadow_base", "risk_base", "shadow_topk8", "risk_topk8"]),
        ]:
            for policy in policies:
                core_specs.append((horizon, checkpoint_kind, policy))
    previous = "001_sync_exact200_chunk10"
    core_done: list[str] = []
    for horizon, checkpoint_kind, policy in core_specs:
        prefix = f"core_exact_{checkpoint_kind}_{policy}_h{horizon}"
        previous = add_runtime_pair(prefix, checkpoint_kind, policy, horizon, [previous])
        core_done.append(previous)

    train_script = BOB_CAMPAIGN / "src/train_frozen_detectors.py"
    chunk_smoke_out = BOB_CAMPAIGN / "smokes/train_chunk10"
    chunk_train_out = BOB_CAMPAIGN / "models/chunk10_exact200"
    train_common = (
        f"/usr/bin/python3 {q(train_script)} --run-root {q(chunk10_dest)} --default-suite libero_goal_object "
        "--cadence native --splits all_tasks_random ood_last2_taskids --variants base unc_topk8 "
    )
    add_job(
        "200_train_chunk10_smoke",
        activated(train_common + f"--output-dir {q(chunk_smoke_out)} --smoke"),
        depends=[core_done[7]],
        checks=[
            {"type": "detector", "path": str(chunk_smoke_out / "all_tasks_random/base")},
            {"type": "detector", "path": str(chunk_smoke_out / "all_tasks_random/unc_topk8")},
        ],
        timeout=7200,
        allow_failed_dependencies=True,
    )
    add_job(
        "201_train_chunk10_full",
        activated(train_common + f"--output-dir {q(chunk_train_out)}"),
        depends=["200_train_chunk10_smoke"],
        checks=[
            {"type": "detector", "path": str(chunk_train_out / "all_tasks_random/base")},
            {"type": "detector", "path": str(chunk_train_out / "all_tasks_random/unc_topk8")},
        ],
        timeout=21600,
    )

    retrained_chunk_jobs = [
        ("chunktrain_original_risk_base_h10", "original", "risk_base"),
        ("chunktrain_modified_risk_base_h10", "modified", "risk_base"),
        ("chunktrain_modified_risk_topk8_h10", "modified", "risk_topk8"),
    ]
    previous = "201_train_chunk10_full"
    for prefix, checkpoint_kind, policy in retrained_chunk_jobs:
        previous = add_runtime_pair(
            prefix,
            checkpoint_kind,
            policy,
            10,
            [previous],
            detector_base=chunk_train_out / "all_tasks_random/base",
            detector_top8=chunk_train_out / "all_tasks_random/unc_topk8",
        )

    receding_dest = BOB_CAMPAIGN / "inputs/datasets/goal_object_exact200_receding"
    add_job(
        "300_sync_exact200_receding",
        [
            "/usr/bin/python3",
            str(sync_script),
            "--remote-host",
            "dean@100.124.50.124",
            "--remote-root",
            "/home/dean/fiper_goal_object_collection_20260605/runs/production_20260605/exact_200/receding",
            "--dest",
            str(receding_dest),
            "--min-episodes",
            "200",
        ],
        depends=[previous],
        checks=[{"type": "file", "path": str(receding_dest / "SYNC_MANIFEST.json")}],
        timeout=86400,
        allow_failed_dependencies=True,
    )

    receding_outputs = {}
    previous = "300_sync_exact200_receding"
    for cadence, cadence_args in [("native", "--cadence native"), ("stride10", "--cadence stride --stride 10")]:
        smoke_id = f"310_train_receding_{cadence}_smoke"
        train_id = f"311_train_receding_{cadence}_full"
        smoke_out = BOB_CAMPAIGN / f"smokes/train_receding_{cadence}"
        train_out = BOB_CAMPAIGN / f"models/receding_exact200_{cadence}"
        receding_outputs[cadence] = train_out
        common = (
            f"/usr/bin/python3 {q(train_script)} --run-root {q(receding_dest)} --default-suite libero_goal_object "
            f"{cadence_args} --splits all_tasks_random ood_last2_taskids --variants base unc_topk8 "
        )
        add_job(
            smoke_id,
            activated(common + f"--output-dir {q(smoke_out)} --smoke"),
            depends=[previous],
            checks=[{"type": "detector", "path": str(smoke_out / "all_tasks_random/base")}],
            timeout=7200,
        )
        add_job(
            train_id,
            activated(common + f"--output-dir {q(train_out)}"),
            depends=[smoke_id],
            checks=[
                {"type": "detector", "path": str(train_out / "all_tasks_random/base")},
                {"type": "detector", "path": str(train_out / "all_tasks_random/unc_topk8")},
            ],
            timeout=21600,
        )
        previous = train_id

    for cadence, horizon in [("native", 1), ("stride10", 10)]:
        model_root = receding_outputs[cadence] / "all_tasks_random"
        for checkpoint_kind, policy in [
            ("original", "risk_base"),
            ("modified", "risk_base"),
            ("modified", "risk_topk8"),
        ]:
            prefix = f"receding_{cadence}_{checkpoint_kind}_{policy}_h{horizon}"
            previous = add_runtime_pair(
                prefix,
                checkpoint_kind,
                policy,
                horizon,
                [previous],
                detector_base=model_root / "base",
                detector_top8=model_root / "unc_topk8",
            )

    # Canonical per-step matrix is expensive, so it runs after native/stride
    # retraining has produced the most relevant detector comparisons.
    for checkpoint_kind, policies in [
        ("original", ["simvla_only", "shadow_base", "risk_base"]),
        ("modified", ["simvla_only", "shadow_base", "risk_base", "shadow_topk8", "risk_topk8"]),
    ]:
        for policy in policies:
            prefix = f"core_exact_{checkpoint_kind}_{policy}_h1"
            previous = add_runtime_pair(prefix, checkpoint_kind, policy, 1, [previous])

    dean_full_dest = BOB_CAMPAIGN / "inputs/datasets/dean_object_uncertainty_4191"
    add_job(
        "400_sync_dean_4191",
        [
            "/usr/bin/python3",
            str(sync_script),
            "--remote-host",
            "dean@100.124.50.124",
            "--remote-root",
            "/home/dean/fiper_uncertainty_collection/runs/dean_object_uncertainty_20260529",
            "--dest",
            str(dean_full_dest),
            "--min-episodes",
            "4191",
        ],
        depends=[previous],
        checks=[{"type": "file", "path": str(dean_full_dest / "SYNC_MANIFEST.json")}],
        timeout=172800,
        allow_failed_dependencies=True,
    )
    previous = "400_sync_dean_4191"
    for cadence, cadence_args in [("native", "--cadence native"), ("stride10", "--cadence stride --stride 10")]:
        smoke_id = f"410_train_dean4191_{cadence}_smoke"
        train_id = f"411_train_dean4191_{cadence}_full"
        smoke_out = BOB_CAMPAIGN / f"smokes/train_dean4191_{cadence}"
        train_out = BOB_CAMPAIGN / f"models/dean4191_{cadence}"
        common = (
            f"/usr/bin/python3 {q(train_script)} --run-root {q(dean_full_dest)} --default-suite libero_object_object "
            f"{cadence_args} --splits all_tasks_random ood_last2_taskids --variants base unc_topk8 "
        )
        add_job(smoke_id, activated(common + f"--output-dir {q(smoke_out)} --smoke"), [previous], [{"type": "detector", "path": str(smoke_out / "all_tasks_random/base")}], 43200)
        add_job(
            train_id,
            activated(common + f"--output-dir {q(train_out)}"),
            [smoke_id],
            [
                {"type": "detector", "path": str(train_out / "all_tasks_random/base")},
                {"type": "detector", "path": str(train_out / "all_tasks_random/unc_topk8")},
            ],
            86400,
        )
        previous = train_id

    old_config = BOB_CAMPAIGN / "configs/v2_018_only.json"
    old_refs = BOB_FIPER / "experiments/prepared_20260527/00_global_main/datasets/refs"
    old_stride_refs = BOB_CAMPAIGN / "inputs/old_global_refs_stride10"
    filter_script = BOB_CAMPAIGN / "src/filter_refs_by_stride.py"
    add_job(
        "500_filter_old_refs_stride10",
        ["/usr/bin/python3", str(filter_script), "--source", str(old_refs), "--dest", str(old_stride_refs), "--stride", "10"],
        depends=[previous],
        checks=[{"type": "file", "path": str(old_stride_refs / "STRIDE_FILTER_REPORT.json")}],
        allow_failed_dependencies=True,
    )
    old_runner = BOB_FIPER / "scripts/run_clean_temporal_nextgen_campaign_v2.py"
    package_script = BOB_CAMPAIGN / "src/package_old_base_detector.py"
    previous = "500_filter_old_refs_stride10"
    for cadence, refs in [("native", old_refs), ("stride10", old_stride_refs)]:
        smoke_id = f"510_train_old_{cadence}_smoke"
        train_id = f"511_train_old_{cadence}_full"
        package_id = f"512_package_old_{cadence}"
        smoke_out = BOB_CAMPAIGN / f"smokes/train_old_{cadence}"
        train_out = BOB_CAMPAIGN / f"models/old4872_{cadence}_raw"
        package_out = BOB_CAMPAIGN / f"models/old4872_{cadence}/base"
        smoke_cmd = activated(
            f"cd {q(BOB_FIPER)}; /usr/bin/python3 {q(old_runner)} --campaign-config {q(old_config)} --refs-dir {q(refs)} "
            f"--output-dir {q(smoke_out)} --base-dir {q(BOB_FIPER)} --device cuda --only-job v2_018_transformer_k16 "
            "--max-train-rows 1024 --max-calib-rows 512 --max-eval-rows 512 --max-epochs 1 --patience 1 --batch-size 128 --force"
        )
        train_cmd = activated(
            f"cd {q(BOB_FIPER)}; /usr/bin/python3 {q(old_runner)} --campaign-config {q(old_config)} --refs-dir {q(refs)} "
            f"--output-dir {q(train_out)} --base-dir {q(BOB_FIPER)} --device cuda --only-job v2_018_transformer_k16 --force"
        )
        add_job(smoke_id, smoke_cmd, [previous], [{"type": "file", "path": str(smoke_out / "jobs/v2_018_transformer_k16/model.pt")}], 43200)
        add_job(train_id, train_cmd, [smoke_id], [{"type": "file", "path": str(train_out / "jobs/v2_018_transformer_k16/model.pt")}], 86400)
        add_job(
            package_id,
            ["/usr/bin/python3", str(package_script), "--source-job", str(train_out / "jobs/v2_018_transformer_k16"), "--dest", str(package_out)],
            [train_id],
            [{"type": "detector", "path": str(package_out)}],
        )
        previous = package_id

    # Long backlog: broad paired success-rate scan. The first ten tasks of each
    # selected suite are prioritized; LIBERO-90 can be extended by regenerating
    # this manifest with a larger task range.
    suite_tasks = {
        "libero_spatial_object": range(10),
        "libero_object_object": range(10),
        "libero_goal_object": range(10),
        "libero_10_object": range(10),
        "libero_90": range(10),
    }
    rng = random.Random(20260605077)
    for suite, task_ids in suite_tasks.items():
        for task_id in task_ids:
            reset_seeds = rng.sample(range(1, 2**31 - 1), 100)
            for checkpoint_kind, policy in [
                ("original", "simvla_only"),
                ("original", "risk_base"),
                ("modified", "risk_topk8"),
            ]:
                prefix = f"broad_{suite}_t{task_id:02d}_{checkpoint_kind}_{policy}_h10"
                previous = add_runtime_pair(
                    prefix,
                    checkpoint_kind,
                    policy,
                    10,
                    [previous],
                    exact=False,
                    suite=suite,
                    task_id=task_id,
                    reset_seeds=reset_seeds,
                )

    manifest = {
        "campaign_id": CAMPAIGN_ID,
        "campaign_root": str(BOB_CAMPAIGN),
        "created": "2026-06-05",
        "min_free_disk_gb": 40,
        "frozen_detector_families": {
            "base": {"static_dim": 43, "uncertainty_dims": []},
            "unc_topk8": {"static_dim": 51, "uncertainty_dims": TOPK8_DIMS},
        },
        "job_count": len(jobs),
        "jobs": jobs,
    }
    write_json(local_root / "manifests/campaign_manifest.json", manifest)
    write_json(
        local_root / "manifests/seed_audit.json",
        {
            "global_action_seed": 206050917,
            "model_load_seed": 206050911,
            "broad_seed_generator": 20260605077,
            "manifest_sha256": hashlib.sha256(json.dumps(manifest, sort_keys=True).encode()).hexdigest(),
        },
    )
    print(json.dumps({"jobs": len(jobs), "manifest": str(local_root / 'manifests/campaign_manifest.json')}, indent=2))


if __name__ == "__main__":
    main()
