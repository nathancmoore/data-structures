"""Various tests for my Trie."""

import pytest
from trie import Trie, Node


@pytest.fixture
def empty_trie():
    """Fixture empty Trie for testing."""
    return Trie()


@pytest.fixture
def short_trie():
    """Fixture Trie with short words for testing."""
    trie = Trie()
    trie.insert('pot')
    trie.insert('jab')
    trie.insert('raft')
    trie.insert('port')
    trie.insert('job')
    return trie


@pytest.fixture
def long_trie():
    """Fixture Trie with long words for testing."""
    trie = Trie()
    trie.insert('potassium')
    trie.insert('communism')
    trie.insert('community')
    trie.insert('saddlemaker')
    trie.insert('antidisestablishmentarianism')
    return trie


def test_node_exists():
    """Ensure that the Node class exists."""
    assert Node(None)


def test_trie_exists():
    """Ensure that the Trie class exists."""
    assert Trie()


def test_insert_only_takes_str(empty_trie):
    """Test that non-string inputs result in a TypeError."""
    with pytest.raises(TypeError):
        empty_trie.insert(6)
    with pytest.raises(TypeError):
        empty_trie.insert(['a', 'b', 'c'])
    with pytest.raises(TypeError):
        empty_trie.insert(3.14159265)
    with pytest.raises(TypeError):
        empty_trie.insert({'party': 'time'})
