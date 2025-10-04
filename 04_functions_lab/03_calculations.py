def arithmetic_operation(operator, number_1, number_2) -> float:
    if operator == "multiply":
        return number_1 * number_2
    elif operator == "divide":
        if number_2 != 0:
            return number_1 / number_2
    elif operator == "add":
        return number_1 + number_2
    elif operator == "subtract":
        return number_1 - number_2


operator_as_a_string = input()
first_number = int(input())
second_number = int(input())

result = arithmetic_operation(operator_as_a_string, first_number, second_number)
if float(result).is_integer():
    print(int(result))
else:
    print(result)
