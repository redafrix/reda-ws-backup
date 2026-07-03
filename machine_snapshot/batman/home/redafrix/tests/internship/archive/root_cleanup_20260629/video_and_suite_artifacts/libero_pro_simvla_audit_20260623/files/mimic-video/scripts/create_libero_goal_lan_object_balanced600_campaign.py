#!/usr/bin/env python3
"""Create frozen configs for the eight-policy balanced-600 campaign."""

from __future__ import annotations

import copy
import hashlib
import json
import pathlib


ROOT = pathlib.Path(__file__).resolve().parents[1]
PROTOCOL = "configs/uq_benchmarks/libero_goal_lan_object_balanced600_eval_seed0_20260622.csv"
CAMPAIGN_ROOT = "results/libero_goal_lan_object_balanced600_20260622"
ARBITER_CONFIG_ROOT = ROOT / "configs" / "arbiter"
CAMPAIGN_PATH = ROOT / "configs" / "uq_benchmarks" / "libero_goal_lan_object_balanced600_campaign_20260622.json"
WM_RISK_MODEL = (
    "model/checkpoints/uncertainty/skill_reliability/"
    "campaign_plus_v2_scalar_only_fusion_20260622/ng_gru_h8_action_v2wace_s1"
)
WM_THRESHOLD = 0.30135667


