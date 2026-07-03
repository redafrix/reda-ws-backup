# FIPER Target-Object OOD Fold_01 Full Results Report

This report summarizes the training and evaluation results for the **Target-Object OOD Fold 01** run on Sam, holding out `butter` and `chocolate_pudding`.

---

## 1. Exact Data Loaded

| Split Name | Rows Count | Episodes Count | Description |
|---|---|---|---|
| `success_train_seen` | 82,151 | 549 | Seen objects success training set (RND training) |
| `success_calib_seen` | 17,334 | 118 | Seen objects success calibration set (Threshold determination) |
| `success_test_seen` | 17,570 | 116 | Seen objects success test evaluation set |
| `success_test_ood` | 32,126 | 183 | Unseen (OOD) objects success evaluation set (`butter`, `chocolate_pudding`) |
| `failure_eval_seen` | 27,000 | 90 | Seen objects physical failure evaluation set |
| `failure_eval_ood` | 10,500 | 35 | Unseen (OOD) objects physical failure evaluation set |
| `failure_eval_ood_late` | 2,625 | 35 | Unseen objects late physical failure evaluation set (subset) |
| `failure_eval_ood_near_end` | 1,750 | 35 | Unseen objects near-end physical failure evaluation set (subset) |

---

## 2. Training

* **Epochs:** 20 (0 to 19)
* **Final Loss:** `0.00011606`
* **Loss Curve:**
  * Epoch 0 (First): `0.00089534`
  * Epoch 19 (Last): `0.00011606`
* **GPU Used:** NVIDIA GeForce RTX 4070 Ti (16GB VRAM) on Sam
* **Runtime:**
  * RND Training Duration: **55 seconds** (16:27:18 to 16:28:13)
  * Evaluation & Scoring Duration: **101 seconds** (16:28:13 to 16:29:54)
  * Total Pipeline Execution: **2 minutes 53 seconds** (16:27:18 to 16:30:11)

---

## 3. Calibrated Conformal Thresholds (q95)

* **RND Thresholds:**
  * `q90`: `0.02692292`
  * `q95`: `0.03335841`
  * `q99`: `0.05155298`
* **ACE Thresholds:**
  * `q90`: `-343.26005136`
  * `q95`: `-342.32687876`
  * `q99`: `-340.95284910`

---

## 4. Row-Level Metrics (q95)

| Split Name | RND q95 Rate | ACE q95 Rate | OR q95 Rate | AND q95 Rate |
|---|---|---|---|---|
| `success_test_seen` | 6.21% (0.0621) | 5.80% (0.0580) | 9.95% (0.0995) | 2.06% (0.0206) |
| `success_test_ood` | 27.81% (0.2781) | 11.50% (0.1150) | 34.05% (0.3405) | 5.25% (0.0525) |
| `failure_eval_seen` | 28.03% (0.2803) | 29.06% (0.2906) | 38.95% (0.3895) | 18.14% (0.1814) |
| `failure_eval_ood` | 47.54% (0.4754) | 40.82% (0.4082) | 57.85% (0.5785) | 30.51% (0.3051) |
| `failure_eval_ood_late` | 61.33% (0.6133) | 72.88% (0.7288) | 80.46% (0.8046) | 53.75% (0.5375) |
| `failure_eval_ood_near_end` | 62.91% (0.6291) | 74.40% (0.7440) | 82.00% (0.8200) | 55.31% (0.5531) |

---

## 5. Episode-Level Metrics

### A. Successful Episodes (False Alarms)

#### 1. Episode False Alarm Rate for OR (K=1)
* **`success_test_seen`:**
  * OR q90: **99.14%** (115/116)
  * OR q95: **90.52%** (105/116)
  * OR q99: **53.45%** (62/116)
* **`success_test_ood`:**
  * OR q90: **100.00%** (183/183)
  * OR q95: **100.00%** (183/183)
  * OR q99: **100.00%** (183/183)

