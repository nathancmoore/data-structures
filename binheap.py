"""Define a BinHeap-class object and its nodes."""


class Node(object):
    """Define Node-class objects."""

    def __init__(self, idx, data=None):
        """Initiate a new instance of a Node object with attributes."""
        self.data = data
        self.idx = idx
        self.lchild_idx = 2 * self.idx + 1
        self.rchild_idx = 2 * self.idx + 2

        if idx % 2 == 1:
            self.parent_idx = (self.idx - 1) // 2
        else:
            self.parent_idx = (self.idx - 2) // 2


class BinHeap(object):
    """Define the class of a max-Binary Heap."""

    def __init__(self, head=None, starting_values=None):
        """Initiate a new instance of a Node object with attributes."""
        self.head = head

        if starting_values:
            self.node_list = []
            idx = 0
            for val in starting_values:
                self.node_list.append(Node(idx, val))
                idx += 1

        else:
            self.node_list = []

    def _swap_nodes(self, node1, node2):
        """Swap the position of two nodes in the heap."""
        temp_node1 = [node1.idx, node1.parent, node1.lchild, node1.rchild]
        temp_node2 = [node2.idx, node2.parent, node2.lchild, node2.rchild]
        node1.idx = temp_node2[0]
        node1.parent = temp_node2[1]
        node1.lchild = temp_node2[2]
        node1.rchild = temp_node2[3]
        node2.idx = temp_node1[0]
        node2.parent = temp_node1[1]
        node2.lchild = temp_node1[2]
        node2.rchild = temp_node1[3]

    def _maintain_heap(self):
        """Bubble sort the heap."""
        for node in self.node_list:
            if node.val < node.lchild.val:
                self._swap_nodes(node, node.lchild)

    def push(self, val):
        """Add a new node to the heap."""
        self.node_list.append(Node(len(self.node_list), val))

        self._maintain_heap()

    def pop(self):
        """Remove and return the top node in the heap."""
        temp_node1 = self.node_list[0]
        temp_node2 = self.node_list[-1]

        self.node_list[0] = temp_node2
        self.node_list[0].idx = 0
        self.node_list[-1] = temp_node1

        popped_node = self.node_list.pop()

        self._maintain_heap()

        return popped_node
