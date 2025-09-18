enter_value = input()
value_list = list(enter_value)

result = [index for index, char in enumerate(value_list) if char.isupper()]

print(result)

