"""Various tests for the Deque-class object."""


def test_node_object_exists():
    """Test that the Node class definition is working."""
    from deque import Node
    node = Node(3)
    assert node


def test_append_into_empty():
    """Test that appending into an empty list assigns the node to both head and tail."""
    from deque import QLinkedList
    d = QLinkedList()
    d.append(5)
    assert d.head == d.tail
    assert d.head and d.tail


def test_appendleft_into_empty():
    """Test that appendleft-ing into an empty list assigns the node to both head and tail."""
    from deque import QLinkedList
    d = QLinkedList()
    d.appendleft(5)
    assert d.head == d.tail
    assert d.head and d.tail


def test_size_when_appending():
    """Test that size works when appending."""
    from deque import QLinkedList
    d = QLinkedList()
    assert d.size() == 0
    d.append(1)
    assert d.size() == 1
    d.append(2)
    assert d.size() == 2


def test_size_when_appendlefting():
    """Test that size works when appendleft-ing."""
    from deque import QLinkedList
    d = QLinkedList()
    assert d.size() == 0
    d.appendleft(1)
    assert d.size() == 1
    d.appendleft(2)
    assert d.size() == 2


def test_pop_on_empty():
    """Test that popping an empty list returns none."""
    from deque import QLinkedList
    import pytest
    d = QLinkedList()
    with pytest.raises(IndexError):
        d.pop()


def test_popleft_on_empty():
    """Test that popleft-ing an empty list returns none."""
    from deque import QLinkedList
    import pytest
    d = QLinkedList()
    with pytest.raises(IndexError):
        d.popleft()


def test_peek_returns_after_pop():
    """Test that peek returns correct value after a pop."""
    from deque import QLinkedList
    d = QLinkedList()
    d.append(5)
    d.append(6)
    d.append(7)
    d.pop()
    assert d.peek().data == 6


def test_peek_returns_after_append():
    """Test that peek works with append method."""
    from deque import QLinkedList
    d = QLinkedList()
    d.append(5)
    d.append(6)
    d.append(7)
    assert d.peek().data == 7


def test_peek_returns_after_popleft():
    """Test that peek returns correct value after a popleft."""
    from deque import QLinkedList
    d = QLinkedList()
    d.append(5)
    d.append(6)
    d.append(7)
    d.popleft()
    assert d.peek().data == 7


def test_peek_returns_after_appendleft():
    """Test that peek returns after appendleft."""
    from deque import QLinkedList
    d = QLinkedList()
    d.appendleft(5)
    d.appendleft(6)
    d.appendleft(7)
    assert d.peek().data == 5


def test_peekleft_returns_after_pop():
    """Test peekleft returns after pop."""
    from deque import QLinkedList
    d = QLinkedList()
    d.appendleft(5)
    d.appendleft(6)
    d.appendleft(7)
    d.pop()
    assert d.peekleft().data == 7


def test_peekleft_returns_after_append():
    """Test peekleft works after an append."""
    from deque import QLinkedList
    d = QLinkedList()
    d.append(5)
    d.append(6)
    d.append(7)
    assert d.peekleft().data == 5

def test_peek_returns_none_on_empty_list():
    """Test peek with empty list."""
    from deque import QLinkedList
    d = QLinkedList()
    assert d.peek() is None


def test_peek_returns_none_on_empty_list():
    """Test peekleft with empty list."""
    from deque import QLinkedList
    d = QLinkedList()
    assert d.peekleft() is None
