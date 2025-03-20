import pytest
import sys
import os

sys.path.append(os.path.abspath("projects/018-text-messaging"))
from python.main import text_message_to_keys


def test_text_message_to_keys_ok():

    result = text_message_to_keys("hello!")
    expected_result = "44335555556661111"

    assert result == expected_result


def test_text_message_case_insensitive():

    result = text_message_to_keys("HeLLo!")
    expected_result = "44335555556661111"

    assert result == expected_result


def test_text_message_with_number_and_spaces():

    result = text_message_to_keys("Hello 123!")
    expected_result = "44335555556660" + "123" + "1111"

    assert result == expected_result


def test_text_message_with_special_characters():

    result = text_message_to_keys(".,?!:")
    expected_result = "1" + "11" + "111" + "1111" + "11111"

    assert result == expected_result


def test_text_message_empty_message():

    result = text_message_to_keys("")
    expected_result = ""

    assert result == expected_result


def test_raise_parameter_type_error():

    with pytest.raises(TypeError):
        text_message_to_keys(123)


if __name__ == "__main__":
    pytest.main()
