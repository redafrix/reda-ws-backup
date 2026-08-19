# Current-Protocol OOD400 Baseline Collector Audit

## 1. Executive Summary
- **Protocol**: IsaacLab Franka Reaching, H10 execution horizon, 30 Hz control rate, 120 Hz physics (decimation 4), max 350 control ticks (1400 simulation steps).
- **Termination Invariant**: Strict success at $\le 0.030\text{ m}$ TCP distance. Immediate termination on first simulation substep meeting distance threshold (**NO DWELL**, `settle_time_s = 0.0`).
- **Baseline Execution Mode**: Normal SimVLA execution where candidate 0 is executed for all control ticks. Shadow risk scoring on 9 sampled candidates per decision query.
- **Intervention Count**: 0 (zero policy modification).
- **Benchmark Manifest**: `benchmarks/reaching_mimic_risk_ood400/full_ood400.json` (SHA256: `264dae5a7de872e5aee0a9554f88adfe7af3d38b5a7e29fd7f9b3e0d1c10da41`, 400 canonical OOD scenes).

## 2. Feature & Storage Specifications
- **History Representation**: 16 timesteps $\times$ 21 dimensions (`history_mean` / `history_std` normalization).
- **Action Representation**: 10 horizon steps $\times$ 7 dimensions (`action_mean` / `action_std` normalization).
- **Static Features (51D)**:
  - 28D action statistics on normalized candidate chunk.
  - 7D ACE vector from 8 ACE alternatives.
  - 8D proprioceptive state (`ee_pos`, `ee_quat`, `finger_opening`).
  - 8D TopK8 uncertainty features at indices `[6, 21, 25, 27, 23, 2, 26, 24]`.
- **Visual Recording**: Agent camera RGB at 320x240 @ 5 FPS, H.264 CRF 30 (~9-12 KB per episode).

## 3. Smoke Test Verification
- Executed on Dean (RTX 5090) over benchmark episodes 0..2.
- Ep 000000: SUCCESS at tick 122 (dist 0.0297m, 13 decisions).
- Ep 000001: FAILURE at tick 350 (dist 0.3627m, 35 decisions).
- Ep 000002: SUCCESS at tick 166 (dist 0.0299m, 17 decisions).
- Verified: No NaNs, exact crossing fields populated, video files non-empty and readable, fingerprints matching manifest.
