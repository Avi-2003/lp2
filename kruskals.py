class UnionFind:
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root1] = root2
                self.rank[root2] += 1


def kruskal_minimum_spanning_tree(graph):
    minimum_spanning_tree = []
    vertices = set()
    for edge in graph:
        vertices.add(edge[0])
        vertices.add(edge[1])
    union_find = UnionFind(vertices)
    graph.sort(key=lambda x: x[2])  # Sort edges by weights
    for edge in graph:
        vertex1, vertex2, weight = edge
        if union_find.find(vertex1) != union_find.find(vertex2):
            union_find.union(vertex1, vertex2)
            minimum_spanning_tree.append(edge)
    return minimum_spanning_tree

graph = [('A', 'B', 10), ('A', 'C', 6), ('B', 'C', 5), ('B', 'D', 15), ('C', 'D', 4)]
minimum_spanning_tree = kruskal_minimum_spanning_tree(graph)
print(minimum_spanning_tree)





///////////////////////////// second solution

V = 6
E = 10
dsuf = [-1] * V
mst= [] * (V-1)
edges = [[0,1,1],
     [1,3,1],
     [2,4,1],
     [0,2,2],
     [2,3,2],
     [3,4,2],
     [1,2,3],
     [1,4,3],
     [4,5,3],
     [3,5,4]]



#printing MST
def printmst():
    print("Minimum spanning tree formed is :\n")
    for edge in mst:
        print("From {0} --> To {1}  Weight ->{2}".format(edge[0], edge[1], edge[2]))
        

#finding the absolute parent 
def find(vertex):
    if dsuf[vertex] == -1:
        return vertex
    return find(dsuf[vertex])
    
#making union of two disjoint sets 
def union(fromP, toP):
    fromP = find(fromP)
    toP = find(toP)
    dsuf[fromP] = toP

#finds MST using Kruskal's algorithm
def kruskals(edges, V, E):
    edges.sort(key=lambda x: int(x[2]))
    i = 0
    j = 0
    while i<V-1 and j<E :
        fromP = find(edges[j][0])
        toP = find(edges[j][1])

        if fromP == toP:
            j = j + 1
            continue
        union(fromP, toP)
        mst.append(edges[j])
        i = i + 1

kruskals(edges, V, E)
printmst()