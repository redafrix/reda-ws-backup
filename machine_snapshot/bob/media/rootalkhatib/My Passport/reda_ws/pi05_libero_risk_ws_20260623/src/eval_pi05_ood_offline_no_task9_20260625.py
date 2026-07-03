#!/usr/bin/env python3
import json
import pathlib
from collections import defaultdict

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset

ONLINE_ROOT = pathlib.Path("/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_libero_goal_object_ood_basic_vs_selected_cap_10ep_20260625")
EXP_ROOT = pathlib.Path("/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/offline_risk_experiments/pi05_goal_object_h10_risk_no_task9_20260625")
OUT_DIR = pathlib.Path("/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/offline_risk_experiments/pi05_goal_object_ood_18task_10ep_eval_no_task9_20260625")


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


def apply_seq_standardizer(x, stats):
    mean = np.array(stats["mean"], dtype=np.float32)
    std = np.array(stats["std"], dtype=np.float32)
    return np.clip((x - mean) / std, -10.0, 10.0).astype(np.float32)


def apply_standardizer(x, stats):
    mean = np.array(stats["mean"], dtype=np.float32)
    std = np.array(stats["std"], dtype=np.float32)
    return np.clip((x - mean) / std, -10.0, 10.0).astype(np.float32)


def compute_metrics(y_true, y_scores, threshold=0.5):
    y_true = np.asarray(y_true)
    y_scores = np.asarray(y_scores)
    y_pred = (y_scores >= threshold).astype(int)
    tp = np.sum((y_true == 1) & (y_pred == 1))
    fp = np.sum((y_true == 0) & (y_pred == 1))
    fn = np.sum((y_true == 1) & (y_pred == 0))
    tn = np.sum((y_true == 0) & (y_pred == 0))
    accuracy = (tp + tn) / max(1, len(y_true))
    precision = tp / max(1, tp + fp)
    recall = tp / max(1, tp + fn)
    f1 = 2 * precision * recall / max(1e-12, precision + recall)
    fpr = fp / max(1, fp + tn)
    fnr = fn / max(1, fn + tp)
    order = np.argsort(y_scores)[::-1]
    yt = y_true[order]
    tp_c = np.cumsum(yt == 1)
    fp_c = np.cumsum(yt == 0)
    if tp_c[-1] > 0 and fp_c[-1] > 0:
        auroc = float(np.trapz(tp_c / tp_c[-1], fp_c / fp_c[-1]))
    else:
        auroc = 0.5
    if tp_c[-1] > 0:
        precision_curve = tp_c / np.maximum(1, tp_c + fp_c)
        recall_curve = tp_c / tp_c[-1]
        auprc = float(np.trapz(precision_curve[np.argsort(recall_curve)], np.sort(recall_curve)))
    else:
        auprc = 0.0
    return {"accuracy": float(accuracy), "precision": float(precision), "recall": float(recall), "f1": float(f1), "fpr": float(fpr), "fnr": float(fnr), "auroc": auroc, "auprc": auprc}


def evaluate_episode(by_ep, thresholds):
    configs = [
        ("best_val_f1", thresholds["best_val_f1"], "k", 1, 0.0),
        ("q90", thresholds["q90"], "k", 1, 0.0),
        ("q95", thresholds["q95"], "k", 1, 0.0),
        ("q99", thresholds["q99"], "k", 1, 0.0),
        ("q95_K3", thresholds["q95"], "k", 3, 0.0),
        ("q99_K3", thresholds["q99"], "k", 3, 0.0),
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
            "fa": fa / max(1, succ),
            "det": det / max(1, fail),
            "det10": det10 / max(1, fail),
            "det25": det25 / max(1, fail),
            "det50": det50 / max(1, fail),
            "mean_time": float(np.mean(det_fracs)) if det_fracs else 1.0,
            "never": never / max(1, fail),
        }
    return out


def main():
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    queries_path = ONLINE_ROOT / "policy_pi05_basic_h10" / "query_records.jsonl"
    queries = [json.loads(line) for line in queries_path.open() if line.strip()]
    h = np.stack([np.asarray(q["history_16x21"], dtype=np.float32) for q in queries])
    a = np.stack([np.asarray(q["main_action_chunk"], dtype=np.float32) for q in queries])
    st = np.stack([np.asarray(q["static_features"], dtype=np.float32) for q in queries])
    y = np.asarray([0.0 if q["success"] else 1.0 for q in queries], dtype=np.float32)

    stats = json.loads((EXP_ROOT / "models" / "normalization.json").read_text())
    thresholds = json.loads((EXP_ROOT / "models" / "thresholds.json").read_text())
    h = apply_seq_standardizer(h, stats["history"])
    a = apply_seq_standardizer(a, stats["action"])
    st = apply_standardizer(st, stats["static"])

    model = SeqRiskModel().to(device)
    model.load_state_dict(torch.load(EXP_ROOT / "models" / "model.pt", map_location=device))
    model.eval()
    preds = []
    with torch.no_grad():
        for batch in DataLoader(QDataset(h, a, st), batch_size=256, shuffle=False):
            batch = {k: v.to(device) for k, v in batch.items()}
            preds.extend(torch.sigmoid(model(batch)).cpu().numpy().tolist())

    by_ep = defaultdict(list)
    for q, score in zip(queries, preds):
        by_ep[q["episode_id"]].append((q["env_step"], 0.0 if q["success"] else 1.0, float(score)))

    step_metrics = compute_metrics(y, preds, threshold=thresholds["best_val_f1"])
    episode_metrics = evaluate_episode(by_ep, thresholds)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    result = {
        "source_online_root": str(ONLINE_ROOT),
        "risk_experiment_root": str(EXP_ROOT),
        "num_queries": len(queries),
        "num_episodes": len(by_ep),
        "thresholds": thresholds,
        "step_metrics": step_metrics,
        "episode_metrics": episode_metrics,
    }
    (OUT_DIR / "offline_ood_eval_metrics.json").write_text(json.dumps(result, indent=2) + "\n")
    lines = [
        "# Pi0.5 No-Task9 Risk Head: OOD Offline Evaluation",
        "",
        f"- Risk experiment: `{EXP_ROOT}`",
        f"- OOD source: `{ONLINE_ROOT}`",
        f"- Episodes: `{len(by_ep)}`",
        f"- Queries: `{len(queries)}`",
        "",
        "## Step Metrics",
        "",
        f"- AUROC: `{step_metrics['auroc']:.4f}`",
        f"- AUPRC: `{step_metrics['auprc']:.4f}`",
        f"- F1: `{step_metrics['f1']:.4f}`",
        f"- FPR: `{step_metrics['fpr']:.4f}`",
        f"- FNR: `{step_metrics['fnr']:.4f}`",
        "",
        "## Episode Metrics",
        "",
        "| Policy | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for name, m in episode_metrics.items():
        lines.append(f"| {name} | {100*m['fa']:.2f}% | {100*m['det']:.2f}% | {100*m['det10']:.1f}% | {100*m['det25']:.1f}% | {100*m['det50']:.1f}% | {m['mean_time']:.3f} | {100*m['never']:.1f}% |")
    (OUT_DIR / "PI05_NO_TASK9_OOD_OFFLINE_EVAL_REPORT_20260625.md").write_text("\n".join(lines) + "\n")
    print(json.dumps({"out_dir": str(OUT_DIR), "step_metrics": step_metrics, "q95_mass_10": episode_metrics.get("q95_mass_10")}, indent=2))


if __name__ == "__main__":
    main()
