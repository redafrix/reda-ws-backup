#!/usr/bin/env python3
import torch, numpy as np, sys, os
from scipy.stats import pearsonr, spearmanr
from sklearn.metrics import roc_auc_score

def eval_simvla_only(predictions, true_errors, context_ids, seeds, bad_action_percentile=70):
    """
    Evaluate uncertainty predictions only on SimVLA generated seeds.
    predictions: list of predicted uncertainties
    true_errors: list of true L2 errors
    context_ids: list of context IDs
    seeds: list of seed IDs corresponding to each row
    """
    preds = np.array(predictions)
    trues = np.array(true_errors)
    cids = np.array(context_ids)
    sids = np.array(seeds)

    # 1. Pearson and 2. Spearman
    p_corr, _ = pearsonr(preds, trues)
    s_corr, _ = spearmanr(preds, trues)

    # 3. AUROC
    thresh = np.percentile(trues, bad_action_percentile)
    labels = (trues > thresh).astype(int)
    auroc = roc_auc_score(labels, preds) if len(np.unique(labels)) > 1 else np.nan

    # Group by context
    unique_cids = np.unique(cids)
    
    pairwise_correct = 0
    pairwise_total = 0
    
    best_pred_errors = []
    seed0_errors = []
    random_errors = []
    oracle_best_errors = []

    for cid in unique_cids:
        idx = np.where(cids == cid)[0]
        c_preds = preds[idx]
        c_trues = trues[idx]
        c_seeds = sids[idx]

        if len(c_preds) < 2:
            continue
            
        # 4. Pairwise ranking
        for i in range(len(c_preds)):
            for j in range(i+1, len(c_preds)):
                if c_trues[i] == c_trues[j]:
                    continue
                # tie in predictions counts as 0.5 regardless of trues
                if c_preds[i] == c_preds[j]:
                    pairwise_correct += 0.5
                elif (c_preds[i] < c_preds[j]) == (c_trues[i] < c_trues[j]):
                    pairwise_correct += 1
                pairwise_total += 1

        # 5. Best-seed selection
        pred_best_idx = np.argmin(c_preds)
        best_pred_errors.append(c_trues[pred_best_idx])
        
        if 0 in c_seeds:
            s0_idx = np.where(c_seeds == 0)[0][0]
            seed0_errors.append(c_trues[s0_idx])
        else:
            seed0_errors.append(c_trues[0]) # fallback

        random_errors.append(np.mean(c_trues))
        oracle_best_errors.append(np.min(c_trues))

    pairwise_acc = pairwise_correct / pairwise_total if pairwise_total > 0 else np.nan
    
    best_pred_mean = np.mean(best_pred_errors)
    seed0_mean = np.mean(seed0_errors)
    random_mean = np.mean(random_errors)
    oracle_mean = np.mean(oracle_best_errors)

    # 6. Risk-coverage
    sort_idx = np.argsort(preds)
    sorted_trues = trues[sort_idx]
    
    coverages = [0.1, 0.25, 0.5, 0.75, 1.0]
    risk_cov = {}
    for c in coverages:
        k = max(1, int(len(sorted_trues) * c))
        risk_cov[c] = np.mean(sorted_trues[:k])

    # 7. Switch proxy
    switch_proxy = {}
    for reject_rate in [0.1, 0.25, 0.5, 0.75]:
        keep_rate = 1.0 - reject_rate
        k = max(1, int(len(sorted_trues) * keep_rate))
        accepted_mean = np.mean(sorted_trues[:k])
        rejected_mean = np.mean(sorted_trues[k:]) if k < len(sorted_trues) else np.nan
        switch_proxy[reject_rate] = {
            'accepted_mean': accepted_mean,
            'rejected_mean': rejected_mean,
            'acceptance_rate': keep_rate
        }

    return {
        'pearson': p_corr,
        'spearman': s_corr,
        'auroc': auroc,
        'pairwise_acc': pairwise_acc,
        'best_seed': {
            'predicted_best': best_pred_mean,
            'seed0': seed0_mean,
            'random': random_mean,
            'oracle_best': oracle_mean,
            'gap_to_oracle': best_pred_mean - oracle_mean,
            'improvement_over_seed0': seed0_mean - best_pred_mean
        },
        'risk_coverage': risk_cov,
        'switch_proxy': switch_proxy
    }

def main():
    print("Testing SimVLA-only evaluator with dummy predictions...")
    
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/data/stage5_debug/multiseed_candidate_debug.pt'
    
    if not os.path.exists(path):
        print(f"File {path} not found.")
        return

    data = torch.load(path, map_location='cpu')
    cands = data['candidates']
    
    simvla_cands = [c for c in cands if c['candidate_type'].startswith('simvla_seed')]
    
    trues = [c['true_chunk_l2_error'] for c in simvla_cands]
    cids = [c['context_id'] for c in simvla_cands]
    seeds = [int(c['candidate_type'].replace('simvla_seed', '')) for c in simvla_cands]
    
    print(f"Evaluating on {len(trues)} SimVLA candidates...")
    
    # Dummy 1: Perfect prediction
    print("\n--- Perfect Prediction Dummy ---")
    res1 = eval_simvla_only(trues, trues, cids, seeds)
    for k, v in res1.items():
        print(f"{k}: {v}")
        
    # Dummy 2: Random prediction
    print("\n--- Random Prediction Dummy ---")
    np.random.seed(42)
    rand_preds = np.random.rand(len(trues))
    res2 = eval_simvla_only(rand_preds, trues, cids, seeds)
    for k, v in res2.items():
        print(f"{k}: {v}")

if __name__ == '__main__':
    main()
