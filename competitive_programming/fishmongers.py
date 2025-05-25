import sys

# Read all input lines
data = sys.stdin.read().strip().split('\n')
n_fish, n_mongers = map(int, data[0].split())
fish_weights = list(map(int, data[1].split()))

# Read each fishmonger's offer (fish they can buy and price/kg)
fishmongers = []
for i in range(2, 2 + n_mongers):
    quantity, price = map(int, data[i].split())
    fishmongers.append((quantity, price))

# Sort fish and mongers by best profit potential
fish_weights.sort(reverse=True)
fishmongers.sort(key=lambda x: x[1], reverse=True)

profit = 0
fish_index = 0

# Sell fish to highest-paying buyers first
for count, price in fishmongers:
    for _ in range(min(count, len(fish_weights) - fish_index)):
        profit += fish_weights[fish_index] * price
        fish_index += 1

print(profit)

