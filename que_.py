"""Define Queue Class."""

from doubly_linked_list import DLinkedList
from doubly_linked_list import Node

class Queue(object):
    """Queue Class which is composed from Linked List."""

    def __init__(self):
        """Constructor for Queue."""
        self.linked_list = DLinkedList()

    def enqueue(self, val):

        new_node = Node(self, val)

        if self.linked_list.head == None:
            self.linked_list.head = new_node
            self.linked_list.tail = new_node
        else:
            self.linked_list.tail.prev_node == new_node
            new_node.next_node = self.linked_list.tail
            self.linked_list.tail == new_node


    def dequeue():

    def peek():

    def size():

