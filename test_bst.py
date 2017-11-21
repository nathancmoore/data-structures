"""Various tests for the Binary Search Tree."""

import pytest


@pytest.fixture
def sample_bst():
    """Make a sample_bst for testing."""
    from bst import BST
    return BST()


def test_bst_exists(sample_bst):
    """Test that the BST class makes something."""
    assert sample_bst


def test_bst_can(sample_bst):
    """Test that the BST class makes something."""
    assert sample_bst


def test_insert_increases_size(sample_bst):
    """Test that the insert method increases the output of the size method."""
    assert sample_bst.size() == 0
    sample_bst.insert(1)
    assert sample_bst.size() == 1
    sample_bst.insert(2)
    assert sample_bst.size() == 2


def test_insert_increases_tree_size(sample_bst):
    """Test that the insert method increases the tree_size attribute."""
    assert sample_bst.tree_size == 0
    sample_bst.insert(1)
    assert sample_bst.tree_size == 1
    sample_bst.insert(2)
    assert sample_bst.tree_size == 2


def test_insert_increases_depth(sample_bst):
    """Test that the insert method increases the output of the depth method."""
    assert sample_bst.depth() == 0
    sample_bst.insert(1)
    assert sample_bst.depth() == 0
    sample_bst.insert(2)
    assert sample_bst.depth() == 1
