import pytest
import os
import sys

sys.path.append(os.path.abspath("projects/023-scrabble-score"))
from python.main import scrabble_score


def test_scrabble_score():

    # Test case 1: Simple word
    assert scrabble_score("hello") == 8, "Expected score for 'hello' is 8"
    
    # Test case 2: Word with high value letters
    assert scrabble_score("quiz") == 22, "Expected score for 'quiz' is 22"
    
    # Test case 4: Word with multiple letters, including repeats
    assert scrabble_score("scrabble") == 14, "Expected score for 'scrabble' is 14"
    
    # Test case 5: Empty string (no letters, so score is 0)
    assert scrabble_score("") == 0, "Expected score for an empty string is 0"
    
    # Test case 6: Word with numbers and special characters (should ignore them)
    assert scrabble_score("hello123!") == 8, "Expected score for 'hello123!' is 8"
    
    # Test case 7: Word with uppercase and lowercase letters (function should be case insensitive)
    assert scrabble_score("Hello") == 8, "Expected score for 'Hello' is 8"
    
    # Test case 8: Testing with all letters of the alphabet
    assert scrabble_score("abcdefghijklmnopqrstuvwxyz") == 87, "Expected score for all letters is 87"


if __name__ == "__main__":
    pytest.main()