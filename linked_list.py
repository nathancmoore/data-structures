"""This is the docstring."""


class Node(object):
    """Define Node-class objects."""

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
        return self.data

    def set_next(self, next):
        """Define what the next node is."""
        self.next = next
        return self.next

    def get_next(self, next):
        """Return what the next node is."""
        return self.next


class LinkedList(object):
    """Define LinkedList-class objects."""

    def __init__(self):
        """Initiate a new instance of a LinkedList object with attributes."""
        self.head = ""

    def size(self):
        """Define the size method of the LinkedList-class object."""
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.get_next()
        return count

    def push(self, val):
        """Define the push method for LinkedList-class object."""

