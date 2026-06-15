#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import random
from pathlib import Path
from typing import Any

import numpy as np
import torch
from torch import nn
from torch.utils.data import DataLoader

import run_dean_uncertainty_transformer_exploration_v2 as v2


CANONICAL_SPLITS = {
    "all_tasks_full": {
        "trained_dir": "/home/dean/fiper_uncertainty_collection/experiments/dean_all_tasks_full_uncertainty_test_20260601",
        "source_split": "all_tasks_random",
        "eval_success": "success_test_seen",
        "eval_failure": "failure_test_seen",
        "topk_job": "/home/dean/fiper_uncertainty_collection/experiments/dean_uncertainty_topk_feature_sweep_v1_20260602/all_tasks_full/unc_topk8",
        "rank_dir": "/home/dean/fiper_uncertainty_collection/experiments/dean_uncertainty_topk_feature_sweep_v1_20260602/all_tasks_full",
    },
    "ood_last2_taskids_full": {
        "trained_dir": "/home/dean/fiper_uncertainty_collection/experiments/dean_ood_last2_taskids_full_v1_20260601",
        "source_split": "ood_last2_taskids_full",
        "eval_success": "success_test_ood",
        "eval_failure": "failure_eval_ood",
        "topk_job": "/home/dean/fiper_uncertainty_collection/experiments/dean_uncertainty_topk_feature_sweep_v1_20260602/ood_last2_taskids_full/unc_topk8",
        "rank_dir": "/home/dean/fiper_uncertainty_collection/experiments/dean_uncertainty_topk_feature_sweep_v1_20260602/ood_last2_taskids_full",
    },
}


VARIANTS = [
    "unc_topk8_deep_static_v1",
    "unc_topk8_gated_static_v1",
    "unc_topk8_grouped_static_v1",
]

SELECTED_DIMS = np.asarray([], dtype=np.int64)
ORIGINAL_MAKE_ARRAYS = v2.make_arrays


def seed_everything(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True, default=str) + "\n")


def select_topk_dims(rank_dir: Path, topk: int) -> list[int]:
    metrics_path = rank_dir / f"unc_topk{topk}" / "metrics.json"
    if metrics_path.exists():
        metrics = load_json(metrics_path)
        dims = metrics.get("feature_selection", {}).get("selected_dims")
        if dims:
            return [int(d) for d in dims]
    ranking = load_json(rank_dir / "uncertainty_dim_ranking.json")
    return [int(r["dim"]) for r in ranking[:topk]]


def make_arrays_static_arch(rows: list[v2.RowEx], variant: str):
    if variant not in VARIANTS:
        return ORIGINAL_MAKE_ARRAYS(rows, variant)
    h = np.stack([r.history for r in rows], axis=0).astype(np.float32)
    a = np.stack([r.action for r in rows], axis=0).astype(np.float32)
    st = np.stack(
        [np.concatenate([r.static_base, r.uncertainty[SELECTED_DIMS]]).astype(np.float32) for r in rows],
        axis=0,
    )
    y = np.asarray([r.y for r in rows], dtype=np.float32)
    episode_ids = [r.episode_id for r in rows]
    timesteps = np.asarray([r.timestep for r in rows], dtype=np.int32)
    return h, a, st, y, episode_ids, timesteps


v2.make_arrays = make_arrays_static_arch


