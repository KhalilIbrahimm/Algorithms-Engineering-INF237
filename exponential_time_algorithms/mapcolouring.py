
import sys

def read_input():
    T = int(sys.stdin.readline())
    test_cases = []
    for _ in range(T):
        n, m = map(int, sys.stdin.readline().split())
        edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
        test_cases.append((n, edges))
    return test_cases

def build_graph(n, edges):
    graph = {i: set() for i in range(n)}
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    return graph

def can_color(node, color, coloring, graph):
    # Check if this color causes conflict with neighbors
    for neighbor in graph[node]:
        if neighbor in coloring and coloring[neighbor] == color:
            return False
    return True

def backtrack(node, graph, coloring, max_colors):
    if node == len(graph):
        return True  # All nodes colored
    for color in range(1, max_colors + 1):
        if can_color(node, color, coloring, graph):
            coloring[node] = color
            if backtrack(node + 1, graph, coloring, max_colors):
                return True
            del coloring[node]
    return False

def solve_coloring(n, edges):
    if n == 1:
        return 1  # Single country needs only one color
    graph = build_graph(n, edges)
    for c in range(1, 5):  # Try 1 to 4 colors
        if backtrack(0, graph, {}, c):
            return c
    return "many"

# Process test cases
cases = read_input()
for n, edges in cases:
    print(solve_coloring(n, edges))

