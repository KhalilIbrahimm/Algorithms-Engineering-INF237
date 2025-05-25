import sys
import math

# Read input: R = radius of pizza, C = crust width
R, C = map(float, sys.stdin.read().strip().split())

# Area of entire pizza
total_area = math.pi * R**2

# Area of cheese-only region
cheese_area = math.pi * (R - C)**2

# Percentage of area that has cheese
cheese_percentage = (cheese_area / total_area) * 100

print(f'{cheese_percentage:.6f}')

