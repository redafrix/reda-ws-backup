import unittest

import numpy as np

from franka_wrist_camera_scene.simvla.policy import SimVLAActionPolicy, SimVLALiveObservation


class FakeRuntime:
    def __init__(self) -> None:
        self.device = "cpu"
        self.calls = 0

    def infer(self, language_instruction, image_input, image_mask, proprio):
        self.calls += 1
        return type(
            "Output",
            (),
            {
                "actions": np.tile(
                    np.array([[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0]], dtype=np.float32),
                    (10, 1),
                ),
                "uncertainty": {},
            },
        )()


class SimVLAPolicyTests(unittest.TestCase):
    def test_policy_replans_at_configured_camera_tick(self) -> None:
        runtime = FakeRuntime()
        policy = SimVLAActionPolicy(runtime, image_rotation="none", replan_steps=2)
        observation = SimVLALiveObservation(
            language_instruction="reach the avocado",
            agent_rgb=np.zeros((480, 640, 3), dtype=np.uint8),
            wrist_rgb=np.zeros((480, 640, 3), dtype=np.uint8),
            ee_pos_w=np.array([0.5, 0.0, 1.0]),
            ee_quat_wxyz=np.array([1.0, 0.0, 0.0, 0.0]),
            env_origin_w=np.zeros(3),
            commanded_finger_opening_m=0.04,
        )

        first = policy.step(observation, camera_tick=0)
        second = policy.step(observation, camera_tick=1)
        third = policy.step(observation, camera_tick=2)

        self.assertEqual(runtime.calls, 2)
        self.assertEqual(first.finger_opening_m, 0.04)
        self.assertEqual(second.finger_opening_m, 0.04)
        self.assertEqual(third.finger_opening_m, 0.04)
        self.assertAlmostEqual(float(first.target_pos_w[0, 0]), 0.55)

    def test_policy_rejects_repeated_camera_tick(self) -> None:
        runtime = FakeRuntime()
        policy = SimVLAActionPolicy(runtime, image_rotation="none", replan_steps=2)
        observation = SimVLALiveObservation(
            language_instruction="reach the avocado",
            agent_rgb=np.zeros((480, 640, 3), dtype=np.uint8),
            wrist_rgb=np.zeros((480, 640, 3), dtype=np.uint8),
            ee_pos_w=np.array([0.5, 0.0, 1.0]),
            ee_quat_wxyz=np.array([1.0, 0.0, 0.0, 0.0]),
            env_origin_w=np.zeros(3),
            commanded_finger_opening_m=0.04,
        )

        policy.step(observation, camera_tick=0)

        with self.assertRaises(RuntimeError):
            policy.step(observation, camera_tick=0)


if __name__ == "__main__":
    unittest.main()
