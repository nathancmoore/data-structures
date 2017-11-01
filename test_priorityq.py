"""This is the test file."""

import pytest


@pytest.fixture
def sample_priorityq():
    """Make a sample_priorityq for testing."""
    from priorityq import PriorityQ
    return PriorityQ()


def test_node_object_exists():
    """Test that the Node class definition is working."""
    from priorityq import Node
    node = Node(0, [1, 2])
    assert node


def test_priorityq_object_exists(sample_priorityq):
    """Test that the Node class definition is working."""
    assert sample_priorityq


def test_push_increases_size(sample_priorityq):
    """Test that the push method increases the size of the heap."""
    assert len(sample_priorityq.heap_list) == 0
    sample_priorityq.insert([5, 1])
    assert len(sample_priorityq.heap_list) == 1
    sample_priorityq.insert([6, 2])
    assert len(sample_priorityq.heap_list) == 2


def test_pop_decreases_size(sample_priorityq):
    """Test that the pop method decreases the size of the heap."""
    for i in range(5):
        sample_priorityq.insert([i, i + 3])
    sample_priorityq.pop()
    assert len(sample_priorityq.heap_list) == 4
    sample_priorityq.pop()
    assert len(sample_priorityq.heap_list) == 3
    sample_priorityq.pop()
    assert len(sample_priorityq.heap_list) == 2


def test_pop_always_returns_highest_priority(sample_priorityq):
    """Test that the pop method always returns the highest priority node's value."""
    sample_priorityq.insert(["value1", 5])
    sample_priorityq.insert(["value2", 10])
    sample_priorityq.insert(["value3", 7])
    sample_priorityq.insert(["value4", 0])
    assert sample_priorityq.pop() == "value2"


def test_peek_always_returns_highest_priority(sample_priorityq):
    """Test that the peek method always returns the highest priority node's value."""
    sample_priorityq.insert(["value1", 5])
    sample_priorityq.insert(["value2", 10])
    sample_priorityq.insert(["value3", 7])
    sample_priorityq.insert(["value4", 0])
    assert sample_priorityq.pop() == "value2"
