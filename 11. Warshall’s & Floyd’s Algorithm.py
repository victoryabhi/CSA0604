'''
11. Warshall’s & Floyd’s Algorithm
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.
Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.



Example 1: 
 
Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2] 
City 1 -> [City 0, City 2, City 3] 
City 2 -> [City 0, City 1, City 3] 
City 3 -> [City 1, City 2] 
Cities 0 and 3 have 2 neighboring cities at a distance Threshold = 4, but we have to return city 3 since it has the greatest number.
Example 2:

 

Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distance Threshold = 2
Output: 0
Explanation: The figure above describes the graph. 
The neighboring cities at a distance Threshold = 2 for each city are:
City 0 -> [City 1] 
City 1 -> [City 0, City 4] 
City 2 -> [City 3, City 4] 
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3] 
The city 0 has 1 neighboring city at a distanceThreshold = 2.
'''
import heapq
from collections import defaultdict

def findTheCity(n, edges, distanceThreshold):
    graph = defaultdict(list)
    
    # Build the graph
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    def dijkstra(start):
        min_heap = [(0, start)]
        distances = {i: float('inf') for i in range(n)}
        distances[start] = 0
        
        while min_heap:
            current_distance, current_node = heapq.heappop(min_heap)
            if current_distance > distances[current_node]:
                continue
            
            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))
        
        return sum(1 for d in distances.values() if d <= distanceThreshold)

    min_reachable = float('inf')
    city_with_max_index = -1
    
    for city in range(n):
        reachable_count = dijkstra(city)
        if (reachable_count < min_reachable) or (reachable_count == min_reachable and city > city_with_max_index):
            min_reachable = reachable_count
            city_with_max_index = city
            
    return city_with_max_index

n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4
print(findTheCity(n, edges, distanceThreshold))  