class StaticArchSeqRiskModel(nn.Module):
    def __init__(
        self,
        hist_dim: int,
        action_dim: int,
        static_dim: int,
        variant: str,
        width: int = 128,
        layers: int = 3,
        heads: int = 4,
        dropout: float = 0.1,
    ) -> None:
        super().__init__()
        if static_dim != 51:
            raise ValueError(f"expected static_dim=51 for topk8 static arch variants, got {static_dim}")
        self.variant = variant
        self.width = width
        self.hist_proj = nn.Linear(hist_dim, width)
        self.action_proj = nn.Linear(action_dim, width)
        enc_layer = nn.TransformerEncoderLayer(
            width,
            heads,
            width * 4,
            dropout=dropout,
            batch_first=True,
            activation="gelu",
        )
        self.cls = nn.Parameter(torch.zeros(1, 1, width))
        self.pos = nn.Parameter(torch.randn(1, 64, width) * 0.02)
        self.seq = nn.TransformerEncoder(enc_layer, layers)

        if variant in {"unc_topk8_deep_static_v1", "unc_topk8_gated_static_v1"}:
            self.static = nn.Sequential(
                nn.LayerNorm(static_dim),
                nn.Linear(static_dim, width),
                nn.GELU(),
                nn.Dropout(dropout),
                nn.Linear(width, width),
                nn.GELU(),
            )
        elif variant == "unc_topk8_grouped_static_v1":
            self.action_stats = nn.Sequential(nn.LayerNorm(28), nn.Linear(28, 48), nn.GELU())
            self.ace = nn.Sequential(nn.LayerNorm(7), nn.Linear(7, 24), nn.GELU())
            self.proprio = nn.Sequential(nn.LayerNorm(8), nn.Linear(8, 24), nn.GELU())
            self.unc = nn.Sequential(nn.LayerNorm(8), nn.Linear(8, 32), nn.GELU())
            self.static = nn.Sequential(
                nn.Linear(48 + 24 + 24 + 32, width),
                nn.GELU(),
                nn.Dropout(dropout),
                nn.Linear(width, width),
                nn.GELU(),
            )
        else:
            raise ValueError(f"unknown variant {variant}")

        if variant == "unc_topk8_gated_static_v1":
            self.gate = nn.Sequential(nn.LayerNorm(width), nn.Linear(width, width), nn.Sigmoid())
            self.head = nn.Sequential(
                nn.LayerNorm(width),
                nn.Linear(width, width),
                nn.GELU(),
                nn.Dropout(dropout),
                nn.Linear(width, 1),
            )
        else:
            self.head = nn.Sequential(
                nn.LayerNorm(width * 2),
                nn.Linear(width * 2, width),
                nn.GELU(),
                nn.Dropout(dropout),
                nn.Linear(width, 1),
            )

    def encode_static(self, st: torch.Tensor) -> torch.Tensor:
        if self.variant == "unc_topk8_grouped_static_v1":
            action_stats = st[:, :28]
            ace = st[:, 28:35]
            proprio = st[:, 35:43]
            unc = st[:, 43:51]
            return self.static(
                torch.cat(
                    [
                        self.action_stats(action_stats),
                        self.ace(ace),
                        self.proprio(proprio),
                        self.unc(unc),
                    ],
                    dim=-1,
                )
            )
        return self.static(st)

    def forward(self, batch: dict[str, torch.Tensor]) -> torch.Tensor:
        tokens = torch.cat([self.hist_proj(batch["history"]), self.action_proj(batch["action"])], dim=1)
        bsz = tokens.shape[0]
        tokens = torch.cat([self.cls.expand(bsz, -1, -1), tokens], dim=1)
        seq = self.seq(tokens + self.pos[:, : tokens.shape[1]])[:, 0]
        static = self.encode_static(batch["static"])
        if self.variant == "unc_topk8_gated_static_v1":
            gate = self.gate(static)
            return self.head(gate * seq + (1.0 - gate) * static).squeeze(-1)
        return self.head(torch.cat([seq, static], dim=-1)).squeeze(-1)


