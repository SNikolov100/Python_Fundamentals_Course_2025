def max_number(numbers: list) -> int:
    return max(map(int, numbers))


def min_number(numbers: list) -> int:
    return min(map(int, numbers))


def sum_number(numbers: list) -> int:
    return sum(int(data) for data in numbers)


sequence_of_numbers = input().split()

result_max = max_number(sequence_of_numbers)
result_min = min_number(sequence_of_numbers)
result_sum = sum_number(sequence_of_numbers)

print(f"The minimum number is {result_min}")
print(f"The maximum number is {result_max}")
print(f"The sum number is: {result_sum}")