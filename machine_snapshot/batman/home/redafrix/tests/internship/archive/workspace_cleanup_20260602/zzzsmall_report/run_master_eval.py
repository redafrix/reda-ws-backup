import sys
import os
import torch
import numpy as np
from pathlib import Path
from torch.utils.data import DataLoader, Dataset
from sklearn.metrics import roc_auc_score

SUITE_TO_ID = { 
    "libero_10_lan": 0,
    "libero_10_object": 1,                                                                                                                                                                                
    "libero_10_swap": 2,  
    "libero_goal_lan": 3,
    "libero_goal_object": 3,
    "libero_goal_swap": 4,
    "libero_object_lan": 5,
    "libero_object_object": 6,                                                                                                                                                                            
    "libero_object_swap": 7,  
    "libero_spatial_lan": 8,                                                                                                                                                                              
    "libero_spatial_object": 9,                                                                                                                                                                           
    "libero_spatial_swap": 10, 
}

class StandardEvalDataset(Dataset):
    def __init__(self, path):
        self.path = Path(path)
        obj = torch.load(self.path, map_location="cpu")
        raw_episodes = obj["episodes"] if isinstance(obj, dict) else obj
        self.episodes = []
        for ep in raw_episodes:
            features = ep["features"]
            if not isinstance(features, torch.Tensor):
                features = torch.tensor(features, dtype=torch.float32)
            else:
                features = features.float()
            
            success = int(ep["success"])
            self.episodes.append({
                "features": features,
                "success": success,
                "suite_id": SUITE_TO_ID.get(ep.get("task_suite", ""), -1),
                "episode_idx": int(ep.get("episode_idx", -1)),
                "instruction": str(ep.get("instruction", "")),
            })
        self.input_dim = int(self.episodes[0]["features"].shape[-1])

    def __len__(self):
        return len(self.episodes)

    def __getitem__(self, idx):
        return self.episodes[idx]

def standard_collate(batch):
    B = len(batch)
    T_max = max(ep["features"].shape[0] for ep in batch)
    F = batch[0]["features"].shape[-1]

    features = torch.zeros(B, T_max, F, dtype=torch.float32)
    mask = torch.zeros(B, T_max, dtype=torch.float32)
    lengths = torch.zeros(B, dtype=torch.long)
    success = torch.zeros(B, dtype=torch.float32)
    suite_id = torch.zeros(B, dtype=torch.long)
    episode_idx = torch.zeros(B, dtype=torch.long)

    for b, ep in enumerate(batch):
        T = ep["features"].shape[0]
        features[b, :T] = ep["features"]
        mask[b, :T] = 1.0
        lengths[b] = T
        success[b] = float(ep["success"])
        suite_id[b] = int(ep["suite_id"])
        episode_idx[b] = int(ep["episode_idx"])

    failure = 1.0 - success

    return {
        "features": features,
        "mask": mask,
        "lengths": lengths,
        "success": success,
        "failure": failure,
        "suite_id": suite_id,
        "episode_idx": episode_idx,
    }

def calculate_metrics(probs, targets):
    if len(probs) == 0:
        return "N/A", "N/A", "N/A", "N/A", "N/A"
    
    preds = (probs > 0.5).astype(int)
    acc = np.mean(preds == targets)
    brier = np.mean(np.square(probs - targets))
    
    try:
        auc = roc_auc_score(targets, probs)
        auc_str = f"{auc:.4f}"
    except ValueError:
        auc_str = "N/A"
        
    # Recall and FPR
    tp = np.sum((preds == 1) & (targets == 1))
    fn = np.sum((preds == 0) & (targets == 1))
    fp = np.sum((preds == 1) & (targets == 0))
    tn = np.sum((preds == 0) & (targets == 0))
    
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    fpr = fp / (fp + tn) if (fp + tn) > 0 else 0.0
    
    return f"{acc:.2%}", f"{brier:.4f}", auc_str, f"{recall:.2%}", f"{fpr:.2%}"

