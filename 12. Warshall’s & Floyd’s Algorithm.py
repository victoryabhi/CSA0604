'''
12. Warshall’s & Floyd’s Algorithm
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
Example 1:

 
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
 

'''
import heapq
from collections import defaultdict

def networkDelayTime(times, n, k):
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    
    min_heap = [(0, k)]  # (time, node)
    time_to_receive = {i: float('inf') for i in range(1, n + 1)}
    time_to_receive[k] = 0
    
    while min_heap:
        current_time, node = heapq.heappop(min_heap)
        
        if current_time > time_to_receive[node]:
            continue
        
        for neighbor, travel_time in graph[node]:
            new_time = current_time + travel_time
            if new_time < time_to_receive[neighbor]:
                time_to_receive[neighbor] = new_time
                heapq.heappush(min_heap, (new_time, neighbor))
    
    max_time = max(time_to_receive.values())
    return max_time if max_time < float('inf') else -1

times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
print(networkDelayTime(times, n, k))  
