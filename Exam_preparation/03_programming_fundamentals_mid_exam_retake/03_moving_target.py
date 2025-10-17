def shoot_target(targets: list, current_index: int, power: int) -> list:
    targets[current_index] -= power
    if targets[current_index] <= 0:
        targets.pop(current_index)
    return targets


def add_target(targets: list, current_index: int, current_value: int) -> list:
    targets.insert(current_index, current_value)
    return targets


def strike_target(targets: list, current_index: int, radius: int) -> list:
    min_border = current_index - radius
    max_border = current_index + radius
    if min_border in range(len(targets)) and max_border in range(len(targets)):
        targets = targets[:min_border] + targets[max_border + 1:]
    else:
        print("Strike missed!")
    return targets


list_of_targets = list(map(int, input().split()))

while True:
    command = input().split()
    if command[0] == "End":
        break
    index = int(command[1])
    value = int(command[2])
    if index in range(len(list_of_targets)):
        if command[0] == "Shoot":
            list_of_targets = shoot_target(list_of_targets, index, value)
        elif command[0] == "Add":
            list_of_targets = add_target(list_of_targets, index, value)
        elif command[0] == "Strike":
            list_of_targets = strike_target(list_of_targets, index, value)
    elif command[0] == "Add":
        print("Invalid placement!")
list_of_targets = list(map(str, list_of_targets))
print("|".join(list_of_targets))
