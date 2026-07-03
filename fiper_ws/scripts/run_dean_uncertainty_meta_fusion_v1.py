#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any

import numpy as np
import torch
from torch import nn

import run_dean_uncertainty_transformer_exploration_v2 as v2


CANONICAL_SPLITS = {
    "all_tasks_full": {
        "trained_dir": "/home/dean/fiper_uncertainty_collection/experiments/dean_all_tasks_full_uncertainty_test_20260601",
        "split_name": "all_tasks_random",
        "eval_success": "success_test_seen",
        "eval_failure": "failure_test_seen",
    },
    "ood_last2_taskids_full": {
        "trained_dir": "/home/dean/fiper_uncertainty_collection/experiments/dean_ood_last2_taskids_full_v1_20260601",
        "split_name": "ood_last2_taskids_full",
        "eval_success": "success_test_ood",
        "eval_failure": "failure_eval_ood",
    },
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True, default=str) + "\n")


def np_stats(obj: dict[str, dict[str, list[float]]]) -> dict[str, dict[str, np.ndarray]]:
    return {k: {kk: np.asarray(vv, dtype=np.float32) for kk, vv in val.items()} for k, val in obj.items()}


def logit_np(x: np.ndarray) -> np.ndarray:
    x = np.clip(x, 1e-5, 1.0 - 1e-5)
    return np.log(x / (1.0 - x)).astype(np.float32)


def make_meta_features(base_scores: np.ndarray, unc_scores: np.ndarray) -> np.ndarray:
    b = np.asarray(base_scores, dtype=np.float32)
    u = np.asarray(unc_scores, dtype=np.float32)
    lb = logit_np(b)
    lu = logit_np(u)
    return np.stack(
        [
            lb,
            lu,
            np.maximum(lb, lu),
            np.minimum(lb, lu),
            lb - lu,
            np.abs(lb - lu),
            b,
            u,
            b * u,
        ],
        axis=1,
    ).astype(np.float32)


class MetaLogReg(nn.Module):
    def __init__(self, in_dim: int) -> None:
        super().__init__()
        self.net = nn.Linear(in_dim, 1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x).squeeze(-1)


def fit_meta_model(
    x_raw: np.ndarray,
    y_raw: np.ndarray,
    seed: int,
    max_epochs: int,
    lr: float,
    weight_decay: float,
) -> tuple[MetaLogReg, dict[str, np.ndarray], list[dict[str, float]]]:
    rng = np.random.default_rng(seed)
    order = rng.permutation(len(y_raw))
    x_raw = x_raw[order]
    y_raw = y_raw[order].astype(np.float32)

    mean = x_raw.mean(axis=0)
    std = x_raw.std(axis=0)
    std = np.where(std < 1e-5, 1.0, std)
    x = np.clip((x_raw - mean) / std, -10.0, 10.0).astype(np.float32)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = MetaLogReg(x.shape[1]).to(device)
    xt = torch.tensor(x, dtype=torch.float32, device=device)
    yt = torch.tensor(y_raw, dtype=torch.float32, device=device)
    neg = float(np.sum(y_raw == 0))
    pos = float(np.sum(y_raw == 1))
    pos_weight = torch.tensor([max(1.0, neg / max(1.0, pos))], dtype=torch.float32, device=device)
    loss_fn = nn.BCEWithLogitsLoss(pos_weight=pos_weight)
    opt = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=weight_decay)

    history: list[dict[str, float]] = []
    best_state = None
    best_loss = float("inf")
    no_improve = 0
    for epoch in range(1, max_epochs + 1):
        model.train()
        opt.zero_grad(set_to_none=True)
        logits = model(xt)
        loss = loss_fn(logits, yt)
        loss.backward()
        opt.step()
        loss_v = float(loss.detach().cpu().item())
        with torch.no_grad():
            scores = torch.sigmoid(model(xt)).detach().cpu().numpy()
        auc = v2.auroc_binary(y_raw, scores)
        history.append({"epoch": epoch, "loss": loss_v, "auc": auc})
        if loss_v < best_loss - 1e-5:
            best_loss = loss_v
            best_state = {k: v.detach().cpu().clone() for k, v in model.state_dict().items()}
            no_improve = 0
        else:
            no_improve += 1
            if no_improve >= 30:
                break
    if best_state is not None:
        model.load_state_dict(best_state)
    return model, {"mean": mean.astype(np.float32), "std": std.astype(np.float32)}, history


