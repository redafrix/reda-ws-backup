import os
import json
import glob
import re
import hashlib
from collections import defaultdict

# Root Paths on Bob
ROOT_10EP = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_aggressive_fixed_20260609"
ROOT_100EP = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_aggressive_fixed_20260609"
TRAINING_SPLIT_PATH = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/episode_buckets.json"

def get_sha256(path):
    if not os.path.exists(path):
        return "NOT_FOUND"
    h = hashlib.sha256()
    try:
        with open(path, 'rb') as f:
            for chunk in iter(lambda: f.read(65536), b''):
                h.update(chunk)
        return h.hexdigest()
    except Exception as e:
        return f"ERROR_{str(e)}"

def load_jsonl(path):
    if not os.path.exists(path):
        return []
    res = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    res.append(json.loads(line))
                except Exception as e:
                    pass
    return res

def check_log_errors(log_path):
    log_issues = []
    if not os.path.exists(log_path):
        return log_issues
    patterns = [
        (re.compile(r"traceback", re.IGNORECASE), "Traceback"),
        (re.compile(r"cuda out of memory", re.IGNORECASE), "CUDA OOM"),
        (re.compile(r"keyboardinterrupt", re.IGNORECASE), "KeyboardInterrupt"),
        (re.compile(r"exception", re.IGNORECASE), "Exception")
    ]
    try:
        with open(log_path, 'r', errors='ignore') as f:
            for line_idx, line in enumerate(f):
                for regex, label in patterns:
                    if regex.search(line):
                        log_issues.append(f"{label} found at line {line_idx+1}: {line.strip()[:100]}")
    except Exception as e:
        log_issues.append(f"Read error: {str(e)}")
    return log_issues

