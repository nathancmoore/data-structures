"""Test the functionality of the Queue class."""


def test_queue_exists():
    """Test that a Queue object is created."""
    from que_ import Queue
    q = Queue()
    assert q


def test_head_tail_of_list_of_len_1():
    """Test that in a one-node list, the node is head and tail."""
    from que_ import Queue
    q = Queue()
    q.enqueue(5)
    assert q.linked_list.head
    assert q.linked_list.tail


def test_output_of_peek_exists():
    """Test that the output exists."""
    from que_ import Queue
    q = Queue()
    q.enqueue(5)
    assert q.peek() is not None


def test_if_peek_needs_no_inputs():
    """Test that an unnecessary parameter will raise a TypeError."""
    import pytest
    from que_ import Queue
    q = Queue()
    q.enqueue(5)
    with pytest.raises(TypeError):
        q.peek(5)
