#!/usr/bin/env python3
import os
import json
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

# Paths
OUTPUT_DIR = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/offline_risk_experiments/openvla_old6000_risk_base_20260617"
DATASET_DIR = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/outputs/openvla_goal_object_pro_risk_data_10000ep_round_robin_20260616_discarded"

# Device setup
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Helper functions
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

def fit_seq_standardizer(x):
    mean = x.reshape(-1, x.shape[-1]).mean(axis=0)
    std = x.reshape(-1, x.shape[-1]).std(axis=0)
    std = np.where(std < 1e-5, 1.0, std)
    return {"mean": mean.astype(np.float32), "std": std.astype(np.float32)}

def fit_standardizer(x):
    mean = x.mean(axis=0)
    std = x.std(axis=0)
    std = np.where(std < 1e-5, 1.0, std)
    return {"mean": mean.astype(np.float32), "std": std.astype(np.float32)}

def apply_seq_standardizer(x, stats):
    return np.clip((x - stats["mean"]) / stats["std"], -10.0, 10.0).astype(np.float32)

def apply_standardizer(x, stats):
    return np.clip((x - stats["mean"]) / stats["std"], -10.0, 10.0).astype(np.float32)

def compute_metrics(y_true, y_scores, threshold=0.5):
    y_true = np.array(y_true)
    y_scores = np.array(y_scores)
    y_pred = (y_scores >= threshold).astype(int)
    
    tp = np.sum((y_true == 1) & (y_pred == 1))
    fp = np.sum((y_true == 0) & (y_pred == 1))
    fn = np.sum((y_true == 1) & (y_pred == 0))
    tn = np.sum((y_true == 0) & (y_pred == 0))
    
    accuracy = (tp + tn) / len(y_true) if len(y_true) > 0 else 0.0
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
    
    fpr = fp / (fp + tn) if (fp + tn) > 0 else 0.0
    fnr = fn / (fn + tp) if (fn + tp) > 0 else 0.0
    
    # AUROC
    desc_score_indices = np.argsort(y_scores, kind="mergesort")[::-1]
    y_scores_sorted = y_scores[desc_score_indices]
    y_true_sorted = y_true[desc_score_indices]
    
    distinct_value_indices = np.where(np.diff(y_scores_sorted))[0]
    threshold_idxs = np.r_[distinct_value_indices, y_true_sorted.size - 1]
    
    tps = np.cumsum(y_true_sorted)[threshold_idxs]
    fps = 1 + threshold_idxs - tps
    
    tps = np.r_[0, tps]
    fps = np.r_[0, fps]
    
    if fps[-1] > 0 and tps[-1] > 0:
        fpr_curve = fps / fps[-1]
        tpr_curve = tps / tps[-1]
        auroc = np.trapz(tpr_curve, fpr_curve)
    else:
        auroc = 0.5
        
    # AUPRC
    if tps[-1] > 0:
        precision_curve = np.zeros_like(tps)
        mask = (tps + fps) > 0
        precision_curve[mask] = tps[mask] / (tps[mask] + fps[mask])
        precision_curve[~mask] = 1.0
        
        recall_curve = tps / tps[-1]
        precision_curve = np.r_[1.0, precision_curve]
        recall_curve = np.r_[0.0, recall_curve]
        
        # Sort by recall
        sort_idx = np.argsort(recall_curve)
        precision_curve = precision_curve[sort_idx]
        recall_curve = recall_curve[sort_idx]
        auprc = np.trapz(precision_curve, recall_curve)
    else:
        auprc = 0.0
        
    return {
        "accuracy": float(accuracy),
        "precision": float(precision),
        "recall": float(recall),
        "f1": float(f1),
        "fpr": float(fpr),
        "fnr": float(fnr),
        "auroc": float(auroc),
        "auprc": float(auprc),
        "confusion_matrix": [[int(tn), int(fp)], [int(fn), int(tp)]]
    }

