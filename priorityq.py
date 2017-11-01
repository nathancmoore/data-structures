"""This is the class for a priority queue."""
from binheap import BinHeap


class Node(object):
    """Define Node-class objects."""

    def __init__(self, index=None, value_list=None):
        """Assign attributes to the Node object."""
        self.index = index
        self.value = value_list
        self.left = 2 * self.index + 1
        self.right = 2 * self.index + 2


class PriorityQ(BinHeap):
    """Implementation of a Priority Queue using an existing binary heap."""

    def __init__(self, iterable=None):
        """Assign the attributes of the PriorityQ Class object."""
        self.heap_list = []

        if iterable:
            self.heap_list = iterable

    def _sort(self):
        """Bubble sort the heap."""
        for i in range(len(self.heap_list)):
            node = self.heap_list[i]
            try:
                print(node.value)
                if node.value[1] < self.heap_list[node.left].value[1]:
                    self._swap(node, self.heap_list[node.left])
                    i = 0
            except(IndexError):
                break

            try:
                if node.value[1] < self.heap_list[node.right].value[1]:
                    self._swap(node, self.heap_list[node.right])
                    i = 0
            except(IndexError):
                break

    def insert(self, value_list):
        """Insert new node based on priority."""
        self.push(value_list)
        self._sort()

    def pop(self):
        """Return and remove highest priority Node."""
        self._swap(self.heap_list[0], self.heap_list[-1])
        popped = self.heap_list.pop().value[0]
        self._sort()
        return popped

    def peek(self):
        """Return highest priority Node without removal."""
        return self.heap_list[0].value[0]
