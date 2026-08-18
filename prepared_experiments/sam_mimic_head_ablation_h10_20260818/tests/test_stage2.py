
import unittest
import numpy as np
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / 'collector'))
from simvla_mimic_action_adapter import action_7d_to_10d
from simvla_mimic_features import compute_denoising_metrics

class TestAdapter(unittest.TestCase):
    def test_shape(self):
        a = np.zeros((10, 10, 7))
        b = action_7d_to_10d(a)
        self.assertEqual(b.shape, (10, 10, 10))
    def test_identity(self):
        a = np.zeros(7)
        b = action_7d_to_10d(a)
        self.assertEqual(b.shape, (10,))
        
class TestDenoising(unittest.TestCase):
    def test_metrics(self):
        X = np.random.randn(8, 10, 7)
        V = np.random.randn(8, 10, 7)
        m = compute_denoising_metrics(X, V)
        self.assertIn("sample_pairwise_mse_mean", m)

if __name__ == '__main__':
    unittest.main()
