def tribonacci_suquence(coefficient: int) -> list:
    """Tribonacci sequence, every number is formed by the sum of the previous 3."""
    sequence_list = []
    for number in range(1, coefficient + 1):
        if number <= 2:
            next_number = 1
        elif number == 3:
            next_number = sequence_list[number - 2] + sequence_list[number - 3]
        else:
            next_number = sequence_list[number - 2] + sequence_list[number - 3] + sequence_list[number - 4]
        sequence_list.append(next_number)
    return sequence_list


coefficient_of_tribonacci = int(input())

result = tribonacci_suquence(coefficient_of_tribonacci)
print(*result)
# result = map(str, result)
# print(" ".join(result))