def predict_meta(model: MetaLogReg, stats: dict[str, np.ndarray], x_raw: np.ndarray, batch_size: int) -> np.ndarray:
    device = next(model.parameters()).device
    x = np.clip((x_raw - stats["mean"]) / stats["std"], -10.0, 10.0).astype(np.float32)
    out = []
    model.eval()
    with torch.no_grad():
        for start in range(0, len(x), batch_size):
            xt = torch.tensor(x[start : start + batch_size], dtype=torch.float32, device=device)
            out.append(torch.sigmoid(model(xt)).detach().cpu().numpy())
    return np.concatenate(out, axis=0).astype(np.float32) if out else np.zeros((0,), dtype=np.float32)


def load_seq_model(job_dir: Path, cfg: dict[str, Any], device: torch.device):
    stats = np_stats(load_json(job_dir / "normalization.json"))
    model = v2.SeqRiskModel(
        hist_dim=int(stats["history"]["mean"].shape[0]),
        action_dim=int(stats["action"]["mean"].shape[0]),
        static_dim=int(stats["static"]["mean"].shape[0]),
        width=int(cfg["width"]),
        layers=int(cfg["layers"]),
        heads=int(cfg["heads"]),
        dropout=float(cfg["dropout"]),
    ).to(device)
    model.load_state_dict(torch.load(job_dir / "model.pt", map_location=device))
    model.eval()
    return model, stats


