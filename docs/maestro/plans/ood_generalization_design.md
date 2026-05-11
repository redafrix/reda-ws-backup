# Implementation Plan: OOD Generalization Strategy

## Objective
Implement and systematically evaluate a series of architectural and representation improvements aimed at improving out-of-distribution (OOD) generalization for the TDQC Calibrator model. 

## Background & Motivation
The current baseline (`v7_exp02`) performs well on in-distribution data but lacks robust generalization for unseen objects, as its representations are scale-dependent. Based on research, we will iterate through several methods to build object-invariant, dynamics-sensitive models.

## Scope & Impact
1. **Experiment 04 (Deltas + Instance Norm):** Augment the feature set to 22D (11 raw + 11 temporal deltas) and apply learnable `InstanceNorm1d` to extract dynamics regardless of absolute scale.
2. **Experiment 05 (DANN):** Implement Domain-Adversarial Neural Networks with a Gradient Reversal Layer to explicitly penalize domain/suite-specific representations.
3. **Experiment 06 (Contrastive Pretraining):** Pretrain the encoder using contrastive pairs to cluster pre-failure states regardless of the object.
4. **Experiment 07 (Custom R&D):** Develop a novel hybrid or attention-based approach based on the empirical results of Exp 04-06.

## Proposed Solution: Experiment 04 Pipeline
1. **Data Prep (22D + OOD):**
   - Write a dataset builder to generate 22D features from the original `phase2_tdqc_denoise_clean_splits_20260504`.
   - Extract `phase2_tdqc_goal_object_ood_denoise_OOD_test.zip`.
   - Process the OOD dataset into the same 22D format.
2. **Model Architecture:**
   - Clone `core/` to `experiments/v7_exp04_delta_instnorm/code/`.
   - Modify `tdqc_model.py` to accept `input_dim=22` and inject `nn.InstanceNorm1d(22, affine=True)` before the LSTM.
3. **Training & Evaluation:**
   - Train `v7_exp04` for 500 epochs in the foreground.
   - Run `eval_full.py` on the standard Test set.
   - Run `eval_full.py` on the OOD Test set to directly measure the generalization gap.

## Alternatives Considered
- **On-the-fly Delta Computation:** Computing deltas in the `DataLoader` saves disk space but slows down training. Pre-computing static `.pt` datasets is preferred for reproducible and fast epoch iteration.
- **Manual Normalization (Fix 3):** Preprocessing with Z-scores removes the absolute scale, but destroys potentially useful signal. `InstanceNorm1d(affine=True)` is strictly more expressive as it learns whether to retain absolute magnitude.

## Phased Implementation Plan
- **Phase 1:** OOD Data Extraction & Preprocessing Script.
- **Phase 2:** Generate Train/Val/Test + OOD Test `22D.pt` files.
- **Phase 3:** Setup `v7_exp04_delta_instnorm` model (Instance Norm) and verify forward pass.
- **Phase 4:** Foreground training for 500 epochs.
- **Phase 5:** Standard vs OOD Evaluation and plotting.
- **Phase 6+:** Iterative execution of Exp 05 (DANN), Exp 06, and Exp 07 using the same rigorous OOD benchmark.

## Verification
- Successful training completion (loss convergence).
- Output plots showing accuracy curves and reliability plots for both Standard Test and OOD Test.
- Expected gain: significantly reduced performance gap between ID and OOD splits.