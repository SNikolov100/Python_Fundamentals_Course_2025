sequence_of_time = list(map(int, input().split()))

time_right_car = 0
time_left_car = 0

middle = len(sequence_of_time) // 2
left_car = sequence_of_time[:middle]
right_car = sequence_of_time[middle + 1:]
right_car.reverse()

for time in left_car:
    if time == 0:
        time_left_car -= time_left_car * 0.2
    else:
        time_left_car += time

for time in right_car:
    if time == 0:
        time_right_car -= time_right_car * 0.2
    else:
        time_right_car += time

if time_left_car < time_right_car :
    print(f"The winner is left with total time: {time_left_car:.1f}")
elif time_left_car > time_right_car:
    print(f"The winner is right with total time: {time_right_car:.1f}")


