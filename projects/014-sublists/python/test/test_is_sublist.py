import pytest
import sys
import os

sys.path.append(os.path.abspath("projects/014-sublists"))
from python.main import is_sublist


def test_is_sublist():

    assert is_sublist([1,2,3,4,5], [3,4]) == True
    assert is_sublist(["a","b","c","d","e"], ["a","b","c"]) == True
    assert is_sublist([1,2,3,4], []) == True
    assert is_sublist([1,"a",3,4,5], [1,"a",3,4,5]) == True

def test_not_sublist():

    assert is_sublist([1,2,3,4,5], [6,7,8]) == False
    assert is_sublist([1,2,3,4,5], [12,34,5]) == False
    assert is_sublist([1, "a", 3], [1, "y", 3]) == False
    assert is_sublist(["1", "2", "3"], [1,2]) == False


if __name__ == "__main__":
    pytest.main()