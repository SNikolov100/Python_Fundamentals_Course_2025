def shoot_target(targets: list, comm: int, count: int):

    if comm in range(len(targets)):
        target = int(targets[comm])
        for index in range(len(targets)):
            if index not in memory_shoot:
                if index == comm:
                    targets[index] = -1
                elif targets[index] > target:
                    targets[index] -= target
                else:
                    targets[index] += target
        count += 1
        memory_shoot.append(comm)
    return targets, count


list_of_targets = list(map(int, input().split()))
memory_shoot = []
count_win = 0

while True:
    command = input()
    if command == "End":
        break
    command = int(command)
    list_of_targets, count_win = shoot_target(list_of_targets, command, count_win)
list_of_targets = map(str, list_of_targets)
print(f"Shot targets: {count_win} -> {' '.join(list_of_targets)}")
