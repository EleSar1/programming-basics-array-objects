import unittest
from main import avoiding_duplicates


class TestAvoidingDuplicates(unittest.TestCase):
    def test_avoiding_duplicates_ok(self):
        result = avoiding_duplicates(["Hello", "Hello", "world"])
        self.assertEqual(result, ["Hello", "world"])

    def test_wrong_parameter_type(self):
        with self.assertRaises(TypeError):
            avoiding_duplicates(4.5)

    def test_wrong_type_in_words(self):
        with self.assertRaises(TypeError):
            avoiding_duplicates(["a", 3, 5, "d"])


if __name__ == "__main__":
    unittest.main()