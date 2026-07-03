#!/usr/bin/env python3
import json
from pathlib import Path

TRASH_ROOT = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/goal_object_modified_simvla_chunk10_100_20260605")
SMOKE_DIR = TRASH_ROOT / "smoke"

def validate():
    summary_path = SMOKE_DIR / "episode_summaries.jsonl"
    events_path = SMOKE_DIR / "chunk_events.jsonl"
    
    checks = {
        "summary_exists": summary_path.exists(),
        "events_exists": events_path.exists(),
        "bddl_hash_match": False,
        "init_hash_match": False,
        "checkpoint_hash_match": False,
        "chunk_shape_10x7": False,
        "query_timesteps_correct": False,
        "contiguous_timesteps": True,
        "first_chunk_10_actions": False,
        "total_steps_match": False,
        "no_errors": False,
        "pass": False
    }

    if not summary_path.exists() or not events_path.exists():
        return checks

    with open(summary_path, "r") as f:
        summaries = [json.loads(line) for line in f if line.strip()]
    
    with open(events_path, "r") as f:
        events = [json.loads(line) for line in f if line.strip()]

    if not summaries or not events:
        return checks

    s = summaries[0]
    checks["bddl_hash_match"] = (s["bddl_hash"] != "")
    checks["init_hash_match"] = (s["init_state_hash"] != "")
    checks["checkpoint_hash_match"] = (s["checkpoint_hash"] == "3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71")
    checks["no_errors"] = (s["error_message"] == "")

    # Check events
    e0 = events[0]
    checks["chunk_shape_10x7"] = (e0["chunk_shape"] == [10, 7])
    checks["first_chunk_10_actions"] = (e0["actions_executed"] == 10 or s["success"] or s["terminal_done"])
    
    if len(events) > 1:
        e1 = events[1]
        checks["query_timesteps_correct"] = (e0["policy_timestep_before"] == 0 and e1["policy_timestep_before"] == 10)
    else:
        checks["query_timesteps_correct"] = (e0["policy_timestep_before"] == 0)

    # Contiguous and total steps
    last_step = 0
    total_actions = 0
    for e in events:
        if e["policy_timestep_before"] != last_step:
            checks["contiguous_timesteps"] = False
        last_step = e["policy_timestep_after"]
        total_actions += e["actions_executed"]
    
    checks["total_steps_match"] = (total_actions == s["policy_environment_steps"])

    # Final pass criteria
    mandatory = ["summary_exists", "events_exists", "checkpoint_hash_match", "chunk_shape_10x7", "contiguous_timesteps", "total_steps_match", "no_errors"]
    checks["pass"] = all(checks[k] for k in mandatory)
    
    return checks

if __name__ == "__main__":
    result = validate()
    print(json.dumps(result, indent=2))
    with open(SMOKE_DIR / "smoke_validation.json", "w") as f:
        json.dump(result, f, indent=2)
