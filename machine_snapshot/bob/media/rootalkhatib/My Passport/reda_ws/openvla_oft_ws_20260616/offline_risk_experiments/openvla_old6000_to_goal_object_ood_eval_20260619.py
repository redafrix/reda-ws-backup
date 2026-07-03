#!/usr/bin/env python3
import json
import math
import os
from collections import defaultdict
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset


WS = Path("/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616")
OLD_DATASET = WS / "outputs/openvla_goal_object_pro_risk_data_10000ep_round_robin_20260616_discarded"
OOD_DATASET = WS / "datasets/openvla_goal_object_final_1890_complete_rounds_20260618"
OLD_EXP = Path(os.environ.get(
    "OLD_OPENVLA_RISK_EXP",
    str(WS / "offline_risk_experiments/openvla_old6000_risk_base_20260617"),
))
OUT = Path(os.environ.get(
    "OLD_TO_OOD_OUT",
    str(WS / "offline_risk_experiments/openvla_old6000_to_goal_object_ood_20260619"),
))


def pad_flat(values, size):
    arr = np.asarray(values if values is not None else [], dtype=np.float32).reshape(-1)
    out = np.zeros(size, dtype=np.float32)
    n = min(size, arr.size)
    if n:
        out[:n] = arr[:n]
    return out


def pad_seq(values, rows, cols):
    arr = np.asarray(values if values is not None else [], dtype=np.float32)
    if arr.size == 0:
        return np.zeros((rows, cols), dtype=np.float32)
    if arr.ndim == 1:
        arr = arr.reshape(-1, cols) if arr.size % cols == 0 else arr.reshape(1, -1)
    out = np.zeros((rows, cols), dtype=np.float32)
    rr = min(rows, arr.shape[0])
    cc = min(cols, arr.shape[1])
    out[:rr, :cc] = arr[:rr, :cc]
    return out


def apply_seq_standardizer(x, stats):
    return np.clip((x - stats["mean"]) / stats["std"], -10.0, 10.0).astype(np.float32)


def apply_standardizer(x, stats):
    return np.clip((x - stats["mean"]) / stats["std"], -10.0, 10.0).astype(np.float32)


def compute_metrics(y_true, y_scores, threshold=0.5):
    y_true = np.asarray(y_true, dtype=np.int32)
    y_scores = np.asarray(y_scores, dtype=np.float64)
    y_pred = (y_scores >= threshold).astype(np.int32)

    tp = int(np.sum((y_true == 1) & (y_pred == 1)))
    fp = int(np.sum((y_true == 0) & (y_pred == 1)))
    fn = int(np.sum((y_true == 1) & (y_pred == 0)))
    tn = int(np.sum((y_true == 0) & (y_pred == 0)))

    accuracy = (tp + tn) / len(y_true) if len(y_true) else 0.0
    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0.0
    fpr = fp / (fp + tn) if (fp + tn) else 0.0
    fnr = fn / (fn + tp) if (fn + tp) else 0.0

    order = np.argsort(y_scores, kind="mergesort")[::-1]
    yt = y_true[order]
    ys = y_scores[order]
    distinct = np.where(np.diff(ys))[0]
    idx = np.r_[distinct, yt.size - 1] if yt.size else np.array([], dtype=np.int64)
    tps = np.cumsum(yt)[idx] if idx.size else np.array([], dtype=np.float64)
    fps = 1 + idx - tps if idx.size else np.array([], dtype=np.float64)
    tps = np.r_[0, tps]
    fps = np.r_[0, fps]
    if len(tps) > 1 and fps[-1] > 0 and tps[-1] > 0:
        auroc = float(np.trapz(tps / tps[-1], fps / fps[-1]))
        prec = np.divide(tps, tps + fps, out=np.ones_like(tps, dtype=np.float64), where=(tps + fps) > 0)
        rec = tps / tps[-1]
        auprc = float(np.trapz(prec[np.argsort(rec)], np.sort(rec)))
    else:
        auroc = 0.5
        auprc = float(np.mean(y_true)) if len(y_true) else 0.0

    return {
        "accuracy": float(accuracy),
        "precision": float(precision),
        "recall": float(recall),
        "f1": float(f1),
        "fpr": float(fpr),
        "fnr": float(fnr),
        "auroc": float(auroc),
        "auprc": float(auprc),
        "confusion_matrix": [[tn, fp], [fn, tp]],
    }


