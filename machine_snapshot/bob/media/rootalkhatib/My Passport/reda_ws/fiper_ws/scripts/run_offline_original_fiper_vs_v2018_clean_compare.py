#!/usr/bin/env python3
"""Clean offline comparison: original FIPER-style RND/ACE vs v2_018.

This runner intentionally uses one canonical refs directory for both methods.
Original FIPER-style training uses only success_train_seen action chunks for RND,
and calibrates RND/ACE thresholds only on success_calib_seen. The selected
v2_018 model is retrained through the existing clean temporal campaign code.
"""

from __future__ import annotations

import argparse
import json
import random
import shutil
import time
from pathlib import Path
from typing import Any

import numpy as np
import torch
from torch import nn
from torch.utils.data import DataLoader, Dataset

import run_clean_temporal_nextgen_campaign_v2 as clean


class ActionDataset(Dataset):
    def __init__(self, x: np.ndarray) -> None:
        self.x = torch.tensor(x, dtype=torch.float32)

    def __len__(self) -> int:
        return int(self.x.shape[0])

    def __getitem__(self, idx: int) -> torch.Tensor:
        return self.x[idx]


class RNDNetwork(nn.Module):
    def __init__(self, input_dim: int = 70, hidden_dim: int = 256, output_dim: int = 128) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_dim),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)


