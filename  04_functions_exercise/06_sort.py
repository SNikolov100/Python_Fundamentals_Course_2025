def ascending_sort(numbers: list) -> list:
    return sorted(int(data) for data in numbers)


sequence_of_numbers = input().split()

result = ascending_sort(sequence_of_numbers)
print(result)
