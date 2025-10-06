def is_palindrome(numbers: list) -> list:
    return [data[::-1] == data for data in numbers]


positive_numbers = input().split(", ")

result = is_palindrome(positive_numbers)
for data in result:
    print(data)