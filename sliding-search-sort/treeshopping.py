
import heapq
import sys

def read_input():
    n, k = map(int, sys.stdin.readline().split())
    heights = list(map(int, sys.stdin.readline().split()))
    return n, k, heights

def find_minimum_height_diff(n, k, heights):
    min_heap, max_heap = [], []
    min_diff = float('inf')

    for i in range(n):
        heapq.heappush(min_heap, (heights[i], i))
        heapq.heappush(max_heap, (-heights[i], i))

        if i >= k - 1:
            while min_heap[0][1] < i - k + 1:
                heapq.heappop(min_heap)
            while max_heap[0][1] < i - k + 1:
                heapq.heappop(max_heap)

            current_min = min_heap[0][0]
            current_max = -max_heap[0][0]
            min_diff = min(min_diff, current_max - current_min)

    return min_diff

def main():
    n, k, heights = read_input()
    print(find_minimum_height_diff(n, k, heights))

if __name__ == "__main__":
    main()

