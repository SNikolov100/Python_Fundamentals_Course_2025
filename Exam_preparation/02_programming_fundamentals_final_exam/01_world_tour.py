def add_stop(current_command: list, current_travel: str) ->str:
    index, string = int(current_command[1]), current_command[2]
    if index not in range(len(current_travel)):
        return current_travel
    current_travel = current_travel[0:index] + string + current_travel[index:len(current_travel)]
    return current_travel


def remove_stop(current_command:list, current_travel: str) -> str:
    start_index, end_index = int(current_command[1]), int(current_command[2])
    if (start_index in range(len(current_travel))) and (end_index in range(len(current_travel))):
        return current_travel[0:start_index] + current_travel[end_index + 1:len(current_travel)]
    return current_travel


def switch(current_command: list, current_travel: str) -> str:
    old_string, new_string = current_command[1], current_command[2]
    if old_string in current_travel:
        current_travel = current_travel.replace(old_string, new_string)
        return current_travel
    return current_travel


travel = input()

while True:
    command = input().split(":")
    if command[0] == "Travel":
        break
    action = command[0]
    if action == "Add Stop":
        travel = add_stop(command, travel)
    elif action == "Remove Stop":
        travel = remove_stop(command, travel)
    elif action == "Switch":
        travel = switch(command, travel)
    print(travel)

print(f"Ready for world tour! Planned stops: {travel}")