class SeqRiskModel(nn.Module):
    def __init__(self, hist_dim, action_dim, static_dim, width=128, layers=3, heads=4, dropout=0.1):
        super().__init__()
        self.hist_proj = nn.Linear(hist_dim, width)
        self.action_proj = nn.Linear(action_dim, width)
        enc_layer = nn.TransformerEncoderLayer(
            width, heads, width * 4, dropout=dropout, batch_first=True, activation="gelu"
        )
        self.cls = nn.Parameter(torch.zeros(1, 1, width))
        self.pos = nn.Parameter(torch.randn(1, 64, width) * 0.02)
        self.seq = nn.TransformerEncoder(enc_layer, layers)
        self.static_in_dropout = nn.Dropout(0.0)
        self.static = nn.Sequential(nn.Linear(static_dim, width), nn.GELU())
        self.head = nn.Sequential(
            nn.LayerNorm(width * 2),
            nn.Linear(width * 2, width),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(width, 1),
        )

    def forward(self, batch):
        tokens = torch.cat([self.hist_proj(batch["history"]), self.action_proj(batch["action"])], dim=1)
        bsz = tokens.shape[0]
        tokens = torch.cat([self.cls.expand(bsz, -1, -1), tokens], dim=1)
        seq = self.seq(tokens + self.pos[:, : tokens.shape[1]])[:, 0]
        static = self.static(self.static_in_dropout(batch["static"]))
        return self.head(torch.cat([seq, static], dim=-1)).squeeze(-1)


class RiskDataset(Dataset):
    def __init__(self, h, a, st):
        self.h = torch.tensor(h, dtype=torch.float32)
        self.a = torch.tensor(a, dtype=torch.float32)
        self.st = torch.tensor(st, dtype=torch.float32)

    def __len__(self):
        return len(self.h)

    def __getitem__(self, idx):
        return {"history": self.h[idx], "action": self.a[idx], "static": self.st[idx]}


def load_episodes(dataset_dir):
    summaries = {}
    with (dataset_dir / "episode_summaries.jsonl").open() as f:
        for line in f:
            if not line.strip():
                continue
            ep = json.loads(line)
            ep_id = ep.get("episode_index_global")
            key = (int(ep["task_id"]), int(ep["reset_seed"]))
            summaries[key] = {
                "episode_index_global": ep_id,
                "task_id": int(ep["task_id"]),
                "reset_seed": int(ep["reset_seed"]),
                "success": bool(ep["success"]),
                "num_steps": int(ep.get("num_steps", 0)),
                "queries": [],
            }
    with (dataset_dir / "query_records.jsonl").open() as f:
        for line in f:
            if not line.strip():
                continue
            q = json.loads(line)
            key = (int(q["task_id"]), int(q["reset_seed"]))
            if key in summaries:
                summaries[key]["queries"].append(q)
    for ep in summaries.values():
        ep["queries"].sort(key=lambda q: int(q["env_timestep"]))
    return list(summaries.values())


