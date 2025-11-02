sequence_of_characters = input()

count_char_dictionary = {}
for index in range(len(sequence_of_characters)):
    if sequence_of_characters[index] == " ":
        continue
    if sequence_of_characters[index] not in count_char_dictionary:
        count_char_dictionary[sequence_of_characters[index]] = 0
    count_char_dictionary[sequence_of_characters[index]] += 1

for char, occurrences in count_char_dictionary.items():
    print(f"{char} -> {occurrences}")

