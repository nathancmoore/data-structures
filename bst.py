"""Implementation of a binary search tree data structure."""


class Node(object):
    """Define the Node-class object."""

    def __init__(self, value, left=None, right=None):
        """Constructor for the Node class."""
        self.val = value
        self.left = left
        self.right = right


class BST(object):
    """Define the BST-class object."""

    def __init__(self):
        """Constructor for the BST class."""
        self.balance = 0
        self.size = 0

    def balance(self):
        """Return the current balance of the BST."""
        return self.balance

    