def main() -> None:
    protocol_path = ROOT / PROTOCOL
    if not protocol_path.is_file():
        raise FileNotFoundError(protocol_path)
    ARBITER_CONFIG_ROOT.mkdir(parents=True, exist_ok=True)
    arbiter_configs = _write_arbiter_configs()
    campaign = {
        "schema_version": "libero_goal_lan_object_balanced600_campaign_v1",
        "campaign_id": "libero_goal_lan_object_balanced600_20260622",
        "protocol_csv": PROTOCOL,
        "protocol_json": PROTOCOL.replace(".csv", ".json"),
        "protocol_sha256": _sha256(protocol_path),
        "expected_episode_count": 600,
        "expected_suites": ["libero_goal_lan", "libero_goal_object"],
        "expected_task_ids": list(range(10)),
        "episodes_per_suite_task": 30,
        "max_episode_steps": 250,
        "prompt_source": "bddl_language",
        "policy_order": [
            "wm_h56",
            "wm_h28",
            "wm_h14",
            "hf_simvla",
            "modified_simvla_60k",
            "wm_risk_h56_h21",
            "wm_risk_medoid_h56_h21",
            "dual_simvla_wm_risk_h56_h21",
        ],
        "policies": {
            "wm_h56": _base_wm_policy(56),
            "wm_h28": _base_wm_policy(28),
            "wm_h14": _base_wm_policy(14),
            "hf_simvla": _arbiter_policy(arbiter_configs["hf_simvla"]),
            "modified_simvla_60k": _arbiter_policy(arbiter_configs["modified_simvla_60k"]),
            "wm_risk_h56_h21": _risk_wm_policy("calibrator_adaptive_horizon"),
            "wm_risk_medoid_h56_h21": _risk_wm_policy("risk_gated_action_medoid_horizon"),
            "dual_simvla_wm_risk_h56_h21": _arbiter_policy(arbiter_configs["dual"]),
        },
        "artifacts": _artifacts(),
    }
    CAMPAIGN_PATH.write_text(json.dumps(campaign, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {CAMPAIGN_PATH}")
    for path in arbiter_configs.values():
        print(f"wrote {path}")


def _base_wm_policy(horizon: int) -> dict[str, object]:
    policy_id = f"wm_h{horizon}"
    return {
        "runner": "world_model",
        "output_root": f"{CAMPAIGN_ROOT}/{policy_id}",
        "enable_v2w_uncertainty": True,
        "execute_horizon": horizon,
        "uq_num_action_candidates": 8,
        "uq_num_world_candidates": 3,
        "uq_action_candidate_batch_size": 4,
        "uq_control_policy": "first_candidate",
        "save_candidate_arrays": True,
        "save_v2w_variance_arrays": True,
    }


def _risk_wm_policy(control_policy: str) -> dict[str, object]:
    policy_id = "wm_risk_medoid_h56_h21" if control_policy == "risk_gated_action_medoid_horizon" else "wm_risk_h56_h21"
    return {
        "runner": "world_model",
        "output_root": f"{CAMPAIGN_ROOT}/{policy_id}",
        "enable_v2w_uncertainty": True,
        "execute_horizon": 56,
        "uq_num_action_candidates": 8,
        "uq_num_world_candidates": 3,
        "uq_action_candidate_batch_size": 4,
        "uq_control_policy": control_policy,
        "uq_risk_model_dir": WM_RISK_MODEL,
        "uq_risk_threshold": WM_THRESHOLD,
        "uq_risk_medium_threshold": 0.0,
        "uq_risk_persistence": 1,
        "uq_risk_medium_execute_actions": 56,
        "uq_risk_high_execute_actions": 21,
        "save_candidate_arrays": True,
        "save_v2w_variance_arrays": True,
    }


def _arbiter_policy(path: pathlib.Path) -> dict[str, object]:
    config = json.loads(path.read_text(encoding="utf-8"))
    return {
        "runner": "arbiter",
        "config": str(path.relative_to(ROOT)),
        "config_sha256": _sha256(path),
        "output_root": config["output_dir"],
    }


def _write_arbiter_configs() -> dict[str, pathlib.Path]:
    base = _arbiter_config_base()
    configs: dict[str, dict[str, object]] = {}

    hf = copy.deepcopy(base)
    hf["arbiter"].update({"policy": "simvla_main", "description": "Official HF SimVLA-LIBERO baseline."})
    hf["simvla"]["checkpoint"] = str((ROOT / "model/checkpoints/simvla_base_libero_hf").resolve())
    hf["output_dir"] = f"{CAMPAIGN_ROOT}/hf_simvla"
    configs["hf_simvla"] = hf

    modified = copy.deepcopy(base)
    modified["arbiter"].update({"policy": "simvla_main", "description": "Modified SimVLA 60k baseline without risk intervention."})
    modified["output_dir"] = f"{CAMPAIGN_ROOT}/modified_simvla_60k"
    configs["modified_simvla_60k"] = modified

    dual = copy.deepcopy(base)
    dual["arbiter"].update(
        {
            "policy": "dual_main_risk_simvla_medoid",
            "description": (
                "Main SimVLA chunk is scored with the calibrated q95 detector; auxiliary chunks provide ACE and "
                "medoid selection. Three consecutive high-risk queries invoke the WM. WM low risk executes h56 "
                "and WM high risk executes h21."
            ),
            "shadow_world_model": True,
            "simvla_high_risk_streak": 3,
            "simvla_risk_score_source": "main",
            "simvla_trigger_threshold": "q95",
            "world_model_low_risk_execute_actions": 56,
            "both_high_execute_actions": 21,
            "max_fallback_calls_per_episode": 25,
            "world_model_risk_gate": True,
        }
    )
    dual["output_dir"] = f"{CAMPAIGN_ROOT}/dual_simvla_wm_risk_h56_h21"
    configs["dual"] = dual

    paths: dict[str, pathlib.Path] = {}
    for name, config in configs.items():
        path = ARBITER_CONFIG_ROOT / f"balanced600_{name}_20260622.json"
        path.write_text(json.dumps(config, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        paths[name] = path
    return paths


def _arbiter_config_base() -> dict[str, object]:
    return {
        "require_empty_output_dir": True,
        "expected_episode_count": 600,
        "simvla_bundle_root": "${WORLD_ROOT}/simvla_modified_risk_topk8_h10_20260608",
        "output_dir": "",
        "arbiter": {
            "policy": "simvla_main",
            "description": "",
            "simvla_trigger_threshold": "q95",
            "simvla_high_risk_streak": 3,
            "simvla_risk_score_source": "main",
            "world_model_low_risk_execute_actions": 56,
            "both_high_execute_actions": 21,
            "max_fallback_calls_per_episode": 25,
            "shadow_world_model": False,
            "world_model_risk_gate": True,
        },
        "simvla": {
            "checkpoint": "checkpoints/simvla_modified_ckpt_60000",
            "risk_model_unc_topk8_dir": "risk_models/h10_unc_topk8",
            "simvla_root": "${SIMVLA_ROOT}",
            "libero_pro_root": "${LIBERO_PRO_ROOT}",
            "norm_stats": "${SIMVLA_NORM_STATS}",
            "smolvlm_path": "${SMOLVLM_PATH}",
            "suite": "libero_goal_lan",
            "task_id": 0,
            "global_action_seed": 206080920,
            "model_load_seed": 206080911,
            "device": "cuda",
            "execution_horizon": 10,
            "ace_candidate_count": 8,
            "history_steps": 16,
            "image_size": 384,
            "resolution": 128,
            "env_camera_height": 480,
            "env_camera_width": 640,
            "simvla_input_height": 128,
            "simvla_input_width": 128,
            "model_denoise_steps": 10,
            "max_steps": 250,
            "warmup": 10,
            "selection_min_margin": 0.1,
            "selection_strong_margin": 0.15,
            "selection_max_first_action_l2": None,
            "selection_main_threshold": "q95",
            "selection_require_candidate_below_q95": False,
            "selection_cooldown_steps": 0,
            "selection_max_modifications_per_episode": 0,
            "selection_min_high_risk_streak": 1,
            "selection_min_timestep": 0,
            "selection_streak_threshold": "q95",
            "expected_topk8_dims": [6, 21, 25, 27, 23, 2, 26, 24],
            "episode_manifest_csv": PROTOCOL,
            "language_prompt_source": "manifest",
            "reset_seeds": [0],
        },
        "world_model": _dual_world_model_config(),
    }


def _dual_world_model_config() -> dict[str, object]:
    return {
        "experiment": "w2a_libero_goal_half_v2w_libero_goal_agentview_lora_rank256_lr1.778e-04_bsz32_iter_000007020_fused_lr1.000e-04_layer20_bsz128",
        "video_model": "model/checkpoints/video_backbone/v2w_libero_goal_agentview_lora_rank256_lr1.778e-04_bsz32_iter_000007020_fused.pt",
        "action_model": "model/checkpoints/action_decoder/w2a_libero_goal_half_v2w_libero_goal_agentview_lora_rank256_lr1.778e-04_bsz32_iter_000007020_fused_lr1.000e-04_layer20_bsz128_iter_000050022.pt",
        "dataset_statistics": "model/checkpoints/dataset_statistics/libero_goal_half.json",
        "v2w_uncertainty_head": "model/checkpoints/uncertainty/v2w_heads/libero_goal_variantA_nll_plus_energy_stride7_eps500_modeB10_from_flow_fixedmask_2ep_20260531_120356/v2w_uncertainty_head.pt",
        "v2w_calibration": "model/checkpoints/uncertainty/v2w_heads/libero_goal_stride7_variantA_calibration.npz",
        "uq_risk_model_dir": WM_RISK_MODEL,
        "uq_risk_threshold": WM_THRESHOLD,
        "img_horizon": 5,
        "lowdim_horizon": 1,
        "stop_video_denoising_step": 0,
        "num_execute_actions": 56,
        "num_sampling_steps": 2,
        "use_text_encoder": False,
        "uq_num_action_candidates": 8,
        "uq_action_candidate_batch_size": 4,
        "uq_num_world_candidates": 3,
        "uq_save_candidate_arrays": True,
        "v2w_uncertainty_variant": "a",
        "v2w_uncertainty_save_variance_arrays": True,
        "uq_control_policy": "calibrator_adaptive_horizon",
        "uq_risk_medium_threshold": 0.0,
        "uq_risk_persistence": 1,
        "uq_risk_medium_execute_actions": 56,
        "uq_risk_high_execute_actions": 21,
        "uq_risk_score_semantics": "episode_failure_risk_action_plus_v2w_ace_history8",
    }


def _artifacts() -> dict[str, dict[str, str]]:
    paths = {
        "wm_risk_model": ROOT / WM_RISK_MODEL / "model.pt",
        "wm_risk_metadata": ROOT / WM_RISK_MODEL / "metadata.json",
        "wm_conformal_thresholds": ROOT / "results/full_uq_model_campaign_plus_v2_scalar_only_fusion_20260622/plus_heldout_eval/conformal_thresholds.csv",
        "wm_video_model": ROOT / "model/checkpoints/video_backbone/v2w_libero_goal_agentview_lora_rank256_lr1.778e-04_bsz32_iter_000007020_fused.pt",
        "wm_action_model": ROOT / "model/checkpoints/action_decoder/w2a_libero_goal_half_v2w_libero_goal_agentview_lora_rank256_lr1.778e-04_bsz32_iter_000007020_fused_lr1.000e-04_layer20_bsz128_iter_000050022.pt",
        "wm_dataset_statistics": ROOT / "model/checkpoints/dataset_statistics/libero_goal_half.json",
        "v2w_uncertainty_head": ROOT / "model/checkpoints/uncertainty/v2w_heads/libero_goal_variantA_nll_plus_energy_stride7_eps500_modeB10_from_flow_fixedmask_2ep_20260531_120356/v2w_uncertainty_head.pt",
        "v2w_calibration": ROOT / "model/checkpoints/uncertainty/v2w_heads/libero_goal_stride7_variantA_calibration.npz",
        "hf_simvla": ROOT / "model/checkpoints/simvla_base_libero_hf/model.safetensors",
        "modified_simvla_60k": ROOT.parent / "simvla_modified_risk_topk8_h10_20260608/checkpoints/simvla_modified_ckpt_60000/model.safetensors",
        "simvla_risk_model": ROOT.parent / "simvla_modified_risk_topk8_h10_20260608/risk_models/h10_unc_topk8/model.pt",
        "simvla_risk_thresholds": ROOT.parent / "simvla_modified_risk_topk8_h10_20260608/risk_models/h10_unc_topk8/thresholds.json",
        "simvla_norm_stats": ROOT.parent / "SimVLA_modified/norm_stats/libero_norm.json",
    }
    missing = [str(path) for path in paths.values() if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"Missing campaign artifacts: {missing}")
    return {
        name: {
            "path": str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path),
            "sha256": _sha256(path),
        }
        for name, path in paths.items()
    }


def _sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


if __name__ == "__main__":
    main()
