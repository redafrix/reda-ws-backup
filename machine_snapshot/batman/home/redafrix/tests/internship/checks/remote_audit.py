import os
import json
import glob
import re
import hashlib
from collections import defaultdict

CAMPAIGNS = {
    "campaign1_risk_proof": "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608",
    "campaign2_aggressive_task3": "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_topk8_aggressive_task3_20260608",
    "campaign3_old_detector_task6": "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_task6_old_topk8_aggressive_20260608",
    "campaign4_ood_goal_swap": "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_ood_goal_object_and_swap_20260608"
}

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

def analyze_jsonl_summaries(path):
    rows = []
    if not os.path.exists(path):
        return None
    try:
        with open(path, 'r') as f:
            for line in f:
                if line.strip():
                    rows.append(json.loads(line))
    except Exception as e:
        return {"error": f"Failed to parse JSONL: {str(e)}"}

    if not rows:
        return {
            "total_rows": 0,
            "success_count": 0,
            "failure_count": 0,
            "error_count": 0,
            "mean_steps_all": 0.0,
            "mean_steps_success": 0.0,
            "mean_steps_failure": 0.0,
            "reset_seeds": [],
            "duplicate_seeds": [],
            "missing_seeds_check": False,
            "zero_step_episodes": 0,
            "error_episodes": []
        }

    success_count = 0
    failure_count = 0
    error_count = 0
    steps_all = []
    steps_success = []
    steps_failure = []
    seeds = []
    zero_step_count = 0
    error_episodes = []

    for r in rows:
        success = r.get("success", False)
        outcome = r.get("outcome", "")
        error_msg = r.get("error_message", "")
        steps = r.get("num_steps", 0)
        seed = r.get("reset_seed", None)
        ep_idx = r.get("episode_index", None)

        if steps == 0:
            zero_step_count += 1

        if error_msg or outcome == "error" or (success and error_msg):
            error_count += 1
            error_episodes.append({
                "episode_index": ep_idx,
                "reset_seed": seed,
                "error_message": error_msg,
                "success_flag": success
            })
        elif success:
            success_count += 1
            steps_success.append(steps)
        else:
            failure_count += 1
            steps_failure.append(steps)

        steps_all.append(steps)
        if seed is not None:
            seeds.append(seed)

    # Check duplicates
    seen = set()
    duplicates = []
    for s in seeds:
        if s in seen:
            duplicates.append(s)
        else:
            seen.add(s)

    return {
        "total_rows": len(rows),
        "success_count": success_count,
        "failure_count": failure_count,
        "error_count": error_count,
        "mean_steps_all": sum(steps_all) / len(steps_all) if steps_all else 0.0,
        "mean_steps_success": sum(steps_success) / len(steps_success) if steps_success else 0.0,
        "mean_steps_failure": sum(steps_failure) / len(steps_failure) if steps_failure else 0.0,
        "reset_seeds": seeds,
        "duplicate_seeds": list(set(duplicates)),
        "zero_step_episodes": zero_step_count,
        "error_episodes": error_episodes
    }

def audit_logs(campaign_root):
    logs_dir = os.path.join(campaign_root, "logs")
    log_issues = []
    if not os.path.exists(logs_dir):
        return log_issues

    patterns = [
        (re.compile(r"traceback", re.IGNORECASE), "Traceback found"),
        (re.compile(r"cuda out of memory", re.IGNORECASE), "CUDA OOM found"),
        (re.compile(r"keyboardinterrupt", re.IGNORECASE), "KeyboardInterrupt found"),
        (re.compile(r"exception", re.IGNORECASE), "Exception found")
    ]

    for root, dirs, files in os.walk(logs_dir):
        for file in files:
            if file.endswith(".log") or file.endswith(".err") or file.endswith(".txt"):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', errors='ignore') as f:
                        for line_idx, line in enumerate(f):
                            for regex, label in patterns:
                                if regex.search(line):
                                    log_issues.append({
                                        "file": os.path.relpath(path, campaign_root),
                                        "line_number": line_idx + 1,
                                        "label": label,
                                        "snippet": line.strip()[:150]
                                    })
                except Exception as e:
                    log_issues.append({
                        "file": os.path.relpath(path, campaign_root),
                        "label": f"Read error: {str(e)}"
                    })
    return log_issues

def check_process_status():
    # We can check running tmux/supervisor processes
    processes = []
    try:
        import subprocess
        out = subprocess.check_output("ps aux | grep -E 'run_policy_matrix|run_online_groups|tmux|supervisor'", shell=True).decode()
        for line in out.splitlines():
            if "grep" not in line:
                processes.append(line[:150])
    except Exception as e:
        processes.append(f"Error checking processes: {str(e)}")
    return processes