def train_model(
    train_rows: list[v2.RowEx],
    val_rows: list[v2.RowEx],
    variant: str,
    args: argparse.Namespace,
    device: torch.device,
) -> tuple[StaticArchSeqRiskModel, dict[str, dict[str, np.ndarray]], list[dict[str, Any]], int]:
    h_train_raw, a_train_raw, st_train_raw, y_train, _, _ = v2.make_arrays(train_rows, variant)
    h_val_raw, a_val_raw, st_val_raw, y_val, _, _ = v2.make_arrays(val_rows, variant)
    stats = {
        "history": v2.fit_seq_standardizer(h_train_raw),
        "action": v2.fit_seq_standardizer(a_train_raw),
        "static": v2.fit_standardizer(st_train_raw),
    }
    h_train = v2.apply_seq_standardizer(h_train_raw, stats["history"])
    a_train = v2.apply_seq_standardizer(a_train_raw, stats["action"])
    st_train = v2.apply_standardizer(st_train_raw, stats["static"])
    h_val = v2.apply_seq_standardizer(h_val_raw, stats["history"])
    a_val = v2.apply_seq_standardizer(a_val_raw, stats["action"])
    st_val = v2.apply_standardizer(st_val_raw, stats["static"])

    model = StaticArchSeqRiskModel(
        hist_dim=h_train.shape[-1],
        action_dim=a_train.shape[-1],
        static_dim=st_train.shape[-1],
        variant=variant,
        width=args.width,
        layers=args.layers,
        heads=args.heads,
        dropout=args.dropout,
    ).to(device)
    neg = float(np.sum(y_train == 0))
    pos = float(np.sum(y_train == 1))
    pos_weight = torch.tensor([max(1.0, neg / max(1.0, pos))], dtype=torch.float32, device=device)
    loss_fn = nn.BCEWithLogitsLoss(pos_weight=pos_weight)
    opt = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    train_loader = DataLoader(v2.SeqDataset(h_train, a_train, st_train, y_train), batch_size=args.batch_size, shuffle=True)
    val_loader = DataLoader(v2.SeqDataset(h_val, a_val, st_val, y_val), batch_size=args.batch_size, shuffle=False)

    best_state = None
    best_auc = -1.0
    best_epoch = 0
    no_improve = 0
    history: list[dict[str, Any]] = []
    for epoch in range(1, args.max_epochs + 1):
        model.train()
        losses = []
        for batch, yb in train_loader:
            batch = v2.move_batch(batch, device)
            yb = yb.to(device)
            opt.zero_grad(set_to_none=True)
            logits = model(batch)
            loss = loss_fn(logits, yb)
            loss.backward()
            nn.utils.clip_grad_norm_(model.parameters(), 5.0)
            opt.step()
            losses.append(float(loss.detach().cpu().item()))
        scores, labels = v2.predict_scores_from_loader(model, val_loader, device, want_labels=True)
        auc = v2.auroc_binary(labels, scores)
        val_loss = float(
            loss_fn(
                torch.logit(torch.tensor(np.clip(scores, 1e-6, 1 - 1e-6), device=device)),
                torch.tensor(labels, device=device),
            )
            .detach()
            .cpu()
            .item()
        )
        rec = {"epoch": epoch, "train_loss": float(np.mean(losses)), "val_auc": auc, "val_loss": val_loss}
        history.append(rec)
        print(f"epoch={epoch} variant={variant} train_loss={rec['train_loss']:.4f} val_auc={auc:.4f}", flush=True)
        if auc > best_auc + 1e-4:
            best_auc = auc
            best_epoch = epoch
            best_state = {k: v.detach().cpu().clone() for k, v in model.state_dict().items()}
            no_improve = 0
        else:
            no_improve += 1
            if no_improve >= args.patience:
                break
    if best_state is not None:
        model.load_state_dict(best_state)
    return model, stats, history, best_epoch


def score_rows(
    model: nn.Module,
    stats: dict[str, dict[str, np.ndarray]],
    rows: list[v2.RowEx],
    variant: str,
    batch_size: int,
    device: torch.device,
) -> tuple[np.ndarray, np.ndarray, list[str], np.ndarray]:
    if not rows:
        return np.zeros((0,), dtype=np.float32), np.zeros((0,), dtype=np.float32), [], np.zeros((0,), dtype=np.int32)
    h_raw, a_raw, st_raw, y, episode_ids, timesteps = v2.make_arrays(rows, variant)
    h = v2.apply_seq_standardizer(h_raw, stats["history"])
    a = v2.apply_seq_standardizer(a_raw, stats["action"])
    st = v2.apply_standardizer(st_raw, stats["static"])
    loader = DataLoader(v2.SeqDataset(h, a, st, None), batch_size=batch_size, shuffle=False)
    return v2.predict_scores_from_loader(model, loader, device), y, episode_ids, timesteps


