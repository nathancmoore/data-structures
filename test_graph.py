"""Various tests for Graph-class objects."""

import pytest

s1 = {
    'B': ['C', 'D'],
    'C': ['X', 'Y', 'Z'],
    'D': ['K', 'N'],
    'N': ['A'],
    'X': [],
    'Y': [],
    'Z': [],
    'K': [],
    'A': []
}

s2 = {
    'B': ['C', 'D'],
    'C': ['X', 'Y', 'Z'],
    'D': ['K', 'N'],
    'N': ['A'],
    'X': ['Y'],
    'Y': ['A'],
    'Z': [],
    'K': [],
    'A': ['K']
}


@pytest.fixture
def sample_graph():
    """Make a sample graph for testing."""
    from graph import Graph
    return Graph()


def test_graph_object_exists(sample_graph):
    """Test that the Graph class definition is working."""
    assert sample_graph


def test_add_node_increases_size(sample_graph):
    """Test that the add_node method increases size of the dict."""
    sample_graph.add_node("A")
    assert len(sample_graph.node_dict) == 1
    sample_graph.add_node("B")
    assert len(sample_graph.node_dict) == 2


def test_add_node_makes_proper_node(sample_graph):
    """Test that added nodes are properly-formed."""
    sample_graph.add_node("A")
    assert sample_graph.node_dict["A"] == []


def test_add_edge_is_working(sample_graph):
    """Test that the add_edge method isn't doing nothing."""
    sample_graph.add_node("A")
    sample_graph.add_node("B")
    sample_graph.add_edge("A", "B")
    assert sample_graph.node_dict["A"] == ["B"]
    sample_graph.add_node("C")
    sample_graph.add_edge("A", "C")
    assert sample_graph.node_dict["A"] == ["B", "C"]


def test_del_node_reduces_dict_size(sample_graph):
    """Test that the del_node method decreases the size of the graph."""
    sample_graph.add_node("A")
    sample_graph.add_node("B")
    sample_graph.add_node("C")
    sample_graph.del_node("C")
    assert len(sample_graph.node_dict) == 2
    sample_graph.del_node("B")
    assert len(sample_graph.node_dict) == 1


def test_has_node(sample_graph):
    """Test that has_node method is working."""
    assert not sample_graph.has_node("A")
    sample_graph.add_node("A")
    assert sample_graph.has_node("A")


def test_has_neighbors_true(sample_graph):
    """Test that graph node has neighbors."""
    sample_graph.add_node("A")
    sample_graph.add_node("B")
    sample_graph.add_node("C")
    sample_graph.add_edge("A", "B")
    sample_graph.add_edge("A", "C")
    assert sample_graph.has_neighbors("A") == ['B', 'C']


def test_has_no_neighbors_false(sample_graph):
    """Test that graph node has no neighbors."""
    sample_graph.add_node("A")
    sample_graph.add_node("B")
    sample_graph.add_node("C")
    sample_graph.add_edge("A", "B")
    assert sample_graph.has_neighbors("C") == []


def test_has_neighbors_returns_error(sample_graph):
    """Test that graph node has neighbors returns Error when node does not exist."""
    sample_graph.add_node("A")
    sample_graph.add_node("C")
    sample_graph.add_edge("A", "C")
    with pytest.raises(KeyError):
        sample_graph.has_neighbors("B")


def test_adjacent_returns_true_multiple_edges(sample_graph):
    """Test if multiple edges between nodes exist."""
    sample_graph.add_node("A")
    sample_graph.add_node("B")
    sample_graph.add_edge("A", "B")
    sample_graph.add_edge("B", "A")
    assert sample_graph.has_adjacent("A", "B")


def test_adjacent_returns_true_one_edge(sample_graph):
    """Test if one edge exists."""
    sample_graph.add_node("A")
    sample_graph.add_node("B")
    sample_graph.add_edge("A", "B")
    assert sample_graph.has_adjacent("A", "B")


def test_has_adjacent_no_edges_returns_false(sample_graph):
    """Test if nodes without edges returns false."""
    sample_graph.add_node("A")
    sample_graph.add_node("B")
    assert sample_graph.has_adjacent("A", "B") is False


def test_has_adjacent_multi_edges_returns_false(sample_graph):
    """Test if no nodes are has_adjacent if other edges exist."""
    sample_graph.add_node("A")
    sample_graph.add_node("C")
    sample_graph.add_node("B")
    sample_graph.add_edge("A", "C")
    sample_graph.add_edge("A", "B")
    assert sample_graph.has_adjacent("B", "C") is False


def test_if_node_has_adjacent_to_itself(sample_graph):
    """Test node should not be has_adjacent to itself."""
    sample_graph.add_node("A")
    assert sample_graph.has_adjacent("A", "A") is False


def test_dfs_one_node(sample_graph):
    """Test one node search on dfs."""
    sample_graph.add_node("A")
    assert sample_graph.depth_first_traversal("A") == ["A"]


def test_dfs_sample_graph_with_loops():
    """Test dfs on a graph with loops."""
    from graph import Graph
    sg = Graph(s2)
    assert sg.depth_first_traversal('B') == ['B', 'C', 'X', 'Y', 'A', 'K', 'Z', 'D', 'N']


def test_dfs_sample_graph_no_loops():
    """Test dfs on a graph without loops."""
    from graph import Graph
    sg = Graph(s1)
    assert sg.depth_first_traversal('B') == ['B', 'C', 'X', 'Y', 'Z', 'D', 'K', 'N', 'A']


def test_bfs_one_node(sample_graph):
    """Test one node search on bfs."""
    sample_graph.add_node("A")
    assert sample_graph.breadth_first_traversal("A") == ["A"]


def test_bfs_sample_graph_with_loops():
    """Test bfs on a graph with loops."""
    from graph import Graph
    sg = Graph(s2)
    assert sg.breadth_first_traversal('B') == ['B', 'C', 'D', 'X', 'Y', 'Z', 'K', 'N', 'A']


def test_bfs_sample_graph_no_loops():
    """Test bfs on a graph without loops."""
    from graph import Graph
    sg = Graph(s1)
    assert sg.breadth_first_traversal('B') == ['B', 'C', 'D', 'X', 'Y', 'Z', 'K', 'N', 'A']
