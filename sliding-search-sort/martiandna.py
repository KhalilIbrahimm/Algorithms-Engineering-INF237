
import sys

def read_input():
    n, a, r = map(int, sys.stdin.readline().split())
    dna = list(map(int, sys.stdin.readline().split()))
    requirements = [tuple(map(int, sys.stdin.readline().split())) for _ in range(r)]
    return n, a, r, dna, requirements

def find_shortest_valid_substring(n, a, r, dna, requirements):
    req_dict = {base: count for base, count in requirements}
    counter = [0] * a
    fulfilled = 0
    left = 0
    min_length = float('inf')

    for right in range(n):
        base = dna[right]
        counter[base] += 1

        if base in req_dict and counter[base] == req_dict[base]:
            fulfilled += 1

        while fulfilled == r:
            min_length = min(min_length, right - left + 1)
            left_base = dna[left]
            counter[left_base] -= 1
            if left_base in req_dict and counter[left_base] < req_dict[left_base]:
                fulfilled -= 1
            left += 1

    return min_length if min_length != float('inf') else "impossible"

def main():
    n, a, r, dna, requirements = read_input()
    print(find_shortest_valid_substring(n, a, r, dna, requirements))

if __name__ == "__main__":
    main()

