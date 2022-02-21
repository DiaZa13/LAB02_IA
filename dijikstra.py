from typing import Optional
from util import Node, Weight, Vertices

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


if __name__ == '__main__':
    from sys import argv
    from util import read_graph

    if len(argv) != 4:
        print("Se debe ingresar el archivo con los datos del grafo, el nodo de origen y el nodo destino.")
        print("ie. py dijiskstra.py .\\data\\grafo.txt 1 2")

    node_count, edges_count, vertices = read_graph(argv[1])
    origin = int(argv[2])
    destination = int(argv[3])
    path = shortest_path(node_count, vertices, origin, destination)
    print(path)