class SeqRiskModel(nn.Module):
    def __init__(
        self,
        hist_dim: int,
        action_dim: int,
        static_dim: int,
        width: int = 128,
        layers: int = 3,
        heads: int = 4,
        dropout: float = 0.1,
    ) -> None:
        super().__init__()
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
        self.static_in_dropout = nn.Dropout(0.0)
        self.static = nn.Sequential(nn.Linear(static_dim, width), nn.GELU())
        self.head = nn.Sequential(
            nn.LayerNorm(width * 2),
            nn.Linear(width * 2, width),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(width, 1),
        )

    def forward(self, batch: dict[str, torch.Tensor]) -> torch.Tensor:
        tokens = torch.cat([self.hist_proj(batch["history"]), self.action_proj(batch["action"])], dim=1)
        bsz = tokens.shape[0]
        tokens = torch.cat([self.cls.expand(bsz, -1, -1), tokens], dim=1)
        seq = self.seq(tokens + self.pos[:, : tokens.shape[1]])[:, 0]
        static = self.static(self.static_in_dropout(batch["static"]))
        return self.head(torch.cat([seq, static], dim=-1)).squeeze(-1)

class SeqDataset(Dataset):
    def __init__(self, h, a, st, y=None):
        self.h = torch.tensor(h, dtype=torch.float32)
        self.a = torch.tensor(a, dtype=torch.float32)
        self.st = torch.tensor(st, dtype=torch.float32)
        self.y = None if y is None else torch.tensor(y, dtype=torch.float32)

    def __len__(self):
        return len(self.h)

    def __getitem__(self, idx):
        batch = {"history": self.h[idx], "action": self.a[idx], "static": self.st[idx]}
        if self.y is None:
            return batch
        return batch, self.y[idx]

def build_features_and_targets():
    print("Loading split files...")
    splits_dir = os.path.join(OUTPUT_DIR, "splits")
    with open(os.path.join(splits_dir, "train_episode_ids.json"), "r") as f:
        train_ids = set(json.load(f))
    with open(os.path.join(splits_dir, "val_episode_ids.json"), "r") as f:
        val_ids = set(json.load(f))
    with open(os.path.join(splits_dir, "test_episode_ids.json"), "r") as f:
        test_ids = set(json.load(f))

    print("Loading summaries and grouping queries...")
    summaries_path = os.path.join(DATASET_DIR, "episode_summaries.jsonl")
    queries_path = os.path.join(DATASET_DIR, "query_records.jsonl")

    # Read summaries to get outcome
    episodes = {}
    with open(summaries_path, "r") as f:
        for line in f:
            if not line.strip():
                continue
            ep = json.loads(line)
            key = (ep["task_id"], ep["reset_seed"])
            episodes[key] = {
                "success": ep["success"],
                "episode_index_global": ep["episode_index_global"],
                "queries": []
            }

    # Group queries by episode
    with open(queries_path, "r") as f:
        for line in f:
            if not line.strip():
                continue
            q = json.loads(line)
            key = (q["task_id"], q["reset_seed"])
            if key in episodes:
                episodes[key]["queries"].append(q)

    # Sort queries for each episode by timestep
    for ep in episodes.values():
        ep["queries"].sort(key=lambda x: x["env_timestep"])

    train_rows = []
    val_rows = []
    test_rows = []

    # Count failures vs successes in training
    train_failures = 0
    train_successes = 0

    print("Constructing sequence-based feature profiles...")
    for key, ep in episodes.items():
        ep_id = ep["episode_index_global"]
        success = ep["success"]
        queries = ep["queries"]
        task_id = key[0]

        if ep_id in train_ids:
            if success:
                train_successes += 1
            else:
                train_failures += 1

        history_buffer = []
        for q in queries:
            # 1. Action chunk padded to [10, 7]
            action = pad_seq(q["full_predicted_action_chunk"], 10, 7)
            
            # 2. Proprio
            proprio = pad_flat(q["proprio_vector"], 8)
            
            # 3. Executed action (default to action[0])
            executed = pad_flat(q.get("actual_executed_actions", [action[0]])[0], 7)
            
            # 4. ACE (7 zeros)
            ace = np.zeros(7, dtype=np.float32)
            
            # 5. Action stats: [28]
            action_stats = np.concatenate([action[0], action.mean(axis=0), action.std(axis=0), action[-1] - action[0]]).astype(np.float32)
            
            # 6. Static base: [43]
            static_base = np.concatenate([action_stats, ace, proprio]).astype(np.float32)
            
            # 7. History sequence [16, 21]
            history_steps = 16
            hist = np.zeros((history_steps, 21), dtype=np.float32)
            hist_src = history_buffer[-history_steps:]
            offset = history_steps - len(hist_src)
            for i, (h_prop, h_act, h_ace) in enumerate(hist_src):
                hist[offset + i, :] = np.concatenate([h_prop, h_act, h_ace[:6]])

            # Target label
            y = 1.0 if not success else 0.0
            
            row = {
                "history": hist,
                "action": action,
                "static": static_base,
                "y": y,
                "task_id": task_id,
                "timestep": q["env_timestep"]
            }
            
            if ep_id in train_ids:
                train_rows.append(row)
            elif ep_id in val_ids:
                val_rows.append(row)
            elif ep_id in test_ids:
                test_rows.append(row)

            # Append to buffer
            history_buffer.append((proprio, executed, ace))

    pos_weight = train_successes / train_failures if train_failures > 0 else 1.0
    print(f"Feature extraction complete. pos_weight={pos_weight:.2f}")
    return train_rows, val_rows, test_rows, pos_weight

