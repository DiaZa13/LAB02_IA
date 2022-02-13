
Node = int
Weight = int
Vertices = list[list[[Node, Weight]]]

def readGraph(file):
   with open(file, 'r') as graph:
       node_count = int(graph.readline())
       edges_count = int(graph.readline())
       edges: Vertices = [[] for _ in range(node_count)]
       for edge in graph:
           x = edge.split()
           edges[int(x[0])-1].append((int(x[1])-1, int(x[2])))
   return node_count, edges_count, edges

print(readGraph('grafo.txt'))

