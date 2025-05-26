
import sys
from collections import defaultdict, deque

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
    return n, edges

def build_graph(n, edges, reversed_edge=None):
    graph = defaultdict(list)
    for u, v in edges:
        if reversed_edge == (u, v):
            graph[v].append(u)
        else:
            graph[u].append(v)
    return graph

def is_strongly_connected(n, graph):
    def bfs(start, graph_ref):
        visited = [False] * (n + 1)
        queue = deque([start])
        visited[start] = True
        while queue:
            node = queue.popleft()
            for neighbor in graph_ref[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return all(visited[1:])

    if not bfs(1, graph):
        return False

    # Build reversed graph
    reverse_graph = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            reverse_graph[v].append(u)

    return bfs(1, reverse_graph)

def main():
    n, edges = read_input()
    for u, v in edges:
        graph = build_graph(n, edges, reversed_edge=(u, v))
        if is_strongly_connected(n, graph):
            return
if __name__ == "__main__":
    main()

