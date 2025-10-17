def swap_elements(list_of_integer: list, index_one: int, index_two: int) -> list:
    list_of_integer[index_one], list_of_integer[index_two] = list_of_integer[index_two], list_of_integer[index_one]
    return list_of_integer


def multiply_elements(list_of_integer: list, index_one: int, index_two: int) -> list:
    list_of_integer[index_one] = list_of_integer[index_two]*list_of_integer[index_one]
    return list_of_integer


def decrease_elements(list_of_integer: list) -> list:
    for index in range(len(list_of_integer)):
        list_of_integer[index] -= 1
    return list_of_integer


sequence_of_integer = list(map(int, input().split()))
command = [0]
while command[0] != "end":
    command = input()
    command = command.split()
    if command[0] == "swap":
        sequence_of_integer = swap_elements(sequence_of_integer, int(command[1]), int(command[2]))
    elif command[0] == "multiply":
        sequence_of_integer = multiply_elements(sequence_of_integer, int(command[1]), int(command[2]))
    elif command[0] == "decrease":
        sequence_of_integer = decrease_elements(sequence_of_integer)
sequence_of_integer = list(map(str, sequence_of_integer))
print(", ".join(sequence_of_integer))
