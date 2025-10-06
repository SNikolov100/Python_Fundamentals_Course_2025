def exchange_command(command: int, sequence: list) -> list:
    if 0 <= command < len(sequence):
        return sequence[command+1:] + sequence[:command+1]
    print("Invalid index")
    return sequence


def even_odd(command: list, all_list: list) -> list:
    if "even" in command:
        return [int(data_even) for data_even in all_list if int(data_even) % 2 == 0]
    return [int(data_odd) for data_odd in all_list if int(data_odd) % 2 != 0]


sequence_list = list(map(int, input().split()))
data_list = []
even_odd_list = []

while True:
    entered_command = input()
    if entered_command == "end":
        break
    entered_command_list = entered_command.split()
    for data in entered_command_list:
        if "exchange" in data:
            sequence_list = exchange_command(int(entered_command_list[1]), sequence_list)
        elif "max" in data:
            even_odd_list = even_odd(entered_command_list, sequence_list)
            if not even_odd_list:
                print("No matches")
            else:
                max_number = max(even_odd_list)
                last_index = len(sequence_list) - 1
                index_max_number = last_index - sequence_list[::-1].index(max_number)
                print(index_max_number)
        elif "min" in data:
            even_odd_list = even_odd(entered_command_list, sequence_list)
            if not even_odd_list:
                print("No matches")
            else:
                max_number = min(even_odd_list)
                last_index = len(sequence_list) - 1
                index_max_number = last_index - sequence_list[::-1].index(max_number)
                print(index_max_number)
        elif "first" in data:
            even_odd_list = even_odd(entered_command_list, sequence_list)
            if len(sequence_list) < int(entered_command_list[1]):
                print("Invalid count")
            else:
                stop_index = int(entered_command_list[1])
                if stop_index > len(even_odd_list):
                    print(even_odd_list)
                else:
                    result_first_odd_even = even_odd_list[:stop_index]
                    print(result_first_odd_even)
        elif "last" in data:
            result_odd_even = even_odd(entered_command_list, sequence_list)
            if len(sequence_list) < int(entered_command_list[1]):
                print("Invalid count")
            else:
                length = len(result_odd_even)
                start = length - int(entered_command_list[1])
                if start <= 0:
                    print(result_odd_even)
                else:
                    result_last_odd_even = result_odd_even[start:length]
                    print(result_last_odd_even)
print(sequence_list)