def run_job(
    split_name: str,
    variant: str,
    rows_by_bucket: dict[str, list[v2.RowEx]],
    episodes: dict[str, v2.EpisodeMeta],
    args: argparse.Namespace,
    device: torch.device,
    out_dir: Path,
) -> dict[str, Any]:
    print(f"Training split={split_name} variant={variant}", flush=True)
    train_rows = rows_by_bucket["success_train_seen"] + rows_by_bucket["failure_train_seen"]
    val_rows = rows_by_bucket["success_val_seen"] + rows_by_bucket["failure_val_seen"]
    model, stats, history, best_epoch = train_model(train_rows, val_rows, variant, args, device)

    scores_by_bucket = {}
    ids_by_bucket = {}
    ts_by_bucket = {}
    for bucket, rows in rows_by_bucket.items():
        scores, _labels, ids, timesteps = score_rows(model, stats, rows, variant, args.batch_size, device)
        scores_by_bucket[bucket] = scores
        ids_by_bucket[bucket] = ids
        ts_by_bucket[bucket] = timesteps

    thresholds = v2.calibrate_thresholds(scores_by_bucket, ids_by_bucket, args.alpha, args.min_conformal_mass)
    metrics_by_bucket = {
        bucket: v2.evaluate_bucket(bucket, rows_by_bucket[bucket], scores_by_bucket[bucket], ids_by_bucket[bucket], ts_by_bucket[bucket], episodes, thresholds)
        for bucket in rows_by_bucket
    }

    job_dir = out_dir / split_name / variant
    job_dir.mkdir(parents=True, exist_ok=True)
    torch.save(model.state_dict(), job_dir / "model.pt")
    write_json(job_dir / "normalization.json", {k: {kk: vv.tolist() for kk, vv in v.items()} for k, v in stats.items()})
    write_json(job_dir / "thresholds.json", thresholds)
    write_json(job_dir / "history.json", history)
    result = {
        "split": split_name,
        "variant": variant,
        "best_epoch": best_epoch,
        "thresholds": thresholds,
        "bucket_counts": {k: {"episodes": len(set(r.episode_id for r in rows)), "rows": len(rows)} for k, rows in rows_by_bucket.items()},
        "metrics_by_bucket": metrics_by_bucket,
        "feature_audit": {
            "uses_reward": False,
            "uses_success": False,
            "uses_future_timestep": False,
            "uses_object_positions_before": False,
            "uses_task_metadata_as_input": False,
            "uses_ood_rows_for_train": False,
            "uses_test_rows_for_feature_selection": False,
            "uses_ood_rows_for_feature_selection": False,
            "input_fields": [
                "history.previous_proprio",
                "history.previous_executed_action",
                "history.previous_ace_metrics",
                "main_candidate_action_chunk_normalized.sequence_tokens",
                "main_candidate_action_chunk_normalized.stats",
                "ace_candidate_chunks_normalized.metrics",
                "current.proprio",
                "current.selected_uncertainty_top8",
            ],
            "architecture_change": variant,
            "selected_uncertainty_dims": SELECTED_DIMS.tolist(),
            "selected_uncertainty_dim_count": int(SELECTED_DIMS.size),
            "history_dim": 21,
            "static_dim": 51,
            "history_steps": args.history_steps,
        },
    }
    write_json(job_dir / "metrics.json", result)
    return result


