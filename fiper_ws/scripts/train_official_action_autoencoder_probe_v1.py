#!/usr/bin/env python3
"""Train one action-chunk autoencoder on official LIBERO expert demos.

This is a GPU-based official-action model probe for OOD monitors.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader

FOLDS: dict[str, list[str]] = {
    "fold_00_holdout_alphabet_soup_bbq_sauce": ["alphabet_soup", "bbq_sauce"],
    "fold_01_holdout_butter_chocolate_pudding": ["butter", "chocolate_pudding"],
    "fold_02_holdout_cream_cheese_ketchup": ["cream_cheese", "ketchup"],
    "fold_03_holdout_milk_orange_juice": ["milk", "orange_juice"],
    "fold_04_holdout_salad_dressing_tomato_sauce": ["salad_dressing", "tomato_sauce"],
}

OBJECTS = [
    "alphabet_soup",
    "bbq_sauce",
    "butter",
    "chocolate_pudding",
    "cream_cheese",
    "ketchup",
    "milk",
    "orange_juice",
    "salad_dressing",
    "tomato_sauce",
]

SPLITS = [
    "success_calib_seen",
    "success_val_seen",
    "success_test_seen",
    "success_test_ood",
    "failure_eval_ood",
]

@dataclass
class RowInput:
    split: str
    episode_key: str
    timestep: int
    action_flat: np.ndarray

@dataclass
class EpisodeTrace:
    fold: str
    split: str
    episode_key: str
    scores: list[float]

def set_seed(seed: int):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open() as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    return rows

def quantile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    xs = sorted(values)
    idx = int(math.ceil(q * len(xs))) - 1
    return xs[max(0, min(idx, len(xs) - 1))]

def conformal_upper_threshold(values: list[float], alpha: float) -> float:
    if not values:
        return float("inf")
    xs = sorted(values)
    rank_1indexed = int(math.ceil((len(xs) + 1) * (1.0 - alpha)))
    if rank_1indexed > len(xs):
        return float("inf")
    return xs[max(0, rank_1indexed - 1)]

def object_demo_path(official_dir: Path, obj: str) -> Path:
    return official_dir / f"pick_up_the_{obj}_and_place_it_in_the_basket_demo.hdf5"

def load_official_action_chunks(
    official_dir: Path,
    objects: list[str],
    chunk_len: int,
    stride: int,
) -> np.ndarray:
    import h5py

    chunks: list[np.ndarray] = []
    for obj in objects:
        path = object_demo_path(official_dir, obj)
        if not path.exists():
            raise FileNotFoundError(path)
        with h5py.File(path, "r") as h5:
            data = h5["data"]
            for demo_name in sorted(data.keys()):
                actions = np.asarray(data[demo_name]["actions"], dtype=np.float32)
                if actions.ndim != 2 or actions.shape[1] < 7:
                    continue
                for start in range(0, max(0, actions.shape[0] - chunk_len + 1), stride):
                    chunks.append(actions[start : start + chunk_len, :7].reshape(-1))
    if not chunks:
        raise RuntimeError(f"no official action chunks loaded for objects={objects}")
    return np.stack(chunks, axis=0)

def action_flat_from_row(row: dict[str, Any], chunk_len: int = 10, action_dim: int = 7) -> np.ndarray:
    chunk = row.get("main_candidate_action_chunk_normalized")
    if chunk is None:
        chunk = row.get("main_candidate_action_chunk")
    arr = np.asarray(chunk if chunk is not None else [], dtype=np.float32)
    if arr.ndim == 1:
        arr = arr.reshape(-1, action_dim) if arr.size % action_dim == 0 else arr.reshape(1, -1)
    out = np.zeros((chunk_len, action_dim), dtype=np.float32)
    if arr.size:
        rr = min(chunk_len, arr.shape[0])
        cc = min(action_dim, arr.shape[1])
        out[:rr, :cc] = arr[:rr, :cc]
    return out.reshape(-1)

def load_receding_rows_for_fold(
    refs_dir: Path,
    base_dir: Path,
    max_rows_per_split: int | None,
) -> list[RowInput]:
    refs_by_source: dict[str, list[tuple[int, dict[str, Any], str]]] = defaultdict(list)
    for split in SPLITS:
        path = refs_dir / f"{split}.rows.jsonl"
        if not path.exists():
            raise FileNotFoundError(path)
        refs = read_jsonl(path)
        if max_rows_per_split and len(refs) > max_rows_per_split:
            indices = np.linspace(0, len(refs) - 1, num=max_rows_per_split, dtype=np.int64)
            refs = [refs[int(i)] for i in indices]
        for ref in refs:
            refs_by_source[str(ref["source_jsonl"])].append((int(ref["line_no"]), ref, split))

    loaded: list[RowInput] = []
    for source, entries in refs_by_source.items():
        entries.sort(key=lambda item: item[0])
        path = Path(source)
        if not path.is_absolute():
            path = base_dir / path
        pending_by_line: dict[int, list[tuple[dict[str, Any], str]]] = defaultdict(list)
        for line_no, ref, split in entries:
            pending_by_line[line_no].append((ref, split))
        wanted = sorted(pending_by_line)
        wanted_idx = 0
        with path.open() as f:
            for current_line_no, line in enumerate(f, start=1):
                while wanted_idx < len(wanted) and wanted[wanted_idx] < current_line_no:
                    wanted_idx += 1
                if wanted_idx >= len(wanted):
                    break
                if current_line_no != wanted[wanted_idx]:
                    continue
                row = json.loads(line)
                action_flat = action_flat_from_row(row)
                for ref, split in pending_by_line[current_line_no]:
                    loaded.append(
                        RowInput(
                            split=split,
                            episode_key=str(ref.get("episode_key") or row.get("episode_id")),
                            timestep=int(ref.get("timestep", row.get("timestep", 0))),
                            action_flat=action_flat,
                        )
                    )
    return loaded

def traces_from_row_scores(
    fold: str,
    row_scores: list[tuple[str, str, int, float]],
) -> list[EpisodeTrace]:
    grouped: dict[tuple[str, str], list[tuple[int, float]]] = defaultdict(list)
    for split, episode_key, timestep, score in row_scores:
        grouped[(split, episode_key)].append((timestep, score))
    traces: list[EpisodeTrace] = []
    for (split, episode_key), values in grouped.items():
        values.sort(key=lambda item: item[0])
        traces.append(
            EpisodeTrace(
                fold=fold,
                split=split,
                episode_key=episode_key,
                scores=[float(score) for _, score in values],
            )
        )
    return traces

def load_current_traces(campaign_root: Path, fold: str, job: str) -> tuple[list[EpisodeTrace], float]:
    job_dir = campaign_root / fold / "jobs" / job
    scores_path = job_dir / "scores.jsonl"
    thresholds_path = job_dir / "thresholds.json"
    if not scores_path.exists():
        raise FileNotFoundError(scores_path)
    thresholds = json.loads(thresholds_path.read_text())["score"]["eventual"]
    row_scores: list[tuple[str, str, int, float]] = []
    with scores_path.open() as f:
        for line in f:
            row = json.loads(line)
            split = row.get("split")
            if split in SPLITS:
                row_scores.append(
                    (
                        split,
                        str(row["episode_key"]),
                        int(row["timestep"]),
                        float(row["score"]),
                    )
                )
    return traces_from_row_scores(fold, row_scores), float(thresholds["q95"])

def episode_masses(traces: list[EpisodeTrace], split: str, row_threshold: float) -> list[float]:
    masses = []
    for trace in traces:
        if trace.split == split:
            masses.append(sum(max(0.0, score - row_threshold) for score in trace.scores))
    return masses

def trigger_mass(scores: list[float], row_threshold: float, mass_threshold: float) -> int | None:
    mass = 0.0
    for idx, score in enumerate(scores):
        mass += max(0.0, score - row_threshold)
        if mass >= mass_threshold:
            return idx
    return None

def trigger_for_trace(
    trace: EpisodeTrace,
    row_threshold: float,
    mass_threshold: float,
) -> int | None:
    return trigger_mass(trace.scores, row_threshold, mass_threshold)

def trace_key(trace: EpisodeTrace) -> tuple[str, str, str]:
    return (trace.fold, trace.split, trace.episode_key)

def evaluate_named_triggers(
    triggers_by_key: dict[tuple[str, str, str], int | None],
    lengths_by_key: dict[tuple[str, str, str], int],
) -> dict[str, float]:
    split_keys: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
    for key in lengths_by_key:
        split_keys[key[1]].append(key)

    out: dict[str, float] = {}
    for split in ["success_test_seen", "success_test_ood", "failure_eval_ood"]:
        keys = split_keys.get(split, [])
        n = len(keys)
        fired = [(triggers_by_key.get(key), lengths_by_key[key]) for key in keys]
        fired = [(step, length) for step, length in fired if step is not None]
        rate = len(fired) / n if n else 0.0
        out[f"{split}_episodes"] = float(n)
        out[f"{split}_alarm_rate"] = rate
        if split == "failure_eval_ood":
            out["failure_det_rate"] = rate
            out["failure_never_rate"] = 1.0 - rate
            out["failure_det_at_10"] = (
                sum(1 for step, length in fired if step / max(1, length) <= 0.10) / n if n else 0.0
            )
            out["failure_det_at_25"] = (
                sum(1 for step, length in fired if step / max(1, length) <= 0.25) / n if n else 0.0
            )
            out["failure_det_at_50"] = (
                sum(1 for step, length in fired if step / max(1, length) <= 0.50) / n if n else 0.0
            )
            out["failure_mean_time_detected_only"] = (
                float(np.mean([step / max(1, length) for step, length in fired])) if fired else 1.0
            )
    return out

def format_pct(value: float) -> str:
    return f"{100.0 * value:.1f}%"

class ActionAutoencoder(nn.Module):
    def __init__(self, input_dim=70, latent_dim=32):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, latent_dim),
        )
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 64),
            nn.ReLU(),
            nn.Linear(64, 128),
            nn.ReLU(),
            nn.Linear(128, input_dim),
        )
    def forward(self, x):
        latent = self.encoder(x)
        reconstructed = self.decoder(latent)
        return reconstructed

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-dir", type=Path, default=Path("."))
    parser.add_argument(
        "--refs-root",
        type=Path,
        default=Path("experiments/prepared_20260527/08_target_object_pick_basket_loto_v1"),
    )
    parser.add_argument(
        "--campaign-root",
        type=Path,
        default=Path("experiments/clean_temporal_nextgen_v2_full_all_20260527"),
    )
    parser.add_argument(
        "--official-dir",
        type=Path,
        default=Path("../intern_ship_ws/assets/data/libero_datasets/libero_object"),
    )
    parser.add_argument("--job", default="v2_018_transformer_k16")
    parser.add_argument("--chunk-len", type=int, default=10)
    parser.add_argument("--official-stride", type=int, default=5)
    parser.add_argument("--alpha", type=float, default=0.15)
    parser.add_argument("--max-rows-per-split", type=int, default=5000)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("experiments/official_expert_action_autoencoder_probe_v1_fold00_smoke_20260528"),
    )
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--latent-dim", type=int, default=32)
    parser.add_argument("--lr", type=float, default=1e-3)
    parser.add_argument("--batch-size", type=int, default=256)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--folds", nargs="+", default=[], help="Specific fold(s) to process. If empty, process all.")
    
    args = parser.parse_args()
    set_seed(args.seed)

    base_dir = args.base_dir.resolve()
    refs_root = (base_dir / args.refs_root).resolve() if not args.refs_root.is_absolute() else args.refs_root
    campaign_root = (
        (base_dir / args.campaign_root).resolve()
        if not args.campaign_root.is_absolute()
        else args.campaign_root
    )
    official_dir = (
        (base_dir / args.official_dir).resolve()
        if not args.official_dir.is_absolute()
        else args.official_dir
    )
    output_dir = (base_dir / args.output_dir).resolve() if not args.output_dir.is_absolute() else args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    rows_for_csv: list[dict[str, Any]] = []
    calibration_report: dict[str, Any] = {}
    all_fold_results: dict[str, dict[str, dict[str, float]]] = {}

    target_folds = args.folds if args.folds else list(FOLDS.keys())

    for fold in target_folds:
        if fold not in FOLDS:
            print(f"Warning: fold '{fold}' not recognized. Skipping.")
            continue
        heldout = FOLDS[fold]
        print(f"\n--- Processing Fold: {fold} ---")
        seen_objects = [obj for obj in OBJECTS if obj not in set(heldout)]
        print(f"Held-out objects: {heldout}")
        print(f"Seen objects for training: {seen_objects}")

        # 1. Load official demos
        official_chunks = load_official_action_chunks(
            official_dir=official_dir,
            objects=seen_objects,
            chunk_len=args.chunk_len,
            stride=args.official_stride,
        )
        print(f"Loaded {official_chunks.shape[0]} official action chunks of shape {official_chunks.shape[1]}.")

        # Compute dataset stats for standardization
        mean = official_chunks.mean(axis=0)
        std = official_chunks.std(axis=0)
        std = np.maximum(std, 1e-5)

        # Standardize official chunks
        normalized_official = (official_chunks - mean) / std

        # 2. Train the Autoencoder
        x_train = torch.from_numpy(normalized_official).float()
        dataset = TensorDataset(x_train)
        loader = DataLoader(dataset, batch_size=args.batch_size, shuffle=True)

        model = ActionAutoencoder(input_dim=args.chunk_len * 7, latent_dim=args.latent_dim).to(device)
        optimizer = optim.Adam(model.parameters(), lr=args.lr)
        criterion = nn.MSELoss()

        model.train()
        for epoch in range(args.epochs):
            epoch_loss = 0.0
            for batch in loader:
                x_batch = batch[0].to(device)
                optimizer.zero_grad()
                reconstructed = model(x_batch)
                loss = criterion(reconstructed, x_batch)
                loss.backward()
                optimizer.step()
                epoch_loss += loss.item() * x_batch.size(0)
            epoch_loss /= len(x_train)
            print(f"  Epoch {epoch+1}/{args.epochs} - Loss: {epoch_loss:.6f}")

        # 3. Load receding rows and evaluate
        refs_dir = refs_root / fold / "datasets" / "refs"
        row_inputs = load_receding_rows_for_fold(
            refs_dir=refs_dir,
            base_dir=base_dir,
            max_rows_per_split=args.max_rows_per_split,
        )
        print(f"Loaded {len(row_inputs)} receding rows.")

        # Reconstruct and score rows
        model.eval()
        expert_row_scores = []
        with torch.no_grad():
            for item in row_inputs:
                x_row = item.action_flat
                # Normalize
                x_row_norm = (x_row - mean) / std
                x_tensor = torch.from_numpy(x_row_norm).float().unsqueeze(0).to(device)
                x_rec = model(x_tensor).cpu().numpy().squeeze(0)
                # Reconstruction loss: MSE
                score = float(np.mean((x_row_norm - x_rec) ** 2))
                expert_row_scores.append((item.split, item.episode_key, item.timestep, score))

        # Convert to traces
        expert_traces = traces_from_row_scores(fold, expert_row_scores)

        # Calibrate q95 on success_calib_seen
        calib_scores = [
            score
            for trace in expert_traces
            if trace.split == "success_calib_seen"
            for score in trace.scores
        ]
        expert_q95 = quantile(calib_scores, 0.95)

        # Calibrate mass conformal on success_val_seen
        expert_mass_threshold = conformal_upper_threshold(
            episode_masses(expert_traces, "success_val_seen", expert_q95),
            args.alpha,
        )

        # Triggers
        expert_trigger_by_key = {
            trace_key(trace): trigger_for_trace(trace, expert_q95, expert_mass_threshold)
            for trace in expert_traces
            if trace.split in {"success_test_seen", "success_test_ood", "failure_eval_ood"}
        }
        expert_lengths_by_key = {
            trace_key(trace): len(trace.scores)
            for trace in expert_traces
            if trace.split in {"success_test_seen", "success_test_ood", "failure_eval_ood"}
        }

        # Load baseline transformer traces
        current_traces, current_q95 = load_current_traces(campaign_root, fold, args.job)
        current_mass_threshold = conformal_upper_threshold(
            episode_masses(current_traces, "success_val_seen", current_q95),
            args.alpha,
        )
        current_trigger_by_key = {
            trace_key(trace): trigger_for_trace(trace, current_q95, current_mass_threshold)
            for trace in current_traces
            if trace.split in {"success_test_seen", "success_test_ood", "failure_eval_ood"}
        }
        lengths_by_key = {
            trace_key(trace): len(trace.scores)
            for trace in current_traces
            if trace.split in {"success_test_seen", "success_test_ood", "failure_eval_ood"}
        }

        fold_results: dict[str, dict[str, float]] = {
            "current_transformer_mass": evaluate_named_triggers(current_trigger_by_key, lengths_by_key),
            "official_autoencoder_mass": evaluate_named_triggers(expert_trigger_by_key, expert_lengths_by_key),
        }

        # Combine trigger logic (AND/OR)
        shared_keys = set(current_trigger_by_key) & set(expert_trigger_by_key)
        and_triggers = {}
        or_triggers = {}
        for key in shared_keys:
            cur = current_trigger_by_key.get(key)
            exp = expert_trigger_by_key.get(key)
            and_triggers[key] = max(cur, exp) if cur is not None and exp is not None else None
            if cur is None:
                or_triggers[key] = exp
            elif exp is None:
                or_triggers[key] = cur
            else:
                or_triggers[key] = min(cur, exp)
        shared_lengths = {key: lengths_by_key[key] for key in shared_keys}
        fold_results["current_AND_official_autoencoder"] = evaluate_named_triggers(
            and_triggers,
            shared_lengths,
        )
        fold_results["current_OR_official_autoencoder"] = evaluate_named_triggers(
            or_triggers,
            shared_lengths,
        )

        calibration_report[fold] = {
            "heldout_objects": heldout,
            "official_seen_objects": seen_objects,
            "official_chunks": int(official_chunks.shape[0]),
            "current_q95": current_q95,
            "current_mass_threshold": current_mass_threshold,
            "autoencoder": {
                "expert_q95": expert_q95,
                "expert_mass_threshold": expert_mass_threshold,
                "success_calib_rows": len(calib_scores),
            }
        }

        all_fold_results[fold] = fold_results
        for policy_name, metrics in fold_results.items():
            rows_for_csv.append({"fold": fold, "policy": policy_name, **metrics})

    # Aggregates across folds if multiple folds are processed
    aggregate: dict[str, dict[str, float]] = {}
    policies = sorted({row["policy"] for row in rows_for_csv})
    for policy in policies:
        policy_rows = [row for row in rows_for_csv if row["policy"] == policy]
        seen_eps = sum(int(row["success_test_seen_episodes"]) for row in policy_rows)
        ood_eps = sum(int(row["success_test_ood_episodes"]) for row in policy_rows)
        fail_eps = sum(int(row["failure_eval_ood_episodes"]) for row in policy_rows)
        seen_alarms = sum(row["success_test_seen_alarm_rate"] * row["success_test_seen_episodes"] for row in policy_rows)
        ood_alarms = sum(row["success_test_ood_alarm_rate"] * row["success_test_ood_episodes"] for row in policy_rows)
        fail_det = sum(row["failure_det_rate"] * row["failure_eval_ood_episodes"] for row in policy_rows)
        fail_det10 = sum(row["failure_det_at_10"] * row["failure_eval_ood_episodes"] for row in policy_rows)
        fail_det25 = sum(row["failure_det_at_25"] * row["failure_eval_ood_episodes"] for row in policy_rows)
        fail_det50 = sum(row["failure_det_at_50"] * row["failure_eval_ood_episodes"] for row in policy_rows)
        det_weight = sum(
            row["failure_det_rate"] * row["failure_eval_ood_episodes"]
            for row in policy_rows
            if row["failure_det_rate"] > 0
        )
        mean_time_num = sum(
            row["failure_mean_time_detected_only"]
            * row["failure_det_rate"]
            * row["failure_eval_ood_episodes"]
            for row in policy_rows
        )
        aggregate[policy] = {
            "success_test_seen_episodes": float(seen_eps),
            "success_test_seen_alarm_rate": seen_alarms / seen_eps if seen_eps else 0.0,
            "success_test_ood_episodes": float(ood_eps),
            "success_test_ood_alarm_rate": ood_alarms / ood_eps if ood_eps else 0.0,
            "failure_eval_ood_episodes": float(fail_eps),
            "failure_det_rate": fail_det / fail_eps if fail_eps else 0.0,
            "failure_det_at_10": fail_det10 / fail_eps if fail_eps else 0.0,
            "failure_det_at_25": fail_det25 / fail_eps if fail_eps else 0.0,
            "failure_det_at_50": fail_det50 / fail_eps if fail_eps else 0.0,
            "failure_never_rate": 1.0 - (fail_det / fail_eps if fail_eps else 0.0),
            "failure_mean_time_detected_only": mean_time_num / det_weight if det_weight else 1.0,
        }
        if len(target_folds) > 1:
            rows_for_csv.append({"fold": "ALL_TARGET_OBJECT_FOLDS", "policy": policy, **aggregate[policy]})

    csv_path = output_dir / "official_expert_action_autoencoder_results.csv"
    with csv_path.open("w", newline="") as f:
        fieldnames = [
            "fold",
            "policy",
            "success_test_seen_episodes",
            "success_test_seen_alarm_rate",
            "success_test_ood_episodes",
            "success_test_ood_alarm_rate",
            "failure_eval_ood_episodes",
            "failure_det_rate",
            "failure_det_at_10",
            "failure_det_at_25",
            "failure_det_at_50",
            "failure_never_rate",
            "failure_mean_time_detected_only",
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows_for_csv)
    print(f"Wrote {csv_path}")

    (output_dir / "official_expert_action_autoencoder_results.json").write_text(
        json.dumps({"folds": all_fold_results, "aggregate": aggregate}, indent=2, sort_keys=True)
    )
    (output_dir / "official_expert_action_autoencoder_calibration.json").write_text(
        json.dumps(calibration_report, indent=2, sort_keys=True)
    )

    report_lines = [
        "# Official LIBERO Expert Action Autoencoder Probe",
        "",
        "## Setup",
        "",
        f"- Current score baseline: `{args.job}` mass-conformal alpha={args.alpha}",
        f"- Official demos: `{official_dir}`",
        "- Leakage rule: each fold excludes its held-out target objects from official expert fitting.",
        "- Features used by expert score: only 10-step main action chunk, flattened to 70 dims.",
        "- Forbidden deploy-time fields used: none.",
        f"- Network architecture: MLP Autoencoder (70 -> 128 -> 64 -> {args.latent_dim} -> 64 -> 128 -> 70)",
        f"- Epochs: {args.epochs}, Batch Size: {args.batch_size}, Learning Rate: {args.lr}",
        "",
        "## Results Table",
        "",
        "| Policy | Seen FA | OOD FA | OOD Failure Det | Det@10 | Det@25 | Det@50 | Mean Det Time | Never |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    
    # We display results for the processed folds
    for row in rows_for_csv:
        # Avoid duplicating aggregate row if there's only one fold
        if len(target_folds) == 1 and row["fold"] == "ALL_TARGET_OBJECT_FOLDS":
            continue
        report_lines.append(
            f"| {row['fold']} - {row['policy']} | "
            + " | ".join(
                [
                    format_pct(row["success_test_seen_alarm_rate"]),
                    format_pct(row["success_test_ood_alarm_rate"]),
                    format_pct(row["failure_det_rate"]),
                    format_pct(row["failure_det_at_10"]),
                    format_pct(row["failure_det_at_25"]),
                    format_pct(row["failure_det_at_50"]),
                    f"{row['failure_mean_time_detected_only']:.3f}",
                    format_pct(row["failure_never_rate"]),
                ]
            )
            + " |"
        )
        
    report_lines.extend(
        [
            "",
            "## Output Files",
            "",
            f"- `{csv_path}`",
            f"- `{output_dir / 'official_expert_action_autoencoder_results.json'}`",
            f"- `{output_dir / 'official_expert_action_autoencoder_calibration.json'}`",
        ]
    )
    
    report_path = output_dir / "OFFICIAL_EXPERT_ACTION_AUTOENCODER_PROBE_REPORT.md"
    report_path.write_text("\n".join(report_lines) + "\n")
    print(f"Wrote {report_path}")

if __name__ == "__main__":
    main()
