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

    def add_node(self, node_key):
        """Add new node to graph."""
        self.node_dict.setdefault(node_key, [])

    def add_edge(self, node_key1, node_key2):
        """Add edge between existing nodes."""
        self.node_dict[node_key1].append(node_key2)
        self.node_dict[node_key2].append(node_key1)

    def del_node(self, node_key):
        """Delete a node and all edges connected to it from the graph."""
        self.node_dict.pop(node_key)
        for key, value in self.node_dict.items():
            for i in value:
                if i == node_key:
                    value.remove(node_key)

    def has_node(self, node_key):
        """Return True if node is in node dictionary."""
        return node_key in self.node_dict

    def has_neighbors(self, node_key):
        """Return a list of all neighbors of a given node."""
        output = self.node_dict[node_key]

        for key, value in self.node_dict.items():
            if key != node_key:
                for i in value:
                    if i == node_key and i not in output and i != node_key:
                        output.append(i)

        return output
