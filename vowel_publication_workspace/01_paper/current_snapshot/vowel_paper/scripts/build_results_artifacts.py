#!/usr/bin/env python3
"""Rebuild paper Results figures and the compact derived-metrics record."""

from __future__ import annotations

import csv
import io
import json
import re
import subprocess
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


SCRIPT = Path(__file__).resolve()
PAPER = SCRIPT.parent.parent
REPO = Path(
    subprocess.check_output(
        ["git", "rev-parse", "--show-toplevel"], cwd=PAPER, text=True
    ).strip()
)
FIGURES = PAPER / "figures"
DATA = PAPER / "results_data"
FIGURES.mkdir(exist_ok=True)
DATA.mkdir(exist_ok=True)

PACKAGE = (
    REPO
    / "vowel_publication_workspace/90_source_snapshots/"
    "20260814_libero_router_tests_package/"
    "libero_router_tests_package_20260814"
)
REPORT = PACKAGE / "reports/goal_object_ood_k1_seed0_report"
BOB_REF = "catalog/bob-20260703"
PROMOTED_PATH = (
    "machine_snapshot/bob/media/rootalkhatib/My Passport/reda_ws/fiper_ws/"
    "cross_suite_official_ood_20260630/experiments/"
    "eval_promoted_single_model_all_ood_20260701/results.json"
)
FIPER_PATH = (
    "machine_snapshot/bob/media/rootalkhatib/My Passport/reda_ws/fiper_ws/"
    "official_fiper_original_bob_20260701/"
    "official_fiper_seen_thresholds_cross_suite_ood_20260702/"
    "official_fiper_seen_thresholds_cross_suite_ood_aggregate.csv"
)

COLORS = {
    "wm": "#0077BB",
    "vla": "#33BBEE",
    "fresh": "#EE7733",
    "latch": "#009988",
    "fiper_entropy": "#7A7A7A",
    "fiper_rnd": "#CC3311",
    "fiper_fusion": "#EE3377",
}


def git_text(path: str) -> str:
    return subprocess.check_output(
        ["git", "show", f"{BOB_REF}:{path}"], cwd=REPO, text=True
    )


def load_manifest(name: str) -> dict:
    return json.loads((REPORT / name).read_text())


def iter_rows(paths: list[str]):
    for rel in paths:
        with (PACKAGE / rel).open() as handle:
            for line in handle:
                if line.strip():
                    yield json.loads(line)


def episode_identity(row: dict) -> tuple[str, int, int, int]:
    initial_state = row.get("initial_state_index", row.get("trial_index"))
    if initial_state is None:
        match = re.search(r"init(?::|_)?0*(\d+)", str(row.get("episode_uid", "")))
        if match is None:
            raise RuntimeError(f"Cannot recover initial-state identity from row: {row}")
        initial_state = match.group(1)
    return (
        str(row["task_suite_name"]),
        int(row["task_id"]),
        int(initial_state),
        int(row.get("eval_seed", 0) or 0),
    )


def validate_manifest(manifest: dict) -> None:
    identity_sets = {}
    for key, entry in manifest.items():
        rows = list(iter_rows(entry["paths"]))
        summary = entry["summary"]
        successes = sum(bool(row["success"]) for row in rows)
        if len(rows) != summary["count"] or successes != summary["successes"]:
            raise RuntimeError(f"Manifest mismatch for {key}")
        identities = {episode_identity(row) for row in rows}
        if len(identities) != len(rows):
            raise RuntimeError(f"Duplicate episode identity for {key}")
        identity_sets[key] = identities

    reference = identity_sets["base_simvla"]
    for key in ("base_wm", "fresh", "latch"):
        if identity_sets[key] != reference:
            raise RuntimeError(f"Identity-set mismatch for {key}")


def suite_success(manifest: dict, key: str) -> dict[str, float]:
    grouped = defaultdict(list)
    for row in iter_rows(manifest[key]["paths"]):
        grouped[row["task_suite_name"]].append(bool(row["success"]))
    return {suite: 100.0 * sum(values) / len(values) for suite, values in grouped.items()}


