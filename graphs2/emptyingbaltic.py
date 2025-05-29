
import sys
import heapq

def read_input():
    h, w = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    sr, sc = map(int, sys.stdin.readline().split())
    return h, w, grid, sr - 1, sc - 1

def compute_drained_water(h, w, grid, sr, sc):
    if grid[sr][sc] >= 0:
        return 0

    drainage = [[0] * w for _ in range(h)]
    drainage[sr][sc] = grid[sr][sc]

    heap = [(grid[sr][sc], sr, sc)]
    directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]

    while heap:
        level, r, c = heapq.heappop(heap)
        if level != drainage[r][c]:
            continue
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] < 0:
                new_level = max(level, grid[nr][nc])
                if new_level < drainage[nr][nc]:
                    drainage[nr][nc] = new_level
                    heapq.heappush(heap, (new_level, nr, nc))

    total = 0
    for r in range(h):
        for c in range(w):
            if grid[r][c] < 0 and drainage[r][c] < 0:
                total += -drainage[r][c]
    return total

def main():
    h, w, grid, sr, sc = read_input()
    print(compute_drained_water(h, w, grid, sr, sc))

if __name__ == "__main__":
    main()

