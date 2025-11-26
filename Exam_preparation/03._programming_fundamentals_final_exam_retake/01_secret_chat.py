def insert_space(func_index: int, func_message: str) -> str:
    func_message = func_message[0:func_index] + " " + func_message[func_index:]
    return func_message


def reverse(string: str, message: str) -> str:
    if string not in message:
        print("error")
        return message
    message = message.replace(string, "", 1)
    string = string[::-1]
    message = message + string
    return message


def change_all(string: str, curr_replacement: str, message: str) -> str:
    message = message.replace(string, curr_replacement)
    return message


concealed_message = input()

while True:
    command = input().split(":|:")
    if command[0] == "Reveal":
        break
    action = command[0]
    if action == "InsertSpace":
        index = int(command[1])
        concealed_message = insert_space(index, concealed_message)
    elif action == "Reverse":
        substring = command[1]
        concealed_message = reverse(substring, concealed_message)
    elif action == "ChangeAll":
        substring, replacement = command[1], command[2]
        concealed_message = change_all(substring, replacement, concealed_message)
    print(concealed_message)

print(f"You have a new text message: {concealed_message}")