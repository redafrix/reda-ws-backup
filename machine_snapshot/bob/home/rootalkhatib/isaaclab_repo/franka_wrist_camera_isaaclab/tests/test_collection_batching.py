from unittest import TestCase

from franka_wrist_camera_scene.collection.batching import effective_asset_bank_episode_batch_size


class TestCollectionBatching(TestCase):
    def test_camera_collection_uses_single_asset_bank_scene(self) -> None:
        self.assertEqual(
            effective_asset_bank_episode_batch_size(
                2,
                episode_count=8,
                record_cameras=True,
            ),
            8,
        )

    def test_camera_collection_keeps_batch_when_it_already_covers_all_episodes(self) -> None:
        self.assertEqual(
            effective_asset_bank_episode_batch_size(
                16,
                episode_count=8,
                record_cameras=True,
            ),
            16,
        )

    def test_non_camera_collection_keeps_configured_batch_size(self) -> None:
        self.assertEqual(
            effective_asset_bank_episode_batch_size(
                2,
                episode_count=8,
                record_cameras=False,
            ),
            2,
        )

    def test_batch_size_must_be_positive(self) -> None:
        with self.assertRaisesRegex(ValueError, "asset_bank_episode_batch_size must be positive"):
            effective_asset_bank_episode_batch_size(
                0,
                episode_count=8,
                record_cameras=True,
            )
