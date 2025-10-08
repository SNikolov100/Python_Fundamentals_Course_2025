# sequence_of_numbers = [int(data) for data in input().split(", ")]
#
# index_even_numbers = [index for index in range(len(sequence_of_numbers)) if sequence_of_numbers[index] % 2 == 0]
# print(index_even_numbers)


# sequence_of_numbers = list(map(int, input().split(", ")))
#
# index_even_numbers = map(lambda x: x if sequence_of_numbers[x] % 2 == 0 else "no", range(len(sequence_of_numbers)))
# temp = list(filter(lambda x: x != "no", index_even_numbers))
# print(temp)

sequence_of_numbers = list(map(int, input().split(", ")))

temp = list(filter(lambda i: sequence_of_numbers[i] % 2 == 0, range(len(sequence_of_numbers))))
print(temp)