#### 2. Episode False Alarm Rate and Alarm Step Statistics for OR q95 with Debounce K
* **`success_test_seen`:**
  * **K=1:** **90.52%** (105/116) | Mean: 15.07 steps | Median: 9.00 steps
  * **K=2:** **74.14%** (86/116)  | Mean: 9.43 steps  | Median: 3.00 steps
  * **K=3:** **58.62%** (68/116)  | Mean: 6.90 steps  | Median: 1.50 steps
  * **K=5:** **38.79%** (45/116)  | Mean: 4.36 steps  | Median: 0.00 steps
* **`success_test_ood`:**
  * **K=1:** **100.00%** (183/183) | Mean: 59.78 steps | Median: 55.00 steps
  * **K=2:** **100.00%** (183/183) | Mean: 45.44 steps | Median: 41.00 steps
  * **K=3:** **100.00%** (183/183) | Mean: 37.95 steps | Median: 35.00 steps
  * **K=5:** **99.45%** (182/183)  | Mean: 29.16 steps | Median: 27.00 steps

---

### B. Failed Episodes (Detection Performance under OR q95)

#### 1. Seen Failure Split: `failure_eval_seen` (90 episodes)
* **K=1:**
  * Detection Rate: **100.00%** (90/90) | Never Detected: 0.00%
  * Det@10%: 21.11% | Det@25%: 92.22% | Det@50%: 100.00%
  * Norm First Det Time (Detected only): Mean **0.1498** | Median **0.1550**
  * Norm First Det Time (All episodes):   Mean **0.1498** | Median **0.1550**
* **K=2:**
  * Detection Rate: **95.56%** (86/90)  | Never Detected: 4.44%
  * Det@10%: 10.00% | Det@25%: 63.33% | Det@50%: 91.11%
  * Norm First Det Time (Detected only): Mean **0.2429** | Median **0.1933**
  * Norm First Det Time (All episodes):   Mean **0.2766** | Median **0.2017**
* **K=3:**
  * Detection Rate: **87.78%** (79/90)  | Never Detected: 12.22%
  * Det@10%: 4.44%  | Det@25%: 51.11% | Det@50%: 81.11%
  * Norm First Det Time (Detected only): Mean **0.2808** | Median **0.2300**
  * Norm First Det Time (All episodes):   Mean **0.3687** | Median **0.2450**
* **K=5:**
  * Detection Rate: **80.00%** (72/90)  | Never Detected: 20.00%
  * Det@10%: 0.00%  | Det@25%: 35.56% | Det@50%: 75.56%
  * Norm First Det Time (Detected only): Mean **0.2997** | Median **0.2567**
  * Norm First Det Time (All episodes):   Mean **0.4397** | Median **0.3150**

#### 2. Unseen Failure Split: `failure_eval_ood` (35 episodes)
* **K=1:**
  * Detection Rate: **100.00%** (35/35) | Never Detected: 0.00%
  * Det@10%: 82.86% | Det@25%: 100.00% | Det@50%: 100.00%
  * Norm First Det Time (Detected only): Mean **0.0442** | Median **0.0367**
  * Norm First Det Time (All episodes):   Mean **0.0442** | Median **0.0367**
* **K=2:**
  * Detection Rate: **100.00%** (35/35) | Never Detected: 0.00%
  * Det@10%: 71.43% | Det@25%: 100.00% | Det@50%: 100.00%
  * Norm First Det Time (Detected only): Mean **0.0689** | Median **0.0533**
  * Norm First Det Time (All episodes):   Mean **0.0689** | Median **0.0533**
* **K=3:**
  * Detection Rate: **100.00%** (35/35) | Never Detected: 0.00%
  * Det@10%: 54.29% | Det@25%: 100.00% | Det@50%: 100.00%
  * Norm First Det Time (Detected only): Mean **0.1025** | Median **0.0933**
  * Norm First Det Time (All episodes):   Mean **0.1025** | Median **0.0933**
* **K=5:**
  * Detection Rate: **100.00%** (35/35) | Never Detected: 0.00%
  * Det@10%: 25.71% | Det@25%: 80.00% | Det@50%: 97.14%
  * Norm First Det Time (Detected only): Mean **0.1844** | Median **0.1667**
  * Norm First Det Time (All episodes):   Mean **0.1844** | Median **0.1667**

