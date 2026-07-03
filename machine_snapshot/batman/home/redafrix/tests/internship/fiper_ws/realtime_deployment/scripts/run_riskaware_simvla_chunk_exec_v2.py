#!/usr/bin/env python3
import os
import sys
import argparse
import json
import random
import time
import fcntl
import hashlib
from pathlib import Path
import numpy as np
import torch
import torch.nn as nn

# Monkeypatch torch.load to bypass weights_only=True default in PyTorch 2.6+
orig_load = torch.load
torch.load = lambda *args, **kwargs: orig_load(*args, **{**kwargs, "weights_only": False})

# Set up paths for imports
REDA_WS = Path(os.environ.get("REDA_WS", "/home/rootalkhatib/test/reda_ws"))
os.environ["REDA_WS"] = str(REDA_WS)

# Include directories needed in PYTHONPATH
asynchvla_src = REDA_WS / "asynchvla_ws/src"
simvla_code = REDA_WS / "intern_ship_ws/simvla/code/SimVLA_modified"
libero_pro = REDA_WS / "intern_ship_ws/assets/repos/LIBERO-PRO"

for p in [asynchvla_src, simvla_code, libero_pro]:
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

try:
    from data_collection_stage9.libero_pro_env_utils import (
        make_env,
        obs_images,
        obs_to_proprio,
        reset_to_init,
    )
    from data_collection_stage9.simvla_candidate_sampler import load_simvla, sample_candidate
except ImportError as e:
    sys.path.append(str(Path(__file__).parent.parent.parent / "scripts"))
    from libero_pro_env_utils import (
        make_env,
        obs_images,
        obs_to_proprio,
        reset_to_init,
    )
    from simvla_candidate_sampler import load_simvla, sample_candidate

# Define SeqRiskModel
class SeqRiskModel(nn.Module):
    def __init__(self, kind, hist_dim, action_dim, static_dim, width=128, layers=2, heads=4, dropout=0.1):
        super().__init__()
        self.kind = kind
        self.hist_proj = nn.Linear(hist_dim, width)
        self.action_proj = nn.Linear(action_dim, width)
        if kind == "transformer":
            enc_layer = nn.TransformerEncoderLayer(width, heads, width * 4, dropout=dropout, batch_first=True, activation="gelu")
            self.cls = nn.Parameter(torch.zeros(1, 1, width))
            self.pos = nn.Parameter(torch.randn(1, 64, width) * 0.02)
            self.seq = nn.TransformerEncoder(enc_layer, layers)
        else:
            raise ValueError(f"Unsupported model kind: {kind}")
        self.static = nn.Sequential(nn.Linear(static_dim, width), nn.GELU())
        latent_dim = width * 2
        self.head = nn.Sequential(nn.LayerNorm(latent_dim), nn.Linear(latent_dim, width), nn.GELU(), nn.Dropout(dropout), nn.Linear(width, 1))

    def forward(self, batch):
        tokens = torch.cat([self.hist_proj(batch["history"]), self.action_proj(batch["action"])], dim=1)
        bsz = tokens.shape[0]
        tokens = torch.cat([self.cls.expand(bsz, -1, -1), tokens], dim=1)
        seq = self.seq(tokens + self.pos[:, : tokens.shape[1]])[:, 0]
        static = self.static(batch["static"])
        latent = torch.cat([seq, static], dim=-1)
        logits = self.head(latent).squeeze(-1)
        return logits, {}

def compute_ace_metrics(ace_chunks_normalized):
    chunks = np.asarray(ace_chunks_normalized, dtype=np.float32)
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
    return np.asarray([entropy, mean_pairwise, per_step_std, trans_std, rot_std, grip_std, flat_std], dtype=np.float32)

def get_action_seed(global_action_seed, reset_seed, episode_index, chunk_index, sample_index):
    hash_input = f"{global_action_seed}_{reset_seed}_{episode_index}_{chunk_index}_{sample_index}".encode()
    h = hashlib.sha256(hash_input).hexdigest()
    return int(h[:8], 16) % (2**31)

