"""These are tests for linked_list.py."""

import pytest


# def test_get_data_method():
#     """Test that the get_data method returns something."""
#     from linked_list import Node
#     node = Node(1, 2)
#     node.set_data(1)
#     assert node.get_data() == 1


# def test_get_next_method():
#     """Test that the get_data method returns something."""
#     from linked_list import Node
#     node = Node(1, 2)
#     node.set_next(2)
#     assert node.get_next(1) == 2


def test_node_object_exists():
    """Test that the Node class definition is working."""
    from linked_list import Node
    node = Node(0, 1)
    assert node


def test_search_found():
    """Test that push value to list then search for it."""
    from linked_list import LinkedList
    test_linked_list = LinkedList()
    test_linked_list.push(20)
    assert test_linked_list.search(20)


def test_search_not_found():
    """Test that will search for value not in list."""
    from linked_list import LinkedList
    test_linked_list = LinkedList()
    test_linked_list.push(5)
    test_linked_list.push(7)
    test_linked_list.push(10)
    assert test_linked_list.search(11) is None


def test_pop_empty():
    """Ensure that the pop method raises an error on an empty list."""
    from linked_list import LinkedList
    test_linked_list = LinkedList()
    with pytest.raises(IndexError):
        test_linked_list.pop()


def test_pop_full():
    """Ensure that pop works."""
    from linked_list import LinkedList
    test_linked_list = LinkedList()
    test_linked_list.push(3)
    test_linked_list.push(5)
    test_linked_list.push(7)
    assert test_linked_list.pop() == 7
    assert test_linked_list.size() == 2
