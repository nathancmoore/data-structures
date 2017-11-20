def dijkstra(graph, start, end, visited=[], weights={}, routes={}):
        """Function utilizing Dijkstra's algorithm.
        Find the shortest path from a starting node to and end node.
        """
        if start == end:
            path_str = ''
            pred = end
            while pred is not None:
                shortest_path.append(pred)
                path_str += pred
                pred = routes.get(pred, None)
            return shortest_path[::-1]
        else:
            if not visited:
                weights[start] = 0
            for edge in graph.nodes[start]:
                if edge not in visited:
                    new_distance = weights[start] + graph.nodes[start][edge]
                    if new_distance < weights.get(edge, float('inf')):
                        weights[edge] = new_distance
                        routes[edge] = start
            visited.append(start)
            unvisited = {}
            for node in graph.nodes:
                if node not in visited:
                    unvisited[node] = weights.get(node, float('inf'))
            new_start = min(unvisited, key=unvisited.get)
            dijkstra(graph, new_start, end, visited, weights, routes)

    dijkstra(graph, start, end)
    return shortest_path[::-1]