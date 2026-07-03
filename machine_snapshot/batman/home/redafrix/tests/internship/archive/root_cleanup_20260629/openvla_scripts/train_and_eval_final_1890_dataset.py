#!/usr/bin/env python3
import os
import json
import random
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

# Directories
OUTPUT_DIR = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/offline_risk_experiments/openvla_final1890_risk_20260618"
DATASET_DIR = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/datasets/openvla_goal_object_final_1890_complete_rounds_20260618"

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Seed everything
def seed_everything(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)

seed_everything(42)

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

# Metric computations
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

# Model definition
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

class SeqDataset(Dataset):
    def __init__(self, h, a, st, y):
        self.h = torch.tensor(h, dtype=torch.float32)
        self.a = torch.tensor(a, dtype=torch.float32)
        self.st = torch.tensor(st, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.float32)

    def __len__(self):
        return len(self.h)

    def __getitem__(self, idx):
        return {"history": self.h[idx], "action": self.a[idx], "static": self.st[idx]}, self.y[idx]

def create_splits():
    print("Creating stratified splits on the 1,891 episodes...")
    summaries_path = os.path.join(DATASET_DIR, "episode_summaries.jsonl")
    
    episodes = []
    with open(summaries_path, "r") as f:
        for line in f:
            if not line.strip():
                continue
            episodes.append(json.loads(line))
            
    # Group by (task_id, success) to stratify
    strata = {}
    for ep in episodes:
        key = (ep["task_id"], ep["success"])
        if key not in strata:
            strata[key] = []
        strata[key].append(ep["episode_index_global"])
        
    train_ids = []
    val_ids = []
    test_ids = []
    
    for key, ids in strata.items():
        random.shuffle(ids)
        n = len(ids)
        n_train = int(0.70 * n)
        n_val = int(0.15 * n)
        
        train_ids.extend(ids[:n_train])
        val_ids.extend(ids[n_train:n_train+n_val])
        test_ids.extend(ids[n_train+n_val:])
        
    os.makedirs(os.path.join(OUTPUT_DIR, "splits"), exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "splits", "train_episode_ids.json"), "w") as f:
        json.dump(train_ids, f)
    with open(os.path.join(OUTPUT_DIR, "splits", "val_episode_ids.json"), "w") as f:
        json.dump(val_ids, f)
    with open(os.path.join(OUTPUT_DIR, "splits", "test_episode_ids.json"), "w") as f:
        json.dump(test_ids, f)
        
    print(f"Splits saved: Train={len(train_ids)}, Val={len(val_ids)}, Test={len(test_ids)}")
    return set(train_ids), set(val_ids), set(test_ids), episodes

def extract_features(episodes, train_ids, val_ids, test_ids, max_fail_steps=800):
    print(f"Extracting features (max_fail_steps={max_fail_steps})...")
    queries_path = os.path.join(DATASET_DIR, "query_records.jsonl")
    
    # Map episode by (task_id, reset_seed)
    ep_map = {}
    for ep in episodes:
        key = (ep["task_id"], ep["reset_seed"])
        ep_map[key] = {
            "success": ep["success"],
            "global_id": ep["episode_index_global"],
            "queries": []
        }
        
    with open(queries_path, "r") as f:
        for line in f:
            if not line.strip():
                continue
            q = json.loads(line)
            key = (q["task_id"], q["reset_seed"])
            if key in ep_map:
                ep_map[key]["queries"].append(q)
                
    # Sort queries chronologically
    for ep in ep_map.values():
        ep["queries"].sort(key=lambda x: x["env_timestep"])
        
    train_rows = []
    val_rows = []
    test_rows = []
    
    train_failures = 0
    train_successes = 0
    
    for ep in ep_map.values():
        gid = ep["global_id"]
        success = ep["success"]
        queries = ep["queries"]
        
        if gid in train_ids:
            if success:
                train_successes += 1
            else:
                train_failures += 1
                
        history_buffer = []
        for q in queries:
            # Cut-off steps for failed episodes
            if not success and q["env_timestep"] > max_fail_steps:
                continue
                
            action = pad_seq(q["full_predicted_action_chunk"], 10, 7)
            proprio = pad_flat(q["proprio_vector"], 8)
            executed = pad_flat(q.get("actual_executed_actions", [action[0]])[0], 7)
            ace = np.zeros(7, dtype=np.float32)
            
            action_stats = np.concatenate([action[0], action.mean(axis=0), action.std(axis=0), action[-1] - action[0]]).astype(np.float32)
            static_base = np.concatenate([action_stats, ace, proprio]).astype(np.float32)
            
            history_steps = 16
            hist = np.zeros((history_steps, 21), dtype=np.float32)
            hist_src = history_buffer[-history_steps:]
            offset = history_steps - len(hist_src)
            for i, (h_prop, h_act, h_ace) in enumerate(hist_src):
                hist[offset + i, :] = np.concatenate([h_prop, h_act, h_ace[:6]])
                
            y = 1.0 if not success else 0.0
            row = {
                "history": hist,
                "action": action,
                "static": static_base,
                "y": y,
                "timestep": q["env_timestep"],
                "global_id": gid
            }
            
            if gid in train_ids:
                train_rows.append(row)
            elif gid in val_ids:
                val_rows.append(row)
            elif gid in test_ids:
                test_rows.append(row)
                
            history_buffer.append((proprio, executed, ace))
            
    pos_weight = train_successes / train_failures if train_failures > 0 else 1.0
    return train_rows, val_rows, test_rows, pos_weight, ep_map

