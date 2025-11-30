def contains(current_command: list, key: str) -> str:
    substring = current_command[1]
    if substring in key:
        return f"{key} contains {substring}"
    return f"Substring not found!"


def flip(current_command: list, key: str) -> str:
    upper_lower, start_index, end_index = current_command[1], int(current_command[2]), int(current_command[3])
    if upper_lower == "Upper":
        return key[0:start_index] + key[start_index:end_index].upper() + key[end_index:]
    return key[0:start_index] + key[start_index:end_index].lower() + key[end_index:]


def slice_def(current_command: list, key: str) -> str:
    start_index, end_index = int(current_command[1]), int(current_command[2])
    return key[0:start_index] + key[end_index:]


activation_key = input()

while True:
    command = input().split(">>>")
    action = command[0]
    if action == "Generate":
        break
    elif action == "Contains":
        print(contains(command, activation_key))
    elif action == "Flip":
        activation_key = flip(command,activation_key)
        print(activation_key)
    elif action == "Slice":
        activation_key = slice_def(command, activation_key)
        print(activation_key)

print(f"Your activation key is: {activation_key}")