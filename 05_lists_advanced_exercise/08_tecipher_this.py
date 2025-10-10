secret_message = input().split()
result_message = []

for data in secret_message:
    first_char = "".join([number for number in data if number.isdigit()])
    last_char = [char for char in data if not char.isdigit()]
    last_char[0], last_char[-1] = last_char[-1], last_char[0]
    first_char = chr(int(first_char))
    result_message += ["".join([first_char] + [*last_char])]

print(*result_message)