def train_model(train_rows, val_rows, model_name="model"):
    # Stack arrays
    def make_arrays(rows):
        h = np.stack([r["history"] for r in rows], axis=0).astype(np.float32)
        a = np.stack([r["action"] for r in rows], axis=0).astype(np.float32)
        st = np.stack([r["static"] for r in rows], axis=0).astype(np.float32)
        y = np.asarray([r["y"] for r in rows], dtype=np.float32)
        return h, a, st, y
        
    h_train_raw, a_train_raw, st_train_raw, y_train = make_arrays(train_rows)
    h_val_raw, a_val_raw, st_val_raw, y_val = make_arrays(val_rows)
    
    # Compute normalizations
    stats = {
        "history": fit_seq_standardizer(h_train_raw),
        "action": fit_seq_standardizer(a_train_raw),
        "static": fit_standardizer(st_train_raw),
    }
    
    # Apply normalizations
    h_train = apply_seq_standardizer(h_train_raw, stats["history"])
    a_train = apply_seq_standardizer(a_train_raw, stats["action"])
    st_train = apply_standardizer(st_train_raw, stats["static"])
    
    h_val = apply_seq_standardizer(h_val_raw, stats["history"])
    a_val = apply_seq_standardizer(a_val_raw, stats["action"])
    st_val = apply_standardizer(st_val_raw, stats["static"])
    
    train_loader = DataLoader(SeqDataset(h_train, a_train, st_train, y_train), batch_size=128, shuffle=True)
    val_loader = DataLoader(SeqDataset(h_val, a_val, st_val, y_val), batch_size=256, shuffle=False)
    
    model = SeqRiskModel(hist_dim=21, action_dim=7, static_dim=43).to(device)
    
    # BCE Loss weight
    neg = float(np.sum(y_train == 0))
    pos = float(np.sum(y_train == 1))
    pos_weight = torch.tensor([max(1.0, neg / max(1.0, pos))], dtype=torch.float32, device=device)
    criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight)
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3, weight_decay=1e-4)
    
    best_state = None
    best_auc = -1.0
    no_improve = 0
    
    print(f"\n--- Training {model_name} (pos_weight={pos_weight.item():.2f}) ---")
    for epoch in range(1, 16):
        model.train()
        train_losses = []
        for batch, yb in train_loader:
            batch = {k: v.to(device) for k, v in batch.items()}
            yb = yb.to(device)
            optimizer.zero_grad(set_to_none=True)
            logits = model(batch)
            loss = criterion(logits, yb)
            loss.backward()
            nn.utils.clip_grad_norm_(model.parameters(), 5.0)
            optimizer.step()
            train_losses.append(loss.item())
            
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
        print(f"Epoch {epoch}/15 - Train Loss: {np.mean(train_losses):.4f}, Val AUROC: {val_auc:.4f}")
        
        if val_auc > best_auc + 1e-4:
            best_auc = val_auc
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}
            no_improve = 0
        else:
            no_improve += 1
            if no_improve >= 5:
                print(f"Early stopping triggered at epoch {epoch}.")
                break
                
    model.load_state_dict({k: v.to(device) for k, v in best_state.items()})
    return model, stats

def rows_to_arrays(rows):
    h = np.stack([r["history"] for r in rows], axis=0).astype(np.float32)
    a = np.stack([r["action"] for r in rows], axis=0).astype(np.float32)
    st = np.stack([r["static"] for r in rows], axis=0).astype(np.float32)
    y = np.asarray([r["y"] for r in rows], dtype=np.float32)
    return h, a, st, y

