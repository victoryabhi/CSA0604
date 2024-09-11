'''
GREED TECHNIQUES 
37. Single Source Shortest Paths: Dijkstra's Algorithm
Q1:Given a graph represented by an adjacency matrix, implement Dijkstra's Algorithm to find the shortest path from a given source vertex to all other vertices in the graph.The graph is represented as an adjacency matrix where graph[i][j] denote the weight of the edge from vertex i to vertex j. If there is no edge between vertices i and j, the value is Infinity (or a very large number).
Test Case 1:
Input:
n = 5
graph = [[0, 10, 3, Infinity, Infinity],[Infinity, 0, 1, 2, Infinity],[Infinity, 4, 0, 8, 2],
    [Infinity, Infinity, Infinity, 0, 7],[Infinity, Infinity, Infinity, 9, 0]]
source = 0
Output:[0, 7, 3, 9, 5]
Test Case 2:
Input:
n = 4
graph = [[0, 5, Infinity, 10],[Infinity, 0, 3, Infinity],[Infinity, Infinity, 0, 1],
    [Infinity, Infinity, Infinity, 0]]
source = 0
Output:[0, 5, 8, 9]

'''
import sys

def dijkstra(graph, source):
    n = len(graph)
    distances = [sys.maxsize] * n
    distances[source] = 0
    visited = [False] * n

    for _ in range(n):
        min_distance = sys.maxsize
        min_index = -1
        
        for v in range(n):
            if not visited[v] and distances[v] < min_distance:
                min_distance = distances[v]
                min_index = v
        
        visited[min_index] = True
        
        for v in range(n):
            if (graph[min_index][v] != sys.maxsize and 
                not visited[v] and 
                distances[min_index] + graph[min_index][v] < distances[v]):
                distances[v] = distances[min_index] + graph[min_index][v]

    return distances

# Test Case
n = 5
graph = [[0, 10, 3, sys.maxsize, sys.maxsize],
         [sys.maxsize, 0, 1, 2, sys.maxsize],
         [sys.maxsize, 4, 0, 8, 2],
         [sys.maxsize, sys.maxsize, sys.maxsize, 0, 7],
         [sys.maxsize, sys.maxsize, sys.maxsize, 9, 0]]
source = 0

output = dijkstra(graph, source)
print(output)  # Output: [0, 7, 3, 9, 5]
