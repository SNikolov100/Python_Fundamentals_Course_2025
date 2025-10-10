def merge(command_list: list, entered_single: list) -> list:
    start_index = max(0, int(command_list[1]))
    end_index = min(int(command_list[2]), len(entered_single) - 1)
    if start_index > end_index:
        return entered_single
    merge_data = "".join((entered_single[start_index:end_index + 1]))
    entered_single[start_index: end_index + 1] = [merge_data]
    return entered_single


def divide(command_list: list, entered_single: list) -> list:
    start_index = max(int(command_list[1]), 0)
    if int(command_list[2]) > len(entered_single[start_index]):
        return entered_single

    group_partition = len(entered_single[start_index]) // int(command_list[2])
    last_partition = len(entered_single[start_index]) % int(command_list[2])

    divide_data = entered_single[start_index]
    merge_list = entered_single[0:start_index]
    temp_merge = [divide_data[index: index + group_partition]
                  for index in range(0, len(divide_data), group_partition)]
    if last_partition != 0:
        temp_data = ["".join(temp_merge[-2:])]
        temp_merge[-2:] = temp_data
    merge_list.extend(temp_merge)
    merge_list.extend(entered_single[start_index + 1:])
    return merge_list


single_line = input().split()

while True:
    command = input().split()
    if command[0] == "3:1":
        break
    elif command[0] == "merge":
        single_line = merge(command, single_line)
    elif command[0] == "divide":
        single_line = divide(command, single_line)

print(*single_line)