def predict_rows(model, stats, rows):
    h_raw, a_raw, st_raw, y = rows_to_arrays(rows)
    h = apply_seq_standardizer(h_raw, stats["history"])
    a = apply_seq_standardizer(a_raw, stats["action"])
    st = apply_standardizer(st_raw, stats["static"])
    loader = DataLoader(SeqDataset(h, a, st, y), batch_size=256, shuffle=False)
    preds = []
    model.eval()
    with torch.no_grad():
        for batch, _ in loader:
            batch = {k: v.to(device) for k, v in batch.items()}
            logits = model(batch)
            preds.extend(torch.sigmoid(logits).cpu().numpy())
    return np.asarray(preds), y

def evaluate_on_test(model, stats, val_rows, test_rows, test_ids, ep_map, max_fail_steps=800):
    model.eval()
    
    # 1. Step-level metrics
    preds_val, y_val = predict_rows(model, stats, val_rows)
    preds_test, y_test = predict_rows(model, stats, test_rows)

    # Select all operating thresholds on validation/calibration only.
    best_f1 = -1.0
    best_thresh = 0.5
    for th in np.arange(0.01, 1.00, 0.01):
        m = compute_metrics(y_val, preds_val, threshold=th)
        if m["f1"] > best_f1:
            best_f1 = m["f1"]
            best_thresh = th
            
    q90_th = np.percentile(preds_val[y_val == 0.0], 90)
    q95_th = np.percentile(preds_val[y_val == 0.0], 95)
    
    thresholds = {
        "best_f1": best_thresh,
        "q95": q95_th,
        "q90": q90_th
    }
    
    step_metrics = {}
    for k, th in thresholds.items():
        step_metrics[k] = compute_metrics(y_test, preds_test, threshold=th)
        step_metrics[k]["threshold_val"] = th
        
    # 2. Episode-level early detection and false alarm rates
    test_failed_episodes = {}
    test_success_episodes = {}
    
    for ep in ep_map.values():
        gid = ep["global_id"]
        success = ep["success"]
        queries = ep["queries"]
        if gid in test_ids:
            # Reconstruct queries for test episodes
            ep_queries = []
            history_buffer = []
            for q in queries:
                if not success and q["env_timestep"] > max_fail_steps:
                    continue
                action = pad_seq(q["full_predicted_action_chunk"], 10, 7)
                proprio = pad_flat(q["proprio_vector"], 8)
                executed = pad_flat(q.get("actual_executed_actions", [action[0]])[0], 7)
                ace = np.zeros(7, dtype=np.float32)
                action_stats = np.concatenate([action[0], action.mean(axis=0), action.std(axis=0), action[-1] - action[0]]).astype(np.float32)
                static_base = np.concatenate([action_stats, ace, proprio]).astype(np.float32)
                
                hist = np.zeros((16, 21), dtype=np.float32)
                hist_src = history_buffer[-16:]
                offset = 16 - len(hist_src)
                for i, (h_prop, h_act, h_ace) in enumerate(hist_src):
                    hist[offset + i, :] = np.concatenate([h_prop, h_act, h_ace[:6]])
                    
                ep_queries.append({
                    "history": hist,
                    "action": action,
                    "static": static_base
                })
                history_buffer.append((proprio, executed, ace))
                
            if success:
                test_success_episodes[gid] = ep_queries
            else:
                test_failed_episodes[gid] = ep_queries
                
    # Run predictions on all episodes
    def predict_episode(queries_list):
        probs = []
        for q in queries_list:
            hist_norm = apply_seq_standardizer(q["history"], stats["history"])
            action_norm = apply_seq_standardizer(q["action"], stats["action"])
            static_norm = apply_standardizer(q["static"], stats["static"])
            batch = {
                "history": torch.tensor(hist_norm, device=device).unsqueeze(0),
                "action": torch.tensor(action_norm, device=device).unsqueeze(0),
                "static": torch.tensor(static_norm, device=device).unsqueeze(0),
            }
            with torch.no_grad():
                prob = torch.sigmoid(model(batch)).cpu().item()
            probs.append(prob)
        return probs
        
    early_ratios = [0.10, 0.25, 0.50]
    early_detection = {r: {k: 0 for k in thresholds} for r in early_ratios}
    
    for gid, queries in test_failed_episodes.items():
        probs = predict_episode(queries)
        N = len(probs)
        for r in early_ratios:
            cutoff = max(1, int(np.ceil(r * N)))
            early_probs = probs[:cutoff]
            max_prob = max(early_probs) if early_probs else 0.0
            for k, th in thresholds.items():
                if max_prob >= th:
                    early_detection[r][k] += 1
                    
    # Episode false alarm rate
    false_alarms = {k: 0 for k in thresholds}
    for gid, queries in test_success_episodes.items():
        probs = predict_episode(queries)
        max_prob = max(probs) if probs else 0.0
        for k, th in thresholds.items():
            if max_prob >= th:
                false_alarms[k] += 1
                
    return step_metrics, early_detection, len(test_failed_episodes), false_alarms, len(test_success_episodes), {
        "best_f1_selected_on": "validation",
        "q90_selected_on": "validation_success_queries",
        "q95_selected_on": "validation_success_queries",
        "val_step_metrics_at_best_f1": compute_metrics(y_val, preds_val, threshold=best_thresh),
        "val_success_query_count": int(np.sum(y_val == 0.0)),
        "val_failure_query_count": int(np.sum(y_val == 1.0)),
        "test_success_query_count": int(np.sum(y_test == 0.0)),
        "test_failure_query_count": int(np.sum(y_test == 1.0)),
    }

