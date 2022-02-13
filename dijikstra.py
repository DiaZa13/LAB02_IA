from typing import Optional
from utilsia import Node, Weight, Vertices

def shortest_path(node_count: Node, vertices: Vertices, origin: Node, destination: Node) -> [list[Node], Weight]:
    last_node: list[Optional[Node]] = [None for _ in range(node_count)]
    weights = [float('inf') for _ in range(node_count)]
    unexplored_nodes: list[Node] = [i for i in range(node_count)]

    last_node[origin] = origin
    weights[origin] = 0

    while len(unexplored_nodes) != 0:
        current_node = min(unexplored_nodes, key=lambda node: weights[node])
        unexplored_nodes.remove(current_node)

        if weights[current_node] == float('inf'):
            continue

        for neighbour, weight in vertices[current_node]:
            total_weight = weight + weights[current_node]

            if weights[neighbour] > total_weight:
                weights[neighbour] = total_weight
                last_node[neighbour] = current_node

    current_node = destination
    path = [destination]
    while current_node != origin:
        current_node = last_node[current_node]
        path.append(current_node)
    path.reverse()

    return path, weights[destination]

