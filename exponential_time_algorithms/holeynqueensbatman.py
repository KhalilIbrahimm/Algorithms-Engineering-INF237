
import sys

def read_input():
    test_cases = []
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        values = list(map(int, line.split()))
        if values == [0, 0]:
            break
        n, k = values
        holes = [[False] * n for _ in range(n)]
        for _ in range(k):
            r, c = map(int, sys.stdin.readline().split())
            holes[r][c] = True
        test_cases.append((n, holes))
    return test_cases

def count_queens(row, n, cols, pos_diag, neg_diag, holes):
    if row == n:
        return 1  # Valid placement found

    total = 0
    for col in range(n):
        d1 = row - col + (n - 1)
        d2 = row + col
        if cols[col] or pos_diag[d1] or neg_diag[d2] or holes[row][col]:
            continue
        # Place queen
        cols[col] = pos_diag[d1] = neg_diag[d2] = True
        total += count_queens(row + 1, n, cols, pos_diag, neg_diag, holes)
        # Backtrack
        cols[col] = pos_diag[d1] = neg_diag[d2] = False
    return total

def main():
    test_cases = read_input()
    for n, holes in test_cases:
        cols = [False] * n
        pos_diag = [False] * (2 * n - 1)
        neg_diag = [False] * (2 * n - 1)
        print(count_queens(0, n, cols, pos_diag, neg_diag, holes))

if __name__ == "__main__":
    main()
