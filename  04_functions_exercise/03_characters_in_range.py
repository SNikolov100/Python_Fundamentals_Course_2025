def characters_in_range(first_str: str, second_str: str) -> list:
    for data in range(ord(first_str) + 1, ord(second_str)):
        char_list.append(chr(data))
    return char_list


first_string = input()
second_string = input()
char_list = []

result = characters_in_range(first_string, second_string)
print(*result)