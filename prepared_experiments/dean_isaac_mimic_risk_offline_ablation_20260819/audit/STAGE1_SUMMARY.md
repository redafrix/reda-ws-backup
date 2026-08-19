# Stage 1 Audit Summary — Dean Isaac Mimic-style Risk Offline Ablation

## 1. Round0 Dataset & Frozen Split
- Committed Episodes: 4000 (Successes: 3908, Failures: 92)
- Total Query Rows: 75603
- Split Breakdown:
  - Train: 2800 episodes (64 failures), 52825 rows
  - Validation: 600 episodes (14 failures), 11410 rows
  - Test: 600 episodes (14 failures), 11368 rows
- Hashes:
  - dataset_manifest.json: `8e3b7f4929fce4a648f174735ec9c0530966cf4e8a93a66a3e793432a5be4859`
  - split_assignments.json: `a4b82dd6e6d944b2719ea071d1e66636cc4816e5e159c23adee382ff9e9ecac3`
  - normalization.json: `78c934b33e0536bd7cb6b7e5b1962da32305729f602d8269d3a38422841ce050`

## 2. Candidate Contract
- Main Candidate Shape: `[10, 7]`
- Alternative Candidates Count: 8
- Alternative Candidates Shape: `[10, 7]`
- Total Candidates: 9
- Seed Violations: 0
- Candidate Violations: 0

## 3. Dynamics & Denoising Evidence
- Candidate 0:
  - Full X_d saved: NO
  - Full V_d saved: NO
  - Raw uncertainty keys saved: ['denoise_mean_trace', 'final_action_normalized', 'initial_noise', 'last_step_variance', 'path_variance', 'uncertainty_parameterization', 'update_norm_trace', 'update_vector_trace', 'velocity_norm_trace']
- Alternatives 1..8:
  - Per-step X_d saved: NO
  - Per-step V_d saved: NO
  - Variance trace saved: NO
  - Raw uncertainty saved: NO

## 4. Friend Head Contract
- Authoritative Source: Paper-level K1 contract from `PROTOCOL.md` (SHA256: `0c49b84254f2fd6caf8d478b76f4e28ee8c36b9d23f2c16781c942babdcf5a71`)
- Architecture: 2-layer GRU (128 hidden, 128 static, 64 latent, 1 logit)
- Features: 37 static scalars + [10, 6] horizon features
- Calibration: Conformal & empirical episode-max on successful validation episodes

## 5. Invalidation Check
- Commit 70327b4b31bde35c01fda29a807f9100b5295a62 blacklisted: YES
- No candidate0 denoising trace copied into alternatives: VERIFIED
