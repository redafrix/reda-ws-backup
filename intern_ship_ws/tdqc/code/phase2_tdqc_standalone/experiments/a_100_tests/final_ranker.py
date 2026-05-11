import os
import json
import pandas as pd
from pathlib import Path

def main():
    base_dir = Path("/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/a_100_tests")
    results = []

    for i in range(1, 101):
        idea_id = f"{i:03d}"
        results_path = base_dir / f"idea_{idea_id}" / "runs" / "granular_results.json"
        
        if results_path.exists():
            with open(results_path, "r") as f:
                data = json.load(f)
            
            # Extract key metrics for ranking
            # We'll rank primarily by OOD Overall Brier (lower is better)
            # and Test Overall AUC (higher is better)
            
            res = {
                "Idea": idea_id,
                "Test_Brier_Overall": data["test"]["Overall"]["Brier"],
                "OOD_Brier_Overall": data["ood"]["Overall"]["Brier"],
                "Test_AUC_Overall": data["test"]["Overall"]["AUC"],
                "OOD_AUC_Overall": data["ood"]["Overall"]["AUC"],
                "Test_Brier_Step50": data["test"]["50"]["Brier"],
                "OOD_Brier_Step50": data["ood"]["50"]["Brier"],
            }
            results.append(res)
        else:
            results.append({
                "Idea": idea_id,
                "Test_Brier_Overall": 999.0,
                "OOD_Brier_Overall": 999.0,
                "Test_AUC_Overall": 0.0,
                "OOD_AUC_Overall": 0.0,
                "Status": "Failed/Missing"
            })

    df = pd.DataFrame(results)
    
    # Ranking score: Composite of Brier and AUC
    # Lower Brier is better, Higher AUC is better.
    # We want models that generalize to OOD.
    df["Rank_Score"] = df["OOD_Brier_Overall"] + (1.0 - df["OOD_AUC_Overall"])
    df = df.sort_values("Rank_Score")

    print("\n" + "="*80)
    print("FINAL 100-EXPERIMENT RANKING (Top 20)")
    print("="*80)
    print(df.head(20).to_string(index=False))
    
    df.to_csv(base_dir / "final_ranking_summary.csv", index=False)
    print(f"\nFull report saved to {base_dir / 'final_ranking_summary.csv'}")

if __name__ == "__main__":
    main()
