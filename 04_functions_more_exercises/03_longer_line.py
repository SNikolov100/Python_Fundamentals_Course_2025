from math import floor


def calculate_line(first: list, second: list) -> float:
    """It calculate the length of line between two points(x,y) in the coordinate system"""
    leg_one = abs(first[0] - second[0]) if first[0] >= second[0] else abs(second[0] - first[0])
    leg_two = abs(first[1] - second[1]) if first[1] >= second[1] else abs(second[1] - first[1])
    hypotenuse = (leg_one ** 2 + leg_two ** 2) ** 0.5
    return hypotenuse


def cartesian_coordinate_system(first_points: list, second_points: list) -> list:
    """Tt calculate and compare two line in the coordinate system from points(x,y)"""
    length_one = (first_points[0] ** 2 + first_points[1] ** 2) ** 0.5
    length_two = (second_points[0] ** 2 + second_points[1] ** 2) ** 0.5
    if length_one <= length_two:
        return [floor(data) for data in first_points]
    return [floor(data) for data in second_points]


first_point = [float(input()) for _ in range(2)]
second_point = [float(input()) for _ in range(2)]
third_point = [float(input()) for _ in range(2)]
fourth_point = [float(input()) for _ in range(2)]

line_one = calculate_line(first_point,second_point)
line_two = calculate_line(third_point,fourth_point)

if line_one >= line_two:
    point_one_or_two = cartesian_coordinate_system(first_point, second_point)
    point_one = first_point if point_one_or_two == first_point else second_point
    point_two = second_point if point_one_or_two == first_point else first_point
else:
    point_one_or_two = cartesian_coordinate_system(third_point, fourth_point)
    point_one = third_point if point_one_or_two == third_point else fourth_point
    point_two = fourth_point if point_one_or_two == third_point else third_point

point_one = [int(floor(data)) for data in point_one]
point_two = [int(floor(data)) for data in point_two]
print(f"({point_one[0]}, {point_one[1]})({point_two[0]}, {point_two[1]})")
