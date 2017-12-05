"""Define Queue Class."""

from doubly_linked_list import Node


class Queue(object):
    """Queue Class which is composed from Linked List."""

    def __init__(self):
        """Constructor for Queue."""
        self.head = None
        self.tail = None
        self.size_ = 0

    def __len__(self):
        """Return size of the queue."""
        return self.size_

    def enqueue(self, val):
        """Add new element to end of the queue."""
        new_node = Node(val)

        if self.size_ == 0:
            self.head = new_node
            self.tail = new_node

        if self.size_ == 1:
            self.head.prev_node = new_node
            new_node.next_node = self.head
            self.tail = new_node
        else:
            new_node.next_node = self.tail
            self.tail.prev_node = new_node
            self.tail = new_node

        self.size_ += 1

    def dequeue(self):
        """Remove from the front of the queue and return it's data."""
        if self.head:
            if self.size_ == 0:
                raise IndexError("List is empty")

            node_to_remove = self.head

            if self.size_ == 1:
                self.size_ -= 1
                self.head = None
                self.tail = None
                return node_to_remove.data

            self.size_ -= 1
            self.head.prev_node.next_node = None
            self.head = self.head.prev_node
            return node_to_remove.data

    def peek(self):
        """Return value of next element in queue."""
        if self.head:
            return self.head.data

    def size(self):
        """Define the size method."""
        return self.size_
