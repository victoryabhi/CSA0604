'''
22.You and your friends are tasked with coloring a map using a limited set of colors, with the following rules: At each step, you can choose any region of the map that hasn't been colored yet and color it with any available color. Your friend Alice will then color the next region using the same strategy, followed by your friend Bob. You aim to maximize the number of regions you color. Given a map represented as a list of regions and their adjacency relationships, write a function to determine the maximum number of regions you can color. Write a program to implement the Graph coloring technique for an undirected graph. Implement an algorithm with minimum number of colors.
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)] No. of vertices, n = 4, k = 3

'''
def is_safe(graph, vertex, color, c):
    for neighbor in graph[vertex]:
        if color[neighbor] == c:
            return False
    return True

def graph_coloring_util(graph, m, color, vertex):
    if vertex == len(graph):
        return True
    
    for c in range(1, m + 1):
        if is_safe(graph, vertex, color, c):
            color[vertex] = c
            if graph_coloring_util(graph, m, color, vertex + 1):
                return True
            color[vertex] = 0  # Backtrack
    return False

def graph_coloring(graph, m):
    color = [0] * len(graph)
    if graph_coloring_util(graph, m, color, 0):
        return color
    return None

# Example usage
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
n = 4  # Number of vertices
k = 3  # Number of colors
graph = [[] for _ in range(n)]

for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

result = graph_coloring(graph, k)
print("Coloring of the graph:", result)