def build_rows(dataset_dir, allowed_episode_ids=None, max_failed_timestep=None):
    rows = []
    for ep in load_episodes(dataset_dir):
        ep_id = ep["episode_index_global"]
        if allowed_episode_ids is not None and ep_id not in allowed_episode_ids:
            continue
        history_buffer = []
        y = 0.0 if ep["success"] else 1.0
        for q in ep["queries"]:
            timestep = int(q["env_timestep"])
            if y == 1.0 and max_failed_timestep is not None and timestep > max_failed_timestep:
                continue
            action = pad_seq(q["full_predicted_action_chunk"], 10, 7)
            proprio = pad_flat(q["proprio_vector"], 8)
            executed_src = q.get("actual_executed_actions") or [action[0]]
            executed = pad_flat(executed_src[0], 7)
            ace = np.zeros(7, dtype=np.float32)
            action_stats = np.concatenate(
                [action[0], action.mean(axis=0), action.std(axis=0), action[-1] - action[0]]
            ).astype(np.float32)
            static = np.concatenate([action_stats, ace, proprio]).astype(np.float32)
            hist = np.zeros((16, 21), dtype=np.float32)
            hist_src = history_buffer[-16:]
            offset = 16 - len(hist_src)
            for i, (h_prop, h_act, h_ace) in enumerate(hist_src):
                hist[offset + i, :] = np.concatenate([h_prop, h_act, h_ace[:6]])
            rows.append(
                {
                    "history": hist,
                    "action": action,
                    "static": static,
                    "y": y,
                    "task_id": ep["task_id"],
                    "reset_seed": ep["reset_seed"],
                    "episode_index_global": ep_id,
                    "timestep": timestep,
                    "episode_success": ep["success"],
                    "episode_steps": ep["num_steps"],
                }
            )
            history_buffer.append((proprio, executed, ace))
    return rows


def arrays(rows, stats):
    h = np.stack([r["history"] for r in rows], axis=0).astype(np.float32)
    a = np.stack([r["action"] for r in rows], axis=0).astype(np.float32)
    st = np.stack([r["static"] for r in rows], axis=0).astype(np.float32)
    y = np.asarray([r["y"] for r in rows], dtype=np.float32)
    h = apply_seq_standardizer(h, stats["history"])
    a = apply_seq_standardizer(a, stats["action"])
    st = apply_standardizer(st, stats["static"])
    return h, a, st, y


def predict(model, rows, stats, device):
    h, a, st, y = arrays(rows, stats)
    loader = DataLoader(RiskDataset(h, a, st), batch_size=512, shuffle=False)
    scores = []
    model.eval()
    with torch.no_grad():
        for batch in loader:
            batch = {k: v.to(device) for k, v in batch.items()}
            scores.extend(torch.sigmoid(model(batch)).cpu().numpy().tolist())
    return y, np.asarray(scores, dtype=np.float64)


def episode_false_alarm(rows, scores, threshold):
    by_ep = defaultdict(list)
    for row, score in zip(rows, scores):
        by_ep[(row["task_id"], row["reset_seed"], row["episode_success"])].append(float(score))
    succ_eps = [(k, v) for k, v in by_ep.items() if k[2]]
    fail_eps = [(k, v) for k, v in by_ep.items() if not k[2]]
    false_alarms = sum(max(v) >= threshold for _, v in succ_eps)
    detected = sum(max(v) >= threshold for _, v in fail_eps)
    return {
        "success_episodes": len(succ_eps),
        "failure_episodes": len(fail_eps),
        "episode_false_alarms": int(false_alarms),
        "episode_false_alarm_rate": float(false_alarms / len(succ_eps)) if succ_eps else 0.0,
        "failure_detected_episodes": int(detected),
        "failure_detection_rate": float(detected / len(fail_eps)) if fail_eps else 0.0,
    }


def early_detection(rows, scores, threshold, windows=(0.10, 0.25, 0.50)):
    by_ep = defaultdict(list)
    for row, score in zip(rows, scores):
        if not row["episode_success"]:
            by_ep[(row["task_id"], row["reset_seed"], row["episode_steps"])].append((row["timestep"], float(score)))
    out = {}
    for w in windows:
        total = 0
        hit = 0
        for (_, _, steps), vals in by_ep.items():
            cutoff = max(1, int(math.ceil(steps * w)))
            total += 1
            if any(score >= threshold for timestep, score in vals if timestep <= cutoff):
                hit += 1
        out[str(w)] = {"hit": int(hit), "total": int(total), "rate": float(hit / total) if total else 0.0}
    return out


