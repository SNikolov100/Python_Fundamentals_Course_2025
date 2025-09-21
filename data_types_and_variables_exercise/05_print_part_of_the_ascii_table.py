start_char = int(input())
last_char = int(input())

for index in range(start_char, last_char  + 1):
    if index == last_char:
        print(f"{chr(index)}")
    else:
        print(f"{chr(index)} ", end="")