def run_evaluation(model_name, model_dir, ckpt_path, dataset_path, is_lstm, use_suite_id, is_49d):
    print(f"\nEvaluating: {model_name} on {Path(dataset_path).name}")
    
    # 1. Dyn import cleanup
    for k in list(sys.modules.keys()):
        if k.startswith('phase2_tdqc'):
            del sys.modules[k]
            
    # Add model_dir to sys.path
    if str(model_dir) not in sys.path:
        sys.path.insert(0, str(model_dir))
        
    from phase2_tdqc.tdqc_features import normalize_features
    if is_lstm:
        from phase2_tdqc.tdqc_model import TDQCLSTMCalibrator as ModelClass
    else:
        from phase2_tdqc.tdqc_model import TDQCTransformerCalibrator as ModelClass
        
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    # Load dataset
    dataset = StandardEvalDataset(dataset_path)
    loader = DataLoader(dataset, batch_size=64, shuffle=False, collate_fn=standard_collate)
    
    # Load checkpoint
    ckpt = torch.load(ckpt_path, map_location=device)
    cfg = ckpt["config"]
    
    # Instantiate model
    if is_lstm:
        hidden_dim = cfg.get("hidden_dim", 128)
        num_layers = cfg.get("num_layers", 1)
        dropout = cfg.get("dropout", 0.0)
        model = ModelClass(input_dim=dataset.input_dim, hidden_dim=hidden_dim, num_layers=num_layers, dropout=dropout).to(device)
    else:
        hidden_dim = cfg.get("hidden_dim", 128)
        num_layers = cfg.get("num_layers", 1)
        try:
            model = ModelClass(input_dim=dataset.input_dim, hidden_dim=hidden_dim, num_layers=num_layers, dropout=cfg.get("dropout", 0.05)).to(device)
        except TypeError:
            model = ModelClass(input_dim=dataset.input_dim, hidden_dim=hidden_dim, num_layers=num_layers).to(device)
            
    model.load_state_dict(ckpt["model"])
    model.eval()
    
    mean = ckpt["mean"].to(device)
    std = ckpt["std"].to(device)
    
    steps_to_check = [10, 12, 15, 50, 100, 150, 200, 300]
    step_data = {s: {"probs": [], "targets": []} for s in steps_to_check}
    overall_data = {"probs": [], "targets": []}
    
    with torch.no_grad():
        for batch in loader:
            batch = {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
            x = normalize_features(batch["features"], mean, std)
            
            if is_lstm:
                if use_suite_id:
                    q = model(x, batch["lengths"], suite_ids=batch["suite_id"])
                else:
                    try:
                        q = model(x, batch["lengths"], suite_ids=None)
                    except TypeError:
                        q = model(x, batch["lengths"])
            else:
                q = model(x, mask=batch["mask"])
                
            targets = batch["failure"].cpu().numpy()
            q_np = q.cpu().numpy()
            
            for b in range(len(targets)):
                target_b = targets[b]
                L = int(batch["lengths"][b].item())
                
                # Overall max probability over full sequence
                max_q_all = np.max(q_np[b, :L])
                overall_data["probs"].append(max_q_all)
                overall_data["targets"].append(target_b)
                
                # Step-wise max probability (Horizon Max-Pooling)
                for s in steps_to_check:
                    if L >= s:
                        max_q = np.max(q_np[b, :s])
                        step_data[s]["probs"].append(max_q)
                        step_data[s]["targets"].append(target_b)
                        
    # Print Markdown Table
    print(f"| Step | Acc (t=0.5) | Brier | AUC-ROC | Recall | FPR | N |")
    print(f"| :--- | :--- | :--- | :--- | :--- | :--- | :--- |")
    for s in steps_to_check:
        probs = np.array(step_data[s]["probs"])
        targets = np.array(step_data[s]["targets"])
        if len(probs) == 0:
            print(f"| {s} | N/A | N/A | N/A | N/A | N/A | 0 |")
            continue
        acc_s, brier_s, auc_s, recall_s, fpr_s = calculate_metrics(probs, targets)
        print(f"| {s} | {acc_s} | {brier_s} | {auc_s} | {recall_s} | {fpr_s} | {len(probs)} |")
        
    # Overall
    probs = np.array(overall_data["probs"])
    targets = np.array(overall_data["targets"])
    acc_o, brier_o, auc_o, recall_o, fpr_o = calculate_metrics(probs, targets)
    print(f"| Overall | {acc_o} | {brier_o} | {auc_o} | {recall_o} | {fpr_o} | {len(probs)} |")
    
    # Cleanup sys.path
    if str(model_dir) in sys.path:
        sys.path.remove(str(model_dir))
        
    return {
        "step150": step_data[150],
        "overall": overall_data
    }

def main():
    base_dir = "/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone"
    
    configs = [
        # 1. v8 tests balanced
        {
            "name": "LSTM Calibrator with Suite ID Prior (Suite ID Enabled)",
            "model_dir": f"{base_dir}/experiments/v8_exp08_balanced/code",
            "ckpt_path": f"{base_dir}/experiments/v8_exp08_balanced/runs/best.pt",
            "is_lstm": True,
            "use_suite_id": True,
            "is_49d": False,
            "is_v9": False
        },
        {
            "name": "LSTM Calibrator with Suite ID Prior (Suite ID Disabled at Eval)",
            "model_dir": f"{base_dir}/experiments/v8_exp08_balanced/code",
            "ckpt_path": f"{base_dir}/experiments/v8_exp08_balanced/runs/best.pt",
            "is_lstm": True,
            "use_suite_id": False,
            "is_49d": False,
            "is_v9": False
        },
        {
            "name": "LSTM Calibrator (No Suite ID - Trained Without It)",
            "model_dir": f"{base_dir}/experiments/v8_exp09_no_suite_embed/code",
            "ckpt_path": f"{base_dir}/experiments/v8_exp09_no_suite_embed/runs/best.pt",
            "is_lstm": True,
            "use_suite_id": False,
            "is_49d": False,
            "is_v9": False
        },
        # 2. Selected ideas from 100 tests folder
        {
            "name": "Time-Blind MLP with Log-Compressed Uncertainty (Idea 139)",
            "model_dir": f"{base_dir}/experiments/a_100_tests/idea_139",
            "ckpt_path": f"{base_dir}/experiments/a_100_tests/idea_139/runs/best.pt",
            "is_lstm": False,
            "use_suite_id": False,
            "is_49d": False,
            "is_v9": False
        },
        {
            "name": "Time-Blind MLP with Softplus-Compressed Uncertainty (Idea 166)",
            "model_dir": f"{base_dir}/experiments/a_100_tests/idea_166",
            "ckpt_path": f"{base_dir}/experiments/a_100_tests/idea_166/runs/best.pt",
            "is_lstm": False,
            "use_suite_id": False,
            "is_49d": False,
            "is_v9": False
        },
        {
            "name": "Time-Blind MLP Safety Specialist (Idea 176)",
            "model_dir": f"{base_dir}/experiments/a_100_tests/idea_176",
            "ckpt_path": f"{base_dir}/experiments/a_100_tests/idea_176/runs/best.pt",
            "is_lstm": False,
            "use_suite_id": False,
            "is_49d": False,
            "is_v9": False
        },
        {
            "name": "Time-Blind MLP Uncertainty-Gated Alerts (Idea 210)",
            "model_dir": f"{base_dir}/experiments/a_100_tests/idea_210",
            "ckpt_path": f"{base_dir}/experiments/a_100_tests/idea_210/runs/best.pt",
            "is_lstm": False,
            "use_suite_id": False,
            "is_49d": False,
            "is_v9": False
        },
        # 3. Final 49D * 2
        {
            "name": "Entropy LSTM (49D + Suite ID - Suite ID Enabled)",
            "model_dir": f"{base_dir}/experiments/v9_exp02/code",
            "ckpt_path": f"{base_dir}/experiments/v9_exp02/runs/best.pt",
            "is_lstm": True,
            "use_suite_id": True,
            "is_49d": True,
            "is_v9": True
        },
        {
            "name": "Entropy LSTM (49D + Suite ID - Suite ID Disabled at Eval)",
            "model_dir": f"{base_dir}/experiments/v9_exp02/code",
            "ckpt_path": f"{base_dir}/experiments/v9_exp02/runs/best.pt",
            "is_lstm": True,
            "use_suite_id": False,
            "is_49d": True,
            "is_v9": True
        },
        {
            "name": "Entropy LSTM (49D - Trained Without Suite ID)",
            "model_dir": f"{base_dir}/experiments/v9_exp01/code",
            "ckpt_path": f"{base_dir}/experiments/v9_exp01/runs/best.pt",
            "is_lstm": True,
            "use_suite_id": False,
            "is_49d": True,
            "is_v9": True
        }
    ]
    
    results = {}
    for config in configs:
        if config["is_v9"]:
            id_data = f"{base_dir}/experiments/v9_exp02/data/v9_test.pt"
            ood_data = f"{base_dir}/experiments/v9_exp02/data/v9_unseen_obj_ood.pt"
        else:
            id_data = f"{base_dir}/data/v8_balanced/v8_test.pt"
            ood_data = f"{base_dir}/data/v8_balanced/v8_unseen_obj_ood.pt"
            
        id_res = run_evaluation(
            model_name=config["name"] + " [In-Distribution]",
            model_dir=config["model_dir"],
            ckpt_path=config["ckpt_path"],
            dataset_path=id_data,
            is_lstm=config["is_lstm"],
            use_suite_id=config["use_suite_id"],
            is_49d=config["is_49d"]
        )
        results[config["name"] + "_ID_150"] = id_res["step150"]
        results[config["name"] + "_ID_overall"] = id_res["overall"]
        
        ood_res = run_evaluation(
            model_name=config["name"] + " [Out-of-Distribution]",
            model_dir=config["model_dir"],
            ckpt_path=config["ckpt_path"],
            dataset_path=ood_data,
            is_lstm=config["is_lstm"],
            use_suite_id=config["use_suite_id"],
            is_49d=config["is_49d"]
        )
        results[config["name"] + "_OOD_150"] = ood_res["step150"]
        results[config["name"] + "_OOD_overall"] = ood_res["overall"]
        
    torch.save(results, f"{base_dir}/all_predictions_data.pt")
    print(f"\nAll prediction data saved to {base_dir}/all_predictions_data.pt")

if __name__ == "__main__":
    main()