def per_task_episode_stats(rows, scores, threshold):
    by_task = {}
    for tid in sorted({r["task_id"] for r in rows}):
        idx = [i for i, r in enumerate(rows) if r["task_id"] == tid]
        y = np.asarray([rows[i]["y"] for i in idx], dtype=np.float32)
        s = np.asarray([scores[i] for i in idx], dtype=np.float64)
        eps = {}
        for i in idx:
            r = rows[i]
            eps.setdefault((r["reset_seed"], r["episode_success"]), []).append(float(scores[i]))
        succ = [(k, v) for k, v in eps.items() if k[1]]
        fail = [(k, v) for k, v in eps.items() if not k[1]]
        fa = sum(max(v) >= threshold for _, v in succ)
        det = sum(max(v) >= threshold for _, v in fail)
        m = compute_metrics(y, s, threshold=threshold) if len(np.unique(y)) > 1 else None
        by_task[str(tid)] = {
            "queries": len(idx),
            "success_episodes": len(succ),
            "failure_episodes": len(fail),
            "episode_false_alarm_rate": float(fa / len(succ)) if succ else None,
            "failure_detection_rate": float(det / len(fail)) if fail else None,
            "auroc": None if m is None else m["auroc"],
            "auprc": None if m is None else m["auprc"],
        }
    return by_task


