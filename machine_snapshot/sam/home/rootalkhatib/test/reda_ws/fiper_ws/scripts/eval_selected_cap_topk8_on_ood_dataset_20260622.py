#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import time
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import torch
import torch.nn as nn
from sklearn.metrics import accuracy_score, average_precision_score, f1_score, roc_auc_score
from torch.utils.data import DataLoader, Dataset


TOPK8_DIMS = [6, 21, 25, 27, 23, 2, 26, 24]
K_HISTORY = 16


def read_jsonl(path: Path):
    with path.open() as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if line:
                yield line_no, json.loads(line)


def pad_flat(value: Any, dim: int) -> np.ndarray:
    arr = np.asarray(value if value is not None else [], dtype=np.float32).reshape(-1)
    out = np.zeros(dim, dtype=np.float32)
    n = min(dim, arr.size)
    if n:
        out[:n] = arr[:n]
    return out


def pad_seq(value: Any, steps: int = 10, dim: int = 7) -> np.ndarray:
    arr = np.asarray(value if value is not None else [], dtype=np.float32)
    out = np.zeros((steps, dim), dtype=np.float32)
    if arr.ndim == 1:
        arr = arr.reshape(-1, dim) if arr.size % dim == 0 else arr.reshape(1, -1)
    if arr.ndim == 2:
        s = min(steps, arr.shape[0])
        d = min(dim, arr.shape[1])
        out[:s, :d] = arr[:s, :d]
    return out


def compute_ace_metrics(candidates: Any) -> np.ndarray:
    chunks = np.asarray(candidates if candidates is not None else [], dtype=np.float32)
    if chunks.ndim != 3 or chunks.shape[0] < 2:
        return np.zeros(7, dtype=np.float32)
    n_seeds = chunks.shape[0]
    flat = chunks.reshape(n_seeds, -1)
    cov = np.cov(flat, rowvar=False)
    eps = 1e-6
    _sign, logdet = np.linalg.slogdet(cov + eps * np.eye(flat.shape[1]))
    entropy = 0.5 * (flat.shape[1] * (1.0 + np.log(2 * np.pi)) + logdet)
    diffs = flat[:, None, :] - flat[None, :, :]
    dists = np.sqrt(np.sum(diffs * diffs, axis=-1))
    mean_pairwise = np.sum(dists) / (n_seeds * (n_seeds - 1))
    per_step_std = float(np.mean(np.std(chunks, axis=0)))
    trans_std = float(np.mean(np.std(chunks[:, :, :3], axis=0)))
    rot_std = float(np.mean(np.std(chunks[:, :, 3:6], axis=0)))
    grip_std = float(np.mean(np.std(chunks[:, :, 6:], axis=0)))
    flat_std = float(np.mean(np.std(flat, axis=0)))
    out = np.asarray([entropy, mean_pairwise, per_step_std, trans_std, rot_std, grip_std, flat_std], dtype=np.float32)
    return np.nan_to_num(out, nan=0.0, posinf=0.0, neginf=0.0).astype(np.float32)


def action_stats(action: np.ndarray) -> np.ndarray:
    return np.concatenate([action[0], action.mean(axis=0), action.std(axis=0), action[-1] - action[0]]).astype(np.float32)


def selected_unc(row: dict[str, Any]) -> np.ndarray:
    vals = pad_flat(row.get("simvla_uncertainty_49d"), 49)
    return vals[TOPK8_DIMS].astype(np.float32)


def current_proprio(row: dict[str, Any]) -> np.ndarray:
    return pad_flat((row.get("current") or {}).get("proprio"), 8)


@dataclass
class FeatRow:
    episode_id: str
    suite: str
    task_id: int
    timestep: int
    y: float
    history: np.ndarray
    action: np.ndarray
    static: np.ndarray


def find_dataset_files(dataset_root: Path) -> tuple[Path, Path]:
    candidates = [
        (dataset_root / "worker_0" / "fiper_receding_samples.jsonl", dataset_root / "worker_0" / "episode_summaries.jsonl"),
        (dataset_root / "fiper_receding_samples.jsonl", dataset_root / "episode_summaries.jsonl"),
        (dataset_root / "worker_0" / "query_samples.jsonl", dataset_root / "worker_0" / "episode_summaries.jsonl"),
        (dataset_root / "query_samples.jsonl", dataset_root / "episode_summaries.jsonl"),
    ]
    for rows, summaries in candidates:
        if rows.exists() and summaries.exists():
            return rows, summaries
    raise FileNotFoundError(f"could not find dataset JSONL files under {dataset_root}")


