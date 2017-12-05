"""Test the functionality of the Queue class."""

import pytest


@pytest.fixture
def sample_queue():
    """Create a sample_queue fixture for testing."""
    from que_ import Queue
    return Queue()


def test_queue_exists(sample_queue):
    """Test that a Queue object is created correctly."""
    assert sample_queue is not None
    assert sample_queue.head is None
    assert sample_queue.tail is None
    assert sample_queue.size() == 0


def test_head_tail_of_list_of_len_1(sample_queue):
    """Test that in a one-node list, the node is head and tail."""
    sample_queue.enqueue(5)
    assert sample_queue.head
    assert sample_queue.tail


def test_output_of_peek_is_correct(sample_queue):
    """Test that the output is correct."""
    sample_queue.enqueue(5)
    assert sample_queue.peek() == 5
    sample_queue.enqueue(6)
    assert sample_queue.peek() == 5
    sample_queue.dequeue()
    assert sample_queue.peek() == 6


def test_if_peek_needs_no_inputs(sample_queue):
    """Test that an unnecessary parameter will raise a TypeError."""
    import pytest
    sample_queue.enqueue(5)
    with pytest.raises(TypeError):
        sample_queue.peek(5)


def test_queue_len_method_is_working(sample_queue):
    """Test that the len method works."""
    assert len(sample_queue) == 0
    sample_queue.enqueue(1)
    assert len(sample_queue) == 1
    sample_queue.enqueue(2)
    assert len(sample_queue) == 2
    sample_queue.dequeue()
    assert len(sample_queue) == 1
    sample_queue.dequeue()
    assert len(sample_queue) == 0
