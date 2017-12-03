"""Definition of the Trie and Node classes."""


class Node(object):
    """Definition of the Node class."""

    def __init__(self, parent, val='$'):
        """Constructor for the Node class."""
        self.parent = parent
        self.val = val
        self.children = {}


class Trie(object):
    """Definition of the Trie class."""

    def __init__(self):
        """Constructor for the Trie class."""
        self.root = Node(None, '*')
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

    def insert(self, word):
        """Insert a word into the Trie."""
        if type(word) is not str:
            raise TypeError('Only strings are valid inputs!')

        self.size += 1

        current = self.root
        for char in word:
            current.children.setdefault(char, Node(current, char))
            current = current.children[char]

        current.children.setdefault('$', Node(current))

    def remove(self, word):
        """Remove a word from the Trie, if it's not in there, raise error."""
        current = self.root
        for char in word:
            if char not in current.children:
                raise KeyError('Word is not in the Trie!')
            current = current.children[char]

        if '$' in current.children:
            self.size -= 1
            del current.children['$']

            current = current.parent
            while len(current.children) == 1:
                current.children.clear()
                current = current.parent

        else:
            raise KeyError('Word is not in the Trie!')
