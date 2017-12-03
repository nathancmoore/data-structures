"""Various tests for my Trie."""

import pytest
from trie import Trie, Node


@pytest.fixture
def sample_trie():
    """Fixture empty Trie for testing."""
    return Trie()


def test_node_exists():
    """Ensure that the Node class exists."""
    assert Node(None)


def test_trie_exists():
    """Ensure that the Trie class exists."""
    assert Trie()


def test_insert_only_takes_str():
    """Test that non-string inputs result in a TypeError."""
    with pytest.raises(TypeError):

