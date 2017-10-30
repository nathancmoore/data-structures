"""Define new Class for Node, Linked List, and Dequeue."""
"""Node and Linked List have been rebuilt for practice."""

class Node(object, val):
     """Define Node-class objects."""
    def __init__(self, data = None, next_node = None, prev_node = None):
        self.data = val
        self.next_node = next_node
        self.prev_node = next_node


class QLinkedList(object):
    def __init__(self):
        """Initiate a new instance of a QLinkedList object with attributes."""
        self.head = None
        self.tail = None

    def size(self):
        """Define the size method of the QLinkedList-class object."""
        return ""

    def push(self):
         """Define the push method for QLinkedList-class object."""
        return ""
    
    def append(self, val):
        """Adds a node to the tail with a specified value."""
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
    
    def appendleft(self, val):
        """Adds a node to the head with a specified value."""
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev_node = new_node
            self.head = new_node

    def remove(self):
        """Remove a node from the list."""
        return ""
    
    def pop(self):
        """Remove and returns the head node of the list."""
        return ""

    def shift(self):
        """Remove and return the tail node of the list."""
        return ""

    def display(self):
        """Display unicode string of linked list contents."""
        return ""

    def search(self):
        """Search the linked list for a node with a particular value."""
        return ""
