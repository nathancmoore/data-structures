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
    d = QLinkedList()
    assert d.pop() is None


def test_popleft_on_empty():
    """Test that popleft-ing an empty list returns none."""
    from deque import QLinkedList
    d = QLinkedList()
    assert d.popleft() is None