def load_episode_labels(summary_path: Path) -> dict[str, float]:
    labels: dict[str, float] = {}
    for _, row in read_jsonl(summary_path):
        eid = str(row.get("episode_id") or row.get("episode_uid"))
        labels[eid] = 0.0 if bool(row.get("success")) else 1.0
    return labels


def load_rows(rows_path: Path, summary_path: Path) -> list[FeatRow]:
    labels = load_episode_labels(summary_path)
    rows: list[FeatRow] = []
    hist_by_ep: dict[str, deque[tuple[np.ndarray, np.ndarray, np.ndarray]]] = defaultdict(lambda: deque(maxlen=K_HISTORY))
    for line_no, row in read_jsonl(rows_path):
        eid = str(row.get("episode_id") or row.get("episode_uid"))
        if eid not in labels:
            continue
        proprio = current_proprio(row)
        executed = pad_flat(row.get("executed_action"), 7)
        ace = compute_ace_metrics(row.get("ace_candidate_chunks_normalized"))
        action = pad_seq(row.get("main_candidate_action_chunk_normalized"), 10, 7)
        static = np.concatenate([action_stats(action), ace, proprio, selected_unc(row)]).astype(np.float32)
        hist = np.zeros((K_HISTORY, 21), dtype=np.float32)
        past = list(hist_by_ep[eid])
        offset = K_HISTORY - len(past)
        for i, (hp, ha, hace) in enumerate(past):
            hist[offset + i] = np.concatenate([hp, ha, hace[:6]]).astype(np.float32)
        rows.append(FeatRow(eid, str(row.get("suite", "")), int(row.get("task_id", -1)), int(row.get("timestep", 0)), labels[eid], hist, action, static))
        hist_by_ep[eid].append((proprio, executed, ace))
        if line_no % 100000 == 0:
            print(f"[load] line={line_no} rows={len(rows)}", flush=True)
    return rows


def arrays(rows: list[FeatRow]):
    return (
        np.stack([r.history for r in rows]).astype(np.float32),
        np.stack([r.action for r in rows]).astype(np.float32),
        np.stack([r.static for r in rows]).astype(np.float32),
        np.asarray([r.y for r in rows], dtype=np.float32),
    )


def load_stats(path: Path) -> dict[str, dict[str, np.ndarray]]:
    raw = json.loads(path.read_text())
    return {k: {kk: np.asarray(vv, dtype=np.float32) for kk, vv in val.items()} for k, val in raw.items()}


def apply_std(x: np.ndarray, stats: dict[str, np.ndarray]) -> np.ndarray:
    mean = stats["mean"]
    std = np.maximum(stats["std"], 1e-6)
    return ((x - mean) / std).astype(np.float32)


class SeqDataset(Dataset):
    def __init__(self, h, a, st):
        self.h = torch.as_tensor(h, dtype=torch.float32)
        self.a = torch.as_tensor(a, dtype=torch.float32)
        self.st = torch.as_tensor(st, dtype=torch.float32)

    def __len__(self):
        return int(self.h.shape[0])

    def __getitem__(self, idx):
        return {"history": self.h[idx], "action": self.a[idx], "static": self.st[idx]}


class SeqRiskModel(nn.Module):
    def __init__(self, hist_dim=21, action_dim=7, static_dim=51, width=128, layers=3, heads=4, dropout=0.1):
        super().__init__()
        self.hist_proj = nn.Linear(hist_dim, width)
        self.action_proj = nn.Linear(action_dim, width)
        layer = nn.TransformerEncoderLayer(width, heads, width * 4, dropout=dropout, batch_first=True, activation="gelu")
        self.cls = nn.Parameter(torch.zeros(1, 1, width))
        self.pos = nn.Parameter(torch.randn(1, 64, width) * 0.02)
        self.seq = nn.TransformerEncoder(layer, layers)
        self.static = nn.Sequential(nn.Linear(static_dim, width), nn.GELU())
        self.head = nn.Sequential(nn.LayerNorm(width * 2), nn.Linear(width * 2, width), nn.GELU(), nn.Dropout(dropout), nn.Linear(width, 1))

    def forward(self, batch):
        tokens = torch.cat([self.hist_proj(batch["history"]), self.action_proj(batch["action"])], dim=1)
        b = tokens.shape[0]
        tokens = torch.cat([self.cls.expand(b, -1, -1), tokens], dim=1)
        seq = self.seq(tokens + self.pos[:, : tokens.shape[1]])[:, 0]
        static = self.static(batch["static"])
        return self.head(torch.cat([seq, static], dim=-1)).squeeze(-1)


