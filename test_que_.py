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
    assert sample_queue.peek() is None


def test_that_enqueue_needs_a_param(sample_queue):
    """Test that without a parameter, enqueue will raise a TypeError."""
    with pytest.raises(TypeError):
        sample_queue.enqueue()


def test_enqueue(sample_queue):
    """Test enqueue places things where they go."""
    sample_queue.enqueue(5)
    assert sample_queue.head.data == 5
    assert sample_queue.tail.data == 5
    sample_queue.enqueue(6)
    assert sample_queue.head.data == 5
    assert sample_queue.tail.data == 6
    assert sample_queue.head.prev_node.data == 6
    assert sample_queue.tail.next_node.data == 5
    sample_queue.enqueue(7)
    assert sample_queue.head.data == 5
    assert sample_queue.tail.data == 7
    assert sample_queue.head.prev_node.data == 6
    assert sample_queue.tail.next_node.data == 6


def test_dequeue(sample_queue):
    """Test that dequeue removes the correct node and returns properly."""
    sample_queue.enqueue(1)
    sample_queue.enqueue(2)
    sample_queue.enqueue(3)
    assert sample_queue.dequeue() == 1
    assert sample_queue.dequeue() == 2
    assert sample_queue.dequeue() == 3


def test_if_dequeue_needs_no_inputs(sample_queue):
    """Test that with dequeue, a parameter will raise an TypeError."""
    sample_queue.enqueue(5)
    with pytest.raises(TypeError):
        sample_queue.dequeue(5)


def test_dequeue_on_empty_list(sample_queue):
    """Test that dequeue'ing on an empty list will raise an IndexError."""
    with pytest.raises(IndexError):
        sample_queue.dequeue()


def test_output_of_peek_is_correct(sample_queue):
    """Test that the output of the peek method is correct."""
    sample_queue.enqueue(5)
    assert sample_queue.peek() == 5
    sample_queue.enqueue(6)
    assert sample_queue.peek() == 5
    sample_queue.dequeue()
    assert sample_queue.peek() == 6


def test_peek_on_empty_list(sample_queue):
    """Test that peeking an empty list returns None."""
    assert sample_queue.peek() is None


def test_if_peek_needs_no_inputs(sample_queue):
    """Test that with peek, an unnecessary parameter will raise a TypeError."""
    sample_queue.enqueue(5)
    with pytest.raises(TypeError):
        sample_queue.peek(5)


def test_queue_len_method_is_working(sample_queue):
    """Test that the redefined len method works."""
    assert len(sample_queue) == 0
    sample_queue.enqueue(1)
    assert len(sample_queue) == 1
    sample_queue.enqueue(2)
    assert len(sample_queue) == 2
    sample_queue.dequeue()
    assert len(sample_queue) == 1
    sample_queue.dequeue()
    assert len(sample_queue) == 0


def test_queue_size_method_is_working(sample_queue):
    """Test that the size method works."""
    assert sample_queue.size() == 0
    sample_queue.enqueue(1)
    assert sample_queue.size() == 1
    sample_queue.enqueue(2)
    assert sample_queue.size() == 2
    sample_queue.dequeue()
    assert sample_queue.size() == 1
    sample_queue.dequeue()
    assert sample_queue.size() == 0
