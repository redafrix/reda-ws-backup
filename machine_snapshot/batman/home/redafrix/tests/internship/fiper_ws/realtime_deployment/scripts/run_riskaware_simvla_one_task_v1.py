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
from typing import Any

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
    print(f"Import error: {e}. Trying local imports.")
    sys.path.append(str(Path(__file__).parent.parent.parent / "scripts"))
    from libero_pro_env_utils import (
        make_env,
        obs_images,
        obs_to_proprio,
        reset_to_init,
    )
    from simvla_candidate_sampler import load_simvla, sample_candidate

# Define SeqRiskModel exactly like the training code
class SeqRiskModel(nn.Module):
    def __init__(
        self,
        kind: str,
        hist_dim: int,
        action_dim: int,
        static_dim: int,
        width: int = 128,
        layers: int = 2,
        heads: int = 4,
        dropout: float = 0.1,
        survival_heads: bool = False,
        dynamics_residual: bool = False,
        num_groups: int = 1,
    ) -> None:
        super().__init__()
        self.kind = kind
        self.survival_heads = survival_heads
        self.dynamics_residual = dynamics_residual
        self.num_groups = num_groups

        self.hist_proj = nn.Linear(hist_dim, width)
        self.action_proj = nn.Linear(action_dim, width)

        if kind == "tcn":
            self.seq = nn.Sequential(
                nn.Conv1d(width, width, 3, padding=1),
                nn.GELU(),
                nn.Conv1d(width, width, 3, padding=2, dilation=2),
                nn.GELU(),
                nn.AdaptiveAvgPool1d(1),
            )
        elif kind in {"gru", "lstm"}:
            rnn_cls = nn.GRU if kind == "gru" else nn.LSTM
            self.seq = rnn_cls(width, width, num_layers=layers, dropout=dropout if layers > 1 else 0.0, batch_first=True)
        elif kind == "transformer":
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
        else:
            raise ValueError(f"unknown sequence model {kind}")

        self.static = nn.Sequential(nn.Linear(static_dim, width), nn.GELU())
        latent_dim = width * 2

        if self.dynamics_residual:
            self.dynamics_head = nn.Sequential(
                nn.Linear(latent_dim, width),
                nn.GELU(),
                nn.Linear(width, 8)
            )
            risk_input_dim = latent_dim + 1
        else:
            risk_input_dim = latent_dim

        out_dim = 4 if self.survival_heads else 1
        self.head = nn.Sequential(
            nn.LayerNorm(risk_input_dim),
            nn.Linear(risk_input_dim, width),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(width, out_dim)
        )

        if self.num_groups > 1:
            self.adv_head = nn.Sequential(
                nn.Linear(latent_dim, width),
                nn.GELU(),
                nn.Linear(width, num_groups)
            )

    def forward(self, batch: dict[str, torch.Tensor], alpha: float = 1.0) -> tuple[torch.Tensor, dict[str, torch.Tensor]]:
        tokens = torch.cat([self.hist_proj(batch["history"]), self.action_proj(batch["action"])], dim=1)
        if self.kind == "tcn":
            seq = self.seq(tokens.transpose(1, 2)).squeeze(-1)
        elif self.kind in {"gru", "lstm"}:
            _out, state = self.seq(tokens)
            if isinstance(state, tuple):
                state = state[0]
            seq = state[-1]
        elif self.kind == "transformer":
            bsz = tokens.shape[0]
            tokens = torch.cat([self.cls.expand(bsz, -1, -1), tokens], dim=1)
            seq = self.seq(tokens + self.pos[:, : tokens.shape[1]])[:, 0]
        else:
            raise ValueError(f"unknown sequence model {self.kind}")

        static = self.static(batch["static"])
        latent = torch.cat([seq, static], dim=-1)

        outputs = {}

        if self.dynamics_residual:
            pred_delta = self.dynamics_head(latent)
            outputs["pred_delta"] = pred_delta
            if "delta_proprio" in batch:
                true_delta = batch["delta_proprio"]
                residual_norm = torch.norm(pred_delta - true_delta, p=2, dim=-1, keepdim=True)
                outputs["residual_norm"] = residual_norm
                risk_input = torch.cat([latent, residual_norm.detach()], dim=-1)
            else:
                risk_input = torch.cat([latent, torch.zeros((latent.shape[0], 1), device=latent.device)], dim=-1)
        else:
            risk_input = latent

        logits = self.head(risk_input)

        if self.num_groups > 1:
            group_logits = self.adv_head(latent)
            outputs["group_logits"] = group_logits

        if not self.survival_heads:
            logits = logits.squeeze(-1)

        return logits, outputs