def predict(model: nn.Module, h: np.ndarray, a: np.ndarray, st: np.ndarray, device: torch.device, batch_size: int) -> np.ndarray:
    loader = DataLoader(SeqDataset(h, a, st), batch_size=batch_size, shuffle=False)
    out = []
    model.eval()
    with torch.no_grad():
        for batch in loader:
            batch = {k: v.to(device) for k, v in batch.items()}
            out.append(torch.sigmoid(model(batch)).detach().cpu().numpy())
    return np.concatenate(out).astype(np.float32)


def step_metrics(y: np.ndarray, scores: np.ndarray, threshold: float) -> dict[str, Any]:
    pred = (scores >= threshold).astype(np.int32)
    yb = y.astype(np.int32)
    tp = int(((pred == 1) & (yb == 1)).sum())
    tn = int(((pred == 0) & (yb == 0)).sum())
    fp = int(((pred == 1) & (yb == 0)).sum())
    fn = int(((pred == 0) & (yb == 1)).sum())
    return {
        "auroc": float(roc_auc_score(yb, scores)) if len(set(yb.tolist())) == 2 else 0.5,
        "auprc": float(average_precision_score(yb, scores)) if len(set(yb.tolist())) == 2 else float(yb.mean() if len(yb) else 0.0),
        "f1": float(f1_score(yb, pred, zero_division=0)),
        "accuracy": float(accuracy_score(yb, pred)) if len(yb) else 0.0,
        "fpr": float(fp / max(1, fp + tn)),
        "fnr": float(fn / max(1, fn + tp)),
        "tp": tp,
        "tn": tn,
        "fp": fp,
        "fn": fn,
    }


def episode_metrics_any_row(rows: list[FeatRow], scores: np.ndarray, threshold: float) -> dict[str, Any]:
    by_ep: dict[str, list[tuple[FeatRow, float]]] = defaultdict(list)
    for r, s in zip(rows, scores):
        by_ep[r.episode_id].append((r, float(s)))
    succ_eps = fail_eps = false_alarm = detected = det10 = det25 = det50 = 0
    det_fracs = []
    task_counts: dict[int, Counter[str]] = defaultdict(Counter)
    for eid, vals in by_ep.items():
        vals.sort(key=lambda x: x[0].timestep)
        y = max(v[0].y for v in vals)
        task_id = vals[0][0].task_id
        hit_positions = [i for i, (_, s) in enumerate(vals) if s >= threshold]
        n = len(vals)
        if y >= 0.5:
            fail_eps += 1
            task_counts[task_id]["failure"] += 1
            if hit_positions:
                detected += 1
                task_counts[task_id]["detected_failure"] += 1
                frac = (hit_positions[0] + 1) / max(1, n)
                det_fracs.append(frac)
                if frac <= 0.10:
                    det10 += 1
                if frac <= 0.25:
                    det25 += 1
                if frac <= 0.50:
                    det50 += 1
        else:
            succ_eps += 1
            task_counts[task_id]["success"] += 1
            if hit_positions:
                false_alarm += 1
                task_counts[task_id]["false_alarm"] += 1
    per_task = {
        str(t): {
            "success_episodes": int(c["success"]),
            "failure_episodes": int(c["failure"]),
            "false_alarm_rate": float(c["false_alarm"] / max(1, c["success"])),
            "failure_detection_rate": float(c["detected_failure"] / max(1, c["failure"])),
        }
        for t, c in sorted(task_counts.items())
    }
    return {
        "episodes": len(by_ep),
        "success_episodes": succ_eps,
        "failure_episodes": fail_eps,
        "episode_false_alarm_rate": false_alarm / max(1, succ_eps),
        "failure_detection_rate": detected / max(1, fail_eps),
        "det_at_10": det10 / max(1, fail_eps),
        "det_at_25": det25 / max(1, fail_eps),
        "det_at_50": det50 / max(1, fail_eps),
        "mean_detection_fraction": float(np.mean(det_fracs)) if det_fracs else None,
        "false_alarm_count": false_alarm,
        "detected_failure_count": detected,
        "per_task": per_task,
    }


