def take_even_number(number: list) -> list:
    return list(number[index_even] for index_even in range(len(number)) if index_even % 2 == 0)


def take_odd_number(number: list) -> list:
    return list(number[index_odd] for index_odd in range(len(number)) if index_odd % 2 != 0)


def non_number_list_pop(number_list: list, index_pop: int):
    taken_data.extend(number_list[:index_pop])
    del number_list[:index_pop]
    return taken_data, number_list


hidden_message = input()
numbers_list = [int(data) for data in hidden_message if data.isdigit()]
non_number_list = [data for data in hidden_message if not data.isdigit()]
taken_string = []
taken_data = []

take_list = take_even_number(numbers_list)
skip_list = take_odd_number(numbers_list)

for index in range(len(take_list)):
    take_index = int(take_list[index])
    skip_index = int(skip_list[index])
    taken_string, non_number_list = non_number_list_pop(non_number_list, take_index)
    del non_number_list[:skip_index]
print("".join(taken_string))
