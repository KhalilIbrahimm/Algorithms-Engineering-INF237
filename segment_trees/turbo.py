import sys

def read_input():
    n = int(sys.stdin.readline())
    arr = [int(sys.stdin.readline()) for _ in range(n)]
    return n, arr

def build_segment_tree(n):
    size = 2 * n
    tree = [0] * size
    for i in range(n):
        tree[n + i] = 1
    for i in range(n - 1, 0, -1):
        tree[i] = tree[2 * i] + tree[2 * i + 1]
    return tree

def query(tree, n, l, r):
    l += n
    r += n
    res = 0
    while l < r:
        if l % 2:
            res += tree[l]
            l += 1
        if r % 2:
            r -= 1
            res += tree[r]
        l //= 2
        r //= 2
    return res

def update(tree, n, pos, val):
    pos += n
    tree[pos] = val
    while pos > 1:
        pos //= 2
        tree[pos] = tree[2 * pos] + tree[2 * pos + 1]

def solve_turbo_sort(n, arr):
    tree = build_segment_tree(n)
    pos = [0] * (n + 1)
    for i, val in enumerate(arr):
        pos[val] = i

    low, high = 1, n
    output = []
    for i in range(n):
        if i % 2 == 0:
            x = low
            low += 1
            swaps = query(tree, n, 0, pos[x])
        else:
            x = high
            high -= 1
            swaps = query(tree, n, pos[x] + 1, n)
        output.append(str(swaps))
        update(tree, n, pos[x], 0)
    return output

def main():
    n, arr = read_input()
    result = solve_turbo_sort(n, arr)
    print("\n".join(result))

if __name__ == "__main__":
    main()