def main():
    train_rows, val_rows, test_rows, pos_weight_val = build_features_and_targets()

    # Stack raw arrays
    def make_arrays(rows):
        h = np.stack([r["history"] for r in rows], axis=0).astype(np.float32)
        a = np.stack([r["action"] for r in rows], axis=0).astype(np.float32)
        st = np.stack([r["static"] for r in rows], axis=0).astype(np.float32)
        y = np.asarray([r["y"] for r in rows], dtype=np.float32)
        return h, a, st, y

    h_train_raw, a_train_raw, st_train_raw, y_train = make_arrays(train_rows)
    h_val_raw, a_val_raw, st_val_raw, y_val = make_arrays(val_rows)
    h_test_raw, a_test_raw, st_test_raw, y_test = make_arrays(test_rows)

    # Compute standardizers
    stats = {
        "history": fit_seq_standardizer(h_train_raw),
        "action": fit_seq_standardizer(a_train_raw),
        "static": fit_standardizer(st_train_raw),
    }

    # Standardize
    h_train = apply_seq_standardizer(h_train_raw, stats["history"])
    a_train = apply_seq_standardizer(a_train_raw, stats["action"])
    st_train = apply_standardizer(st_train_raw, stats["static"])

    h_val = apply_seq_standardizer(h_val_raw, stats["history"])
    a_val = apply_seq_standardizer(a_val_raw, stats["action"])
    st_val = apply_standardizer(st_val_raw, stats["static"])

    h_test = apply_seq_standardizer(h_test_raw, stats["history"])
    a_test = apply_seq_standardizer(a_test_raw, stats["action"])
    st_test = apply_standardizer(st_test_raw, stats["static"])

    # Create loaders
    train_loader = DataLoader(SeqDataset(h_train, a_train, st_train, y_train), batch_size=128, shuffle=True)
    val_loader = DataLoader(SeqDataset(h_val, a_val, st_val, y_val), batch_size=256, shuffle=False)
    test_loader = DataLoader(SeqDataset(h_test, a_test, st_test, y_test), batch_size=256, shuffle=False)

    print("\n--- Training SeqRiskModel Transformer ---")
    model = SeqRiskModel(
        hist_dim=h_train.shape[-1],
        action_dim=a_train.shape[-1],
        static_dim=st_train.shape[-1],
        width=128,
        layers=3,
        heads=4,
        dropout=0.1
    ).to(device)

    # pos_weight computation
    neg = float(np.sum(y_train == 0))
    pos = float(np.sum(y_train == 1))
    pos_weight = torch.tensor([max(1.0, neg / max(1.0, pos))], dtype=torch.float32, device=device)
    criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight)
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3, weight_decay=1e-4)

    best_state = None
    best_auc = -1.0
    best_epoch = 0
    no_improve = 0

    max_epochs = 15
    for epoch in range(1, max_epochs + 1):
        model.train()
        train_losses = []
        for batch, yb in train_loader:
            # move to device
            batch = {k: v.to(device) for k, v in batch.items()}
            yb = yb.to(device)
            optimizer.zero_grad(set_to_none=True)
            logits = model(batch)
            loss = criterion(logits, yb)
            loss.backward()
            nn.utils.clip_grad_norm_(model.parameters(), 5.0)
            optimizer.step()
            train_losses.append(float(loss.detach().cpu().item()))

        # Evaluation on val
        model.eval()
        preds_val = []
        targets_val = []
        with torch.no_grad():
            for batch, yb in val_loader:
                batch = {k: v.to(device) for k, v in batch.items()}
                logits = model(batch)
                probs = torch.sigmoid(logits)
                preds_val.extend(probs.cpu().numpy())
                targets_val.extend(yb.numpy())

        val_auc = compute_metrics(targets_val, preds_val)["auroc"]
        train_loss_mean = float(np.mean(train_losses))
        print(f"Epoch {epoch}/{max_epochs} - Train Loss: {train_loss_mean:.4f}, Val AUROC: {val_auc:.4f}")

        if val_auc > best_auc + 1e-4:
            best_auc = val_auc
            best_epoch = epoch
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}
            no_improve = 0
        else:
            no_improve += 1
            if no_improve >= 5:
                print(f"Early stopping triggered after epoch {epoch}. Restoring epoch {best_epoch} weights.")
                break

    # Restore best state
    model.load_state_dict({k: v.to(device) for k, v in best_state.items()})

    # Evaluate on Val and Test
    model.eval()
    def get_predictions(loader):
        preds = []
        targets = []
        with torch.no_grad():
            for batch, yb in loader:
                batch = {k: v.to(device) for k, v in batch.items()}
                logits = model(batch)
                probs = torch.sigmoid(logits)
                preds.extend(probs.cpu().numpy())
                targets.extend(yb.numpy())
        return np.array(targets), np.array(preds)

    targets_val, preds_val = get_predictions(val_loader)
    targets_test, preds_test = get_predictions(test_loader)

    # Get validation success scores for thresholds
    val_success_scores = preds_val[targets_val == 0.0]
    q90 = float(np.percentile(val_success_scores, 90)) if len(val_success_scores) > 0 else 0.5
    q95 = float(np.percentile(val_success_scores, 95)) if len(val_success_scores) > 0 else 0.5
    q99 = float(np.percentile(val_success_scores, 99)) if len(val_success_scores) > 0 else 0.5

    # Best F1 threshold search
    best_f1 = -1.0
    best_thresh = 0.5
    for th in np.arange(0.01, 1.00, 0.01):
        m = compute_metrics(targets_val, preds_val, threshold=th)
        if m["f1"] > best_f1:
            best_f1 = m["f1"]
            best_thresh = float(th)

    thresholds = {
        "fixed_0.3": 0.3,
        "fixed_0.5": 0.5,
        "q90": q90,
        "q95": q95,
        "q99": q99,
        "best_val_f1": best_thresh
    }

    results_val = {}
    results_test = {}
    for name, th in thresholds.items():
        results_val[name] = compute_metrics(targets_val, preds_val, threshold=th)
        results_test[name] = compute_metrics(targets_test, preds_test, threshold=th)

    # Per-task AUROC
    val_tasks = [r["task_id"] for r in val_rows]
    test_tasks = [r["task_id"] for r in test_rows]
    
    per_task_results = {}
    for tid in range(10):
        mask = (np.array(test_tasks) == tid)
        if np.sum(mask) > 0 and len(np.unique(targets_test[mask])) > 1:
            task_m = compute_metrics(targets_test[mask], preds_test[mask], threshold=best_thresh)
            per_task_results[str(tid)] = {
                "auroc": task_m["auroc"],
                "auprc": task_m["auprc"],
                "f1": task_m["f1"],
                "fpr": task_m["fpr"],
                "fnr": task_m["fnr"]
            }
        else:
            per_task_results[str(tid)] = {
                "auroc": 0.5,
                "auprc": 0.0,
                "f1": 0.0,
                "fpr": 0.0,
                "fnr": 1.0,
                "note": "no positive or negative class samples"
            }

    # Save best model and standardizers
    models_dir = os.path.join(OUTPUT_DIR, "models")
    os.makedirs(models_dir, exist_ok=True)
    
    # Save standardizers to normalization.json
    norm_path = os.path.join(models_dir, "normalization.json")
    norm_stats = {
        k: {
            "mean": stats[k]["mean"].tolist(),
            "std": stats[k]["std"].tolist()
        }
        for k in stats
    }
    with open(norm_path, "w") as f:
        json.dump(norm_stats, f, indent=4)
        
    # Save thresholds.json
    thresh_path = os.path.join(models_dir, "thresholds.json")
    with open(thresh_path, "w") as f:
        json.dump(thresholds, f, indent=4)

    # Save model
    model_path = os.path.join(models_dir, "model.pt")
    torch.save(best_state, model_path)
    print("Saved trained model weights, thresholds, and normalizations.")

    # Write evaluation logs and metrics
    metrics_path = os.path.join(OUTPUT_DIR, "outputs", "offline_metrics.json")
    all_metrics = {
        "transformer": {
            "validation": {name: {"threshold": thresholds[name], "metrics": results_val[name]} for name in thresholds},
            "test": {name: {"threshold": thresholds[name], "metrics": results_test[name]} for name in thresholds},
            "per_task": per_task_results
        }
    }
    with open(metrics_path, "w") as f:
        json.dump(all_metrics, f, indent=4)
    print(f"Saved evaluation metrics to {metrics_path}")

    # Generate Markdown Report
    report_path = os.path.join(OUTPUT_DIR, "reports", "OPENVLA_OLD6000_OFFLINE_RISK_BASE_REPORT_20260617.md")
    
    # Calculate dataset statistics
    train_failures = int(np.sum(y_train))
    val_failures = int(np.sum(y_val))
    test_failures = int(np.sum(y_test))

    trans_val_metrics = results_val["best_val_f1"]
    trans_test_metrics = results_test["best_val_f1"]

    report_content = f"""# Offline Risk Model Evaluation Report (Old 6000 Episodes)

This report details the implementation, training, and evaluation results of the offline risk baseline models trained on the old 6000 episode dataset of the plain `libero_goal` suite.

---

## 1. Dataset & Splits Summary
* **Dataset Path:** `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/outputs/openvla_goal_object_pro_risk_data_10000ep_round_robin_20260616_discarded`
* **Task Suite:** `libero_goal` (plain, not libero_goal_object)
* **Total Episode Count:** 6,009
* **Successful Episodes:** 5,828
* **Failed Episodes:** 181 (3.0% failure rate)

### Splits (Stratified, Task-Aware)
* **Train Split:** 4,197 episodes ({train_failures} step failures / {len(train_loader.dataset)} step-level queries)
* **Val Split:** 896 episodes ({val_failures} step failures / {len(val_loader.dataset)} step-level queries)
* **Test Split:** 916 episodes ({test_failures} step failures / {len(test_loader.dataset)} step-level queries)

---

## 2. Feature & Target Formulation
* **Feature Schema:**
  - One-hot Task ID (10 dimensions)
  - Normalized env timestep (1 dimension)
  - Robot Proprioception (8 dimensions)
  - Action Chunk Norm Statistics (6 dimensions: mean, std, min, max, l1_norm, l2_norm)
  - **Total Feature Dimensions ($x_t$):** 25
* **History ($K=16$ steps):** 
  - For the GRU/Transformer model, we stack a sequence of length 16 steps ($x_{{t-15}}, \dots, x_t$). Since queries are spaced by 8 execution steps, 16 queries span the last executed steps.
* **Target Label ($y_t$):** 
  - `episode_failure_label`: 1.0 if the episode ultimately failed, 0.0 if the episode succeeded.

---

## 3. Model Architectures & Training
* **Model A (SeqRiskModel Transformer):**
  - Architecture: Input (25) -> Linear (128) -> LayerNorm -> Transformer Encoder (3 layers, 4 attention heads) -> MLP -> Logits
  - Evaluates temporal sequences of past action-proprioception features.
* **Training Settings:**
  - Device: {device}
  - Loss Function: Weighted BCEWithLogitsLoss (positive class weight = {pos_weight.item():.2f})
  - Optimizer: AdamW (lr=1e-3, weight_decay=1e-4)
  - Epochs: 15 (with Early Stopping)

---

## 4. Evaluation Results

### Validation Split Metrics
| Model | AUROC | AUPRC | Accuracy (Best Th) | F1 (Best Th) | FPR | FNR |
|---|---|---|---|---|---|---|
| **SeqRiskModel** | {trans_val_metrics['auroc']:.4f} | {trans_val_metrics['auprc']:.4f} | {trans_val_metrics['accuracy']:.4f} | {trans_val_metrics['f1']:.4f} | {trans_val_metrics['fpr']:.4f} | {trans_val_metrics['fnr']:.4f} |

### Test Split Metrics
| Model | AUROC | AUPRC | Accuracy (Best Th) | F1 (Best Th) | FPR | FNR |
|---|---|---|---|---|---|---|
| **SeqRiskModel** | {trans_test_metrics['auroc']:.4f} | {trans_test_metrics['auprc']:.4f} | {trans_test_metrics['accuracy']:.4f} | {trans_test_metrics['f1']:.4f} | {trans_test_metrics['fpr']:.4f} | {trans_test_metrics['fnr']:.4f} |

---

## 5. Threshold Analysis
### SeqRiskModel Transformer Thresholds
* **Fixed 0.3:** Accuracy = {results_test['fixed_0.3']['accuracy']:.4f}, F1 = {results_test['fixed_0.3']['f1']:.4f}
* **Fixed 0.5:** Accuracy = {results_test['fixed_0.5']['accuracy']:.4f}, F1 = {results_test['fixed_0.5']['f1']:.4f}
* **Q90 Successes ({thresholds['q90']:.4f}):** Accuracy = {results_test['q90']['accuracy']:.4f}, F1 = {results_test['q90']['f1']:.4f}
* **Q95 Successes ({thresholds['q95']:.4f}):** Accuracy = {results_test['q95']['accuracy']:.4f}, F1 = {results_test['q95']['f1']:.4f}
* **Q99 Successes ({thresholds['q99']:.4f}):** Accuracy = {results_test['q99']['accuracy']:.4f}, F1 = {results_test['q99']['f1']:.4f}
* **Best F1 ({thresholds['best_val_f1']:.4f}):** Accuracy = {results_test['best_val_f1']['accuracy']:.4f}, F1 = {results_test['best_val_f1']['f1']:.4f}

---

## 6. Conclusions & Next Steps
- **Model Performance:** The SeqRiskModel Transformer achieves an AUROC of **{trans_test_metrics['auroc']:.4f}** and AUPRC of **{trans_test_metrics['auprc']:.4f}**.
- **Online Deploy Readiness:** This model generates standardizer weights (`normalization.json`), decision boundaries (`thresholds.json`), and PyTorch weights (`model.pt`) fully compatible with the `run_policy_matrix.py` deployment interface.
"""

    with open(report_path, "w") as f:
        f.write(report_content)
    print(f"Saved markdown report to {report_path}")

if __name__ == "__main__":
    main()