def main():
    train_ids, val_ids, test_ids, episodes = create_splits()
    
    # 1. Train and eval 800-step model
    train_800, val_800, test_800, pw_800, ep_map_800 = extract_features(
        episodes, train_ids, val_ids, test_ids, max_fail_steps=800
    )
    model_800, stats_800 = train_model(train_800, val_800, model_name="800-Step Model")
    metrics_800, early_800, n_fail_800, fa_800, n_succ_800, audit_800 = evaluate_on_test(
        model_800, stats_800, val_800, test_800, test_ids, ep_map_800, max_fail_steps=800
    )
    
    # 2. Train and eval 300-step model
    train_300, val_300, test_300, pw_300, ep_map_300 = extract_features(
        episodes, train_ids, val_ids, test_ids, max_fail_steps=300
    )
    model_300, stats_300 = train_model(train_300, val_300, model_name="300-Step Model")
    metrics_300, early_300, n_fail_300, fa_300, n_succ_300, audit_300 = evaluate_on_test(
        model_300, stats_300, val_300, test_300, test_ids, ep_map_300, max_fail_steps=300
    )
    
    # Save the model weights
    models_dir = os.path.join(OUTPUT_DIR, "models")
    os.makedirs(models_dir, exist_ok=True)
    torch.save(model_800.state_dict(), os.path.join(models_dir, "model_800steps.pt"))
    torch.save(model_300.state_dict(), os.path.join(models_dir, "model_300steps.pt"))
    
    # Print results in Markdown tables
    total_eps = len(episodes)
    total_success = sum(1 for ep in episodes if ep["success"])
    total_fail = total_eps - total_success
    report_path = os.path.join(OUTPUT_DIR, "reports", "FINAL_1890_DATASET_RISK_EVALUATION_REPORT_20260618.md")
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    
    # Construct Markdown Report Content
    report_content = f"""# Final Comparative Evaluation Report: OpenVLA Goal-Object {total_eps}-Episode Dataset

This corrected report compares the performance of the `SeqRiskModel` temporal Transformer risk model trained on the cleaned final {total_eps}-episode `libero_goal_object` dataset on Bob under two failure logging horizons: **800 steps max** (default) vs. **300 steps max** (truncated).

All operating thresholds below are selected on the validation split, not the test split. This run uses the frozen complete-round dataset with reset seeds 100000..100188.

---

## 1. Dataset & Split Stats
* **Total Collected Episodes:** {total_eps}
* **Successful Episodes:** {total_success} ({total_success/total_eps*100:.2f}%)
* **Failed Episodes:** {total_fail} ({total_fail/total_eps*100:.2f}%)
* **Train Split:** {len(train_ids)} episodes
* **Val Split:** {len(val_ids)} episodes
* **Test Split:** {len(test_ids)} episodes ({n_succ_800} successful, {n_fail_800} failed)
* **Threshold source:** validation split only
* **800-step val queries:** {audit_800['val_success_query_count']} success / {audit_800['val_failure_query_count']} failure
* **300-step val queries:** {audit_300['val_success_query_count']} success / {audit_300['val_failure_query_count']} failure

---

## 2. Step-Level Test Metrics Comparison

| Metric | 800-Step Model (Best F1 Th={metrics_800['best_f1']['threshold_val']:.4f}) | 800-Step Model (Q95 Th={metrics_800['q95']['threshold_val']:.4f}) | 300-Step Model (Best F1 Th={metrics_300['best_f1']['threshold_val']:.4f}) | 300-Step Model (Q95 Th={metrics_300['q95']['threshold_val']:.4f}) |
| :--- | :---: | :---: | :---: | :---: |
| **AUROC** | {metrics_800['best_f1']['auroc']:.4f} | {metrics_800['q95']['auroc']:.4f} | {metrics_300['best_f1']['auroc']:.4f} | {metrics_300['q95']['auroc']:.4f} |
| **AUPRC** | {metrics_800['best_f1']['auprc']:.4f} | {metrics_800['q95']['auprc']:.4f} | {metrics_300['best_f1']['auprc']:.4f} | {metrics_300['q95']['auprc']:.4f} |
| **F1-Score** | {metrics_800['best_f1']['f1']:.4f} | {metrics_800['q95']['f1']:.4f} | {metrics_300['best_f1']['f1']:.4f} | {metrics_300['q95']['f1']:.4f} |
| **Accuracy** | {metrics_800['best_f1']['accuracy']:.4f} | {metrics_800['q95']['accuracy']:.4f} | {metrics_300['best_f1']['accuracy']:.4f} | {metrics_300['q95']['accuracy']:.4f} |
| **Step FPR** | {metrics_800['best_f1']['fpr']:.4f} | {metrics_800['q95']['fpr']:.4f} | {metrics_300['best_f1']['fpr']:.4f} | {metrics_300['q95']['fpr']:.4f} |
| **Step FNR** | {metrics_800['best_f1']['fnr']:.4f} | {metrics_800['q95']['fnr']:.4f} | {metrics_300['best_f1']['fnr']:.4f} | {metrics_300['q95']['fnr']:.4f} |

---

## 3. Episode-Level Early Failure Detection Rates

Percentage of failed episodes in the test split ({n_fail_800} episodes) successfully flagged within early windows:

| Step Window | 800-Step Model (Best F1) | 800-Step Model (Q95) | 300-Step Model (Best F1) | 300-Step Model (Q95) |
| :--- | :---: | :---: | :---: | :---: |
| **First 10%** of execution | {early_800[0.10]['best_f1']/n_fail_800*100:.2f}% | {early_800[0.10]['q95']/n_fail_800*100:.2f}% | {early_300[0.10]['best_f1']/n_fail_300*100:.2f}% | {early_300[0.10]['q95']/n_fail_300*100:.2f}% |
| **First 25%** of execution | {early_800[0.25]['best_f1']/n_fail_800*100:.2f}% | {early_800[0.25]['q95']/n_fail_800*100:.2f}% | {early_300[0.25]['best_f1']/n_fail_300*100:.2f}% | {early_300[0.25]['q95']/n_fail_300*100:.2f}% |
| **First 50%** of execution | {early_800[0.50]['best_f1']/n_fail_800*100:.2f}% | {early_800[0.50]['q95']/n_fail_800*100:.2f}% | {early_300[0.50]['best_f1']/n_fail_300*100:.2f}% | {early_300[0.50]['q95']/n_fail_300*100:.2f}% |

---

## 4. Episode-Level False Alarm Rates (FPR)

Percentage of successful test episodes ({n_succ_800} episodes) triggering a false alarm at any step:

| Threshold Type | 800-Step Model False Alarm Rate | 300-Step Model False Alarm Rate |
| :--- | :---: | :---: |
| **Best F1** | {fa_800['best_f1']/n_succ_800*100:.2f}% ({fa_800['best_f1']}/{n_succ_800}) | {fa_300['best_f1']/n_succ_300*100:.2f}% ({fa_300['best_f1']}/{n_succ_300}) |
| **Q95** | {fa_800['q95']/n_succ_800*100:.2f}% ({fa_800['q95']}/{n_succ_800}) | {fa_300['q95']/n_succ_300*100:.2f}% ({fa_300['q95']}/{n_succ_300}) |
| **Q90** | {fa_800['q90']/n_succ_800*100:.2f}% ({fa_800['q90']}/{n_succ_800}) | {fa_300['q90']/n_succ_300*100:.2f}% ({fa_300['q90']}/{n_succ_300}) |

---

## 5. Validity Notes

* The original 20260618 report used test-set predictions to select `best_f1`, `q90`, and `q95` thresholds. This corrected run fixes that leakage.
* Splits are grouped by episode and non-overlapping, but they are not round-held-out. Future final runs should also test held-out rounds/seeds.
* Some tasks are nearly deterministic in this partial collection: tasks 2 and 9 have no successes, while tasks 5 and 7 have no failures. Task identity can therefore be a strong shortcut; ablations without task-id should be run before claiming the model learned transferable physical risk.
* `query_records.jsonl` can be joined to episodes by `(task_id, reset_seed)`, but `step_records.jsonl` lacks task/seed/episode identifiers. Future collection should add these identifiers to every step row.
"""

    with open(report_path, "w") as f:
        f.write(report_content)
    print(f"\nSaved comparison report to {report_path}")

if __name__ == "__main__":
    main()
