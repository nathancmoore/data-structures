"""Test the functionality of the Queue class."""


def test_empty_queue_is_length_zero():
    """Test length of empty queue."""
    from que_ import Queue
    q = Queue()
    assert q.__len__() == 0


def test_enqueue_one_node_return_length_is_one():
    """Test add one node to queue."""
    from que_ import Queue
    q = Queue()
    q.enqueue(1)
    assert q.__len__() == 1


def test_enqueu_length_is_len_of_range_of_random_nodes():
    """Test enqueue of sample space of randoms."""
    from que_ import Queue
    import random
    q = Queue()

    random_nodes = random.sample(range(1, 10), 9)
    test_len_size = len(random_nodes)

    for i in random_nodes:
        q.enqueue(1)

    assert q.__len__() == test_len_size


def test_deque_empty_queue_raises_error():
    """Test attempt to dequeue from empty queue."""
    import pytest
    from que_ import Queue
    q = Queue()
    with pytest.raises(IndexError):
        q.dequeue()


def test_dequeue_after_one_enqueue():
    """Test dequeue after enqueue."""
    from que_ import Queue
    q = Queue()
    q.enqueue(1)
    assert q.dequeue() is None


def test_dequeue_after_multiple_enqueue():
    """Test dequeue of range of enqueues."""
    from que_ import Queue
    q = Queue()
    test_nodes = [i for i in range(20)]
    for i in test_nodes:
        q.enqueue(i)

    q.dequeue()
    assert q.__len__() == len(test_nodes)


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