def episode_metrics_conformal_mass(rows: list[FeatRow], scores: np.ndarray, q95: float, mass_threshold: float) -> dict[str, Any]:
    by_ep: dict[str, list[tuple[FeatRow, float]]] = defaultdict(list)
    for r, s in zip(rows, scores):
        by_ep[r.episode_id].append((r, float(s)))
    succ_eps = fail_eps = false_alarm = detected = det10 = det25 = det50 = 0
    det_fracs = []
    final_masses = []
    task_counts: dict[int, Counter[str]] = defaultdict(Counter)
    for eid, vals in by_ep.items():
        vals.sort(key=lambda x: x[0].timestep)
        y = max(v[0].y for v in vals)
        task_id = vals[0][0].task_id
        mass = 0.0
        first_alarm_idx = None
        first_alarm_timestep = None
        for i, (r, s) in enumerate(vals):
            mass += max(0.0, float(s) - float(q95))
            if first_alarm_idx is None and mass >= float(mass_threshold):
                first_alarm_idx = i
                first_alarm_timestep = int(r.timestep)
        final_masses.append(float(mass))
        n = len(vals)
        if y >= 0.5:
            fail_eps += 1
            task_counts[task_id]["failure"] += 1
            if first_alarm_idx is not None:
                detected += 1
                task_counts[task_id]["detected_failure"] += 1
                frac = (first_alarm_idx + 1) / max(1, n)
                timestep_frac = (first_alarm_timestep or 0) / max(1, vals[-1][0].timestep if vals else n)
                det_fracs.append(timestep_frac)
                if frac <= 0.10:
                    det10 += 1
                if frac <= 0.25:
                    det25 += 1
                if frac <= 0.50:
                    det50 += 1
        else:
            succ_eps += 1
            task_counts[task_id]["success"] += 1
            if first_alarm_idx is not None:
                false_alarm += 1
                task_counts[task_id]["false_alarm"] += 1
    per_task = {
        str(t): {
            "success_episodes": int(c["success"]),
            "failure_episodes": int(c["failure"]),
            "false_alarm_rate": float(c["false_alarm"] / max(1, c["success"])),
            "failure_detection_rate": float(c["detected_failure"] / max(1, c["failure"])),
        }
        for t, c in sorted(task_counts.items())
    }
    return {
        "episodes": len(by_ep),
        "success_episodes": succ_eps,
        "failure_episodes": fail_eps,
        "episode_false_alarm_rate": false_alarm / max(1, succ_eps),
        "failure_detection_rate": detected / max(1, fail_eps),
        "det_at_10": det10 / max(1, fail_eps),
        "det_at_25": det25 / max(1, fail_eps),
        "det_at_50": det50 / max(1, fail_eps),
        "mean_detection_fraction": float(np.mean(det_fracs)) if det_fracs else None,
        "mean_final_mass": float(np.mean(final_masses)) if final_masses else None,
        "false_alarm_count": false_alarm,
        "detected_failure_count": detected,
        "q95_row_threshold": float(q95),
        "conformal_mass_threshold": float(mass_threshold),
        "per_task": per_task,
    }