def run_audit():
    result = {}
    
    # 1. Gather all runs
    for camp_name, camp_path in CAMPAIGNS.items():
        result[camp_name] = {
            "root": camp_path,
            "exists": os.path.exists(camp_path),
            "runs": []
        }
        if not os.path.exists(camp_path):
            continue

        # Look for episode_summaries.jsonl
        jsonl_paths = []
        for root, dirs, files in os.walk(camp_path):
            for file in files:
                if file == "episode_summaries.jsonl":
                    jsonl_paths.append(os.path.join(root, file))

        for jp in jsonl_paths:
            run_dir = os.path.dirname(jp)
            rel_run_dir = os.path.relpath(run_dir, camp_path)
            
            # Determine run type: smoke vs production
            is_smoke = "smoke" in rel_run_dir or "online_smoke" in rel_run_dir
            
            # Look for run_manifest.json
            manifest_path = os.path.join(run_dir, "run_manifest.json")
            manifest_data = {}
            if os.path.exists(manifest_path):
                try:
                    with open(manifest_path, 'r') as f:
                        manifest_data = json.load(f)
                except Exception as e:
                    manifest_data = {"error": f"Failed to load manifest: {str(e)}"}
            
            # Read stats
            stats = analyze_jsonl_summaries(jp)
            
            # Extract config if referenced in manifest
            config_data = {}
            config_path = manifest_data.get("config", "")
            if config_path and os.path.exists(config_path):
                try:
                    with open(config_path, 'r') as f:
                        config_data = json.load(f)
                except Exception as e:
                    config_data = {"error": f"Failed to load config: {str(e)}"}
            elif config_path:
                # Try relative search or campaign config search
                filename = os.path.basename(config_path)
                search_path = os.path.join(camp_path, "configs", "online", filename)
                if os.path.exists(search_path):
                    try:
                        with open(search_path, 'r') as f:
                            config_data = json.load(f)
                    except Exception:
                        pass

            result[camp_name]["runs"].append({
                "rel_dir": rel_run_dir,
                "is_smoke": is_smoke,
                "manifest": manifest_data,
                "config": config_data,
                "stats": stats
            })

        # Check logs
        result[camp_name]["log_issues"] = audit_logs(camp_path)

    # 2. Check detector datasets and leakage
    # We look at Campaign 1's models/h10_continuous
    c1_path = CAMPAIGNS["campaign1_risk_proof"]
    detector_audit = {}
    if os.path.exists(c1_path):
        buckets_path = os.path.join(c1_path, "models", "h10_continuous", "all_tasks_random", "episode_buckets.json")
        counts_path = os.path.join(c1_path, "models", "h10_continuous", "all_tasks_random", "bucket_counts.json")
        dataset_summary_path = os.path.join(c1_path, "models", "h10_continuous", "available_dataset_summary.json")
        dataset_flat_summaries = os.path.join(c1_path, "inputs", "datasets", "continuous_chunk10_flat", "worker_0", "episode_summaries.jsonl")

        detector_audit["buckets_exist"] = os.path.exists(buckets_path)
        detector_audit["counts_exist"] = os.path.exists(counts_path)
        detector_audit["flat_summaries_exist"] = os.path.exists(dataset_flat_summaries)

        buckets = {}
        if os.path.exists(buckets_path):
            try:
                with open(buckets_path, 'r') as f:
                    buckets = json.load(f)
            except Exception as e:
                detector_audit["buckets_error"] = str(e)

        counts = {}
        if os.path.exists(counts_path):
            try:
                with open(counts_path, 'r') as f:
                    counts = json.load(f)
            except Exception as e:
                detector_audit["counts_error"] = str(e)

        # Let's map episode_uid to task_id and seed from the dataset flat_summaries
        dataset_mapping = {}
        if os.path.exists(dataset_flat_summaries):
            try:
                with open(dataset_flat_summaries, 'r') as f:
                    for line in f:
                        if line.strip():
                            r = json.loads(line)
                            ep_uid = r.get("episode_uid", "")
                            task = r.get("task_id", None)
                            seed = r.get("episode_seed", r.get("eval_seed", None))
                            dataset_mapping[ep_uid] = {"task_id": task, "seed": seed}
            except Exception as e:
                detector_audit["mapping_error"] = str(e)

        detector_audit["total_mapped_episodes"] = len(dataset_mapping)

        # Analyze task/seed distributions in each bucket
        bucket_analysis = {}
        for bucket_name, ep_uids in buckets.items():
            task_counts = defaultdict(int)
            seeds_used = defaultdict(list)
            missing_mapping_count = 0
            for uid in ep_uids:
                if uid in dataset_mapping:
                    t = dataset_mapping[uid]["task_id"]
                    s = dataset_mapping[uid]["seed"]
                    task_counts[t] += 1
                    if s is not None:
                        seeds_used[t].append(s)
                else:
                    missing_mapping_count += 1
            bucket_analysis[bucket_name] = {
                "total_episodes": len(ep_uids),
                "task_counts": dict(task_counts),
                "missing_mappings": missing_mapping_count,
                # Store sample seeds to check against test seeds
                "seeds_by_task": {t: list(set(s_list)) for t, s_list in seeds_used.items()}
            }
        detector_audit["buckets"] = bucket_analysis

    result["detector_audit"] = detector_audit
    result["processes"] = check_process_status()

    # Get SHAs of checkpoints to verify model identity
    c1_configs_online = glob.glob(os.path.join(c1_path, "configs/online/*.json"))
    c1_ckpts = set()
    for cp in c1_configs_online:
        try:
            with open(cp, 'r') as f:
                c1_ckpts.add(json.load(f).get("checkpoint", ""))
        except Exception:
            pass
    
    ckpt_shas = {}
    for cpath in c1_ckpts:
        if cpath:
            # Check model files inside or direct path
            # Original simvla could be directory or file
            # Let's check if it has pytorch_model.bin or model.pt
            shas = {}
            if os.path.isdir(cpath):
                for subfile in ["pytorch_model.bin", "model.pt", "model.safetensors", "config.json"]:
                    subpath = os.path.join(cpath, subfile)
                    if os.path.exists(subpath):
                        shas[subfile] = get_sha256(subpath)
            else:
                shas["file"] = get_sha256(cpath)
            ckpt_shas[cpath] = shas
    result["checkpoint_shas"] = ckpt_shas

    return result

if __name__ == "__main__":
    import sys
    res = run_audit()
    print(json.dumps(res, indent=2))
