def test_node_object_exists():
    """Test that the Node class definition is working."""
    from doubly_linked_list import Node
    node = Node(0, 1, 3)
    assert node