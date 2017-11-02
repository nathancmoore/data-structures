"""Class for Graph Implementation."""


class Graph(object):
    """Class for graph and all methods."""

    def __init__(self):
        """Constructor for Graph class."""
        self.node_dict = {}

    def _form_edge_string(self, node1, node2):
        """Return formatted edges of graph."""
        return "{} --> {}".format(node1.val, node2.val)

    def nodes(self):
        """Return all nodes in graph."""
        return self.node_dict.keys()

    def add_node(self, val):
        """Add new node to graph."""
        self.node_dict.setdefault(val, [])

    def add_edge(self, val1, val2):
        """Add edge between existing nodes."""
        self.node_dict[val1].append(val2)
        self.node_dict[val2].append(val1)
