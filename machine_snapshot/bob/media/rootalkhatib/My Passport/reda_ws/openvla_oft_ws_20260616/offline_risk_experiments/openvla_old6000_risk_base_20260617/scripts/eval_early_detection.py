#!/usr/bin/env python3
import os
import json
import numpy as np
import torch
import torch.nn as nn

OUTPUT_DIR = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/offline_risk_experiments/openvla_old6000_risk_base_20260617"
DATASET_DIR = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/outputs/openvla_goal_object_pro_risk_data_10000ep_round_robin_20260616_discarded"

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

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
    return np.clip((x - np.array(stats["mean"])) / np.array(stats["std"]), -10.0, 10.0).astype(np.float32)

def apply_standardizer(x, stats):
    return np.clip((x - np.array(stats["mean"])) / np.array(stats["std"]), -10.0, 10.0).astype(np.float32)

def main():
    print("Loading test split episode IDs...")
    with open(os.path.join(OUTPUT_DIR, "splits", "test_episode_ids.json"), "r") as f:
        test_ids = set(json.load(f))

    print("Loading thresholds and normalization stats...")
    with open(os.path.join(OUTPUT_DIR, "models", "thresholds.json"), "r") as f:
        thresholds = json.load(f)
    with open(os.path.join(OUTPUT_DIR, "models", "normalization.json"), "r") as f:
        norm_stats = json.load(f)

    # Load model
    model = SeqRiskModel(hist_dim=21, action_dim=7, static_dim=43).to(device)
    model.load_state_dict(torch.load(os.path.join(OUTPUT_DIR, "models", "model.pt"), map_location=device))
    model.eval()

    print("Loading queries...")
    queries_path = os.path.join(DATASET_DIR, "query_records.jsonl")
    summaries_path = os.path.join(DATASET_DIR, "episode_summaries.jsonl")

    # Better mapping
    summaries_map = {}
    with open(summaries_path, "r") as f:
        for line in f:
            if not line.strip():
                continue
            ep = json.loads(line)
            summaries_map[(ep["task_id"], ep["reset_seed"])] = ep

    test_failed_episodes = {}
    test_success_episodes = {}

    with open(queries_path, "r") as f:
        for line in f:
            if not line.strip():
                continue
            q = json.loads(line)
            key = (q["task_id"], q["reset_seed"])
            if key in summaries_map:
                ep = summaries_map[key]
                global_id = ep["episode_index_global"]
                if global_id in test_ids:
                    if ep["success"]:
                        if global_id not in test_success_episodes:
                            test_success_episodes[global_id] = []
                        test_success_episodes[global_id].append(q)
                    else:
                        if global_id not in test_failed_episodes:
                            test_failed_episodes[global_id] = []
                        test_failed_episodes[global_id].append(q)

    # Sort queries by timestep
    for gid in test_failed_episodes:
        test_failed_episodes[gid].sort(key=lambda x: x["env_timestep"])
    for gid in test_success_episodes:
        test_success_episodes[gid].sort(key=lambda x: x["env_timestep"])

    print(f"Test split: {len(test_failed_episodes)} failed episodes, {len(test_success_episodes)} successful episodes.")

    # Function to compute predictions for an episode
    def get_episode_probs(queries):
        history_buffer = []
        probs = []
        for q in queries:
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

            # Apply standardization
            hist_norm = apply_seq_standardizer(hist, norm_stats["history"])
            action_norm = apply_seq_standardizer(action, norm_stats["action"])
            static_norm = apply_standardizer(static_base, norm_stats["static"])

            # Run inference
            batch = {
                "history": torch.tensor(hist_norm, dtype=torch.float32, device=device).unsqueeze(0),
                "action": torch.tensor(action_norm, dtype=torch.float32, device=device).unsqueeze(0),
                "static": torch.tensor(static_norm, dtype=torch.float32, device=device).unsqueeze(0),
            }
            with torch.no_grad():
                prob = torch.sigmoid(model(batch)).cpu().item()
            probs.append(prob)

            history_buffer.append((proprio, executed, ace))
        return probs

    # Evaluate early detection on failed episodes
    early_ratios = [0.10, 0.25, 0.50]
    threshold_keys = ["best_val_f1", "q95", "q90"]
    
    detection_results = {r: {k: 0 for k in threshold_keys} for r in early_ratios}

    for gid, queries in test_failed_episodes.items():
        probs = get_episode_probs(queries)
        N = len(probs)
        for r in early_ratios:
            cutoff = max(1, int(np.ceil(r * N)))
            early_probs = probs[:cutoff]
            max_prob = max(early_probs) if early_probs else 0.0
            for k in threshold_keys:
                th = thresholds[k]
                if max_prob >= th:
                    detection_results[r][k] += 1

    print("\n=== Early Failure Detection Rates on Test Split ===")
    for r in early_ratios:
        print(f"\nWithin first {int(r*100)}% of the episode steps:")
        for k in threshold_keys:
            count = detection_results[r][k]
            rate = count / len(test_failed_episodes) * 100
            print(f"  - Using threshold {k} ({thresholds[k]:.4f}): {rate:.2f}% detected ({count}/{len(test_failed_episodes)})")

if __name__ == "__main__":
    main()
