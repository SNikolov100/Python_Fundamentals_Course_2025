def absolute_number(sequence_list: list) -> list:
    return [abs(float(data)) for data in sequence_list]


sequence_of_numbers = input().split()
print(absolute_number(sequence_of_numbers))
