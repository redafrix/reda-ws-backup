# Pi0.5 Online OOD Evaluation Report (18-Task, 10-Episode Sweep)
    
This report evaluates the online performance of the Pi0.5 vision-language-action policy on the official 18-task `libero_goal_object_ood` suite on Bob. We compare Policy A (`pi05_basic_h10`) against Policy B (`pi05_risk_selected_cap_topk8_h10`) using SimVLA selected-cap triggers.

* **Reset Seeds:** 200..209 (paired across policies)
* **Suite:** `libero_goal_object_ood` (18 tasks, max steps = 800)
* **Horizon Execution:** H=10
* **Selected-cap parameters:** Trigger threshold 0.3, Min margin 0.02, Strong margin 0.05, Cap 0.4

---

## 1. Global Success Rates

* **Basic Policy (`pi05_basic_h10`):** 97.78% (176 / 180 successes)
* **Risk-Aware Selected-Cap Policy:** 97.78% (176 / 180 successes)
* **Net Success Gain:** +0.00 percentage points
* **Average Successful Episode Length:**
  - Basic Policy: 112.5 steps
  - Risk-Aware Policy: 113.8 steps

---

## 2. Per-Task Success & Intervention Table

| Task | Basic Success | Risk Success | Delta | Avg Risk Mods / Ep |
|---|---:|---:|---:|---:|
| 0 | 100.0% | 100.0% | +0.0% | 0.00 |
| 1 | 100.0% | 100.0% | +0.0% | 0.00 |
| 2 | 100.0% | 90.0% | -10.0% | 0.00 |
| 3 | 100.0% | 100.0% | +0.0% | 0.00 |
| 4 | 90.0% | 100.0% | +10.0% | 0.00 |
| 5 | 100.0% | 100.0% | +0.0% | 0.00 |
| 6 | 100.0% | 100.0% | +0.0% | 0.00 |
| 7 | 100.0% | 100.0% | +0.0% | 0.00 |
| 8 | 100.0% | 100.0% | +0.0% | 0.00 |
| 9 | 90.0% | 90.0% | +0.0% | 0.00 |
| 10 | 100.0% | 100.0% | +0.0% | 0.00 |
| 11 | 100.0% | 100.0% | +0.0% | 0.00 |
| 12 | 90.0% | 90.0% | +0.0% | 0.00 |
| 13 | 90.0% | 100.0% | +10.0% | 0.00 |
| 14 | 100.0% | 100.0% | +0.0% | 0.00 |
| 15 | 100.0% | 100.0% | +0.0% | 0.00 |
| 16 | 100.0% | 90.0% | -10.0% | 0.00 |
| 17 | 100.0% | 100.0% | +0.0% | 0.20 |


---

## 3. Intervention Statistics & Conformal Mass Alarm

* **Selected-cap replacements:** 2 query-level replacements total across the risk-aware sweep.
* **q95_mass_10 alarm episodes:** 2 / 180 episodes (1.11%)
* **Candidate Choice Distribution:** Cand 4: 1, Cand 8: 1
* **Average Main Risk Score:** 0.7949
* **Average Selected Risk Score:** 0.7949 (an average absolute risk reduction of 0.0000 per query)
* **Conformal Mass Alarm Rate (q95_mass_10):** 1.11% of risk-policy episodes triggered

---

## 4. Transfer Caveats from SimVLA to Pi0.5
While the selected-cap constants (0.3 trigger, 0.02 min margin, 0.05 strong margin, 0.4 cap) successfully transferred to Pi0.5 online sweeps, it is critical to note that the under-the-hood risk scores are different due to model family variance. Pi0.5's wrist camera inputs were real (compared to the padded ones used in SimVLA OOD runs) and its flow noise candidates produced real, valid ACE entropy. Therefore, the absolute risk values represent model-specific confidence margins.
