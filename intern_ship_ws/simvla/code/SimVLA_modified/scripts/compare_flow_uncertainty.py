from __future__ import annotations

import argparse
import csv
import json
import math
import random
import sys
from pathlib import Path
from typing import Any

import numpy as np
import torch

REPO_ROOT = Path(__file__).resolve().parents[1]
repo_root_str = str(REPO_ROOT)
if repo_root_str in sys.path:
    sys.path.remove(repo_root_str)
sys.path.insert(0, repo_root_str)

from datasets import create_smolvlm_dataloader
from models.modeling_smolvlm_vla import SmolVLMVLA
from models.processing_smolvlm_vla import SmolVLMVLAProcessor


def rankdata(values: np.ndarray) -> np.ndarray:
    values = np.asarray(values, dtype=np.float64)
    order = np.argsort(values, kind="mergesort")
    ranks = np.empty(len(values), dtype=np.float64)
    sorted_values = values[order]
    start = 0
    while start < len(values):
        end = start + 1
        while end < len(values) and sorted_values[end] == sorted_values[start]:
            end += 1
        ranks[order[start:end]] = 0.5 * (start + 1 + end)
        start = end
    return ranks


def pearson(x: np.ndarray, y: np.ndarray) -> float:
    x = np.asarray(x, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    if len(x) < 2:
        return float("nan")
    x = x - x.mean()
    y = y - y.mean()
    denom = math.sqrt(float((x * x).sum() * (y * y).sum()))
    if denom <= 0.0:
        return float("nan")
    return float((x * y).sum() / denom)


def spearman(x: np.ndarray, y: np.ndarray) -> float:
    return pearson(rankdata(x), rankdata(y))


def binary_auroc(scores: np.ndarray, labels: np.ndarray) -> float:
    scores = np.asarray(scores, dtype=np.float64)
    labels = np.asarray(labels, dtype=np.int64)
    pos = labels == 1
    neg = labels == 0
    n_pos = int(pos.sum())
    n_neg = int(neg.sum())
    if n_pos == 0 or n_neg == 0:
        return float("nan")
    ranks = rankdata(scores)
    sum_pos = float(ranks[pos].sum())
    return float((sum_pos - n_pos * (n_pos + 1) / 2.0) / (n_pos * n_neg))


def safe_mean(values: np.ndarray) -> float:
    return float(np.asarray(values, dtype=np.float64).mean()) if len(values) else float("nan")


def calibration_bins(unc: np.ndarray, err: np.ndarray, num_bins: int) -> list[dict[str, float]]:
    order = np.argsort(unc)
    bins: list[dict[str, float]] = []
    for idxs in np.array_split(order, num_bins):
        if len(idxs) == 0:
            continue
        u = unc[idxs]
        e = err[idxs]
        bins.append(
            {
                "count": int(len(idxs)),
                "uncertainty_mean": safe_mean(u),
                "residual2_mean": safe_mean(e),
                "abs_gap": float(abs(safe_mean(u) - safe_mean(e))),
                "ratio_residual_to_uncertainty": float(safe_mean(e) / max(safe_mean(u), 1e-12)),
            }
        )
    return bins


def summarize(records: list[dict[str, float]], num_bins: int) -> dict[str, Any]:
    sample_records = [r for r in records if r["record_type"] == "sample"]
    element_records = [r for r in records if r["record_type"] == "element"]
    sample_unc = np.asarray([r["sample_uncertainty_mean"] for r in sample_records], dtype=np.float64)
    sample_err = np.asarray([r["sample_residual2_mean"] for r in sample_records], dtype=np.float64)
    elem_unc = np.asarray([r["element_uncertainty"] for r in records], dtype=np.float64)
    elem_err = np.asarray([r["element_residual2"] for r in records], dtype=np.float64)

    q90 = float(np.quantile(sample_err, 0.9))
    q95 = float(np.quantile(sample_err, 0.95))
    top10 = (sample_err >= q90).astype(np.int64)
    top5 = (sample_err >= q95).astype(np.int64)

    nll_elem = 0.5 * (elem_err / np.maximum(elem_unc, 1e-12) + np.log(np.maximum(elem_unc, 1e-12)))
    nll_sample = np.asarray([r["sample_nll"] for r in sample_records], dtype=np.float64)

    bins = calibration_bins(sample_unc, sample_err, num_bins=num_bins)
    weighted_abs_gap = sum(b["count"] * b["abs_gap"] for b in bins) / max(len(sample_unc), 1)

    return {
        "num_samples": int(len(sample_unc)),
        "num_elements": int(len(element_records)),
        "sample_uncertainty_mean": safe_mean(sample_unc),
        "sample_uncertainty_std": float(sample_unc.std()) if len(sample_unc) else float("nan"),
        "sample_residual2_mean": safe_mean(sample_err),
        "sample_residual2_std": float(sample_err.std()) if len(sample_err) else float("nan"),
        "sample_pearson_unc_vs_error": pearson(sample_unc, sample_err),
        "sample_spearman_unc_vs_error": spearman(sample_unc, sample_err),
        "sample_auroc_top10_error": binary_auroc(sample_unc, top10),
        "sample_auroc_top5_error": binary_auroc(sample_unc, top5),
        "element_pearson_unc_vs_error": pearson(elem_unc, elem_err),
        "element_spearman_unc_vs_error": spearman(elem_unc, elem_err),
        "constantless_gaussian_nll_element_mean": safe_mean(nll_elem),
        "constantless_gaussian_nll_sample_mean": safe_mean(nll_sample),
        "calibration_weighted_abs_gap": float(weighted_abs_gap),
        "calibration_bins": bins,
    }


def collect_checkpoint(
    *,
    name: str,
    checkpoint: Path,
    norm_stats: Path,
    dataloader,
    processor: SmolVLMVLAProcessor,
    device: torch.device,
    max_batches: int,
) -> tuple[dict[str, Any], list[dict[str, float]]]:
    model = SmolVLMVLA.from_pretrained(str(checkpoint)).to(device)
    model.eval()
    model.requires_grad_(False)
    model.action_space.load_norm_stats(str(norm_stats))
    model.action_space.to(device)

    records: list[dict[str, float]] = []
    with torch.no_grad():
        for batch_idx, batch in enumerate(dataloader):
            if batch_idx >= max_batches:
                break
            lang = processor.encode_language(batch["language_instruction"])
            input_ids = lang["input_ids"].to(device)
            image_input = batch["image_input"].to(device, non_blocking=True)
            image_mask = batch["image_mask"].to(device, non_blocking=True)
            proprio = batch["proprio"].to(device, non_blocking=True)
            action = batch["action"].to(device, non_blocking=True)

            out = model.collect_flow_uncertainty_calibration_batch(
                input_ids=input_ids,
                image_input=image_input,
                image_mask=image_mask,
                proprio=proprio,
                action=action,
            )
            sigma2 = out["sigma2"].float().cpu().numpy()
            residual2 = out["residual2"].float().cpu().numpy()
            log_sigma2 = out["log_sigma2"].float().cpu().numpy()
            tau = out["tau"].float().cpu().numpy()

            batch_size = sigma2.shape[0]
            for b in range(batch_size):
                s = sigma2[b]
                e = residual2[b]
                nll = 0.5 * (e / np.maximum(s, 1e-12) + log_sigma2[b])
                base = {
                    "checkpoint": name,
                    "record_type": "sample",
                    "batch_idx": float(batch_idx),
                    "sample_idx": float(batch_idx * batch_size + b),
                    "tau": float(tau[b]),
                    "sample_uncertainty_mean": float(s.mean()),
                    "sample_uncertainty_max": float(s.max()),
                    "sample_residual2_mean": float(e.mean()),
                    "sample_residual2_max": float(e.max()),
                    "sample_nll": float(nll.mean()),
                    "element_uncertainty": float(s.mean()),
                    "element_residual2": float(e.mean()),
                }
                records.append(base)

                # Add a light element-level subsample for element correlation without
                # writing every H*D point to disk.
                flat_s = s.reshape(-1)
                flat_e = e.reshape(-1)
                stride = max(1, len(flat_s) // 8)
                for j in range(0, len(flat_s), stride):
                    records.append(
                        {
                            "checkpoint": name,
                            "record_type": "element",
                            "batch_idx": float(batch_idx),
                            "sample_idx": float(batch_idx * batch_size + b),
                            "tau": float(tau[b]),
                            "sample_uncertainty_mean": float(s.mean()),
                            "sample_uncertainty_max": float(s.max()),
                            "sample_residual2_mean": float(e.mean()),
                            "sample_residual2_max": float(e.max()),
                            "sample_nll": float(nll.mean()),
                            "element_uncertainty": float(flat_s[j]),
                            "element_residual2": float(flat_e[j]),
                        }
                    )

    summary = summarize(records, num_bins=10)
    summary["checkpoint"] = name
    summary["checkpoint_path"] = str(checkpoint)
    return summary, records


def write_markdown(path: Path, summaries: list[dict[str, Any]], args: argparse.Namespace) -> None:
    lines = [
        "# Flow-Uncertainty Calibration Comparison",
        "",
        "This evaluates whether the learned variance head ranks actual flow-matching error correctly on LIBERO demo batches.",
        "",
        "## Setup",
        "",
        f"- metadata: `{args.metas_path}`",
        f"- norm stats: `{args.norm_stats}`",
        f"- max batches: `{args.max_batches}`",
        f"- batch size: `{args.batch_size}`",
        f"- device: `{args.device}`",
        "",
        "## Summary",
        "",
        "| Checkpoint | Samples | Mean residual2 | Mean uncertainty | Spearman | Pearson | AUROC top10 error | AUROC top5 error | NLL | Calib abs gap |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for s in summaries:
        lines.append(
            "| {checkpoint} | {num_samples} | {sample_residual2_mean:.6f} | "
            "{sample_uncertainty_mean:.6f} | {sample_spearman_unc_vs_error:.4f} | "
            "{sample_pearson_unc_vs_error:.4f} | {sample_auroc_top10_error:.4f} | "
            "{sample_auroc_top5_error:.4f} | {constantless_gaussian_nll_sample_mean:.6f} | "
            "{calibration_weighted_abs_gap:.6f} |".format(**s)
        )
    lines.extend(["", "## Calibration Bins", ""])
    for s in summaries:
        lines.append(f"### {s['checkpoint']}")
        lines.append("")
        lines.append("| Bin | Count | Pred var mean | Residual2 mean | Residual / Pred | Abs gap |")
        lines.append("|---:|---:|---:|---:|---:|---:|")
        for i, b in enumerate(s["calibration_bins"]):
            lines.append(
                f"| {i} | {b['count']} | {b['uncertainty_mean']:.6f} | "
                f"{b['residual2_mean']:.6f} | {b['ratio_residual_to_uncertainty']:.4f} | "
                f"{b['abs_gap']:.6f} |"
            )
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ckpt60", type=Path, required=True)
    parser.add_argument("--ckpt80", type=Path, required=True)
    parser.add_argument("--metas_path", type=Path, required=True)
    parser.add_argument("--norm_stats", type=Path, required=True)
    parser.add_argument("--output_dir", type=Path, required=True)
    parser.add_argument("--batch_size", type=int, default=8)
    parser.add_argument("--max_batches", type=int, default=64)
    parser.add_argument("--num_workers", type=int, default=0)
    parser.add_argument("--device", type=str, default="cuda")
    parser.add_argument("--seed", type=int, default=123)
    args = parser.parse_args()

    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(args.seed)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    device = torch.device(args.device)
    processor = SmolVLMVLAProcessor.from_pretrained("HuggingFaceTB/SmolVLM-500M-Instruct")

    summaries: list[dict[str, Any]] = []
    all_records: list[dict[str, float]] = []
    for name, ckpt in [("ckpt-60000", args.ckpt60), ("ckpt-80000", args.ckpt80)]:
        dataloader = create_smolvlm_dataloader(
            metas_path=str(args.metas_path),
            batch_size=args.batch_size,
            num_actions=10,
            training=False,
            action_mode="libero_joint",
            num_workers=args.num_workers,
            image_size=384,
        )
        summary, records = collect_checkpoint(
            name=name,
            checkpoint=ckpt,
            norm_stats=args.norm_stats,
            dataloader=dataloader,
            processor=processor,
            device=device,
            max_batches=args.max_batches,
        )
        summaries.append(summary)
        all_records.extend(records)
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

    with (args.output_dir / "summary.json").open("w", encoding="utf-8") as f:
        json.dump(summaries, f, indent=2)
    with (args.output_dir / "records.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(all_records[0].keys()))
        writer.writeheader()
        writer.writerows(all_records)
    write_markdown(args.output_dir / "flow_uncertainty_comparison.md", summaries, args)
    print(json.dumps(summaries, indent=2))


if __name__ == "__main__":
    main()
