#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import math
import os
from pathlib import Path
from typing import Dict, Tuple

import matplotlib.pyplot as plt
import numpy as np
import torch
from tqdm import tqdm

from datasets import create_smolvlm_dataloader
from models.modeling_smolvlm_vla import SmolVLMVLA
from models.processing_smolvlm_vla import SmolVLMVLAProcessor


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        "Build predicted sigma^2 vs empirical flow MSE reliability curves"
    )
    parser.add_argument("--checkpoint", type=str, required=True)
    parser.add_argument("--metas_path", type=str, required=True)
    parser.add_argument("--output_dir", type=str, required=True)

    parser.add_argument("--norm_stats_path", type=str, default=None)
    parser.add_argument("--smolvlm_model_path", type=str, default=None)

    parser.add_argument("--batch_size", type=int, default=8)
    parser.add_argument("--num_workers", type=int, default=4)
    parser.add_argument("--num_time_samples", type=int, default=4)
    parser.add_argument("--max_batches", type=int, default=0)
    parser.add_argument("--max_points", type=int, default=2_000_000)

    parser.add_argument("--n_bins", type=int, default=15)
    parser.add_argument("--n_tau_bins", type=int, default=5)
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--device", type=str, default="cuda" if torch.cuda.is_available() else "cpu")
    return parser.parse_args()


def rankdata_average(x: np.ndarray) -> np.ndarray:
    order = np.argsort(x)
    ranks = np.empty_like(order, dtype=np.float64)
    sorted_x = x[order]

    start = 0
    while start < len(x):
        end = start + 1
        while end < len(x) and sorted_x[end] == sorted_x[start]:
            end += 1
        avg_rank = 0.5 * (start + 1 + end)
        ranks[order[start:end]] = avg_rank
        start = end

    return ranks