def metrics_summary(result: dict[str, Any], spec: dict[str, str]) -> dict[str, Any]:
    metrics = result["metrics_by_bucket"]
    success_eval = spec["eval_success"]
    failure_eval = spec["eval_failure"]
    return {
        "success_fa": metrics[success_eval].get("success_false_alarm_rate"),
        "failure_detection": metrics[failure_eval].get("failure_detection_rate"),
        "failure_det_at_25": metrics[failure_eval].get("det_at_25"),
        "failure_det_at_50": metrics[failure_eval].get("det_at_50"),
        "failure_mean_detection_time": metrics[failure_eval].get("mean_detection_time"),
    }


def load_reference_rows() -> list[dict[str, Any]]:
    refs = []
    for split_key, spec in CANONICAL_SPLITS.items():
        csv_path = Path(spec["trained_dir"]) / "dean_uncertainty_comparison_results.csv"
        with csv_path.open() as f:
            for row in csv.DictReader(f):
                if row.get("variant") != "base":
                    continue
                refs.append(
                    {
                        "canonical_split": split_key,
                        "policy": "ref_base",
                        "best_epoch": row.get("best_epoch", ""),
                        "success_fa": row.get("seen_success_fa") if split_key == "all_tasks_full" else row.get("ood_success_fa"),
                        "failure_detection": row.get("seen_failure_detection") if split_key == "all_tasks_full" else row.get("ood_failure_detection"),
                        "failure_det_at_25": row.get("seen_failure_det_at_25") if split_key == "all_tasks_full" else row.get("ood_failure_det_at_25"),
                        "failure_det_at_50": row.get("seen_failure_det_at_50") if split_key == "all_tasks_full" else row.get("ood_failure_det_at_50"),
                        "failure_mean_detection_time": "",
                    }
                )
        topk_metrics = load_json(Path(spec["topk_job"]) / "metrics.json")
        refs.append(
            {
                "canonical_split": split_key,
                "policy": "ref_unc_topk8",
                "best_epoch": topk_metrics["best_epoch"],
                **metrics_summary(topk_metrics, spec),
            }
        )
    return refs


def as_float(v: Any) -> float | None:
    if v is None or v == "":
        return None
    return float(v)


def pct(v: Any) -> str:
    val = as_float(v)
    return "" if val is None else f"{100.0 * val:.1f}%"


