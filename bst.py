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

    def __init__(self, starting_values=None):
        """Constructor for the BST class."""
        self.balance = 0
        self.size = 0

        if starting_values is None:
            self.root = None

        elif isinstance(starting_values, (list, str, tuple, set)):
            self.root = starting_values[0]
            self.size += 1
            for i in len(starting_values) - 1:
                self.insert(starting_values[i + 1])

        else:
            raise TypeError('Only iterables or None\
                are valid parameters!')

    def balance(self):
        """Return the current balance of the BST."""
        return self.balance

    def size(self):
        """Return the current size of the BST."""
        return self.size

    def insert(self, value):
        """Insert a new node into the BST, and adjust the balance."""
        new_node = Node(value)

        if self.root:
            if new_node > self.root:
                self.balance += 1
                if self.root.right:
                    self._find_home(new_node, self.root.right)
                else:
                    self.root.right = new_node
                    self.size += 1

            elif new_node < self.root:
                self.balance -= 1
                if self.root.left:
                    self._find_home(new_node, self.root.left)
                else:
                    self.root.left = new_node
                    self.size += 1

        else:
            self.root = new_node

    def _find_home(self, node_to_add, node_to_check):
        r""".

        Check if the node_to_add belongs on the left or right\
         of the node_to_check, then place it there if that spot is empty,\
          otherwise recur.
        """
        if node_to_add > node_to_check:
            if node_to_check.right:
                self._find_home(node_to_add, node_to_check.right)
            else:
                node_to_check.right = node_to_add
                self.size += 1

        elif node_to_add < node_to_check:
            if node_to_check.left:
                self._find_home(node_to_add, node_to_check.left)
            else:
                node_to_check.left = node_to_add
                self.size += 1

    def search(self, value):
        """Return whether or not a value is in the BST."""
        return self._check_for_equivalence(value, self.root)

    def _check_for_equivalence(self, value, node_to_check):
        r""".

        Check if the value matches that of the node_to_check\
         if it does, return true if it doesn't, go left or right
         as appropriate and recur. If you reach a dead end, return false.\
        """
        if value > node_to_check:
            if node_to_check.right:
                self._check_for_equivalence(value, node_to_check.right)
            else:
                node_to_check.right = value

        elif value < node_to_check:
            if node_to_check.left:
                self._check_for_equivalence(value, node_to_check.left)
            else:
                node_to_check.left = value
