#!/usr/bin/env python3
import json

def main():
    summaries_path = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/outputs/openvla_goal_object_pro_risk_data_10000ep_round_robin_20260616_discarded/episode_summaries.jsonl"
    queries_path = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/outputs/openvla_goal_object_pro_risk_data_10000ep_round_robin_20260616_discarded/query_records.jsonl"
    steps_path = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/outputs/openvla_goal_object_pro_risk_data_10000ep_round_robin_20260616_discarded/step_records.jsonl"

    print("Loading summaries...")
    episodes = []
    with open(summaries_path) as f:
        for line in f:
            episodes.append(json.loads(line))

    print("Loading queries...")
    queries_by_ep = {}
    with open(queries_path) as f:
        for line in f:
            q = json.loads(line)
            key = (q["task_id"], q["reset_seed"])
            if key not in queries_by_ep:
                queries_by_ep[key] = []
            queries_by_ep[key].append(q)

    print("Verifying steps sequential alignment...")
    steps_file = open(steps_path)
    for i, ep in enumerate(episodes):
        is_timeout = (ep["num_steps"] == 800)
        expected_steps = 800 if is_timeout else ep["num_steps"] + 1
        expected_queries = 100 if is_timeout else (ep["num_steps"] // 8) + 1
        
        ep_steps = []
        for _ in range(expected_steps):
            line = steps_file.readline()
            if not line:
                print(f"Error: early EOF at episode {i}")
                return
            ep_steps.append(json.loads(line))
            
        key = (ep["task_id"], ep["reset_seed"])
        q_list = queries_by_ep.get(key, [])
        if len(q_list) != expected_queries:
            print(f"Mismatch at ep {i} (seed={ep['reset_seed']}): expected {expected_queries} queries, got {len(q_list)}")
            return
            
    steps_file.close()
    print("Verification complete: perfect alignment!")

if __name__ == "__main__":
    main()
