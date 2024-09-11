'''
19.Implement Floyd's Algorithm to find the shortest path between all pairs of cities. Display the distance matrix before and after applying the algorithm. Identify and print the shortest path


Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2] 
City 1 -> [City 0, City 2, City 3] 
City 2 -> [City 0, City 1, City 3] 
City 3 -> [City 1, City 2] 
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.

Test cases :
a)	You are given a small network of 4 cities connected by roads with the following distances:
    City 1 to City 2: 3
    City 1 to City 3: 8
    City 1 to City 4: -4
    City 2 to City 4: 1
    City 2 to City 3: 4
    City 3 to City 1: 2
    City 4 to City 3: -5
    City 4 to City 2: 6
Implement Floyd's Algorithm to find the shortest path between all pairs of cities.Display the distance matrix before and after applying the algorithm.Identify and print the shortest path from City 1 to City 3.
Input as above
Output : City 1 to City 3 = -9 

b.	Consider a network with 6 routers. The initial routing table is as follows:
    Router A to Router B: 1
    Router A to Router C: 5
    Router B to Router C: 2
    Router B to Router D: 1
    Router C to Router E: 3
    Router D to Router E: 1
    Router D to Router F: 6
    Router E to Router F: 2

Write a Program to implement Floyd's Algorithm to calculate the shortest paths between all pairs of routers. Simulate a change where the link between Router B and Router D fails. Update the distance matrix accordingly. Display the shortest path from Router A to Router F before and after the link failure.
Input as above
Output :Router A to Router F = 5


'''
import numpy as np

def floyd_warshall(n, edges):
    # Initialize distance matrix
    dist = np.full((n, n), float('inf'))
    for i in range(n):
        dist[i][i] = 0
    
    for u, v, w in edges:
        dist[u][v] = w
        dist[v][u] = w  # Assuming undirected graph

    print("Distance matrix before applying Floyd's Algorithm:")
    print(dist)

    # Floyd-Warshall Algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    print("Distance matrix after applying Floyd's Algorithm:")
    print(dist)

    return dist

def find_city_with_max_neighbors(n, dist, distance_threshold):
    max_neighbors = -1
    city_with_max_neighbors = -1

    for city in range(n):
        neighbors = sum(1 for d in dist[city] if d <= distance_threshold)
        if neighbors > max_neighbors or (neighbors == max_neighbors and city > city_with_max_neighbors):
            max_neighbors = neighbors
            city_with_max_neighbors = city

    return city_with_max_neighbors

# Input
n = 4
edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
distance_threshold = 4

# Execute
distance_matrix = floyd_warshall(n, edges)
result_city = find_city_with_max_neighbors(n, distance_matrix, distance_threshold)
print(f"The city with the maximum number of neighbors within the distance threshold is: City {result_city}")
