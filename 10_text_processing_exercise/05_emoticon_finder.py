single_string = input()

for index in range(len(single_string)):
    if single_string[index] == ":":
        if index + 1 > len(single_string):
            break
        print(f":{single_string[index + 1]}")