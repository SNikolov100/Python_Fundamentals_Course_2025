sequence_of_words = input().lower().split()
odd_even_dictionary = {}
my_dictionary = {}

for data in sequence_of_words:
    if data not in my_dictionary:
        my_dictionary[data] = 0
    my_dictionary[data] += 1

result = []
for data in my_dictionary:
    if my_dictionary[data] % 2 != 0:
        result.append(data)
print(f"{' '.join(result)}")




