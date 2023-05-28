import heapq

def dijkstra_minimum_spanning_tree(graph, source):
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0
    queue = [(0, source)]
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances

graph = {
    'A': [('B', 5), ('C', 2)],
    'B': [('A', 5), ('C', 1)],
    'C': [('A', 2), ('B', 1), ('D', 4)],
    'D': [('C', 4)]
}
source = 'A'
distances = dijkstra_minimum_spanning_tree(graph, source)
print(distances)





//////////////////////









from heapq import *
def dijkstra (graph,start,visited,distance):

    distance[start]=0
    bag=[]
    heappush(bag,(0,start))

    while bag:
        d,n = heappop(bag)  # Node with minimum distance will pop
        visited[n]=1 # become visited
        for cd,cn in graph[n]:   # check for all adjecent node of selected node
            # if  not visited and parent dist + new distance is less than current node's dist from source
            if not visited[cn] and distance[n] + cd < distance[cn]:
                # update new distance and parent dist + new dist
                distance[cn] = distance[n] + cd
                # push new distance and node in bag
                heappush(bag,(distance[cn],cn))
    print("Vertex : Shortest Distance" ,distance)

ipt =[[1,3,2],[1,2,1],[2,3,1],[2,5,1],[3,4,2],[5,4,3]]

n=5
graph ={}
distance={}
visited={}

for i in range (1,n+1):
    graph[i]=[]
    distance[i]=10**8+1
    visited[i]=0

for u,v,d in ipt:
    graph[u].append([d,v])
    graph[v].append([d,u])

start=1 # this is source
dijkstra(graph,start,visited,distance)