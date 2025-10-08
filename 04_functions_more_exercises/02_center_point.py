from math import floor


def cartesian_coordinate_system(first_points: list, second_points: list) -> list:
    length_one = (first_points[0] ** 2 + first_points[1] ** 2) ** 0.5
    length_two = (second_points[0] ** 2 + second_points[1] ** 2) ** 0.5
    if length_one <= length_two:
        return [floor(data) for data in first_points]
    return [floor(data) for data in second_points]


first_coordinate_points = [float(input()) for _ in range(2)]
second_coordinate_points = [float(input()) for _ in range(2)]


result = cartesian_coordinate_system(first_coordinate_points, second_coordinate_points)
print(f"({result[0]}, {result[1]})")
