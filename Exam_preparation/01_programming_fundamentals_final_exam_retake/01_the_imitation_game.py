def move_action(encrypt_message: str, current_message: list) -> str:
    number_of_letters = int(current_message[1])
    if number_of_letters > len(encrypt_message):
        return encrypt_message
    return encrypt_message[number_of_letters: len(encrypt_message)] + encrypt_message[0:number_of_letters]


def insert_action(encrypt_message: str, current_index: int, current_value: str) -> str:
    if current_index >= len(encrypt_message):
        return encrypt_message + current_value
    return encrypt_message[0:current_index] + current_value + encrypt_message[current_index:len(encrypt_message)]


def change_all_action(current_message: str, current_substring: str, current_replacement: str) ->str:
    new_message = ""
    for char in current_message:
        if char == current_substring:
            new_message += current_replacement
        else:
            new_message += char
    return new_message


encrypted_message = input()

while True:
    command = input()
    if command == "Decode":
        break
    message = command.split("|")
    action = message[0]
    if action == "Move":
        encrypted_message = move_action(encrypted_message, message)
    elif action == "Insert":
        index, value = int(message[1]), message[2]
        encrypted_message = insert_action(encrypted_message, index, value)
    elif action == "ChangeAll":
        substring, replacement = message[1], message[2]
        encrypted_message = change_all_action(encrypted_message, substring, replacement)

print(f"The decrypted message is: {encrypted_message}")
