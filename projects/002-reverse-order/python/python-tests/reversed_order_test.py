import unittest
from ..code.main import reversed_order


class TestReversedOrder(unittest.TestCase):
    def test_reversed_ok(self):
        result = reversed_order([2,5,3,4,1])
        expected_result = [5,4,3,2,1]
        self.assertEqual(result, expected_result, f"The expected result of [2, 5, 3, 4, 1] was {expected_result}, got {result} instead.")


    def test_type_error(self):
        with self.assertRaises(TypeError):
            reversed_order(45)

if __name__ == '__main__':
    unittest.main()
