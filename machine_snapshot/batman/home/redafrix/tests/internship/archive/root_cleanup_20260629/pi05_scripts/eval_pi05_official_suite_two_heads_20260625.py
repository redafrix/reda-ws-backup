#!/usr/bin/env python3
import argparse
import json
import pathlib
from collections import defaultdict

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset


class SeqRiskModel(nn.Module):
    def __init__(self, hist_dim=21, action_dim=7, static_dim=51, width=128, layers=3, heads=4, dropout=0.1):
        super().__init__()
        self.hist_proj = nn.Linear(hist_dim, width)
        self.action_proj = nn.Linear(action_dim, width)
        enc_layer = nn.TransformerEncoderLayer(width, heads, width * 4, dropout=dropout, batch_first=True, activation="gelu")
        self.cls = nn.Parameter(torch.zeros(1, 1, width))
        self.pos = nn.Parameter(torch.randn(1, 64, width) * 0.02)
        self.seq = nn.TransformerEncoder(enc_layer, layers)
        self.static_in_dropout = nn.Dropout(0.0)
        self.static = nn.Sequential(nn.Linear(static_dim, width), nn.GELU())
        self.head = nn.Sequential(nn.LayerNorm(width * 2), nn.Linear(width * 2, width), nn.GELU(), nn.Dropout(dropout), nn.Linear(width, 1))

    def forward(self, batch):
        tokens = torch.cat([self.hist_proj(batch["history"]), self.action_proj(batch["action"])], dim=1)
        bsz = tokens.shape[0]
        tokens = torch.cat([self.cls.expand(bsz, -1, -1), tokens], dim=1)
        seq = self.seq(tokens + self.pos[:, : tokens.shape[1]])[:, 0]
        static = self.static(self.static_in_dropout(batch["static"]))
        return self.head(torch.cat([seq, static], dim=-1)).squeeze(-1)


class QDataset(Dataset):
    def __init__(self, h, a, st):
        self.h = torch.tensor(h, dtype=torch.float32)
        self.a = torch.tensor(a, dtype=torch.float32)
        self.st = torch.tensor(st, dtype=torch.float32)

    def __len__(self):
        return len(self.h)

    def __getitem__(self, idx):
        return {"history": self.h[idx], "action": self.a[idx], "static": self.st[idx]}


def load_jsonl(path):
    if not path.exists():
        return []
    with path.open() as f:
        return [json.loads(line) for line in f if line.strip()]


def apply_seq_standardizer(x, stats):
    mean = np.array(stats["mean"], dtype=np.float32)
    std = np.array(stats["std"], dtype=np.float32)
    return np.clip((x - mean) / std, -10.0, 10.0).astype(np.float32)


def apply_standardizer(x, stats):
    mean = np.array(stats["mean"], dtype=np.float32)
    std = np.array(stats["std"], dtype=np.float32)
    return np.clip((x - mean) / std, -10.0, 10.0).astype(np.float32)


def compute_metrics(y_true, y_scores, threshold):
    y_true = np.asarray(y_true)
    y_scores = np.asarray(y_scores)
    y_pred = (y_scores >= threshold).astype(int)
    tp = np.sum((y_true == 1) & (y_pred == 1))
    fp = np.sum((y_true == 0) & (y_pred == 1))
    fn = np.sum((y_true == 1) & (y_pred == 0))
    tn = np.sum((y_true == 0) & (y_pred == 0))
    precision = tp / max(1, tp + fp)
    recall = tp / max(1, tp + fn)
    f1 = 2 * precision * recall / max(1e-12, precision + recall)
    order = np.argsort(y_scores)[::-1]
    yt = y_true[order]
    tp_c = np.cumsum(yt == 1)
    fp_c = np.cumsum(yt == 0)
    if len(yt) and tp_c[-1] > 0 and fp_c[-1] > 0:
        auroc = float(np.trapz(tp_c / tp_c[-1], fp_c / fp_c[-1]))
    else:
        auroc = 0.5
    if len(yt) and tp_c[-1] > 0:
        precision_curve = tp_c / np.maximum(1, tp_c + fp_c)
        recall_curve = tp_c / tp_c[-1]
        auprc = float(np.trapz(precision_curve[np.argsort(recall_curve)], np.sort(recall_curve)))
    else:
        auprc = 0.0
    return {
        "accuracy": float((tp + tn) / max(1, len(y_true))),
        "precision": float(precision),
        "recall": float(recall),
        "f1": float(f1),
        "fpr": float(fp / max(1, fp + tn)),
        "fnr": float(fn / max(1, fn + tp)),
        "auroc": auroc,
        "auprc": auprc,
    }


