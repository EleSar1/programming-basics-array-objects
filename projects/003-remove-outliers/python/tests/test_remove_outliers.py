import unittest
from ..source.main import remove_outliers

class TestRemoveOutliers(unittest.TestCase):
    def test_removed_outliers_ok(self):
        result = remove_outliers([4, -5, 14, 2, 5], 2)
        self.assertEqual(result, [4], f"Expected [4] as result, got {result} instead.")

    def test_parameters_type_error(self):
        with self.assertRaises(TypeError):
            remove_outliers(5, "")


    def test_negative_n(self):
        with self.assertRaises(ValueError):
            remove_outliers([1,2,3], -1)


if __name__ == '__main__':
    unittest.main()
