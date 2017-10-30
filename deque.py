"""Define new Class for Node, Linked List, and Dequeue."""
"""Node and Linked List have been rebuilt for practice."""

class Node(object, val):
     """Define Node-class objects."""

    def __init__(self, data = None, next_node = None, prev_node = None):
        """."""
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
        count = 0
        current_node = self.head
        while current_node:
            count+=1
            current_node = current_node.next

        return count

    
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
    
    def pop(self):
        """Remove and returns the tail node of the list."""
        try:
            popped_node = self.tail
            self.tail.prev_node.next_node = None
            self.tail = self.tail.prev_node
            return popped_node

        except:
            raise(IndexError)

    def popleft(self):
    """Remove and returns the head node of the list."""
        try:
            popped_node = self.head
            self.head.next_node.prev_node = None
            self.head = self.head.next_node
            return popped_node

        except:
            raise(IndexError)

    def peek(self):
        """Return value from end of list without removing it"""
        if self.head == None:
            return None
        else:
            return self.tail

    def peekleft(self):
        """Return value from front of list without removing it"""
        if self.head == None:
            return None
        else:
            return self.head
