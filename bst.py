"""Implementation of a binary search tree data structure."""


class Node(object):
    """Define the Node-class object."""

    def __init__(self, value, left=None, right=None):
        """Constructor for the Node class."""
        self.val = value
        self.left = left
        self.right = right
        self.depth = 0


class BST(object):
    """Define the BST-class object."""

    def __init__(self, starting_values=None):
        """Constructor for the BST class."""
        self.tree_size = 0
        self.left_depth = 0
        self.right_depth = 0

        if starting_values is None:
            self.root = None

        elif isinstance(starting_values, (list, str, tuple)):
            self.root = Node(starting_values[0])
            self.tree_size += 1
            for i in range(len(starting_values) - 1):
                self.insert(starting_values[i + 1])

        else:
            raise TypeError('Only iterables or None\
                are valid parameters!')

    def balance(self):
        """Return the current balance of the BST."""
        return self.right_depth - self.left_depth

    def size(self):
        """Return the current size of the BST."""
        return self.tree_size

    def insert(self, value):
        """Insert a new node into the BST, and adjust the balance."""
        new_node = Node(value)

        if self.root:
            if new_node.val > self.root.val:
                if self.root.right:
                    self._find_home(new_node, self.root.right)
                    if new_node.depth > self.right_depth:
                        self.right_depth = new_node.depth
                else:
                    self.root.right = new_node
                    self.root.right.depth = 1
                    if self.root.right.depth > self.right_depth:
                        self.right_depth = self.root.right.depth
                    self.tree_size += 1

            elif new_node.val < self.root.val:
                if self.root.left:
                    self._find_home(new_node, self.root.left)
                    if new_node.depth > self.left_depth:
                        self.left_depth = new_node.depth
                else:
                    self.root.left = new_node
                    self.root.left.depth = 1
                    if self.root.left.depth > self.left_depth:
                        self.left_depth = self.root.left.depth
                    self.tree_size += 1
        else:
            self.root = new_node
            self.tree_size += 1

    def _find_home(self, node_to_add, node_to_check):
        """.

        Check if the node_to_add belongs on the left or right
         of the node_to_check, then place it there if that spot is empty,
          otherwise recur.
        """
        if node_to_add.val > node_to_check.val:
            if node_to_check.right:
                self._find_home(node_to_add, node_to_check.right)
            else:
                node_to_check.right = node_to_add
                node_to_check.right.depth = node_to_check.depth + 1
                self.tree_size += 1

        elif node_to_add.val < node_to_check.val:
            if node_to_check.left:
                self._find_home(node_to_add, node_to_check.left)
            else:
                node_to_check.left = node_to_add
                node_to_check.left.depth = node_to_check.depth + 1
                self.tree_size += 1

    def search(self, value):
        """If a value is in the BST, return its node."""
        return self._check_for_equivalence(value, self.root)

    def contains(self, value):
        """Return whether or not a value is in the BST."""
        return bool(self.search(value))

    def _check_for_equivalence(self, value, node_to_check):
        """.

        Check if the value matches that of the node_to_check
         if it does, return the node. If it doesn't, go left or right
         as appropriate and recur. If you reach a dead end, return None.
        """
        try:
            if value == node_to_check.val:
                return node_to_check

        except AttributeError:
            return None

        if value > node_to_check.val and node_to_check.right:
            return self._check_for_equivalence(value, node_to_check.right)

        elif value < node_to_check.val and node_to_check.left:
            return self._check_for_equivalence(value, node_to_check.left)

    def depth(self):
        """Return the depth of the BST."""
        if self.left_depth > self.right_depth:
            return self.left_depth
        return self.right_depth