---

## 6. RND vs ACE Complementarity on `failure_eval_ood` (q95)

At the **episode level**, both RND and ACE trigger alarms on all 35 OOD failure episodes independently for all K settings:

| Debounce Setting | Both Detect | Only RND Detects | Only ACE Detects | Missed by Both |
|---|---|---|---|---|
| **K=1** | **100.00%** (35/35) | 0.00% (0/35) | 0.00% (0/35) | 0.00% (0/35) |
| **K=2** | **100.00%** (35/35) | 0.00% (0/35) | 0.00% (0/35) | 0.00% (0/35) |
| **K=3** | **100.00%** (35/35) | 0.00% (0/35) | 0.00% (0/35) | 0.00% (0/35) |
| **K=5** | **100.00%** (35/35) | 0.00% (0/35) | 0.00% (0/35) | 0.00% (0/35) |

*Note on Row-Level Complementarity (q95) for `failure_eval_ood`: RND triggers on 47.54% of steps, ACE on 40.82% of steps, with the intersection (AND) covering 30.51% of steps, and the union (OR) covering 57.85% of steps.*

---

## 7. Honest Judgment

### 1. Is target-object OOD failure detection useful?
**No, as currently implemented.** Although the monitor achieves a 100% detection rate on OOD failure episodes, this is a visual artifact. The visual features of the OOD target objects (`butter`, `chocolate_pudding`) trigger RND novelty alarms from the very first frame of the episode, regardless of whether the policy behaves correctly or fails. Because the successful OOD episodes (`success_test_ood`) also trigger false alarms at a **100.00% rate** (even with K=3), the detector has zero discriminative power between success and failure in OOD contexts.

### 2. Is target-object OOD early detection useful?
**No.** The extremely early detection times reported (e.g., mean norm time of `0.0442` for K=1, `0.1025` for K=3 on OOD failures) are misleading. They reflect the visual novelty of the object present at the beginning of the rollout rather than the detection of actual physical failure sequences.

### 3. Is target-object OOD success false alarm acceptable?
**Absolutely not.** An episode-level false alarm rate of **99.45%** (even at K=5) on successful OOD rollouts would render any physical deployment completely unusable. It would halt the robot during almost every single successful execution.

### 4. Is it deployable as a hard stop or only warning?
* **Hard Stop:** **No.** It would halt the robot on 100% of successful OOD tasks.
* **Warning:** **No.** Constant alarms from the start of every OOD run would result in immediate operator alarm fatigue, leading to warnings being ignored.

### 5. Does RND add value beyond ACE?
**No.** RND is extremely sensitive to pure visual distribution shift, causing a row-level false alarm rate of **27.81%** on successful OOD rollouts (compared to 6.21% on seen test success rollouts). This sensitivity makes RND the primary source of false alarms in OOD tasks, polluting the joint OR monitor.

### 6. Does ACE add value beyond RND?
**Yes, significantly.** ACE (Action Chunking Entropy) measures policy confidence and behavioral shift rather than pure pixel-level visual novelty. On `success_test_ood`, ACE's row-level false alarm rate is only **11.50%** (compared to RND's 27.81%). With debounce K=5, ACE's episode-level false alarm rate drops to **46.99%** (compared to RND's 98.36%). While 46.99% is still too high for deployment, it confirms that behavioral monitoring (ACE) is significantly more robust to visual OOD than pure representation novelty (RND).

---

## 8. Final Fields

```text
TARGET_OBJECT_FOLD_01_FULL_RUN_COMPLETE = YES
TARGET_OBJECT_OOD_FAILURE_DETECTION_USEFUL = NO
TARGET_OBJECT_OOD_EARLY_DETECTION_USEFUL = NO
TARGET_OBJECT_OOD_FALSE_ALARM_ACCEPTABLE = NO
READY_TO_RUN_MORE_TARGET_OBJECT_FOLDS = YES
RECOMMENDED_NEXT_FOLD = fold_00
```
