def positive_numbers(numbers: list) -> list:
    return [data for data in numbers if data >= 0]


def negative_numbers(numbers: list) -> list:
    return [data for data in numbers if data < 0]


def even_numbers(numbers: list) -> list:
    return [data for data in numbers if data % 2 == 0]


def odd_numbers(numbers: list) -> list:
    return [data for data in numbers if data % 2 != 0]


list_of_numbers = [int(number) for number in input().split(", ")]

result_positive_numbers = positive_numbers(list_of_numbers)
result_negative_numbers = negative_numbers(list_of_numbers)
result_even_numbers = even_numbers(list_of_numbers)
result_odd_numbers = odd_numbers(list_of_numbers)

print(f"Positive: {', '.join(str(data) for data in result_positive_numbers)}")
print(f"Negative: {', '.join(str(data) for data in result_negative_numbers)}")
print(f"Even: {', '.join(str(data) for data in result_even_numbers)}")
print(f"Odd: {', '.join(str(data) for data in result_odd_numbers)}")
