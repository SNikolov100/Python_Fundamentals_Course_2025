def sum_of_all_even(number: list) -> int:
    return sum([int(data) for data in number if int(data) % 2 == 0])


def sum_of_all_odd(number: list) -> int:
    return sum([int(data) for data in number if int(data) % 2 != 0])


entered_number = input()
entered_number_list = [data for data in entered_number]

result_even = sum_of_all_even(entered_number_list)
result_odd = sum_of_all_odd(entered_number_list)

print(f"Odd sum = {result_odd}, Even sum = {result_even}")
