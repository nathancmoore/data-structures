"""Define the Stack class."""
from linked_list import Node
from linked_list import LinkedList

class Stack(LinkedList):
    """Define Stack-class objects."""

    def __init__(self):
        """Initiate a new instance of a LinkedList object with attributes."""
        self.linked_list = LinkedList()

    def size(self):
        """Define the size method."""
        return self.linked_list.size()

    def push(self, val):
        """Define the size method."""
        return self.linked_list.push(val)

    def pop(self):
        """Define the size method."""
        return self.linked_list.pop()

    def __len__(self):
        """Change the len() method."""
        return self.size()
