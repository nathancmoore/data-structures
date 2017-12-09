"""Various tests for insertion_sort."""

from insertion import insertion_sort
from random import randint
import pytest

TEST_CASES = (
    [1, 2, 3, 4, 5, 6],
    [6, 5, 4, 3, 2, 1],
    [],
    [5],
    [randint(1, 1000) for i in range(50)]
)


def test_output_type():
    """Test that the output type is a list."""
    assert type(insertion_sort([3, 2, 1])) == list


def test_wrong_input_type():
    """Test that only lists are valid inputs."""
    with pytest.raises(TypeError):
        insertion_sort("abcde")
    with pytest.raises(TypeError):
        insertion_sort(12345)
    with pytest.raises(TypeError):
        insertion_sort(123.45)
    with pytest.raises(TypeError):
        insertion_sort({1, 2, 3})
    with pytest.raises(TypeError):
        insertion_sort(("abcde", 12345))
    with pytest.raises(TypeError):
        insertion_sort({"abc": 123})


def test_correct_output():
    """Test that insertion_sort sorts correctly."""
    for x in TEST_CASES:
        assert insertion_sort(x) == sorted(x)