def generate_chunk(model, proc, lang, obs, seed, device, steps=10):
    img, wrist = obs_images(obs)
    prop = obs_to_proprio(obs)
    cand = sample_candidate(model, proc, lang, img, wrist, prop, seed=seed, device=device, steps=steps, flowtrace=False)
    chunk = cand['candidate_action_env'].numpy().astype(np.float32)
    norm = cand['candidate_action_normalized'].numpy().astype(np.float32)
    return chunk, norm

def apply_stats(x, stats):
    return np.clip((x - stats["mean"]) / stats["std"], -10.0, 10.0).astype(np.float32)

def evaluate_v2_strict(model, device, all_norms, prop, history_seq_norm, norm_stats, q95, q99, config):
    scores = []
    for idx in range(9):
        chunk = all_norms[idx]
        others = [all_norms[j] for j in range(9) if j != idx]
        ace_metrics = compute_ace_metrics(others)
        action_stats = np.concatenate([chunk[0], chunk.mean(axis=0), chunk.std(axis=0), chunk[-1] - chunk[0]]).astype(np.float32)
        static_feat = np.concatenate([action_stats, ace_metrics, prop]).astype(np.float32)
        
        batch = {
            "history": torch.tensor(history_seq_norm, dtype=torch.float32).unsqueeze(0).to(device),
            "action": torch.tensor(apply_stats(chunk, norm_stats["action"]), dtype=torch.float32).unsqueeze(0).to(device),
            "static": torch.tensor(apply_stats(static_feat, norm_stats["static"]), dtype=torch.float32).unsqueeze(0).to(device),
        }
        with torch.no_grad():
            logits, _ = model(batch)
            scores.append(float(torch.sigmoid(logits).cpu().item()))
    
    main_score = scores[0]
    best_idx = int(np.argmin(scores))
    best_score = scores[best_idx]
    
    min_imp = config.get("action_mod_min_improvement", 0.10)
    q99_min_imp = config.get("action_mod_q99_min_improvement", 0.15)
    
    cond_A = (best_idx != 0)
    cond_B = (main_score >= q95)
    cond_C = (main_score - best_score >= min_imp)
    cond_D = (best_score < q95) or (main_score >= q99 and main_score - best_score >= q99_min_imp)
    
    if cond_A and cond_B and cond_C and cond_D:
        return best_idx, True, "v2_strict_modification", scores
    return 0, False, "v2_strict_fallback_main", scores

def update_live_status(status_path, worker_id, episode_idx, success):
    lock_file = open(status_path.parent / "live_status.lock", "w")
    try:
        fcntl.flock(lock_file, fcntl.LOCK_EX)
        status = {}
        if status_path.exists():
            try:
                status = json.loads(status_path.read_text())
            except Exception:
                status = {}
        if "workers" not in status:
            status["workers"] = {}
        status["workers"][worker_id] = {"last_episode_idx": episode_idx, "success": success, "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S")}
        summaries_path = status_path.parent / "episode_summaries.jsonl"
        successes = total = 0
        if summaries_path.exists():
            with open(summaries_path, "r") as f:
                for line in f:
                    if line.strip():
                        data = json.loads(line)
                        total += 1
                        if data.get("success"): successes += 1
        status.update({"total_episodes_attempted": total, "total_successes": successes, "total_failures": total - successes, "success_rate": successes / total if total > 0 else 0.0, "last_updated": time.strftime("%Y-%m-%dT%H:%M:%S")})
        status_path.write_text(json.dumps(status, indent=2) + "\n")
    finally:
        fcntl.flock(lock_file, fcntl.LOCK_UN)
        lock_file.close()

