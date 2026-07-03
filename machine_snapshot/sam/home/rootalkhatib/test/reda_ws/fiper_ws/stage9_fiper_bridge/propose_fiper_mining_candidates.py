import argparse
import json
from pathlib import Path
from .stage9_io import read_jsonl, write_jsonl

def main():
    parser = argparse.ArgumentParser(description="Rank and propose states for active failure-risk mining.")
    parser.add_argument("--ace-jsonl", required=True, help="Path to ace_group_summaries.jsonl")
    parser.add_argument("--rnd-jsonl", help="Optional path to RND observation scores by state_id (JSONL)")
    parser.add_argument("--out-jsonl", required=True, help="Output path for proposed candidate states")
    args = parser.parse_args()
    
    print(f"Reading ACE summaries from {args.ace_jsonl}...")
    ace_groups = read_jsonl(args.ace_jsonl)
    print(f"Loaded {len(ace_groups)} ACE state summaries.")
    
    # Merge RND scores if available
    rnd_by_state = {}
    if args.rnd_jsonl:
        print(f"Reading RND scores from {args.rnd_jsonl}...")
        rnd_rows = read_jsonl(args.rnd_jsonl)
        for r in rnd_rows:
            sid = r.get("state_id") or r.get("sample_id")
            if "_seed" in sid:
                sid = sid.split("_seed")[0]
            # Average scores if multiple samples per state, or take max
            score = r.get("rnd_score") or r.get("rnd_oe_score") or r.get("loss")
            if sid and score is not None:
                rnd_by_state[sid] = float(score)
        print(f"Merged RND scores for {len(rnd_by_state)} states.")
        
    proposed_candidates = []
    
    for g in ace_groups:
        sid = g["state_id"]
        ace = g["ace_score"]
        
        rnd_score = rnd_by_state.get(sid, 0.0)
        has_rnd = sid in rnd_by_state
        
        # Extract risk parameters
        risk_range = g.get("risk_score_range", 0.0)
        group_type = g.get("group_type", "unknown")
        
        # Compute combined mining priority score
        # Priority should be higher for:
        # - High ACE (high action uncertainty)
        # - High RND (OOD observation)
        # - High risk range/spread (bifurcation state)
        # - group_type is NOT all_safe (since all_safe means no failures observed yet)
        
        # Simple heuristic priority:
        # standardizing ACE: let's assume raw ACE ranges between 0 and 20+ (differential entropy)
        # For a simple ranking, we can use:
        # Priority = ACE + (RND * 5.0 if has_rnd else 0.0) + (risk_range * 10.0)
        # If group_type is all_safe_or_weak_safe, we multiply by 0.5 to prioritize active failures,
        # but keep it in the loop for benign OOD detection.
        priority = ace + (rnd_score * 10.0 if has_rnd else 0.0) + (risk_range * 5.0)
        if group_type == "all_safe_or_weak_safe":
            priority *= 0.5
            
        candidate = {
            "state_id": sid,
            "priority_score": float(priority),
            "ace_score": ace,
            "rnd_score": rnd_score if has_rnd else None,
            "risk_score_range": risk_range,
            "group_type": group_type,
            "action_std_mean": g.get("action_std_mean", 0.0),
            "translation_std": g.get("translation_std", 0.0),
            "rotation_std": g.get("rotation_std", 0.0),
            "num_candidates": g.get("num_candidates", 0)
        }
        proposed_candidates.append(candidate)
        
    # Rank by priority descending
    proposed_candidates.sort(key=lambda x: x["priority_score"], reverse=True)
    
    # Save the output
    write_jsonl(args.out_jsonl, proposed_candidates)
    print(f"Proposed {len(proposed_candidates)} candidates saved to {args.out_jsonl}")
    
    # Print top 5 candidates
    print("\nTop 5 proposed failure-risk mining candidates:")
    for idx, c in enumerate(proposed_candidates[:5]):
        print(f"  {idx+1}. State: {c['state_id']}")
        print(f"     Priority Score: {c['priority_score']:.4f} | ACE: {c['ace_score']:.4f} | Risk Range: {c['risk_score_range']:.2f} | Type: {c['group_type']}")

if __name__ == "__main__":
    main()
