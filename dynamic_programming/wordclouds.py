
import sys

def read_input():
    lines = sys.stdin.read().strip().split('\n')
    n, max_width = map(int, lines[0].split())
    words = [tuple(map(int, line.split())) for line in lines[1:]]
    return n, max_width, words

def minimal_cloud_height(n, max_width, words):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # Base case

    for end in range(1, n + 1):
        width_sum = 0
        max_height = 0

        for start in reversed(range(1, end + 1)):
            word_width, word_height = words[start - 1]
            width_sum += word_width
            if width_sum > max_width:
                break
            max_height = max(max_height, word_height)
            dp[end] = min(dp[end], dp[start - 1] + max_height)

    return dp[n]

def main():
    n, max_width, words = read_input()
    print(minimal_cloud_height(n, max_width, words))

if __name__ == "__main__":
    main()