def append_jsonl(path, data):
    with open(path, "a") as f:
        f.write(json.dumps(data) + "\n")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--num-episodes", type=int)
    parser.add_argument("--worker-id", required=True)
    args = parser.parse_args()

    config = json.loads(Path(args.config).read_text())
    suite, task_id, seeds = config["suite"], config["task_id"], config["seeds"]
    max_steps = config.get("max_steps", 300)
    global_action_seed = config.get("global_action_seed", 424242)
    
    out_dir = Path(config["output_dir"])
    out_dir.mkdir(parents=True, exist_ok=True)
    status_path, summaries_path, scores_path = out_dir / "live_status.json", out_dir / "episode_summaries.jsonl", out_dir / "chunk_scores.jsonl"
    
    fiper_ws = Path(__file__).parent.parent.parent
    job_dir = fiper_ws / config["risk_model_job_dir"]
    try:
        risk_config = json.loads((job_dir / "config.json").read_text())
    except FileNotFoundError:
        risk_config = {}
    thresholds = json.loads((job_dir / "thresholds.json" if (job_dir / "thresholds.json").exists() else job_dir / "policy_thresholds.json").read_text())
    norm_stats = json.loads((job_dir / "normalization.json").read_text())
    if "score" in thresholds:
        q95, q99 = thresholds["score"]["eventual"]["q95"], thresholds["score"]["eventual"]["q99"]
    else:
        q95, q99 = thresholds["q95"], thresholds["q99"]
    
    print(f"[{args.worker_id}] Loading models...", flush=True)
    simvla_model, simvla_proc, device = load_simvla()
    static_dim = len(norm_stats["static"]["mean"])
    risk_model = SeqRiskModel("transformer", 21, 7, static_dim, width=risk_config.get("width", 128), layers=risk_config.get("layers", 3), heads=risk_config.get("heads", 4), dropout=0.0).to(device)
    risk_model.load_state_dict(torch.load(job_dir / "model.pt", map_location=device))
    risk_model.eval()
    
    env, bundle = make_env(suite, task_id, resolution=128, seed=7)
    lang = bundle["task"].language
    
    num_episodes = args.num_episodes if args.num_episodes is not None else len(seeds)
    for ep_idx in range(num_episodes):
        reset_seed = seeds[ep_idx % len(seeds)]
        print(f"[{args.worker_id}] --- Episode {ep_idx} (Seed {reset_seed}) ---", flush=True)
        random.seed(reset_seed); np.random.seed(reset_seed); torch.manual_seed(reset_seed)
        obs = reset_to_init(env, bundle["init_states"][ep_idx % len(bundle["init_states"])], warmup=10)
        
        start_time, success, step_count, num_chunk_queries, mod_count, first_mod_idx, first_mod_ts = time.time(), False, 0, 0, 0, -1, -1
        history_buffer = [] # [{"proprio", "action", "ace"}]
        all_main_risks, all_selected_risks = [], []
        error_msg = "" # FIXED: Initialize error_msg to prevent UnboundLocalError on failure
        
        try:
            while step_count < max_steps and not success:
                num_chunk_queries += 1
                chunk_idx = num_chunk_queries - 1
                env_step_start = step_count
                
                # Sample 9 chunks
                seeds_list = [get_action_seed(global_action_seed, reset_seed, ep_idx, chunk_idx, i) for i in range(9)]
                assert len(set(seeds_list)) == 9, f"Seed collision detected: {seeds_list}"
                all_chunks, all_norms = [], []
                for s in seeds_list:
                    c, n = generate_chunk(simvla_model, simvla_proc, lang, obs, s, device)
                    all_chunks.append(c); all_norms.append(n)
                
                ace_metrics = compute_ace_metrics(all_norms[1:])
                prop = obs_to_proprio(obs)
                
                # Build history
                hist_steps = 16
                history_seq = np.zeros((hist_steps, 21), dtype=np.float32)
                for i in range(hist_steps):
                    t_prev = step_count - hist_steps + i
                    if 0 <= t_prev < len(history_buffer):
                        hb = history_buffer[t_prev]
                        history_seq[i] = np.concatenate([hb["proprio"], hb["action"], hb["ace"][:6]])
                history_seq_norm = apply_stats(history_seq, norm_stats["history"])
                
                # Select action (skip chunk 0 as requested)
                if chunk_idx == 0:
                    sel_idx, modified, reason = 0, False, "skip_chunk_0"
                    scores = [0.0] * 9
                else:
                    sel_idx, modified, reason, scores = evaluate_v2_strict(risk_model, device, all_norms, prop, history_seq_norm, norm_stats, q95, q99, config)
                
                if modified:
                    mod_count += 1
                    if first_mod_idx == -1: first_mod_idx, first_mod_ts = chunk_idx, step_count
                
                all_main_risks.append(scores[0]); all_selected_risks.append(scores[sel_idx])
                
                # Execute FULL chunk
                sel_chunk = all_chunks[sel_idx]
                actions_executed = 0
                for i in range(len(sel_chunk)):
                    prop_before = obs_to_proprio(obs)
                    step_count += 1
                    actions_executed += 1
                    act = sel_chunk[i].astype(np.float32)
                    obs, rew, done, info = env.step(act)
                    
                    history_buffer.append({"proprio": prop_before, "action": act, "ace": ace_metrics})
                    
                    success = success or bool(rew > 0)
                    if done or success: break
                
                append_jsonl(scores_path, {
                    "episode_index": ep_idx, "reset_seed": reset_seed, "chunk_index": chunk_idx, "env_step_start": env_step_start,
                    "main_action_seed": seeds_list[0], "ace_candidate_action_seeds": seeds_list[1:], "all_action_seeds_unique": bool(len(set(seeds_list)) == 9),
                    "main_risk_score": scores[0], "selected_risk_score": scores[sel_idx], "risk_score_all_candidates": scores,
                    "selected_candidate_index": sel_idx, "selected_action_source": "candidate_"+str(sel_idx) if sel_idx > 0 else "main_chunk",
                    "action_modified": bool(modified), "selected_reason": reason, "main_minus_selected_risk": scores[0] - scores[sel_idx],
                    "row_threshold_q95": q95, "row_threshold_q99": q99, "actions_executed_from_chunk": actions_executed, "success_after_chunk": bool(success), "done_after_chunk": bool(done)
                })
                if done or success: break
        except Exception as exc:
            error_msg = repr(exc); print(f"[{args.worker_id}] Error: {error_msg}")
            
        wall_time = time.time() - start_time
        append_jsonl(summaries_path, {
            "episode_index": ep_idx, "reset_seed": reset_seed, "outcome": "success" if success else "failure", "success": bool(success),
            "num_steps": step_count, "num_chunk_queries": num_chunk_queries, "wall_time_seconds": wall_time,
            "action_modifications_count": mod_count, "first_modification_chunk_index": first_mod_idx, "first_modification_timestep": first_mod_ts,
            "risk_score_min": float(np.min(all_main_risks)) if all_main_risks else 0, "risk_score_mean": float(np.mean(all_main_risks)) if all_main_risks else 0, "risk_score_max": float(np.max(all_main_risks)) if all_main_risks else 0,
            "selected_risk_min": float(np.min(all_selected_risks)) if all_selected_risks else 0, "selected_risk_mean": float(np.mean(all_selected_risks)) if all_selected_risks else 0, "selected_risk_max": float(np.max(all_selected_risks)) if all_selected_risks else 0,
            "seed_collisions": 0, "main_seed_collisions_with_ace": 0, "error_message": error_msg if not success else ""
        })
        update_live_status(status_path, args.worker_id, ep_idx, success)
        print(f"[{args.worker_id}] Result: {'Success' if success else 'Failure'}, Steps: {step_count}, Mods: {mod_count}")

    env.close()

if __name__ == "__main__":
    main()
