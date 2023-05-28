def prim_minimum_spanning_tree(graph):
    minimum_spanning_tree = []
    visited = set()
    # Start with any vertex
    start_vertex = list(graph.keys())[0]
    visited.add(start_vertex)
    while len(visited) < len(graph):
        min_weight = float('inf')
        min_edge = None
        for vertex in visited:
            for neighbor, weight in graph[vertex]:
                if neighbor not in visited and weight < min_weight:
                    min_weight = weight
                    min_edge = (vertex, neighbor)
        minimum_spanning_tree.append(min_edge)
        visited.add(min_edge[1])
    return minimum_spanning_tree

graph = {
    'A': [('B', 10), ('C', 6)],
    'B': [('A', 10), ('C', 5), ('D', 15)],
    'C': [('A', 6), ('B', 5), ('D', 4)],
    'D': [('B', 15), ('C', 4)]
}
minimum_spanning_tree = prim_minimum_spanning_tree(graph)
print(minimum_spanning_tree)


////////////////////////







INF = 9999999
# number of vertices in graph
N = 5
#creating graph by adjacency matrix method
G = [[0, 19, 5, 0, 0],
     [19, 0, 5, 9, 2],
     [5, 5, 0, 1, 6],
     [0, 9, 1, 0, 1],
     [0, 2, 6, 1, 0]]

selected_node = [0, 0, 0, 0, 0]

no_edge = 0

selected_node[0] = True

# printing for edge and weight
print("Edge : Weight\n")
while (no_edge < N - 1):
    minimum = INF
    a = 0
    b = 0
    for m in range(N):
        # Check if the node is not selected and there is an edge (weight > 0)
        if selected_node[m]:
            for n in range(N):
                if not selected_node[n] and G[m][n]:  
                    # not in selected and there is an edge
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
    print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
    selected_node[b] = True
    no_edge += 1
