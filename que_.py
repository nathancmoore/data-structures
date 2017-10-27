"""Define Queue Class."""

from doubly_linked_list import DLinkedList
from doubly_linked_list import Node


class Queue(object):
    """Queue Class which is composed from Linked List."""

    def __init__(self):
        """Constructor for Queue."""
        self.linked_list = DLinkedList()

    def enqueue(self, val):
        """Add new element to end of the queue."""
        new_node = Node(self, val)

        if self.linked_list.head is None:
            self.linked_list.head = new_node
            self.linked_list.tail = new_node
        else:
            self.linked_list.tail.prev_node == new_node
            new_node.next_node = self.linked_list.tail
            self.linked_list.tail == new_node

    def dequeue(self):
        """Remove from the end of the queue."""
        if self.linked_list.head is not None:
            removed_node = self.linked_list.head
            self.linked_list.head.prev_node = self.linked_list.head
            return removed_node.data
        raise IndexError("List is empty")

    def peek(self):
        """Return value of next element in queue."""
        return self.linked_list.head

    def size(self):
        """Define the size method."""
        return self.linked_list.size()
        