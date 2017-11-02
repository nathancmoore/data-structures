"""Various tests for Graph-class objects."""

import pytest


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


def test_del_node_removes_edges(sample_graph):
    """Test that the del_node method removes edges properly."""
    sample_graph.add_node("A")
    sample_graph.add_node("B")
    sample_graph.add_node("C")
    sample_graph.add_edge("A", "B")
    sample_graph.add_edge("A", "C")
    sample_graph.del_node("C")
    assert sample_graph.node_dict["A"] == ["B"]
    sample_graph.del_node("B")
    assert sample_graph.node_dict["A"] == []
