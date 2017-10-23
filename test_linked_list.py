"""These are tests for linked_list.py."""

import pytest


def test_get_data_method():
    """Test that the get_data method returns something."""
    from linked_list import Node
    node = Node(1, 2)
    assert node.get_data() is not None


def test_node_object_exists():
    """Test that the Node class definition is working."""
    from linked_list import Node
    node = Node(0, 1)
    assert node


def test_set_data_method():
    """Test that the set_data method works and returns something."""
    from linked_list import Node
    node = Node(1, 2)
    assert node.set_data(6) is not None
    assert node.data == 6
