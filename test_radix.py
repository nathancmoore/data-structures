"""Various tests for radix_sort."""

from radix import radix_sort
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
    assert type(radix_sort([3, 2, 1])) == list


def test_wrong_input_type():
    """Test that only lists are valid inputs."""
    with pytest.raises(TypeError):
        radix_sort("abcde")
    with pytest.raises(TypeError):
        radix_sort(12345)
    with pytest.raises(TypeError):
        radix_sort(123.45)
    with pytest.raises(TypeError):
        radix_sort({1, 2, 3})
    with pytest.raises(TypeError):
        radix_sort(("abcde", 12345))
    with pytest.raises(TypeError):
        radix_sort({"abc": 123})


def test_correct_output():
    """Test that radix_sort sorts correctly."""
    for x in TEST_CASES:
        assert radix_sort(x) == sorted(x)


def test_many_times():
    """Test lots of big-numbered lists."""
    for i in range(20):
        test = [randint(1, 1000000) for i in range(50)]
        assert radix_sort(test[:]) == sorted(test[:])
