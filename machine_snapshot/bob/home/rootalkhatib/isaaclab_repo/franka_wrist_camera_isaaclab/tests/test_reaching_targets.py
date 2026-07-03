import unittest
import torch

from franka_wrist_camera_scene.policies.reaching_targets import compute_reaching_targets, quat_apply_xyzw


class TestReachingTargets(unittest.TestCase):
    def test_quat_apply_xyzw(self) -> None:
        quat = torch.tensor([[0.0, 0.0, 0.0, 1.0]])
        vec = torch.tensor([[0.1, 0.2, 0.3]])
        res = quat_apply_xyzw(quat, vec)
        self.assertTrue(torch.allclose(res, vec))

        quat = torch.tensor([[0.0, 0.0, 0.7071068, 0.7071068]])
        vec = torch.tensor([[1.0, 0.0, 0.0]])
        res = quat_apply_xyzw(quat, vec)
        expected = torch.tensor([[0.0, 1.0, 0.0]])
        self.assertTrue(torch.allclose(res, expected, atol=1e-5))

    def test_tcp_target_math_and_coordinate_conversion(self) -> None:
        ee_quat_w = torch.tensor([[0.0, 0.0, 0.0, 1.0]])
        ee_pos_w = torch.tensor([[0.1, 0.2, 0.3]])
        reach_pos_w = torch.tensor([[0.5, 0.2, 0.1]])
        tcp_offset_local = torch.tensor([[0.02, -0.01, 0.15]])

        target_hand_pos_w, state, state_start, motion, done = compute_reaching_targets(
            sim_time_s=0.0,
            state="move_to_target",
            state_start_time=None,
            motion=None,
            ee_pos_w=ee_pos_w,
            ee_quat_w=ee_quat_w,
            reach_pos_w=reach_pos_w,
            tcp_offset_local=tcp_offset_local,
            direct_reach_max_speed_m_s=0.16,
            reach_dwell_s=1.0,
        )

        target_hand_pos_w, state, state_start, motion, done = compute_reaching_targets(
            sim_time_s=10.0,
            state=state,
            state_start_time=state_start,
            motion=motion,
            ee_pos_w=ee_pos_w,
            ee_quat_w=ee_quat_w,
            reach_pos_w=reach_pos_w,
            tcp_offset_local=tcp_offset_local,
            direct_reach_max_speed_m_s=0.16,
            reach_dwell_s=1.0,
        )

        tcp_offset_w = quat_apply_xyzw(ee_quat_w, tcp_offset_local)
        reconstructed_tcp = target_hand_pos_w + tcp_offset_w
        self.assertTrue(torch.allclose(reconstructed_tcp, reach_pos_w, atol=1e-4))
        self.assertEqual(state, "reach_dwell")

    def test_reach_dwell_transitions_to_done(self) -> None:
        ee_quat_w = torch.tensor([[0.0, 0.0, 0.0, 1.0]])
        ee_pos_w = torch.tensor([[0.1, 0.2, 0.3]])
        reach_pos_w = torch.tensor([[0.5, 0.2, 0.1]])
        tcp_offset_local = torch.tensor([[0.02, -0.01, 0.15]])

        target_hand_pos_w, state, state_start, motion, done = compute_reaching_targets(
            sim_time_s=5.0,
            state="reach_dwell",
            state_start_time=5.0,
            motion=None,
            ee_pos_w=ee_pos_w,
            ee_quat_w=ee_quat_w,
            reach_pos_w=reach_pos_w,
            tcp_offset_local=tcp_offset_local,
            direct_reach_max_speed_m_s=0.16,
            reach_dwell_s=1.0,
        )
        self.assertFalse(done)
        self.assertEqual(state, "reach_dwell")

        target_hand_pos_w, state, state_start, motion, done = compute_reaching_targets(
            sim_time_s=6.1,
            state="reach_dwell",
            state_start_time=5.0,
            motion=None,
            ee_pos_w=ee_pos_w,
            ee_quat_w=ee_quat_w,
            reach_pos_w=reach_pos_w,
            tcp_offset_local=tcp_offset_local,
            direct_reach_max_speed_m_s=0.16,
            reach_dwell_s=1.0,
        )
        self.assertTrue(done)

    def test_unknown_reaching_state_raises(self) -> None:
        with self.assertRaises(ValueError):
            compute_reaching_targets(
                sim_time_s=0.0,
                state="bad_state",
                state_start_time=None,
                motion=None,
                ee_pos_w=torch.zeros(1, 3),
                ee_quat_w=torch.tensor([[0.0, 0.0, 0.0, 1.0]]),
                reach_pos_w=torch.zeros(1, 3),
                tcp_offset_local=torch.zeros(1, 3),
                direct_reach_max_speed_m_s=0.16,
                reach_dwell_s=1.0,
            )
