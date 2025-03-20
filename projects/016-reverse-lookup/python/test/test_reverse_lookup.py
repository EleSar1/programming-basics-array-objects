import pytest
import os
import sys

sys.path.append(os.path.abspath("projects/016-reverse-lookup"))
from python.main import reverse_lookup


def test_reverse_lookup():

    result = reverse_lookup({"n1": 1, "n2": 2, "n3": 3, "n4": 4}, 3)
    expected_result = ["n3"]

    assert result == expected_result


def test_reverse_lookup_no_existing_value():

    result = reverse_lookup({"n1": 1, "n2": 2, "n3": 3, "n4": 4}, 5)
    expected_result = []

    assert result == expected_result


def test_reverse_lookup_multiple_same_values():

    result = reverse_lookup({"n1": 1, "n2": 2, "n3": 1, "n4": 4}, 1)
    expected_result = ["n1", "n3"]

    assert result == expected_result


def test_reverse_lookup_empty_dict():

    result = reverse_lookup({}, 1)
    expected_result = []

    assert result == expected_result


def test_reverse_lookup_string_values():

    result = reverse_lookup({"k1": "apple", "k2": "banana", "k3": "apple"}, "apple")
    expected_result = ["k1", "k3"]
    
    assert result == expected_result


def test_reverse_lookup_float_values():

    result = reverse_lookup({"x": 1.1, "y": 2.2, "z": 1.1}, 1.1)
    expected_result = ["x", "z"]

    assert result == expected_result


def test_reverse_lookup_boolean_values():

    result = reverse_lookup({"t1": True, "t2": False, "t3": True}, True)
    expected_result = ["t1", "t3"]

    assert result == expected_result


def test_reverse_lookup_numeric_keys():

    result = reverse_lookup({1: "val", 2: "val", 3: "other"}, "val")
    expected_result = [1, 2]

    assert result == expected_result


def test_reverse_lookup_none_value():

    result = reverse_lookup({"a": None, "b": 2, "c": None}, None)
    expected_result = ["a", "c"]

    assert result == expected_result


if __name__ == "__main__":
    pytest.main()