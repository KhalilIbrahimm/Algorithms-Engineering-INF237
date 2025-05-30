
import sys

def read_input():
    t = int(sys.stdin.readline())
    cases = []
    for _ in range(t):
        m, r = map(int, sys.stdin.readline().split())
        requests = list(map(int, sys.stdin.readline().split()))
        cases.append((m, r, requests))
    return cases

def build_tree(size):
    n = 1
    while n < size:
        n <<= 1
    tree = [0] * (2 * n)
    return tree, n

def update(tree, n, idx, val):
    idx += n - 1
    tree[idx] = val
    while idx > 1:
        idx //= 2
        tree[idx] = tree[2 * idx] + tree[2 * idx + 1]

def query(tree, n, l, r):
    l += n - 1
    r += n - 1
    res = 0
    while l <= r:
        if l % 2 == 1:
            res += tree[l]
            l += 1
        if r % 2 == 0:
            res += tree[r]
            r -= 1
        l //= 2
        r //= 2
    return res

def solve_movie_cases(cases):
    results = []
    for m, r, reqs in cases:
        size = m + r + 1
        tree, base = build_tree(size)
        pos = [0] * (m + 1)
        for i in range(1, m + 1):
            idx = m - i + 1
            pos[i] = idx
            update(tree, base, idx, 1)

        top = m
        res = []
        for f in reqs:
            idx = pos[f]
            res.append(str(query(tree, base, idx + 1, top)))
            update(tree, base, idx, 0)
            top += 1
            pos[f] = top
            update(tree, base, top, 1)
        results.append(" ".join(res))
    return results

def main():
    cases = read_input()
    results = solve_movie_cases(cases)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()