def evaluate_canonical(name: str, args: argparse.Namespace, episodes: dict[str, v2.EpisodeMeta]) -> dict[str, Any]:
    spec = CANONICAL_SPLITS[name]
    trained_dir = Path(spec["trained_dir"])
    split_name = spec["split_name"]
    cfg = load_json(trained_dir / "run_config.json")
    buckets = {k: set(v) for k, v in load_json(trained_dir / split_name / "episode_buckets.json").items()}
    rows_by_bucket = v2.build_rows_for_split(Path(args.run_root), episodes, buckets, int(cfg["history_steps"]))

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    base_model, base_stats = load_seq_model(trained_dir / split_name / "base", cfg, device)
    unc_model, unc_stats = load_seq_model(trained_dir / split_name / "unc_raw", cfg, device)

    score_pack: dict[str, dict[str, Any]] = {}
    for bucket, rows in rows_by_bucket.items():
        bs, labels, ids, ts = v2.score_rows(base_model, base_stats, rows, "base", args.batch_size, device)
        us, labels2, ids2, ts2 = v2.score_rows(unc_model, unc_stats, rows, "unc_raw", args.batch_size, device)
        if ids != ids2 or not np.array_equal(ts, ts2) or not np.array_equal(labels, labels2):
            raise RuntimeError(f"score alignment mismatch for {name}/{bucket}")
        score_pack[bucket] = {
            "base": bs,
            "unc": us,
            "labels": labels,
            "ids": ids,
            "ts": ts,
        }

    meta_train_buckets = ["success_val_seen", "failure_val_seen"]
    train_x = np.concatenate([make_meta_features(score_pack[b]["base"], score_pack[b]["unc"]) for b in meta_train_buckets], axis=0)
    train_y = np.concatenate([score_pack[b]["labels"] for b in meta_train_buckets], axis=0)
    meta_model, meta_stats, history = fit_meta_model(train_x, train_y, args.seed, args.meta_epochs, args.meta_lr, args.meta_weight_decay)

    meta_scores_by_bucket: dict[str, np.ndarray] = {}
    ids_by_bucket: dict[str, list[str]] = {}
    ts_by_bucket: dict[str, np.ndarray] = {}
    for bucket, pack in score_pack.items():
        x = make_meta_features(pack["base"], pack["unc"])
        meta_scores_by_bucket[bucket] = predict_meta(meta_model, meta_stats, x, args.batch_size)
        ids_by_bucket[bucket] = pack["ids"]
        ts_by_bucket[bucket] = pack["ts"]

    thresholds = v2.calibrate_thresholds(meta_scores_by_bucket, ids_by_bucket, args.alpha, args.min_conformal_mass)
    metrics_by_bucket = {
        bucket: v2.evaluate_bucket(bucket, rows_by_bucket[bucket], meta_scores_by_bucket[bucket], ids_by_bucket[bucket], ts_by_bucket[bucket], episodes, thresholds)
        for bucket in rows_by_bucket
    }

    success_eval = spec["eval_success"]
    failure_eval = spec["eval_failure"]
    result = {
        "canonical_split": name,
        "source_split": split_name,
        "policy": "meta_logreg_base_unc_raw_v1",
        "thresholds": thresholds,
        "meta_history": history,
        "bucket_counts": {k: {"episodes": len(set(r.episode_id for r in rows)), "rows": len(rows)} for k, rows in rows_by_bucket.items()},
        "metrics_by_bucket": metrics_by_bucket,
        "summary": {
            "success_eval_bucket": success_eval,
            "failure_eval_bucket": failure_eval,
            "success_fa": metrics_by_bucket[success_eval].get("success_false_alarm_rate"),
            "failure_detection": metrics_by_bucket[failure_eval].get("failure_detection_rate"),
            "failure_det_at_25": metrics_by_bucket[failure_eval].get("det_at_25"),
            "failure_det_at_50": metrics_by_bucket[failure_eval].get("det_at_50"),
            "failure_mean_detection_time": metrics_by_bucket[failure_eval].get("mean_detection_time"),
        },
    }
    return result


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--run-root", default="/home/dean/fiper_uncertainty_collection/runs/dean_object_uncertainty_20260529")
    p.add_argument("--output-dir", default="/home/dean/fiper_uncertainty_collection/experiments/dean_uncertainty_meta_fusion_v1_20260601")
    p.add_argument("--splits", nargs="+", default=["all_tasks_full", "ood_last2_taskids_full"])
    p.add_argument("--batch-size", type=int, default=512)
    p.add_argument("--alpha", type=float, default=0.15)
    p.add_argument("--min-conformal-mass", type=float, default=0.15)
    p.add_argument("--meta-epochs", type=int, default=400)
    p.add_argument("--meta-lr", type=float, default=3e-3)
    p.add_argument("--meta-weight-decay", type=float, default=5e-3)
    p.add_argument("--seed", type=int, default=20260601)
    args = p.parse_args()

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    episodes = v2.load_episode_meta(Path(args.run_root))
    results = []
    for split in args.splits:
        print(f"=== META FUSION {split} ===", flush=True)
        result = evaluate_canonical(split, args, episodes)
        results.append(result)
        write_json(out_dir / split / "metrics.json", result)
        print(json.dumps(result["summary"], sort_keys=True), flush=True)

    csv_path = out_dir / "dean_uncertainty_meta_fusion_results.csv"
    fields = [
        "canonical_split",
        "policy",
        "success_fa",
        "failure_detection",
        "failure_det_at_25",
        "failure_det_at_50",
        "failure_mean_detection_time",
        "q95",
        "q99",
        "conformal_mass",
    ]
    with csv_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for r in results:
            row = {
                "canonical_split": r["canonical_split"],
                "policy": r["policy"],
                **r["summary"],
                "q95": r["thresholds"]["q95"],
                "q99": r["thresholds"]["q99"],
                "conformal_mass": r["thresholds"]["conformal_mass"],
            }
            row.pop("success_eval_bucket", None)
            row.pop("failure_eval_bucket", None)
            writer.writerow(row)
    write_json(out_dir / "run_config.json", vars(args))
    print(f"Wrote {csv_path}", flush=True)


if __name__ == "__main__":
    main()
