"""These are tests for linked_list.py."""

import pytest


def test_get_data_method():
    """Test that the get_data method returns something."""
    from linked_list import Node
    node = Node(1, 2)
    assert node.get_data() is not None
