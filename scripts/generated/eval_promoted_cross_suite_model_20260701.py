#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import shutil
import sys
from pathlib import Path

import numpy as np
import torch


ROOT = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630")
TRAIN_SCRIPT = ROOT / "scripts/train_seen_goal_object_to_many_ood_20260630.py"
SOURCE_EXP = ROOT / "experiments/train_seen_goal_object_eval_goal_swap_100"
PROMOTED = ROOT / "models/simvla_h10_topk8_official_goal_object_seen_main_20260701"
OUT = ROOT / "experiments/eval_promoted_single_model_all_ood_20260701"

DATASETS = [
    "goal_swap_100",
    "goal_task_100",
    "goal_object_ood_180",
    "spatial_object_100",
    "object_object_100",
    "libero10_object_100",
]


def load_train_module():
    spec = importlib.util.spec_from_file_location("train_seen_goal_object_to_many_ood_20260630", TRAIN_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot import {TRAIN_SCRIPT}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def promote_model():
    PROMOTED.mkdir(parents=True, exist_ok=True)
    for name in ["model.pt", "normalization.json", "results.json", "split_episode_ids.json", "SIMVLA_GOAL_TO_GOAL_OBJECT_OOD_REPORT_20260622.md"]:
        src = SOURCE_EXP / name
        if src.exists():
            shutil.copy2(src, PROMOTED / name)

    src_results = json.loads((SOURCE_EXP / "results.json").read_text())
    manifest = {
        "promoted_model_name": "simvla_h10_topk8_official_goal_object_seen_main_20260701",
        "source_experiment": str(SOURCE_EXP),
        "selection_rule": "highest source validation AUPRC among the six repeated same-source trainings; no OOD performance used for selection",
        "selected_source_val_auprc": max(r["val_auprc"] for r in src_results["train_history"]),
        "selected_source_val_auroc": max(src_results["train_history"], key=lambda r: r["val_auprc"])["val_auroc"],
        "selected_epoch": src_results["best_epoch"],
        "source_dataset": src_results["source"],
        "thresholds": src_results["thresholds"],
        "feature_schema": src_results["feature_schema"],
        "notes": [
            "This is the new promoted main model for the cross-suite official OOD campaign.",
            "It was trained only on the Sam official libero_goal_object seen source dataset.",
            "The same checkpoint and same seen-calibrated thresholds are applied to every OOD dataset in eval_promoted_single_model_all_ood_20260701.",
        ],
    }
    (PROMOTED / "PROMOTED_MODEL_MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n")
    (PROMOTED / "README.md").write_text(
        "# Promoted Main SimVLA H10 TopK8 Risk Model\n\n"
        "Name: `simvla_h10_topk8_official_goal_object_seen_main_20260701`\n\n"
        "Selected from repeated same-source trainings by highest source validation AUPRC only. "
        "No OOD target performance was used to choose this checkpoint.\n\n"
        f"Source experiment: `{SOURCE_EXP}`\n\n"
        "Use this directory's `model.pt`, `normalization.json`, and `results.json` thresholds for future offline OOD evaluations.\n"
    )
    return manifest


def std_from_json(path: Path):
    d = json.loads(path.read_text())
    return {
        key: {
            "mean": np.asarray(val["mean"], dtype=np.float32),
            "std": np.asarray(val["std"], dtype=np.float32),
        }
        for key, val in d.items()
    }


def evaluate_dataset(mod, model, stats, thresholds, dataset_id, device):
    target_root = ROOT / "datasets" / dataset_id
    target_query, target_summary = mod.find_dataset_files(target_root)
    target_rows = mod.load_goal_object_target(target_query, target_summary, None)
    h_raw, a_raw, st_raw, y = mod.arrays(target_rows)
    h = mod.apply_std(h_raw, stats["history"])
    a = mod.apply_std(a_raw, stats["action"])
    st = mod.apply_std(st_raw, stats["static"])
    scores = mod.predict(model, h, a, st, device, 4096)
    step = {
        "auroc": float(mod.roc_auc_score(y.astype(int), scores)) if len(set(y.astype(int).tolist())) == 2 else 0.5,
        "auprc": float(mod.average_precision_score(y.astype(int), scores)) if len(set(y.astype(int).tolist())) == 2 else 0.0,
    }
    metrics = {}
    for name, th in thresholds.items():
        metrics[name] = {
            "threshold": float(th),
            "step": mod.step_metrics(y, scores, float(th)),
            "episode": mod.episode_metrics(target_rows, scores, float(th)),
        }
    return {
        "dataset": dataset_id,
        "target_root": str(target_root),
        "rows": len(target_rows),
        "episodes": len({r.episode_id for r in target_rows}),
        "success_episodes": len({r.episode_id for r in target_rows if r.y < 0.5}),
        "failure_episodes": len({r.episode_id for r in target_rows if r.y >= 0.5}),
        "step_overall": step,
        "metrics": metrics,
    }


def main():
    mod = load_train_module()
    manifest = promote_model()
    OUT.mkdir(parents=True, exist_ok=True)

    thresholds = manifest["thresholds"]
    stats = std_from_json(PROMOTED / "normalization.json")
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = mod.SeqRiskModel(static_dim=manifest["feature_schema"]["static_dim"]).to(device)
    state = torch.load(PROMOTED / "model.pt", map_location=device)
    model.load_state_dict(state)
    model.eval()

    results = {
        "experiment": "eval_promoted_single_model_all_ood_20260701",
        "promoted_model": manifest,
        "datasets": {},
    }
    rows = []
    for dataset_id in DATASETS:
        print(f"[eval] {dataset_id}", flush=True)
        res = evaluate_dataset(mod, model, stats, thresholds, dataset_id, device)
        results["datasets"][dataset_id] = res
        for th_name, th_res in res["metrics"].items():
            ep = th_res["episode"]
            rows.append({
                "dataset": dataset_id,
                "threshold": th_name,
                "value": th_res["threshold"],
                "success_fa": ep["episode_false_alarm_rate"],
                "failure_det": ep["failure_detection_rate"],
                "det10": ep.get("det_at_10"),
                "det25": ep["det_at_25"],
                "det50": ep["det_at_50"],
                "mean_time": ep["mean_detection_fraction"],
            })

    (OUT / "results.json").write_text(json.dumps(results, indent=2) + "\n")

    report = [
        "# Promoted Single-Checkpoint Cross-Suite OOD Evaluation",
        "",
        f"Promoted model: `{manifest['promoted_model_name']}`",
        f"Selection rule: {manifest['selection_rule']}",
        "",
        "## Best Per Dataset Among Seen-Calibrated Thresholds",
        "",
        "| Dataset | Threshold | Value | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for dataset_id in DATASETS:
        ds_rows = [r for r in rows if r["dataset"] == dataset_id]
        best = max(ds_rows, key=lambda r: (r["failure_det"] - r["success_fa"], r["failure_det"], -r["mean_time"] if r["mean_time"] is not None else -9))
        mt = "n/a" if best["mean_time"] is None else f"{best['mean_time']:.3f}"
        det10 = "n/a" if best["det10"] is None else f"{100*best['det10']:.2f}%"
        report.append(
            f"| {dataset_id} | {best['threshold']} | {best['value']:.4f} | "
            f"{100*best['success_fa']:.2f}% | {100*best['failure_det']:.2f}% | "
            f"{det10} | {100*best['det25']:.2f}% | {100*best['det50']:.2f}% | {mt} |"
        )

    report += [
        "",
        "## Full Threshold Table",
        "",
        "| Dataset | Threshold | Value | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for r in rows:
        mt = "n/a" if r["mean_time"] is None else f"{r['mean_time']:.3f}"
        det10 = "n/a" if r["det10"] is None else f"{100*r['det10']:.2f}%"
        report.append(
            f"| {r['dataset']} | {r['threshold']} | {r['value']:.4f} | "
            f"{100*r['success_fa']:.2f}% | {100*r['failure_det']:.2f}% | "
            f"{det10} | {100*r['det25']:.2f}% | {100*r['det50']:.2f}% | {mt} |"
        )
    report += [
        "",
        "## Legitimacy Notes",
        "",
        "- This evaluation uses one promoted checkpoint for every OOD dataset.",
        "- The checkpoint was selected by source validation AUPRC only.",
        "- Threshold values are carried from the promoted model's source validation calibration.",
        "- The per-dataset best row is diagnostic only because it chooses among seen-calibrated threshold rules after seeing OOD outcomes.",
    ]
    (OUT / "PROMOTED_SINGLE_MODEL_OOD_EVAL_REPORT_20260701.md").write_text("\n".join(report) + "\n")
    print(f"DONE {OUT / 'PROMOTED_SINGLE_MODEL_OOD_EVAL_REPORT_20260701.md'}", flush=True)


if __name__ == "__main__":
    main()
