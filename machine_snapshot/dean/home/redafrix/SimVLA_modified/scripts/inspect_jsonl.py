import json

def inspect_file(filepath, name):
    print(f"=== {name} ({filepath}) ===")
    with open(filepath, "r") as f:
        count = 0
        for line in f:
            data = json.loads(line)
            print(f"Keys: {list(data.keys())}")
            print(f"task_id: {data.get('task_id')}, episode: {data.get('episode')}, success: {data.get('success')}")
            # Check if seed or seed_id or task_suite exist
            for k in ['seed', 'seed_id', 'task_suite', 'task_description']:
                if k in data:
                    print(f"  {k}: {data[k]}")
            if "uncertainty_trace" in data and len(data["uncertainty_trace"]) > 0:
                print(f"  Trace len: {len(data['uncertainty_trace'])}")
                print(f"  Trace keys: {list(data['uncertainty_trace'][0].keys())}")
            print("-" * 40)
            count += 1
            if count >= 3:
                break

inspect_file("evaluation/libero/eval_libero_pro/eval_ckpt_110000_200eps/ckpt-110000/combined_libero_object_object_all_seeds.jsonl", "ckpt-110000")
inspect_file("evaluation/libero/eval_libero_pro/phase2_tdqc_ckpt_sweep_500eps_20260504_162406/ckpt-60000/combined_libero_object_object_all_seeds.jsonl", "ckpt-60000")
