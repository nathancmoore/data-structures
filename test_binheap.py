"""Various tests for binheap.py."""

import pytest


@pytest.fixture
def sample_heap():
    """A fixture for a sample heap to use."""
    from binheap import BinHeap
    return BinHeap()


def test_node_object_exists():
    """Test that the Node class definition is working."""
    from binheap import Node
    node = Node(0, 1)
    assert node


def test_binheap_object_exists(sample_heap):
    """Test that the Node class definition is working."""
    assert sample_heap


def test_push_increases_size(sample_heap):
    """Test that the push method increases the size of the heap."""
    assert len(sample_heap.heap_list) == 0
    sample_heap.push(5)
    assert len(sample_heap.heap_list) == 1
    sample_heap.push(6)
    assert len(sample_heap.heap_list) == 2


def test_pop_decreases_size(sample_heap):
    """Test that the pop method decreases the size of the heap."""
    for i in range(5):
        sample_heap.push(i)
    sample_heap.pop()
    assert len(sample_heap.heap_list) == 4
    sample_heap.pop()
    assert len(sample_heap.heap_list) == 3
    sample_heap.pop()
    assert len(sample_heap.heap_list) == 2


def test_pop_always_returns_highest_value(sample_heap):
    """Test that the pop method always returns the highest val in the heap."""
