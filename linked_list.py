"""This is the docstring."""


class Node(object):
    """Define Node objects."""

    def __init__(self, data, next):
        """Initiate a new instance of a Node object with attributes."""
        self.data = data
        self.next = next

    def get_data(self):
        """Write something here."""
        return self.data

    def set_data(self, data):
        """Write something here."""
        self.data = data
