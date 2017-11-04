"""Define Queue Class."""


from doubly_linked_list import DLinkedList


class Queue(DLinkedList):
    """Queue Class which is composed from Linked List."""

    def __init__(self):
        """Constructor for Queue."""
        self.q = DLinkedList()

    def __len__(self):
        """Return size of the queue."""
        return self.q.size()

    def enqueue(self, val):
        """Add new element to end of the queue."""
        self.q.append(val)

    def dequeue(self):
        """Remove from the end of the queue."""
        self.q.shift()

    def peek(self):
        """Return value of next element in queue."""
        return self.q.head.data
