def factorial_division(first: int, second: int) -> float:
    first_number_factorial = first
    second_number_factorial = second
    for data in range(1, first):
        first_number_factorial *= data
    for data in range(1, second):
        second_number_factorial *= data
    return first_number_factorial / second_number_factorial


first_number = int(input())
second_number = int(input())

result = factorial_division(first_number, second_number)
print(f"{result:.2f}")