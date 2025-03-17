import unittest
import sys
import os

sys.path.append(os.path.abspath("projects/007-only-the-words")) #can launch test directly from programming-basics-array-objects folder
from python.main import only_the_words


class TestOnlyTheWords(unittest.TestCase):

    def test_only_the_words_ok(self):

        """Tests the only_the_words function with a sentence containing contractions.  
        Verifies that punctuation at the edges is correctly removed while keeping contractions intact."""

        sentence = "Contractions include: don't, isn't, and wouldn't."
        result = only_the_words(sentence)
        expected_result = ["Contractions", "include", "don't", "isn't", "and", "wouldn't"]

        self.assertEqual(result, expected_result, f"Expected {expected_result} as result, got {result}.")

    
    def test_only_the_words_no_empty_spaces(self):

        """Tests the only_the_words function to ensure no empty strings  
        are included when punctuation appears alone."""

        sentence = "Contractions include: don't, - isn't, ! and wouldn't."
        result = only_the_words(sentence)
        expected_result = ["Contractions", "include", "don't", "isn't", "and", "wouldn't"]

        self.assertEqual(result, expected_result, f"Expected {expected_result} as result, got {result}.")

    
    def test_wrong_type_parameter(self):

        """Tests the only_the_words function with incorrect parameter types.  
        Ensures that passing non-string values raises a TypeError."""

        wrong_parameter = [1, 2.5, "Not supported"]
        with self.assertRaises(TypeError):
            for value in wrong_parameter:    
                only_the_words(value)


if __name__ == "__main__":
    unittest.main()