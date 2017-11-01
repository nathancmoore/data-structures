"""This is the class for a priority queue."""
from binheap import BinHeap

class Node(object):
    """Define Node-class objects."""

    def __init__(self, index=None, value=None, priority=0):
        """Assign attributes to the Node object."""
        self.index = index
        self.value = [value, priority]
        self.left = 2 * self.index + 1
        self.right = 2 * self.index + 2

class PriorityQ(object):
    """Implementation of a Priority Queue using an existing binary heap."""

    def __init__(self, val=None, priority=None):
        self.val = val
        self.binheap = BinHeap()
        def self.binheap._sort(self):
        """Bubble sort the heap."""
        for i in range(len(self.heap_list)):
            node = self.heap_list[i]
            try:
                if node.value[1] < self.heap_list[node.left][1]:
                    self._swap(node, self.heap_list[node.left])
                    i = 0
            except(IndexError):
                break

            try:
                if node.value[1] < self.heap_list[node.right][1]:
                    self._swap(node, self.heap_list[node.right])
                    i = 0
            except(IndexError):
                break

    def insert(self, value, priority=0):
        """."""

        self.binheap.push()

        return ""

    def pop(self):
        """."""
        return ""

    def peek(self):
        """."""
        return



priority []
#pass priority to bin heap

priorityq = binheap index of [val]