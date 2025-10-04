def sum_numbers(first_n, second_n) -> int:
    return first_n + second_n


def subtract(result_from_sum_numbers, third_n) -> int:
    return result_from_sum_numbers - third_n

first_number = int(input())
second_number = int(input())
third_number = int(input())

result = sum_numbers(first_number, second_number)
result = subtract(result, third_number)
print(result)
