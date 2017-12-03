"""Definition of the Trie and Node classes."""


class Node(object):
    """Definition of the Node class."""

    def __init__(self, val='$')
    self.val = val
    self.children = {}


class Trie(object):
    """Definition of the Trie class."""

    def __init__(self):
        """Constructor for the Trie class."""
        self.root = Node('*')
        self.size = 0

    def size(self):
        """Return the number of words in the Trie."""
        return self.size

    def contains(self, word):
        """Return True if a word is in the Trie, False if not."""
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]

        if '$' in current.children:
            return True

        return False
