"""Define new Class for Node, Linked List, and Dequeue."""
"""Node and Linked List have been rebuilt for practice."""


class Node(object):
    """Define Node-class objects."""

    def __init__(self, data=None, next_node=None, prev_node=None):
        """Initiate a new instance of a Node object with attributes."""
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class Deque(object):
    """Define Deque-class objects."""

    def __init__(self):
        """Initiate a new instance of a Deque object with attributes."""
        self.head = None
        self.tail = None

    def size(self):
        """Define the size method of the Deque-class object."""
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next_node

        return count

    def append(self, val):
        """Add a node to the tail with a specified value."""
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node

    def appendleft(self, val):
        """Add a node to the head with a specified value."""
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev_node = new_node
            new_node.next_node = self.head
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
        """Return value from end of list without removing it."""
        if self.head is None:
            return None
        else:
            return self.tail

    def peekleft(self):
        """Return value from front of list without removing it."""
        if self.head is None:
            return None
        else:
            return self.head