def pooled_vla_metrics(promoted: dict) -> list[dict]:
    output = []
    thresholds = [
        "best_val_f1",
        "fixed_0.5",
        "q90_success",
        "q95_success",
        "q99_success",
    ]
    for threshold in thresholds:
        success_count = failure_count = false_alarms = detections = 0
        for dataset in promoted["datasets"].values():
            episode = dataset["metrics"][threshold]["episode"]
            success_count += dataset["success_episodes"]
            failure_count += dataset["failure_episodes"]
            false_alarms += episode["false_alarm_count"]
            detections += episode["detected_failure_count"]
        output.append(
            {
                "family": "Ours",
                "rule": threshold,
                "success_false_alarm": false_alarms / success_count,
                "failure_detection": detections / failure_count,
                "success_count": success_count,
                "failure_count": failure_count,
            }
        )
    return output


def pooled_fiper_metrics(promoted: dict, rows: list[dict]) -> list[dict]:
    counts = {
        name: (dataset["success_episodes"], dataset["failure_episodes"])
        for name, dataset in promoted["datasets"].items()
    }
    output = []
    methods = ("entropy", "rnd_oe", "rnd_oe_and_entropy")
    styles = ("ct_quantile", "tvt_quantile", "tvt_cp_band")
    for method in methods:
        for style in styles:
            selected = [
                row
                for row in rows
                if row["method"] == method and row["threshold_style"] == style
            ]
            success_count = sum(counts[row["dataset"]][0] for row in selected)
            failure_count = sum(counts[row["dataset"]][1] for row in selected)
            false_alarms = sum(
                float(row["success_false_alarm"]) * counts[row["dataset"]][0]
                for row in selected
            )
            detections = sum(
                float(row["failure_detection"]) * counts[row["dataset"]][1]
                for row in selected
            )
            output.append(
                {
                    "family": method,
                    "rule": style,
                    "success_false_alarm": false_alarms / success_count,
                    "failure_detection": detections / failure_count,
                    "success_count": success_count,
                    "failure_count": failure_count,
                }
            )
    return output


def configure_plotting() -> None:
    plt.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["DejaVu Sans"],
            "font.size": 8,
            "axes.labelsize": 8,
            "xtick.labelsize": 7,
            "ytick.labelsize": 7,
            "legend.fontsize": 7,
            "figure.dpi": 180,
            "savefig.dpi": 300,
            "savefig.bbox": "tight",
            "axes.spines.top": False,
            "axes.spines.right": False,
        }
    )


def save(fig, stem: str) -> None:
    fig.savefig(FIGURES / f"{stem}.pdf")
    fig.savefig(FIGURES / f"{stem}.png")
    plt.close(fig)


def plot_suite_success(official: dict) -> None:
    order = ["libero_goal_lan", "libero_goal_object", "libero_goal_swap", "libero_goal_task"]
    labels = ["Language", "Object", "Swap", "Task"]
    policies = [
        ("base_wm", "World model", COLORS["wm"]),
        ("base_simvla", "SimVLA", COLORS["vla"]),
        ("latch", "U-VOWEL", COLORS["latch"]),
    ]
    x = np.arange(len(order))
    width = 0.24
    fig, ax = plt.subplots(figsize=(6.85, 2.55))
    for index, (key, label, color) in enumerate(policies):
        values = suite_success(official, key)
        ys = [values[suite] for suite in order]
        bars = ax.bar(
            x + (index - 1) * width,
            ys,
            width,
            label=label,
            color=color,
            edgecolor="black",
            linewidth=0.45,
        )
        ax.bar_label(bars, labels=[f"{value:.1f}" for value in ys], padding=2, fontsize=6.5)
    ax.set_ylabel("Episode success (%)")
    ax.set_xticks(x, labels)
    ax.set_ylim(0, 100)
    ax.grid(axis="y", color="#D9D9D9", linewidth=0.5)
    ax.legend(frameon=False, ncol=3, loc="upper center")
    fig.tight_layout()
    save(fig, "fig_results_libero_pro_success")


