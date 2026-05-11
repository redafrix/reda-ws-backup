# Workspace Migration Log (May 5, 2026)

## 🚨 CRITICAL PATH CHANGES
- **NEW WORKSPACE:** `/media/redafrix/My Passport/reda_ws`
- **STABLE ENV:** `/home/redafrix/envs/simvla`

## 🛠 POST-MIGRATION TASKS
1. **Update Activate Script:** Need to rewrite `intern_ship_ws/activate_simvla.sh` to point to `/home/redafrix/envs/simvla`.
2. **Fix PyTorch/CUDA:** The migrated environment needs a fresh PyTorch install to recognize the GPU on the new path.
3. **Run Exp 10 (33D Features):** 
   - **Target:** `experiments/v8_exp10_33d/`
   - **Data:** `data/v8_33d/` (v8_train.pt, v8_val.pt, v8_test.pt, v8_unseen_obj_ood.pt)
   - **Spec:** `input_dim=33` (0-10 raw, 11-21 deltas, 22-32 accelerations).
   - **Hyperparams:** Same as `v8_exp08_balanced`.
   - **Evals:** Test ID (v8_test.pt) and Test OOD (v8_unseen_obj_ood.pt). Report Brier, AUC, and OOD/ID ratio.

## 📝 MIGRATION DETAILS
- Moved ~122GB to external exfat drive.
- Moved 9.4GB environment to internal SSD to avoid exfat symlink issues.
- Original workspace `/home/redafrix/tests/intern_ship_research` has been DELETED to free space.
