import sys

# Read input from stdin
data = sys.stdin.read().strip().split('\n')
n, k = map(int, data[0].split())
d, s = map(int, data[1].split())

# Total average difficulty and solved difficulty
total_diff = d * n
solved_diff = s * k
unsolved_diff = total_diff - solved_diff

remaining = n - k

# Check if it's possible to reach the target average
if remaining <= 0 or unsolved_diff < 0:
    print('impossible')
else:
    avg_unsolved = unsolved_diff / remaining
    if 0 <= avg_unsolved <= 100:
        print(f'{avg_unsolved:.6f}')
    else:
        print('impossible')

