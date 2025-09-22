key = int(input())
number_strings = int(input())
enter_char_int = 0
for _ in range(1, (number_strings + 1)):
    enter_char = input()
    enter_char_int = int(ord(enter_char)) + key
    enter_char = chr(enter_char_int)
    print(enter_char, end="")
