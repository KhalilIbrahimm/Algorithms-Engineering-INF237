
import sys
import math

def read_input():
    """
    Reads input for multiple scenarios.
    Each scenario consists of:
    - The number of mosquitoes
    - The bowl's diameter
    - A list of mosquito coordinates
    """
    num_cases = int(sys.stdin.readline().strip())
    scenarios = []

    for _ in range(num_cases):
        sys.stdin.readline()  # Skip empty line
        num_mosquitoes, diameter = sys.stdin.readline().split()
        num_mosquitoes = int(num_mosquitoes)
        diameter = float(diameter)

        mosquito_positions = [
            tuple(map(float, sys.stdin.readline().split()))
            for _ in range(num_mosquitoes)
        ]

        scenarios.append((num_mosquitoes, diameter, mosquito_positions))

    return scenarios


def max_mosquitoes_caught(scenarios):
    """
    For each scenario, finds the maximum number of mosquitoes
    that can fit inside a bowl of the given diameter.
    """
    results = []

    for num_mosquitoes, diameter, mosquitoes in scenarios:
        radius = diameter / 2.0
        radius_squared = radius ** 2
        max_caught = 0

        # First strategy: Use each mosquito as the center
        for i in range(num_mosquitoes):
            center_x, center_y = mosquitoes[i]
            caught = sum(
                math.isclose((x - center_x) ** 2 + (y - center_y) ** 2, radius_squared, rel_tol=1e-7) or
                (x - center_x) ** 2 + (y - center_y) ** 2 < radius_squared
                for x, y in mosquitoes
            )
            max_caught = max(max_caught, caught)

        # Second strategy: Use the midpoint between pairs of mosquitoes
        for i in range(num_mosquitoes):
            for j in range(i + 1, num_mosquitoes):
                x1, y1 = mosquitoes[i]
                x2, y2 = mosquitoes[j]
                dist_squared = (x2 - x1) ** 2 + (y2 - y1) ** 2

                if dist_squared > diameter ** 2 + 1e-9:
                    continue  # Too far apart to fit in the bowl

                mid_x = (x1 + x2) / 2.0
                mid_y = (y1 + y2) / 2.0
                dist = math.sqrt(dist_squared)

                # Compute possible alternative centers (rotated vector offset)
                if dist > 0:
                    offset = math.sqrt(radius_squared - (dist / 2) ** 2)
                    norm_x = (y2 - y1) / dist
                    norm_y = (x1 - x2) / dist

                    centers = [
                        (mid_x + offset * norm_x, mid_y + offset * norm_y),
                        (mid_x - offset * norm_x, mid_y - offset * norm_y)
                    ]
                else:
                    centers = [(mid_x, mid_y)]

                for cx, cy in centers:
                    caught = sum(
                        math.isclose((x - cx) ** 2 + (y - cy) ** 2, radius_squared, rel_tol=1e-7) or
                        (x - cx) ** 2 + (y - cy) ** 2 < radius_squared
                        for x, y in mosquitoes
                    )
                    max_caught = max(max_caught, caught)

        results.append(max_caught)

    return results


if __name__ == "__main__":
    scenarios = read_input()
    results = max_mosquitoes_caught(scenarios)

    for result in results:
        print(result)

