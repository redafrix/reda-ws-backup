# OpenVLA-OFT OOD Basic vs Risk-Horizon Online Evaluation Launch

Date: 2026-06-18
Host: Bob / PCROBOTUBUNTU02

## Goal

Run the OpenVLA equivalent of the same-seed LIBERO-PRO goal-object OOD comparison used for the SimVLA selected-cap campaign.

## Suite and Seeds

- Suite: `libero_goal_object_ood`
- Task count: 18
- Tasks: all task ids `0..17`
- Seeds: `10..109`
- Episodes per task: 100
- Max steps: 800
- Total episodes: 3600

## Policies

1. `openvla_basic`
   - OpenVLA-OFT native execution horizon H=8.

2. `openvla_risk_horizon`
   - OpenVLA-OFT predicts H=8 chunks.
   - Risk model: final cleaned OpenVLA goal-object risk model, 300-step variant.
   - Model path: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/offline_risk_experiments/openvla_final1890_risk_20260618/models/model_300steps.pt`
   - Threshold: validation Q95 = `0.8049`
   - Policy: if risk >= 0.8049, execute H=1; otherwise execute H=8.

Note: This is not selected-cap action replacement, because OpenVLA has no validated ACE / candidate action generation path. It is the closest risk-aware online intervention available from the current trained OpenVLA risk model.

## Source Artifacts

- Runner: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/src/run_openvla_ood_online_baseline_vs_risk_20260618.py`
- Frozen training dataset: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/datasets/openvla_goal_object_final_1890_complete_rounds_20260618`
- Offline risk report: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/offline_risk_experiments/openvla_final1890_risk_20260618/reports/FINAL_1890_DATASET_RISK_EVALUATION_REPORT_20260618.md`

## Output

- Output root: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/online_evals/libero_goal_object_ood_openvla_basic_vs_risk_100ep_20260618`
- Log root: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/logs/libero_goal_object_ood_openvla_basic_vs_risk_100ep_20260618`
- Main log: `sweep_supervisor.log`
- Tmux session: `openvla_ood_basic_vs_risk_100ep_20260618`

## Smoke Verification

Before production launch, a smoke run was executed on task 0 / seed 10 for both policies.

- `openvla_basic`: success, 159 steps
- `openvla_risk_horizon`: success, 151 steps
- Risk query logging worked.
- The LIBERO-PRO OOD BDDL alias was patched in the runner only: init states use `libero_goal_object_ood`; BDDL resolves through `libero_goal_object_ood_temp`.

## Launch Status

Production launched successfully in tmux. First production episodes are being written.

At initial monitor:

- Episodes written: 4
- Current progress: `openvla_basic`, task 0, advancing through seeds
- No traceback after launch
- Tmux active

## Final Flags

SUITE = libero_goal_object_ood
TASK_COUNT = 18
SEEDS = 10..109
POLICIES = openvla_basic, openvla_risk_horizon
MAX_STEPS = 800
TOTAL_TARGET_EPISODES = 3600
RISK_MODEL = model_300steps.pt
RISK_THRESHOLD = 0.8049
RISK_POLICY = H1_IF_RISK_ELSE_H8
ACE_AVAILABLE = NO
SELECTED_CAP_REPLACEMENT = NO
TMUX_SESSION = openvla_ood_basic_vs_risk_100ep_20260618
STATUS = RUNNING
NEXT_ACTION = monitor only
