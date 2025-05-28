
import sys

def read_input():
    n_and_costs = list(map(int, sys.stdin.read().strip().split()))
    n = n_and_costs[0]
    costs = n_and_costs[1:]
    return n, costs

def min_total_cost(n, costs):
    INF = float('inf')
    memo = {}

    def dp(position, jump):
        if position == n:
            return 0
        if (position, jump) in memo:
            return memo[(position, jump)]

        cost_options = []

        # Forward jump (increase jump length)
        next_pos = position + jump + 1
        if next_pos <= n:
            cost_options.append(costs[next_pos - 1] + dp(next_pos, jump + 1))

        # Backward jump (keep jump length)
        prev_pos = position - jump
        if prev_pos >= 1:
            cost_options.append(costs[prev_pos - 1] + dp(prev_pos, jump))

        memo[(position, jump)] = min(cost_options) if cost_options else INF
        return memo[(position, jump)]

    # Start at tile 1 and jump to tile 2 (first move)
    return costs[1] + dp(2, 1)

def main():
    n, costs = read_input()
    print(min_total_cost(n, costs))

if __name__ == "__main__":
    main()

