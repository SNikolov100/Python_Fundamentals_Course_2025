def sum_pack(numbers: list) -> list:
    for data in numbers:
        sum_list.append(sum(int(data_x) for data_x in data))
    return sum_list


def pass_message(message: str, numbers: list) -> str:
    result = ""
    length = len(message)
    for data in numbers:
        if length <= data:
            index = data - length
            result += message[index]
            message = message[0:index] + message[index+1:]
        else:
            result += message[data]
            message = message[0:data] + message[data + 1:]
    return result


entered_numbers = input().split()
entered_message = input()
sum_list = []

sum_of_numbers = sum_pack(entered_numbers)
keys_of_message = pass_message(entered_message, sum_of_numbers)
print(keys_of_message)