def write_reports(out_dir: Path, rows: list[dict[str, Any]], refs: list[dict[str, Any]]) -> None:
    fields = [
        "canonical_split",
        "policy",
        "topk",
        "best_epoch",
        "success_fa",
        "failure_detection",
        "failure_det_at_25",
        "failure_det_at_50",
        "failure_mean_detection_time",
        "q95",
        "q99",
        "conformal_mass",
        "selected_dims",
    ]
    csv_path = out_dir / "dean_uncertainty_static_arch_sweep_results.csv"
    with csv_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k) for k in fields})

    lines = [
        "# Dean Uncertainty Static Architecture Sweep v1",
        "",
        "## Method",
        "",
        "This sweep keeps the canonical transformer sequence path unchanged and keeps the same `unc_topk8` current uncertainty features.",
        "Only the static/current branch or final fusion changes.",
        "",
        "- `unc_topk8_deep_static_v1`: LayerNorm + 2-layer static MLP.",
        "- `unc_topk8_gated_static_v1`: 2-layer static MLP plus learned gate between transformer CLS and static embedding.",
        "- `unc_topk8_grouped_static_v1`: separate encoders for action stats, ACE, proprio, and top-8 uncertainty before fusion.",
        "",
        "## Results",
        "",
        "| Split | Policy | FA | Det | Det@25 | Det@50 | Mean Time | Best Epoch |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for split in CANONICAL_SPLITS:
        for row in [r for r in refs + rows if r["canonical_split"] == split]:
            mean = row.get("failure_mean_detection_time")
            mean_s = "" if mean in {None, ""} else f"{float(mean):.3f}"
            lines.append(
                f"| {split} | {row['policy']} | {pct(row.get('success_fa'))} | "
                f"{pct(row.get('failure_detection'))} | {pct(row.get('failure_det_at_25'))} | "
                f"{pct(row.get('failure_det_at_50'))} | {mean_s} | {row.get('best_epoch', '')} |"
            )
    report_path = out_dir / "DEAN_UNCERTAINTY_STATIC_ARCH_SWEEP_REPORT.md"
    report_path.write_text("\n".join(lines) + "\n")
    print(f"Wrote {csv_path}", flush=True)
    print(f"Wrote {report_path}", flush=True)


def run_split(split_key: str, args: argparse.Namespace, episodes: dict[str, v2.EpisodeMeta]) -> list[dict[str, Any]]:
    global SELECTED_DIMS
    spec = CANONICAL_SPLITS[split_key]
    cfg = load_json(Path(spec["trained_dir"]) / "run_config.json")
    buckets = {k: set(v) for k, v in load_json(Path(spec["trained_dir"]) / spec["source_split"] / "episode_buckets.json").items()}
    dims = select_topk_dims(Path(spec["rank_dir"]), args.topk)
    SELECTED_DIMS = np.asarray(dims, dtype=np.int64)
    print(f"=== SPLIT {split_key} dims={dims} ===", flush=True)
    rows_by_bucket = v2.build_rows_for_split(Path(args.run_root), episodes, buckets, int(cfg["history_steps"]))

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    results = []
    for variant in args.variants:
        result = run_job(split_key, variant, rows_by_bucket, episodes, args, device, Path(args.output_dir))
        summary = metrics_summary(result, spec)
        results.append(
            {
                "canonical_split": split_key,
                "policy": variant,
                "topk": int(args.topk),
                "best_epoch": result["best_epoch"],
                **summary,
                "q95": result["thresholds"]["q95"],
                "q99": result["thresholds"]["q99"],
                "conformal_mass": result["thresholds"]["conformal_mass"],
                "selected_dims": ",".join(str(d) for d in dims),
            }
        )
    return results


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--run-root", default="/home/dean/fiper_uncertainty_collection/runs/dean_object_uncertainty_20260529")
    p.add_argument("--output-dir", default="/home/dean/fiper_uncertainty_collection/experiments/dean_uncertainty_static_arch_sweep_v1_20260602")
    p.add_argument("--splits", nargs="+", default=["all_tasks_full", "ood_last2_taskids_full"])
    p.add_argument("--variants", nargs="+", default=VARIANTS)
    p.add_argument("--topk", type=int, default=8)
    p.add_argument("--history-steps", type=int, default=16)
    p.add_argument("--width", type=int, default=128)
    p.add_argument("--layers", type=int, default=3)
    p.add_argument("--heads", type=int, default=4)
    p.add_argument("--dropout", type=float, default=0.1)
    p.add_argument("--batch-size", type=int, default=512)
    p.add_argument("--max-epochs", type=int, default=35)
    p.add_argument("--patience", type=int, default=8)
    p.add_argument("--lr", type=float, default=2e-4)
    p.add_argument("--weight-decay", type=float, default=1e-4)
    p.add_argument("--alpha", type=float, default=0.15)
    p.add_argument("--min-conformal-mass", type=float, default=0.15)
    p.add_argument("--seed", type=int, default=20260602)
    return p.parse_args()


def main() -> None:
    args = parse_args()
    seed_everything(args.seed)
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"Using device={'cuda' if torch.cuda.is_available() else 'cpu'}", flush=True)
    episodes = v2.load_episode_meta(Path(args.run_root))
    refs = load_reference_rows()
    all_rows: list[dict[str, Any]] = []
    for split in args.splits:
        all_rows.extend(run_split(split, args, episodes))
        write_reports(out_dir, all_rows, refs)
    write_json(out_dir / "run_config.json", vars(args))
    write_reports(out_dir, all_rows, refs)


if __name__ == "__main__":
    main()
