def time_left_right_cars(time: list) -> list:
    current_time_left_car = 0
    current_time_right_car = 0
    length_of_time = len(time) // 2
    for index in range(length_of_time):
        if time[index] == "0":
            current_time_left_car *= 0.8
        else:
            current_time_left_car += int(time[index])
    for index in range(len(time) - 1, length_of_time, -1):
        if time[index] == "0":
            current_time_right_car *= 0.8
        else:
            current_time_right_car += int(time[index])
    return [current_time_left_car, current_time_right_car]


time_of_racers = input().split()

time_of_cars = time_left_right_cars(time_of_racers)
if time_of_cars[0] < time_of_cars[1]:
    print(f"The winner is left with total time: {time_of_cars[0]:.1f}")
elif time_of_cars[0] > time_of_cars[1]:
    print(f"The winner is right with total time: {time_of_cars[1]:.1f}")