def spearman_corr(x: np.ndarray, y: np.ndarray) -> float:
    x = np.asarray(x, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    mask = np.isfinite(x) & np.isfinite(y)
    x = x[mask]
    y = y[mask]
    if len(x) < 3:
        return float("nan")

    rx = rankdata_average(x)
    ry = rankdata_average(y)

    rx = rx - rx.mean()
    ry = ry - ry.mean()

    denom = math.sqrt(float((rx * rx).sum() * (ry * ry).sum()))
    if denom <= 0:
        return float("nan")
    return float((rx * ry).sum() / denom)


def make_reliability_curve(
    sigma2: np.ndarray,
    residual2: np.ndarray,
    n_bins: int,
) -> Tuple[list[dict], dict]:
    sigma2 = np.asarray(sigma2, dtype=np.float64).reshape(-1)
    residual2 = np.asarray(residual2, dtype=np.float64).reshape(-1)

    mask = (
        np.isfinite(sigma2)
        & np.isfinite(residual2)
        & (sigma2 > 0.0)
        & (residual2 >= 0.0)
    )
    sigma2 = sigma2[mask]
    residual2 = residual2[mask]

    if len(sigma2) == 0:
        raise ValueError("No valid points for reliability curve")

    quantiles = np.linspace(0.0, 1.0, n_bins + 1)
    edges = np.quantile(sigma2, quantiles)
    edges = np.unique(edges)

    if len(edges) <= 2:
        raise ValueError("Predicted sigma2 has too few unique values to bin")

    # Bin IDs from 0 to len(edges)-2
    bin_ids = np.searchsorted(edges[1:-1], sigma2, side="right")

    rows = []
    total = len(sigma2)
    uce = 0.0

    for b in range(len(edges) - 1):
        idx = bin_ids == b
        if not np.any(idx):
            continue

        pred_mean = float(sigma2[idx].mean())
        mse_mean = float(residual2[idx].mean())
        count = int(idx.sum())
        stderr = float(residual2[idx].std() / math.sqrt(max(count, 1)))

        abs_gap = abs(mse_mean - pred_mean)
        uce += (count / total) * abs_gap

        rows.append(
            {
                "bin": int(b),
                "count": count,
                "sigma2_min": float(sigma2[idx].min()),
                "sigma2_max": float(sigma2[idx].max()),
                "mean_pred_sigma2": pred_mean,
                "empirical_flow_mse": mse_mean,
                "stderr_flow_mse": stderr,
                "abs_gap": float(abs_gap),
                "ratio_mse_over_sigma2": float(mse_mean / max(pred_mean, 1e-12)),
            }
        )

    metrics = {
        "num_points": int(total),
        "uce": float(uce),
        "mean_sigma2": float(sigma2.mean()),
        "mean_residual2": float(residual2.mean()),
        "global_scale_residual_over_sigma": float(residual2.mean() / max(sigma2.mean(), 1e-12)),
        "spearman_sigma2_residual2": spearman_corr(sigma2, residual2),
    }

    return rows, metrics


def save_curve_plot(rows: list[dict], output_path: Path, title: str) -> None:
    x = np.asarray([r["mean_pred_sigma2"] for r in rows], dtype=np.float64)
    y = np.asarray([r["empirical_flow_mse"] for r in rows], dtype=np.float64)
    yerr = np.asarray([r["stderr_flow_mse"] for r in rows], dtype=np.float64)

    fig, ax = plt.subplots(figsize=(6.5, 6.0))
    ax.errorbar(x, y, yerr=yerr, marker="o", capsize=3, linewidth=1.5)

    lo = float(min(x.min(), y.min()))
    hi = float(max(x.max(), y.max()))
    if hi <= lo:
        hi = lo + 1.0

    ax.plot([lo, hi], [lo, hi], linestyle="--", linewidth=1.2, label="perfect calibration")
    ax.set_xlabel("Mean predicted variance $\\sigma^2$")
    ax.set_ylabel("Empirical flow MSE $(v_\\theta - u^*)^2$")
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(output_path, dpi=180)
    plt.close(fig)


def save_curve_csv(rows: list[dict], output_path: Path) -> None:
    if not rows:
        return
    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def collect_arrays(args: argparse.Namespace) -> Dict[str, np.ndarray]:
    torch.manual_seed(args.seed)
    np.random.seed(args.seed)

    device = torch.device(args.device)

    load_kwargs = {}
    if args.smolvlm_model_path is not None:
        load_kwargs["smolvlm_model_path"] = args.smolvlm_model_path

    model = SmolVLMVLA.from_pretrained(
        args.checkpoint,
        predict_uncertainty=True,
        **load_kwargs,
    ).to(device)
    model.eval()

    if not getattr(model.config, "predict_uncertainty", False):
        raise RuntimeError("Loaded model does not have predict_uncertainty=True")

    if args.norm_stats_path:
        model.action_space.load_norm_stats(args.norm_stats_path)

    smolvlm_path = args.smolvlm_model_path or getattr(
        model.config,
        "smolvlm_model_path",
        "HuggingFaceTB/SmolVLM-500M-Instruct",
    )
    processor = SmolVLMVLAProcessor.from_pretrained(smolvlm_path)

    dataloader = create_smolvlm_dataloader(
        batch_size=args.batch_size,
        metas_path=args.metas_path,
        num_actions=model.num_actions,
        action_mode=model.action_mode,
        training=False,
        num_workers=args.num_workers,
        image_size=model.image_size,
    )

    sigma2_chunks = []
    residual2_chunks = []
    tau_chunks = []
    h_chunks = []
    d_chunks = []

    batches_seen = 0

    for batch in tqdm(dataloader, desc="Collecting flow calibration points"):
        if args.max_batches > 0 and batches_seen >= args.max_batches:
            break
        batches_seen += 1

        lang = processor.encode_language(batch["language_instruction"])
        batch.pop("language_instruction", None)

        inputs = {**batch, **lang}
        inputs = {
            k: v.to(device, non_blocking=True) if torch.is_tensor(v) else v
            for k, v in inputs.items()
        }

        for _ in range(args.num_time_samples):
            out = model.collect_flow_uncertainty_calibration_batch(**inputs)

            sigma2 = out["sigma2"]
            residual2 = out["residual2"]
            tau = out["tau"]

            B, H, D = sigma2.shape

            tau_full = tau.view(B, 1, 1).expand(B, H, D)
            h_full = torch.arange(H, device=device).view(1, H, 1).expand(B, H, D)
            d_full = torch.arange(D, device=device).view(1, 1, D).expand(B, H, D)

            sigma2_chunks.append(sigma2.reshape(-1).cpu())
            residual2_chunks.append(residual2.reshape(-1).cpu())
            tau_chunks.append(tau_full.reshape(-1).cpu())
            h_chunks.append(h_full.reshape(-1).cpu())
            d_chunks.append(d_full.reshape(-1).cpu())

    sigma2_all = torch.cat(sigma2_chunks).numpy()
    residual2_all = torch.cat(residual2_chunks).numpy()
    tau_all = torch.cat(tau_chunks).numpy()
    h_all = torch.cat(h_chunks).numpy()
    d_all = torch.cat(d_chunks).numpy()

    n = len(sigma2_all)
    if args.max_points > 0 and n > args.max_points:
        rng = np.random.default_rng(args.seed)
        idx = rng.choice(n, size=args.max_points, replace=False)
        sigma2_all = sigma2_all[idx]
        residual2_all = residual2_all[idx]
        tau_all = tau_all[idx]
        h_all = h_all[idx]
        d_all = d_all[idx]

    return {
        "sigma2": sigma2_all,
        "residual2": residual2_all,
        "tau": tau_all,
        "h": h_all,
        "d": d_all,
    }


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    arrays = collect_arrays(args)

    np.savez_compressed(output_dir / "flow_uncertainty_calibration_points.npz", **arrays)

    # Global reliability curve
    rows, metrics = make_reliability_curve(
        arrays["sigma2"],
        arrays["residual2"],
        n_bins=args.n_bins,
    )
    save_curve_csv(rows, output_dir / "global_reliability_curve.csv")
    save_curve_plot(
        rows,
        output_dir / "global_reliability_curve.png",
        title="Global reliability: predicted $\\sigma^2$ vs empirical flow MSE",
    )

    all_metrics = {"global": metrics}

    # Per tau-bin reliability curves
    tau_edges = np.linspace(0.0, 1.0, args.n_tau_bins + 1)
    tau_rows_summary = []

    for i in range(args.n_tau_bins):
        lo = tau_edges[i]
        hi = tau_edges[i + 1]
        if i == args.n_tau_bins - 1:
            mask = (arrays["tau"] >= lo) & (arrays["tau"] <= hi)
        else:
            mask = (arrays["tau"] >= lo) & (arrays["tau"] < hi)

        if int(mask.sum()) < max(args.n_bins * 5, 100):
            continue

        try:
            tau_rows, tau_metrics = make_reliability_curve(
                arrays["sigma2"][mask],
                arrays["residual2"][mask],
                n_bins=args.n_bins,
            )
        except ValueError:
            continue

        tag = f"tau_{lo:.2f}_{hi:.2f}".replace(".", "p")
        save_curve_csv(tau_rows, output_dir / f"{tag}_reliability_curve.csv")
        save_curve_plot(
            tau_rows,
            output_dir / f"{tag}_reliability_curve.png",
            title=f"Reliability for tau in [{lo:.2f}, {hi:.2f}]",
        )

        all_metrics[tag] = tau_metrics
        tau_rows_summary.append(
            {
                "tau_min": float(lo),
                "tau_max": float(hi),
                **tau_metrics,
            }
        )

    with (output_dir / "metrics.json").open("w", encoding="utf-8") as f:
        json.dump(all_metrics, f, indent=2, sort_keys=True)

    if tau_rows_summary:
        save_curve_csv(tau_rows_summary, output_dir / "tau_bin_metrics.csv")

    print(json.dumps(all_metrics, indent=2, sort_keys=True))
    print(f"\nSaved results to: {output_dir}")


if __name__ == "__main__":
    main()