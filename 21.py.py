'''
GRAPH COLOURING:
21.You and your friends are assigned the task of coloring a map with a limited number of colors. The map is represented as a list of regions and their adjacency relationships. The rules are as follows: At each step, you can choose any uncolored region and color it with any available color. Your friend Alice follows the same strategy immediately after you, and then your friend Bob follows suit. You want to maximize the number of regions you personally color. Write a function that takes the map's adjacency list representation and returns the maximum number of regions you can color before all regions are colored.Write a program to implement the Graph coloring technique for an undirected graph. Implement an algorithm with minimum number of colors.
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)] No. of vertices, n = 4


'''
def is_safe(graph, vertex, color, colors):
    for neighbor in graph[vertex]:
        if colors[neighbor] == color:
            return False
    return True

def graph_coloring_util(graph, m, colors, vertex):
    if vertex == len(graph):
        return True

    for color in range(1, m + 1):
        if is_safe(graph, vertex, color, colors):
            colors[vertex] = color
            if graph_coloring_util(graph, m, colors, vertex + 1):
                return True
            colors[vertex] = 0  # Backtrack

    return False

def graph_coloring(graph, m):
    colors = [0] * len(graph)
    if graph_coloring_util(graph, m, colors, 0):
        return colors
    return None

# Example usage
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
n = 4
graph = [[] for _ in range(n)]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

m = 3  # Number of colors
result = graph_coloring(graph, m)
print("Coloring of the graph:", result)