class OriginalFIPERRND(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.predictor = RNDNetwork()
        self.prior = RNDNetwork()
        for p in self.prior.parameters():
            p.requires_grad = False

    def score(self, x: torch.Tensor) -> torch.Tensor:
        pred = self.predictor(x)
        with torch.no_grad():
            target = self.prior(x)
        return torch.norm(pred - target, dim=-1) ** 2


def seed_everything(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def fit_standardizer(actions: np.ndarray) -> dict[str, list[float]]:
    mean = np.mean(actions, axis=0)
    std = np.std(actions, axis=0)
    std = np.where(std < 1e-4, 1.0, std)
    return {"mean": mean.tolist(), "std": std.tolist()}


def apply_standardizer(actions: np.ndarray, stats: dict[str, Any]) -> np.ndarray:
    mean = np.asarray(stats["mean"], dtype=np.float32)
    std = np.asarray(stats["std"], dtype=np.float32)
    out = (actions.astype(np.float32) - mean) / std
    return np.clip(out, -10.0, 10.0).astype(np.float32)


def flat_actions(rows: list[clean.CompactRow]) -> np.ndarray:
    return np.stack([r.action_flat for r in rows], axis=0).astype(np.float32)


def train_original_fiper(
    rows_by_split: dict[str, list[clean.CompactRow]],
    out_dir: Path,
    device: torch.device,
    epochs: int,
    batch_size: int,
) -> tuple[OriginalFIPERRND, dict[str, Any], list[dict[str, Any]]]:
    model = OriginalFIPERRND().to(device)
    train_actions_raw = flat_actions(rows_by_split["success_train_seen"])
    stats = fit_standardizer(train_actions_raw)
    train_actions = apply_standardizer(train_actions_raw, stats)
    loader = DataLoader(ActionDataset(train_actions), batch_size=batch_size, shuffle=True, drop_last=False)
    opt = torch.optim.Adam(model.predictor.parameters(), lr=1e-3)
    history: list[dict[str, Any]] = []

    for epoch in range(1, epochs + 1):
        model.train()
        losses: list[float] = []
        for xb in loader:
            xb = xb.to(device)
            opt.zero_grad(set_to_none=True)
            pred = model.predictor(xb)
            with torch.no_grad():
                target = model.prior(xb)
            loss = nn.functional.mse_loss(pred, target)
            loss.backward()
            opt.step()
            losses.append(float(loss.detach().cpu()))
        row = {"epoch": epoch, "loss": float(np.mean(losses))}
        history.append(row)
        print(json.dumps({"original_fiper_rnd": row}, sort_keys=True), flush=True)

    model_dir = out_dir / "original_fiper" / "model"
    model_dir.mkdir(parents=True, exist_ok=True)
    torch.save(model.predictor.state_dict(), model_dir / "rnd_predictor.pt")
    torch.save(model.prior.state_dict(), model_dir / "rnd_prior.pt")
    (model_dir / "normalization.json").write_text(json.dumps(stats, indent=2, sort_keys=True) + "\n")
    (model_dir / "training_history.json").write_text(json.dumps(history, indent=2, sort_keys=True) + "\n")
    return model, stats, history


def score_original_fiper(
    model: OriginalFIPERRND,
    rows_by_split: dict[str, list[clean.CompactRow]],
    stats: dict[str, Any],
    device: torch.device,
    batch_size: int,
) -> dict[str, np.ndarray]:
    scores: dict[str, np.ndarray] = {}
    model.eval()
    with torch.no_grad():
        for split, rows in rows_by_split.items():
            x = apply_standardizer(flat_actions(rows), stats)
            loader = DataLoader(ActionDataset(x), batch_size=batch_size, shuffle=False, drop_last=False)
            parts: list[np.ndarray] = []
            for xb in loader:
                parts.append(model.score(xb.to(device)).detach().cpu().numpy())
            scores[split] = np.concatenate(parts).astype(np.float32)
    return scores


def original_thresholds(
    rows_by_split: dict[str, list[clean.CompactRow]],
    scores_by_split: dict[str, np.ndarray],
) -> dict[str, Any]:
    calib_scores = scores_by_split["success_calib_seen"]
    calib_ace = np.asarray([r.ace[0] for r in rows_by_split["success_calib_seen"]], dtype=np.float32)
    quantiles = {"q90": 0.90, "q95": 0.95, "q99": 0.99}
    return {
        "score": {
            "eventual": {
                q: float(np.quantile(calib_scores, p))
                for q, p in quantiles.items()
            }
        },
        "ace": {
            q: float(np.quantile(calib_ace, p))
            for q, p in quantiles.items()
        },
        "residual": {},
    }


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def metric(metrics: dict[str, Any], split: str, policy: str, field: str) -> Any:
    return metrics.get("episode_metrics", {}).get(split, {}).get(policy, {}).get(field)


def compact_metric_table(metrics: dict[str, Any], policies: list[str]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for policy in policies:
        out[policy] = {
            "seen_success_false_alarm": metric(metrics, "success_test_seen", policy, "episode_alarm_rate"),
            "ood_success_false_alarm": metric(metrics, "success_test_ood", policy, "episode_alarm_rate"),
            "seen_failure_detection": metric(metrics, "failure_test_seen", policy, "episode_alarm_rate"),
            "seen_failure_det_at_25": metric(metrics, "failure_test_seen", policy, "det_at_25"),
            "seen_failure_det_at_50": metric(metrics, "failure_test_seen", policy, "det_at_50"),
            "ood_failure_detection": metric(metrics, "failure_eval_ood", policy, "episode_alarm_rate"),
            "ood_failure_det_at_10": metric(metrics, "failure_eval_ood", policy, "det_at_10"),
            "ood_failure_det_at_25": metric(metrics, "failure_eval_ood", policy, "det_at_25"),
            "ood_failure_det_at_50": metric(metrics, "failure_eval_ood", policy, "det_at_50"),
            "ood_failure_mean_detection_time": metric(metrics, "failure_eval_ood", policy, "mean_first_norm_detected"),
            "ood_failure_never": metric(metrics, "failure_eval_ood", policy, "never_rate"),
        }
    return out


def pct(value: Any) -> str:
    if value is None:
        return "NA"
    return f"{float(value) * 100:.1f}%"


def num(value: Any) -> str:
    if value is None:
        return "NA"
    return f"{float(value):.3f}"


def write_report(
    out_dir: Path,
    refs_dir: Path,
    original_summary: dict[str, Any],
    v2018_summary: dict[str, Any],
    v2018_job_summary: dict[str, Any],
) -> None:
    rows = [
        ("Original FIPER RND score q95 K3", original_summary["eventual_score_q95_K3"]),
        ("Original FIPER ACE q95 K3", original_summary["eventual_ace_q95_K3"]),
        ("Original FIPER OR q95 K3", original_summary["eventual_or_q95_K3"]),
        ("Original FIPER AND q95 K3", original_summary["eventual_and_q95_K3"]),
        ("Selected v2_018 score q95 K3", v2018_summary["eventual_score_q95_K3"]),
        ("Selected v2_018 ACE q95 K3", v2018_summary["eventual_ace_q95_K3"]),
        ("Selected v2_018 OR q95 K3", v2018_summary["eventual_or_q95_K3"]),
        ("Selected v2_018 AND q95 K3", v2018_summary["eventual_and_q95_K3"]),
    ]
    lines = [
        "# Clean Offline Original FIPER vs v2_018 Comparison",
        "",
        f"- Created: {time.strftime('%Y-%m-%d %H:%M:%S')}",
        f"- Refs dir: `{refs_dir}`",
        "- Training hygiene:",
        "  - Original FIPER RND trained only on `success_train_seen`.",
        "  - Original FIPER thresholds calibrated only on `success_calib_seen`.",
        "  - v2_018 retrained with the clean temporal campaign code on seen success/failure train rows.",
        "  - OOD rows are evaluation-only for both methods.",
        "",
        "## Main Shared Metrics",
        "",
        "| Method / Policy | Seen FA | OOD FA | Seen Failure Det | OOD Failure Det | OOD Det@10 | OOD Det@25 | OOD Det@50 | Mean OOD Det Time | OOD Never |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for name, vals in rows:
        lines.append(
            f"| {name} | {pct(vals['seen_success_false_alarm'])} | {pct(vals['ood_success_false_alarm'])} | "
            f"{pct(vals['seen_failure_detection'])} | {pct(vals['ood_failure_detection'])} | "
            f"{pct(vals['ood_failure_det_at_10'])} | {pct(vals['ood_failure_det_at_25'])} | "
            f"{pct(vals['ood_failure_det_at_50'])} | {num(vals['ood_failure_mean_detection_time'])} | "
            f"{pct(vals['ood_failure_never'])} |"
        )
    lines.extend([
        "",
        "## v2_018 Run Details",
        "",
        f"- Best epoch: `{v2018_job_summary.get('best_epoch')}`",
        f"- Feature audit history dim: `{v2018_job_summary.get('feature_audit', {}).get('history_dim')}`",
        f"- Feature audit static dim: `{v2018_job_summary.get('feature_audit', {}).get('current_feature_dim')}`",
        f"- Uses reward: `{v2018_job_summary.get('feature_audit', {}).get('uses_reward')}`",
        f"- Uses success: `{v2018_job_summary.get('feature_audit', {}).get('uses_success')}`",
        f"- Uses object poses: `{v2018_job_summary.get('feature_audit', {}).get('uses_object_positions_before')}`",
        f"- Uses task metadata as input: `{v2018_job_summary.get('feature_audit', {}).get('uses_task_metadata_as_input')}`",
        f"- Uses OOD rows for train: `{v2018_job_summary.get('feature_audit', {}).get('uses_ood_rows_for_train')}`",
        "",
        "## Verdict",
        "",
        "Use the `eventual_or_q95_K3` rows when comparing closest to the older FIPER alarm logic.",
        "Use the `eventual_score_q95_K3` rows when comparing learned-risk score-only behavior.",
    ])
    (out_dir / "CLEAN_OFFLINE_ORIGINAL_FIPER_VS_V2018_REPORT.md").write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refs-dir", required=True)
    parser.add_argument("--base-dir", default=".")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--rnd-epochs", type=int, default=20)
    parser.add_argument("--batch-size", type=int, default=384)
    parser.add_argument("--v2018-max-epochs", type=int, default=120)
    parser.add_argument("--v2018-patience", type=int, default=18)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    seed_everything(args.seed)
    out_dir = Path(args.output_dir)
    if args.force and out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(Path(__file__), out_dir / "runner_snapshot.py")

    device = torch.device(args.device if args.device == "cpu" or torch.cuda.is_available() else "cpu")
    refs_dir = Path(args.refs_dir)
    base_dir = Path(args.base_dir)
    history_steps_needed = [4, 8, 16]
    rows_by_split = clean.load_rows_from_refs(refs_dir, base_dir, {}, history_steps_needed)

    for split in ["success_train_seen", "success_val_seen", "success_calib_seen", "failure_train_seen", "failure_val_seen"]:
        bad = [r.episode_key for r in rows_by_split[split] if r.is_ood_split or "ood" in r.split]
        if bad:
            raise RuntimeError(f"OOD leakage into {split}: first={bad[:3]}")

    dataset_manifest = {
        "refs_dir": str(refs_dir),
        "base_dir": str(base_dir),
        "splits": {
            split: {
                "rows": len(rows),
                "episodes": len({r.episode_key for r in rows}),
                "success_rows": sum(1 for r in rows if r.outcome == "success"),
                "failure_rows": sum(1 for r in rows if r.outcome != "success"),
            }
            for split, rows in rows_by_split.items()
        },
    }
    write_json(out_dir / "dataset_manifest.json", dataset_manifest)

    model, rnd_stats, rnd_history = train_original_fiper(
        rows_by_split, out_dir, device, args.rnd_epochs, args.batch_size
    )
    original_scores = score_original_fiper(model, rows_by_split, rnd_stats, device, args.batch_size)
    original_thresholds_obj = original_thresholds(rows_by_split, original_scores)
    original_metrics = clean.evaluate_job(
        rows_by_split,
        original_scores,
        {split: None for split in rows_by_split},
        original_thresholds_obj,
        {
            "name": "original_fiper_rnd_ace_clean",
            "mode": "success_only_rnd_plus_ace",
            "include_ace": True,
            "include_ace_history": False,
            "include_action": True,
            "include_proprio": False,
            "include_history": False,
        },
    )
    original_summary = compact_metric_table(
        original_metrics,
        ["eventual_score_q95_K3", "eventual_ace_q95_K3", "eventual_or_q95_K3", "eventual_and_q95_K3"],
    )
    write_json(out_dir / "original_fiper" / "thresholds.json", original_thresholds_obj)
    write_json(out_dir / "original_fiper" / "metrics.json", original_metrics)
    write_json(out_dir / "original_fiper" / "summary_metrics.json", original_summary)

    v2018_cfg = {
        "action_repr": "stats",
        "batch_size": args.batch_size,
        "heads": 4,
        "history_steps": 16,
        "include_ace": True,
        "include_ace_history": True,
        "include_action": True,
        "include_objects": False,
        "include_proprio": True,
        "layers": 3,
        "max_epochs": args.v2018_max_epochs,
        "mode": "supervised",
        "model": "seq_transformer",
        "name": "v2_018_transformer_k16_clean_rerun",
        "patience": args.v2018_patience,
        "seed": args.seed,
        "width": 128,
    }
    ns = argparse.Namespace(force=args.force)
    v2018_job_summary = clean.run_one_job(v2018_cfg, rows_by_split, out_dir / "v2018", device, ns)
    v2018_metrics = json.loads((out_dir / "v2018" / "jobs" / v2018_cfg["name"] / "metrics.json").read_text())
    v2018_summary = compact_metric_table(
        v2018_metrics,
        ["eventual_score_q95_K3", "eventual_ace_q95_K3", "eventual_or_q95_K3", "eventual_and_q95_K3"],
    )
    write_json(out_dir / "v2018" / "summary_metrics.json", v2018_summary)

    write_report(out_dir, refs_dir, original_summary, v2018_summary, v2018_job_summary)
    write_json(
        out_dir / "run_manifest.json",
        {
            "seed": args.seed,
            "device": str(device),
            "rnd_epochs": args.rnd_epochs,
            "batch_size": args.batch_size,
            "v2018_config": v2018_cfg,
            "feature_hygiene": {
                "original_fiper_uses_failure_labels_for_training": False,
                "original_fiper_uses_ood_for_training": False,
                "v2018_uses_ood_for_training": bool(v2018_job_summary.get("feature_audit", {}).get("uses_ood_rows_for_train")),
            },
        },
    )
    print(json.dumps({"done": True, "output_dir": str(out_dir)}, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
