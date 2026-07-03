import json
from pathlib import Path

def main():
    refs_dir = Path("/home/dean/fiper_uncertainty_collection/experiments/prepared_20260527/08_target_object_pick_basket_loto_v1/fold_00_holdout_alphabet_soup_bbq_sauce/datasets/refs")
    base_dir = Path("/home/dean/fiper_uncertainty_collection")
    
    splits = [
        "success_train_seen",
        "success_calib_seen",
        "success_test_seen",
        "success_test_ood",
        "failure_test_seen",
        "failure_eval_ood"
    ]
    
    # Load all line requirements
    requirements = {} # path -> set of 0-indexed lines
    for split in splits:
        ref_path = refs_dir / f"{split}.rows.jsonl"
        print(f"Loading {ref_path.name}...")
        with ref_path.open() as f:
            for line in f:
                if not line.strip():
                    continue
                row = json.loads(line)
                src = row["source_jsonl"]
                line_idx = int(row["line_no"]) - 1 # line_no is 1-based
                requirements.setdefault(src, set()).add(line_idx)
                
    # Now read the paths from the source files
    state_paths = set()
    total_rows = 0
    for src, lines in requirements.items():
        src_path = base_dir / src
        print(f"Scanning {src_path} for {len(lines)} lines...")
        with src_path.open() as f:
            for idx, line in enumerate(f):
                if idx in lines:
                    row = json.loads(line)
                    sim_state_path = row["current"]["sim_state_path"]
                    state_paths.add(sim_state_path)
                    total_rows += 1
                    
    print(f"Total rows matched: {total_rows}")
    print(f"Unique sim_state_paths: {len(state_paths)}")
    
if __name__ == "__main__":
    main()
