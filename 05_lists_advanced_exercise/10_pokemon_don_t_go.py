sequence_of_integer = list(map(int, input().split()))
sum_remove_elements = 0
add_element = 0

while sequence_of_integer:
    entered_index = int(input())
    length = len(sequence_of_integer) - 1
    if entered_index < 0:
        remove_item = sequence_of_integer[0]
        sequence_of_integer[0] = sequence_of_integer[-1]

    elif entered_index >= len(sequence_of_integer):
        remove_item = sequence_of_integer[-1]
        sequence_of_integer[-1] = sequence_of_integer[0]

    else:
        remove_item = sequence_of_integer.pop(entered_index)

    sum_remove_elements += remove_item

    for inx in range(len(sequence_of_integer)):
        if sequence_of_integer[inx] <= remove_item:
            sequence_of_integer[inx] += remove_item
        else:
            sequence_of_integer[inx] -= remove_item

print(sum_remove_elements)


