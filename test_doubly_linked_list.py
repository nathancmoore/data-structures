def test_node_object_exists():
    """Test that the Node class definition is working."""
    from doubly_linked_list import Node
    node = Node(0, 1, 3)
    assert node


def test_search_found():
    """Test that push value to list then search for it."""
    from doubly_linked_list import DLinkedList
    test_dlinked_list = DLinkedList()
    test_dlinked_list.push(20)
    assert test_dlinked_list.search(20)


def test_search_not_found():
    """Test that will search for value not in list."""
    from doubly_linked_list import DLinkedList
    test_dlinked_list = DLinkedList()
    test_dlinked_list.push(5)
    test_dlinked_list.push(7)
    test_dlinked_list.push(10)
    assert test_dlinked_list.search(11) is None

def test_search_for_appended_found():
    from doubly_linked_list import DLinkedList
    test_dlinked_list = DLinkedList()
    test_dlinked_list.append(20)
    assert test_dlinked_list.search(20)

def test_search_for_appended_not_found():
    from doubly_linked_list import DLinkedList
    test_dlinked_list = DLinkedList()
    test_dlinked_list.append(5)
    test_dlinked_list.append(7)
    test_dlinked_list.append(10)
    assert test_dlinked_list.search(11) is None

def test_search_for_remove_head():
    import pytest
    from doubly_linked_list import DLinkedList
    test_dlinked_list = DLinkedList()
    test_dlinked_list.push(5)
    test_dlinked_list.push(7)
    test_dlinked_list.push(10)
    test_dlinked_list.remove(5)
    assert test_dlinked_list.size() == 2

def test_search_for_remove_tail():
    import pytest
    from doubly_linked_list import DLinkedList
    test_dlinked_list = DLinkedList()
    test_dlinked_list.push(5)
    test_dlinked_list.push(7)
    test_dlinked_list.push(10)
    test_dlinked_list.remove(10)
    assert test_dlinked_list.size() == 2

def test_search_for_remove_middle():
    import pytest
    from doubly_linked_list import DLinkedList
    test_dlinked_list = DLinkedList()
    test_dlinked_list.push(5)
    test_dlinked_list.push(7)
    test_dlinked_list.push(10)
    test_dlinked_list.remove(7)
    assert test_dlinked_list.size() == 2