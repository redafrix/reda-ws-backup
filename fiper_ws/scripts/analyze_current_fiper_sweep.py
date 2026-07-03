#!/usr/bin/env python3
"""Current Stage 9 FIPER offline audit/train/eval pipeline.

This script is intentionally not hard-coded to one old archive. It is designed
for the current v2 receding JSONL schema:

- one executed main chunk per timestep
- only first main action executed
- ACE candidates sampled from the same observation and never replayed
- success rows train/calib/eval eligible
- failure/timeout rows eval only

Default mode is audit-only. Pass --run-train-eval to train RND and compute the
RND + ACE monitor metrics.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import random
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, Iterator, List, Optional, Sequence, Tuple

import numpy as np


REQUIRED_KEYS = {
    "episode_id",
    "timestep",
    "suite",
    "task_id",
    "task_instruction",
    "main_seed",
    "main_candidate_action_chunk_normalized",
    "main_candidate_action_chunk_env",
    "executed_action",
    "ace_candidate_seeds",
    "ace_candidate_chunks_normalized",
    "ace_candidate_chunks_env",
    "episode_outcome",
    "allowed_use",
}


def perturbation_group(suite: str) -> str:
    if "with_mug" in suite or suite.endswith("_mug"):
        return "mug"
    if "with_milk" in suite or suite.endswith("_milk"):
        return "milk"
    if suite.endswith("_env") or "_env" in suite:
        return "env"
    if suite.endswith("_object") or "_object" in suite:
        return "object"
    return "unknown"


def detect_machine(path: Path) -> str:
    text = str(path).lower()
    if "pcrobot" in text or "my passport" in text or "bob" in text:
        return "bob"
    if "sam" in text or "/home/rootalkhatib/test/reda_ws" in text:
        return "sam"
    return "unknown"


def episode_key(path: Path, row: dict) -> str:
    instance = path.parent.name
    campaign = path.parent.parent.name
    machine = detect_machine(path)
    ep_id = row["episode_id"]
    return f"{machine}|{campaign}|{instance}|{ep_id}"


def parse_suite_task(value: str) -> Tuple[str, int]:
    if ":" not in value:
        raise argparse.ArgumentTypeError(f"Expected SUITE:TASK_ID, got {value!r}")
    suite, task_text = value.rsplit(":", 1)
    return suite, int(task_text)


def discover_jsonls(input_roots: Sequence[Path], input_jsonls: Sequence[Path]) -> List[Path]:
    paths: List[Path] = []
    for path in input_jsonls:
        paths.append(path)
    for root in input_roots:
        if root.is_file() and root.name.endswith(".jsonl"):
            paths.append(root)
        elif root.exists():
            paths.extend(sorted(root.glob("**/fiper_receding_samples.jsonl")))
    deduped = []
    seen = set()
    for path in paths:
        key = str(path)
        if key not in seen:
            seen.add(key)
            deduped.append(path)
    return deduped


def load_config(path: Optional[Path]) -> dict:
    if path is None:
        return {}
    with path.open("r") as f:
        return json.load(f)


@dataclass
class EpisodeInfo:
    key: str
    machine: str
    source_path: str
    campaign: str
    instance: str
    episode_id: str
    suite: str
    task_id: int
    group: str
    outcome: str
    rows: int = 0
    first_timestep: int = 10**12
    last_timestep: int = -1


def safe_shape(value) -> Tuple[int, ...]:
    try:
        return tuple(np.asarray(value).shape)
    except Exception:
        return ()


def rows_from_paths(paths: Sequence[Path]) -> Iterator[Tuple[Path, int, Optional[dict], Optional[str]]]:
    for path in paths:
        with path.open("r") as f:
            for line_no, line in enumerate(f, start=1):
                if not line.strip():
                    continue
                try:
                    yield path, line_no, json.loads(line), None
                except Exception as exc:
                    yield path, line_no, None, str(exc)


def is_excluded(row: dict, excluded: set[Tuple[str, int]]) -> bool:
    return (row.get("suite"), int(row.get("task_id", -1))) in excluded


def audit_dataset(paths: Sequence[Path], excluded: set[Tuple[str, int]]) -> Tuple[Dict[str, EpisodeInfo], dict]:
    episodes: Dict[str, EpisodeInfo] = {}
    stats = {
        "raw_rows": 0,
        "used_rows": 0,
        "excluded_rows": 0,
        "corrupt_rows": 0,
        "missing_required_rows": 0,
        "ace_replay_violations": 0,
        "first_action_mismatches": 0,
        "first_action_checked": 0,
        "rows_by_machine": Counter(),
        "rows_by_suite": Counter(),
        "rows_by_task": Counter(),
        "rows_by_group": Counter(),
        "rows_by_outcome": Counter(),
        "ace_candidate_count": Counter(),
        "main_chunk_shape": Counter(),
        "executed_action_shape": Counter(),
        "duplicate_main_seeds": 0,
        "duplicate_ace_seeds": 0,
        "unique_main_seeds": 0,
        "unique_ace_seeds": 0,
    }
    main_seeds = set()
    ace_seeds = set()

    for path, line_no, row, parse_error in rows_from_paths(paths):
        stats["raw_rows"] += 1
        if parse_error is not None:
            stats["corrupt_rows"] += 1
            continue
        missing = REQUIRED_KEYS.difference(row)
        if missing:
            stats["missing_required_rows"] += 1
            continue
        if is_excluded(row, excluded):
            stats["excluded_rows"] += 1
            continue

        key = episode_key(path, row)
        machine = detect_machine(path)
        campaign = path.parent.parent.name
        instance = path.parent.name
        suite = row["suite"]
        task_id = int(row["task_id"])
        group = perturbation_group(suite)
        outcome = row["episode_outcome"]

        if key not in episodes:
            episodes[key] = EpisodeInfo(
                key=key,
                machine=machine,
                source_path=str(path),
                campaign=campaign,
                instance=instance,
                episode_id=str(row["episode_id"]),
                suite=suite,
                task_id=task_id,
                group=group,
                outcome=outcome,
            )
        ep = episodes[key]
        ep.rows += 1
        ep.first_timestep = min(ep.first_timestep, int(row["timestep"]))
        ep.last_timestep = max(ep.last_timestep, int(row["timestep"]))

        stats["used_rows"] += 1
        stats["rows_by_machine"][machine] += 1
        stats["rows_by_suite"][suite] += 1
        stats["rows_by_task"][f"{suite}:t{task_id}"] += 1
        stats["rows_by_group"][group] += 1
        stats["rows_by_outcome"][outcome] += 1
        stats["ace_candidate_count"][len(row["ace_candidate_chunks_normalized"])] += 1
        stats["main_chunk_shape"][str(safe_shape(row["main_candidate_action_chunk_normalized"]))] += 1
        stats["executed_action_shape"][str(safe_shape(row["executed_action"]))] += 1

        metadata = row.get("metadata", {})
        if metadata.get("ace_replay_used", False) is not False:
            stats["ace_replay_violations"] += 1

        executed = np.asarray(row["executed_action"], dtype=np.float32)
        first = np.asarray(row["main_candidate_action_chunk_env"][0], dtype=np.float32)
        stats["first_action_checked"] += 1
        if not np.allclose(executed, first, atol=1e-5):
            stats["first_action_mismatches"] += 1

        main_seed = int(row["main_seed"])
        if main_seed in main_seeds:
            stats["duplicate_main_seeds"] += 1
        main_seeds.add(main_seed)

        for seed in row["ace_candidate_seeds"]:
            seed = int(seed)
            if seed in ace_seeds:
                stats["duplicate_ace_seeds"] += 1
            ace_seeds.add(seed)

    stats["unique_main_seeds"] = len(main_seeds)
    stats["unique_ace_seeds"] = len(ace_seeds)
    return episodes, stats


def assign_splits(
    episodes: Dict[str, EpisodeInfo],
    seed: int,
    train_fraction: float,
    calib_fraction: float,
    holdout_suites: set[str],
    holdout_groups: set[str],
    holdout_tasks: set[Tuple[str, int]],
) -> Dict[str, str]:
    rng = random.Random(seed)
    split_by_episode: Dict[str, str] = {}
    success_by_stratum: Dict[Tuple[str, int], List[str]] = defaultdict(list)

    for key, ep in episodes.items():
        if ep.outcome == "failure_or_timeout":
            split_by_episode[key] = "failure_eval_all"
            continue
        if ep.outcome != "success":
            split_by_episode[key] = "unknown_outcome_eval_only"
            continue

        if ep.suite in holdout_suites or ep.group in holdout_groups or (ep.suite, ep.task_id) in holdout_tasks:
            split_by_episode[key] = "success_ood"
            continue
        success_by_stratum[(ep.suite, ep.task_id)].append(key)

    for keys in success_by_stratum.values():
        rng.shuffle(keys)
        n = len(keys)
        if n == 1:
            n_train, n_calib = 1, 0
        elif n == 2:
            n_train, n_calib = 1, 1
        else:
            n_train = max(1, int(round(n * train_fraction)))
            n_calib = max(1, int(round(n * calib_fraction)))
            if n_train + n_calib >= n:
                n_train = max(1, n - 2)
                n_calib = 1
        for key in keys[:n_train]:
            split_by_episode[key] = "success_train"
        for key in keys[n_train:n_train + n_calib]:
            split_by_episode[key] = "success_calib"
        for key in keys[n_train + n_calib:]:
            split_by_episode[key] = "success_test_id"

    return split_by_episode


def save_episode_manifest(output_dir: Path, episodes: Dict[str, EpisodeInfo], split_by_episode: Dict[str, str]) -> None:
    path = output_dir / "episode_manifest.csv"
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "episode_key",
                "split",
                "machine",
                "campaign",
                "instance",
                "episode_id",
                "suite",
                "task_id",
                "group",
                "outcome",
                "rows",
                "first_timestep",
                "last_timestep",
                "source_path",
            ],
        )
        writer.writeheader()
        for key in sorted(episodes):
            ep = episodes[key]
            writer.writerow(
                {
                    "episode_key": key,
                    "split": split_by_episode.get(key, "unassigned"),
                    "machine": ep.machine,
                    "campaign": ep.campaign,
                    "instance": ep.instance,
                    "episode_id": ep.episode_id,
                    "suite": ep.suite,
                    "task_id": ep.task_id,
                    "group": ep.group,
                    "outcome": ep.outcome,
                    "rows": ep.rows,
                    "first_timestep": ep.first_timestep,
                    "last_timestep": ep.last_timestep,
                    "source_path": ep.source_path,
                }
            )


def gaussian_entropy(candidates_norm: np.ndarray, reg: float = 1e-4) -> float:
    flat = candidates_norm.reshape(candidates_norm.shape[0], -1)
    cov = np.cov(flat, rowvar=False)
    cov_reg = cov + reg * np.eye(cov.shape[0], dtype=np.float64)
    sign, logdet = np.linalg.slogdet(cov_reg)
    if sign <= 0:
        return float("nan")
    dim = cov.shape[0]
    return float(0.5 * dim * (1.0 + np.log(2 * np.pi)) + 0.5 * logdet)


def row_features(row: dict) -> Tuple[np.ndarray, float]:
    action = np.asarray(row["main_candidate_action_chunk_normalized"], dtype=np.float32).reshape(-1)
    candidates = np.asarray(row["ace_candidate_chunks_normalized"], dtype=np.float32)
    return action, gaussian_entropy(candidates)


def collect_features(
    paths: Sequence[Path],
    excluded: set[Tuple[str, int]],
    split_by_episode: Dict[str, str],
) -> Dict[str, dict]:
    by_split: Dict[str, dict] = defaultdict(lambda: {"x": [], "ace": [], "meta": []})
    for path, line_no, row, parse_error in rows_from_paths(paths):
        if parse_error is not None or row is None:
            continue
        if REQUIRED_KEYS.difference(row) or is_excluded(row, excluded):
            continue
        key = episode_key(path, row)
        split = split_by_episode.get(key)
        if split is None:
            continue
        x, ace = row_features(row)
        by_split[split]["x"].append(x)
        by_split[split]["ace"].append(ace)
        by_split[split]["meta"].append(
            {
                "episode_key": key,
                "suite": row["suite"],
                "task_id": int(row["task_id"]),
                "group": perturbation_group(row["suite"]),
                "outcome": row["episode_outcome"],
            }
        )

    for split, data in by_split.items():
        data["x"] = np.asarray(data["x"], dtype=np.float32)
        data["ace"] = np.asarray(data["ace"], dtype=np.float32)
    return by_split


def build_failure_subsplits(episodes: Dict[str, EpisodeInfo], split_by_episode: Dict[str, str]) -> Dict[str, set[Tuple[str, int]]]:
    ranges = {
        "failure_eval_early": set(),
        "failure_eval_late": set(),
        "failure_eval_near_end": set(),
    }
    for key, ep in episodes.items():
        if split_by_episode.get(key) != "failure_eval_all":
            continue
        n = ep.rows
        if n <= 0:
            continue
        early_cut = math.ceil(0.25 * n)
        late_start = max(0, n - math.ceil(0.25 * n))
        near_start = max(0, n - 50)
        for idx in range(0, early_cut):
            ranges["failure_eval_early"].add((key, idx))
        for idx in range(late_start, n):
            ranges["failure_eval_late"].add((key, idx))
        for idx in range(near_start, n):
            ranges["failure_eval_near_end"].add((key, idx))
    return ranges


class RNDMLP:
    def __init__(self, input_dim: int, out_dim: int = 128):
        import torch.nn as nn

        self.model = nn.Sequential(
            nn.Linear(input_dim, 256),
            nn.ReLU(),
            nn.Linear(256, 256),
            nn.ReLU(),
            nn.Linear(256, out_dim),
        )


def train_rnd(train_x: np.ndarray, calib_x: np.ndarray, output_dir: Path, seed: int, epochs: int, batch_size: int):
    import torch
    import torch.nn as nn
    import torch.optim as optim
    from torch.utils.data import DataLoader, TensorDataset

    torch.manual_seed(seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    target = RNDMLP(train_x.shape[1]).model.to(device)
    predictor = RNDMLP(train_x.shape[1]).model.to(device)
    for param in target.parameters():
        param.requires_grad = False

    loader = DataLoader(TensorDataset(torch.tensor(train_x, dtype=torch.float32)), batch_size=batch_size, shuffle=True)
    optimizer = optim.Adam(predictor.parameters(), lr=1e-3)
    criterion = nn.MSELoss()
    best_state = None
    best_loss = float("inf")
    calib_tensor = torch.tensor(calib_x, dtype=torch.float32).to(device)

    for _epoch in range(epochs):
        predictor.train()
        for (batch,) in loader:
            batch = batch.to(device)
            optimizer.zero_grad()
            with torch.no_grad():
                target_out = target(batch)
            pred_out = predictor(batch)
            loss = criterion(pred_out, target_out)
            loss.backward()
            optimizer.step()

        predictor.eval()
        with torch.no_grad():
            val_loss = criterion(predictor(calib_tensor), target(calib_tensor)).item()
        if val_loss < best_loss:
            best_loss = val_loss
            best_state = {k: v.detach().cpu().clone() for k, v in predictor.state_dict().items()}

    if best_state is not None:
        predictor.load_state_dict(best_state)

    torch.save(predictor.state_dict(), output_dir / "rnd_predictor.pt")
    torch.save(target.state_dict(), output_dir / "rnd_target.pt")
    return predictor, target, device


def rnd_scores(predictor, target, x: np.ndarray, device) -> np.ndarray:
    import torch

    if len(x) == 0:
        return np.asarray([], dtype=np.float32)
    predictor.eval()
    target.eval()
    scores = []
    with torch.no_grad():
        for start in range(0, len(x), 8192):
            batch = torch.tensor(x[start:start + 8192], dtype=torch.float32).to(device)
            diff = (predictor(batch) - target(batch)) ** 2
            scores.append(diff.mean(dim=1).detach().cpu().numpy())
    return np.concatenate(scores).astype(np.float32)


def normalize_train_calib(train_raw: np.ndarray, calib_raw: np.ndarray) -> Tuple[np.ndarray, np.ndarray, dict]:
    mean = train_raw.mean(axis=0)
    std = train_raw.std(axis=0)
    kept = np.where(std >= 1e-4)[0]
    mean_kept = mean[kept]
    std_kept = std[kept]

    def norm(x: np.ndarray) -> np.ndarray:
        return np.clip((x[:, kept] - mean_kept) / std_kept, -10.0, 10.0).astype(np.float32)

    stats = {
        "kept_dims": kept.tolist(),
        "dropped_dims": int(train_raw.shape[1] - len(kept)),
        "mean": mean_kept.astype(float).tolist(),
        "std": std_kept.astype(float).tolist(),
    }
    return norm(train_raw), norm(calib_raw), {"stats": stats, "normalize": norm}


def alarm_rates(scores: np.ndarray, thresholds: dict) -> dict:
    if len(scores) == 0:
        return {"count": 0, "q90": None, "q95": None, "q99": None}
    return {
        "count": int(len(scores)),
        "q90": float(np.mean(scores > thresholds["q90"]) * 100.0),
        "q95": float(np.mean(scores > thresholds["q95"]) * 100.0),
        "q99": float(np.mean(scores > thresholds["q99"]) * 100.0),
    }


def quadrant_rates(rnd: np.ndarray, ace: np.ndarray, rnd_q95: float, ace_q95: float) -> dict:
    if len(rnd) == 0:
        return {"count": 0}
    counts = Counter()
    for r_score, a_score in zip(rnd, ace):
        r_alarm = r_score > rnd_q95
        a_alarm = a_score > ace_q95
        if not r_alarm and not a_alarm:
            counts["normal_confident"] += 1
        elif r_alarm and not a_alarm:
            counts["ood_confident"] += 1
        elif not r_alarm and a_alarm:
            counts["action_uncertain"] += 1
        else:
            counts["fiper_alarm"] += 1
    total = float(len(rnd))
    return {"count": int(total), **{k: float(v / total * 100.0) for k, v in counts.items()}}


def run_train_eval(features: Dict[str, dict], output_dir: Path, seed: int, epochs: int, batch_size: int) -> dict:
    train_raw = features["success_train"]["x"]
    calib_raw = features["success_calib"]["x"]
    if len(train_raw) == 0 or len(calib_raw) == 0:
        raise RuntimeError("Need non-empty success_train and success_calib splits for RND.")

    train_x, calib_x, norm_pack = normalize_train_calib(train_raw, calib_raw)
    predictor, target, device = train_rnd(train_x, calib_x, output_dir, seed=seed, epochs=epochs, batch_size=batch_size)
    calib_scores = rnd_scores(predictor, target, calib_x, device)
    rnd_thresholds = {
        "q90": float(np.percentile(calib_scores, 90)),
        "q95": float(np.percentile(calib_scores, 95)),
        "q99": float(np.percentile(calib_scores, 99)),
    }
    ace_calib = features["success_calib"]["ace"]
    ace_thresholds = {
        "q90": float(np.percentile(ace_calib, 90)),
        "q95": float(np.percentile(ace_calib, 95)),
        "q99": float(np.percentile(ace_calib, 99)),
    }

    summary = {
        "normalization": norm_pack["stats"],
        "rnd_thresholds": rnd_thresholds,
        "ace_thresholds": ace_thresholds,
        "splits": {},
    }

    normalize = norm_pack["normalize"]
    for split, data in sorted(features.items()):
        x_raw = data["x"]
        ace = data["ace"]
        x = normalize(x_raw) if len(x_raw) else np.asarray([], dtype=np.float32)
        scores = rnd_scores(predictor, target, x, device)
        summary["splits"][split] = {
            "rows": int(len(x_raw)),
            "rnd_alarm_rates": alarm_rates(scores, rnd_thresholds),
            "ace_alarm_rates": alarm_rates(ace, ace_thresholds),
            "quadrants_q95": quadrant_rates(scores, ace, rnd_thresholds["q95"], ace_thresholds["q95"]),
            "rnd_mean": float(np.mean(scores)) if len(scores) else None,
            "ace_mean": float(np.mean(ace)) if len(ace) else None,
        }

    with (output_dir / "model_summary.json").open("w") as f:
        json.dump(summary, f, indent=2)
    return summary


def jsonable_stats(stats: dict, episodes: Dict[str, EpisodeInfo], split_by_episode: Dict[str, str]) -> dict:
    eps_by_outcome = Counter(ep.outcome for ep in episodes.values())
    eps_by_suite = Counter(ep.suite for ep in episodes.values())
    eps_by_group = Counter(ep.group for ep in episodes.values())
    eps_by_split = Counter(split_by_episode.values())
    lengths = [ep.rows for ep in episodes.values()]
    return {
        "rows": {
            "raw": stats["raw_rows"],
            "used": stats["used_rows"],
            "excluded": stats["excluded_rows"],
            "corrupt": stats["corrupt_rows"],
            "missing_required": stats["missing_required_rows"],
            "by_machine": dict(stats["rows_by_machine"]),
            "by_suite": dict(stats["rows_by_suite"]),
            "by_task": dict(stats["rows_by_task"]),
            "by_group": dict(stats["rows_by_group"]),
            "by_outcome": dict(stats["rows_by_outcome"]),
        },
        "episodes": {
            "total": len(episodes),
            "by_outcome": dict(eps_by_outcome),
            "by_suite": dict(eps_by_suite),
            "by_group": dict(eps_by_group),
            "by_split": dict(eps_by_split),
            "length_avg": float(np.mean(lengths)) if lengths else 0.0,
            "length_min": int(np.min(lengths)) if lengths else 0,
            "length_max": int(np.max(lengths)) if lengths else 0,
        },
        "schema": {
            "ace_candidate_count": dict(stats["ace_candidate_count"]),
            "main_chunk_shape": dict(stats["main_chunk_shape"]),
            "executed_action_shape": dict(stats["executed_action_shape"]),
            "ace_replay_violations": stats["ace_replay_violations"],
            "first_action_checked": stats["first_action_checked"],
            "first_action_mismatches": stats["first_action_mismatches"],
            "unique_main_seeds": stats["unique_main_seeds"],
            "duplicate_main_seeds": stats["duplicate_main_seeds"],
            "unique_ace_seeds": stats["unique_ace_seeds"],
            "duplicate_ace_seeds": stats["duplicate_ace_seeds"],
        },
    }


def write_markdown_report(output_dir: Path, summary: dict, train_summary: Optional[dict], paths: Sequence[Path]) -> None:
    lines = [
        "# Current FIPER Sweep Analysis Report",
        "",
        f"Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Inputs",
        "",
    ]
    for path in paths:
        lines.append(f"- `{path}`")
    rows = summary["rows"]
    eps = summary["episodes"]
    schema = summary["schema"]
    lines += [
        "",
        "## Dataset",
        "",
        f"- Raw rows: {rows['raw']}",
        f"- Used rows: {rows['used']}",
        f"- Excluded rows: {rows['excluded']}",
        f"- Corrupt rows: {rows['corrupt']}",
        f"- Missing required rows: {rows['missing_required']}",
        f"- Episodes: {eps['total']}",
        f"- Episodes by outcome: `{eps['by_outcome']}`",
        f"- Episode length avg/min/max: {eps['length_avg']:.2f} / {eps['length_min']} / {eps['length_max']}",
        "",
        "## Schema Checks",
        "",
        f"- ACE candidate count distribution: `{schema['ace_candidate_count']}`",
        f"- Main chunk shape distribution: `{schema['main_chunk_shape']}`",
        f"- Executed action shape distribution: `{schema['executed_action_shape']}`",
        f"- ACE replay violations: {schema['ace_replay_violations']}",
        f"- First-action mismatches: {schema['first_action_mismatches']} / {schema['first_action_checked']}",
        f"- Unique main seeds: {schema['unique_main_seeds']}",
        f"- Duplicate main seeds: {schema['duplicate_main_seeds']}",
        f"- Unique ACE seeds: {schema['unique_ace_seeds']}",
        f"- Duplicate ACE seeds: {schema['duplicate_ace_seeds']}",
        "",
        "## Splits",
        "",
        f"- Episodes by split: `{eps['by_split']}`",
    ]
    if train_summary is not None:
        lines += [
            "",
            "## Train/Eval",
            "",
            f"- RND thresholds: `{train_summary['rnd_thresholds']}`",
            f"- ACE thresholds: `{train_summary['ace_thresholds']}`",
            "",
            "| Split | Rows | RND q95 alarm % | ACE q95 alarm % | FIPER q95 alarm % |",
            "|---|---:|---:|---:|---:|",
        ]
        for split, info in sorted(train_summary["splits"].items()):
            rnd_q95 = info["rnd_alarm_rates"]["q95"]
            ace_q95 = info["ace_alarm_rates"]["q95"]
            fiper_q95 = info["quadrants_q95"].get("fiper_alarm")
            lines.append(
                f"| `{split}` | {info['rows']} | "
                f"{rnd_q95 if rnd_q95 is not None else 'NA'} | "
                f"{ace_q95 if ace_q95 is not None else 'NA'} | "
                f"{fiper_q95 if fiper_q95 is not None else 'NA'} |"
            )
    else:
        lines += [
            "",
            "Train/eval was not run. Re-run with `--run-train-eval` after freezing data.",
        ]

    (output_dir / "CURRENT_FIPER_SWEEP_ANALYSIS_REPORT.md").write_text("\n".join(lines) + "\n")


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=None)
    parser.add_argument("--input-root", type=Path, action="append", default=[])
    parser.add_argument("--input-jsonl", type=Path, action="append", default=[])
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--exclude-suite-task", type=parse_suite_task, action="append", default=[])
    parser.add_argument("--holdout-suite", action="append", default=[])
    parser.add_argument("--holdout-group", action="append", default=[])
    parser.add_argument("--holdout-task", type=parse_suite_task, action="append", default=[])
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--train-fraction", type=float, default=0.70)
    parser.add_argument("--calib-fraction", type=float, default=0.15)
    parser.add_argument("--run-train-eval", action="store_true")
    parser.add_argument("--epochs", type=int, default=80)
    parser.add_argument("--batch-size", type=int, default=256)
    return parser


def main() -> None:
    args = build_arg_parser().parse_args()
    config = load_config(args.config)

    excluded = set(args.exclude_suite_task)
    for item in config.get("excluded_suite_tasks", []):
        excluded.add((item["suite"], int(item["task_id"])))

    input_roots = list(args.input_root)
    if not input_roots and config:
        roots_list = config.get("input_roots")
        if roots_list:
            for r in roots_list:
                input_roots.append(Path(r))
        else:
            for node in ("sam", "bob"):
                root = config.get(node, {}).get("campaign_root")
                if root:
                    input_roots.append(Path(root))

    paths = discover_jsonls(input_roots, args.input_jsonl)
    if not paths:
        raise SystemExit("No fiper_receding_samples.jsonl files found.")

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    output_dir = args.output_dir or Path("experiments") / f"current_fiper_sweep_analysis_{timestamp}"
    output_dir.mkdir(parents=True, exist_ok=True)

    episodes, stats = audit_dataset(paths, excluded)
    split_by_episode = assign_splits(
        episodes=episodes,
        seed=args.seed,
        train_fraction=args.train_fraction,
        calib_fraction=args.calib_fraction,
        holdout_suites=set(args.holdout_suite),
        holdout_groups=set(args.holdout_group),
        holdout_tasks=set(args.holdout_task),
    )
    save_episode_manifest(output_dir, episodes, split_by_episode)
    summary = jsonable_stats(stats, episodes, split_by_episode)
    with (output_dir / "dataset_audit_summary.json").open("w") as f:
        json.dump(summary, f, indent=2)

    train_summary = None
    if args.run_train_eval:
        features = collect_features(paths, excluded, split_by_episode)
        train_summary = run_train_eval(features, output_dir, seed=args.seed, epochs=args.epochs, batch_size=args.batch_size)

    write_markdown_report(output_dir, summary, train_summary, paths)
    print(f"Wrote analysis outputs to {output_dir}")


if __name__ == "__main__":
    main()