def evaluate_episode(by_ep, thresholds):
    configs = [
        ("best_val_f1", thresholds["best_val_f1"], "k", 1, 0.0),
        ("q90", thresholds["q90"], "k", 1, 0.0),
        ("q95", thresholds["q95"], "k", 1, 0.0),
        ("q99", thresholds["q99"], "k", 1, 0.0),
        ("q95_K3", thresholds["q95"], "k", 3, 0.0),
        ("q99_K3", thresholds["q99"], "k", 3, 0.0),
        ("q95_mass_0.2", thresholds["q95"], "mass", 1, 0.2),
        ("q95_mass_1", thresholds["q95"], "mass", 1, 1.0),
        ("q95_mass_5", thresholds["q95"], "mass", 1, 5.0),
        ("q95_mass_10", thresholds["q95"], "mass", 1, 10.0),
        ("q95_mass_20", thresholds["q95"], "mass", 1, 20.0),
        ("q95_mass_50", thresholds["q95"], "mass", 1, 50.0),
    ]
    out = {}
    for name, th, mode, k, mass_th in configs:
        succ = fail = fa = det = det10 = det25 = det50 = never = 0
        det_fracs = []
        for _eid, rows in by_ep.items():
            rows = sorted(rows, key=lambda x: x[0])
            y = max(r[1] for r in rows)
            first = None
            if mode == "k":
                run = 0
                for i, (_t, _y, score) in enumerate(rows):
                    run = run + 1 if score >= th else 0
                    if run >= k:
                        first = i - k + 1
                        break
            else:
                mass = 0.0
                for i, (_t, _y, score) in enumerate(rows):
                    mass += max(0.0, score - th)
                    if mass >= mass_th:
                        first = i
                        break
            n = max(1, len(rows))
            if y >= 0.5:
                fail += 1
                if first is None:
                    never += 1
                else:
                    det += 1
                    frac = (first + 1) / n
                    det_fracs.append(frac)
                    det10 += frac <= 0.10
                    det25 += frac <= 0.25
                    det50 += frac <= 0.50
            else:
                succ += 1
                fa += first is not None
        out[name] = {
            "success_episodes": succ,
            "failure_episodes": fail,
            "fa": fa / max(1, succ),
            "det": det / max(1, fail),
            "det10": det10 / max(1, fail),
            "det25": det25 / max(1, fail),
            "det50": det50 / max(1, fail),
            "mean_time": float(np.mean(det_fracs)) if det_fracs else 1.0,
            "never": never / max(1, fail),
        }
    return out


def score_queries(queries, exp_root, device):
    h = np.stack([np.asarray(q["history_16x21"], dtype=np.float32) for q in queries])
    a = np.stack([np.asarray(q["main_action_chunk"], dtype=np.float32) for q in queries])
    st = np.stack([np.asarray(q["static_features"], dtype=np.float32) for q in queries])
    y = np.asarray([0.0 if q["success"] else 1.0 for q in queries], dtype=np.float32)

    stats = json.loads((exp_root / "models" / "normalization.json").read_text())
    thresholds = json.loads((exp_root / "models" / "thresholds.json").read_text())
    h = apply_seq_standardizer(h, stats["history"])
    a = apply_seq_standardizer(a, stats["action"])
    st = apply_standardizer(st, stats["static"])

    model = SeqRiskModel().to(device)
    model.load_state_dict(torch.load(exp_root / "models" / "model.pt", map_location=device))
    model.eval()
    preds = []
    with torch.no_grad():
        for batch in DataLoader(QDataset(h, a, st), batch_size=512, shuffle=False):
            batch = {k: v.to(device) for k, v in batch.items()}
            preds.extend(torch.sigmoid(model(batch)).cpu().numpy().tolist())

    by_ep = defaultdict(list)
    for q, score in zip(queries, preds):
        by_ep[q["episode_id"]].append((q["env_step"], 0.0 if q["success"] else 1.0, float(score)))
    return {
        "num_queries": len(queries),
        "num_episodes": len(by_ep),
        "thresholds": thresholds,
        "step_metrics": compute_metrics(y, preds, thresholds["best_val_f1"]),
        "episode_metrics": evaluate_episode(by_ep, thresholds),
    }


