import os
import json
import glob
import re
import hashlib
from collections import defaultdict

# Root Paths on Bob
ROOT_10EP = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_aggressive_fixed_20260609"
ROOT_100EP = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_threshold_q95_20260610"
TRAINING_SPLIT_PATH = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/episode_buckets.json"
DATASET_SUMMARIES_PATH = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/inputs/datasets/continuous_chunk10_flat/worker_0/episode_summaries.jsonl"
Q95_THRESH = 0.6155413389205933

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
                except Exception:
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

def run_comprehensive_audit():
    audit_data = {}
    
    # 1. Check training dataset & seed mappings
    dataset_mapping = {}
    if os.path.exists(DATASET_SUMMARIES_PATH):
        try:
            with open(DATASET_SUMMARIES_PATH, 'r') as f:
                for line in f:
                    if line.strip():
                        r = json.loads(line)
                        ep_uid = r.get("episode_uid", "")
                        task = r.get("task_id", None)
                        seed = r.get("episode_seed", r.get("eval_seed", None))
                        dataset_mapping[ep_uid] = {"task_id": str(task) if task is not None else None, "seed": seed}
        except Exception as e:
            audit_data["dataset_mapping_error"] = str(e)
            
    training_seeds = defaultdict(set)
    if os.path.exists(TRAINING_SPLIT_PATH):
        with open(TRAINING_SPLIT_PATH, 'r') as f:
            buckets = json.load(f)
        for bucket_name, ep_uids in buckets.items():
            if "train" in bucket_name or "val" in bucket_name or "calib" in bucket_name:
                for uid in ep_uids:
                    if uid in dataset_mapping:
                        t = dataset_mapping[uid]["task_id"]
                        s = dataset_mapping[uid]["seed"]
                        if t is not None and s is not None:
                            training_seeds[t].add(s)
                            
        audit_data["training_split_info"] = {k: len(v) for k, v in buckets.items()}
        audit_data["training_seeds_by_task"] = {t: len(s) for t, s in training_seeds.items()}
    else:
        audit_data["training_split_exists"] = False

    # 2. Audit Runs function
    def audit_run_root(root_dir, expected_seeds_range, target_thresh=None):
        run_data = {}
        run_data["exists"] = os.path.exists(root_dir)
        if not run_data["exists"]:
            return run_data
            
        configs_dir = os.path.join(root_dir, "configs")
        runs_dir = os.path.join(root_dir, "runs")
        
        config_files = glob.glob(os.path.join(configs_dir, "*.json"))
        run_data["configs_count"] = len(config_files)
        
        config_errors = []
        parsed_configs = {}
        for cf in sorted(config_files):
            try:
                with open(cf, "r") as f:
                    cfg = json.load(f)
                task_id = cfg.get("task_id")
                experiment_id = cfg.get("experiment_id", "")
                policy = experiment_id.replace(f"task{task_id}_", "") if experiment_id else "unknown"
                
                suite = cfg.get("suite")
                if suite != "libero_goal_object_ood":
                    config_errors.append(f"{os.path.basename(cf)}: Suite is {suite} instead of libero_goal_object_ood")
                    
                horizon = cfg.get("execution_horizon")
                if horizon != 10:
                    config_errors.append(f"{os.path.basename(cf)}: Execution horizon is {horizon} instead of 10")
                    
                if "risk" in policy and target_thresh is not None:
                    main_thresh = cfg.get("selection_main_threshold")
                    streak_thresh = cfg.get("selection_streak_threshold")
                    min_margin = cfg.get("selection_min_margin")
                    strong_margin = cfg.get("selection_strong_margin")
                    if abs(main_thresh - target_thresh) > 1e-6 or abs(streak_thresh - target_thresh) > 1e-6:
                        config_errors.append(f"{os.path.basename(cf)}: Risk thresholds are not {target_thresh} (main={main_thresh}, streak={streak_thresh})")
                    if min_margin != 0.02 or strong_margin != 0.05:
                        config_errors.append(f"{os.path.basename(cf)}: Risk margins are incorrect (min={min_margin}, strong={strong_margin})")
                        
                reset_seeds = cfg.get("reset_seeds", [])
                if not all(s in expected_seeds_range for s in reset_seeds):
                    config_errors.append(f"{os.path.basename(cf)}: Seeds not in range {expected_seeds_range}")
                    
                parsed_configs[(task_id, policy)] = cfg
            except Exception as e:
                config_errors.append(f"Failed to read {cf}: {str(e)}")
                
        run_data["config_errors"] = config_errors
        
        # Monitor runs
        tasks = sorted([t for t in os.listdir(runs_dir) if t.startswith("task") and os.path.isdir(os.path.join(runs_dir, t))]) if os.path.exists(runs_dir) else []
        run_data["tasks_found"] = len(tasks)
        
        task_data = {}
        seed_parity_errors = []
        leakage_errors = []
        horizon_errors = []
        zero_step_errors = []
        error_episodes = []
        
        total_queries = 0
        modified_queries = 0
        
        policies_to_check = ["modified_h10_risk_topk8"] if "threshold_q95" in root_dir else ["original_simvla", "modified_simvla", "modified_h10_risk_topk8"]
        
        for t in tasks:
            task_num = int(t.replace("task", ""))
            t_path = os.path.join(runs_dir, t)
            
            task_policies = {}
            for pol in policies_to_check:
                pol_path = os.path.join(t_path, pol)
                if not os.path.exists(pol_path):
                    continue
                subdirs = [d for d in os.listdir(pol_path) if os.path.isdir(os.path.join(pol_path, d))]
                if not subdirs:
                    continue
                sub_dir = os.path.join(pol_path, subdirs[0])
                
                episode_summaries = load_jsonl(os.path.join(sub_dir, "episode_summaries.jsonl"))
                episode_summaries = sorted(episode_summaries, key=lambda x: x.get("episode_index", 0))
                
                task_policies[pol] = episode_summaries
                
                for ep in episode_summaries:
                    ep_idx = ep.get("episode_index", 0)
                    steps = ep.get("num_steps", 0)
                    success = ep.get("success", False) or ep.get("outcome") == "success"
                    err_msg = ep.get("error_message")
                    
                    if steps == 0:
                        zero_step_errors.append(f"Task {task_num} {pol} Ep {ep_idx} has 0 steps")
                    if err_msg:
                        error_episodes.append(f"Task {task_num} {pol} Ep {ep_idx} has error: {err_msg}")
                        
                    if not success and not err_msg:
                        if steps != 300:
                            horizon_errors.append(f"Task {task_num} {pol} Ep {ep_idx} failed with non-300 steps: {steps}")
                            
                if pol == "modified_h10_risk_topk8":
                    scores_path = os.path.join(sub_dir, "step_scores_risk_topk8.jsonl")
                    if os.path.exists(scores_path):
                        steps_scores = load_jsonl(scores_path)
                        for step in steps_scores:
                            if "main_risk" in step or "main_score" in step or "query_index" in step:
                                total_queries += 1
                                if step.get("selected_candidate_index", 0) != 0:
                                    modified_queries += 1
                                    
            if "original_simvla" in task_policies:
                s_orig = [ep.get("reset_seed") for ep in task_policies["original_simvla"]]
                task_train_seeds = training_seeds[str(task_num)]
                leak_seeds = set(s_orig).intersection(task_train_seeds)
                if leak_seeds:
                    leakage_errors.append(f"Task {task_num} evaluation seeds leak with training split: {leak_seeds}")
                    
            task_data[task_num] = {}
            for pol, eps in task_policies.items():
                s_rate = sum(1 for ep in eps if ep.get("success", False) or ep.get("outcome") == "success") / len(eps) if eps else 0
                mean_s = sum(ep.get("num_steps", 0) for ep in eps) / len(eps) if eps else 0
                task_data[task_num][pol] = {
                    "completed": len(eps),
                    "success_rate": s_rate,
                    "mean_steps": mean_s
                }
                
        run_data["task_stats"] = task_data
        run_data["seed_parity_errors"] = seed_parity_errors
        run_data["leakage_errors"] = leakage_errors
        run_data["horizon_errors"] = horizon_errors
        run_data["zero_step_errors"] = zero_step_errors
        run_data["error_episodes"] = error_episodes
        run_data["query_stats"] = {
            "total_queries": total_queries,
            "modified_queries": modified_queries,
            "modification_rate": modified_queries / total_queries if total_queries > 0 else 0
        }
        
        sup_log = os.path.join(root_dir, "sweep_supervisor.log")
        run_data["log_issues"] = check_log_errors(sup_log)
        
        return run_data

    # 100ep run uses seeds [10, 110)
    audit_data["100ep_run"] = audit_run_root(ROOT_100EP, set(range(10, 110)), target_thresh=Q95_THRESH)
    
    # Model Identity Verification
    audit_data["checkpoint_identity"] = {
        "original_simvla": get_sha256("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO/model.safetensors"),
        "modified_simvla": get_sha256("/tmp/ood_ckpt60000/model.safetensors"),
        "detector": get_sha256("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8/model.pt")
    }
    
    return audit_data

if __name__ == "__main__":
    res = run_comprehensive_audit()
    print(json.dumps(res))
