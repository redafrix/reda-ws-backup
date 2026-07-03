#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


METRICS = [
    "mean_path_uncertainty",
    "max_path_uncertainty",
    "mean_last_step_uncertainty",
    "max_last_step_uncertainty",
]

TRACE_METRICS = [
    "path_step_mean",
    "last_step_mean",
    "mean_path_var",
    "mean_last_var",
    "max_path_var",
    "max_last_var",
]


def load_rows(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def metric_values(rows: list[dict], key: str) -> list[float]:
    return [float(r[key]) for r in rows if r.get(key) is not None]


def resample_trace(values: list[float], length: int = 100) -> np.ndarray:
    if not values:
        return np.full(length, np.nan)
    if len(values) == 1:
        return np.full(length, values[0], dtype=float)
    x_old = np.linspace(0.0, 1.0, len(values))
    x_new = np.linspace(0.0, 1.0, length)
    return np.interp(x_new, x_old, values)


def extract_episode_trace(row: dict, key: str) -> list[float]:
    return [step[key] for step in row.get("uncertainty_trace", []) if step.get(key) is not None]


def outcome_split(rows: list[dict]) -> tuple[list[dict], list[dict]]:
    succ = [r for r in rows if r["success"]]
    fail = [r for r in rows if not r["success"]]
    return succ, fail


def safe_mean(values: list[float]) -> float:
    return float(np.mean(values)) if values else float("nan")


def roc_auc_from_scores(rows: list[dict], metric: str) -> float:
    scored = [(float(r[metric]), 1 if not r["success"] else 0) for r in rows if r.get(metric) is not None]
    if not scored:
        return float("nan")
    pos = sum(label for _, label in scored)
    neg = len(scored) - pos
    if pos == 0 or neg == 0:
        return float("nan")
    scored.sort(key=lambda x: x[0])
    rank_sum = 0.0
    i = 0
    rank = 1
    while i < len(scored):
        j = i
        while j < len(scored) and scored[j][0] == scored[i][0]:
            j += 1
        avg_rank = (rank + (rank + (j - i) - 1)) / 2.0
        positives = sum(label for _, label in scored[i:j])
        rank_sum += positives * avg_rank
        rank += j - i
        i = j
    return (rank_sum - pos * (pos + 1) / 2.0) / (pos * neg)


def save_success_rate_by_task(rows: list[dict], outdir: Path) -> None:
    task_ids = sorted({r["task_id"] for r in rows})
    rates = []
    labels = []
    counts = []
    for tid in task_ids:
        rs = [r for r in rows if r["task_id"] == tid]
        rate = sum(bool(r["success"]) for r in rs) / len(rs)
        rates.append(rate * 100.0)
        labels.append(str(tid))
        counts.append(len(rs))

    fig, ax = plt.subplots(figsize=(10, 4.5))
    bars = ax.bar(labels, rates, color="#4C78A8")
    ax.set_title("Success Rate by Task")
    ax.set_xlabel("Task ID")
    ax.set_ylabel("Success Rate (%)")
    ax.set_ylim(0, 100)
    for bar, rate, count in zip(bars, rates, counts):
        ax.text(bar.get_x() + bar.get_width() / 2, rate + 1, f"{rate:.0f}%\n(n={count})",
                ha="center", va="bottom", fontsize=8)
    fig.tight_layout()
    fig.savefig(outdir / "success_rate_by_task.png", dpi=180)
    plt.close(fig)


def save_metric_boxplots(rows: list[dict], outdir: Path) -> None:
    succ, fail = outcome_split(rows)

    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    axes = axes.ravel()
    for ax, metric in zip(axes, METRICS):
        data = [metric_values(succ, metric), metric_values(fail, metric)]
        ax.boxplot(data, labels=["Success", "Failure"], showfliers=True)
        ax.set_title(metric.replace("_", " "))
        ax.grid(alpha=0.2)
    fig.suptitle("Episode-Level Uncertainty by Outcome", y=1.02)
    fig.tight_layout()
    fig.savefig(outdir / "uncertainty_boxplots_by_outcome.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def save_metric_scatter(rows: list[dict], outdir: Path) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    axes = axes.ravel()
    colors = ["#D62728" if not r["success"] else "#2CA02C" for r in rows]
    x = np.arange(len(rows))
    for ax, metric in zip(axes, METRICS):
        y = [r.get(metric, np.nan) for r in rows]
        ax.scatter(x, y, c=colors, alpha=0.8, s=22)
        ax.set_title(metric.replace("_", " "))
        ax.set_xlabel("Episode")
        ax.grid(alpha=0.2)
    fig.suptitle("Episode-Level Uncertainty Scatter", y=1.02)
    fig.tight_layout()
    fig.savefig(outdir / "uncertainty_scatter_by_episode.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def save_metric_histograms(rows: list[dict], outdir: Path) -> None:
    succ, fail = outcome_split(rows)
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    axes = axes.ravel()
    for ax, metric in zip(axes, METRICS):
        succ_vals = metric_values(succ, metric)
        fail_vals = metric_values(fail, metric)
        bins = 20
        ax.hist(succ_vals, bins=bins, alpha=0.6, color="#2CA02C", density=True, label="Success")
        ax.hist(fail_vals, bins=bins, alpha=0.6, color="#D62728", density=True, label="Failure")
        ax.set_title(metric.replace("_", " "))
        ax.grid(alpha=0.2)
    axes[0].legend()
    fig.suptitle("Outcome Distributions of Episode-Level Uncertainty", y=1.02)
    fig.tight_layout()
    fig.savefig(outdir / "uncertainty_histograms_by_outcome.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def save_trajectory_overlay(rows: list[dict], outdir: Path, trace_key: str, filename: str, title: str) -> None:
    succ, fail = outcome_split(rows)

    fig, ax = plt.subplots(figsize=(10, 5))
    succ_traces = []
    fail_traces = []

    for row in succ:
        vals = extract_episode_trace(row, trace_key)
        if vals:
            arr = resample_trace(vals, 100)
            succ_traces.append(arr)
            ax.plot(arr, color="#2CA02C", alpha=0.18, linewidth=1)

    for row in fail:
        vals = extract_episode_trace(row, trace_key)
        if vals:
            arr = resample_trace(vals, 100)
            fail_traces.append(arr)
            ax.plot(arr, color="#D62728", alpha=0.12, linewidth=1)

    if succ_traces:
        succ_stack = np.stack(succ_traces)
        succ_mean = np.nanmean(succ_stack, axis=0)
        succ_std = np.nanstd(succ_stack, axis=0)
        ax.plot(succ_mean, color="#1B7F1B", linewidth=2.5, label="Success mean")
        ax.fill_between(np.arange(len(succ_mean)), succ_mean - succ_std, succ_mean + succ_std, color="#2CA02C", alpha=0.18)
    if fail_traces:
        fail_stack = np.stack(fail_traces)
        fail_mean = np.nanmean(fail_stack, axis=0)
        fail_std = np.nanstd(fail_stack, axis=0)
        ax.plot(fail_mean, color="#B22222", linewidth=2.5, label="Failure mean")
        ax.fill_between(np.arange(len(fail_mean)), fail_mean - fail_std, fail_mean + fail_std, color="#D62728", alpha=0.16)

    ax.set_title(title)
    ax.set_xlabel("Normalized rollout progress")
    ax.set_ylabel("Uncertainty")
    ax.legend()
    ax.grid(alpha=0.2)
    fig.tight_layout()
    fig.savefig(outdir / filename, dpi=180)
    plt.close(fig)


def save_task_outcome_bars(rows: list[dict], outdir: Path) -> None:
    task_ids = sorted({r["task_id"] for r in rows})
    succ_rates = []
    fail_rates = []
    for tid in task_ids:
        rs = [r for r in rows if r["task_id"] == tid]
        succ = sum(bool(r["success"]) for r in rs)
        fail = len(rs) - succ
        succ_rates.append(100.0 * succ / len(rs))
        fail_rates.append(100.0 * fail / len(rs))

    x = np.arange(len(task_ids))
    fig, ax = plt.subplots(figsize=(10, 4.8))
    ax.bar(x, succ_rates, color="#2CA02C", label="Success")
    ax.bar(x, fail_rates, bottom=succ_rates, color="#D62728", label="Failure")
    ax.set_xticks(x, labels=[str(t) for t in task_ids])
    ax.set_ylim(0, 100)
    ax.set_xlabel("Task ID")
    ax.set_ylabel("Episode share (%)")
    ax.set_title("Outcome Composition by Task")
    ax.legend()
    ax.grid(axis="y", alpha=0.2)
    fig.tight_layout()
    fig.savefig(outdir / "outcome_composition_by_task.png", dpi=180)
    plt.close(fig)


def save_task_metric_strip(rows: list[dict], outdir: Path, metric: str) -> None:
    task_ids = sorted({r["task_id"] for r in rows})
    fig, ax = plt.subplots(figsize=(11, 5))
    for i, tid in enumerate(task_ids):
        rs = [r for r in rows if r["task_id"] == tid and r.get(metric) is not None]
        succ = [float(r[metric]) for r in rs if r["success"]]
        fail = [float(r[metric]) for r in rs if not r["success"]]
        if succ:
            xs = np.full(len(succ), i - 0.12)
            ax.scatter(xs, succ, color="#2CA02C", alpha=0.8, s=24)
        if fail:
            xs = np.full(len(fail), i + 0.12)
            ax.scatter(xs, fail, color="#D62728", alpha=0.8, s=24)
    ax.set_xticks(np.arange(len(task_ids)), labels=[str(t) for t in task_ids])
    ax.set_xlabel("Task ID")
    ax.set_ylabel(metric.replace("_", " "))
    ax.set_title(f"Per-Task {metric.replace('_', ' ')} by Outcome")
    ax.grid(alpha=0.2)
    fig.tight_layout()
    fig.savefig(outdir / f"strip_{metric}.png", dpi=180)
    plt.close(fig)


def save_task_heatmap(rows: list[dict], outdir: Path, metric: str) -> None:
    task_ids = sorted({r["task_id"] for r in rows})
    mat = np.full((len(task_ids), 2), np.nan)
    for i, tid in enumerate(task_ids):
        rs = [r for r in rows if r["task_id"] == tid]
        succ = [r[metric] for r in rs if r["success"] and r.get(metric) is not None]
        fail = [r[metric] for r in rs if (not r["success"]) and r.get(metric) is not None]
        if succ:
            mat[i, 0] = float(np.mean(succ))
        if fail:
            mat[i, 1] = float(np.mean(fail))

    fig, ax = plt.subplots(figsize=(6, max(4, 0.5 * len(task_ids))))
    im = ax.imshow(mat, aspect="auto", cmap="viridis")
    ax.set_xticks([0, 1], labels=["Success", "Failure"])
    ax.set_yticks(np.arange(len(task_ids)), labels=[str(t) for t in task_ids])
    ax.set_xlabel("Outcome")
    ax.set_ylabel("Task ID")
    ax.set_title(f"Task-Level Mean {metric.replace('_', ' ')}")
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if not np.isnan(mat[i, j]):
                ax.text(j, i, f"{mat[i, j]:.3f}", ha="center", va="center", color="white", fontsize=8)
    fig.colorbar(im, ax=ax, shrink=0.85)
    fig.tight_layout()
    fig.savefig(outdir / f"heatmap_{metric}.png", dpi=180)
    plt.close(fig)


def save_trace_metric_heatmap(rows: list[dict], outdir: Path, trace_key: str) -> None:
    task_ids = sorted({r["task_id"] for r in rows})
    mat = np.full((len(task_ids), 2), np.nan)
    for i, tid in enumerate(task_ids):
        rs = [r for r in rows if r["task_id"] == tid]
        succ_vals = []
        fail_vals = []
        for r in rs:
            vals = extract_episode_trace(r, trace_key)
            if not vals:
                continue
            if r["success"]:
                succ_vals.append(float(np.mean(vals)))
            else:
                fail_vals.append(float(np.mean(vals)))
        if succ_vals:
            mat[i, 0] = float(np.mean(succ_vals))
        if fail_vals:
            mat[i, 1] = float(np.mean(fail_vals))

    fig, ax = plt.subplots(figsize=(6, max(4, 0.5 * len(task_ids))))
    im = ax.imshow(mat, aspect="auto", cmap="magma")
    ax.set_xticks([0, 1], labels=["Success", "Failure"])
    ax.set_yticks(np.arange(len(task_ids)), labels=[str(t) for t in task_ids])
    ax.set_xlabel("Outcome")
    ax.set_ylabel("Task ID")
    ax.set_title(f"Task-Level Mean {trace_key}")
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if not np.isnan(mat[i, j]):
                ax.text(j, i, f"{mat[i, j]:.3f}", ha="center", va="center", color="white", fontsize=8)
    fig.colorbar(im, ax=ax, shrink=0.85)
    fig.tight_layout()
    fig.savefig(outdir / f"heatmap_{trace_key}.png", dpi=180)
    plt.close(fig)


def save_steps_vs_uncertainty(rows: list[dict], outdir: Path) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8))
    colors = ["#2CA02C" if r["success"] else "#D62728" for r in rows]
    steps = [r.get("steps", np.nan) for r in rows]
    y1 = [r.get("mean_path_uncertainty", np.nan) for r in rows]
    y2 = [r.get("mean_last_step_uncertainty", np.nan) for r in rows]
    axes[0].scatter(steps, y1, c=colors, alpha=0.8, s=26)
    axes[0].set_title("Episode Length vs Mean Path Uncertainty")
    axes[0].set_xlabel("Episode steps")
    axes[0].set_ylabel("Mean path uncertainty")
    axes[0].grid(alpha=0.2)
    axes[1].scatter(steps, y2, c=colors, alpha=0.8, s=26)
    axes[1].set_title("Episode Length vs Mean Last-Step Uncertainty")
    axes[1].set_xlabel("Episode steps")
    axes[1].set_ylabel("Mean last-step uncertainty")
    axes[1].grid(alpha=0.2)
    fig.tight_layout()
    fig.savefig(outdir / "steps_vs_uncertainty.png", dpi=180)
    plt.close(fig)


def save_roc_bar(rows: list[dict], outdir: Path) -> None:
    aucs = [roc_auc_from_scores(rows, metric) for metric in METRICS]
    fig, ax = plt.subplots(figsize=(8.5, 4.5))
    bars = ax.bar(range(len(METRICS)), aucs, color="#4C78A8")
    ax.axhline(0.5, color="black", linestyle="--", linewidth=1, alpha=0.6)
    ax.set_xticks(range(len(METRICS)), labels=[m.replace("_uncertainty", "").replace("_", "\n") for m in METRICS])
    ax.set_ylabel("AUROC for Failure Detection")
    ax.set_ylim(0, 1)
    ax.set_title("How Predictive Each Uncertainty Metric Is of Failure")
    for bar, auc in zip(bars, aucs):
        if not np.isnan(auc):
            ax.text(bar.get_x() + bar.get_width() / 2, auc + 0.02, f"{auc:.3f}", ha="center", va="bottom", fontsize=9)
    fig.tight_layout()
    fig.savefig(outdir / "failure_detection_auroc.png", dpi=180)
    plt.close(fig)


def save_summary(rows: list[dict], outdir: Path) -> None:
    task_ids = sorted({r["task_id"] for r in rows})
    succ, fail = outcome_split(rows)

    lines = []
    lines.append("# Uncertainty Analysis Summary")
    lines.append("")
    lines.append(f"- Episodes: `{len(rows)}`")
    lines.append(f"- Successes: `{len(succ)}`")
    lines.append(f"- Failures: `{len(fail)}`")
    lines.append(f"- Tasks present: `{task_ids}`")
    lines.append("")
    lines.append("## Outcome Means")
    lines.append("")
    for metric in METRICS:
        succ_vals = metric_values(succ, metric)
        fail_vals = metric_values(fail, metric)
        succ_mean = safe_mean(succ_vals)
        fail_mean = safe_mean(fail_vals)
        auc = roc_auc_from_scores(rows, metric)
        lines.append(
            f"- `{metric}`: success=`{succ_mean:.6f}` failure=`{fail_mean:.6f}` "
            f"delta(fail-success)=`{(fail_mean - succ_mean):.6f}` auroc=`{auc:.3f}`"
        )
    lines.append("")
    lines.append("## Trace-Level Means")
    lines.append("")
    for metric in TRACE_METRICS:
        succ_trace_means = []
        fail_trace_means = []
        for row in succ:
            vals = extract_episode_trace(row, metric)
            if vals:
                succ_trace_means.append(float(np.mean(vals)))
        for row in fail:
            vals = extract_episode_trace(row, metric)
            if vals:
                fail_trace_means.append(float(np.mean(vals)))
        lines.append(
            f"- `{metric}`: success=`{safe_mean(succ_trace_means):.6f}` "
            f"failure=`{safe_mean(fail_trace_means):.6f}`"
        )
    lines.append("")
    lines.append("## Task Success Rates")
    lines.append("")
    for tid in task_ids:
        rs = [r for r in rows if r["task_id"] == tid]
        rate = 100.0 * sum(bool(r["success"]) for r in rs) / len(rs)
        lines.append(f"- Task `{tid}`: `{sum(bool(r['success']) for r in rs)}/{len(rs)}` = `{rate:.1f}%`")
    (outdir / "summary.md").write_text("\n".join(lines))


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze LIBERO uncertainty JSONL logs")
    parser.add_argument("--log", required=True, help="Path to JSONL uncertainty log")
    parser.add_argument("--outdir", default=None, help="Output directory for figures")
    args = parser.parse_args()

    log_path = Path(args.log)
    outdir = Path(args.outdir) if args.outdir else log_path.with_suffix("")
    outdir.mkdir(parents=True, exist_ok=True)

    rows = load_rows(log_path)
    if not rows:
        raise SystemExit("No rows found in log.")

    save_success_rate_by_task(rows, outdir)
    save_task_outcome_bars(rows, outdir)
    save_metric_boxplots(rows, outdir)
    save_metric_histograms(rows, outdir)
    save_metric_scatter(rows, outdir)
    save_steps_vs_uncertainty(rows, outdir)
    save_roc_bar(rows, outdir)
    save_trajectory_overlay(
        rows,
        outdir,
        trace_key="path_step_mean",
        filename="trajectory_overlay_path_step_mean.png",
        title="Trajectory Overlay: Path-Step Mean Uncertainty",
    )
    save_trajectory_overlay(
        rows,
        outdir,
        trace_key="last_step_mean",
        filename="trajectory_overlay_last_step_mean.png",
        title="Trajectory Overlay: Last-Step Mean Uncertainty",
    )
    save_trajectory_overlay(
        rows,
        outdir,
        trace_key="mean_path_var",
        filename="trajectory_overlay_mean_path_var.png",
        title="Trajectory Overlay: Mean Path Variance",
    )
    save_trajectory_overlay(
        rows,
        outdir,
        trace_key="mean_last_var",
        filename="trajectory_overlay_mean_last_var.png",
        title="Trajectory Overlay: Mean Last-Step Variance",
    )
    save_task_heatmap(rows, outdir, "mean_path_uncertainty")
    save_task_heatmap(rows, outdir, "max_path_uncertainty")
    save_task_heatmap(rows, outdir, "mean_last_step_uncertainty")
    save_task_heatmap(rows, outdir, "max_last_step_uncertainty")
    save_trace_metric_heatmap(rows, outdir, "path_step_mean")
    save_trace_metric_heatmap(rows, outdir, "last_step_mean")
    save_task_metric_strip(rows, outdir, "mean_path_uncertainty")
    save_task_metric_strip(rows, outdir, "mean_last_step_uncertainty")
    save_summary(rows, outdir)


if __name__ == "__main__":
    main()
