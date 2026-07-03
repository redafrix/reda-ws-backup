# Stage 5 SimVLA-only Evaluator Utility Report

Machine: Bob / `pcrobot` / `PCROBOTUBUNTU02`
Workspace: `/media/rootalkhatib/My Passport/reda_ws`
Branch: `bob`
Date: 2026-05-13

## 1. SimVLA-only Evaluator Status

Status: `OK`

Script:
`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/eval/eval_simvla_only.py`

Command:
```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source asynchvla_ws/scripts/activate_simvla_bob.sh
python3 asynchvla_ws/src/eval/eval_simvla_only.py
```

## 2. Utility Implementation

The `eval_simvla_only.py` script implements the following essential SimVLA-specific metrics required for Stage 5:
- **Pearson and Spearman Correlation:** Measures how well the predicted uncertainty correlates with true L2 error strictly on generated candidates (`simvla_seedX`).
- **AUROC for Bad-Action Detection:** Evaluates binary classification of the worst actions (top 30% by error) using the uncertainty proxy.
- **Pairwise Seed Ranking:** Calculates how often the seed with lower predicted uncertainty also possesses the lower true L2 error within the same context.
- **Best-Seed Selection:** Compares the mean true error of the seed with the lowest predicted uncertainty against a single static seed (seed 0), the random baseline, and the oracle best seed.
- **Risk-Coverage:** Computes mean error as confidence thresholds reject increasing percentages of candidate actions.
- **Switch Proxy:** Measures accepted and rejected mean errors given simulated fallback/rejection thresholds (10%, 25%, 50%, 75%).

## 3. Dummy Prediction Validation

The script was verified on the 250 debug SimVLA candidates using a "Perfect Prediction" (predictions equal to true errors) and "Random Prediction" (uniform random) baseline.

### Perfect Prediction Dummy
- **Pearson / Spearman:** 1.000 / 1.000
- **AUROC:** 1.000
- **Pairwise Accuracy:** 1.000
- **Best Seed Selection:** Gap to oracle = 0.0, Improvement over seed0 = 0.0789
- **Switch Proxy (Reject 50%):** Accepted Mean = 0.958, Rejected Mean = 2.061

### Random Prediction Dummy
- **Pearson / Spearman:** ~0.05 / ~0.05
- **AUROC:** 0.520
- **Pairwise Accuracy:** 0.448
- **Best Seed Selection:** Gap to oracle = 0.0613, Improvement over seed0 = 0.0176
- **Switch Proxy (Reject 50%):** Accepted Mean = 1.487, Rejected Mean = 1.532

## 4. Conclusion
Phase 3 completed successfully. The evaluator properly filters candidate types to isolate SimVLA-generated chunks, computing the core metrics needed to validate multi-seed sampling and runtime switching safety. The evaluator is ready to be integrated after the rater is trained.
