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
        self.trie_size = 0
        self.visited = []

    def size(self):
        """Return the number of words in the Trie."""
        return self.trie_size

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

        self.trie_size += 1

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
            self.trie_size -= 1
            del current.children['$']

            current = current.parent
            while len(current.children) == 1:
                current.children.clear()
                if current.parent:
                    current = current.parent

        else:
            raise KeyError('Word is not in the Trie!')

    def traversal(self, start='*'):
        """Perform a depth-first traversal of the Trie."""
        self.visited = []

        if not self.root:
            return None

        self.visited.append(self.root.val)

        for child in self.root.children.keys():
            if child not in self.visited:
                self._traversal_helper(self.root.children[child])

        gen = self._traversal_gen(start)

        return gen

    def _traversal_helper(self, start_node):
        """Recursive helper method for traversal method."""
        print(self.visited)
        for child in start_node.children.keys():
            if child not in self.visited:
                self._traversal_helper(start_node.children[child])

        self.visited.insert(0, start_node.val)

    def _traversal_gen(self, start):
        """Generator for the traversal method."""
        while self.visited[0] != start:
            self.visited.pop(0)

        while True:
            yield self.visited.pop(0)