def compute_ace_metrics(ace_chunks_normalized: Any) -> np.ndarray:
    chunks = np.asarray(ace_chunks_normalized, dtype=np.float32)
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
    return np.asarray([entropy, mean_pairwise, per_step_std, trans_std, rot_std, grip_std, flat_std], dtype=np.float32)

def generate_chunk(model, proc, lang, obs, seed: int, device, steps: int = 10):
    img, wrist = obs_images(obs)
    prop = obs_to_proprio(obs)
    cand = sample_candidate(model, proc, lang, img, wrist, prop, seed=seed, device=device, steps=steps, flowtrace=False)
    chunk = cand['candidate_action_env'].numpy().astype(np.float32)
    norm = cand['candidate_action_normalized'].numpy().astype(np.float32)
    return chunk, norm

def apply_standardizer(x: np.ndarray, stats: dict[str, np.ndarray]) -> np.ndarray:
    return np.clip((x - stats["mean"]) / stats["std"], -10.0, 10.0).astype(np.float32)

def apply_seq_standardizer(x: np.ndarray, stats: dict[str, np.ndarray]) -> np.ndarray:
    return np.clip((x - stats["mean"]) / stats["std"], -10.0, 10.0).astype(np.float32)

def update_live_status(status_path, worker_id, success, attempted, successes):
    lock_file = open(status_path.parent / "live_status.lock", "w")
    try:
        fcntl.flock(lock_file, fcntl.LOCK_EX)
        status = {
            "workers": {
                worker_id: {
                    "last_episode_idx": 0,
                    "success": success,
                    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S")
                }
            },
            "total_episodes_attempted": attempted,
            "total_successes": successes,
            "total_failures": attempted - successes,
            "success_rate": successes / attempted if attempted > 0 else 0.0,
            "last_updated": time.strftime("%Y-%m-%dT%H:%M:%S")
        }
        status_path.write_text(json.dumps(status, indent=2) + "\n")
    finally:
        fcntl.flock(lock_file, fcntl.LOCK_UN)
        lock_file.close()

# Deterministic Reproducible Seed Generator
def get_action_seed(global_run_seed: int, episode_index: int, timestep: int, sample_index: int) -> int:
    hash_input = f"seed_{global_run_seed}_{episode_index}_{timestep}_{sample_index}".encode()
    h = hashlib.sha256(hash_input).hexdigest()
    return int(h[:8], 16) % (2**32)

# Future Action Selection Policy Design: risk_filtered_lowest_score_candidate_v1
def evaluate_risk_filtered_policy(
    model, device, main_norm, ace_chunks_norm, prop, history_seq_norm, norm_stats, row_threshold
):
    all_chunks = [main_norm] + [np.asarray(c) for c in ace_chunks_norm]
    candidate_scores = []
    
    for idx in range(9):
        chunk_to_score = all_chunks[idx]
        other_chunks = [all_chunks[j] for j in range(9) if j != idx]
        ace_metrics_idx = compute_ace_metrics(other_chunks)
        
        action_stats_idx = np.concatenate([
            chunk_to_score[0],
            chunk_to_score.mean(axis=0),
            chunk_to_score.std(axis=0),
            (chunk_to_score[-1] - chunk_to_score[0])
        ]).astype(np.float32)
        
        static_feat_idx = np.concatenate([action_stats_idx, ace_metrics_idx, prop]).astype(np.float32)
        action_seq_norm_idx = apply_seq_standardizer(chunk_to_score.astype(np.float32), norm_stats["action"])
        static_feat_norm_idx = apply_standardizer(static_feat_idx, norm_stats["static"])
        
        batch_idx = {
            "history": torch.tensor(history_seq_norm, dtype=torch.float32).unsqueeze(0).to(device),
            "action": torch.tensor(action_seq_norm_idx, dtype=torch.float32).unsqueeze(0).to(device),
            "static": torch.tensor(static_feat_norm_idx, dtype=torch.float32).unsqueeze(0).to(device),
        }
        
        with torch.no_grad():
            logits, _ = model(batch_idx)
            score_idx = float(torch.sigmoid(logits).cpu().item())
        candidate_scores.append(score_idx)
        
    main_risk_score = candidate_scores[0]
    if main_risk_score < row_threshold:
        selected_idx = 0
        selected_reason = "main_chunk_safe"
    else:
        selected_idx = int(np.argmin(candidate_scores))
        selected_reason = "fallback_lowest_risk"
        
    selected_risk_score = candidate_scores[selected_idx]
    action_modified = (selected_idx != 0)
    
    return {
        "action_modified": action_modified,
        "selected_candidate_index": selected_idx,
        "main_risk_score": main_risk_score,
        "selected_risk_score": selected_risk_score,
        "risk_score_all_candidates": candidate_scores,
        "selected_reason": selected_reason
    }

