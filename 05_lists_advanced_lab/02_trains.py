wagons = [0] * int(input())
add_command = []

while True:
    add_command = input().split()
    if "End" in add_command:
        break
    elif "add" in add_command:
        wagons[-1] += int(add_command[1])
    elif "insert" in add_command:
        wagons[int(add_command[1])] += int(add_command[2])
    elif "leave":
        wagons[int(add_command[1])] -= int(add_command[2])

print(wagons)






