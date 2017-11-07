"""Class for Graph Implementation."""


class Graph(object):
    """Class for graph and all methods."""

    def __init__(self, dict_=None):
        """Constructor for Graph class."""
        self.node_dict = {}

        self.visited = []

        if dict_:
            self.node_dict = dict_

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
        if node_key1 not in self.node_dict.keys():
            self.add_node(node_key1)

        if node_key2 not in self.node_dict.keys():
            self.add_node(node_key2)

        self.node_dict[node_key1].append(node_key2)

    def del_node(self, node_key):
        """Delete a node and all edges connected to it from the graph."""
        self.node_dict.pop(node_key)
        for key, value in self.node_dict.items():
            for i in value:
                if i == node_key:
                    self.del_edge(i, node_key)

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

    def has_adjacent(self, node_key1, node_key2):
        """Confirm or disconfirm that two nodes are neighbors."""
        return node_key1 in self.node_dict[node_key2] or node_key2 in self.node_dict[node_key1]

    def del_edge(self, node_key, node_key2):
        """Delete an edge between two given nodes."""
        self.node_dict[node_key].remove(node_key2)

    def depth_first_traversal(self, start_val):
        """Recursive Depth First Search Implementation."""

        self.visited.append(start_val)
       # print("START VAL", start_val)
        if len(self.node_dict[start_val]) > 0:
            for child in self.node_dict[start_val]:
                   
                if child not in self.visited:
                    self.depth_first_traversal(child)
        #print(self.visited)
        return self.visited


        '''
        self._traverse(start_val)

      
        def _traverse(self, node_val):
            """."""
            visited.append(node_val)
            if self.has_neighbors(node_val):
                for child in self.node_dict[node_val]:
                    if child not in visited:
                        self._traverse(self.node_dict[child])

        return visited
        '''

if __name__ == '__main__':
    
    graph1 = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
    }

    g = Graph(graph1)
    
    t = g.depth_first_traversal('A')
    print(t)


