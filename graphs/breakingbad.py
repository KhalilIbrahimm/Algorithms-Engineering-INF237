import sys
from collections import defaultdict

def read_input():
    lines = sys.stdin.read().strip().split('\n')
    n, m = map(int, lines[0].split())
    edges = [tuple(map(int, line.split())) for line in lines[1:]]
    return n, m, edges

def build_graph(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u - 1].append(v - 1)
    return graph

def dfs(node, visited, graph):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, graph)

def is_strongly_connected(n, edges):
    graph = build_graph(n, edges)
    reverse_graph = build_graph(n, [(v, u) for u, v in edges])

    visited = [False] * n
    dfs(0, visited, graph)
    if not all(visited):
        return False

    visited = [False] * n
    dfs(0, visited, reverse_graph)
    return all(visited)

def try_reverse_one_edge(n, edges):
    for i, (u, v) in enumerate(edges):
        modified = edges[:i] + [(v, u)] + edges[i + 1:]
        if is_strongly_connected(n, modified):
            return u, v
    return None

def main():
    n, m, edges = read_input()

    if is_strongly_connected(n, edges):
        print("valid")
        return

    reversal = try_reverse_one_edge(n, edges)
    if reversal:
        print(f"{reversal[0]} {reversal[1]}")
    else:
        print("invalid")

if __name__ == "__main__":
    main()

