def smallest_number(first_n, second_n, third_n) -> int:
    return min(first_n, second_n, third_n)


first_number = int(input())
second_number = int(input())
third_number = int(input())

result = smallest_number(first_number, second_number, third_number)
print(result)