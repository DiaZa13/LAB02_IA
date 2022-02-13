from typing import Optional

Node = int
Weight = int
Vertices = list[list[[Node, Weight]]]
NODE_COUNT = 6


test_vertices: Vertices = [[] for _ in range(NODE_COUNT)]

#     Origen   Destino, Peso
test_vertices[0].append((2, 12))
test_vertices[0].append((3, 60))
test_vertices[1].append((0, 10))
test_vertices[2].append((1, 20))
test_vertices[2].append((3, 32))
test_vertices[4].append((0, 7))


def shortest_path(vertices: Vertices, origin: Node, destination: Node) -> [list[Node], Weight]:
    last_node: list[Optional[Node]] = [None for _ in range(NODE_COUNT)]
    weights = [float('inf') for _ in range(NODE_COUNT)]
    unexplored_nodes: list[Node] = [i for i in range(NODE_COUNT)]

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


print(shortest_path(test_vertices, 3, 4))
