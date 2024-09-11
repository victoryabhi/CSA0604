'''
38:Given a graph represented by an edge list, implement Dijkstra's Algorithm to find the shortest path from a given source vertex to a target vertex.The graph is represented as a list of edges where each edge is a tuple (u, v, w) representing an edge from vertex u to vertex v with weight w.
Test Case 1:
Input:
n = 6
edges = [(0, 1, 7), (0, 2, 9), (0, 5, 14),(1, 2, 10), (1, 3, 15),
(2, 3, 11), (2, 5, 2),(3, 4, 6),(4, 5, 9)]
source = 0
target = 4
Output:20
Test Case 2:
Input:
n = 5
edges = [(0, 1, 10), (0, 4, 3),(1, 2, 2), (1, 4, 4),(2, 3, 9),(3, 2, 7),(4, 1, 1), (4, 2, 8), (4, 3, 2)]
source = 0
target = 3
Output:8


'''
import heapq

def dijkstra(n, edges, source, target):
    graph = {i: [] for i in range(n)}
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))  # Assuming undirected graph

    min_heap = [(0, source)]  # (distance, vertex)
    distances = {i: float('inf') for i in range(n)}
    distances[source] = 0

    while min_heap:
        current_distance, current_vertex = heapq.heappop(min_heap)

        if current_vertex == target:
            return current_distance

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return distances[target]

# Test Case
n = 6
edges = [(0, 1, 7), (0, 2, 9), (0, 5, 14), (1, 2, 10), (1, 3, 15),
         (2, 3, 11), (2, 5, 2), (3, 4, 6), (4, 5, 9)]
source = 0
target = 4
output = dijkstra(n, edges, source, target)
print(output)  # Output: 20
