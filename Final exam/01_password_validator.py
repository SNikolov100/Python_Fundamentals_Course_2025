def make(current_command: list, current_password: str) -> str:
    upper_lower, index = current_command[1], int(current_command[2])
    if upper_lower == "Upper":
        replace_char = current_password[index].upper()
        current_password = current_password[:index] + replace_char + current_password[index+1:]
        print(current_password)
        return current_password
    elif upper_lower == "Lower":
        replace_char = current_password[index].lower()
        current_password = current_password[:index] + replace_char + current_password[index + 1:]
        print(current_password)
    return current_password


def insert(current_command: list, current_password: str) -> str:
    index, char = int(current_command[1]), current_command[2]
    if index not in range(len(current_password)):
        return current_password
    current_password = current_password[:index] + char + current_password[index:]
    print(current_password)
    return current_password


def replace(current_command: list, current_password: str) -> str:
    char, value = current_command[1], int(current_command[2])
    if char not in current_password:
        return current_password
    value += ord(char)
    new_char = chr(value)
    current_password = current_password.replace(char, new_char)
    print(current_password)
    return current_password


def validation(current_command: list, current_password: str) -> str:
    is_upper = False
    is_lower = False
    is_digit = False
    if len(current_password) < 8:
        print("Password must be at least 8 characters long!")
    if not current_password.isalnum():
        if "_" not in current_password:
            print("Password must consist only of letters, digits and _!")
    for char in current_password:
        if char.isupper():
            is_upper = True
    if not is_upper:
        print("Password must consist at least one uppercase letter!")
    for char in current_password:
        if char.islower():
            is_lower = True
    if not is_lower:
        print("Password must consist at least one lowercase letter!")
    for char in current_password:
        if char.isdigit():
            is_digit = True
    if not is_digit:
        print("Password must consist at least one digit!")
    return current_password


password = input()

while True:
    command = input().split()
    action = command[0]
    if action == "Complete":
        break
    elif action == "Make":
        password = make(command, password)
    elif action == "Insert":
        password = insert(command, password)
    elif action == "Replace":
        password = replace(command, password)
    elif action == "Validation":
        password = validation(command, password)



