import numpy as np

adjacency_matrix = np.array([
    [0,1,1,1],
    [1,0,1,0],
    [1,1,0,1],
    [1,0,1,0]
])




def graph_coloring(graph, colors):
    num_vertices = len(graph)
    color = [-1] * num_vertices
    
    def graph_coloring_util(v):
        if v == num_vertices:
            return True
        
        for c in range(colors):
            if is_safe(v, graph, color, c):
                color[v] = c
                if graph_coloring_util(v+1):
                    return True
                color[v] = -1
                
        return False
    
    if not graph_coloring_util(0):
        return "No Solution exists"
    
    return color




def is_safe(v, graph, color, c):
    for i in range(len(graph)):
        if graph[v][i] and color[i] == c:
            return False
    return True



num_colors = 3
solution = graph_coloring(adjacency_matrix, num_colors)

if isinstance(solution, str):
    print(solution)
else:
    print("Graph coloring solution:", solution)