def evaluate_risk_filtered_policy_v2_strict(
    model, device, main_norm, ace_chunks_norm, prop, history_seq_norm, norm_stats, q95, q99, config
):
    all_chunks = [main_norm] + [np.asarray(c) for c in ace_chunks_norm]
    candidate_scores = []
    
    for idx in range(9):
        chunk_to_score = all_chunks[idx]
        other_chunks = [all_chunks[j] for j in range(9) if j != idx]
        ace_metrics_idx = compute_ace_metrics(other_chunks)
        
        action_stats_idx = np.concatenate([
            chunk_to_score[0],
            chunk_to_score.mean(axis=0),
            chunk_to_score.std(axis=0),
            (chunk_to_score[-1] - chunk_to_score[0])
        ]).astype(np.float32)
        
        static_feat_idx = np.concatenate([action_stats_idx, ace_metrics_idx, prop]).astype(np.float32)
        action_seq_norm_idx = apply_seq_standardizer(chunk_to_score.astype(np.float32), norm_stats["action"])
        static_feat_norm_idx = apply_standardizer(static_feat_idx, norm_stats["static"])
        
        batch_idx = {
            "history": torch.tensor(history_seq_norm, dtype=torch.float32).unsqueeze(0).to(device),
            "action": torch.tensor(action_seq_norm_idx, dtype=torch.float32).unsqueeze(0).to(device),
            "static": torch.tensor(static_feat_norm_idx, dtype=torch.float32).unsqueeze(0).to(device),
        }
        
        with torch.no_grad():
            logits, _ = model(batch_idx)
            score_idx = float(torch.sigmoid(logits).cpu().item())
        candidate_scores.append(score_idx)
        
    main_score = candidate_scores[0]
    best_idx = int(np.argmin(candidate_scores))
    best_score = candidate_scores[best_idx]
    
    min_improvement = config.get("action_mod_min_improvement", 0.10)
    q99_min_improvement = config.get("action_mod_q99_min_improvement", 0.15)
    
    # Check conditions A, B, C, D
    cond_A = (best_idx != 0)
    cond_B = (main_score >= q95)
    cond_C = (main_score - best_score >= min_improvement)
    
    cond_D_1 = (best_score < q95)
    cond_D_2 = (main_score >= q99 and main_score - best_score >= q99_min_improvement)
    cond_D = (cond_D_1 or cond_D_2)
    
    if cond_A and cond_B and cond_C and cond_D:
        selected_idx = best_idx
        action_modified = True
        selected_reason = "v2_strict_modification"
    else:
        selected_idx = 0
        action_modified = False
        selected_reason = "v2_strict_fallback_main"
        
    selected_risk_score = candidate_scores[selected_idx]
    
    return {
        "action_modified": action_modified,
        "selected_candidate_index": selected_idx,
        "main_risk_score": main_score,
        "selected_risk_score": selected_risk_score,
        "risk_score_all_candidates": candidate_scores,
        "selected_reason": selected_reason
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True, help="Path to config JSON")
    parser.add_argument("--num-episodes", type=int, default=1, help="Number of episodes to run")
    parser.add_argument("--episode-offset", type=int, default=0, help="Starting episode index (for multi-worker runs)")
    parser.add_argument("--worker-id", required=True, help="Worker identifier")
    args = parser.parse_args()

    # 1. Load config
    config_path = Path(args.config)
    config = json.loads(config_path.read_text())
    
    suite = config["suite"]
    task_id = config["task_id"]
    max_steps = config.get("max_steps", 300)
    output_dir = Path(config["output_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "logs").mkdir(parents=True, exist_ok=True)
    
    status_path = output_dir / "live_status.json"
    # Per-worker output files to avoid clobbering in multi-worker runs
    worker_suffix = str(args.worker_id).replace("/", "_")
    scores_path = output_dir / f"step_scores_w{worker_suffix}.jsonl"
    summary_path = output_dir / f"episode_summary_w{worker_suffix}.jsonl"
    
    # Clean previous scores for THIS worker only
    if scores_path.exists():
        scores_path.unlink()
    if summary_path.exists():
        summary_path.unlink()
        
    # 2. Check for baseline risk model directory and artifacts
    fiper_ws_dir = Path(__file__).parent.parent.parent
    job_dir = fiper_ws_dir / config["risk_model_job_dir"]
    if not (job_dir / "model.pt").exists() or not (job_dir / "config.json").exists():
        fallback_job_dir = fiper_ws_dir / config["fallback_risk_model_job_dir"]
        print(f"Global detector model not found at {job_dir}. Checking fallback: {fallback_job_dir}")
        job_dir = fallback_job_dir

    print(f"Selected Risk Model Job Dir: {job_dir}")
    
    # Verify required deployment files
    required_files = ["model.pt", "config.json", "FEATURE_AUDIT.json"]
    for rf in required_files:
        if not (job_dir / rf).exists():
            print(f"MISSING_DEPLOYMENT_ARTIFACTS = YES. Missing file: {rf}")
            sys.exit(1)
            
    threshold_file = job_dir / "thresholds.json"
    if not threshold_file.exists():
        threshold_file = job_dir / "policy_thresholds.json"
    if not threshold_file.exists():
        print("MISSING_DEPLOYMENT_ARTIFACTS = YES. Missing threshold file.")
        sys.exit(1)
        
    # Check for normalization/standardization statistics files
    stats_file = None
    for sf in ["normalization.json", "stats.json", "standardizer.json", "standardization.json"]:
        if (job_dir / sf).exists():
            stats_file = job_dir / sf
            break
            
    if stats_file is None:
        print("MISSING_DEPLOYMENT_ARTIFACTS = YES. Standardization/normalization statistics files are missing from the job dir!")
        sys.exit(1)
        
    print(f"Loading normalization statistics from: {stats_file}")
    norm_stats = json.loads(stats_file.read_text())
    
    # Load model config and thresholds
    risk_config = json.loads((job_dir / "config.json").read_text())
    thresholds = json.loads(threshold_file.read_text())
    
    # Extract conformal mass thresholds & event score threshold q95 / q99
    row_threshold_q95 = thresholds["score"]["eventual"]["q95"]
    row_threshold_q99 = thresholds["score"]["eventual"]["q99"]
    conformal_mass_threshold = thresholds.get("policy", {}).get("conformal_threshold", 0.15)
    
    print(f"Row threshold q95: {row_threshold_q95}")
    print(f"Row threshold q99: {row_threshold_q99}")
    print(f"Conformal mass threshold: {conformal_mass_threshold}")
    
    # 3. Load SimVLA
    print(f"[{args.worker_id}] Loading SimVLA model...", flush=True)
    simvla_model, simvla_proc, device = load_simvla()
    print(f"[{args.worker_id}] SimVLA model loaded on {device}.", flush=True)
    
    # 4. Load Risk Model
    print(f"[{args.worker_id}] Loading SeqRiskModel...", flush=True)
    history_steps = int(risk_config.get("history_steps", 16))
    
    hist_dim = 21 # [proprio(8), action(7), ace[:6](6)]
    action_dim = 7 # sequence tokens 10x7
    static_dim = 43 # action_stats(28) + ace(7) + proprio(8)
    
    risk_model = SeqRiskModel(
        kind=str(risk_config.get("model", "transformer")).replace("seq_", ""),
        hist_dim=hist_dim,
        action_dim=action_dim,
        static_dim=static_dim,
        width=int(risk_config.get("width", 128)),
        layers=int(risk_config.get("layers", 3)),
        heads=int(risk_config.get("heads", 4)),
        dropout=0.0,
        survival_heads=False,
        dynamics_residual=False
    )
    
    risk_model.load_state_dict(torch.load(job_dir / "model.pt", map_location="cpu"))
    risk_model = risk_model.to(device)
    risk_model.eval()
    print(f"[{args.worker_id}] SeqRiskModel loaded successfully.", flush=True)
    
    # 5. Create Environment
    print(f"[{args.worker_id}] Creating environment for {suite}_t{task_id}...", flush=True)
    env, bundle = make_env(suite, task_id, resolution=128, seed=7)
    init_states = bundle["init_states"]
    lang = bundle["task"].language
    print(f"[{args.worker_id}] BDDL task prompt: '{lang}'", flush=True)
    
    seeds = config.get("seeds", [10000])
    
    # Deterministic worker RNG initialization
    try:
        worker_offset = int(args.worker_id)
    except ValueError:
        worker_offset = int(hashlib.md5(args.worker_id.encode()).hexdigest(), 16) % 1000
    
    global_action_seed = config.get("global_action_seed", 424242)
    enforce_unique_action_seeds_per_timestep = config.get("enforce_unique_action_seeds_per_timestep", True)
    ace_candidate_count = config.get("ace_candidate_count", 8)
    
    if enforce_unique_action_seeds_per_timestep:
        rng = np.random.default_rng(global_action_seed + worker_offset)
    
    successes = 0
    attempted = 0
    
    total_timesteps_checked = 0
    total_seed_collisions = 0
    total_main_seed_collisions_with_ace = 0
    
    for local_ep_idx in range(args.num_episodes):
        global_ep_idx = args.episode_offset + local_ep_idx
        reset_seed = seeds[global_ep_idx % len(seeds)]
        print(f"[{args.worker_id}] --- Starting Episode {global_ep_idx} (local {local_ep_idx}, Reset Seed {reset_seed}) ---", flush=True)
        
        start_time = time.time()
        
        # Reset env
        init_state_to_use = init_states[global_ep_idx % len(init_states)]
        obs = reset_to_init(env, init_state_to_use, warmup=10)
        
        success = False
        step_count = 0
        error_msg = ""
        
        # Online history buffer
        history_buffer = [] # list of dicts: {"proprio": np.ndarray(8), "action": np.ndarray(7), "ace": np.ndarray(6)}
        
        conformal_mass = 0.0
        alarm_triggered = False
        alarm_timestep = -1
        
        episode_scores = []
        
        # Action modification metrics
        episode_action_modifications_count = 0
        first_modification_timestep = -1
        episode_main_risks = []
        episode_selected_risks = []
        
        try:
            for t in range(max_steps):
                step_count += 1
                
                # 1. Generate seeds
                if enforce_unique_action_seeds_per_timestep:
                    total_required_seeds = 1 + ace_candidate_count
                    while True:
                        proposed_seeds = [int(rng.integers(0, 2**31 - 1)) for _ in range(total_required_seeds)]
                        if len(set(proposed_seeds)) == total_required_seeds:
                            break
                    main_seed = proposed_seeds[0]
                    candidate_seeds = proposed_seeds[1:]
                else:
                    main_seed = get_action_seed(reset_seed, ep_idx, t, 0)
                    candidate_seeds = [get_action_seed(reset_seed, ep_idx, t, i) for i in range(1, 1 + ace_candidate_count)]
                
                # Log seeds to console for trace
                print(f"[{args.worker_id}] Step {t} Seeds: main={main_seed}, ace={candidate_seeds}", flush=True)
                
                # 2. Strict seed collision validations
                all_seeds = [main_seed] + candidate_seeds
                unique_seeds = set(all_seeds)
                
                seed_collision_detected = False
                all_action_seeds_unique = True
                
                total_timesteps_checked += 1
                
                # Check for duplicate seeds among candidates or main
                if len(unique_seeds) != len(all_seeds):
                    seed_collision_detected = True
                    all_action_seeds_unique = False
                    total_seed_collisions += 1
                    print(f"[{args.worker_id}] SEED COLLISION: Duplicate seeds found at timestep {t}! {all_seeds}")
                    raise ValueError(f"Seed collision detected! Seeds: {all_seeds}")
                    
                # Check for collision between main_seed and any ACE seed
                if main_seed in candidate_seeds:
                    seed_collision_detected = True
                    all_action_seeds_unique = False
                    total_main_seed_collisions_with_ace += 1
                    print(f"[{args.worker_id}] SEED COLLISION: main_seed {main_seed} collides with ACE seeds {candidate_seeds}!")
                    raise ValueError(f"Main seed {main_seed} collides with candidate seeds {candidate_seeds}")
                
                # 3. Observe current state
                prop = obs_to_proprio(obs)
                
                # 4. Sample main action chunk from SimVLA
                main_chunk, main_norm = generate_chunk(simvla_model, simvla_proc, lang, obs, seed=main_seed, device=device, steps=10)
                
                # 5. Sample 8 extra candidate chunks from the same observation for ACE
                ace_chunks = []
                ace_chunks_norm = []
                for cs in candidate_seeds:
                    chunk_c, norm_c = generate_chunk(simvla_model, simvla_proc, lang, obs, seed=cs, device=device, steps=10)
                    ace_chunks.append(chunk_c)
                    ace_chunks_norm.append(norm_c)
                    
                # Compute ACE metrics
                ace_metrics = compute_ace_metrics(ace_chunks_norm)
                ace_entropy = float(ace_metrics[0])
                
                # 6. Build online features
                action_stats = np.concatenate([
                    main_norm[0],
                    main_norm.mean(axis=0),
                    main_norm.std(axis=0),
                    (main_norm[-1] - main_norm[0])
                ]).astype(np.float32)
                
                history_seq = np.zeros((history_steps, 21), dtype=np.float32)
                hist_len = len(history_buffer)
                for i in range(history_steps):
                    t_prev = t - history_steps + i
                    if t_prev >= 0 and t_prev < hist_len:
                        hb = history_buffer[t_prev]
                        history_seq[i, :] = np.concatenate([hb["proprio"], hb["action"], hb["ace"][:6]])
                        
                action_seq = main_norm.astype(np.float32)
                static_feat = np.concatenate([action_stats, ace_metrics, prop]).astype(np.float32)
                
                # Standardize features
                history_seq_norm = apply_seq_standardizer(history_seq, norm_stats["history"])
                action_seq_norm = apply_seq_standardizer(action_seq, norm_stats["action"])
                static_feat_norm = apply_standardizer(static_feat, norm_stats["static"])
                
                # 7. Run risk model
                batch = {
                    "history": torch.tensor(history_seq_norm, dtype=torch.float32).unsqueeze(0).to(device),
                    "action": torch.tensor(action_seq_norm, dtype=torch.float32).unsqueeze(0).to(device),
                    "static": torch.tensor(static_feat_norm, dtype=torch.float32).unsqueeze(0).to(device),
                }
                
                with torch.no_grad():
                    logits, _ = risk_model(batch)
                    risk_score = float(torch.sigmoid(logits).cpu().item())
                    
                # 8. Update conformal mass online
                excess_t = max(0.0, risk_score - row_threshold_q95)
                conformal_mass += excess_t
                
                alarm_boolean = conformal_mass >= conformal_mass_threshold
                if alarm_boolean and not alarm_triggered:
                    alarm_triggered = True
                    alarm_timestep = t
                    print(f"[{args.worker_id}] ALARM BREACH at step {t}! Conformal mass {conformal_mass:.4f} >= {conformal_mass_threshold}")
                
                # 9. Evaluate the future action selection policy design (lowest risk)
                action_selection_policy = config.get("action_selection_policy", "passive_monitor_only")
                modify_actions = config.get("modify_actions", False)
                
                if action_selection_policy == "risk_filtered_lowest_score_candidate_v2_strict_margin":
                    policy_info = evaluate_risk_filtered_policy_v2_strict(
                        risk_model, device, main_norm, ace_chunks_norm, prop, history_seq_norm, norm_stats, row_threshold_q95, row_threshold_q99, config
                    )
                else:
                    policy_info = evaluate_risk_filtered_policy(
                        risk_model, device, main_norm, ace_chunks_norm, prop, history_seq_norm, norm_stats, row_threshold_q95
                    )
                
                if modify_actions:
                    if action_selection_policy in ["risk_filtered_lowest_score_candidate_v2_strict_margin", "risk_filtered_lowest_score_candidate_v1"]:
                        selected_idx = policy_info["selected_candidate_index"]
                        all_chunks_denorm = [main_chunk] + ace_chunks
                        act_to_execute = all_chunks_denorm[selected_idx]
                        selected_action_source = f"candidate_{selected_idx}" if selected_idx > 0 else "main_chunk"
                        action_modified = policy_info["action_modified"]
                        selected_reason = policy_info["selected_reason"]
                        selected_risk_score = policy_info["selected_risk_score"]
                    else:
                        act_to_execute = main_chunk
                        selected_action_source = "main_chunk"
                        action_modified = False
                        selected_reason = "passive_monitor_only"
                        selected_risk_score = risk_score
                else:
                    act_to_execute = main_chunk
                    selected_action_source = "main_chunk"
                    action_modified = False
                    selected_reason = "passive_monitor_only"
                    selected_risk_score = risk_score
                
                if action_modified:
                    episode_action_modifications_count += 1
                    if first_modification_timestep == -1:
                        first_modification_timestep = t
                
                episode_main_risks.append(risk_score)
                episode_selected_risks.append(selected_risk_score)
                
                # Log step score to jsonl
                step_score_row = {
                    "timestep": t,
                    "reset_seed": reset_seed,
                    "main_action_seed": int(main_seed),
                    "ace_candidate_action_seeds": [int(s) for s in candidate_seeds],
                    "all_action_seeds_unique": all_action_seeds_unique,
                    "seed_collision_detected": seed_collision_detected,
                    "main_risk_score": risk_score,
                    "selected_risk_score": selected_risk_score,
                    "risk_score_all_candidates": policy_info["risk_score_all_candidates"],
                    "selected_candidate_index": policy_info["selected_candidate_index"],
                    "selected_action_source": selected_action_source,
                    "action_modified": action_modified,
                    "selected_reason": selected_reason,
                    "main_minus_selected_risk": float(risk_score - selected_risk_score),
                    "row_threshold_q95": row_threshold_q95,
                    "row_threshold_q99": row_threshold_q99,
                    "conformal_mass": conformal_mass,
                    "alarm_boolean": alarm_boolean
                }
                
                with open(scores_path, "a") as f:
                    f.write(json.dumps(step_score_row) + "\n")
                    
                episode_scores.append(risk_score)
                
                # 10. Execute chosen chunk's first action
                act = act_to_execute[0].astype(np.float32)
                obs, rew, done, info = env.step(act)
                
                # 11. Update history buffer
                history_buffer.append({
                    "proprio": prop.astype(np.float32),
                    "action": act.astype(np.float32),
                    "ace": ace_metrics.astype(np.float32)
                })
                
                success = success or bool(rew > 0)
                if done or success:
                    break
                    
        except Exception as exc:
            error_msg = repr(exc)
            print(f"[{args.worker_id}] Error in episode {global_ep_idx}: {error_msg}", flush=True)
            
        wall_time = time.time() - start_time
        outcome = "success" if success else "failure_or_timeout"
        if success:
            successes += 1
        attempted += 1
        
        # Log episode summary
        ep_summary = {
            "episode_index": global_ep_idx,
            "worker_id": args.worker_id,
            "reset_seed": reset_seed,
            "outcome": outcome,
            "success": success,
            "num_steps": step_count,
            "wall_time_seconds": wall_time,
            
            # Action modification stats
            "action_modifications_count": episode_action_modifications_count,
            "first_modification_timestep": first_modification_timestep,
            
            # Main risk stats
            "risk_score_min": float(np.min(episode_main_risks)) if episode_main_risks else 0.0,
            "risk_score_mean": float(np.mean(episode_main_risks)) if episode_main_risks else 0.0,
            "risk_score_max": float(np.max(episode_main_risks)) if episode_main_risks else 0.0,
            
            # Selected risk stats
            "selected_risk_min": float(np.min(episode_selected_risks)) if episode_selected_risks else 0.0,
            "selected_risk_mean": float(np.mean(episode_selected_risks)) if episode_selected_risks else 0.0,
            "selected_risk_max": float(np.max(episode_selected_risks)) if episode_selected_risks else 0.0,
            
            "mean_main_minus_selected_risk": float(np.mean([m - s for m, s in zip(episode_main_risks, episode_selected_risks)])) if episode_main_risks else 0.0,
            
            "timesteps_seed_checked": total_timesteps_checked,
            "seed_collisions": total_seed_collisions,
            "main_seed_collisions_with_ace": total_main_seed_collisions_with_ace,
            "error_message": error_msg
        }
        
        # Append episode summary as JSONL (one line per episode) for multi-worker safety
        with open(summary_path, "a") as f:
            f.write(json.dumps(ep_summary) + "\n")
        update_live_status(status_path, args.worker_id, success, attempted, successes)
        
        print(f"[{args.worker_id}] Episode {global_ep_idx} finished. Steps: {step_count}. Outcome: {outcome}. Time: {wall_time:.1f}s", flush=True)

    env.close()
    print(f"[{args.worker_id}] Smoke test run completed. Checked {total_timesteps_checked} timesteps. Seed collisions: {total_seed_collisions}.", flush=True)

if __name__ == "__main__":
    main()
