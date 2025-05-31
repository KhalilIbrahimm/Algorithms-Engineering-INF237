
import sys

def read_input():
    """
    Reads triangle corners and apple tree coordinates from input.
    """
    x_a, y_a = map(int, sys.stdin.readline().split())
    x_b, y_b = map(int, sys.stdin.readline().split())
    x_c, y_c = map(int, sys.stdin.readline().split())

    num_trees = int(sys.stdin.readline())
    trees = [tuple(map(int, sys.stdin.readline().split())) for _ in range(num_trees)]

    return (x_a, y_a), (x_b, y_b), (x_c, y_c), trees


def triangle_area(x1, y1, x2, y2, x3, y3):
    """
    Calculates the area of a triangle using the determinant method.
    """
    return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0


def is_point_inside_triangle(triangle, point):
    """
    Determines whether the given point lies inside or on the edge of the triangle.
    """
    (x_a, y_a), (x_b, y_b), (x_c, y_c) = triangle
    x, y = point

    total_area = triangle_area(x_a, y_a, x_b, y_b, x_c, y_c)
    area1 = triangle_area(x, y, x_b, y_b, x_c, y_c)
    area2 = triangle_area(x_a, y_a, x, y, x_c, y_c)
    area3 = triangle_area(x_a, y_a, x_b, y_b, x, y)

    return abs(total_area - (area1 + area2 + area3)) < 1e-7


def main():
    point_a, point_b, point_c, trees = read_input()

    area = triangle_area(*point_a, *point_b, *point_c)
    trees_inside = sum(1 for tree in trees if is_point_inside_triangle([point_a, point_b, point_c], tree))

    print(f"{area:.1f}")
    print(trees_inside)


if __name__ == "__main__":
    main()