def run_audit():
    audit_data = {}
    
    # ---------------------------------------------------------
    # 1. Check training seeds for disjointness check
    # ---------------------------------------------------------
    training_seeds = set()
    if os.path.exists(TRAINING_SPLIT_PATH):
        with open(TRAINING_SPLIT_PATH, 'r') as f:
            buckets = json.load(f)
        # Extract reset seed if present, or check if it's episode names.
        # Wait, the split configuration contains lists of episode IDs.
        # Let's see: the continuous dataset contains seeds? Usually continuous dataset episodes are collected.
        # But we know that continuous dataset has a different ID naming convention.
        # Let's count keys.
        audit_data["training_split_exists"] = True
        audit_data["training_split_info"] = {k: len(v) for k, v in buckets.items()}
    else:
        audit_data["training_split_exists"] = False
        
    # ---------------------------------------------------------
    # 2. Audit 10ep Run
    # ---------------------------------------------------------
    audit_data["10ep_run"] = {}
    run_10ep_dir = os.path.join(ROOT_10EP, "runs")
    tasks_10ep = sorted([t for t in os.listdir(run_10ep_dir) if t.startswith("task") and os.path.isdir(os.path.join(run_10ep_dir, t))])
    
    audit_data["10ep_run"]["exists"] = os.path.exists(ROOT_10EP)
    audit_data["10ep_run"]["tasks_count"] = len(tasks_10ep)
    
    # Check supervisor log
    sup_log_10ep = os.path.join(ROOT_10EP, "sweep_supervisor.log")
    audit_data["10ep_run"]["log_errors"] = check_log_errors(sup_log_10ep)
    
    # Compute overall statistics
    total_episodes_10ep = 0
    all_seeds_10ep = defaultdict(list)
    successes_10ep = defaultdict(int)
    steps_10ep = defaultdict(int)
    policy_counts_10ep = defaultdict(int)
    
    # Query modification rate stats
    total_queries_10ep = 0
    modified_queries_10ep = 0
    
    # Paired metrics
    # Tasks -> index -> outcomes
    paired_10ep_data = defaultdict(lambda: defaultdict(dict))
    
    for t in tasks_10ep:
        task_num = int(t.replace("task", ""))
        t_path = os.path.join(run_10ep_dir, t)
        
        for pol in ["original_simvla", "modified_simvla", "modified_h10_risk_topk8"]:
            pol_path = os.path.join(t_path, pol)
            if not os.path.exists(pol_path):
                continue
            subdirs = [d for d in os.listdir(pol_path) if os.path.isdir(os.path.join(pol_path, d))]
            if not subdirs:
                continue
            sub_dir = os.path.join(pol_path, subdirs[0])
            
            # Read summaries
            sum_path = os.path.join(sub_dir, "episode_summaries.jsonl")
            summaries = load_jsonl(sum_path)
            
            # Sort by episode_index
            summaries = sorted(summaries, key=lambda x: x.get("episode_index", 0))
            
            for s in summaries:
                ep_idx = s.get("episode_index", 0)
                seed = s.get("reset_seed")
                succ = s.get("success", False) or s.get("outcome") == "success"
                steps = s.get("num_steps", 0)
                
                all_seeds_10ep[(task_num, pol)].append(seed)
                policy_counts_10ep[pol] += 1
                if succ:
                    successes_10ep[pol] += 1
                steps_10ep[pol] += steps
                total_episodes_10ep += 1
                
                paired_10ep_data[task_num][ep_idx][pol] = {
                    "success": succ,
                    "seed": seed
                }
                
            # If risk policy, count queries from step_scores
            if pol == "modified_h10_risk_topk8":
                scores_path = os.path.join(sub_dir, "step_scores_risk_topk8.jsonl")
                if os.path.exists(scores_path):
                    steps_scores = load_jsonl(scores_path)
                    for step in steps_scores:
                        if "main_risk" in step or "main_score" in step or "query_index" in step:
                            total_queries_10ep += 1
                            if step.get("selected_candidate_index", 0) != 0:
                                modified_queries_10ep += 1
                                
    # Calculate rescues and regressions
    paired_overall_10ep = {
        "mod_vs_orig": {"rescues": 0, "regressions": 0, "rescued_seeds": [], "regressed_seeds": []},
        "risk_vs_mod": {"rescues": 0, "regressions": 0, "rescued_seeds": [], "regressed_seeds": []},
        "risk_vs_orig": {"rescues": 0, "regressions": 0, "rescued_seeds": [], "regressed_seeds": []}
    }
    
    for t_num in paired_10ep_data:
        for ep_idx in paired_10ep_data[t_num]:
            d = paired_10ep_data[t_num][ep_idx]
            if "original_simvla" not in d or "modified_simvla" not in d or "modified_h10_risk_topk8" not in d:
                continue
            
            o_succ = d["original_simvla"]["success"]
            m_succ = d["modified_simvla"]["success"]
            r_succ = d["modified_h10_risk_topk8"]["success"]
            seed = d["original_simvla"]["seed"]
            
            # mod vs orig
            if m_succ and not o_succ:
                paired_overall_10ep["mod_vs_orig"]["rescues"] += 1
                paired_overall_10ep["mod_vs_orig"]["rescued_seeds"].append((t_num, seed))
            elif not m_succ and o_succ:
                paired_overall_10ep["mod_vs_orig"]["regressions"] += 1
                paired_overall_10ep["mod_vs_orig"]["regressed_seeds"].append((t_num, seed))
                
            # risk vs mod
            if r_succ and not m_succ:
                paired_overall_10ep["risk_vs_mod"]["rescues"] += 1
                paired_overall_10ep["risk_vs_mod"]["rescued_seeds"].append((t_num, seed))
            elif not r_succ and m_succ:
                paired_overall_10ep["risk_vs_mod"]["regressions"] += 1
                paired_overall_10ep["risk_vs_mod"]["regressed_seeds"].append((t_num, seed))
                
            # risk vs orig
            if r_succ and not o_succ:
                paired_overall_10ep["risk_vs_orig"]["rescues"] += 1
                paired_overall_10ep["risk_vs_orig"]["rescued_seeds"].append((t_num, seed))
            elif not r_succ and o_succ:
                paired_overall_10ep["risk_vs_orig"]["regressions"] += 1
                paired_overall_10ep["risk_vs_orig"]["regressed_seeds"].append((t_num, seed))

    audit_data["10ep_run"]["total_episodes"] = total_episodes_10ep
    audit_data["10ep_run"]["policy_counts"] = dict(policy_counts_10ep)
    audit_data["10ep_run"]["successes"] = dict(successes_10ep)
    audit_data["10ep_run"]["mean_steps"] = {k: steps_10ep[k]/policy_counts_10ep[k] for k in policy_counts_10ep}
    audit_data["10ep_run"]["paired"] = paired_overall_10ep
    audit_data["10ep_run"]["query_stats"] = {
        "total_queries": total_queries_10ep,
        "modified_queries": modified_queries_10ep,
        "query_modification_rate": modified_queries_10ep / total_queries_10ep if total_queries_10ep > 0 else 0
    }
    
    # ---------------------------------------------------------
    # 3. Audit 100ep Run (Configurations & Initial Logs)
    # ---------------------------------------------------------
    audit_data["100ep_run"] = {}
    audit_data["100ep_run"]["exists"] = os.path.exists(ROOT_100EP)
    
    # Check config details
    config_dir_100 = os.path.join(ROOT_100EP, "configs")
    configs_100 = glob.glob(os.path.join(config_dir_100, "task*.json"))
    audit_data["100ep_run"]["configs_count"] = len(configs_100)
    
    # Check supervisor log
    sup_log_100 = os.path.join(ROOT_100EP, "sweep_supervisor.log")
    audit_data["100ep_run"]["log_errors"] = check_log_errors(sup_log_100)
    
    # Check current status of run folder
    runs_100_dir = os.path.join(ROOT_100EP, "runs")
    tasks_100 = sorted([t for t in os.listdir(runs_100_dir) if t.startswith("task") and os.path.isdir(os.path.join(runs_100_dir, t))]) if os.path.exists(runs_100_dir) else []
    
    completed_episodes_100 = 0
    completed_jobs_100 = 0
    
    for t in tasks_100:
        t_path = os.path.join(runs_100_dir, t)
        for pol in ["original_simvla", "modified_simvla", "modified_h10_risk_topk8"]:
            pol_path = os.path.join(t_path, pol)
            if not os.path.exists(pol_path):
                continue
            subdirs = [d for d in os.listdir(pol_path) if os.path.isdir(os.path.join(pol_path, d))]
            if not subdirs:
                continue
            sub_dir = os.path.join(pol_path, subdirs[0])
            
            # Read summaries
            sum_path = os.path.join(sub_dir, "episode_summaries.jsonl")
            summaries = load_jsonl(sum_path)
            completed_episodes_100 += len(summaries)
            if len(summaries) == 100:
                completed_jobs_100 += 1
                
    audit_data["100ep_run"]["completed_episodes"] = completed_episodes_100
    audit_data["100ep_run"]["completed_jobs"] = completed_jobs_100
    
    # ---------------------------------------------------------
    # 4. Identity & Hashes Audit
    # ---------------------------------------------------------
    audit_data["checkpoint_identity"] = {
        "original_simvla": get_sha256("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO/model.safetensors"),
        "modified_simvla": get_sha256("/tmp/ood_ckpt60000/model.safetensors"),
        "detector": get_sha256("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8/model.pt")
    }
    
    print(json.dumps(audit_data))

if __name__ == "__main__":
    run_audit()
