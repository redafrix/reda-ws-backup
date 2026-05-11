import json
import numpy as np
import os
from glob import glob
import pandas as pd
from pathlib import Path

def build_database_table(data_dir):
    files = glob(os.path.join(data_dir, "*.json"))
    data = []
    
    # Unique substrings to identify LIBERO Spatial tasks (truncated to ~50 chars)
    identifiers = [
        "between_the_plate", # 0
        "next_to_the_plate", # 1
        "from_table_center", # 2
        "on_the_cookie_box", # 3
        "top_drawer",        # 4
        "on_the_ramekin",    # 5
        "next_to_the_cookie_box", # 6
        "on_the_stove",      # 7
        "next_to_the_ramekin", # 8
        "on_the_wooden_cabinet" # 9
    ]

    for f in sorted(files):
        filename = os.path.basename(f)
        
        task_id = -1
        for i, ident in enumerate(identifiers):
            if ident in filename:
                task_id = i
                break

        if task_id == -1:
            continue

        parts = filename.split('_')
        try:
            ep_part = [p for p in parts if p.startswith('ep')][0]
            trial_idx = int(ep_part.replace('ep', ''))
            result = "SUCCESS" if "success" in filename else "FAILURE"
        except:
            trial_idx = -1
            result = "unknown"

        with open(f, 'r') as j:
            traj_data = json.load(j)
            all_vars = [np.mean(step['path_variance']) for step in traj_data]
            
            data.append({
                "Task ID": task_id,
                "Trial": trial_idx,
                "Result": result,
                "Steps": len(all_vars),
                "Mean Uncertainty": np.mean(all_vars),
                "Max Uncertainty": np.max(all_vars)
            })
            
    df = pd.DataFrame(data).sort_values(["Task ID", "Trial"])
    print(df.to_markdown(index=False))

ROOT = Path(__file__).parents[1]
data_dir = ROOT / "outputs/eval/task5_database_20trials/"
build_database_table(data_dir)