def plot_success_compute(official: dict) -> None:
    points = [
        ("base_simvla", "SimVLA", COLORS["vla"], "o"),
        ("base_wm", "World model", COLORS["wm"], "s"),
        ("fresh", "Fresh U-VOWEL", COLORS["fresh"], "^"),
        ("latch", "Latch-50 U-VOWEL", COLORS["latch"], "D"),
    ]
    fig, ax = plt.subplots(figsize=(3.35, 2.55))
    annotations = {
        "SimVLA": ((5, -13), "left"),
        "World model": ((-8, -14), "right"),
        "Fresh U-VOWEL": ((-5, -16), "right"),
        "Latch-50 U-VOWEL": ((-5, 10), "right"),
    }
    for key, label, color, marker in points:
        summary = official[key]["summary"]
        x = summary["successful_mean"]
        y = 100.0 * summary["rate"]
        ax.scatter(x, y, s=48, color=color, marker=marker, edgecolor="black", linewidth=0.5, zorder=3)
        offset, alignment = annotations[label]
        ax.annotate(
            label,
            (x, y),
            xytext=offset,
            textcoords="offset points",
            fontsize=6.5,
            ha=alignment,
        )
    ax.set_xlabel("Successful-episode wall time (s)")
    ax.set_ylabel("Episode success (%)")
    ax.set_xlim(0, 16)
    ax.set_ylim(39.5, 45.0)
    ax.grid(color="#D9D9D9", linewidth=0.5)
    fig.tight_layout()
    save(fig, "fig_results_success_compute")


def plot_detector_transfer(rows: list[dict]) -> None:
    fig, ax = plt.subplots(figsize=(3.35, 2.65))
    ours = [row for row in rows if row["family"] == "Ours"]
    ax.plot(
        [100 * row["success_false_alarm"] for row in ours],
        [100 * row["failure_detection"] for row in ours],
        color=COLORS["wm"],
        marker="o",
        linewidth=1.2,
        label="Temporal risk head",
    )
    for row in ours:
        if row["rule"] in {"q95_success", "q99_success"}:
            ax.annotate(
                row["rule"].replace("_success", ""),
                (100 * row["success_false_alarm"], 100 * row["failure_detection"]),
                xytext=(4, 4),
                textcoords="offset points",
                fontsize=6.2,
            )

    styles = {
        "entropy": (COLORS["fiper_entropy"], "^", "FIPER entropy"),
        "rnd_oe": (COLORS["fiper_rnd"], "s", "FIPER RND-OE"),
        "rnd_oe_and_entropy": (COLORS["fiper_fusion"], "D", "FIPER fusion"),
    }
    for family, (color, marker, label) in styles.items():
        selected = [row for row in rows if row["family"] == family]
        ax.scatter(
            [100 * row["success_false_alarm"] for row in selected],
            [100 * row["failure_detection"] for row in selected],
            color=color,
            marker=marker,
            s=34,
            edgecolor="black",
            linewidth=0.4,
            label=label,
        )
    ax.set_xlabel("Success false alarm (%)")
    ax.set_ylabel("Failure detection (%)")
    ax.set_xlim(-2, 102)
    ax.set_ylim(-2, 102)
    ax.grid(color="#D9D9D9", linewidth=0.5)
    ax.legend(frameon=False, loc="lower right")
    fig.tight_layout()
    save(fig, "fig_results_seen_calibrated_ood_transfer")


def main() -> None:
    configure_plotting()
    official = load_manifest("official_2000_manifest.json")
    goal_ood = load_manifest("goal_object_900_manifest.json")
    validate_manifest(official)
    validate_manifest(goal_ood)

    promoted = json.loads(git_text(PROMOTED_PATH))
    fiper_rows = list(csv.DictReader(io.StringIO(git_text(FIPER_PATH))))
    detector_rows = pooled_vla_metrics(promoted) + pooled_fiper_metrics(promoted, fiper_rows)

    derived = {
        "source_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=REPO, text=True
        ).strip(),
        "official_2000": {key: value["summary"] for key, value in official.items()},
        "goal_object_ood_900": {key: value["summary"] for key, value in goal_ood.items()},
        "detector_transfer_pooled": detector_rows,
    }
    (DATA / "paper_results_metrics.json").write_text(json.dumps(derived, indent=2) + "\n")

    plot_suite_success(official)
    plot_success_compute(official)
    plot_detector_transfer(detector_rows)
    print("Validated matched raw episode identities and rebuilt Results artifacts.")


if __name__ == "__main__":
    main()
