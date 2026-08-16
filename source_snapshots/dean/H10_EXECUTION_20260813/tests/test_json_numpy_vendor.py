from __future__ import annotations

import unittest

import numpy as np

import json_numpy


class JsonNumpyVendorTest(unittest.TestCase):
    def test_round_trip(self) -> None:
        source = np.arange(12, dtype=np.float32).reshape(3, 4)
        decoded = json_numpy.loads(json_numpy.dumps({"value": source}))["value"]
        np.testing.assert_array_equal(decoded, source)
        self.assertEqual(decoded.dtype, source.dtype)


if __name__ == "__main__":
    unittest.main()
