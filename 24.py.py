'''
24. You are given an undirected graph represented by a list of edges and the number of vertices n. Your task is to determine if there exists a Hamiltonian cycle in the graph. A Hamiltonian cycle is a cycle that visits each vertex exactly once and returns to the starting vertex. Write a function that takes the list of edges and the number of vertices as input and returns true if there exists a Hamiltonian cycle in the graph, otherwise return false.
Example:edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]  and n = 4

'''
def is_hamiltonian_cycle(edges, n):
    from collections import defaultdict

    # Create an adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def backtrack(path):
        if len(path) == n:
            return path[0] in graph[path[-1]]  # Check if last vertex connects to the first

        for neighbor in graph[path[-1]]:
            if neighbor not in path:
                path.append(neighbor)
                if backtrack(path):
                    return True
                path.pop()  # Backtrack

        return False

    for start in range(n):
        if backtrack([start]):
            return True

    return False

# Example usage
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
n = 4
print(is_hamiltonian_cycle(edges, n))  # Output: True
