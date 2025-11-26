def take_odd(password: str) -> str:
    counter = 0
    new_password = ""
    for char in password:
        if counter % 2 != 0:
            new_password += char
        counter += 1
    print(new_password)
    return new_password


def cut(current_command: list, password: str) -> str:
    index, length = int(current_command[1]), int(current_command[2])
    new_password = password[0:index] + password[index+length:]
    print(new_password)
    return new_password


def substitute(current_command: list, password: str) -> str:
    substring, current_substitute = current_command[1], current_command[2]
    if substring not in password:
        print("Nothing to replace!")
        return password
    new_password = password.replace(substring, current_substitute)
    print(new_password)
    return new_password


old_password = input()

while True:
    command = input().split()
    action = command[0]
    if action == "Done":
        break
    elif action == "TakeOdd":
        old_password = take_odd(old_password)
    elif action == "Cut":
        old_password = cut(command, old_password)
    elif action == "Substitute":
        old_password = substitute(command, old_password)

print(f"Your password is: {old_password}")