def summarize_rows(rows: list[FeatRow]) -> dict[str, Any]:
    eps: dict[str, float] = {}
    tasks = Counter()
    for r in rows:
        eps[r.episode_id] = max(eps.get(r.episode_id, 0.0), r.y)
        tasks[r.task_id] += 1
    failures = sum(1 for y in eps.values() if y >= 0.5)
    return {"rows": len(rows), "episodes": len(eps), "success_episodes": len(eps) - failures, "failure_episodes": failures, "row_task_counts": dict(sorted(tasks.items()))}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset-root", required=True)
    ap.add_argument("--risk-model-dir", required=True)
    ap.add_argument("--output-root", required=True)
    ap.add_argument("--batch-size", type=int, default=2048)
    args = ap.parse_args()

    started = time.time()
    dataset_root = Path(args.dataset_root)
    risk_model_dir = Path(args.risk_model_dir)
    out = Path(args.output_root)
    out.mkdir(parents=True, exist_ok=True)

    rows_path, summaries_path = find_dataset_files(dataset_root)
    rows = load_rows(rows_path, summaries_path)
    if not rows:
        raise RuntimeError("no rows loaded from dataset")
    h_raw, a_raw, st_raw, y = arrays(rows)
    stats = load_stats(risk_model_dir / "normalization.json")
    h = apply_std(h_raw, stats["history"])
    a = apply_std(a_raw, stats["action"])
    st = apply_std(st_raw, stats["static"])

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = SeqRiskModel(static_dim=st.shape[-1]).to(device)
    state = torch.load(risk_model_dir / "model.pt", map_location="cpu")
    model.load_state_dict(state)
    scores = predict(model, h, a, st, device, args.batch_size)

    thresholds = {"fixed_0.3_online_gate": 0.3, "fixed_0.5": 0.5}
    threshold_path = risk_model_dir / "thresholds.json"
    if threshold_path.exists():
        for k, v in json.loads(threshold_path.read_text()).items():
            if isinstance(v, (int, float)):
                thresholds[k] = float(v)

    results = {
        "experiment": "selected_cap_topk8_offline_on_libero_goal_object_ood_180ep_20260622",
        "dataset_root": str(dataset_root),
        "rows_path": str(rows_path),
        "summaries_path": str(summaries_path),
        "risk_model_dir": str(risk_model_dir),
        "feature_schema": {
            "history_dim": 21,
            "history_steps": 16,
            "action_shape": [10, 7],
            "static_dim": int(st.shape[-1]),
            "static_layout": "action_stats_28 + ace_7 + proprio_8 + selected_uncertainty_topk8_8",
            "selected_uncertainty_dims": TOPK8_DIMS,
            "explicit_task_id_input": False,
            "explicit_timestep_input": False,
        },
        "dataset_summary": summarize_rows(rows),
        "thresholds": thresholds,
        "metrics": {},
        "runtime_seconds": time.time() - started,
    }
    q95 = float(thresholds.get("q95", 0.95))
    mass_threshold = float(thresholds.get("conformal_mass", 0.15))
    results["metrics"]["score_q95_mass_conformal"] = {
        "step": step_metrics(y, scores, q95),
        "episode": episode_metrics_conformal_mass(rows, scores, q95, mass_threshold),
    }
    for name, th in thresholds.items():
        if name == "conformal_mass":
            continue
        results["metrics"][f"any_row_{name}"] = {"step": step_metrics(y, scores, th), "episode": episode_metrics_any_row(rows, scores, th)}

    (out / "results.json").write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    np.savez_compressed(out / "scores.npz", y=y, scores=scores)

    lines = [
        "# Selected-Cap TopK8 Offline Evaluation on LIBERO Goal-Object OOD",
        "",
        f"- Dataset root: `{dataset_root}`",
        f"- Risk model dir: `{risk_model_dir}`",
        f"- Rows: `{results['dataset_summary']['rows']}`",
        f"- Episodes: `{results['dataset_summary']['episodes']}`",
        f"- Success episodes: `{results['dataset_summary']['success_episodes']}`",
        f"- Failure episodes: `{results['dataset_summary']['failure_episodes']}`",
        f"- Runtime seconds: `{results['runtime_seconds']:.1f}`",
        "",
        "## Policy Metrics",
        "",
        "Primary policy is the historical selected-cap TopK8 offline policy: cumulative conformal risk mass above the q95 row threshold.",
        "",
        "| Threshold | Value | AUROC | AUPRC | Step FPR | Step FNR | Episode false alarm | Failure detection | Det@10 | Det@25 | Det@50 | Mean detection frac |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for name, m in results["metrics"].items():
        th = thresholds.get(name.replace("any_row_", ""), mass_threshold if name == "score_q95_mass_conformal" else float("nan"))
        m = results["metrics"][name]
        st_m = m["step"]
        ep_m = m["episode"]
        mean_det = ep_m["mean_detection_fraction"]
        lines.append(
            f"| {name} | {th:.4f} | {st_m['auroc']:.4f} | {st_m['auprc']:.4f} | {100*st_m['fpr']:.2f}% | {100*st_m['fnr']:.2f}% | "
            f"{100*ep_m['episode_false_alarm_rate']:.2f}% | {100*ep_m['failure_detection_rate']:.2f}% | {100*ep_m['det_at_10']:.2f}% | "
            f"{100*ep_m['det_at_25']:.2f}% | {100*ep_m['det_at_50']:.2f}% | {mean_det if mean_det is not None else 'NA'} |"
        )
    lines += [
        "",
        "## Legitimacy Notes",
        "",
        "- Dataset collection uses modified SimVLA with uncertainty head, not the risk-aware selected-cap policy.",
        "- This script only loads the selected-cap TopK8 detector after collection and scores rows offline.",
        "- Primary policy uses `mass_t += max(0, score_t - q95)` and alarms when mass reaches the saved conformal-mass threshold.",
        "- Inputs exclude explicit task id and explicit timestep.",
    ]
    report_path = out / "SELECTED_CAP_TOPK8_OFFLINE_LIBERO_GOAL_OBJECT_OOD_180EP_20260622.md"
    report_path.write_text("\n".join(lines) + "\n")
    print(f"DONE report={report_path}", flush=True)


if __name__ == "__main__":
    main()
