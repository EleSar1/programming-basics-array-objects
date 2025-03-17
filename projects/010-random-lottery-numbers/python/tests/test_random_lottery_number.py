import unittest
import os
import sys

sys.path.append(os.path.abspath("projects/010-random-lottery-numbers"))
from python.main import random_lottery_numbers


class TestRandomLotteryNumbers(unittest.TestCase):

    def test_len_random_lottery_numbers(self):
            
        """
        Verify that 'random_lottery_numbers' returns exactly 6 numbers.
        """

        result_length = len(random_lottery_numbers())
        expected = [0] * 6
        expected_len = len(expected)

        self.assertEqual(result_length, expected_len, f"Length out of range: got {result_length}, expected {expected_len}")


    def test_random_lottery_numbers_out_of_range(self):

        """
        Verify that returned value (numbers) contains only numbers between 1 and 49.
        """

        numbers = random_lottery_numbers()
        
        for number in numbers:
            if number < 1 or number > 49:
                self.fail(f"Number out of range: {number}.")


if __name__ == "__main__":
    unittest.main()