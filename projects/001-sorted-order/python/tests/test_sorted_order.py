import unittest
from ..code.main import sorted_order

class TestSortedOrder(unittest.TestCase):
    def test_sorted_order_positive_numbers(self):

        self.assertEqual(sorted_order([3, 1, 55, 15]), [1, 3, 15, 55], "Result of [3, 1, 55, 15] should be: [1, 3, 15, 55]")

    def test_sorted_order_negative_numbers(self):

        self.assertEqual(sorted_order([-4, -8, -2, -15]), [-15, -8, -4, -2], "Result of [-4, -8, -2, -15] should be [-15, -8, -4, -2]")

    def test_sorted_order_mixed_numbers(self):

        self.assertEqual(sorted_order([5, -50, 10, -2]), [-50, -2, 5, 10], "Result of [5, -50, 10, -2] should be [-50, -2, 5, 10]")

    def test_sorted_order_with_invalid_parameter(self):

        with self.assertRaises(TypeError):
            sorted_order(45)

if __name__ == '__main__':
    unittest.main()
