def twin_elements_remove(elements: list, index: list):
    index_one = index[0]
    index_two = index[1]
    if elements[index_one] == elements[index_two]:
        remove_element = elements[index_one]
        elements.remove(remove_element)
        elements.remove(remove_element)
        print(f"Congrats! You have found matching elements - {remove_element}!")
    else:
        print("Try again!")
    return elements


sequence_of_elements = input().split()
number_of_moves = 0
is_game_over = False

while True:
    number_of_moves += 1
    command = input()
    if command == "end":
        is_game_over = True
        break
    command_indexes = list(map(int, command.split()))
    if command_indexes[0] in range(len(sequence_of_elements))\
            and command_indexes[1] in range(len(sequence_of_elements))\
            and command_indexes[0] != command_indexes[1]:
        sequence_of_elements = twin_elements_remove(sequence_of_elements, command_indexes)
        if not sequence_of_elements:
            print(f"You have won in {number_of_moves} turns!")
            break
    else:
        middle_index = (len(sequence_of_elements) // 2)
        for _ in range(2):
            sequence_of_elements.insert(middle_index, f"-{number_of_moves}a")
        print("Invalid input! Adding additional elements to the board")


if is_game_over:
    print(f"Sorry you lose :(")
    print(*sequence_of_elements)