def fmt_pct(x):
    return f"{100.0 * x:.2f}%"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "reports").mkdir(parents=True, exist_ok=True)
    device = torch.device("cpu")

    with (OLD_EXP / "models/normalization.json").open() as f:
        raw_stats = json.load(f)
    stats = {k: {"mean": np.asarray(v["mean"], dtype=np.float32), "std": np.asarray(v["std"], dtype=np.float32)} for k, v in raw_stats.items()}
    with (OLD_EXP / "models/thresholds.json").open() as f:
        thresholds = json.load(f)
    with (OLD_EXP / "splits/test_episode_ids.json").open() as f:
        old_test_ids = set(json.load(f))

    model = SeqRiskModel(hist_dim=21, action_dim=7, static_dim=43)
    state = torch.load(OLD_EXP / "models/model.pt", map_location="cpu")
    model.load_state_dict(state)
    model.to(device)

    old_test_rows = build_rows(OLD_DATASET, allowed_episode_ids=old_test_ids)
    ood_rows = build_rows(OOD_DATASET, allowed_episode_ids=None)

    all_results = {}
    markdown_sections = []
    for name, rows in [("old6000_test_id", old_test_rows), ("goal_object_ood_all1890", ood_rows)]:
        y, scores = predict(model, rows, stats, device)
        dataset_results = {
            "queries": int(len(rows)),
            "episodes": int(len({(r["task_id"], r["reset_seed"]) for r in rows})),
            "success_episodes": int(len({(r["task_id"], r["reset_seed"]) for r in rows if r["episode_success"]})),
            "failure_episodes": int(len({(r["task_id"], r["reset_seed"]) for r in rows if not r["episode_success"]})),
            "thresholds": {},
        }
        for th_name in ["best_val_f1", "q95", "q99", "fixed_0.5"]:
            th = float(thresholds[th_name])
            step = compute_metrics(y, scores, threshold=th)
            ep = episode_false_alarm(rows, scores, th)
            early = early_detection(rows, scores, th)
            dataset_results["thresholds"][th_name] = {
                "threshold": th,
                "step_metrics": step,
                "episode_metrics": ep,
                "early_detection": early,
            }
        dataset_results["per_task_at_q95"] = per_task_episode_stats(rows, scores, float(thresholds["q95"]))
        all_results[name] = dataset_results

    with (OUT / "cross_dataset_metrics.json").open("w") as f:
        json.dump(all_results, f, indent=2)

    def table_row(dataset_name, th_name):
        r = all_results[dataset_name]["thresholds"][th_name]
        m = r["step_metrics"]
        e = r["episode_metrics"]
        early = r["early_detection"]
        return (
            f"| `{th_name}` | {r['threshold']:.4f} | {m['auroc']:.4f} | {m['auprc']:.4f} | "
            f"{m['f1']:.4f} | {fmt_pct(m['fpr'])} | {fmt_pct(m['fnr'])} | "
            f"{fmt_pct(e['episode_false_alarm_rate'])} ({e['episode_false_alarms']}/{e['success_episodes']}) | "
            f"{fmt_pct(e['failure_detection_rate'])} ({e['failure_detected_episodes']}/{e['failure_episodes']}) | "
            f"{fmt_pct(early['0.25']['rate'])} ({early['0.25']['hit']}/{early['0.25']['total']}) |"
        )

    report = []
    report.append("# Old-6000 OpenVLA Risk Model Cross-Dataset OOD Evaluation\n")
    report.append("## Setup\n")
    report.append(f"- Training source/model: `{OLD_EXP}`\n")
    report.append(f"- In-domain test dataset: `{OLD_DATASET}` using old heldout test split only\n")
    report.append(f"- External OOD dataset: `{OOD_DATASET}` using all complete 1890 goal-object episodes\n")
    report.append("- Evaluation only: CPU inference, no online rollout process touched.\n")
    report.append("- Model: old-6000 `SeqRiskModel` Transformer, `K=16`, action padded to `[10, 7]`, static dim `43`.\n")
    report.append("- Thresholds are the old-6000 validation thresholds, so the external OOD dataset is not used for calibration.\n\n")
    report.append("## Dataset Counts\n\n")
    report.append("| Dataset | Episodes | Success eps | Failure eps | Query rows |\n")
    report.append("|---|---:|---:|---:|---:|\n")
    for name in ["old6000_test_id", "goal_object_ood_all1890"]:
        r = all_results[name]
        report.append(f"| `{name}` | {r['episodes']} | {r['success_episodes']} | {r['failure_episodes']} | {r['queries']} |\n")
    report.append("\n## Threshold Results\n\n")
    for name in ["old6000_test_id", "goal_object_ood_all1890"]:
        report.append(f"### `{name}`\n\n")
        report.append("| Threshold | Value | AUROC | AUPRC | Step F1 | Step FPR | Step FNR | Episode false alarms | Episode failure detected | Failure detected by first 25% |\n")
        report.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|\n")
        for th_name in ["best_val_f1", "q95", "q99", "fixed_0.5"]:
            report.append(table_row(name, th_name) + "\n")
        report.append("\n")
    report.append("## External OOD Per-Task Results At Old Validation Q95\n\n")
    report.append("| Task | Success eps | Failure eps | AUROC | AUPRC | Episode FA | Failure detected |\n")
    report.append("|---:|---:|---:|---:|---:|---:|---:|\n")
    for tid, r in all_results["goal_object_ood_all1890"]["per_task_at_q95"].items():
        fa = "NA" if r["episode_false_alarm_rate"] is None else fmt_pct(r["episode_false_alarm_rate"])
        det = "NA" if r["failure_detection_rate"] is None else fmt_pct(r["failure_detection_rate"])
        auroc = "NA" if r["auroc"] is None else f"{r['auroc']:.4f}"
        auprc = "NA" if r["auprc"] is None else f"{r['auprc']:.4f}"
        report.append(f"| {tid} | {r['success_episodes']} | {r['failure_episodes']} | {auroc} | {auprc} | {fa} | {det} |\n")
    report.append("\n## Interpretation\n\n")
    report.append("- This is a strict cross-dataset test: old plain `libero_goal` training/calibration, then external `libero_goal_object` evaluation without threshold tuning.\n")
    report.append("- If external OOD episode false alarms are high, that means the old goal-only risk model does not transfer cleanly as an online alarm policy to goal-object, even if AUROC remains useful for ranking.\n")
    report.append("- If external OOD failure detection remains high but false alarms rise, the model is detecting difficulty, but its old thresholds are not deployment-calibrated for the goal-object distribution.\n")

    report_path = OUT / "reports/OLD6000_TO_GOAL_OBJECT_OOD_EVAL_20260619.md"
    report_path.write_text("".join(report))
    print(report_path)
    print(json.dumps(all_results, indent=2)[:6000])


if __name__ == "__main__":
    main()
