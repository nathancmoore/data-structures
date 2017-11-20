"""Implementation of a binary search tree data structure."""


class Node(object):
    """Define the Node-class object."""

    def __init__(self, value, left=None, right=None):
        """Constructor for the Node class."""
        self.val = value
        self.left = left
        self.right = right

    def __repr__(self):
        """Show each node as its value."""
        return self.val


class BST(object):
    """Define the BST-class object."""

    def __init__(self):
        """Constructor for the BST class."""
        self.balance = 0
        self.size = 0
        self.root = None

    def balance(self):
        """Return the current balance of the BST."""
        return self.balance

    def insert(self, value):
        """Insert a new node into the BST."""
        new_node = Node(value)

        if self.root:
            self._find_spot(new_node, self.root)

    def _find_spot(self, node_to_add, node_to_check):
        r""".

        Check if the node_to_add belongs on the left or right\
         of the node_to_check, then place it there if that spot is empty,\
          otherwise recur.
        """
        if node_to_add > node_to_check:
            if node_to_check.right:
                self._find_spot(node_to_add, node_to_check.right)
            node_to_check.right = node_to_add

        elif node_to_add < node_to_check:
            if node_to_check.left:
                self._find_spot(node_to_add, node_to_check.left)
            node_to_check.left = node_to_add
