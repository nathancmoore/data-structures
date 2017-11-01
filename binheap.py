"""Define a BinHeap-class object and its nodes."""


class Node(object):
    """Define Node-class objects."""
    def __init__(self, index=None, value=None):
        self.index = index
        self.value = value
        self.left = 2 * self.index + 1
        self.right = 2 * self.index + 2

        '''
        if index % 2 == 1:
            self.parent = (self.index - 1) // 2
        else:
            self.parent = (self.index - 2) // 2
        '''

class BinHeap(object):
    """Define the class of a max-Binary Heap."""

    def __init__(self, iterable=None):
         """Initiate a new instance of a Binheap object with attributes."""
        self.heap_list = []

        if isinstance(iterable, list)):
            self.heap_list = iterable

    def push(self, val):
        """Add new node to Heap."""
        self.heap_list.append(Node(len(self.heap_list), val))
        self._sort()

    def swap(parent, child):
        """Change indices of two nodes."""
        tmp = parent.index
        parent.index = child.index
        child.index = tmp
        self.heap_list[parent.index] = parent
        self.heap_list[child.index] = child
        self._sort()

    def pop():
        """Return root node of Heap."""
        swap(self.heap_list[0], self.heap_list[-1]) #swap root with bottom most child
        popped = self.heap_list.pop().value
        self._sort()
        return popped

    def _sort():
        """Bubble sort on heap."""
        for i in range(len(self.heap_list)):
            node = self.heap_list[i]
            if node.value < self.heap_list[node.left]:
                swap(node, self.heap_list[node.left])
                i = 0
            if node.value < self.heap_list[node.right]:
                swap(node, self.heap_list[node.right])
                i = 0