import json
from pathlib import Path
import glob

def check_structure():
    files = glob.glob("/home/rootalkhatib/test/reda_ws/fiper_ws/data/frozen/fiper_sweep_eternal_20260526_combined/*/fiper_receding_samples.jsonl")
    print("Found files:", files)
    
    suite_tasks = {}
    row_count = 0
    
    for f_path in files:
        print(f"Reading first few lines of {f_path}...")
        with open(f_path, "r") as f:
            for i in range(10):
                line = f.readline()
                if not line:
                    break
                row = json.loads(line)
                suite = row.get("suite")
                task_id = row.get("task_id")
                instruction = row.get("task_instruction")
                print(f"Suite: {suite}, Task ID: {task_id}, Instruction: {instruction}")
                
if __name__ == "__main__":
    check_structure()
