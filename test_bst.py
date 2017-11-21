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


def test_bst_can_take_list():
    """Test that the BST can take a list as a param."""
    from bst import BST
    b = BST([1, 2, 3])
    assert b.size() == 3
    assert b.depth() == 2
    assert b.left_depth == 0
    assert b.right_depth == 2


def test_bst_can_take_tuple():
    """Test that the BST can take a tuple as a param."""
    from bst import BST
    b = BST((1, 2, 3))
    assert b.size() == 3
    assert b.depth() == 2
    assert b.left_depth == 0
    assert b.right_depth == 2


def test_bst_can_take_string():
    """Test that the BST can take a string as a param."""
    from bst import BST
    b = BST('abc')
    assert b.size() == 3
    assert b.depth() == 2
    assert b.left_depth == 0
    assert b.right_depth == 2


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


def test_search_right(sample_bst):
    """Assert that the search method returns something and that it's a Node."""
    from bst import Node
    sample_bst.insert(1)
    sample_bst.insert(2)
    sample_bst.insert(3)
    found = sample_bst.search(3)
    assert found.val == 3
    assert isinstance(found, Node)


def test_search_left(sample_bst):
    """Assert that the search method returns something and that it's a Node."""
    from bst import Node
    sample_bst.insert(3)
    sample_bst.insert(2)
    sample_bst.insert(1)
    found = sample_bst.search(3)
    assert found.val == 3
    assert isinstance(found, Node)


def test_search_not_found_returns_none(sample_bst):
    """Assert that the search method returns None when value isn't found."""
    sample_bst.insert(1)
    sample_bst.insert(2)
    sample_bst.insert(3)
    found = sample_bst.search(4)
    assert found is None


def test_contains_right(sample_bst):
    """Assert that the contains method returns True."""
    sample_bst.insert(1)
    sample_bst.insert(2)
    sample_bst.insert(3)
    found = sample_bst.contains(3)
    assert found is True


def test_contains_left(sample_bst):
    """Assert that the contains method returns True."""
    sample_bst.insert(3)
    sample_bst.insert(2)
    sample_bst.insert(1)
    found = sample_bst.contains(3)
    assert found is True


def test_contains_not_found_returns_none(sample_bst):
    """Assert that the contains method returns False when value isn't found."""
    sample_bst.insert(1)
    sample_bst.insert(2)
    sample_bst.insert(3)
    found = sample_bst.contains(4)
    assert found is False
