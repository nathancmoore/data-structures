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
    """Ensure that the Node class and its arguments work and exist."""
    assert Node(None, 'a')
    assert Node(Node(None, 'a'))


def test_trie_exists():
    """Ensure that the Trie class exists."""
    t = Trie()
    assert t
    assert t.root
    assert t.trie_size == 0


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


def test_size_method(empty_trie):
    """Test that the size method returns the expected values."""
    assert empty_trie.size() == 0
    empty_trie.insert('a')
    assert empty_trie.size() == 1
    empty_trie.insert('bob')
    assert empty_trie.size() == 2
    empty_trie.remove('bob')
    assert empty_trie.size() == 1


def test_contains_method(short_trie, long_trie):
    """Test the contains method with short and long words."""
    assert short_trie.contains('pot')
    assert short_trie.contains('port')
    assert not short_trie.contains('house')
    assert long_trie.contains('communism')
    assert long_trie.contains('saddlemaker')
    assert not long_trie.contains('chocolateparty')


def test_insert_method_works(empty_trie, short_trie, long_trie):
    """Test that the insert method changes the size and works."""
    empty_trie.insert('house')
    assert empty_trie.size() == 1
    assert empty_trie.contains('house')
    short_trie.insert('house')
    assert short_trie.size() == 6
    assert short_trie.contains('house')
    long_trie.insert('house')
    assert long_trie.size() == 6
    assert long_trie.contains('house')


def test_remove_method_works(empty_trie, short_trie, long_trie):
    """Test that the remove method changes the size and works."""
    empty_trie.insert('house')
    empty_trie.remove('house')
    assert not empty_trie.contains('house')
    assert empty_trie.size() == 0
    short_trie.insert('house')
    short_trie.remove('house')
    assert not short_trie.contains('house')
    assert short_trie.size() == 5
    long_trie.insert('house')
    long_trie.remove('house')
    assert not long_trie.contains('house')
    assert long_trie.size() == 5


def test_remove_word_isnt_there(short_trie, long_trie):
    """Test that trying to remove a nonexistent word raises error."""
    with pytest.raises(KeyError):
        short_trie.remove('bung')
    with pytest.raises(KeyError):
        long_trie.remove('bung')
    with pytest.raises(KeyError):
        short_trie.remove('por')
    with pytest.raises(KeyError):
        long_trie.remove('antidis')
