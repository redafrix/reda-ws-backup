import torch

def check_balance(path):
    d = torch.load(path, map_location="cpu")
    eps = d["episodes"]
    steps = [10, 50, 100, 150, 200, 300]
    print(f"{'Step':<5} | {'Success':<8} | {'Failure':<8} | {'Failure %':<10}")
    print("-" * 40)
    for s in steps:
        sc = sum(1 for e in eps if e["success"] and len(e["features"]) >= s)
        fc = sum(1 for e in eps if not e["success"] and len(e["features"]) >= s)
        total = sc + fc
        ratio = fc / total if total > 0 else 0
        print(f"{s:<5} | {sc:<8} | {fc:<8} | {ratio:>10.1%}")

if __name__ == "__main__":
    print("ID TEST SET:")
    check_balance("/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/v10_exp01/data/v10_test.pt")
    print("\nOOD TEST SET:")
    check_balance("/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/v10_exp01/data/v10_unseen_obj_ood.pt")
