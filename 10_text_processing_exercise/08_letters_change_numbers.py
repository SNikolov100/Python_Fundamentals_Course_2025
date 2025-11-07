input_strings = input().split()
total_sum = 0

for data in input_strings:
    first_char, number, last_char = data[0], data[1:len(data) - 1], data[len(data)-1]
    if first_char.isupper():
        total_sum += int(number) / (ord(first_char) - 64)
    elif first_char.islower():
        total_sum += int(number) * (ord(first_char) - 96)
    if last_char.isupper():
        total_sum -= (ord(last_char) - 64)
    if last_char.islower():
        total_sum += (ord(last_char) - 96)

print(f"{total_sum:.2f}")
