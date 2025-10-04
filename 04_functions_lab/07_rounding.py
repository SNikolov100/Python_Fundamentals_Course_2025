def rounding_list(number) -> list:
    return [round(float(data)) for data in number]


list_of_numbers = input().split()

result = rounding_list(list_of_numbers)
print(result)
