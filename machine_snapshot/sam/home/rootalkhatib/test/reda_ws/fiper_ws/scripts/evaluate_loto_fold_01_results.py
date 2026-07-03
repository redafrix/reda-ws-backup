#!/usr/bin/env python3
import json
import sys
from pathlib import Path
from collections import defaultdict
import numpy as np

def first_alarm_index(boolean_list, K):
    n = len(boolean_list)
    for i in range(n - K + 1):
        if all(boolean_list[i + j] for j in range(K)):
            return i
    return -1

def get_alarm_steps(boolean_list, K):
    n = len(boolean_list)
    alarm_steps = [False] * n
    for t in range(n):
        if t >= K - 1:
            if all(boolean_list[t - j] for j in range(K)):
                alarm_steps[t] = True
    return alarm_steps

def main():
    base_dir = Path("experiments/fiper_target_object_pick_basket_fold_01_full_20260526")
    rnd_scores_path = base_dir / "scores" / "rnd_scores_by_split.jsonl"
    ace_scores_path = base_dir / "scores" / "ace_scores_by_split.jsonl"
    rnd_thresh_path = base_dir / "thresholds" / "rnd_thresholds.json"
    ace_thresh_path = base_dir / "thresholds" / "ace_thresholds.json"

    # 1. Load thresholds
    with rnd_thresh_path.open() as f:
        rnd_thresholds = json.load(f)
    with ace_thresh_path.open() as f:
        ace_thresholds = json.load(f)

    # 2. Load scores
    print("Loading score files...")
    rnd_file = rnd_scores_path.open()
    ace_file = ace_scores_path.open()

    merged_data = defaultdict(lambda: defaultdict(list))
    
    line_idx = 0
    while True:
        rnd_line = rnd_file.readline()
        ace_line = ace_file.readline()

        if not rnd_line and not ace_line:
            break
        if not rnd_line or not ace_line:
            raise AssertionError("File length mismatch!")

        rnd_val = json.loads(rnd_line)
        ace_val = json.loads(ace_line)

        assert rnd_val["split"] == ace_val["split"]
        assert rnd_val["ek"] == ace_val["ek"]
        assert rnd_val["timestep"] == ace_val["timestep"]

        split = rnd_val["split"]
        ek = rnd_val["ek"]
        t = rnd_val["timestep"]
        rnd_score = rnd_val["rnd_score"]
        ace_entropy = ace_val["ace_entropy"]

        merged_data[split][ek].append({
            "timestep": t,
            "rnd_score": rnd_score,
            "ace_entropy": ace_entropy
        })
        line_idx += 1

    rnd_file.close()
    ace_file.close()
    print(f"Loaded {line_idx} rows successfully.")

    # Sort each episode by timestep
    for split in merged_data:
        for ek in merged_data[split]:
            merged_data[split][ek].sort(key=lambda x: x["timestep"])

    r_th = rnd_thresholds["q95"]
    a_th = ace_thresholds["q95"]

    # 3. Compute Row-Level Metrics (q95)
    print("\n--- Row-Level Metrics (q95) ---")
    for split in merged_data:
        total_rows = 0
        rnd_alarms = 0
        ace_alarms = 0
        or_alarms = 0
        and_alarms = 0

        for ek in merged_data[split]:
            for step in merged_data[split][ek]:
                total_rows += 1
                r_val = step["rnd_score"]
                a_val = step["ace_entropy"]

                r_alarm = r_val > r_th
                a_alarm = a_val > a_th

                if r_alarm:
                    rnd_alarms += 1
                if a_alarm:
                    ace_alarms += 1
                if r_alarm or a_alarm:
                    or_alarms += 1
                if r_alarm and a_alarm:
                    and_alarms += 1

        print(f"Split: {split}")
        print(f"  RND q95 alarm rate: {rnd_alarms / total_rows:.4f}")
        print(f"  ACE q95 alarm rate: {ace_alarms / total_rows:.4f}")
        print(f"  OR q95 alarm rate:  {or_alarms / total_rows:.4f}")
        print(f"  AND q95 alarm rate: {and_alarms / total_rows:.4f}")

    # 4. Episode-Level Metrics for Successful Splits (success_test_seen, success_test_ood)
    print("\n--- Episode-Level Metrics (Success Splits) ---")
    success_splits = ["success_test_seen", "success_test_ood"]
    
    # Episode false alarm rate for OR q90/q95/q99 (K=1)
    for split in success_splits:
        print(f"\nSplit: {split}")
        episodes = merged_data[split]
        n_eps = len(episodes)
        if n_eps == 0:
            continue
        
        for q in ["q90", "q95", "q99"]:
            r_val_th = rnd_thresholds[q]
            a_val_th = ace_thresholds[q]
            fa_eps = 0
            for ek in episodes:
                has_fa = False
                for step in episodes[ek]:
                    if step["rnd_score"] > r_val_th or step["ace_entropy"] > a_val_th:
                        has_fa = True
                        break
                if has_fa:
                    fa_eps += 1
            print(f"  OR {q} Episode False Alarm Rate (K=1): {fa_eps / n_eps:.4f} ({fa_eps}/{n_eps})")

        # RND-only, ACE-only, OR q95 for K=1,2,3,5
        for k in [1, 2, 3, 5]:
            print(f"  K={k}:")
            for name, r_flag, a_flag in [("RND-only", True, False), ("ACE-only", False, True), ("OR", True, True)]:
                fa_eps = 0
                alarm_steps_counts = []
                for ek in episodes:
                    boolean_list = []
                    for step in episodes[ek]:
                        cond = False
                        if r_flag and step["rnd_score"] > r_th:
                            cond = True
                        if a_flag and step["ace_entropy"] > a_th:
                            cond = True
                        boolean_list.append(cond)
                    
                    alarm_steps = get_alarm_steps(boolean_list, k)
                    if any(alarm_steps):
                        fa_eps += 1
                    alarm_steps_counts.append(sum(alarm_steps))
                
                mean_steps = np.mean(alarm_steps_counts)
                median_steps = np.median(alarm_steps_counts)
                print(f"    {name} Episode False Alarm Rate: {fa_eps / n_eps:.4f} ({fa_eps}/{n_eps})")
                print(f"      Mean alarm steps per ep: {mean_steps:.2f}")
                print(f"      Median alarm steps per ep: {median_steps:.2f}")

    # 5. Episode-Level Metrics for Failure Splits (failure_eval_seen, failure_eval_ood)
    print("\n--- Episode-Level Metrics (Failure Splits) ---")
    failure_splits = ["failure_eval_seen", "failure_eval_ood"]

    for split in failure_splits:
        print(f"\nSplit: {split}")
        episodes = merged_data[split]
        n_eps = len(episodes)
        if n_eps == 0:
            continue
            
        for k in [1, 2, 3, 5]:
            print(f"  K={k}:")
            for name, r_flag, a_flag in [("RND-only", True, False), ("ACE-only", False, True), ("OR", True, True)]:
                detected_count = 0
                first_detection_times_detected_only = []
                first_detection_times_all = []
                det_10_count = 0
                det_25_count = 0
                det_50_count = 0
                
                for ek in episodes:
                    boolean_list = []
                    for step in episodes[ek]:
                        cond = False
                        if r_flag and step["rnd_score"] > r_th:
                            cond = True
                        if a_flag and step["ace_entropy"] > a_th:
                            cond = True
                        boolean_list.append(cond)
                        
                    alarm_steps = get_alarm_steps(boolean_list, k)
                    
                    # Check if detected
                    idx = -1
                    for i, active in enumerate(alarm_steps):
                        if active:
                            idx = i
                            break
                    
                    if idx != -1:
                        detected_count += 1
                        norm_time = idx / len(alarm_steps)
                        first_detection_times_detected_only.append(norm_time)
                        first_detection_times_all.append(norm_time)
                        
                        if norm_time <= 0.10:
                            det_10_count += 1
                        if norm_time <= 0.25:
                            det_25_count += 1
                        if norm_time <= 0.50:
                            det_50_count += 1
                    else:
                        first_detection_times_all.append(1.0)
                
                det_rate = detected_count / n_eps
                never_det_rate = 1.0 - det_rate
                
                mean_time_det_only = np.mean(first_detection_times_detected_only) if first_detection_times_detected_only else float('nan')
                median_time_det_only = np.median(first_detection_times_detected_only) if first_detection_times_detected_only else float('nan')
                
                mean_time_all = np.mean(first_detection_times_all)
                median_time_all = np.median(first_detection_times_all)
                
                print(f"    {name}:")
                print(f"      Detection Rate:                     {det_rate:.4f} ({detected_count}/{n_eps})")
                print(f"      Never Detected Rate:                {never_det_rate:.4f}")
                print(f"      Det@10%:                            {det_10_count / n_eps:.4f} ({det_10_count}/{n_eps})")
                print(f"      Det@25%:                            {det_25_count / n_eps:.4f} ({det_25_count}/{n_eps})")
                print(f"      Det@50%:                            {det_50_count / n_eps:.4f} ({det_50_count}/{n_eps})")
                print(f"      Mean Norm First Det Time (det only): {mean_time_det_only:.4f}")
                print(f"      Median Norm First Det Time (det only):{median_time_det_only:.4f}")
                print(f"      Mean Norm First Det Time (all=1.0):  {mean_time_all:.4f}")
                print(f"      Median Norm First Det Time (all=1.0): {median_time_all:.4f}")

    # 6. RND vs ACE complementarity on failure_eval_ood (q95, K=1, 2, 3, 5)
    print("\n--- RND vs ACE Complementarity (failure_eval_ood) ---")
    ood_episodes = merged_data["failure_eval_ood"]
    n_ood = len(ood_episodes)
    
    for k in [1, 2, 3, 5]:
        both_det = 0
        only_rnd = 0
        only_ace = 0
        missed = 0
        
        for ek in ood_episodes:
            rnd_bool = [step["rnd_score"] > r_th for step in ood_episodes[ek]]
            ace_bool = [step["ace_entropy"] > a_th for step in ood_episodes[ek]]
            
            rnd_steps = get_alarm_steps(rnd_bool, k)
            ace_steps = get_alarm_steps(ace_bool, k)
            
            rnd_detected = any(rnd_steps)
            ace_detected = any(ace_steps)
            
            if rnd_detected and ace_detected:
                both_det += 1
            elif rnd_detected and not ace_detected:
                only_rnd += 1
            elif not rnd_detected and ace_detected:
                only_ace += 1
            else:
                missed += 1
                
        print(f"  Debounce K={k}:")
        print(f"    Both detect:      {both_det / n_ood:.4f} ({both_det}/{n_ood})")
        print(f"    Only RND detects: {only_rnd / n_ood:.4f} ({only_rnd}/{n_ood})")
        print(f"    Only ACE detects: {only_ace / n_ood:.4f} ({only_ace}/{n_ood})")
        print(f"    Missed by both:   {missed / n_ood:.4f} ({missed}/{n_ood})")

if __name__ == "__main__":
    main()
