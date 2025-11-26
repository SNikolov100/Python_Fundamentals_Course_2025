def letters(current_info: str, current_username: str) -> str:
    if current_info == "Lower":
        return current_username.lower()
    return current_username.upper()


def reverse(current_start_index: int, current_end_index: int, current_username: str) -> str:
    if (current_start_index < current_end_index) and (current_start_index in range(len(current_username)))\
            and (current_end_index in range(len(current_username) - 1)):
        temp_string = current_username[current_start_index: end_index + 1]
        print(temp_string[::-1])
    return current_username


def substring_def(current_substring: str, current_username: str) -> str:
    if current_substring in current_username:
        current_username = current_username.replace(current_substring, "")
        print(current_username)
    else:
        print(f"The username {current_username} doesn't contain {current_substring}.")
    return current_username


username = input()

while True:
    command = input().split()
    if command[0] == "Registration":
        break
    action = command[0]
    if action == "Letters":
        info = command[1]
        username = letters(info, username)
        print(username)
    elif action == "Reverse":
        start_index = int(command[1])
        end_index = int(command[2])
        username = reverse(start_index, end_index, username)
    elif action == "Substring":
        substring = command[1]
        username = substring_def(substring, username)
    elif action == "Replace":
        sub_char = command[1]
        length = len(sub_char)
        username = username.replace(sub_char, "-"*length)
        print(username)
    elif action == "IsValid":
        given_char = command[1]
        if given_char in username:
            print("Valid username.")
        else:
            print(f"{given_char} must be contained in your username.")

