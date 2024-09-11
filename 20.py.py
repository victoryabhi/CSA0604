'''
20.Implement Floyd's Algorithm to find the shortest path between all pairs of cities. Display the distance matrix before and after applying the algorithm. Identify and print the shortest path

Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
Output: 0
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -> [City 1] 
City 1 -> [City 0, City 4] 
City 2 -> [City 3, City 4] 
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3] 
The city 0 has 1 neighboring city at a distanceThreshold = 2.

a)	Test cases :
B to A 2
A TO C 3
C TO D 1
D TO A 6 
C TO B 7 
Find shortest path from C to A 
Output = 7 
b)	Find shortest path from E to C
c)	C TO A 2
A TO B 4
B TO C 1
B TO E 6
E TO A 1
A TO D 5
D TO E 2
E TO D 4
D TO C 1
C TO D 3
Output : E to C = 5


'''
import numpy as np

def floyd_warshall(n, edges):
    # Initialize distance matrix
    dist = np.full((n, n), float('inf'))
    for i in range(n):
        dist[i][i] = 0
    
    # Fill the distance matrix with edge weights
    for u, v, w in edges:
        dist[u][v] = w
        dist[v][u] = w  # Assuming undirected graph

    print("Distance matrix before applying Floyd's Algorithm:")
    print(dist)

    # Floyd's Algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    print("Distance matrix after applying Floyd's Algorithm:")
    print(dist)

    # Identify and print the shortest path for distance threshold
    neighboring_cities = {}
    for i in range(n):
        neighboring_cities[i] = [j for j in range(n) if dist[i][j] <= 2 and i != j]

    for city, neighbors in neighboring_cities.items():
        print(f"City {city} -> {neighbors}")

# Example usage
n = 5
edges = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]
floyd_warshall(n, edges)