def summarize_online(online_root):
    out = {}
    for policy_dir in sorted(online_root.glob("policy_*")):
        summaries = load_jsonl(policy_dir / "episode_summaries.jsonl")
        if not summaries:
            continue
        by_task = {}
        for task_id in sorted({int(r["task_id"]) for r in summaries}):
            rows = [r for r in summaries if int(r["task_id"]) == task_id]
            succ = sum(bool(r.get("success")) for r in rows)
            mods = [int(r.get("action_modifications_count", 0) or 0) for r in rows]
            fails = [r for r in rows if not r.get("success")]
            by_task[str(task_id)] = {
                "episodes": len(rows),
                "success": succ,
                "success_rate": succ / max(1, len(rows)),
                "avg_steps": float(np.mean([int(r.get("steps", 0)) for r in rows])),
                "action_modifications_total": int(sum(mods)),
                "action_modifications_mean": float(np.mean(mods)) if mods else 0.0,
                "failure_seeds": [r.get("reset_seed") for r in fails],
                "failure_action_modifications": [int(r.get("action_modifications_count", 0) or 0) for r in fails],
            }
        out[policy_dir.name.replace("policy_", "")] = {
            "episodes": len(summaries),
            "success": sum(bool(r.get("success")) for r in summaries),
            "success_rate": sum(bool(r.get("success")) for r in summaries) / max(1, len(summaries)),
            "action_modifications_total": sum(int(r.get("action_modifications_count", 0) or 0) for r in summaries),
            "by_task": by_task,
        }
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--online-root", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--old-exp-root", default="/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/offline_risk_experiments/pi05_goal_object_h10_risk_20260625")
    parser.add_argument("--no-task9-exp-root", default="/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/offline_risk_experiments/pi05_goal_object_h10_risk_no_task9_20260625")
    args = parser.parse_args()

    online_root = pathlib.Path(args.online_root)
    out_dir = pathlib.Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    policy_query_sets = {}
    for policy_name in ["pi05_basic_h10", "pi05_risk_selected_cap_topk8_h10"]:
        qpath = online_root / f"policy_{policy_name}" / "query_records.jsonl"
        queries = load_jsonl(qpath)
        if queries:
            policy_query_sets[policy_name] = queries

    model_roots = {
        "old_with_task9": pathlib.Path(args.old_exp_root),
        "no_task9": pathlib.Path(args.no_task9_exp_root),
    }
    results = {
        "online_root": str(online_root),
        "online_summary": summarize_online(online_root),
        "offline": {},
    }
    for policy_name, queries in policy_query_sets.items():
        results["offline"][policy_name] = {}
        for model_name, exp_root in model_roots.items():
            results["offline"][policy_name][model_name] = score_queries(queries, exp_root, device)

    (out_dir / "pi05_official_ood_two_heads_metrics.json").write_text(json.dumps(results, indent=2) + "\n")

    lines = [
        "# Pi0.5 Official Suite Online + Offline Risk Evaluation",
        "",
        f"- Online root: `{online_root}`",
        f"- Output dir: `{out_dir}`",
        "",
        "## Online Success Summary",
        "",
        "| Policy | Episodes | Success | Success Rate | Action Mods |",
        "|---|---:|---:|---:|---:|",
    ]
    for policy, info in results["online_summary"].items():
        lines.append(f"| {policy} | {info['episodes']} | {info['success']} | {100*info['success_rate']:.2f}% | {info['action_modifications_total']} |")

    lines += ["", "## Online Per-Task Summary", ""]
    for policy, info in results["online_summary"].items():
        lines += [
            f"### {policy}",
            "",
            "| Task | Episodes | Success | SR | Avg Steps | Mods | Failure Seeds | Failure Mods |",
            "|---:|---:|---:|---:|---:|---:|---|---|",
        ]
        for task, row in info["by_task"].items():
            lines.append(
                f"| {task} | {row['episodes']} | {row['success']} | {100*row['success_rate']:.2f}% | "
                f"{row['avg_steps']:.1f} | {row['action_modifications_total']} | "
                f"{row['failure_seeds']} | {row['failure_action_modifications']} |"
            )
        lines.append("")

    lines += ["", "## Offline Risk Metrics", ""]
    for policy_name, model_results in results["offline"].items():
        lines += [f"### Query Source: {policy_name}", ""]
        for model_name, res in model_results.items():
            sm = res["step_metrics"]
            lines += [
                f"#### Model: {model_name}",
                "",
                f"- Episodes: `{res['num_episodes']}`",
                f"- Queries: `{res['num_queries']}`",
                f"- AUROC: `{sm['auroc']:.4f}`",
                f"- AUPRC: `{sm['auprc']:.4f}`",
                f"- F1: `{sm['f1']:.4f}`",
                f"- FPR: `{sm['fpr']:.4f}`",
                f"- FNR: `{sm['fnr']:.4f}`",
                "",
                "| Policy | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |",
                "|---|---:|---:|---:|---:|---:|---:|---:|",
            ]
            for name, m in res["episode_metrics"].items():
                lines.append(
                    f"| {name} | {100*m['fa']:.2f}% | {100*m['det']:.2f}% | {100*m['det10']:.1f}% | "
                    f"{100*m['det25']:.1f}% | {100*m['det50']:.1f}% | {m['mean_time']:.3f} | {100*m['never']:.1f}% |"
                )
            lines.append("")

    report_path = out_dir / "PI05_OFFICIAL_OOD_18TASK_TWO_HEADS_REPORT_20260625.md"
    report_path.write_text("\n".join(lines) + "\n")
    print(json.dumps({"out_dir": str(out_dir), "report": str(report_path)}, indent=2))


if __name__ == "__main__":
    main()
