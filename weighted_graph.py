"""Class for Wieghted Graph"""

'''

definitions: 

   
    node -- no change to this

    neighbors -- an edge with a wieght
                return format -- neighbors = {'e' : 'w'}

     vertex -- a node with neighbors: 
            return format: {node: neighbors}


class Vertex(self):
    constructor(node, neighbors):
        self.node = node
        self.neigbors = neighbors

        self.vertex = {}

    def create_vertex(self, node, neighbors)
        return self.vertex[node] = neighbors

    def get_wieght(self, start_node, end_node):
        connections = self.vertex[start_node] -- the dictionary of neighbors

        return connections[end_node] -- the integer value associated with a neighbor key

class Graph(self):
    constructor(self, vertices)
        self.vertices = {} --> this is node_dict{}

        I think I might be overly complicating things because this means creating 
        a dicitonary of dictionaries of dictionaries --> I'm looking for ways to NOT
        reimplement our graph class.

        I would like your feedback.


'''