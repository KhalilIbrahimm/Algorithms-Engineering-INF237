
import sys
import heapq

def read_input():
    datasets = []
    num_datasets = int(sys.stdin.readline())
    for _ in range(num_datasets):
        n, m, b, _ = map(int, sys.stdin.readline().split())
        installed = list(map(int, sys.stdin.readline().split()))
        edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
        datasets.append((n, b, installed, edges))
    return datasets

def build_graph(n, edges):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, cost in edges:
        graph[u].append((cost, v))
        graph[v].append((cost, u))
    return graph

def compute_energy(n, b, installed, edges):
    graph = build_graph(n, edges)
    visited = set(installed)
    heap = []

    for node in installed:
        for cost, neighbor in graph[node]:
            heapq.heappush(heap, (cost, neighbor))

    total_activation = 0
    transfers = 0

    while len(visited) < n and heap:
        cost, node = heapq.heappop(heap)
        if node not in visited:
            visited.add(node)
            total_activation += cost
            transfers += 1
            for edge_cost, neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (edge_cost, neighbor))

    return total_activation + (transfers * b)

def main():
    datasets = read_input()
    for n, b, installed, edges in datasets:
        print(compute_energy(n, b, installed, edges))

if __name__ == "__main__":
    main()

